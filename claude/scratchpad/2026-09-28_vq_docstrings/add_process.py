"""Give every Equation a process= line, derived from what the code already says:
the first sentence of compute()'s docstring, else the equation's display text."""
import ast, contextlib, io, re, sys, pathlib, os, textwrap
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.__main__ import _register_all

reg = _register_all()
ROOT = pathlib.Path('/home/rendier/Projects/ThePlace/ValaQuenta')

def first_sentence(doc):
    doc = ' '.join(doc.strip().split('\n\n')[0].split())
    m = re.match(r'(.+?[.!?])(\s|$)', doc)
    s = m.group(1) if m else doc
    return s

def shouty(s):
    letters = [c for c in s if c.isalpha()]
    return len(letters) > 8 and sum(c.isupper() for c in letters) / len(letters) > 0.6

def clean(s):
    s = s.replace('\\|', '|').replace('\\*', '*')
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'\[(OPEN|SOLVED|ESTABLISHED|THEORETICAL)[^\]]*\]\s*$', '', s).strip()
    return s

def process_for(e):
    doc = getattr(e.compute, '__doc__', None) if e.compute else None
    cand = ''
    if doc:
        cand = clean(first_sentence(doc))
    if not cand or shouty(cand) or len(cand) < 12 or cand.startswith(':'):
        cand = clean(e.display)
        if ':' in cand:
            head, _, tail = cand.partition(':')
            if head.strip().upper() == head.strip() and tail.strip():
                cand = tail.strip()
    if len(cand) > 170:
        cand = cand[:167].rsplit(' ', 1)[0] + '…'
    return cand

total = 0
for name in reg.list_modules():
    mod = reg.get_module(name)
    procs = {e.name: process_for(e) for e in mod.formulary() if not e.process}
    path = ROOT / 'modules' / name / 'tools.py'
    src = path.read_text()
    tree = ast.parse(src)
    starts = [0]
    for l in src.split('\n'):
        starts.append(starts[-1] + len(l) + 1)
    def off(line, col):      # col is a UTF-8 byte offset
        text = src.split('\n')[line - 1]
        return starts[line - 1] + len(text.encode()[:col].decode())
    edits = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and getattr(n.func, 'id', None) == 'Equation':
            if any(k.arg == 'process' for k in n.keywords):
                continue
            parts = list(n.args) + [k.value for k in n.keywords]
            if not parts:
                continue
            key = None
            if n.args and isinstance(n.args[0], ast.Constant):
                key = n.args[0].value
            for k in n.keywords:
                if k.arg == 'name' and isinstance(k.value, ast.Constant):
                    key = k.value.value
            if key not in procs:
                continue
            last = max(parts, key=lambda x: (x.end_lineno, x.end_col_offset))
            edits.append((last, n, procs.pop(key)))
    for last, n, proc in sorted(edits, key=lambda x: (x[0].end_lineno, x[0].end_col_offset), reverse=True):
        pos = off(last.end_lineno, last.end_col_offset)
        multi = n.end_lineno > n.lineno
        if multi and last.lineno > n.lineno:
            line = src.split('\n')[last.lineno - 1]
            indent = re.match(r'\s*', line).group(0)
            ins = f",\n{indent}process={proc!r}"
        else:
            ins = f", process={proc!r}"
        src = src[:pos] + ins + src[pos:]
        total += 1
    if edits:
        ast.parse(src)
        path.write_text(src)
    if procs:
        print('UNPLACED', name, list(procs))
print('inserted', total)
