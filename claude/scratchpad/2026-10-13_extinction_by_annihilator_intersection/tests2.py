"""T1 structure of the survivors; T2 one map, two readings (many-to-one / one-to-many); T3 a G2 flow driven by a focus deforms the kite
and the extinction logic is invariant while the lattice labels move."""
import sys, itertools, collections
sys.path.insert(0,'/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-10-13_portals_inventory_moving_kite')
from common import *
from scipy.linalg import expm
from scipy.optimize import least_squares
keys=list(DV.keys()); Y=[DV[k] for k in keys]
def Rm(y): return np.einsum('j,ijk->ki',y,T_)
R=[Rm(y) for y in Y]
def ker(idx):
    M=np.vstack([R[i] for i in idx]); u,s,vt=np.linalg.svd(M); r=int((s>1e-9).sum()); return vt[r:].T
# T1
c4=c2=0; same_assessor=0; supp=collections.Counter()
for i,j in itertools.combinations(range(84),2):
    K=ker([i,j]); d=K.shape[1]
    if d==4:
        c4+=1; same_assessor+= (keys[i][:2]==keys[j][:2])
    elif d==2:
        c2+=1
        sup=tuple(np.where(np.abs(K).max(axis=1)>1e-9)[0]); supp[sup]+=1
print("T1 dim4 pairs:",c4," of which the +/- diagonals of ONE Assessor:",same_assessor)
print("T1 dim2 pairs:",c2," distinct kernel supports (basis indices touched):",len(supp)); 
for s,n in list(supp.items())[:4]: print("   support",s,"x",n)
a_of=lambda k:(k[0],k[1])
# are the dim2 pairs: two different Assessors that are edge-neighbours in a kite?
edge=0
for i,j in itertools.combinations(range(84),2):
    if ker([i,j]).shape[1]==2:
        (a,b,_),(c,d,_)=keys[i],keys[j]; edge+= ((a^b)==(c^d)) and (a,b)!=(c,d) and (a,b)!=(d,c)
print("T1 dim2 pairs that are same-strut, different, non-reversed Assessors (= kite edge rule):",edge,"/",c2)
# T2 singular spectrum and the coset
sv=np.linalg.svd(R[0]/np.linalg.norm(Y[0]),compute_uv=False); print("\nT2 normalised sv of x->xy:",np.round(sv,4)," => contract x%d, neutral x%d, dilate x%d"%((sv<1e-9).sum(),(abs(sv-1)<1e-9).sum(),(abs(sv-2**.5)<1e-9).sum()))
rng=np.random.default_rng(1); z=R[0]@rng.normal(size=16)           # a point of the image
x0=np.linalg.lstsq(R[0],z,rcond=None)[0]; N=ker([0])
errs=[np.linalg.norm(R[0]@(x0+N@rng.normal(size=4))-z) for _ in range(200)]
print("   forward many-to-one: every x in z+N(y) maps to the same z (max err %.1e); inverse one-to-many: z has a 4-dim coset of preimages"%max(errs))
# T3: G2 flow carrying a reference diagonal onto a focus diagonal
Ds=derivations()
def flow(t): return expm(sum(ti*D for ti,D in zip(t,Ds)))
y0,y1=Y[0],Y[keys.index((keys[40][0],keys[40][1],keys[40][2]))]
sol=least_squares(lambda t: flow(t)@y0-y1, np.zeros(14)); print("\nT3 residual carrying y0 onto focus y1 by exp(sum t_i D_i):",float(np.linalg.norm(sol.fun)),"  |t|=%.3f"%np.linalg.norm(sol.x))
g=flow(sol.x)
# automorphism check and annihilator covariance
x,y=rng.normal(size=16),rng.normal(size=16); print("   g automorphism err:",float(np.linalg.norm(g@m(x,y)-m(g@x,g@y))))
Ng=g@ker([0]); print("   g N(y0) annihilates g y0: max |x*(g y0)| =",float(max(np.linalg.norm(m(Ng[:,k],g@y0)) for k in range(4))))
# extinction dims invariant under g, lattice labels not
pairs=[(0,1),(0,2),(5,17),(3,60)]
for i,j in pairs:
    M=np.vstack([Rm(g@Y[i]),Rm(g@Y[j])]); d1=16-int((np.linalg.svd(M,compute_uv=False)>1e-9).sum()); print("   pair",i,j,"common-kernel dim before",ker([i,j]).shape[1],"after flow",d1)
gy=g@Y[0]; print("   flowed reference diagonal off the lattice (non-zero entries):",int((abs(gy)>1e-9).sum()),"(lattice diagonal has 2)")
