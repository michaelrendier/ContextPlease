#!/usr/bin/env python3
"""
un_sieve.py — the recursive UN-sieve: what order do the composites ARRIVE
(are born, defined by existence) rather than fall (go extinct)?

Ground state: "Just Prime Numbers" — only primes exist, no composites.
Turn primes on one at a time; a composite is BORN the moment its LAST needed
prime factor is turned on.

Four orders over integers 2..N:

  A  extinction, low→high   gen = rank_asc(spf(n))   — the classic sieve
  B  extinction, high→low   gen = rank_desc(gpf(n))  — strike big primes first
  C  birth,      low→high   gen = rank_asc(gpf(n))   — un-sieve, primes ascending
  D  birth,      high→low   gen = rank_desc(spf(n))  — un-sieve, primes descending

Predictions (Cody):
  • D mirrors A exactly (same partition by spf, generation index reversed).
  • C is NOT a simple mirror — birth-by-gpf vs death-by-spf is asymmetric;
    the difference is the fine structure / mass-gap-analog residual.
  • extinction "finishes" at the largest prime with p² ≤ N (√N);
    birth "finishes" at the largest prime with 2p ≤ N (N/2). That gap is
    itself a residual.
"""
from __future__ import annotations
import math

N = 100_000


def spf_gpf(N):
    """least and greatest prime factor for every n ≤ N, linear sieve."""
    spf = [0] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > N:
                break
            spf[i * p] = p
    gpf = [0] * (N + 1)
    for n in range(2, N + 1):
        m, g = n, 1
        while m > 1:
            p = spf[m]
            g = p
            while m % p == 0:
                m //= p
        gpf[n] = g
    return spf, gpf, primes


def entropy(hist):
    tot = sum(hist)
    if tot == 0:
        return 0.0
    h = 0.0
    for c in hist:
        if c:
            q = c / tot
            h -= q * math.log2(q)
    return h


def main():
    spf, gpf, primes = spf_gpf(N)
    pi = {p: i for i, p in enumerate(primes)}       # 0-indexed ordinal
    P = len(primes)
    asc = lambda p: pi[p]                            # rank low→high
    desc = lambda p: P - 1 - pi[p]                   # rank high→low
    comps = [n for n in range(4, N + 1) if spf[n] != n]

    print(f"N = {N:,}   primes ≤ N: {P:,}   composites: {len(comps):,}\n")

    orders = {
        "A  extinction low→high  rank_asc(spf)":  [asc(spf[n]) for n in comps],
        "B  extinction high→low  rank_desc(gpf)": [desc(gpf[n]) for n in comps],
        "C  birth      low→high  rank_asc(gpf)":  [asc(gpf[n]) for n in comps],
        "D  birth      high→low  rank_desc(spf)": [desc(spf[n]) for n in comps],
    }
    hists = {}
    for name, gens in orders.items():
        h = [0] * P
        for g in gens:
            h[g] += 1
        hists[name] = h
        first_nonzero = next(i for i, c in enumerate(h) if c)
        last_nonzero = max(i for i, c in enumerate(h) if c)
        print(f"{name}")
        print(f"    generations used : [{first_nonzero} .. {last_nonzero}]  "
              f"of {P}")
        print(f"    entropy          : {entropy(h):.4f} bits")
        print(f"    pass-0 share     : {h[0]/len(comps)*100:.1f}%   "
              f"(top pass strikes/births this fraction)")
        print()

    # ── D mirrors A? ──
    A = [asc(spf[n]) for n in comps]
    D = [desc(spf[n]) for n in comps]
    mirror_ok = all(D[i] == P - 1 - A[i] for i in range(len(comps)))
    print(f"D == reverse(A) exactly (birth high→low mirrors extinction low→high): "
          f"{mirror_ok}")
    print(f"H(A) = H(D) = {entropy(hists['A  extinction low→high  rank_asc(spf)']):.4f} bits "
          f"(mirror preserves entropy)\n")

    # ── C vs A — the residual / fine structure ──
    hA = hists["A  extinction low→high  rank_asc(spf)"]
    hC = hists["C  birth      low→high  rank_asc(gpf)"]
    hCrev = list(reversed(hists["B  extinction high→low  rank_desc(gpf)"]))
    print("C vs A — birth-by-gpf against death-by-spf (both low→high):")
    print(f"    H(C) − H(A) = {entropy(hC) - entropy(hA):+.4f} bits "
          f"(the birth order spreads the same info wider)")
    # where the two histograms diverge most
    resid = [(g, hC[g] - hA[g]) for g in range(min(80, P))]
    big = sorted(resid, key=lambda t: -abs(t[1]))[:8]
    print("    largest residuals hC(g) − hA(g) over the first 80 generations:")
    for g, r in sorted(big):
        p = primes[g]
        print(f"      gen {g:>3} (prime {p:>4}) : {r:+7d}")
    print()

    # ── the two boundary primes ──
    ext_boundary = max(p for p in primes if p * p <= N)
    birth_boundary = max(p for p in primes if 2 * p <= N)
    print("boundary primes:")
    print(f"    extinction completes at  p² ≤ N  →  p = {ext_boundary}  "
          f"(π = {pi[ext_boundary]+1}) — the '{ext_boundary} Sieve'")
    print(f"    birth      completes at  2p ≤ N  →  p = {birth_boundary}  "
          f"(π = {pi[birth_boundary]+1})")
    print(f"    the sieve finishes KILLING at √N = {int(math.isqrt(N))}, "
          f"finishes BIRTHING at N/2 = {N//2}.")
    gap_births = sum(1 for n in comps if gpf[n] > ext_boundary)
    print(f"    composites born after the extinction boundary "
          f"(gpf > {ext_boundary}): {gap_births:,}  "
          f"({gap_births/len(comps)*100:.1f}% of all composites) — the residual.")


if __name__ == "__main__":
    main()
