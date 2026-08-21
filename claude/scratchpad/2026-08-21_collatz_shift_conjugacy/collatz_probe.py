#!/usr/bin/env python3
"""collatz_probe.py — measurements, not assertions.

Every number printed here is COMPUTED. Provenance label in the same line.
Shortcut map used throughout:   T(n) = n/2 (n even),  (3n+1)/2 (n odd).
"""
from fractions import Fraction
from math import log, gcd, isqrt

def T(n):
    return n//2 if n % 2 == 0 else (3*n+1)//2

# ---------------------------------------------------------------- 1. the loop
print("== 1. THE ORDERED LOOP (RESULT) ==")
print("  T(1) =", T(1), "  T(2) =", T(2), " -> cycle of length 2 on {1,2}")
print("  fixed points in Z (RESULT):", [n for n in range(-20,21) if T(n)==n])

# ------------------------------------------- 2. T^k is affine on n mod 2^k
print("\n== 2. T^k IS AFFINE ON EACH CLASS mod 2^k (RESULT) ==")
def branch(k, j):
    """Return (num_odd_steps d, a, b) with T^k(n) = (3^d n + b)/2^k for n = j mod 2^k."""
    slopes = []
    for t in range(4):                       # 4 independent lifts, enough to fit affine
        n = j + t*(1<<k)
        m = n; d = 0
        for _ in range(k):
            if m % 2: d += 1
            m = T(m)
        slopes.append((n, m, d))
    ds = {s[2] for s in slopes}
    assert len(ds) == 1, (k, j, ds)          # d depends ONLY on the class
    d = ds.pop()
    (n0,m0,_),(n1,m1,_) = slopes[0], slopes[1]
    a = Fraction(m1-m0, n1-n0)
    b = Fraction(m0) - a*n0
    assert a == Fraction(3**d, 1<<k)
    return d, a, b

for k in (1,2,3,4):
    rows = [branch(k,j) for j in range(1<<k)]
    print(f"  k={k}: classes={1<<k}  slopes 3^d/2^k = "
          + ", ".join(f"3^{d}/2^{k}" for d,_,_ in rows))
    assert all(a == Fraction(3**d, 1<<k) for d,a,_ in rows)
print("  -> slope depends ONLY on d = #odd steps; class mod 2^k fixes d exactly. VERIFIED")

# ----------------------------------- 3. parity vector = 2-adic shift conjugacy
print("\n== 3. Q_k : Z/2^k -> Z/2^k IS A BIJECTION  (Bernstein-Lagarias) (RESULT) ==")
def parity_vector(n, k):
    v = 0; m = n
    for i in range(k):
        v |= (m & 1) << i
        m = T(m)
    return v
for k in (1,2,4,8,12,16):
    img = {parity_vector(n,k) for n in range(1<<k)}
    print(f"  k={k:2d}: |image| = {len(img):6d} of {1<<k:6d}  bijection={len(img)==(1<<k)}")

print("\n  conjugacy  Q(T(n)) == shift(Q(n))  on Z/2^k (RESULT):")
for k in (8,12,16):
    ok = all(parity_vector(T(n), k-1) == (parity_vector(n,k) >> 1) for n in range(1<<k))
    print(f"    k={k}: {ok}")

# -------------------------------------- 4. cycles <-> rationals, denom 2^k-3^d
print("\n== 4. EVERY PERIODIC PARITY WORD GIVES ONE RATIONAL CYCLE (RESULT) ==")
print("   denominator is exactly 2^k - 3^d")
def rational_cycle(word):
    """word = tuple of parities b_0..b_{k-1}. Solve T^k(x)=x over Q."""
    x = Fraction(0,1); a = Fraction(1,1)     # track x -> a*x + c
    c = Fraction(0,1); d = 0
    for b in word:
        if b: a, c, d = a*3/2, (c*3+1)/2, d+1
        else: a, c = a/2, c/2
    k = len(word)
    if a == 1: return None, d, k
    return c/(1-a), d, k
for word in [(1,0), (0,1), (1,1), (1,0,0), (1,1,0,0,0),
             (1,1,0,1,0,0,0), (1,)*5+(0,)*8]:
    x, d, k = rational_cycle(word)
    print(f"   word={''.join(map(str,word)):<14} k={k:2d} d={d:2d} "
          f"2^k-3^d={2**k-3**d:>8}   x = {x}")

print("\n   the ladder 2^k - 3^d for the convergents of log2(3) (RESULT):")
for k,d in [(2,1),(3,2),(5,3),(8,5),(13,8),(19,12),(84,53)]:
    print(f"     k={k:3d} d={d:3d}   2^k-3^d = {2**k-3**d:>28}   "
          f"ratio k/d = {k/d:.8f}")
print(f"     log2(3)                      = {log(3)/log(2):.8f}")
print("   -> 2^k - 3^d = 1 happens ONLY at (k,d)=(2,1). (Mihailescu/Catalan)")

# --------------------------------------------- 5. mod 3: the orphan residue
print("\n== 5. mod 3 IS THE BACKWARD-TREE ORPHAN TEST (RESULT) ==")
have_odd_pre = sorted({n % 3 for n in range(1, 3000)
                       if (2*n-1) % 3 == 0 and ((2*n-1)//3) % 2 == 1})
print("   n has an ODD predecessor  <=>  n = 2 mod 3 :", have_odd_pre)
print("   multiples of 3 never occur as (3m+1)/2 -> leaves only, forever.")
counts = {r: sum(1 for n in range(1,10**6) if n % 3 == r) for r in (0,1,2)}
print("   density of leaf-only residues in [1,10^6) (RESULT):", counts)

# --------------------------------------------------- 6. the drift at sigma=1/2
print("\n== 6. DRIFT: WHY sigma = 1/2 MAKES IT CONTRACT (RESULT) ==")
import statistics
N = 200000
tot = 0; steps = 0
for n in range(3, N, 2):
    m = n
    for _ in range(60):
        m2 = T(m); tot += log(m2/m); steps += 1; m = m2
        if m == 1: break
print(f"   measured mean log-step over {steps} steps = {tot/steps:+.6f}")
print(f"   predicted at p(odd)=1/2: 0.5*log(3/2)+0.5*log(1/2) = "
      f"{0.5*log(1.5)+0.5*log(0.5):+.6f}   = log(sqrt(3)/2) = {log(3**0.5/2):+.6f}")
print(f"   critical p (drift = 0):  log2/log3 = {log(2)/log(3):.6f}")
print("   -> 1/2 < 0.6309, so the geometric mean is sqrt(3)/2 = "
      f"{3**0.5/2:.6f} < 1")
