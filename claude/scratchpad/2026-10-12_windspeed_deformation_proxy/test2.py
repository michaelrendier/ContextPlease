#!/usr/bin/env python3
"""Follow-up: (A) are the strut sign patterns eps the rows of the Sylvester-Hadamard (Walsh) matrix?
(B) how many different groupings of rigid/responding struts do different ANCHORS produce?
(C) the three regimes (continuous / semi-continuous / discrete) from H = -cos(sum eps*phi)."""
import sys, math, random, itertools
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.box_kite import maths as bk
HP = math.pi / 2
def gen(a, b, phi):
    v = [0.0]*16; v[a] = math.cos(phi); v[b] = math.sin(phi); return v
def Hfun(r, phis):
    st = bk.pencil(r); p = gen(*st[0], phis[0])
    for k in range(1, 7): p = bk.multiply(p, gen(*st[k], phis[k]))
    return p[0]

# (A) fit eps for every pencil r = 1..15, compare with Sylvester-Hadamard rows on j = k-1 = 0..6
def had(i, j): return -1 if bin(i & j).count("1") % 2 else 1
random.seed(5)
phis_list = [[random.uniform(0, HP) for _ in range(7)] for _ in range(40)]
print("A. eps pattern per pencil r (r<=7 are the box-kite struts) vs Hadamard rows (columns j=0..6)")
for r in range(1, 16):
    hs = [Hfun(r, p) for p in phis_list]; best = None
    for eps in itertools.product((1, -1), repeat=7):
        err = max(abs(h + math.cos(sum(e*x for e, x in zip(eps, p)))) for h, p in zip(hs, phis_list))
        if best is None or err < best[0]: best = (err, eps)
    err, eps = best
    match = [i for i in range(8) if all(eps[j]*had(i, j) == eps[0]*had(i, 0) for j in range(7))]
    print("   r=%-2d err=%.1e eps=%s  = +/- Hadamard row %s" % (r, err, "".join("+" if e > 0 else "-" for e in eps), match or "NONE"))

# (B) anchors: hold a subset K of stations fixed (rate 0); signed Noether rate sum per strut
EPS = {1:"++--++-", 2:"+--++--", 3:"++--++-", 4:"+++++++", 5:"+-+-+-+", 6:"++--++-", 7:"+--++--"}
eps = {s: [1 if c == "+" else -1 for c in v] for s, v in EPS.items()}
def S(s, K):  # signed rate sum with stations in K anchored
    return sum(eps[s][k]*(k+1)/7*HP for k in range(7) if k not in K)
parts = {}
for n in range(8):
    for K in itertools.combinations(range(7), n):
        sig = {}
        for s in range(1, 8):
            sig.setdefault(round(abs(S(s, K)) % (2*math.pi), 6) if abs(S(s, K)) > 1e-9 else 0.0, []).append(s)
        key = tuple(sorted(tuple(v) for v in sig.values()))
        parts.setdefault(key, []).append(K)
print("\nB. anchoring: %d different subsets of stations held fixed -> %d different groupings of the 7 struts" % (2**7, len(parts)))
rigid = [K for key, Ks in parts.items() for K in Ks if all(abs(S(s, K)) < 1e-9 for s in (1, 3, 6))]
print("   {1,3,6} stay rigid under %d of 128 anchor subsets; rigid-set sizes seen: %s" % (
    len(rigid), sorted(set(sum(1 for s in range(1, 8) if abs(S(s, K)) < 1e-9) for K in itertools.chain.from_iterable(parts.values())))))
for key in sorted(parts, key=lambda k: -len(parts[k]))[:5]:
    print("   grouping %s  <- %d anchor subsets, e.g. anchored stations %s" % (key, len(parts[key]), [k+1 for k in parts[key][0]]))

# (C) discrete: phases in {0, pi/2}  -> H in {-1,0,1};  semi-continuous: phases on a finite grid
print("\nC. regimes of the SAME law H = -cos(sum eps*phi), strut 1:")
random.seed(3)
disc = sorted(set(round(Hfun(1, [random.choice((0, HP)) for _ in range(7)]), 9) for _ in range(300)))
grid = sorted(set(round(Hfun(1, [random.choice([i*HP/4 for i in range(5)]) for _ in range(7)]), 6) for _ in range(300)))
print("   discrete  phi in {0,pi/2}            : H values seen = %s" % disc)
print("   semi-cont phi on grid {0,pi/8,...,pi/2}: %d distinct H values, from %.3f to %.3f" % (len(grid), grid[0], grid[-1]))
print("   continuous phi real                   : H fills [-1, 1]")
