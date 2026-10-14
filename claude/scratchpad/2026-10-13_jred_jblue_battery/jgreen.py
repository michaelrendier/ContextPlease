"""JG: J_red + J_blue = J_green = 0_RB - 0_BR  (Cody 2026-10-13: 'builds in the cross and dot product, how an addition equals a subtraction').
Operational readings tried (explicit, mine):  0_RB := r*b, 0_BR := b*r  (ordered products of the red and blue parts of a state psi = r + b)."""
exec(open('jb.py').read().split('print("JB-1')[0])
import itertools
# JG-1: dot/cross decomposition xy = -<x,y>e0 + (1/2)[x,y] for pure-imaginary x,y (all CD algebras); here over random red/blue and over the 84 diagonals
e0=np.eye(16)[0]; worst=0
for _ in range(300):
    x=vec(list(range(1,16))); y=vec(list(range(1,16)))
    worst=max(worst,nz(m(x,y)-(-np.dot(x,y)*e0+0.5*(m(x,y)-m(y,x)))))
print("JG-1 xy = -<x,y>e0 + (1/2)[x,y] for pure imaginary x,y: max residual %.1e  (dot = symmetric part, in e0; cross = antisymmetric part)"%worst)
# JG-2: 0_RB - 0_BR = [r,b] ; 0_RB + 0_BR = -2<r,b> + 2 r0 b
res=[]
for _ in range(300):
    r=vec(RED); b=vec(BLUE); ORB,OBR=m(r,b),m(b,r)
    res.append((nz((ORB-OBR)-2*m(vec_im(r) if False else (r-r[0]*e0),b)), nz((ORB+OBR)-2*r[0]*b), nz(part(ORB-OBR,RED))))
R=np.array(res); print("JG-2 with r=r0e0+r_im (red), b (blue): [r,b]=2 r_im b: %.1e ; r b + b r = 2 r0 b: %.1e ; red part of 0_RB-0_BR: %.1e"%(R[:,0].max(),R[:,1].max(),R[:,2].max()))
# JG-3: grading obstruction: J_red+J_blue = r+b has a red part r; any ordered-product difference 0_RB-0_BR lies in BLUE only.
r=vec(RED[1:]); b=vec(BLUE); psi=r+b
print("JG-3 psi=J_red+J_blue: |red part| %.3f, |blue part| %.3f ; 0_RB-0_BR=[r,b]: |red part| %.1e, |blue part| %.3f  => equality as sedenion vectors is impossible whenever the red part is nonzero"%(nz(part(psi,RED)),nz(part(psi,BLUE)),nz(part(m(r,b)-m(b,r),RED)),nz(part(m(r,b)-m(b,r),BLUE))))
# JG-4: Dirichlet reading. F(s)=sum a_n n^-s ; J_red=F(s) ; J_blue=F(1-s) UNSIGNED -> sum symmetric about 1/2. SIGNED (orientation-reversed) J_blue=-F(1-s) -> J_red+J_blue = F(s)-F(1-s): antisymmetric, = 0 at s=1/2.
rng=np.random.default_rng(5); a=rng.normal(size=200); n=np.arange(1,201)
F=lambda s:np.sum(a*n**(-s))
print("JG-4 Dirichlet, random a_n, N=200:")
for s in (0.2,0.35,0.5,0.65,0.8):
    print(f"   s={s}: F(s)+F(1-s)={F(s)+F(1-s):9.4f} (unsigned sum, symmetric)   F(s)-F(1-s)={F(s)-F(1-s):9.4f} (signed sum = antisymmetrisation)")
print("   unsigned sum at s and 1-s equal:",abs((F(.2)+F(.8))-(F(.8)+F(.2)))<1e-12,"; signed difference odd about 1/2:",abs((F(.2)-F(.8))+(F(.8)-F(.2)))<1e-12,"; signed difference at 1/2 =",F(.5)-F(.5))
