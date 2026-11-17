import sys, math, numpy as np
sys.path.insert(0,'/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.tier8_sedenion.maths import cd_mul
from ValaQuenta.modules.box_kite.maths import box_kites, basis_vector
from math import gamma, pi
print("n-ball V_n, S^{n-1} area")
for n in [1,2,3,4,5,6,7,8,15,16,32]:
    V=pi**(n/2)/gamma(n/2+1); print(n, round(V,5), round(2*pi**(n/2)/gamma(n/2),5), "ball/cube", V/2**n)
rng=np.random.default_rng(0)
for dim in [2,4,8,16]:
    d=0
    for _ in range(2000):
        a=rng.normal(size=dim);a/=np.linalg.norm(a);b=rng.normal(size=dim);b/=np.linalg.norm(b)
        d=max(d,abs(np.linalg.norm(cd_mul(a,b))-1))
    print("dim",dim,"max | |ab|-1 | =",d)
E=np.eye(16)
def L(x): return np.array([cd_mul(x,E[j]) for j in range(16)]).T
print("L_k^2+I defect",[round(np.linalg.norm(L(E[k])@L(E[k])+np.eye(16)),3) for k in range(1,16)])
u=rng.normal(size=15);u/=np.linalg.norm(u);U=np.concatenate([[0],u])
print("u*u+1",np.linalg.norm(cd_mul(U,U)+E[0]))
res={}
for a in range(1,8):
  for b in range(1,8):
    for s in (1,-1):
      d=np.array(basis_vector((1.0,a),(float(s),b+8)))
      M=L(d); sv=np.linalg.svd(M,compute_uv=False)
      res[(a,b,s)]=(int(np.sum(sv<1e-9)),tuple(np.round(sv,3)))
sigs={}
for k,v in res.items(): sigs.setdefault(v,[]).append(k)
print("distinct signatures over 84 diagonals:",len(sigs))
for k,v in sigs.items(): print(len(v),"nullity",k[0],k[1])
