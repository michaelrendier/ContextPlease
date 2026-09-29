import ast,re,glob,sys
P=r'FactoralDecomposition|\bformerly\b|\brenamed\b|\b20\d\d-\d\d-\d\d\b|\bPhase \d\b|\bnot yet\b|\bTODO\b|\bpending\b|\bpreviously\b|\bused to\b|\bno longer\b|\bnow (?:lives|uses|returns)\b'
for f in sorted(glob.glob('**/*.py',recursive=True)):
    if any(s in f for s in('.venv','build/','__pycache__','notebooks/','code/','addenda/')): continue
    if len(sys.argv)>1 and not f.startswith(sys.argv[1]): continue
    t=ast.parse(open(f).read())
    for n in ast.walk(t):
        if isinstance(n,(ast.FunctionDef,ast.ClassDef,ast.Module,ast.AsyncFunctionDef)):
            d=ast.get_docstring(n)
            if d:
                for m in re.finditer(P,d): print(f"{f}:{getattr(n,'lineno',1)} {getattr(n,'name','<module>')}: …{d[max(0,m.start()-70):m.end()+50]!r}")
