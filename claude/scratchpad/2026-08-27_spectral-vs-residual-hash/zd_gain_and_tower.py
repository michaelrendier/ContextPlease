#!/usr/bin/env python3
"""
zd_gain_and_tower.py

TEST 2 (Cody): is a zero-divisor annihilation 'the end of a path', or does
the INVERSE exist -- two 'zeros' whose product comes out GREATER than 0?
  -> enumerate sedenion unit ZD-candidates (e_i +/- e_j)/sqrt2, take ALL
     pairwise product norms, show the gain spectrum. Canonical claim: {0,1,sqrt2}.
     gain 0   = annihilation      ("end of path")
     gain 1   = norm-preserving   (immortal pass-through)
     gain V2  = AMPLIFICATION     (two zeros -> greater than either: the inverse)
  -> also: a*b vs b*a when a*b = 0  (portal, not endpoint?)

TEST 1 (Cody): "factoring is indistinguishable from noise too high up the
tower" -> is the ZD gain spectrum still DISCRETE at CD levels 5, 6 (dim 32,
64), or does it smear toward a continuum (= noise)?
"""
import sys, math, random, itertools
sys.path.insert(0, "/home/rendier/Projects/ThePlace")
import numpy as np
from ValaQuenta.modules.box_kite.maths import cd_multiplication_table

random.seed(20260827); np.random.seed(20260827)


def make_mul(levels):
    tab, dim = cd_multiplication_table(levels)
    T = np.zeros((dim, dim), dtype=np.int32)      # index
    S = np.zeros((dim, dim), dtype=np.int8)       # sign
    for (i, j), (s, k) in tab.items():
        T[i, j] = k; S[i, j] = s
    def mul(x, y):
        out = np.zeros(dim)
        nzx = np.nonzero(x)[0]
        for i in nzx:
            xi = x[i]
            k = T[i]; s = S[i]
            out[k] += s * xi * y
        return out
    return mul, dim


def unit_2term(dim, rng):
    i, j = rng.sample(range(1, dim), 2)
    s = rng.choice([1.0, -1.0])
    v = np.zeros(dim); v[i] = 1/math.sqrt(2); v[j] = s/math.sqrt(2)
    return v


def gain_spectrum(levels, n_elts, n_pairs, label):
    mul, dim = make_mul(levels)
    rng = random.Random(levels * 7 + 1)
    elts = [unit_2term(dim, rng) for _ in range(n_elts)]
    gains = []
    annih = []            # (a*b, b*a) norms where a*b ~ 0
    for _ in range(n_pairs):
        a = elts[rng.randrange(len(elts))]
        b = elts[rng.randrange(len(elts))]
        g = np.linalg.norm(mul(a, b))
        gains.append(g)
        if g < 1e-9:
            annih.append(np.linalg.norm(mul(b, a)))
    gains = np.array(gains)
    # discreteness: cluster gains, count peaks holding >2% mass each
    hist, edges = np.histogram(gains, bins=200, range=(0, 2.2))
    mass = hist / hist.sum()
    peaks = int(np.sum(mass > 0.02))
    # entropy of the binned distribution (bits) -- low = discrete, high = smeared
    p = mass[mass > 0]
    Hbits = -np.sum(p * np.log2(p))
    near0 = float(np.mean(gains < 1e-6))
    near1 = float(np.mean(np.abs(gains - 1.0) < 1e-6))
    nearV2 = float(np.mean(np.abs(gains - math.sqrt(2)) < 1e-6))
    other = 1 - near0 - near1 - nearV2
    print(f"  {label:22s} dim={dim:3d}  peaks>2%={peaks:2d}  binH={Hbits:4.2f} bits")
    print(f"      gain=0 :{near0:6.3f}   gain=1 :{near1:6.3f}   "
          f"gain=V2:{nearV2:6.3f}   other :{other:6.3f}")
    if annih:
        aa = np.array(annih)
        print(f"      of {len(annih)} annihilating a*b=0 pairs: "
              f"b*a also 0 in {np.mean(aa<1e-9):.2f}, "
              f"b*a nonzero in {np.mean(aa>=1e-9):.2f}  "
              f"(mean |b*a| over the nonzero = {aa[aa>=1e-9].mean() if np.any(aa>=1e-9) else 0:.3f})")
    return gains, dim


print("=" * 74)
print("TEST 2 -- sedenion ZD gain spectrum (is annihilation the only outcome?)")
print("=" * 74)
gS, _ = gain_spectrum(4, 240, 40000, "sedenion (2^4)")

# explicit amplification examples: |a|=|b|=1, |a*b| = sqrt2 > either
mul16, _ = make_mul(4)
rng = random.Random(1)
print("\n  amplification examples  (|a|=|b|=1  ->  |a*b| = sqrt2 = 1.414... > 1):")
shown = 0
for _ in range(20000):
    a = unit_2term(16, rng); b = unit_2term(16, rng)
    g = np.linalg.norm(mul16(a, b))
    if abs(g - math.sqrt(2)) < 1e-9:
        ai = [(round(c, 3), k) for k, c in enumerate(a) if c]
        bi = [(round(c, 3), k) for k, c in enumerate(b) if c]
        print(f"    a={ai}  b={bi}  |a*b|={g:.4f}")
        shown += 1
        if shown >= 5:
            break

print("\n" + "=" * 74)
print("TEST 1 -- does the gain spectrum stay DISCRETE up the CD tower?")
print("=" * 74)
for lv, ne, npair in [(4, 240, 40000), (5, 240, 40000), (6, 200, 25000)]:
    gain_spectrum(lv, ne, npair, f"CD level {lv} (2^{lv})")

print("\nread:")
print("  TEST 2: gain=V2 mass > 0  => the inverse of annihilation EXISTS")
print("          (two unit 'zeros' -> product of norm sqrt2, larger than either)")
print("  TEST 1: peaks>2% and binH rising with dim => spectrum smearing toward")
print("          a continuum = factoring structure dissolving into noise")
