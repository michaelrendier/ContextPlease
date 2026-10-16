"""P7 — more types of unit circle: the l_p unit circle {|x|^p+|y|^p=1}, measured in its own metric; its own pi_p = circumference / diameter, and area.
UNS constants as the exponent p.  Check Adler-Tanton duality pi_p = pi_q (1/p+1/q=1) and the three Cayley-Klein types (elliptic/parabolic/hyperbolic)."""
import numpy as np, math
from scipy.integrate import quad
from scipy.special import gamma as G
def pi_p(p):
    if math.isinf(p): return 4.0
    if p == 1: return 4.0
    q = p/(p-1)
    f = lambda x: (1 + (abs(x)**(p-1)/(1-x**p)**((p-1)/p))**p)**(1/p) if x < 1 else 1.0   # ell_p arclength element with y=(1-x^p)^(1/p)
    # parametrise by angle t: x=cos^(2/p) t, y=sin^(2/p) t ;  ell_p length of dx,dy
    def ds(t):
        dx = (2/p)*math.cos(t)**(2/p-1)*(-math.sin(t)); dy = (2/p)*math.sin(t)**(2/p-1)*math.cos(t)
        return (abs(dx)**p + abs(dy)**p)**(1/p)
    L, _ = quad(ds, 0, math.pi/2, limit=400, epsabs=1e-12)
    return 4*L/2
def area_p(p):
    if math.isinf(p): return 4.0
    return 4*G(1+1/p)**2/G(1+2/p)
LN10 = math.log(10); PHI = (1+5**.5)/2; OM = 0.5671432904097838
print(f"{'p':>12} {'name':>8} {'pi_p':>10} {'area':>10} {'area/pi_p':>10}   (Euclid p=2: pi, pi, 1)")
for name, p in (("1", 1.0), ("Omega^-1", 1/OM), ("phi", PHI), ("sqrt2", 2**.5), ("2", 2.0), ("e", math.e), ("ln10", LN10), ("3", 3.0), ("pi", math.pi), ("inf", float("inf"))):
    print(f"{p:12.6f} {name:>8} {pi_p(p):10.6f} {area_p(p):10.6f} {area_p(p)/pi_p(p):10.6f}")
print("\nduality pi_p = pi_q for 1/p+1/q = 1 (Adler-Tanton 1980): the p <-> q fold is the circle's inversion fold")
for p in (1.3, PHI, 2**.5, 3.0, math.e):
    q = p/(p-1); print(f"   p={p:.4f} q={q:.4f}  pi_p={pi_p(p):.8f}  pi_q={pi_p(q):.8f}  diff={abs(pi_p(p)-pi_p(q)):.1e}")
print("   p=2 is the self-dual point (q=2) and the MINIMUM of pi_p: pi_2 = pi =", pi_p(2.0), " ;  p=1,inf give 4 (taxicab, Chebyshev)")
ps = np.linspace(1.01, 8, 300); vals = [pi_p(p) for p in ps]; print(f"   min over p in (1,8): {min(vals):.8f} at p={ps[int(np.argmin(vals))]:.3f}")
print("\nCayley-Klein types (one-parameter family  x^2 + eps y^2 = 1):  eps=+1 circle (elliptic),  eps=0 two lines x=±1 (parabolic, dual numbers),  eps=-1 hyperbola (hyperbolic, split-complex)")
for eps in (1, 0, -1):
    print(f"   eps={eps:+d}: norm form x^2{'+' if eps>0 else '-' if eps<0 else '+0*'}y^2 ; unit conic: {'circle' if eps>0 else 'lines' if eps==0 else 'hyperbola'} ; one-parameter group: {'rotation (periodic, trace<2)' if eps>0 else 'shear (trace=2)' if eps==0 else 'boost/dilation (trace>2)'}")
