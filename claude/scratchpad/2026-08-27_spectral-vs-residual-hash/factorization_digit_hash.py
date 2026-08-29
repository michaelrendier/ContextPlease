#!/usr/bin/env python3
"""
factorization_digit_hash.py

Same trailing-digit metric, but the target is PRIME FACTORIZATION structure
instead of a yes/no primality bit.

Trailing k decimal digits = N mod 10^k, which fully pins the 2-adic and
5-adic valuations of N (v2, v5) -- i.e. the part of N's factorization built
from the prime factors OF THE BASE (10 = 2*5) -- and NOTHING coprime to 10.

So the prediction:
  - targets that ARE the {2,5}-part  -> normalised MI -> 1 within a few digits
  - Omega, omega, smallest-prime-factor -> JUMP at k=1 (the 2,5 contribution)
    then FLAT PLATEAU (the coprime-to-10 part is global, invisible to a suffix)
  - Omega of the coprime-to-10 part -> ~0 at every k

Contrast run in base 30 (= 2*3*5): there the suffix-local primes should be
exactly {2,3,5}.
"""
import numpy as np

def run(LO, HI, base, kmax, label):
    n = HI - LO
    print(f"\n=== {label}: [{LO:,},{HI:,})  base {base}  ({n:,} ints) ===")
    # smallest-prime-factor sieve
    spf = np.zeros(HI, dtype=np.int32)
    for p in range(2, int(HI**0.5) + 1):
        if spf[p] == 0:
            spf[p:HI:p][spf[p:HI:p] == 0] = p
    spf[spf == 0] = np.arange(HI)[spf == 0]  # primes: spf = self
    spf[:2] = [0, 1]

    N = np.arange(LO, HI, dtype=np.int64)
    Omega = np.zeros(n, np.int16)      # with multiplicity
    omega = np.zeros(n, np.int16)      # distinct
    v_base = np.zeros(n, np.int16)     # total valuation at the base's primes
    Omega_cop = np.zeros(n, np.int16)  # Omega of the part coprime to base
    spf_small = np.zeros(n, np.int16)
    prime_pow = np.zeros(n, bool)
    squarefree = np.ones(n, bool)

    base_primes = []
    b = base
    d = 2
    while d * d <= b:
        if b % d == 0:
            base_primes.append(d)
            while b % d == 0:
                b //= d
        d += 1
    if b > 1:
        base_primes.append(b)
    base_primes = set(base_primes)

    for i in range(n):
        m = int(N[i])
        first = spf[m] if m >= 2 else 0
        spf_small[i] = first if first <= 97 else 999
        distinct = 0
        tot = 0
        last_p = 0
        while m > 1:
            p = spf[m]
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            distinct += 1
            tot += e
            if e >= 2:
                squarefree[i] = False
            if p in base_primes:
                v_base[i] += e
            else:
                Omega_cop[i] += e
            last_p = p
        Omega[i] = tot
        omega[i] = distinct
        prime_pow[i] = (distinct == 1)

    def mi_norm(feat, tgt):
        # I(feat;tgt)/H(tgt), both integer-coded
        vals, tcode = np.unique(tgt, return_inverse=True)
        K = len(vals)
        if K < 2:
            return 0.0
        pt = np.bincount(tcode, minlength=K) / len(tcode)
        Ht = -np.sum(pt[pt > 0] * np.log2(pt[pt > 0]))
        order = np.argsort(feat, kind="stable")
        f = feat[order]; tc = tcode[order]
        bnd = np.flatnonzero(np.diff(f)) + 1
        starts = np.concatenate(([0], bnd)); ends = np.concatenate((bnd, [len(f)]))
        Hcond = 0.0
        M = len(f)
        for s, e in zip(starts, ends):
            w = (e - s) / M
            c = np.bincount(tc[s:e], minlength=K)
            pp = c / c.sum()
            pp = pp[pp > 0]
            Hcond += w * (-np.sum(pp * np.log2(pp)))
        return (Ht - Hcond) / Ht

    targets = [
        ("v_base (2,5 or 2,3,5 part)", v_base),
        ("Omega (w/ multiplicity)", Omega),
        ("omega (distinct)", omega),
        ("Omega of coprime-to-base part", Omega_cop),
        ("smallest prime factor", spf_small),
        ("squarefree?", squarefree.astype(np.int8)),
        ("prime power?", prime_pow.astype(np.int8)),
    ]
    hdr = "  ".join(f"k={k}" for k in range(1, kmax + 1))
    print(f"  {'target':32s} | last-k: {hdr}   | first-k(k={kmax})")
    print("  " + "-" * 78)
    for name, tgt in targets:
        lastvals = []
        for k in range(1, kmax + 1):
            lastvals.append(mi_norm((N % base**k).astype(np.int64), tgt))
        D = len(np.base_repr(HI - 1, base))
        first_k = mi_norm((N // base**(D - kmax)).astype(np.int64), tgt)
        row = "  ".join(f"{v:.3f}" for v in lastvals)
        print(f"  {name:32s} | {row}   | {first_k:.3f}")


run(10_000_000, 20_000_000, 10, 5, "prime factorization vs trailing decimal digits")
run(10_000_000, 20_000_000, 30, 4, "contrast: base 30 (= 2*3*5)")
print("\nread: JUMP at k=1 then FLAT => only the base's own prime factors are")
print("      suffix-local; everything coprime to the base is global.")
