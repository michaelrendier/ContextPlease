import os,ast,importlib,sys,textwrap
D=os.environ['CLAUDE_SCRATCH']+'/2026-09-28_vq_docstrings'
sys.path.insert(0,D)
import docedit
n=0
for d in sorted(os.listdir('ValaQuenta/modules')):
    tp=f'ValaQuenta/modules/{d}/tools.py'; ip=f'ValaQuenta/modules/{d}/__init__.py'
    if not os.path.exists(tp): continue
    try:
        m=importlib.import_module(f'ValaQuenta.modules.{d}')
        cn=[x for x in getattr(m,'__all__',[]) if x.endswith('Module')]
        if not cn:
            t=ast.parse(open(tp).read()); cn=[c.name for c in t.body if isinstance(c,ast.ClassDef) and c.name.endswith('Module')]
        cls=getattr(m,cn[0]); o=cls()
    except Exception as e:
        print('skip',d,e); continue
    desc=textwrap.fill(' '.join(o.description.split()),width=76)
    t=ast.parse(open(tp).read())
    c=[x for x in t.body if isinstance(x,ast.ClassDef) and x.name==cls.__name__][0]
    if not ast.get_docstring(c):
        doc=f"{o.display_name}\n\n{desc}\n\nRegistry module for ``{d}``: :meth:`formulary` lists the equations, :meth:`run` executes one, and :meth:`viewer_data` formats a result for a viewer. The mathematics lives in :mod:`ValaQuenta.modules.{d}.maths`."
        docedit.apply(tp,{cls.__name__:{'doc':doc}}); n+=1
    it=ast.parse(open(ip).read())
    if not ast.get_docstring(it):
        doc=f"{o.display_name}\n\nRegistry class :class:`~ValaQuenta.modules.{d}.tools.{cls.__name__}`; mathematics in :mod:`ValaQuenta.modules.{d}.maths`."
        docedit.apply(ip,{'<module>':{'doc':doc}}); n+=1
print(n)
