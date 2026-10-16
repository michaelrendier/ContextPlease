"""P2 — every unit circle: take each UNS constant as the radius, diameter, circumference or area, and list all four.
Then chase coincidences: do values from different (constant, role, quantity) cells agree to 1e-3 more often than chance?"""
import math, itertools, random, cmath
import mpmath as mp
mp.mp.dps = 25
pi = mp.pi
LN10 = mp.log(10); OMEGA = mp.lambertw(1).real; PHI = (1+mp.sqrt(5))/2
CONST = {"1/2": mp.mpf(1)/2, "1": mp.mpf(1), "2": mp.mpf(2), "pi": pi, "phi": PHI, "e": mp.e, "ln10": LN10, "sqrt2": mp.sqrt(2),
         "Omega_ZS": OMEGA, "d*=d*_taut": OMEGA/LN10, "d*_spec": mp.mpf("0.246"), "GAP": mp.mpf(1)/(1000*mp.sqrt(2)), "1/pi": 1/pi, "2pi": 2*pi}
def circle_from(role, c):
    if role == "radius": r = c
    elif role == "diameter": r = c/2
    elif role == "circumference": r = c/(2*pi)
    elif role == "area": r = mp.sqrt(c/pi)
    return dict(r=r, d=2*r, C=2*pi*r, A=pi*r*r)
print(f"{'constant':12} {'role':14} {'radius':>12} {'diameter':>12} {'circumf.':>12} {'area':>12}")
rows = []
for name, c in CONST.items():
    for role in ("radius", "diameter", "circumference", "area"):
        q = circle_from(role, c); rows.append((name, role, q))
        print(f"{name:12} {role:14} {float(q['r']):12.6f} {float(q['d']):12.6f} {float(q['C']):12.6f} {float(q['A']):12.6f}")
# i as the unit (complex radius): the algebra stays exact
print("\n-- 'i' as radius / diameter (the circle becomes imaginary):")
for role in ("radius", "diameter"):
    r = 1j if role == "radius" else 0.5j
    print(f"  {role}=i : r={r}  d={2*r}  C=2πr={2*math.pi*r}  A=πr²={math.pi*r*r}   (area negative real: the circle is the 'hyperbola' of signature flip, C imaginary)")
print("  radius=1 with i^2=-1 turns x²+y²=r² into x²+y²=-1: no real points (imaginary circle); x²-y²=1 is the split-complex unit 'circle'")
# special circles
print("\n-- special: r=1/2 (d=1): C=π, A=π/4 ;  r=1/(2π): C=1 ; r=1/√π: A=1 ; r=2: C=A=4π ; d=C never (π≠1)")
print("   C=A at r=2 :", 2*math.pi*2, math.pi*4)
# coincidence chase: all four quantities of all circles, all constants as radius; cross-matches at 1e-3 relative
cells = []
for name, c in CONST.items():
    q = circle_from("radius", c)
    for k in "rdCA": cells.append((f"{k}({name})", float(q[k])))
hits = []
for (a, va), (b, vb) in itertools.combinations(cells, 2):
    if a.split("(")[1] == b.split("(")[1]: continue            # same constant: trivially related by 2, pi
    if va > 0 and vb > 0 and abs(va-vb)/max(va, vb) < 1e-3: hits.append((a, b, va, vb))
print(f"\ncross-constant near-equalities (<1e-3) among {len(cells)} cells: {len(hits)}")
for h in hits[:25]: print("  ", h[0], "≈", h[1], f"{h[2]:.6f} vs {h[3]:.6f}")
# chance baseline: replace the 14 constants by random constants of the same log-range, repeat 400x
random.seed(1); lo, hi = math.log(0.003), math.log(7)
def nhits(vals):
    cs = []
    for c in vals:
        r = c; cs += [r, 2*r, 2*math.pi*r, math.pi*r*r]
    n = 0
    for i, j in itertools.combinations(range(len(cs)), 2):
        if i//4 == j//4: continue
        a, b = cs[i], cs[j]
        if abs(a-b)/max(a, b) < 1e-3: n += 1
    return n
base = [nhits([math.exp(random.uniform(lo, hi)) for _ in CONST]) for _ in range(400)]
print(f"chance: mean {sum(base)/len(base):.2f} hits, max {max(base)}; observed {len(hits)}  -> {'unremarkable' if len(hits) <= max(base) else 'ABOVE chance'}")
