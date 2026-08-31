# 2026-08-30 — the ADD:SCALE:SIGN "DNA" of the primes

Cody: *"I would like to see the 'DNA' of the prime numbers."* — this is that,
read off the **tested** FactoralDecomposition generational-lineage engine
(`engine/lineage.py`: `sieve_lineage`, `sieve_recurrence`).

`prime_dna.py` → `prime_dna_output.txt`. Three views:

1. **the genome** (integers 2..64) — per number: kind, *generation* =
   `π(spf(n))` (which sieve wave strikes it; 0 = the p=2 wave), ω / Ω, and
   the factor lineage as a string of SCALE steps. Primes = "the primer",
   irreducible, generation = their own ordinal index.
2. **per-prime DNA** — each prime's Dirichlet **wavelength** `2π/p` and its
   σ=½ von-Mangoldt **expression level** `ln p / √p`. **Peaks at p = 7**
   (0.7355); p = 2 is the quietest (0.4901). The mid-sized primes are loudest
   at the critical line — this is the D.2 weight from the RHP addendum.
3. **the codon table** — `φ(x,a) = Σ_(d|Pₐ) μ(d)·⌊x/d⌋ = ADD ∘ SIGN ∘ SCALE`.
   One signed, scaled term per squarefree product of the first a primes. The
   Legendre two-term recurrence shows each prime folding φ in half:
   30030 → 15015 → 10010 → 8008 → 6864 → 6240 → 5760.

## Status

- **Machinery: implemented and tested.** Engine check passes — one pass per
  prime, `generation = π(spf(n))` exact over all composites, recurrence
  exact, closed form matches.
- **Addendum: written.** `RiemannHypothesisProof/ADDENDUM_generational_lineage_2026-08-28.md`.
- **Not a proof.** Does **not** close C1 (mode identification, `TODO.md` — the
  central open problem). Cody's own framing: "a second bearing on it," "a
  moderately more simple understanding of the primes." ζ imports the zeros
  from outside; every other ζ operation is tier-0 ADD/SCALE/SIGN; that one
  import *is* the content of RH.
