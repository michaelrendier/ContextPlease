"""P3 — is the circle machinery a cheap (cheaper) way to a fast inverse square root?
(a) Quake's bit trick measured; (b) it IS a scale in the log chart u=ln x (Archimedes screw); (c) where a circle gives a free starting point;
(d) the magic constant's offset sigma vs the UNS constants (chase, with a chance baseline)."""
import numpy as np, math, struct, random, itertools
def f2i(x): return np.array(x, dtype=np.float32).view(np.uint32).astype(np.int64)
def i2f(i): return (np.array(i, dtype=np.int64) & 0xFFFFFFFF).astype(np.uint32).view(np.float32)
rng = np.random.default_rng(0)
x = np.exp(rng.uniform(math.log(1e-6), math.log(1e6), 2_000_000)).astype(np.float32)
true = 1/np.sqrt(x.astype(np.float64))
def relerr(y): return np.abs(y.astype(np.float64)/true - 1)
def newton(x, y): return (y*(np.float32(1.5) - np.float32(0.5)*x*y*y)).astype(np.float32)
for name, magic in (("Quake 0x5f3759df", 0x5f3759df), ("Lomont 0x5f37642f", 0x5f37642f)):
    y0 = i2f(magic - (f2i(x) >> 1)); y1 = newton(x, y0); y2 = newton(x, y1)
    print(f"{name}: guess max rel err {relerr(y0).max():.4%} | +1 Newton {relerr(y1).max():.4%} | +2 Newton {relerr(y2).max():.2e}")
# (b) the trick in the log chart: float bits ~ 2^23 (log2 x + 127 - sigma);  integer shift = scale by 1/2 and negate in u
print("\n(b) float bits as a log: i(x) ≈ 2^23 (log2 x + 127 − σ0), σ0 ≈ 0.0430 on average. Then magic − i/2 = 2^23 (127·1.5 − σ·1.5·... ) :")
def sigma_of(magic): return 127 - (2*magic/ (3*2**23)) * 1  # i(y)=magic - i(x)/2 ; log2 y = -log2 x /2 =>  magic = 2^23*(1.5*(127 - sigma))
for name, magic in (("Quake", 0x5f3759df), ("Lomont", 0x5f37642f)):
    s = 127 - magic/(1.5*2**23); print(f"   {name}: magic = 2^23 · 1.5 · (127 − σ)  ->  σ = {s:.7f}")
# optimal sigma for the minimax relative error of the bare guess (no Newton)
def guess_err(sig):
    magic = int(round(1.5*2**23*(127 - sig))); y0 = i2f(magic - (f2i(x[:400000]) >> 1)); return (np.abs(y0.astype(np.float64)/true[:400000] - 1)).max()
sigs = np.linspace(0.0, 0.1, 201); errs = [guess_err(s) for s in sigs]; sbest = sigs[int(np.argmin(errs))]
print(f"   minimax-optimal σ for the bare guess ≈ {sbest:.4f} (max rel err {min(errs):.4%}); Quake's σ = 0.0450466 is optimal AFTER one Newton step (a different target)")
# (c) the circle: renormalising a vector that is already near the unit circle needs no magic: y0 = 1 is a Newton start
print("\n(c) circle start: vector (c,s) with r^2 = 1+eps. one Newton step from y0=1:  1/r ≈ (3 − r²)/2 = 1 − eps/2.")
for eps in (0.2, 0.1, 0.01, 0.001):
    r2 = 1+eps; ap = (3 - r2)/2; print(f"   eps={eps:6}: (3-r²)/2 = {ap:.8f}, true 1/r = {r2**-0.5:.8f}, rel err {abs(ap*r2**.5-1):.2e} ≈ 3ε²/8·... = {0.375*eps*eps:.2e}")
print("   cost: 1 sub + 1 mul (no sqrt, no divide, no bit tricks) -> the rotor/phase renormalisation the engine already does: cheaper than any bit trick, but ONLY near the circle")
# (d) chase: is Quake's sigma special among UNS constants?
OM = 0.5671432904097838; LN10 = math.log(10)
UNS = {"d*": OM/LN10, "d*_spec": 0.246, "GAP": 1/(1000*2**.5), "Omega": OM, "ln2": math.log(2), "1/phi^2": ((5**.5-1)/2)**2, "1/e^3": math.e**-3, "d*^2": (OM/LN10)**2, "Omega/4π": OM/(4*math.pi), "ln10/16·.31":0}
UNS.pop("ln10/16·.31")
cands = {}
for n, v in UNS.items():
    for m, f in (("x1", 1), ("x1/2", .5), ("x2", 2), ("x1/4", .25), ("x4", 4)): cands[f"{n}·{m[1:]}"] = v*f
sig_q = 127 - 0x5f3759df/(1.5*2**23)
near = [(k, v) for k, v in cands.items() if abs(v - sig_q)/sig_q < 0.02]
print(f"\n(d) Quake σ = {sig_q:.6f}; UNS-derived candidates within 2%: {near}")
random.seed(3); ncand = len(cands)
trials = []
for _ in range(2000):
    t = random.uniform(0.01, 1.0); vals = [math.exp(random.uniform(math.log(1e-4), math.log(3))) for _ in UNS]
    c2 = [v*f for v in vals for f in (1, .5, 2, .25, 4)]; trials.append(sum(abs(v - sig_q)/sig_q < 0.02 for v in c2) > 0)
print(f"    chance that some random constant×{{1,½,2,¼,4}} lands within 2% of σ: {sum(trials)/len(trials):.1%} (observed hit: {'yes' if near else 'no'})")
