"""What is actually lost at each rung of the Cayley-Dickson tower?"""
import numpy as np, sys
sys.path.insert(0,'/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/2026-08-08_sedenion_igpu_benchmark')
from sedbench2 import cd_mul_slow as mul, cd_conj as conj

rng = np.random.default_rng(11)
def rel(x, y):
    d = np.linalg.norm(x-y); s = max(np.linalg.norm(x), np.linalg.norm(y), 1e-30)
    return d/s

TESTS = {
 'commutative      ab = ba'          : lambda a,b,c: (mul(a,b), mul(b,a)),
 'associative      (ab)c = a(bc)'    : lambda a,b,c: (mul(mul(a,b),c), mul(a,mul(b,c))),
 'alternative      (aa)b = a(ab)'    : lambda a,b,c: (mul(mul(a,a),b), mul(a,mul(a,b))),
 'FLEXIBLE         (ab)a = a(ba)'    : lambda a,b,c: (mul(mul(a,b),a), mul(a,mul(b,a))),
 'power-assoc      (aa)a = a(aa)'    : lambda a,b,c: (mul(mul(a,a),a), mul(a,mul(a,a))),
 'norm mult.       N(ab) = N(a)N(b)' : None,
 'conj antiauto    (ab)* = b* a*'    : lambda a,b,c: (conj(mul(a,b)), mul(conj(b),conj(a))),
 'quadratic        x^2-2Re x+N = 0'  : None,
}
print(f"{'property':36s} " + "".join(f"{'dim '+str(d):>12s}" for d in (4,8,16,32,64)))
print("-"*36 + "-"*60)
for name, fn in TESTS.items():
    row = ""
    for dim in (4,8,16,32,64):
        errs = []
        for _ in range(60):
            a,b,c = (rng.normal(size=dim) for _ in range(3))
            if name.startswith('norm'):
                n = lambda v: float(v@v)
                errs.append(abs(n(mul(a,b)) - n(a)*n(b))/max(n(a)*n(b),1e-30))
            elif name.startswith('quadratic'):
                re_ = a[0]; N = float(a@a)
                lhs = mul(a,a) - 2*re_*a
                lhs[0] += N
                errs.append(np.linalg.norm(lhs)/max(N,1e-30))
            else:
                L,R = fn(a,b,c); errs.append(rel(L,R))
        m = float(np.median(errs))
        row += f"{('HOLDS' if m<1e-12 else f'{m:.2f}'):>12s}"
    print(f"{name:36s} {row}")

print("\n=== conjugation: fixed locus at every level ===")
for dim in (4,8,16,32):
    a = rng.normal(size=dim)
    fixed = np.allclose(conj(a)*np.array([1]+[0]*(dim-1)), a*np.array([1]+[0]*(dim-1)))
    s = a + conj(a)
    print(f"  dim {dim:3d}: x + x* is real-only: {np.allclose(s[1:],0)}   "
          f"x x* real: {np.allclose(mul(a,conj(a))[1:],0)}   (fixed locus = span(e_0))")
