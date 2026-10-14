"""Are the struts singular or multiple? Is there a binding force (friction) where struts cross?
Strut = the 3 antipodal pairs of a kite = reversal pairs of Assessors {(a,b),(b,a)}, b=a^s. 4 diagonals each: (a,b,+-),(b,a,+-).
Friction proxies (all exact, tol 1e-9): |xy|/|x||y|, |yx|/..., commutator |xy-yx|, annihilator relations, closure of partner spaces."""
import sys, itertools, collections
sys.path.insert(0,'/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-10-13_portals_inventory_moving_kite')
from common import *
keys=list(DV.keys()); Y={k:DV[k] for k in keys}
def Rm(y): return np.einsum('j,ijk->ki',y,T_)
def ker(*ys):
    M=np.vstack([Rm(y) for y in ys]); u,s,vt=np.linalg.svd(M); r=int((s>1e-9).sum()); return vt[r:].T
nz=lambda v:np.linalg.norm(v)
def stats(x,y):
    p,q=m(x,y),m(y,x); n=nz(x)*nz(y)
    return nz(p)/n, nz(q)/n, nz(p-q)/n, nz(p+q)/n
print("== one strut, its four diagonals: (a,b,+),(a,b,-),(b,a,+),(b,a,-)   [a,b]=(1,2) strut s=3")
a,b=1,2; four=[(a,b,1),(a,b,-1),(b,a,1),(b,a,-1)]
print("pair                         |xy|   |yx|   |[x,y]| |{x,y}|  commonKerDim")
for k1,k2 in itertools.combinations(four,2):
    st=stats(Y[k1],Y[k2]); print(f"{str(k1):13s}{str(k2):13s} "+" ".join(f"{v:6.3f}" for v in st)+f"   {ker(Y[k1],Y[k2]).shape[1]}")
# the two components: N+ = common annihilator of (a,b,+),(b,a,-); N- = of (a,b,-),(b,a,+)
Np=ker(Y[(a,b,1)],Y[(b,a,-1)]); Nm=ker(Y[(a,b,-1)],Y[(b,a,1)])
print("\ncomponent partner spaces: dim N+ =",Np.shape[1]," dim N- =",Nm.shape[1]," overlap dim =",Np.shape[1]+Nm.shape[1]-np.linalg.matrix_rank(np.hstack([Np,Nm]),tol=1e-9))
print("  max |<N+,N->| (orthogonality):",float(np.abs(Np.T@Nm).max()))
S=np.hstack([Np,Nm]); print("  span(N+,N-) dim =",np.linalg.matrix_rank(S,tol=1e-9))
Q,_=np.linalg.qr(S); r=np.linalg.matrix_rank(S,tol=1e-9); Q=Q[:,:r]
rng=np.random.default_rng(0); worst=0
for _ in range(50):
    x=Q@rng.normal(size=r); y=Q@rng.normal(size=r); worst=max(worst,nz(Q@(Q.T@m(x,y))-m(x,y)))
print("  span closed under product? max residual outside span:",round(float(worst),4),"(0 => a subalgebra)")
supp=sorted(set(np.where(np.abs(S).max(axis=1)>1e-9)[0])); print("  basis indices touched by span(N+,N-):",supp)
# friction across struts: classify all pairs of the 84 diagonals
cls=collections.defaultdict(list)
def kind(k1,k2):
    (a1,b1,s1),(a2,b2,s2)=k1,k2; st1,st2=a1^b1,a2^b2
    if st1!=st2: return "different kite"
    if (a1,b1)==(a2,b2): return "same Assessor, +/-"
    if (a1,b1)==(b2,a2): return "same strut (reversal), "+("same sign" if s1==s2 else "opp sign")
    return "same kite, different strut"
for k1,k2 in itertools.combinations(keys,2):
    cls[kind(k1,k2)].append(stats(Y[k1],Y[k2]))
print("\n== friction by class (mean over pairs; |xy|/|x||y| , |yx| , |[x,y]| , |{x,y}|) and fraction with xy=0")
for c,v in sorted(cls.items()):
    A=np.array(v); print(f"{c:36s} n={len(v):5d}  "+" ".join(f"{A[:,i].mean():6.3f}" for i in range(4))+f"   xy=0: {(A[:,0]<1e-9).mean():.2f}  [x,y]=0: {(A[:,2]<1e-9).mean():.2f}")
