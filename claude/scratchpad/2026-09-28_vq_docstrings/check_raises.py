import ast,glob,re,sys
bad=0
for f in sorted(glob.glob('**/*.py',recursive=True)):
    if any(s in f for s in('.venv','build/','__pycache__','notebooks/')): continue
    t=ast.parse(open(f).read())
    for n in ast.walk(t):
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
            d=ast.get_docstring(n) or ''
            doc=set(re.findall(r'^\s*:raises (\w+):',d,re.M))
            body=set()
            for x in ast.walk(n):
                if isinstance(x,ast.Raise) and x.exc is not None:
                    e=x.exc.func if isinstance(x.exc,ast.Call) else x.exc
                    body.add(ast.unparse(e))
            miss=doc-body
            if miss: bad+=1; print(f"{f}:{n.lineno} {n.name}: documents {sorted(miss)} but body raises {sorted(body)}")
print(bad)
