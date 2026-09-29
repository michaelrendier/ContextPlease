"""Docstring audit for ValaQuenta. Usage: audit.py [--missing] [--json]"""
import ast, glob, re, sys, collections, json
SKIP = ('build/', '.venv', '__pycache__', 'notebooks/', 'docs/', 'tools/')
STALE = [r'ainulindale_engine', r'FactoralDecomposition', r'\bformerly\b', r'\brenamed\b', r'\bPhase \d\b',
         r'\bnot yet\b', r'\bpending\b', r'\bwas fixed\b', r'\b20\d\d-\d\d-\d\d\b', r'\bTODO\b', r'\bdeprecated\b', r'\bLicenseRef']
def style(d):
    if not d: return None
    if re.search(r'^\s*:(param|returns?|rtype|raises|type|ivar)\b', d, re.M): return 'rest'
    if re.search(r'^\s*(Args|Returns|Raises|Attributes):\s*$', d, re.M): return 'google'
    if re.search(r'^\s*(Parameters|Returns)\s*\n\s*-{3,}', d, re.M): return 'numpy'
    return 'plain'
rows = []
for f in sorted(glob.glob('**/*.py', recursive=True)):
    if any(s in f for s in SKIP): continue
    try: t = ast.parse(open(f).read())
    except Exception: continue
    def add(kind, name, node, line):
        d = ast.get_docstring(node)
        rows.append(dict(file=f, kind=kind, name=name, line=line, has=bool(d), style=style(d),
                         stale=[p for p in STALE if d and re.search(p, d)],
                         nparams=(len([a for a in node.args.args+node.args.kwonlyargs if a.arg not in ('self','cls')]) if kind!='class' and kind!='module' else 0)))
    add('module', f, t, 1)
    BASE = {'name','display_name','version','description','confidence_floor','formulary','run','viewer_data','on_register','shell_commands','summary','process_description','manifest'}
    def walk(node, prefix=''):
        for n in getattr(node, 'body', []):
            if isinstance(n, ast.ClassDef):
                if not n.name.startswith('_'): add('class', prefix+n.name, n, n.lineno); walk(n, prefix+n.name+'.')
            elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if n.name.startswith('_'): continue
                if prefix and n.name in BASE and not ast.get_docstring(n): continue  # inherits EquationModule docstring
                add('func', prefix+n.name, n, n.lineno)
    walk(t)
if '--json' in sys.argv: print(json.dumps(rows)); sys.exit()
c = collections.Counter((r['kind'], r['has']) for r in rows); print(dict(c))
print('styles', collections.Counter(r['style'] for r in rows if r['has']))
st = collections.Counter(p for r in rows for p in r['stale']); print('stale', dict(st))
byf = collections.defaultdict(lambda:[0,0])
for r in rows:
    byf[r['file']][0] += 1; byf[r['file']][1] += (not r['has'])
if '--missing' in sys.argv:
    for f,(n,m) in sorted(byf.items(), key=lambda x:-x[1][1]):
        if m: print(f'{m:4d}/{n:4d}  {f}')
