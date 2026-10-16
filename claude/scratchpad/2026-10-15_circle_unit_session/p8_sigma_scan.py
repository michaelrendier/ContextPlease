"""P8 — every circle 'unit' value used as sigma_RB. Uses ValaQuenta h_rb_hat (the engine) and GL circle.sigma_reading (cross-check)."""
import sys, math, cmath, csv, importlib.util
sys.path.insert(0, "/home/rendier/Projects/ThePlace/GenerationalLineage")
from engine.toolsets import circle as C
spec = importlib.util.spec_from_file_location("hrb", "/home/rendier/Projects/ThePlace/ValaQuenta/modules/h_rb_hat/maths.py")
hrb = importlib.util.module_from_spec(spec); spec.loader.exec_module(hrb)

# 1. cross-check: GL sigma_reading == h_rb_hat for real sigma
mx = 0
for s in (0.1, 0.25, 0.5, 1.0, 2.0, 3.14159, -0.7):
    a = C.sigma_reading(s)["euler_product"]; b = hrb.euler_product(s, 0.0, 20)
    mx = max(mx, abs(a - b) / max(1, abs(b)))
print("max rel diff GL vs h_rb_hat euler_product:", mx)

# 2. Noether-current ratio = wire profile: |G_p(s)/G_p(1-s)| = p^(1-2s) = exp(-2u ln p), u = s-1/2 ; min/max = exp(-2|u| ln p)
for s in (0.1, 0.3, 0.7):
    for p in (2, 3):
        r = hrb.geometric_coupling(p, s) / hrb.geometric_coupling(p, 1 - s)
        print(f"  s={s} p={p}: G(s)/G(1-s)={r:.6f}  p^(1-2s)={p**(1-2*s):.6f}  wire e^(-2|u|ln p) for min/max = {math.exp(-2*abs(s-.5)*math.log(p)):.6f}")

rows = []
def add(label, sig):
    rd = C.sigma_reading(sig)
    s = sig
    re = s.real if isinstance(s, complex) else s
    sym = 1 - s   # functional-equation partner
    rows.append(dict(label=label, sigma=s, regime=rd["regime"], theory=(hrb.sigma_to_theory(re)),
                     G2=rd["G2"], coupling_sum=rd["coupling_sum"], euler_abs=abs(rd["euler_product"]),
                     converges=rd["converges_absolutely"], offset=s - .5, partner=sym,
                     ratio_to_critical=abs(rd["coupling_sum"]) / abs(C.sigma_reading(.5)["coupling_sum"])))
for name, v in C.CONSTANTS.items():
    if name == "i": continue
    add(f"r = {name}", v)                     # constant as radius
    add(f"r = {name}/2 (half of diameter {name})", v / 2)   # half-diameter radius
    add(f"d of r={name}  (2·{name})", 2 * v)
    add(f"C of r={name}  (2π·{name})", 2 * math.pi * v)
    add(f"A of r={name}  (π·{name}²)", math.pi * v * v)
add("r = i", 1j); add("d of r=i  (2i)", 2j); add("C of r=i (2πi)", 2j * math.pi); add("A of r=i (−π)", -math.pi)
add("r = 1/2 (d=1): C = π", math.pi); add("1 − (1/2)", 0.5)

with open("p8_sigma_scan.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["label", "sigma", "regime", "G_2=2^-sigma", "sum_G_20", "|euler|", "abs_converge", "sigma-1/2", "1-sigma", "sum/sum(1/2)"])
    for r in rows:
        fmt = lambda z: (f"{z.real:.6g}" if (not isinstance(z, complex) or z.imag == 0) else f"{z:.6g}")
        w.writerow([r["label"], fmt(r["sigma"]), r["regime"], fmt(r["G2"]), fmt(r["coupling_sum"]), f"{r['euler_abs']:.6g}", r["converges"], fmt(r["offset"]), fmt(r["partner"]), f"{r['ratio_to_critical']:.4g}"])
print(len(rows), "rows -> p8_sigma_scan.csv")
print(f"{'label':44} {'sigma':>10} {'regime':34} {'sumG20':>10} {'|euler|':>10}")
for r in rows:
    if "(" in r["label"] and "half" not in r["label"] and not r["label"].startswith("r ="): continue
    if r["label"].startswith("r =") or "i" in r["label"][:6]:
        s = r["sigma"]; ss = f"{s.real:.5f}" if (not isinstance(s, complex) or s.imag == 0) else f"{s:.4f}"
        print(f"{r['label']:44} {ss:>10} {r['regime']:34} {abs(r['coupling_sum']):10.4f} {r['euler_abs']:10.4g}")
