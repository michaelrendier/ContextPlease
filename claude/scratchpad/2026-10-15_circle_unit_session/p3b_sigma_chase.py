"""P3b — chase: Quake's offset σ = 0.0450466 vs Ω_ZS/(4π) = 0.0451318 (0.19% apart).  Is the match structural or chance?
Model the bit trick as a real-valued function (no float rounding), find the exact minimax σ for (i) the bare guess, (ii) the guess after one Newton step;
compare each to Ω/4π and other closed forms.  Then quantify chance properly at the observed tightness."""
import numpy as np, math, random
from scipy.optimize import minimize_scalar
OM = 0.5671432904097838
t = np.linspace(0, 2, 400001)[:-1]                           # log2 x over one exponent-parity period (2 octaves)
fr = t - np.floor(t); e = np.floor(t)
bitsx = e + fr                                              # exponent + mantissa field as one real (units 2^23, bias removed)  ≈ t + (2^fr -1 - fr)
Lx = e + (2**fr - 1)                                        # the integer-reinterpreted float: exponent + mantissa m=2^fr-1
def guess(sig):
    Ly = 1.5*(-sig) - Lx/2 + 1.5*0 + 127*0                  # y bits (bias handled analytically): magic - Lx/2 with magic=1.5*(127-sig) -> bias cancels: use real exponent form
    Ly = 1.5*(127 - sig) - (Lx + 127)/2 - 127               # real-valued exponent+mantissa of y, bias removed
    ey = np.floor(Ly); y = 2**ey * (1 + (Ly - ey))
    return y
true = 2**(-t/2)
def maxerr_guess(sig): return np.max(np.abs(guess(sig)/true - 1))
def maxerr_newton(sig):
    y = guess(sig); x = 2**t; y1 = y*(1.5 - 0.5*x*y*y); return np.max(np.abs(y1/true - 1))
r0 = minimize_scalar(maxerr_guess, bounds=(0.0, 0.1), method="bounded", options={"xatol": 1e-12})
r1 = minimize_scalar(maxerr_newton, bounds=(0.0, 0.1), method="bounded", options={"xatol": 1e-12})
print(f"minimax σ, bare guess : {r0.x:.7f}  (max rel err {r0.fun:.4%})")
print(f"minimax σ, +1 Newton  : {r1.x:.7f}  (max rel err {r1.fun:.4%})    Quake σ=0.0450466 Lomont σ=0.0448368")
cands = {"Omega/4π": OM/(4*math.pi), "ln2 − 2/3·... (n/a)": 0, "1/22": 1/22, "(√2−1)/9.2": 0}
cands = {k: v for k, v in cands.items() if v}
for k, v in cands.items(): print(f"  {k}: {v:.7f}   vs Newton-optimal {r1.x:.7f}  ({abs(v-r1.x)/r1.x:.2%})   vs bare {r0.x:.7f} ({abs(v-r0.x)/r0.x:.2%})")
# chance at the observed tightness: relative distance 0.19%, with this candidate family size
obs = abs(OM/(4*math.pi) - r1.x)/r1.x
random.seed(11); target = r1.x; fam = 50; trials = 20000; hit = 0
for _ in range(trials):
    vals = [math.exp(random.uniform(math.log(1e-4), math.log(3))) for _ in range(10)]
    c = [v*f for v in vals for f in (1, .5, 2, .25, 4)]
    hit += any(abs(v - target)/target <= obs for v in c)
print(f"observed relative distance {obs:.3%}; chance that a 50-candidate family has a member that close: {hit/trials:.2%}")
# structure: does any Lambert-W closed form fall out of the log-linear minimax?  (equioscillation: the worst cases are at the mantissa extremes m=0 and the interior turning point)
