import ast,sys,os,glob
def first(p):
    try:
        t=ast.parse(open(p,encoding='utf8',errors='ignore').read())
        d=ast.get_docstring(t) or ''
        return ' '.join(d.split())[:110]
    except Exception as e: return 'PARSE:'+type(e).__name__
for pat in sys.argv[1:]:
    print('##',pat)
    for p in sorted(glob.glob(pat)):
        if '__pycache__' in p or '/.venv' in p: continue
        n=sum(1 for _ in open(p,errors='ignore'))
        print(f'{n:5d} {p.split("ThePlace/")[-1]} :: {first(p)}')
