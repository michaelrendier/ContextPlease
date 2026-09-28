"""
Is SIGN the only thing that matters to the direction of the Noether currents?
Measured 2026-09-28 against the live code (GenerationalLineage/engine/add_scale_sign.py).
Run:  python3 sign_noether_direction.py   (from anywhere; PYTHONPATH=$PROJ)

  A. the F,B model of ValaQuenta/noether.py forced_sigma:  F=e^{-σE}, B=e^{-(1-σ)E}
       h(σ)=ln F−ln B = E(1−2σ) = ASS(add=0, scale=2E, sign=−1) applied to x=σ−½   (exact identity)
  B. flipping SIGN changes the fold u=g·ln s+a by (g−1)·ln s — zero at s=1
  C. commutation on the tier-0 floor: SIGN,SCALE commute; SIGN,ADD and SCALE,ADD do not
"""
import math, sys, os
sys.path.insert(0, os.environ.get("PROJ", "/home/rendier/Projects/ThePlace"))
from GenerationalLineage.engine.add_scale_sign import ASS

print("=== A. net direction = sign of E(1−2σ) = sign·scale·(σ−½);  F+B is NOT constant")
print(f"{'E':>5} {'σ':>5} {'lnF−lnB':>10} {'ASS(0,2E,−1)(σ−½)':>19} {'dir':>4} {'F+B':>9}")
ident_err = 0.0
for E in (0.5, 2.0, 10.0):
    T = ASS(0.0, 2.0 * E, -1)
    for s in (0.0, 0.25, 0.5, 0.75, 1.0):
        F, B = math.exp(-s * E), math.exp(-(1 - s) * E)
        h = math.log(F) - math.log(B)
        a = T(s - 0.5)
        ident_err = max(ident_err, abs(h - a))
        d = 0 if abs(h) < 1e-12 else (1 if h > 0 else -1)
        print(f"{E:5.1f} {s:5.2f} {h:10.4f} {a:19.4f} {d:+4d} {F + B:9.5f}")
print(f"max |ln F − ln B − ASS(0,2E,−1)(σ−½)| over all rows = {ident_err:.2e}")
E = 2.0
v = [math.exp(-s * E) + math.exp(-(1 - s) * E) for s in (i / 100 for i in range(101))]
im = min(range(101), key=lambda i: v[i])
print(f"F+B at E=2 over σ∈[0,1]: min {v[im]:.5f} at σ={im/100:.2f}; max {max(v):.5f}  → not conserved in σ")

print("\n=== B. flipping SIGN: Δu = (g−1)·ln s = −2 ln s")
print(f"{'scale':>6} {'add':>5} {'u(g=+1)':>10} {'u(g=−1)':>10} {'Δu':>10} {'−2 ln s':>10}")
for s, a in ((1.0, 0.0), (1.0, 2.0), (2.0, 0.0), (2.0, 2.0), (0.5, 1.0), (10.0, 0.0)):
    p, m = ASS(a, s, 1), ASS(a, s, -1)
    print(f"{s:6.2f} {a:5.1f} {p.u():10.5f} {m.u():10.5f} {m.u()-p.u():10.5f} {-2*math.log(s):10.5f}")

print("\n=== C. commutation of composed elements (add, scale, sign)")
t = lambda z: (z.add, z.scale, z.sign)
S2, A3, G = ASS.SCALE(2.0), ASS.ADD(3.0), ASS.SIGN(-1)
for name, x, y in (("SIGN,SCALE", G, S2), ("SIGN,ADD", G, A3), ("SCALE,ADD", S2, A3)):
    xy, yx = x @ y, y @ x
    print(f"{name:11} X@Y={t(xy)!s:22} Y@X={t(yx)!s:22} commute={t(xy)==t(yx)}")
for name, c in (("[ADD(3),SCALE(2)]", (~A3) @ (~S2) @ A3 @ S2),
                ("[ADD(3),SIGN(−1)]", (~A3) @ (~G) @ A3 @ G),
                ("[SCALE(2),SIGN(−1)]", (~S2) @ (~G) @ S2 @ G)):
    print(f"group commutator {name:20} = {t(c)}   (pure translation or identity)")
