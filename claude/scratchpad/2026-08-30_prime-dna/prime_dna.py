#!/usr/bin/env python3
"""
prime_dna.py — the ADD:SCALE:SIGN "DNA" of the prime numbers.

Reads the FactoralDecomposition generational-lineage engine (tested) and lays
its output out as a genome:

  • per integer n : which sieve wave strikes it (generation = π(spf(n))),
                    ω / Ω, and its factor lineage as a string of SCALE steps.
  • per prime p   : its ordinal index π(p), its Dirichlet WAVELENGTH 2π/p,
                    and its σ=½ von-Mangoldt spectral WEIGHT ln p / √p
                    (the "expression level" — peaks at p = 7).
  • the codon table: φ(x,a) = Σ_{d | Pₐ} μ(d)·⌊x/d⌋  =  ADD ∘ SIGN ∘ SCALE
                    — one signed, scaled term per squarefree product of the
                    first a primes. 2^a codons.

Not a proof. The generational-lineage ADDENDUM in RiemannHypothesisProof is a
second bearing on C1 (the open nodal-mode step), not a closer.
"""
from __future__ import annotations
import math, os, sys

_FD = os.path.expanduser("~/Projects/ThePlace/FactoralDecomposition")
if _FD not in sys.path:
    sys.path.insert(0, _FD)
from engine.lineage import sieve_lineage, sieve_recurrence   # tested engine

N = 64
A = 6                     # codon table over the first 6 primes (primorial 30030)


def _spf(n):
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            return p
    return n


def _factors(n):
    out, m, d = [], n, 2
    while d * d <= m:
        while m % d == 0:
            out.append(d); m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def main():
    sl = sieve_lineage(N, order="ordinal")
    gen = sl["generation_of"]                       # composite -> which wave
    primes = [k for k in range(2, N + 1) if _spf(k) == k]
    pi = {p: i + 1 for i, p in enumerate(primes)}   # π(p), 1-indexed

    print("=== engine check (FactoralDecomposition/engine/lineage.py) ===")
    print(f"  one pass per prime      : {sl['one_pass_per_prime']}  "
          f"(π(√{N}) = {sl['pi_sqrt_N']} working passes)")
    print(f"  generation = π(spf(n))  : {sl['generation_matches_pi_spf']}  "
          f"(exact over {sl['n_composites']} composites)")
    print()

    print(f"=== the genome — integers 2..{N} ===")
    print("  n   kind      gen  ω  Ω   lineage (÷ = one SCALE step)")
    print("  --  --------  ---  -  --  --------------------------------")
    for n in range(2, N + 1):
        fs = _factors(n)
        omega = len(set(fs)); Omega = len(fs)
        if len(fs) == 1:
            kind, g = "PRIME", pi[n]
            word = f"e₀ · p_{pi[n]}          (irreducible — the primer)"
        else:
            kind, g = "composite", gen[n]
            word = "1 " + " ".join(f"÷{p}" for p in fs) + f"  → {n}"
        print(f"  {n:>2}  {kind:<8}  {g:>3}  {omega}  {Omega:>2}  {word}")

    print()
    print("=== per-prime DNA: wavelength and expression level ===")
    print("   p   π(p)   wavelength 2π/p    weight ln p/√p   (bar)")
    print("  ---  ----   ---------------    -------------   " + "-" * 20)
    wmax = max(math.log(p) / math.sqrt(p) for p in primes)
    for p in primes:
        w = math.log(p) / math.sqrt(p)
        bar = "█" * round(40 * w / wmax)
        print(f"  {p:>3}  {pi[p]:>3}    {2*math.pi/p:>13.6f}    "
              f"{w:>10.6f}   {bar}")
    peak = max(primes, key=lambda p: math.log(p) / math.sqrt(p))
    print(f"  expression peaks at p = {peak}  "
          f"(the mid-sized primes are 'loudest' at σ = ½)")

    print()
    print(f"=== codon table: φ(x, {A}) = Σ_(d | P_{A}) μ(d)·⌊x/d⌋ "
          f"= ADD ∘ SIGN ∘ SCALE ===")
    sr = sieve_recurrence(x=30_030, a=A)
    print(f"  P_{A} (primorial)          : {sr['P_a']}")
    print(f"  recurrence exact          : {sr['recurrence_exact']}")
    print(f"  closed form Σ μ(d)⌊x/d⌋    : {sr['closed_form_sum_mu_floor']}  "
          f"(matches φ: {sr['closed_form_matches']})")
    print(f"  decomposition             : Σ_d → {sr['decomposition']['sum_d']} ; "
          f"μ(d) → {sr['decomposition']['mu(d)']} ; "
          f"⌊x/d⌋ → {sr['decomposition']['floor(x/d)']}")
    print(f"  {sr['fibonacci_note']}")
    print()
    print("  the two-term wave (Legendre): each prime folds φ in half —")
    print("   a  p_a    φ(x,a)      = φ(x,a-1) − φ(x/p_a, a-1)   [SCALE by p_a]")
    print("  --  ---  ----------    " + "-" * 40)
    for t in sr["recurrence_trace"]:
        print(f"  {t['a']:>2}  {t['p_a']:>3}  {t['phi']:>10}    "
              f"= {t['term1']:>10} − {t['term2_scaled']:>10}")


if __name__ == "__main__":
    main()
