# 133 — Canonical Maths (Ainulindalë)

**Written 2026-11-13.** The reference page for the maths the whole repository set uses: what each symbol means, which objects share a letter, what is established / measured / open, and where the full statement lives. It is a **reference, not a derivation**; derivations are in the files named. Wiki [131](131_riemann_canonical_maths.md) is the Riemann / Two-Trees chapter of this page and keeps its own full text.
Sources: `~/.clauderc_canonical_maths` (27 RCCM blocks; pull one with `source ~/.clauderc_ctx; rccm NAME`), `RiemannHypothesisProof` (RHP) docs and the primers `ContextPlease/claude/hist_prime/RiemannHypothesisProof/PRIMER_2026-11-{08,11,12}_*`, `VAPMIP/docs/wiki/J_red-J_blue-0_RB-Record.md`, wikis 17, 123, 127.
Maths in Unicode. Nothing here claims a Clay problem is solved; 0_RB is engineered maths and is not claimed to imply or subsume any established open programme.

**Authority order (Cody, 2026-11-11/12).** (1) Cody's current statement; (2) 0_RB as he specifies it; (3) the wikis and context files, which are **pointers to where things live, not always current information**. Where this page and a primer disagree, the primer's date and Cody's latest statement win, and the disagreement is listed in §7.

**Status labels.** `ESTABLISHED` literature · `MEASURED` / `:CALCULATED` computed here with code and tests · `READING` an interpretation, not a theorem · `THEORETICAL` · `CONJECTURE` · `OPEN`. Tier order ESTABLISHED > THEORETICAL > CONJECTURE > OPEN (RCCM `CONFIDENCE_TIERS`); a compound label takes its weakest tier.

---

## 0. Letters that collide (write the subscripted form; never a bare α, σ, Ω or d*)

| letter | the objects | write |
|---|---|---|
| **α / Α** | (1) the fine-structure constant 1/137.035999… of the Standard Model — here only the source of a discipline (a quantity must say the same thing in every version of the maths), not an ingredient of the horizon mechanism; (2) **Α_π = A_fermat**, the Fermat-side structural constant (capital Alpha) — **not α_fs**; (3) **α_NN**, the neural fine-structure constant, g²/(4πħ_NN ln r), defined to say the same thing at every tower layer; also the widget slider "Inertia (α)" | **α_fs**, **A_fermat**, **α_NN** |
| **σ** | (1) Re s, the Dirichlet/Euler coupling exponent, critical line σ = ½; (2) the σ-strata σ₀…σ₄ of the sedenion, ordinal nested-inclusion levels (σ₄ = string / ground state); (3) σ_RB[k] = ψ[k]·conj ψ[k⊕4], the oblique-gear tilt (Re) and axis (Im), and the derived scalar σ_self | **σ_ζ**, **σ-stratum**, **σ_RB** |
| **Ω** | (1) Ω_ζΣ = W(1) = 0.5671432904097838, the Lambert fixed point of x = e^{−x}; (2) ω_H = e^π = 23.1406926, the Gelfond / Hagedorn ceiling; (3) the "Entropy (Ω)" widget slider; (4) Ω(n), number of prime factors with multiplicity | **Ω_ζΣ**, **ω_H**, **Ω(n)** |
| **d\*** | five values, §2.2: Boundary, RG, taut, ln10 (the four faces) and the measured d*_spec | always subscripted |
| **0** | **0_RB** the Null Operator (an empty slot, never the numeral 0) · **0_RZ** Riemann zeros ρ = ½ + iγ · **0_ZD** zero divisors (a·b = 0, a, b ≠ 0) | RCCM `ZERO_QUALIFIERS` |
| **W** | Lambert W and its branches W₀, W₋₁ | W(0), W(1) = Ω_ζΣ, W(−1/e) = −1 |

**A_fermat — open item.** The original 2026-04-09 derivation puts it at the d = 0 endpoint (x = T/T_P = 1, the ceiling of the forward curve); wiki 17's older text puts it at 1/137.035999… as the "domain floor", which is how it was mistaken for α_fs. **Cody, 2026-11-13: A_fermat is the "chasing inertia" constant: it is what turned up when the search ran from the Fermat side of the maths. It is not α_fs.** That fixes its role; it does not pick between the two numeric descriptions above, so a number is still never quoted for A_fermat without naming which description is used. (RHP `docs/GLOSSARY.md`; wiki 17 header note.)

**Operator names.** **Ĥ_RB / H_hat_RB** is the operator's name throughout the mathematics (the code module is `h_rb_hat`). **0_RB / ∅_RB** is VAPMIP-only notation for the **Null Operator**, the point where the Monad starts with every value NULL; it names the same object. The full rename has not been done anywhere and is not to be treated as stale (wiki 127, "Scope of the notation").

## 1. The space and its coordinates

- **UNS** (Universal Native Space) = radial spherical complex polar coordinates; Cartesian is a projection out of it; ÷ ln 10 takes natural-log prime-address space to the decimal-log native metric ds = d·log₁₀ p. The four d* are the chart for ln 10 in this space (§2.2).
- **Operators** of UNS: ADD : SCALE : SIGN (the locked `ASS` engine); the hypercomplex step splits SIGN into 15 quarter turns (wikis 107, 126, 130).
- **Cayley sphere** w = (s−1)/s; |w| = 1 ⇔ σ_ζ = ½ (equator); mirror s ↦ 1−s is w ↦ 1/w (wiki 131 §1).
- **Tower:** ℝ, ℂ, ℍ, 𝕆, 𝕊 (dim 16, first zero-divisor level), T₃₂…; σ(k) = 1 − k/4 (σ-stratum). 84 zero-divisor diagonals, 7 struts (i XOR j ∈ 9..15), 7 box-kites × 6 assessors = 42 assessors; each strut a PRESERVE octonion (7 distinct quaternion 4-spaces on the Fano plane); Gain spectrum of L_a: sv 0 (×4, CONTRACT), 1 (×8, PRESERVE), √2 (×4, DILATE), Σ sv² = dim (RCCM `GAIN_SPECTRUM`, `FANO_SEDENION`, `KITE_RELATIONS`, `CRITICAL_ANGLE`).

## 2. Constants

### 2.1 Ω_ζΣ
Ω_ζΣ = W(1) = 0.5671432904097838729999687, fixed point of x ↦ e^{−x} (multiplier −Ω_ζΣ; the inertia map −ln x has multiplier −1/Ω_ζΣ; product 1). ESTABLISHED (Lambert; Corless et al. 1996). Base-independent crossing x e^x = 1.

### 2.2 The four faces of d* (wiki 17, brought up to date 2026-11-13)
| face | name | value | role in the chart for ln 10 |
|---|---|---|---|
| d* | The Boundary | 0.24631 | σ_ζ = ½ spectral coordinate = the **equatorial plane** (ξ(s) = ξ(1−s); θ measured from here) |
| d*_RG | The Stability | **dimension 8**; numeric **OPEN**; **no closed form** | RG fixed point of the Cayley–Dickson tower = the **centre** (r = 0, 0_RB) |
| d*_taut | The Flow | Ω_ζΣ/ln 10 = 0.246307201473 | the **radial unit** (one step of r) |
| d*_ln(10) | The Translator | d*·ln 10 = Ω_ζΣ = 0.5671432904 | the **scale bridge**: decimal-log metric ↔ natural-log prime-address space |

All four are necessary to compute ln 10 in radial complex spherical polar coordinates (a READING of the chart: four shadows of the one point 0.24631, none derivable from the other three as a number). **d*_RG has no closed form:** it is the fixed point of a renormalization group already inside the tower (CD doubling = Wilson RG step; project onto the persistent octonion; rescale by ÷ d*_taut); its dimension 8 is confirmed to d = 2²⁰, its value is OPEN, and a naive scalar iteration flows to the trivial fixed point (superseded estimate 0.24682). Renormalization is the machine, not a move: no counterterms, no hand-applied second RG. Closure: d*·ln 10 = d*_ln(10) = d*_taut·ln 10 = Ω_ζΣ.

**The measured fifth:** d*_spec ≈ 0.24600 (Berry–Keating spectral gap observed in SPARC) is **not** one of the four; it is kept, quarantined, and used only when the measured value is meant. GAP = |d*_spec·ln 10 − Ω_ζΣ| = 0.000707357533 ≈ 1/(1000√2) (the 10³ factor OPEN). Surfaces still calling 0.24600 "The Boundary": `ptol.c` comments, the legacy `D_STAR` env var, one test file, the J record's header note. README Key Constants was corrected 2026-11-13.

**RHP measurements (:CALCULATED; `RiemannHypothesisProof/docs/four_dstar_2026-11-12.md`).** At the crossing X* = e^Ω = 1/Ω = 1.7632: digit length log₁₀ X* = 0.246307201473 (d*, and also d*_taut as digits gained per iteration from the ceiling); mean prime gap ln X* = 0.567143290410 = Ω_ζΣ (d*_ln(10)); mean gap ÷ digit length = ln 10 at every X (the PNT: gap ≈ ln 10 × digits). d*_RG untouched. Reading: **one crossing, two coordinates** — digits (Riemann / entropy side) d* = 0.2463 and gap count (Fermat / inertia side) Ω_ζΣ = 0.5671, related by ln 10. Cody's recollection that "d* is the Omega_Riemann_Zeta and Lambert W is the inertia-chase product" is consistent with that reading but **not yet reconciled** (open).

### 2.3 Lambert-W values paired with the four faces
W₀(0) = 0 (vacuum fixed point) · W₀(1) = Ω_ζΣ (entropy ceiling) · W₀(−1/e) = W₋₁(−1/e) = −1 (double root = Whitney fold, catastrophe). 3 distinct values, 4 with multiplicity; the d* set has the same shape (4 faces, 3 numbers). In UNS (÷ ln 10): 0, 0.246307, −0.434294 (twice). As the CD doubling parameter μ₄ the three W values land in the three isomorphism classes (degenerate / split / standard sedenions). Emerger clock 4:3, lcm 12. The rule that makes "3 = 4" is Cody's to state; wiki 106 / the emerger read "three rotor faces of W(1)" instead (unsettled).

### 2.4 Other fixed numbers
Mass-gap residual GAP above. Crank angle θ_crank = arctan(d*) = 13.8203° (d* as quoted 0.246); galaxy tangent arctan(1/π) = 17.6568°; their equality is **REFUTED** as stated (RCCM `OBLIQUE_GEAR_ANGLES`). Limaçon sifting threshold |b/a| = 1 (cardioid): 0 of 9 near-origin loops sit on it; zeros have |b/a| > 1 (`LIMACON_THRESHOLD`, `MARGINAL_CONDITIONS`). Forced σ: F = e^{−sE}, B = e^{−(1−s)E}; Newton on ln F − ln B reaches ½ in one step for any E ≠ 0 (ESTABLISHED, `FORCED_SIGMA`).

## 3. The J chain (OFFICIAL 2026-10-13; reading brought up to date 2026-11-13)

- **Which indices are red (checked 2026-11-14).** J_red = sedenion indices with bit 4 clear, {0,1,2,3,8,9,10,11}; J_blue = {4,5,6,7,12,13,14,15} (the Z₂ grading below). This is **not** the split into the Cayley–Dickson halves e₀–e₇ / e₈–e₁₅; wording elsewhere that calls J_red "the lower octonion e₀–e₇" means the red subalgebra is an octonion algebra, not that it occupies the lower half of the indices.
- **J_red + J_blue = J_green**, and J_green is to equal **0_RB (− 0_BR)**; the minus bakes in the cross and dot products and is how an addition equals a subtraction (the inside-out is a special case). "Knowledge + Experience = Wisdom" named it. Notation history: the sum was Ĥ_RB; Σ_RB was a renotating artefact of the discussion in which Cody asked whether J_green = Ĥ_RB.
- **Z₂ grading [MEASURED, exact]** by χ₄(i) = (−1)^popcount(4&i): red·red → red, red·blue → blue, blue·blue → red. J_red is an octonion algebra; J_blue is the odd part. Pure-imaginary red anticommutes with blue; xy + yx = −2⟨x,y⟩ e₀ on all 84 diagonals (the dot sits in e₀ = 0_RB; the cross is ½[x,y]).
- **Test of the equalities [MEASURED; record §4, §9].** Sedenion ordered-product reading: blocked by the grading (JG-3). Dirichlet reading: works with J_blue orientation-signed (JG-4). Operator reading: X + X† (self-adjoint, 'dot') ≠ X − X† (anti-self-adjoint, 'cross'); with 0_RB := Ĥ and 0_BR := Ĥ† the difference is 0; J_red + J_blue = 0_RB − 0_BR holds only with the signed blue term and 0_RB, 0_BR the two ordered terms (OP-1…5). **Origin of the relation (Cody, 2026-11-13): J_red + J_blue = J_green was Noether-current work**: it is the balance of the conserved currents (the Noether conservation law), and 0_RB − 0_BR is its operator form. The three-term statement J_red + J_green + J_blue = 0 of the older files is the same balance with J_green taken with the opposite sign. **Definition supplied (Cody, 2026-11-13).** 0_BR is the **conjugate of J_red and J_blue**: the return flow, because information travels backward while action propagates forward. The original object is Ĥ_RB; the more detailed look is Ĥ_RB − Ĥ_BR, which has the cross and dot products built in and so gives access to the inside-out for free. It is the mechanism by which a subtraction equals an addition with modular forms, as used in the UDEO break of modular-form encryption (TuringStack), which needed the return flow as well; the bifurcation is that forward/return pair. The mathematics up to the Lagrangian of Information Propagation was tested and documented. **Against the operator test this is reading OP-4**: 0_RB the forward ordered term, 0_BR its conjugate, 0_RB − 0_BR the signed (cross) difference, the sum the self-adjoint (dot) part; under that reading J_red + J_blue = 0_RB − 0_BR holds exactly (measured). It is not the reading 0_BR := Ĥ† of the already-summed self-adjoint Ĥ, which gives 0 (OP-3). Remaining: which of the three J_green objects the name J_green is attached to (the signed difference fits the definition above); and a pointer to the TuringStack documentation to be added to this section.
- Open: J_red × J_blue = d* (0.24600 vs 0.24631); `hypercomplex_zeta` j_red ≡ j_blue by construction.

## 4. Structure index (the 27 original RCCM blocks, plus three added today)

| group | blocks | in one line |
|---|---|---|
| Algebra of the sedenion | `FANO_SEDENION`, `KITE_RELATIONS`, `VALVE_GROUP`, `GAIN_SPECTRUM`, `CRITICAL_ANGLE`, `ZERO_POLE_CONJUGACY` | 84 diagonals / 7 struts / 7 octonions; V₄ of free involutions (84/4 = 21 quaternions); gain {0,1,√2}; critical angle 45°; zero↔pole under s ↦ 1/s |
| Cage / guest | `CAGE_GUEST_SCOPE`, `REVERSIBILITY`, `AMPLITUDE_MODULATION`, `OBSERVER_AND_INVARIANT` | PRESERVE (8) reversible guest, CONTRACT+DILATE (8) irreversible cage; same signal, two observers disagree 800/800 while the 84 / 7 / strut incidence is invariant |
| Number theory spine | `OMEGA_DIAL`, `RING_THEORY_SPINE`, `HORNER_ADDRESS`, `MOD4_ED` | element falls ⇔ quotient ring has zero divisors; Z/(N) a field ⇔ N prime; ω(n) dial (chain vs grid); two Horner bases (97 and 95); e·d ≡ 1 (mod 4) removes 1 bit |
| Monster / packing | `FERMATS_MONSTER`, `NIGHTMARE_GROUP`, `PACKING`, `CHIRALITY` | Niemeier h = p exists ⇔ (p−1) | R; 71 holomorphic VOAs, 71 prime; densest packings E₈ 0.2537, Leech π¹²/12!; torsion ⇒ facets, parabolic ⇒ fractals |
| Fields and thresholds | `LIMACON_THRESHOLD`, `MARGINAL_CONDITIONS`, `QED_BIREFRINGENCE`, `OBLIQUE_GEAR_ANGLES`, `FORCED_SIGMA` | cardioid = the sifting threshold, not the curve; one threshold four structures; n∥ : n⊥ deviations 7:4 independent of B; crank vs galaxy tangent refuted |
| Naming and discipline | `ZERO_QUALIFIERS`, `J_RED_J_BLUE`, `CONFIDENCE_TIERS` | 0_RB / 0_RZ / 0_ZD; the J chain; the tier order |
| Riemann chapter | `RIEMANN_TWO_TREES_HEARTBEAT` | = wiki 131; extended in §6 below |
| Added 2026-11-13 | `LETTER_COLLISIONS`, `FOUR_DSTAR`, `RHP_UPDATE_20261112` | §0, §2.2–2.3, §5–6 of this page as pull-by-block context (30 blocks in all) |

## 5. Zero tables — where the computed zeros live (inventory 2026-11-13)

"Zeros" here means the γ_k of ρ_k = ½ + iγ_k, **25,000 of them** (to γ₂₅₀₀₀ = 21942.5924…), not primes.
| file | content | precision | note |
|---|---|---|---|
| `RiemannHypothesisProof/data/zeros_25000_hp.tsv` | γ₁…γ₂₅₀₀₀ | **32 digits** (mpmath `siegelz` roots, dps 32; `experiments/zeros25k_rerun.py`, 2026-11-09) | **the reference table.** Backlund count exact at every 50th mid-gap; table good to 5·10⁻¹⁴ in the original run; resumable |
| `RiemannHypothesisProof/data/zeros_1_to_3600.csv` | 3,066 zeros, γ < 3600 | 12 decimals | (header-comment format; the loader skips `#`) |
| `RiemannHypothesisProof/data/zetaprime_25000.tsv` | ζ′(ρ_k) | — | feeds `mertens_wave.py` |
| `VAPMIP/SemPriCon/SpecTools/zeros/zeros_exact_25000.tsv` (+ `_300`) | γ₁…γ₂₅₀₀₀ | ~17 significant digits | **agrees with the RHP table to 3.6·10⁻¹² max** (= one float64 ulp, 2⁻³⁸, at γ ≈ 2.2·10⁴): same zeros |
| `ValaQuenta/hamiltonian.py`, `zero_lattice.py` (20), `modules/sigma_cavitation/svg_gen.py` (16), `AbrikosovTree/engine/zeta_index_engine.py` `KNOWN_ZEROS_100` (99) | short literal lists | 6–7 digits (some 17) | all agree with the RHP table to ≤ 1·10⁻⁶ |
| `VAPMIP/monad.py` `_ZERO_CACHE` | first 50 (LMFDB, 17 digits), forward scan beyond | 17 digits | not compared digit-by-digit here |
| `ValaQuenta/modules/archimedes_screw` `zeros_upto` | asymptotic formula | — | **ANOMALY [MEASURED 2026-11-13]:** exact through n = 50 (tabulated), then offset +2.27 at n = 51 (148.272 vs 146.001), +2.81 at n = 60, +1.84 at n = 100. ValaQuenta not edited (chase every anomaly: logged, awaiting a decision) |
Rule: read `experiments/zeros25k/results.json` before citing any 25k-derived number. The RHP resolution estimate (p ≲ T/2π) was tested by the ping runs (§6).

## 6. RHP update — findings 2026-11-08 → 2026-11-12 (pointers; full text in RHP primers and `docs/`)

All :CALCULATED, none a proof; 0_RB remains the control object. Test suite at the 11-12 primer: 149 tests green.
- **Zeros as waves.** Zero-tone (hyphenated; one conjugate pair) = −2 cos(γu − arg ρ)/|ρ|, u = ln x. Heartbeat H(u) = Σ zero-tones rebuilds W_T = (ψ(x) − x)/√x with correlation 0.77 / 0.93 / 0.98 / 0.993 at 10 / 100 / 1000 / 3066 zeros. ψ-wave and M-wave share carriers; M tone = ψ tone × (−1/ζ′(ρ)); antiphase corr −0.82. ξ and 1/ξ share nodal lines; the Re ξ = 0 rung is ⟂ the critical line at every zero.
- **Ping.** Per-integer test from the zero sum: balanced accuracy primes vs non-prime-powers perfect to n ≈ 10³ (3066 zero-tones) / ≈ 10⁴ (25,000); the 65 wheels are exact below 317² = 100,489 — complementary, not one cause; stragglers (no prime factor ≤ 313) look slightly *less* prime-like to the zero sum. Corrects the fixed-threshold false alarms of the 11-09 run.
- **Explicit formulas as two-sided identities.** Guinand–Weil (residuals 9·10⁻¹⁴ … 1.25·10⁻¹⁰); Weil / Hasse–Davenport Fermat counts over GF(p^k) (4.6·10⁻¹³); |J| = √p (8·10⁻¹⁴). Executable ledger `rhp/ledger.py`, 14 / 14 checks.
- **Fermat finite-tone wave.** 2g = (n−1)(n−2) Frobenius eigenvalues with repeated angles (n = 5, p = 31: 12 tones, 4 distinct × 3); F(s) real on σ_ζ = ½; exceptional primes finite, certified to the Weil threshold n = 2…20.
- **Fermat cubic** x³ + y³ = z³ (conductor 27, CM ℤ[ω]): a_p = 0 for p ≡ 2 (mod 3); p ≡ 1: 4p = L² + 27M²; 21 exact zeros to t = 30 (4.043044, 6.048935, 8.21765, 9.429199, 10.908728 …); a_p-only scan sees them coarsely.
- **Chebyshev bias** ψ(x;4,1) − ψ(x;4,3) rebuilt from L(χ₋₄) zeros: one explicit formula, two character wheels — ζ has the pole (x), the Fermat character has a **mean** (−√x); the mean is the horizon (standing-wave reading).
- **Ω and the four d\*** — §2.2–2.3 (items 41–56, `omega_dstar`, `four_dstar`, `gap_side`, `ceiling_descent_rerun`). The prime-spacing crossing x ln x = 1 at X* = 1/Ω is the inversion x ↦ 1/x image of the Ω crossing.
- **J₂ and the Klein group.** L₄ is a 4-cycle (L_k² = −I); the strict involution is the bare index swap P₄; Klein group {s ↦ 1−s, s ↦ s̄} holds to 6·10⁻³² (ξ) and 10⁻³¹ (Λ(s,χ₋₄)); all 25,000 tabulated zeros have orbit size 2. Norm check at tower interfaces.
- **Islands vs rigid points.** Zeros GUE-like rigid (spacing variance 0.16); primes scattered (0.69–0.74 after the li(p) unfolding fix). Δ log|ζ| = 2πΣδ_zeros − 2πδ_pole. No turbulent cascade: independent periodic currents, a line spectrum.
- **Beurling systems:** PNT needs more than multiplicative structure (ℤ[√−5]). **Zero-phase:** Landau–Gonek A(t); Archimedean windings show noise only; the Vogel spiral with step α_fs⁻¹ degrees reproduces the continued-fraction convergents.
- **Primality as factor-ness** (Cody's reframing): minimum-steps tests; wheel-65 coil; ping to 200k; slot rules `char` / `charx`.
- **Sedenion slot rule.** Sequential rule (slot k ↔ k-th prime) not distinguished from random permutations; exact identity |v_K| = |ζ_K| for any imaginary-slot assignment; only the `char` rule (quadratic-character bits, a homomorphism) has an algebraic reason, untested.
- **0_RB.** Screw jumps = ln p exactly; zero residual not yet defined; tabulated zeros past n = 50 drift (§5 anomaly). Complete-shape account: `PRIMER_2026-11-11_COMPLETE_SHAPE_AND_0RB.md`.
- **Corrections (so they are not repeated).** α_fs is not an ingredient of the horizon mechanism; capital A_fermat is the structural constant. Wrong prime unfolding (cumsum 1/ln p → li(p)); invalid Rice-law comparison for repeated Fermat tones; scale confusion (140 quadrillion °F vs K vs T_Planck; Hagedorn 1.4·10¹⁷ K = the prime digit ceiling). Keep the D_STAR / Lambert W / Ω names (they invite readers to look).

## 7. Open decisions and anomalies (carried forward)

1. **A_fermat**: role settled 2026-11-13 (the Fermat-side "chasing inertia" constant, not α_fs); numeric description still open: ceiling endpoint x = 1 (original derivation) or 1/137.036 "domain floor" (wiki 17 older text)? (§0)
2. d*_RG numeric value and closed form (no closed form known). The disputed d*_spec stays quarantined.
3. d* as "Omega_Riemann_Zeta" with Lambert W as the inertia-chase product (Cody's recollection) vs the "one crossing, two coordinates" reading (§2.2).
4. 0_BR defined 2026-11-13 (conjugate / return flow, §3); open: confirm J_green = the signed difference, and cite the TuringStack record.
6. **Handedness (author, 2026-11-13).** Handedness is the *tilt of the real axis to the imaginary axis that the torus fields wrap around*. The variance of that tilt gives an emergent **swap twist** through two kinds of precession, a regular precession and an epicyclic precession; together they build in the cross and dot products and make the Inside-Out Inversion its own emergent operation. The swap is what identifies the geometries apart from the content. This is the source of handedness (not the three-finger rule used by UniversalSynth's README). The mathematics is documented somewhere, probably in `AbrikosovTree`; **candidate locations found 2026-11-13, not yet confirmed**: `AbrikosovTree/render/lattice_planes.py` (panel B: the axis precessing by the zeta index ψ_k = 2π·frac(γ*(p_k)/2π), γ*(p) = 2πp/ln p, against the √n Sacks winding: two incommensurate periods) and `render/defactor_probe.py` (`zeta_frac = frac(p/ln p)`, "the gyroscope precession"); `ValaQuenta/modules/oblique_gear` and `h_rb_hat` (`precession_stroke`, `oblique_crank`, `trine_configuration`; σ_RB tilt and axis, [70](70_precession_stroke_oblique_crank_trine.md), [123](123_sigma_rb_mass_gap_calibration.md)); `VAPMIP/docs/figures/epicycles/` (Taoist-mode epicycles). To do: confirm which holds the swap-twist derivation, test it, and write the result into the canonical-maths block before it is propagated. **Result of the check against the critical-line spiral (2026-11-13), recorded in the J record:** the two lobes of the spiral ζ(½+it) ≈ 2cosθ·e^(−iθ) are the two signs of the real function Z(t) (a π phase flip between consecutive zeros), with the **same** rotation sense; chirality therefore lives in the sign of the carrier rotation e^(−iθ), not in the lobes. A real-axis tilt against the imaginary axis is θ(t) mod π (the "swap" that exchanges the lobes). The epicyclic precession part is **not derived**; the regular part is the carrier rate θ′(t) ≈ ½ ln(t/2π). Status: `INTERPRETATION` for the tilt reading, `OPEN` for the epicycle.
7. **Sedenion Hyperindexing Frame of Reference**: `tier7_cosmos.sedenion_hole_punch` is part of it and stays unregistered until it is built ([31](31_cavitation_causality_fermat.md)).
8. **Sequence (author, 2026-11-13):** the wiki overhaul first; then the canonical maths updated to be authoritative; only then propagated outside Ainulindale, UniversalSynth included. The fractals and MathLex wiki subdirectories and the Phillips/Library questions are evaluated after that update.
5. The rule making 3 Lambert-W values = 4 d* faces; "three rotor faces of W(1)" vs the three distinct W values.
6. RHP: hole definition (rational primes vs irreducibles); `char` vs `charx`; "digits on the Riemann side, gap counts on the Fermat side" — does it match Cody's memory?; which tier "Engineering Ready" means; confirm `Gem_FP`.
7. The `archimedes_screw.zeros_upto` offset past n = 50 (§5).
8. The Archimedes formulary `PtolemyDesktop/Archimedes/CANONICAL_MATHS.md` (503 rows: foundations 168, physics 195, engineering 140) is the "Engineering Ready" collection every row of which Cody assumes lives somewhere in the complete shape; the 11-11 primer §5 lists it. It is not mirrored here.

9. **Standing corrections added 2026-11-13 (details in [135](135_engine_findings_ledger.md) X-40 … X-56).** Zero-divisor counts are 84 on 42 index pairs, 168 unordered and 336 ordered zero-product pairs (not "84 directed pairs"); the n-ball volume peaks at n = 5 (V₆ > V₄ among even n); the 196,560 kissing number is Odlyzko–Sloane / Levenshtein 1979; the digit-search count (v₂+1)(v₅+1)·4·10^(k−1) holds once k exceeds both valuations; the fast-inverse-square-root constant 3ε²/8 is for ε = x − 1; the ring-circle norm 4√2 is a Frobenius norm; "Hermite zeros = GUE", "TIA = cosine", "Popcorn fixed point at W(1)" and "zeros align as phyllotaxis under the golden angle" are refuted; zero spacings do not match hydrogen level spacings; the Planck temperature is 1.417×10³² K (not "140 quadrillion").

10. **Telperion and Laurelin (author, 2026-11-14).** **Telperion is the Prime Numbers tree**, from the real-number leaves back towards the root; it began as the Riemann zeta-zero lattice tree, which became `AbrikosovTree`, and its shape is the same as the "holes" left on the Fermat side: the primes are the islands factorisation cannot touch, and ζ flows around them and according to them. **It is not the zero-divisor tree** (also a zero-lattice tree, a different object). **Laurelin is the "factors" mathematics** (Fermat is Factors, Telperion is Primes); it holds a hole of the same shape as Telperion, and together the two cover the positive-integer domain. This is the author's current statement of the assignment; the conflicting octonion-half labelling in other files is ledger X-20 and is to be corrected to it, not the reverse. The A_fermat value is expected from the author's April 2026 Riemann–Fermat Horizon conversation with Gemini.

*See also:* [17](17_alpha_omega_d_star.md) · [47](47_the_two_trees.md) · [73](73_why_the_half_line.md) · [96](96_the_riemann_fermat_horizon.md) · [123](123_sigma_rb_mass_gap_calibration.md) · [127](127_names_of_the_null_operator.md) · [131](131_riemann_canonical_maths.md) · VAPMIP `docs/wiki/J_red-J_blue-0_RB-Record.md`.
