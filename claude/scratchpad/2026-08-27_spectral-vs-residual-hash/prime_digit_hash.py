#!/usr/bin/env python3
"""
prime_digit_hash.py

Metric: how many digits from the END of a number are needed to know it's prime?

If primes are HASH-LIKE in the decimal representation, then knowing the last k
digits should carry ONLY the mod-2 / mod-5 information (killed at k=1) and then
a FLAT PLATEAU -- because primality's dependence on every other prime divisor
is a function of the WHOLE number, not any suffix. A gradual climb instead
would mean the suffix leaks partial primality info.

Measured: normalised mutual information  I(isprime ; N mod 10^k) / H(isprime)
for k = 1..6, over a window of integers, with:
  - last  k digits   (N mod 10^k)
  - first k digits   (N // 10^(D-k))
  - k digits from the middle
plus the divisibility baseline  I(coprime-to-10 ; last k digits).
"""
import numpy as np

LO, HI = 10_000_000, 40_000_000          # 3e7 integers, D = 8 digits
print(f"window [{LO:,}, {HI:,})   ({HI-LO:,} integers)")

# ---- sieve ----
sieve = np.ones(HI, dtype=bool)
sieve[:2] = False
for p in range(2, int(HI**0.5) + 1):
    if sieve[p]:
        sieve[p*p::p] = False
N = np.arange(LO, HI, dtype=np.int64)
isprime = sieve[LO:HI]
del sieve
nprime = int(isprime.sum())
print(f"primes in window: {nprime:,}  (density {nprime/len(N):.4f}, "
      f"1/ln x = {1/np.log((LO+HI)/2):.4f})\n")


def H(bits):
    p = bits.mean()
    if p <= 0 or p >= 1:
        return 0.0
    return -(p*np.log2(p) + (1-p)*np.log2(1-p))


def mi_norm(feature, target):
    """I(feature; target) / H(target), feature integer-coded, target bool."""
    Ht = H(target)
    if Ht == 0:
        return 0.0
    order = np.argsort(feature, kind="stable")
    f = feature[order]; t = target[order]
    # boundaries between distinct feature values
    bnd = np.flatnonzero(np.diff(f)) + 1
    starts = np.concatenate(([0], bnd))
    ends = np.concatenate((bnd, [len(f)]))
    n = len(f)
    Hcond = 0.0
    for s, e in zip(starts, ends):
        w = (e - s) / n
        pp = t[s:e].mean()
        if 0 < pp < 1:
            Hcond += w * (-(pp*np.log2(pp) + (1-pp)*np.log2(1-pp)))
    return (Ht - Hcond) / Ht


D = len(str(HI - 1))
coprime10 = (N % 2 != 0) & (N % 5 != 0)

print(f"{'k':>2} | {'last-k':>8} {'first-k':>8} {'mid-k':>8} | {'coprime10|last-k':>16}")
print("-" * 56)
for k in range(1, 7):
    last_k = (N % (10**k)).astype(np.int64)
    first_k = (N // (10**(D - k))).astype(np.int64)
    midpos = (D - k) // 2
    mid_k = ((N // (10**midpos)) % (10**k)).astype(np.int64)
    mi_last = mi_norm(last_k, isprime)
    mi_first = mi_norm(first_k, isprime)
    mi_mid = mi_norm(mid_k, isprime)
    mi_cop = mi_norm(last_k, coprime10)
    print(f"{k:>2} | {mi_last:8.4f} {mi_first:8.4f} {mi_mid:8.4f} | {mi_cop:16.4f}")

print("\nread:")
print("  last-k jump at k=1 then FLAT  => primes are hash-like in the suffix")
print("  (all primality info beyond mod-2,5 lives in the whole number)")
print("  coprime10|last-k should hit 1.00 immediately (pure divisibility)")

# --- the actual 'how many digits' answer, as a classifier accuracy ---
print("\nclassifier: predict prime from last k digits (P(prime|suffix) > 0.5 rule)")
base_acc = max(isprime.mean(), 1 - isprime.mean())
print(f"  baseline (always 'composite'): {base_acc:.4f}")
for k in (1, 2, 3, 4, 6):
    key = (N % (10**k)).astype(np.int64)
    order = np.argsort(key, kind="stable")
    ks = key[order]; ts = isprime[order]
    bnd = np.flatnonzero(np.diff(ks)) + 1
    starts = np.concatenate(([0], bnd)); ends = np.concatenate((bnd, [len(ks)]))
    correct = 0
    for s, e in zip(starts, ends):
        pp = ts[s:e].mean()
        correct += (e - s) * (pp if pp > 0.5 else 1 - pp)
    print(f"  k={k}: accuracy {correct/len(N):.4f}   "
          f"(lift over baseline {correct/len(N) - base_acc:+.4f})")
