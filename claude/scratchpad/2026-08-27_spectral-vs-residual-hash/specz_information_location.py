#!/usr/bin/env python3
"""
specz_information_location.py  (v2, vectorised sieve)

Information location over Spec Z: normalised MI( T ; N mod p^k ) / H(T)
for each target T, prime p, depth k.

  T = isprime -> flat small per-prime contribution  => GLOBAL / hash-like
  T = spf     -> steep concentration on small primes => LOCAL
  T = Omega / omega -> in between
"""
import numpy as np

LO, HI = 2_000_000, 12_000_000
n = HI - LO
print(f"window [{LO:,},{HI:,})  ({n:,} ints)\n")

# ---- SPF sieve (stride only to sqrt) ----
spf = np.zeros(HI, np.int64)
for p in range(2, int(HI**0.5) + 1):
    if spf[p] == 0:
        blk = spf[p*p::p]
        blk[blk == 0] = p
isprime_full = (spf == 0)
isprime_full[:2] = False
spf[isprime_full] = np.nonzero(isprime_full)[0]
spf[:2] = 0

# ---- omega / Omega via prime loop ----
primes_all = np.nonzero(isprime_full)[0]
omega = np.zeros(HI, np.int8)
Omega = np.zeros(HI, np.int8)
for p in primes_all:
    omega[p::p] += 1
    pe = int(p)
    while pe < HI:
        Omega[pe::pe] += 1
        pe *= p
print(f"sieve done: {len(primes_all):,} primes < {HI:,}")

N = np.arange(LO, HI)
T_isprime = isprime_full[LO:HI].astype(np.int64)
T_spf = spf[LO:HI]
T_Omega = np.clip(Omega[LO:HI].astype(np.int64), 0, 12)
T_omega = np.clip(omega[LO:HI].astype(np.int64), 0, 8)
print(f"prime density {T_isprime.mean():.4f}   mean Omega {Omega[LO:HI].mean():.2f}"
      f"   mean omega {omega[LO:HI].mean():.2f}\n")


def Hd(c):
    p = c / c.sum(); p = p[p > 0]; return -np.sum(p * np.log2(p))


def mi_norm(residue, P, target, K):
    tot = np.bincount(target, minlength=K)
    Ht = Hd(tot)
    if Ht == 0:
        return 0.0
    j = np.bincount(residue.astype(np.int64) * K + target, minlength=P * K).reshape(P, K)
    rc = j.sum(1)
    Hc = 0.0
    for r in range(P):
        if rc[r]:
            Hc += (rc[r] / n) * Hd(j[r])
    return (Ht - Hc) / Ht


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
DEPTHS = [1, 2, 3]

spf_classes = np.array(PRIMES + [10**9])
spf_code = np.searchsorted(spf_classes, T_spf, side="left")
spf_code[T_spf > 47] = len(PRIMES)
K_spf = len(spf_classes)

targets = [
    ("isprime", T_isprime, 2),
    ("spf (capped @47)", spf_code, K_spf),
    ("Omega", T_Omega, 13),
    ("omega", T_omega, 9),
]

for name, tgt, K in targets:
    print(f"--- {name} : normalised MI( T ; N mod p^k ) ---")
    print("    p  |   k=1     k=2     k=3")
    persum = 0.0
    for p in PRIMES:
        row = [mi_norm(N % (p**k), p**k, tgt, K) for k in DEPTHS]
        persum += row[0]
        print(f"  {p:3d}  | " + "  ".join(f"{v:.4f}" for v in row))
    print(f"  sum of k=1 column over these 15 primes: {persum:.3f}")
    # cumulative primorial
    prim = 1; cum = []
    for p in PRIMES:
        prim *= p
        if prim > 3_000_000:
            break
        cum.append((p, mi_norm(N % prim, prim, tgt, K)))
    print("  cumulative MI( T ; N mod primorial ): "
          + "  ".join(f"<={p}:{v:.3f}" for p, v in cum))
    print()
