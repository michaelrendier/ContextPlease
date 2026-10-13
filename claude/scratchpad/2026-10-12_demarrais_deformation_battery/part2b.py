import sys, math, json
sys.path.insert(0,'.')
import numpy as np
from cdalg import *
asr = bk.assessors()
DV = np.array([diag_vec(a, b, s) for (a, b) in asr for s in (1, -1)])
nz = lambda v, t=1e-9: np.linalg.norm(v) < t
pairs = [(i, j) for i in range(84) for j in range(84) if nz(mul(DV[i], DV[j]))]
GAP = 1/(1000*2**0.5)

# (i) GAP all-levels: is 537 a tolerance artifact?  count capable plane pairs at a much tighter threshold.
def count_pairs(mus, tol):
    T = table(mus); planes=[(a,b+8) for (a,b) in asr]; n=0
    for p1 in range(42):
        for p2 in range(42):
            i1,i2=planes[p1]; j1,j2=planes[p2]
            M=np.stack([T[i1,j1],T[i1,j2],T[i2,j1],T[i2,j2]],axis=1)
            s=np.linalg.svd(M,compute_uv=False)
            if s[-1] < tol*max(1.0, s[0]) : n+=1
    return n
print("(i) GAP at all four levels, plane pairs with a null direction (before the rank-1 test), by tolerance:")
for tol in (1e-9, 1e-12, 1e-14):
    print("    tol=%g : %d  [standard algebra: %d]" % (tol, count_pairs((-GAP,)*4, tol), count_pairs(STD, tol)))

# (ii) one-parameter ZD-preserving families: left / right multiplication by exp(theta e_t)
print("\n(ii) multiplication by u=cos(th)+sin(th) e_t  -- fraction of the 336 ZD pairs kept (th=0.3 and th=1.1)")
print("    t   R_u both  R_u x-only  R_u y-only |  L_u both  L_u x-only  L_u y-only")
E=np.eye(16)
def frac(f): return sum(1 for (i,j) in pairs if f(DV[i],DV[j]))/len(pairs)
out={}
for t in range(1,16):
    row=[]
    for th in (0.3,1.1):
        u=np.zeros(16); u[0]=math.cos(th); u[t]=math.sin(th)
        R=lambda v: mul(v,u); L=lambda v: mul(u,v)
        row.append((frac(lambda x,y: nz(mul(R(x),R(y)))),frac(lambda x,y: nz(mul(R(x),y))),frac(lambda x,y: nz(mul(x,R(y)))),
                    frac(lambda x,y: nz(mul(L(x),L(y)))),frac(lambda x,y: nz(mul(L(x),y))),frac(lambda x,y: nz(mul(x,L(y))))))
    same = all(abs(a-b)<1e-9 for a,b in zip(row[0],row[1]))
    out[t]=row
    print("   %2d   %.3f      %.3f       %.3f    |  %.3f      %.3f       %.3f   %s" % ((t,)+tuple(row[0])+("" if same else "(depends on theta)",)))

# (iii) constants as rotation angle in the Assessor plane, min over partner diagonals
print("\n(iii) constants as the rotation angle theta (radians) of a diagonal inside its own plane; defect = min_y ||x(theta) y||  (analytic: 2|sin(theta - pi/4)|)")
phi=(1+5**.5)/2; W1=0.5671432904097838
C=[('0',0.0),('1',1.0),('1/2',.5),('sqrt2',2**.5),('2',2.0),('e',math.e),('pi',math.pi),('phi',phi),('ln10',math.log(10)),
   ('Omega_ZS',W1),('d*',W1/math.log(10)),('d*_spec',0.246),('GAP',GAP)]
a,b=asr[0]
for n,c in C:
    x=np.zeros(16); x[a]=math.cos(c); x[b+8]=math.sin(c)
    d=min(np.linalg.norm(mul(x,DV[j])) for j in range(84))
    print("    %-9s theta=%.5f  defect=%.5f   analytic=%.5f" % (n,c,d,2*abs(math.sin(c-math.pi/4))))

# (iv) constants as the phase scale in the strut tension law:  H_end = -cos(c * S_s)
print("\n(iv) tension at the end of the Noether path if every phase is scaled by c:  H = -cos(c * S_s)   (S: strut 1,3,6 = 0 ; 4 = 2pi ; 2,7 = -4pi/7 ; 5 = 2pi/7)")
S={'1,3,6':0.0,'4':2*math.pi,'2,7':-4*math.pi/7,'5':2*math.pi/7}
print("    %-9s %s" % ("c", "  ".join("%-9s"%k for k in S)))
for n,c in C+[('i(imag)',None)]:
    if c is None:
        print("    %-9s %s" % (n, "  ".join("%-9s"%("-cosh(%.3f)"%abs(v)) if v else "%-9s"%"-1" for v in S.values())) + "   (phase scale i: -cos(i S) = -cosh(S): leaves [-1,1])")
        continue
    print("    %-9s %s" % (n,"  ".join("%+.5f "%(-math.cos(c*v)) for v in S.values())))
