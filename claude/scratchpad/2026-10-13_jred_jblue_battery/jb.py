"""J_red / J_blue required battery (standing rule, Cody 2026-10-13). ptol.c: J_red = k in {0-3,8-11} (cos, forward), J_blue = {4-7,12-15} (sin, return).
JB-1 grading; JB-2 interface (commutator lands where); JB-3 struts vs J (per-Assessor polar u; u=4 is ptol's fixed pair); JB-4 muscle test;
JB-5 friction = real part; JB-6 strut as a sheet of zero divisors and where forward/backward cross."""
import sys, itertools, collections
sys.path.insert(0,'/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-10-13_portals_inventory_moving_kite')
from common import *
from scipy.linalg import expm
RED=[0,1,2,3,8,9,10,11]; BLUE=[4,5,6,7,12,13,14,15]
chi=lambda u,i:1 if bin(u&i).count('1')%2==0 else -1
rng=np.random.default_rng(7)
def vec(S): v=np.zeros(16); v[S]=rng.normal(size=len(S)); return v
def part(v,S): w=np.zeros(16); w[S]=v[S]; return w
nz=np.linalg.norm
print("JB-1 grading by chi_4 (J_red=%s, J_blue=%s)"%(RED,BLUE))
for A,B,name in [(RED,RED,'red*red'),(RED,BLUE,'red*blue'),(BLUE,RED,'blue*red'),(BLUE,BLUE,'blue*blue')]:
    leak=[];
    for _ in range(100):
        p=m(vec(A),vec(B)); leak.append((nz(part(p,RED)),nz(part(p,BLUE))))
    L=np.array(leak); print(f"   {name:10s} mean |red part| {L[:,0].mean():7.3f}  mean |blue part| {L[:,1].mean():7.3f}")
# J_red alternative / norm multiplicative?
x,y=vec(RED),vec(RED); print("   J_red norm-multiplicative: | |xy|-|x||y| | =%.1e ; alternative: |x(xy)-(xx)y| = %.1e"%(abs(nz(m(x,y))-nz(x)*nz(y)),nz(m(x,m(x,y))-m(m(x,x),y))))
x,y=vec(BLUE),vec(BLUE); print("   J_blue*J_blue norm: | |xy|-|x||y| | = %.1e (blue is not a subalgebra; odd part)"%abs(nz(m(x,y))-nz(x)*nz(y)))
print("JB-2 interface: commutator [r,b] and [b,b'] landing")
for A,B,name in [(RED,BLUE,'[red,blue]'),(BLUE,BLUE,'[blue,blue]'),(RED,RED,'[red,red]')]:
    r=[]
    for _ in range(100):
        a,b=vec(A),vec(B); c=m(a,b)-m(b,a); r.append((nz(part(c,RED)),nz(part(c,BLUE))))
    r=np.array(r); print(f"   {name:12s} red part {r[:,0].mean():7.3f}  blue part {r[:,1].mean():7.3f}")
keys=list(DV.keys()); Y={k:DV[k] for k in keys}
def Rm(y): return np.einsum('j,ijk->ki',y,T_)
def ker(*ys):
    M=np.vstack([Rm(y) for y in ys]); u,s,vt=np.linalg.svd(M); r=int((s>1e-9).sum()); return vt[r:].T
print("JB-3 struts vs J: per strut (a,b) polar u = unique u in 1..7 with chi_u(a)=chi_u(b)=+1")
rows=[];cnt=collections.Counter()
for s in range(1,8):
    for a in range(1,8):
        b=a^s
        if a>=b: continue
        us=[u for u in range(1,8) if chi(u,a)==1 and chi(u,b)==1]; u=us[0]
        pos=[i for i in range(16) if chi(u,i)==1]; neg=[i for i in range(16) if chi(u,i)==-1]
        d_in=all(set(np.where(np.abs(Y[(a,b,sg)])>0)[0])<=set(pos) for sg in (1,-1))
        Np=ker(Y[(a,b,1)],Y[(b,a,-1)]); Nm=ker(Y[(a,b,-1)],Y[(b,a,1)])
        inneg=max(np.abs(Np[pos]).max(),np.abs(Nm[pos]).max())<1e-9
        cnt[u]+=1; rows.append((s,a,b,u,d_in,inneg))
print("   struts per polar u:",dict(sorted(cnt.items())),"(u=4 is ptol's fixed J_red/J_blue)")
print("   all diagonals inside ker chi_u:",all(r[4] for r in rows),"; all partner spaces inside the chi_u=-1 coset:",all(r[5] for r in rows))
print("JB-4 muscle test: L_x^2 = -|x|^2 ?")
worst=0; kept=collections.defaultdict(list)
for k in keys:
    x=Y[k]; L=np.einsum('i,ijk->kj',x,T_)  # y -> x y
    worst=max(worst,np.abs(L@L+np.dot(x,x)*np.eye(16)).max())
print("   max |L_x^2 + |x|^2 I| over 84 diagonals: %.2e"%worst)
x=Y[(1,2,1)]; Lx=np.einsum('i,ijk->kj',x,T_)/nz(x)
def zdness(y): return int((np.linalg.svd(Rm(y),compute_uv=False)<1e-9).sum())
def cls(k1,k2):
    (a1,b1,_),(a2,b2,_)=k1,k2
    if (a1,b1)==(a2,b2) or (a1,b1)==(b2,a2): return 'same strut'
    return 'same kite, other strut' if a1^b1==a2^b2 else 'other kite'
print("   rotate every diagonal by exp(theta L_x/|x|) (x=(1,2,+), strut s=3); kernel dim of the image (4 = still a zero divisor):")
for th in (0.0,0.3,0.8,np.pi/2):
    R=expm(th*Lx); out=collections.defaultdict(list)
    for k in keys: out[cls((1,2,1),k)].append(zdness(R@Y[k]))
    print("   theta=%.2f"%th, {c:dict(collections.Counter(v)) for c,v in out.items()})
print("JB-5 friction: symmetric part xy+yx vs -2<x,y>e0 over all pairs of diagonals")
bad=0
for k1,k2 in itertools.combinations(keys,2):
    s=m(Y[k1],Y[k2])+m(Y[k2],Y[k1]); bad=max(bad,nz(s+2*np.dot(Y[k1],Y[k2])*np.eye(16)[0]))
print("   max |xy+yx + 2<x,y>e0| = %.1e  (symmetric part is exactly the REAL part: friction = <x,y> deposited in e0)"%bad)
print("JB-6 strut as a sheet of zero divisors; where forward and backward cross")
a,b=1,2; y1,y3=Y[(a,b,1)],Y[(b,a,-1)]; y2,y4=Y[(a,b,-1)],Y[(b,a,1)]
print("   within one component (y1,y3 share N+): kernel dim of cos t y1+sin t y3:",collections.Counter(zdness(np.cos(t)*y1+np.sin(t)*y3) for t in np.linspace(0,2*np.pi,73)))
print("   across components (+ with -): kernel dim of cos t y1+sin t y2 along t:",[ (round(t,2),zdness(np.cos(t)*y1+np.sin(t)*y2)) for t in np.linspace(0,np.pi,13)])
print("   across components (y1 with y4):",collections.Counter(zdness(np.cos(t)*y1+np.sin(t)*y4) for t in np.linspace(0,2*np.pi,73)))
