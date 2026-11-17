import sys, numpy as np
sys.path.insert(0,'/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.circle_atlas import maths as A
from ValaQuenta.modules.tier8_sedenion.maths import cd_mul
from ValaQuenta.modules.box_kite.maths import zero_divisor_pairs
E=np.eye(16)
def L(x): return np.array([cd_mul(x,E[j]) for j in range(16)]).T
pairs=zero_divisor_pairs(); zd=sorted({p[0] for p in pairs})
parent={d:d for d in zd}
def find(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
for x,y in pairs: parent[find(x)]=find(y)
comp={d:find(d) for d in zd}
Ls={d:L(A._diag(d)) for d in zd}
def read(a,b): return tuple(np.round(np.linalg.svd(Ls[a]@Ls[b],compute_uv=False),4))
for a in zd[:3]:
    cls={}
    for b in zd:
        cls.setdefault(read(a,b),[]).append(('same' if comp[b]==comp[a] else 'other',b==a))
    print(a, len(cls))
    for k,v in cls.items(): print('  ',len(v), {x for x in v}, k[:16:3])
