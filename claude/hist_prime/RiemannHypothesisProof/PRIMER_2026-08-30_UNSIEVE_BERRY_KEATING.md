# CONTEXT PRIMER — the recursive un-sieve, and the Berry-Keating flesh-out

**2026-08-30 · Claude Sonnet 5.** Two pieces of work across five repos, all
from one measurement.

Engine: `FactoralDecomposition/engine/lineage.py::un_sieve` (new; companion to
`sieve_lineage`). Scratchpad + full output:
`ContextPlease/claude/scratchpad/2026-08-30_prime-dna/` (`un_sieve.py`,
`prime_dna.py`).

---

## 1. The recursive un-sieve — birth order vs extinction order

`sieve_lineage` watches composites **fall** — die on the pass of their
smallest prime, `generation(n) = π(spf(n))`. The un-sieve watches them
**arrive**, from the ground state *"Just Prime Numbers"*: turn primes on one
at a time, a composite is born when its last needed prime is switched on.

**Four orders, N = 10⁵ (90 407 composites):**

| | reading | key | entropy | gen. range | top pass |
|---|---|---|---|---|---|
| A | extinction low→high | `rank_asc(spf)` | 2.491 b | [0…64] | 55.3% |
| B | extinction high→low | `rank_desc(gpf)` | 9.685 b | [4459…9591] | — |
| C | birth low→high | `rank_asc(gpf)` | 9.685 b | [0…5132] | — |
| D | birth high→low | `rank_desc(spf)` | 2.491 b | [9527…9591] | — |

**Confirmed (Cody's predictions):**
- **`D == reverse(A)` exactly** — bit for bit over all 90 407 composites;
  `H(A) = H(D)`, the reflection preserves entropy. `B == reverse(C)` likewise.
  Birth high→low **mirrors** extinction low→high.
- **C is not a mirror.** `H(C) − H(A) = +7.19 bits` — same composites, same
  information, spread over ~5 000 generations instead of 65. Residual `hC−hA`:
  big negative front at the small primes (`p=2: −49 984`, decaying through
  `p=13`), small positive ripples at mid primes (`p=47: +593`, `p=61: +591`).
  The §D.2 fine-structure shape, from the construction side.
- **Two boundary primes.** Extinction completes at the largest prime with
  `p²≤N` = **313** (the "313 Sieve"). Birth completes at the largest prime
  with `2p≤N` = **49 999**. The sieve finishes KILLING at `√N` but does not
  finish BIRTHING until `N/2`. **60.5%** of every composite is born after the
  extinction boundary — decided by primes that strike nothing. The `√N` vs
  `N/2` scale gap is the construction-side shadow of a mass gap.

**The split (Cody, 2026-08-30):** *"factoring to extinction is free…
factoring to existence is not free."* Defining a number by **what it cannot
be** needs only its smallest prime — bounded, front-loaded, bought with
primes ≤ `√N`. Defining it by **what it is** needs every prime factor present
— `+7.19 bits`, not done until `N/2`. ζ describes by exclusion (through the
zeros) — the cheap side. Construction is the priced side; the un-sieve is
where it is paid. Same as the 08-28 addendum §A descriptive-vs-definitional
pair, now with a price on it.

**Zeta as ground state / a Zeta Hamiltonian for free.** The un-sieve from
"Just Prime Numbers" is a *path* — generation the time coordinate, `dN/dg` the
velocity. ζ describes that ground state. Mechanics are mechanics: a path /
Lagrangian description Legendre-transforms to a Hamiltonian one, so the
*existence* of a Zeta Hamiltonian is licensed with no new maths; pinning its
exact form is the same open problem as Berry–Keating.

---

## 2. The Berry-Keating flesh-out — `RiemannHypothesisProof/PAPER.md §2.4`

One paragraph → five subsections:

- **2.4.1 Hilbert–Pólya lineage** — Montgomery (1973) pair correlation → GUE
  (Dyson), Odlyzko numerics, Berry (1986): GUE = chaotic Hamiltonian, no
  time-reversal.
- **2.4.2 Why H = x p** — the semiclassical count
  `N_BK(E) = E/2π·(ln(E/2π)−1) + 7/8` is term-for-term the Riemann–von
  Mangoldt smooth term (leading term, the −1, the 7/8). Eq (2.1)–(2.4).
- **2.4.3 Why it is still open** — `Ĥ_BK = −i(x∂_x + ½)` on L²(0,∞) has
  continuous spectrum (all of ℝ). Five proposals to force discreteness — BK
  cutoffs, Connes (absorption spectrum / Weil positivity), Sierra–Townsend
  `√x̂ p̂ √x̂`, Bender–Brody–Müller PT-symmetric, BK 2011 — none proven to
  give exactly `{γ_n}`.
- **2.4.4 What the paper needs** — only the equivalence (the Ainulindale
  Hypothesis), not the operator. A **three-bearings** table: Noether current
  (from the symmetry), semiclassical `xp` (from the count), the un-sieve
  (from the construction — a Zeta Hamiltonian by Legendre, no new maths, plus
  the `√N`-vs-`N/2` mass-gap shape the spectrum must reproduce).
- **2.4.5 The identification (Cody):** **Zeta Hamiltonian = ∅_RB** (the
  RedBlue system of §4); **Zeta Lagrangian = L_(I|O)** (the Two-Trees
  intertwiner, `U H_Red = H_Blue U`); **ζ = the on-shell action** recording
  their trajectory. Concretely the Riemann–Siegel theta
  `θ(t) = arg Γ(¼+it/2) − (t/2)ln π` **is** `S_cl(t) = ∫ L_(I|O) dt` along
  the ∅_RB orbit; `ζ(½+it) = 2 Σ_{n≤√(t/2π)} n^{−½} cos(θ(t) − t ln n) + R(t)`
  is the stationary-phase sum over classical paths; the **zeros are its saddle
  points** = the stable equilibria where `J(σ,E) = 0`.

---

## 3. Where it all landed

- `FactoralDecomposition/engine/lineage.py` — `un_sieve(N)` (remote still
  `SedenionFactoralRelativity`).
- `RiemannHypothesisProof/` — `PAPER.md §2.4` rewritten;
  `ADDENDUM_recursive_unsieve_2026-08-30.md` (companion to the 08-28
  generational-lineage addendum §D).
- `ValaQuenta/wiki/un_sieve.md` — Telperion (extinction, free) / Laurelin
  (birth, priced), the mirror, the residual, the split.
- `Ainulindale/wiki/47_the_two_trees.md` — new "counter-rotate — measured"
  + "the split" sections.
- `AbrikosovTree/README.md` — the residual as the silver-leaf population;
  winding number set at birth (Laurelin's book).

None of it claims a proof or closes C1. It adds a construction-side residual,
a price on the exclusion-vs-construction split, and a no-new-maths route to a
Zeta Hamiltonian identified with ∅_RB / L_(I|O).

See `RiemannHypothesisProof/ADDENDUM_generational_lineage_2026-08-28.md`,
`ContextPlease/claude/scratchpad/2026-08-30_prime-dna/`,
[[project-two-trees-lio]], [[project-null-operator-rb]],
[[project-factoral-decomposition-tool]].
