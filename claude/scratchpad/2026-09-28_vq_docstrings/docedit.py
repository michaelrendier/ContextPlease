"""AST-guided docstring editor.  dump: signatures+docs; apply: JSON -> rewrite docstrings only."""
import ast, json, sys, textwrap, re

def _sig(n):
    a = n.args
    parts = []
    pos = a.posonlyargs + a.args
    defs = [None] * (len(pos) - len(a.defaults)) + list(a.defaults)
    for x, d in zip(pos, defs):
        s = x.arg + (': ' + ast.unparse(x.annotation) if x.annotation else '')
        if d is not None: s += ' = ' + ast.unparse(d)
        parts.append(s)
    if a.vararg: parts.append('*' + a.vararg.arg)
    elif a.kwonlyargs: parts.append('*')
    for x, d in zip(a.kwonlyargs, a.kw_defaults):
        s = x.arg + (': ' + ast.unparse(x.annotation) if x.annotation else '')
        if d is not None: s += ' = ' + ast.unparse(d)
        parts.append(s)
    if a.kwarg: parts.append('**' + a.kwarg.arg)
    r = ' -> ' + ast.unparse(n.returns) if n.returns else ''
    return f"({', '.join(parts)}){r}"

def items(tree):
    """yield (qualname, kind, node) for module + public classes/functions."""
    yield ('<module>', 'module', tree)
    def walk(node, prefix):
        for n in node.body:
            if isinstance(n, ast.ClassDef) and not n.name.startswith('_'):
                yield (prefix + n.name, 'class', n); yield from walk(n, prefix + n.name + '.')
            elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and not n.name.startswith('_'):
                yield (prefix + n.name, 'func', n)
    yield from walk(tree, '')

BASE = {'name','display_name','version','description','confidence_floor','formulary','run','viewer_data','on_register','shell_commands','summary','process_description','manifest'}

def dump(path, only_todo=True, maxdoc=380, body_lines=0):
    src = open(path).read(); tree = ast.parse(src); lines = src.splitlines()
    for q, k, n in items(tree):
        d = ast.get_docstring(n)
        if k == 'func' and '.' in q and n.name in BASE and d is None and path.endswith('tools.py'): continue
        isrest = bool(d and re.search(r'^\s*:(param|returns?)\b', d, re.M))
        nparam = 0
        if k == 'func': nparam = len([x for x in n.args.args + n.args.kwonlyargs if x.arg not in ('self', 'cls')])
        stale = bool(d and re.search(r'ainulindale_engine|FactoralDecomposition|\bformerly\b|\brenamed\b|\b20\d\d-\d\d-\d\d\b|\bPhase \d\b|\bnot yet\b', d))
        need = (d is None) or stale or (k == 'func' and nparam and not isrest)
        if k == 'class' and d is None: need = True
        if only_todo and not need: continue
        print(f"### {q} [{k}]" + (f" L{n.lineno}" if k != 'module' else ''))
        if k == 'func':
            print(f"sig: {n.name}{_sig(n)}")
            rs = sorted({ast.unparse(x.exc.func if isinstance(x.exc, ast.Call) else x.exc) for x in ast.walk(n) if isinstance(x, ast.Raise) and x.exc})
            if rs: print("raises:", rs)
        if d is None:
            print("doc: <MISSING>")
            if body_lines and k != 'module':
                b = lines[n.body[0].lineno - 1: n.body[0].lineno - 1 + body_lines]
                print("body:\n" + "\n".join("  " + l for l in b))
        else:
            print("doc:" + (" [STALE]" if stale else "") + (" [rest]" if isrest else ""))
            print(textwrap.indent(d if len(d) <= maxdoc else d[:maxdoc] + ' …', '  '))
        print()

def render(doc, indent):
    doc = doc.strip('\n')
    doc = textwrap.dedent(doc).strip('\n')
    raw = '\\' in doc
    doc = doc.replace('"""', "'''")
    lines = doc.split('\n')
    pad = ' ' * indent
    q = ('r' if raw else '') + '"""'
    if len(lines) == 1 and len(pad) + len(lines[0]) + 8 < 100:
        return [pad + q + lines[0] + '"""']
    body = [(pad + l if l.strip() else '') for l in lines]
    return [pad + q + lines[0]] + body[1:] + [pad + '"""'] if False else [pad + q + '\n' + pad + lines[0]] + body[1:] + [pad + '"""']

def fields(spec):
    out = []
    for k, v in (spec.get('params') or {}).items():
        out.append(f":param {k}: {v}")
        t = (spec.get('types') or {}).get(k)
        if t: out.append(f":type {k}: {t}")
    if spec.get('returns'): out.append(f":returns: {spec['returns']}")
    if spec.get('rtype'): out.append(f":rtype: {spec['rtype']}")
    for k, v in (spec.get('raises') or {}).items(): out.append(f":raises {k}: {v}")
    return out

def apply(path, edits):
    src = open(path).read(); tree = ast.parse(src); lines = src.split('\n')
    plan = []  # (start, end, newlines) 0-indexed [start,end)
    seen = set()
    for q, k, n in items(tree):
        if q not in edits: continue
        seen.add(q); spec = edits[q]
        first = n.body[0] if n.body else None
        has = isinstance(first, ast.Expr) and isinstance(getattr(first, 'value', None), ast.Constant) and isinstance(first.value.value, str)
        if k == 'module': indent = 0
        else: indent = (first.col_offset if first else n.col_offset + 4)
        old = ast.get_docstring(n) if has else None
        if spec.get('doc') is not None: text = spec['doc']
        elif old is not None:
            text = old
            for a, b in spec.get('sub', []):
                if a not in text: print(f'WARN {path}: {q}: sub text not found: {a[:40]!r}')
                text = text.replace(a, b)
        else: text = spec.get('summary', '')
        f = fields(spec)
        if f:
            text = text.rstrip('\n') + ('\n\n' if text.strip() else '') + '\n'.join(f)
        new = render(text, indent)
        if has: plan.append((first.lineno - 1, first.end_lineno, new))
        else:
            if k == 'module': plan.append((0, 0, new))
            else:
                if first.lineno == n.lineno and not getattr(first,'decorator_list',None): print(f"WARN one-line def {q}"); continue
                start = min([first.lineno] + [x.lineno for x in getattr(first, 'decorator_list', [])]) - 1
                plan.append((start, start, new))
    for q in edits:
        if q not in seen: print(f"WARN {path}: {q} not found")
    for s, e, new in sorted(plan, reverse=True): lines[s:e] = new
    out = '\n'.join(lines); ast.parse(out); open(path, 'w').write(out)

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'dump': dump(sys.argv[2], only_todo='--all' not in sys.argv, body_lines=int(next((a[7:] for a in sys.argv if a.startswith('--body=')), 0)))
    elif cmd == 'apply': apply(sys.argv[2], json.load(open(sys.argv[3])))
