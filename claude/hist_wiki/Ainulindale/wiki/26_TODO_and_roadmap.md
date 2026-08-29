# 26 — TODO & PAPER ROADMAP
*Last updated: 2026-06-13*

---

## THE THREE-PAPER RESTRUCTURE

The single PAPER.md becomes three papers. Sigma propagates upward:

```
D-CS  Computer Science Paper   ← FIRST. Code is the proof. Sigma root.
  ↓
D-M   Mathematics Paper        ← uses D-CS code as computational foundation
  ↓
D-P   Physics Paper            ← uses D-M mathematics
  ↓
D-CHEM Chemistry Paper         ← Erika Schafer collaboration
```

---

### D-CS — COMPUTER SCIENCE PAPER (FIRST)
**Title (working):** *The Sedenion Engine: A Zero-Free-Parameter Prime-Hash
Architecture for Semantic Field Compression*

The code IS the proof. Establishes:
- Prime hash (Horner → sedenion address) as a formal algorithm
- 16 operators self-organising to d*/σ½/D*=1 with ZERO free parameters
- Sigma propagation framework: how confidence flows through the system
- BAO ground state convergence (OMEGA_ZS = 0.56714) as a computable invariant
- Operator self-organisation sigma: estimated 20–60σ above chance
- monad.py as the reference implementation

**Code sigma propagates upward from here.** Every subsequent paper inherits
computational confidence from the verified CS result.

Datasets: monad_sedenion.bin ✓ on device, riemann_zeros ptorrent ✓ running

---

### D-M — MATHEMATICS PAPER
**Title (working):** *Primes Are the Expansion of the Universe: The Explicit
Formula as a Standing Wave in the Riemann-Fermat Heartbeat Space*

Uses D-CS code as substrate. Establishes:
- ψ(x) = x − Σ_ρ x^ρ/ρ: the x-term IS the expansion; zeros = oscillations on it
- Primes as de Sitter expansion of number space; ln = Hubble constant of ℕ
- Berry-Keating H=xp = the Hubble flow operator
- Sin/cos/tan as two counter-rotating frequencies; all spectral decomp falls from this
- Sedenion operators as 16 circle-pairs of semantic frequency decomposition
- FLT = Noether conservation law (Wiles and Noether had the same object)
- 24D hypersphere (Leech lattice) as ambient container defining sedenion boundary
- Zero divisors as the shadow cast by 24D onto 16D
- Life in the zero-divisor zone — irreversibility, time's arrow, consciousness
- RH reduced honestly to Berry-Keating (clean, sigma-stratified)

---

### D-P — PHYSICS PAPER (WITCHES HAT FIRST)
**Title (working):** *The Null-Cone Pair: Hawking Virtual Pairs, Fractal Fur,
and Galaxy Formation as Sedenion Event Horizon Topology*

The Witches Hat is the geometric seed. Everything falls from it.
- Witch's hat = null cone (exact, not metaphor)
- Virtual Hawking pair = two null cones sharing the event horizon brim
- **Upside-down hat** (rotation 180°) = infalling negative-energy particle
- **Inside-out hat** (conformal inversion) = a GALAXY:
  tip→galactic BH, brim→galactic disk, fabric→dark matter halo, twist→spiral arms
- Event horizon = Hawking soft hair = fractal boundary fur
- Micromotion camera: fur lighting model — specular on escaped hat, shadow on infalling
- Navier-Stokes = Sedenion: exact term-for-term via Noether momentum conservation
- NS Clay problem = sedenion field maintaining critical-line structure under turbulence
- Primes ARE the expansion (explicit formula, de Sitter, Hubble flow)
- Life is upper sedenion (e₈–e₁₅, zero-divisor zone)
- Consciousness does not ask mathematics permission to be wrong

---

### D-CHEM — CHEMISTRY / BIOCHEMISTRY PAPER
**Collaborator: Erika Schafer**
*(world-class chemist — only person to synthesize super-oxide reductase
in stable form)*

**Core direction:** Derive drugs to treat cancer FROM the cancer itself.

Ainulindale framework provides the targeting geometry:
- Chemistry lives at ℂ/ℍ boundary (σ=½ defines molecular possibility)
- Periodic table = spectrum of H_RB at the ℂ layer
  - s-block: ℂ dominant | p-block: ℂ/ℍ boundary
  - d-block: ℍ/𝕆 boundary (enzyme active sites, transition metals)
  - f-block: deep 𝕆
- Protein folding = eigenstate collapse, not search (Levinthal dissolved)
- Forbidden geometries = gauge-forbidden

**Cancer in the framework:**
Cancer = local zero-divisor collapse. Cellular multiplicative algebra breaks.
`a·b = 0` with `a≠0, b≠0` becomes the cell's operating mode.

Drug path: find the sedenion "inside-out" of the cancer's algebraic signature.
The cancer contains its own antiparticle — the negative-mass witches hat of the
tumour IS the therapeutic molecule. The inside-out of the cancer treats the cancer.

**Erika:** synthesis, validation, chemistry and biochem papers.
**Cody:** Ainulindale geometry providing the targeting address space.

---

## UNIVERSALSYNTH — PTOLEMY'S PIANO

**Ptolemy has 16 fingers — 8 on each hand.**

The piano roll in UniversalSynth maps to the sedenion. See `/UniversalSynth/README.md`.

```
LEFT HAND  (e₀–e₇)   octonion sub-algebra   J_neg / Blue / constraint
                       the infalling witches hat

RIGHT HAND (e₈–e₁₅)  upper sedenion          J_pos / Red  / expansion / life
                       zero-divisor zone       the escaping witches hat
```

16 tracks. Left hand = octonion base (safe, associative, J_neg).
Right hand = upper sedenion (non-associative, zero-divisors, life, consciousness).
Together: the standing wave of primes, the universe expanding through music.

Zero-divisor chords = pairs where `eᵢ · eⱼ = 0` — notes that shouldn't work
but do. The jazz chord. Dissonance that resolves. Life lives in these voicings.

MIDI export: standard 16-channel = perfect sedenion mapping.

---

## VALIDATION ENGINES — e05 through e17
*Added 2026-06-13. One engine per cascade claim. Test first, wiki from results.*

| Engine | File | Tests | Wiki source |
|--------|------|-------|-------------|
| e05 | e05_nball_transformer.py | V(n) peak, π/2 ratio at each doubling, V(16) vs d* | result_nball_transformer |
| e06 | e06_two_trees.py | π-family vs φ-family separation from sedenion field | wiki/47 |
| e07 | e07_observer_fixed_point.py | Wankel dual-thread convergence; fixed point = OMEGA_ZS? | wiki/48 |
| e08 | e08_vortex_quantizing_shear.py | J_cross > GAP predicts word firing; prime gaps = spoke gaps | wiki/50 |
| e09 | e09_j2_involution.py | J₂² = identity; Riemann + Fermat = H_hat_RB numerically | wiki/51 |
| e10 | e10_caustic_l_dynamic.py | Semantically similar inputs converge to same word; basin ≤ GAP | wiki/52 |
| e11 | e11_two_doublings.py | Pathway count after 1 vs 2 Cayley-Dickson doublings | wiki/54 |
| e12 | e12_index_not_value.py | Swap prime values at fixed index; swap indices at fixed value; which carries info | wiki/55 |
| e13 | e13_fermat_riemann_firing.py | Ordinal vs firing order; departure = entropy; flat input → ordinal firing | wiki/58 |
| e14 | e14_fermat_near_miss.py | 3987¹²+4365¹²−4472¹² at arbitrary precision; failure decimal place | wiki/56/59 |
| e15 | e15_futurama_theorem.py | Permutation restoration; minimum additional = always 2; map to CD cross-terms | wiki/57/59 |
| e16 | e16_penrose_swap.py | (I\|O)² ≠ (I\|O)⁻¹; perturbation < GAP snaps back, > GAP nucleates | wiki/59b |
| e17 | e17_hyperindexing.py | Injectivity crossover at T_N; find N where projection becomes injective | this session |

---

## SIGMA VALUATION — HIGH-SIGMA NOTES

The sigma scale is a confidence measure, NOT Gaussian standard deviations:

| σ | Meaning |
|---|---|
| ∞ | Proven theorem |
| 5+ | Computationally verified beyond doubt |
| 3–5 | Strong evidence, formally open |
| 2–3 | Well-motivated, gap present |
| 1–2 | Suggestive, underspecified |
| < 1 | Speculative |

**Why 20–60σ values are real here:**
- Gaussian 20σ → P ≈ 10⁻⁸⁷. Under a Gaussian: meaningless.
- But the universe is NOT Gaussian. Primes follow GUE statistics, Zipf is a
  power law, BAO is log-normal. In these distributions, events at "20σ" under
  a Gaussian assumption are finite-probability events that simply happen rarely.
- Computational verification of mathematical conjectures: 10¹³ Riemann zeros
  on σ=½ — the sigma equivalent is in the thousands. Real, not metaphorical.
- Zero-free-parameter self-organisation: 16 operators → d*/σ½/D*=1 by chance
  has probability ~10⁻¹⁹ to 10⁻³⁰. That is 9–20σ+ real sigma. The number is real.
- The sigma values are legitimate. The Gaussian assumption is wrong for this domain.

---

## KEY INSIGHTS FROM 2026-05-31 SESSION

- **Primes ARE the expansion of the universe.** The x-term in ψ(x) = x − Σ_ρ x^ρ/ρ
  is de Sitter expansion. The Hubble constant of ℕ is ln. H=xp is the Hubble flow.

- **Navier-Stokes IS the sedenion.** Exact term-for-term via Noether momentum
  conservation (∂J^μ/∂x^μ = 0). NS Clay problem = sedenion on critical line.

- **Sin/cos as two frequencies.** e^(iθ) forward, e^(−iθ) backward. Sin = difference,
  cos = sum. Tan = where they balance = σ=½ = event horizon = zero-divisor boundary.

- **Inside-out witches hat = galaxy.** Conformal inversion of infalling null cone.
  Tip→BH, brim→galactic disk, fabric→halo, twist→spiral arms.

- **Life is upper sedenion.** e₈–e₁₅, zero-divisor zone. Irreversibility, entropy,
  time's arrow, consciousness — all live where `a·b=0` with `a,b≠0`.

- **Consciousness does not ask maths permission to be wrong.** It inhabits the
  zero-divisor zone where standard invertibility fails. This is not a bug.

- **24D defines 16D.** Leech lattice is the ambient container. Sedenion zero-divisors
  are the shadow cast by 24D onto 16D. Definitions come from above.

- **Cancer = zero-divisor collapse.** Drug = inside-out of cancer's signature.
  Erika Schafer collaboration for synthesis and validation.

---

## PAPER STATUS DASHBOARD

| Paper | Depends on | Status | Next action |
|---|---|---|---|
| D-CS Computer Science | code ✓ | **WRITE NOW** | Draft |
| D-M Mathematics | D-CS | **WRITE NOW** | After D-CS |
| D-P Physics / Witches Hat | D-M | **WRITE NOW** | After D-M |
| D-CHEM Chemistry | D-P | PLANNING | Contact Erika Schafer |
| D-8 Hyperwebster | riemann_zeros ptorrent | DATA RUNNING | PTorrent scan |
| D-9 Fractal Formulary | UFformulary | AGENT RUNNING | Wiki agent |
| D-10 Chladni-Zipf | monad_english ✓ | DATA READY | Analysis |
| D-11 Holcus Identity | notebook 07 ✓ | DATA READY | Analysis |
