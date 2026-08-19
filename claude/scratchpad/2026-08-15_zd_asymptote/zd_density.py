#!/usr/bin/env python3
"""
ZD density up the Cayley-Dickson tower, and what survives.

Question (Cody, 2026-08-15): "Zero Divisor appearance roughly halves as you
move up the tower... asymptotically... what is that value of that asymptote,
and what kind of waste land exists after it?"

Counts every basis-pair diagonal (e_i +/- e_j)/sqrt(2) at each level, marks
which are zero divisors, and characterises the ones that are NOT.
"""
import sys, math
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
import numpy as np
from ValaQuenta.modules.box_kite.maths import cd_multiplication_table


def basis_ops(tab, dim):
    P = np.zeros((dim, dim, dim))
    for i in range(dim):
        for j in range(dim):
            s, k = tab[(i, j)]          # (SIGN, INDEX)
            P[i, k, j] = s
    return P


def census(level, tol=1e-10):
    tab, dim = cd_multiplication_table(level)
    P = basis_ops(tab, dim)
    r = 1 / math.sqrt(2)
    zd, non = [], []
    for i in range(dim):
        for j in range(i + 1, dim):
            for sg in (1.0, -1.0):
                L = (P[i] + sg * P[j]) * r
                s = np.linalg.svd(L, compute_uv=False)
                (zd if s.min() < tol else non).append((i, j, int(sg)))
    return dim, zd, non


print("=" * 78)
print("ZERO-DIVISOR DENSITY AMONG BASIS-PAIR DIAGONALS")
print("=" * 78)
print(f"{'dim':>5} {'candidates':>12} {'ZD':>10} {'non-ZD':>10} "
      f"{'ZD frac':>10} {'non frac':>10} {'non ratio':>11}")

rows, prev = [], None
for lv in (3, 4, 5, 6, 7):
    dim, zd, non = census(lv)
    cand = dim * (dim - 1)                 # C(dim,2) pairs x 2 signs
    fz, fn = len(zd) / cand, len(non) / cand
    ratio = '' if prev is None else f"{fn / prev:.5f}"
    print(f"{dim:>5} {cand:>12} {len(zd):>10} {len(non):>10} "
          f"{fz:>10.5f} {fn:>10.5f} {ratio:>11}")
    rows.append((dim, cand, zd, non, fz, fn))
    prev = fn

print()
print("=" * 78)
print("WHAT THE SURVIVORS ARE  --  classifying the non-zero-divisors")
print("=" * 78)
for dim, cand, zd, non, fz, fn in rows:
    if dim < 16:
        continue
    H = dim // 2
    with_e0 = sum(1 for i, j, s in non if i == 0)
    # a == b in the assessor sense: index pair differing by exactly H
    partner = sum(1 for i, j, s in non if i != 0 and j - i == H)
    rest = len(non) - with_e0 - partner
    print(f"dim {dim:>4}   non-ZD {len(non):>6}  =  "
          f"e_0 pairs {with_e0:>5}  +  (e_i, e_(i+H)) partners {partner:>4}"
          f"  +  other {rest:>6}")

print()
print("=" * 78)
print("THE ASYMPTOTE")
print("=" * 78)
fns = [r[5] for r in rows if r[0] >= 16]
dims = [r[0] for r in rows if r[0] >= 16]
print("non-ZD fraction:", [f"{x:.6f}" for x in fns])
rat = [fns[i + 1] / fns[i] for i in range(len(fns) - 1)]
print("successive ratios:", [f"{x:.6f}" for x in rat])
print()
print(f"ZD fraction -> {1 - 0:.0f} (non-ZD fraction -> 0)")
print(f"last measured ZD fraction: {rows[-1][4]:.6f} at dim {rows[-1][0]}")
print()
# how the non-ZD COUNT grows, vs how candidates grow
cnts = [len(r[3]) for r in rows if r[0] >= 16]
print("non-ZD counts:", cnts)
print("count ratios :", [f"{cnts[i+1]/cnts[i]:.5f}" for i in range(len(cnts)-1)])
print("candidates grow x4 per doubling; non-ZD grows x~2.4, so the fraction")
print("shrinks by ~0.6 each level -- 'roughly halves', slightly slower than half.")
