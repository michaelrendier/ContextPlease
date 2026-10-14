"""Strut as muscle, v2: the internal motion that FIXES a strut diagonal y exactly = the stabiliser of y in Der(sedenions) (dim 3 = SU(2)). Flow it: what moves?"""
exec(open('jb.py').read().split('print("JB-1')[0])
Ds=derivations(); keys=list(DV.keys()); Y={k:DV[k] for k in keys}
y=Y[(1,2,1)]; M=np.array([D@y for D in Ds]).T      # 16 x 14
u,s,vt=np.linalg.svd(M); r=int((s>1e-9).sum()); S=vt[r:]; print("stabiliser of y=(1,2,+) in g2: dim",S.shape[0])
Dst=[sum(c*D for c,D in zip(row,Ds)) for row in S]
def Rm(v): return np.einsum('j,ijk->ki',v,T_)
def kerd(v): return int((np.linalg.svd(Rm(v),compute_uv=False)<1e-9).sum())
nbrs=[k for k in keys if nz(m(Y[k],y))<1e-9 and k!=(1,2,1)]   # z with z*y=0 : lattice partners N(y)
opp=Y[(2,1,-1)]
print("lattice partners z with z*y=0:",len(nbrs),nbrs)
g0=np.eye(16)
rng=np.random.default_rng(2); t=rng.normal(size=3); D=sum(c*d for c,d in zip(t,Dst))
for th in (0.3,0.8,1.6):
    g=expm(th*D)/1.0
    # D is a generator scaled arbitrarily; report movement
    ok=nz(g@y-y)
    mv=[nz(g@Y[k]-Y[k]) for k in nbrs]; lat=[int((np.abs(g@Y[k])>1e-9).sum()) for k in nbrs]
    print(f" theta={th}: |g y - y|={ok:.1e}; opposite diag moved {nz(g@opp-opp):.3f}; 4 partners moved {np.round(mv,3)}; nonzeros per partner {lat}; partners still annihilate y: {max(nz(m(g@Y[k],y)) for k in nbrs):.1e}; images are ZD: {[kerd(g@Y[k]) for k in nbrs]}")
# does the strut's own kite stay a kite? other 4 vertices (neighbour-of-opposite etc)
ker_idx=[k for k in keys if (k[0]^k[1])==3]; 
g=expm(0.8*D); print(" whole kite s=3 (12 diagonals) after flow, still ZD (kernel 4):",all(kerd(g@Y[k])==4 for k in ker_idx),"; other kites also ZD:",all(kerd(g@Y[k])==4 for k in keys))
