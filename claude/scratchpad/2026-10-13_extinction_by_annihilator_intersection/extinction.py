"""Extinction of response possibilities = intersection of annihilators N(y)={x: x y = 0}.
Prompt = set of zero-divisor diagonals; surviving responses = common kernel. Exact (SVD rank, tol 1e-9)."""
import sys, itertools, collections
import numpy as np
sys.path.insert(0, '/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-10-12_demarrais_deformation_battery')
import cdalg
T = cdalg.table()
def Rmat(y):          # x -> x y
    return np.einsum('i,ijk->kj', np.ones(16), np.zeros((16,16,16))) if False else np.einsum('j,ijk->ki', y, T)
diags=[]
for a in range(1,8):
    for b in range(1,8):
        if a==b: continue
        for s in (1,-1):
            y=np.zeros(16); y[a]=1; y[b+8]=s; diags.append(((a,b,s),y))
assert len(diags)==84
R=[Rmat(y) for _,y in diags]
def kerdim(idx):
    M=np.vstack([R[i] for i in idx]); sv=np.linalg.svd(M,compute_uv=False)
    return 16-int((sv>1e-9).sum())
print("single N(y) dims:",collections.Counter(kerdim([i]) for i in range(84)))
pc=collections.Counter(kerdim(p) for p in itertools.combinations(range(84),2)); print("pairs (3486):",dict(pc))
# same strut, same kite
key=lambda i: diags[i][0][0]^diags[i][0][1]
sk=collections.Counter(); dk=collections.Counter()
for p in itertools.combinations(range(84),2):
    (sk if key(p[0])==key(p[1]) else dk)[kerdim(p)]+=1
print(" pairs same strut:",dict(sk)," different strut:",dict(dk))
tc=collections.Counter(kerdim(t) for t in itertools.combinations(range(84),3)); print("triples (95284):",dict(tc))
# is the surviving space made of lattice points? for pairs with dim>0 report whether common kernel contains a basis vector e_i
nz=0;lat=0
for p in itertools.combinations(range(84),2):
    M=np.vstack([R[i] for i in p]); u,s,vt=np.linalg.svd(M); r=int((s>1e-9).sum())
    if r<16:
        nz+=1; K=vt[r:].T
        if any(np.linalg.norm(K@(K.T@np.eye(16)[:,i])-np.eye(16)[:,i])<1e-9 for i in range(16)): lat+=1
print("pairs with nonempty common kernel:",nz," containing a basis vector e_i:",lat)
