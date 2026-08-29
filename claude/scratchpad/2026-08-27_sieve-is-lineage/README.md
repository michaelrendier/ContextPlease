# The Sieve IS Generational Lineage — Fibonacci under factoring waves

Cody, 2026-08-27: *"The Sieve IS Generational Lineage... it's fibonacci under
factoring waves... the list of primes is the list of decompositional order...
the ordinal values... easy enough to test the sieve in both orderings."*

`sieve_lineage.py` — 7/7 checks PASS.

| claim | result |
|---|---|
| **C1** sieve pass order = lineage order: `generation(n) = π(spf(n))` | HOLDS, 182015/182015 |
| **C1** composites form a disjoint partition by first-mark pass | HOLDS |
| **C2** "one pass per prime": working passes = π(√N) = 86, exact | MATCH — single forward sweep, no iteration, no backtracking. *This is why the stability test was uniform.* |
| **C3** Legendre `φ(x,a) = φ(x,a−1) − φ(x/pₐ, a−1)` — Fibonacci's 2-term shape, 2nd term SCALE-shifted by a prime not index-shifted by 1 | HOLDS a=1..6 |
| **C4** closed form `φ = Σ_{d\|Pₐ} μ(d)⌊x/d⌋` = ADD∘SIGN∘SCALE (32 +, 32 −) | MATCH |
| **C5** final prime set + disjoint partition are ORDER-INVARIANT | same under ordinal / descending / zeta |
| **C5** `generation = π(spf)` is UNIQUE to the ordinal (ascending prime) order | HOLDS |

**Riemann-zeta ordering** (primes by `ln p/√p` descending, the σ=½ von-Mangoldt
term size) starts `[7, 11, 5, 13, 17, 19, 23, 3, 29]` — 2 comes late. It still
finds the same primes and still produces a disjoint partition, but the
generation map is scrambled and its entropy is higher (3.69 bits vs the
ordinal's 2.56; descending is 5.07). **The ordinal order is the canonical,
maximum-compression decomposition order** — pass 0 alone kills every even,
55% of all composites in one wave.

Verdict: Cody's bet holds. The sieve is the movement method through the factor
tree; the ordered prime list is the lineage; it is Fibonacci-shaped with a
multiplicative (factoring-wave) second term; and it decomposes cleanly onto
ADD/SCALE/SIGN.

Wired into: `VAPMIP/engines/e10_generational_lineage.py` (R10, R11),
`SedenionFactoralRelativity/engine/lineage.py` (`sieve_lineage`,
`sieve_recurrence`).
