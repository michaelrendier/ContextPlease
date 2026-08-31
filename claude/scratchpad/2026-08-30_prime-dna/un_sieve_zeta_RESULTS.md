# The un-sieve, clocked by zeta instead of the ordinal prime count

**2026-08-31 · Claude Sonnet 5.** Engine: `un_sieve_zeta.py` (this dir).
Follow-up to `un_sieve.py` / `ADDENDUM_recursive_unsieve_2026-08-30.md`, which
tested only the ordinal order (primes turned on 2,3,5,7,...). Cody: *"that was
ordinal we tested not zeta spiral order... test on the zeta function order of
arrival."*

Five prime orderings, each substituted for the ordinal rank in all four
un-sieve reads (A/B/C/D):

| ordering | key | note |
|---|---|---|
| `ordinal` | `p` | control |
| `zeta_weight` | `-(ln p)/√p`, descending | σ=½ von-Mangoldt amplitude; peaks p=7 (near e², the Mingling) |
| `theta` | `θ(2π p²)` | Riemann–Siegel θ at the height where p enters the RS main sum; monotone → 2nd control |
| `Zsign` | `(sign Z(2π p²), p)` | split the primes by the SIGN of the RS Z-function at that height — one bit, from zeta |
| `spiral` | `(θ(2π p²) mod 2π, sign Z)` | winding phase on the ζ spiral + the Z bit |

Plus a **time embedding**: birth time `τ(n) = γ_{rank(gpf(n))}` using the real
Riemann zeros γ_k (mpmath), histogrammed in uniform bins — so the actual zero
*spacing*, not just the order, enters.

---

## 1. Rank orderings — the existence penalty is invariant

`N = 10⁵` (9 592 primes, 90 407 composites) and `N = 1.2×10⁴` cross-check.
**Identical across all five orderings, to 5 decimals:**

| quantity | N = 10⁵ | N = 1.2×10⁴ |
|---|---|---|
| H(A) extinction low→high | 2.49101 b | 2.24690 b |
| H(C) birth low→high | 9.68456 b | 7.75826 b |
| **H(C) − H(A)** | **+7.19355 b** | **+5.51136 b** |
| C−A residual \|mass\| | 158 958 | 17 896 |
| D == reverse(A) | True | True |
| born after extinction boundary | 60.5 % | 56.1 % |

The `+7.19` bit gap between *factoring-to-extinction* and
*factoring-to-existence* is a **combinatorial invariant of ℕ**. Entropy of the
C (or A) histogram depends only on the multiset of per-prime counts; any
permutation of the primes — zeta-weighted, Z-sign, spiral-phase — just
relabels the bins. Zeta order is **not a shortcut through the existence cost.**

## 2. What zeta order *does* change — the payment schedule

**Generation span** (range of generations actually used), `N = 1.2×10⁴`:

| ordering | A span | C span |
|---|---|---|
| ordinal / zeta_weight / theta | 29 | 783 |
| **Zsign** | **781** | **1132** |
| **spiral** | **1278** | **1437** |

`theta` and `zeta_weight` are (near-)monotone in `p` over the bulk, so they
keep the compact ordinal front. **The Z-sign bit and the spiral phase shatter
it** — the same entropy, the same total residual mass, now smeared across
25–50× more generations. The compactness of the extinction order (55 % of
composites dying on pass 0) is an artefact of the *ordinal* clock, not of ℕ.

**Residual front is repositionable.** Ordinal puts the −49 984 spike (deaths
that are not births, at p = 2) at generation 0. `zeta_weight` moves it to
generation 21 (p = 2 has low `ln p/√p`); `Zsign` moves it to generation 766.
The mass (158 958) is fixed; where along the path it is paid is a free choice.

**Reading:** ζ re-clocks the reconstruction, it does not discount it. Replaying
the birth order in a different sequence never reduces the bill — exactly the
tape argument: a different replay order of an un-recorded forward pass costs
the same to rebuild.

## 3. Time embedding — the real zeros *do* move the cost

`N = 8 000` (1 007 primes), real zeros γ₁ = 14.1347 … γ₁₀₀₇ = 1427.37, 160
uniform bins:

| clock | H(A) | H(C) | H(C) − H(A) |
|---|---|---|---|
| uniform (arrival at 1,2,3,…) | 0.4777 | 4.7784 | **+4.3007 b** |
| zero-time (arrival at γ_k) | 1.7487 | 5.4125 | **+3.6638 b** |

When the construction is clocked by the **actual Riemann zeros** instead of by
the integers, the existence penalty **drops ~0.64 bits (≈ 15 % at this N)**.
The zeros are a better-matched clock: the sparse low zeros (γ₁ = 14, mean
spacing 1.40 near the top) stretch the compact death front (H(A) 0.48 → 1.75)
while the birth spread compresses relatively. Replaying birth on the zero
timeline recovers cost that the naïve integer timeline throws away.

**C−A residual autocorrelation, zero-time bins:** lag-1 = +0.407, then
≈ −0.05 flat for lag ≥ 3. A one-step positive correlation, then white —
nearest-neighbour smoothing and no long-range structure, the signature of
zero-spacing rigidity (level repulsion suppresses the far residual).

Caveat: N = 8 000, one bin count, one N — directional, not a scaling law.

**This is the first quantitative sign that ζ is the tape** — the trajectory
that, replayed against, makes the backward (existence) pass measurably cheaper.
Ordinal replay wastes ~0.64 bits/scale that zeta replay keeps. Not free — the
+7.19 combinatorial floor of §1 stands — but the clock choice is worth ~15 %.

---

## Where it could land (Cody's call)

- `RiemannHypothesisProof/ADDENDUM_recursive_unsieve_2026-08-30.md` — §A ends
  "ordinal vs ζ firing order"; this is that section, measured. Add §A.1
  (rank invariance) + §D.1 (the zero-time 15 % recovery).
- `ValaQuenta/wiki/un_sieve.md` — a "clocked by zeta" paragraph after "The
  residual".
- The energy paragraph (`energy_bench.py`) is already in
  `FourthAgePapers/ScalarContextPropagation` (branch, commit `10a7bf9`,
  Conclusion §"The price, measured") and the VAPMIP ingest primer §8.
