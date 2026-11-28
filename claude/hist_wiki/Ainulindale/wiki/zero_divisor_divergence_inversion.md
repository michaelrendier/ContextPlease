# Zero Divisors as Divergence-Inverted Sources (2026-06-01 reframing, with 2026-11-13 corrections)

| | |
|---|---|
| Scope | the claim that a sedenion zero-product a·b = 0 is a source and not a sink, the n-ball volume Vₙ read as phase available at Cayley–Dickson level n, the "phase gate" φ_ZD = V₂₄ − V₁₆, and the decomposition of the 196,560 Leech minimal vectors |
| Written | 2026-06-01 (status then: THEORETICAL, "major reframing of E-8-6"); corrected 2026-11-13 |
| Engine | `ValaQuenta/modules/tier8_sedenion/maths.py`, `leech_divergence_inversion()` (re-run 2026-11-13: its volume table reproduces Listing 1); notebook `ValaQuenta/notebooks/tier8/leech_divergence_inversion.ipynb` |
| Confidence | the arithmetic (Vₙ, φ_ZD, the Leech shape counts): ESTABLISHED (re-run) · the divergence argument as written: its premise is retired (§2) · every physical consequence (§5): `CONJECTURE`, not tested by anything on this page |
| Last verified | 2026-11-13: Listing 1 executed; the engine function run. The notebook was not re-run |

This page is unnumbered; it belongs in sequence with [25](25_sedenion_manual.md) (the sedenion manual) and [120](120_symmetry_breaking_is_the_instrument.md). The original 2026-06-01 text is kept below in its own words, with a label and a correction beside each claim that did not survive; the maths is written in Unicode, not LaTeX.

## 1. The old reading, and what the reframing keeps

The older reading took a·b = 0 with a, b ≠ 0 as a permanent sink: information enters and nothing leaves, the Pauli-style "forbidden state", the termination of the algebra. The 2026-06-01 page called that "false… only half the picture — the 16D projection". What can be said **exactly** is narrower and stronger: a zero divisor is not an ending of the algebra. Verified elsewhere in the wiki ([25](25_sedenion_manual.md), [133](133_canonical_maths.md)): the sedenions have 84 zero-divisors on 42 index pairs, 168 unordered and 336 ordered zero-product pairs; the zero divisors are **not** an ideal (a + b = √2·e₁ is invertible), so the set is not closed under the algebra's own addition; and a product of two zero divisors being 0 is an ordinary entry of the multiplication table. Nothing in the algebra makes it a sink or a source; "sink" and "source" are properties of a **flow** that has to be defined first.

## 2. The divergence argument  `THEORETICAL`, premise retired

The 2026-06-01 argument: the sedenion unit ball B¹⁶ has boundary S¹⁵; the "Noether balance" J_R + J_G + J_B = 0 requires ∮_{S¹⁵} (J_R + J_G + J_B)·dA = 0; by the divergence theorem the total divergence inside B¹⁶ is zero; if zero divisors were pure sinks, ∇·F|_ZD = −δ(x_ZD) < 0 and the flux would be net inward ("the universe would drain"); so every sink needs an equal and opposite source, which is placed in the eight dimensions of ℝ²⁴ ∖ ℝ¹⁶ (the Leech lattice's extra dimensions).

**Corrections, kept beside the original (not replacing it).**

- The premise "Noether balance" is retired: s ↦ 1 − s is a discrete involution, so there is no continuous symmetry and no Noether current ([133](133_canonical_maths.md) §3; ledger [135](135_engine_findings_ledger.md)); J_red + J_blue = J_green is a notation of the J chain, not a conserved current. The divergence argument therefore proves nothing as stated: it assumes the conservation law it is meant to support.
- No vector field F on B¹⁶ is defined whose divergence is −δ at a zero divisor. A zero-product a·b = 0 is a point of a multiplication table, not a delta function of any field defined on the page. "Sink" is a figure of speech here.
- The step "so the source lies in the eight missing dimensions" is a placement chosen to restore balance; ℝ²⁴ is picked because the Leech lattice lives there. Nothing derives it.

What survives is the observation that a closed ball must have zero net flux **if** a conserved flow is defined on it, which is a general fact and not specific to zero divisors.

## 3. The n-ball volume as "phase available"  `ESTABLISHED` (arithmetic), `INTERPRETATION` (the reading)

Vₙ = π^{n/2}/(n/2)! (even n). **Listing 1 — the volumes, the gate and the Leech counts** (written for this page; python3 standard library; runs cold)

```python
from math import pi, factorial as f, comb, gamma
V = lambda n: pi ** (n / 2) / f(n // 2)
for n in (2, 4, 6, 8, 10, 16, 24): print(n, V(n))
phi = V(24) - V(16)
print('phi_ZD', phi, '; 195,456 x phi_ZD =', 195456 * phi, '; 196,560 x phi_ZD =', 196560 * phi)
print('Leech shapes', comb(24, 2) * 4, 759 * 2 ** 7, 24 * 2 ** 12, 'sum', comb(24, 2) * 4 + 759 * 2 ** 7 + 24 * 2 ** 12)
print('integer n with the largest unit-ball volume:', max(range(1, 30), key=lambda n: pi ** (n / 2) / gamma(n / 2 + 1)))
```

```
2 3.141592653589793
4 4.934802200544679
6 5.167712780049969
8 4.058712126416768
10 2.550164039877345
16 0.23533063035889312
24 0.001929574309403922
phi_ZD -0.23340105604948921 ; 195,456 x phi_ZD = -45619.63681120896 ; 196,560 x phi_ZD = -45877.3115770876
Leech shapes 1104 97152 98304 sum 196560
integer n with the largest unit-ball volume: 5
```

| n | Algebra | Vₙ | Role claimed in 2026-06-01 |
|---|---|---|---|
| 2 | ℂ (U(1)) | π = 3.14159 | full U(1) period |
| 4 | ℍ (SU(2)) | π²/2 = 4.935 | "SU(2) volume (**maximum!**)" |
| 8 | 𝕆 (G₂ ⊃ SU(3)) | π⁴/24 = 4.059 | E₈ sphere, Viazovska optimal |
| 16 | 𝕊 (sedenion) | π⁸/8! = 0.2353 | sedenion phase space |
| 24 | Λ₂₄ (Leech) | π¹²/12! = 0.001929 | Leech phase space, Viazovska optimal |

**Correction (kept): "maximum" is wrong.** The unit-ball volume peaks at n = 5 (V = 5.264) and, among the even n, at n = 6 (V₆ = π³/6 = 5.1677 > V₄ = 4.935); the engine's own table lists V₆ = 5.1677 and so contradicts the "maximum!" note. The ratio Vₙ/Vₙ₋₂ = π/(n/2) is exact, and "every Cayley–Dickson doubling costs a factor of π/(n/2)" is a correct restatement of it, but the doublings 2 → 4 → 8 → 16 are steps of ×2 in dimension, not of 2 in n, so the ratio between **successive algebras** is V₈/V₄ = 0.8225 and V₁₆/V₈ = 0.0580, not π/(n/2). Why Vₙ should be the "phase available to the path integral" at level n is not argued; it is a reading (`INTERPRETATION`). The same n-ball was tested against the extinction curves in [131](131_riemann_canonical_maths.md) §9 and the naive form failed there.

## 4. The phase gate  `ESTABLISHED` (value), `CONJECTURE` (meaning)

φ_ZD = V₂₄ − V₁₆ = π¹²/12! − π⁸/8! = −0.23340106 (Listing 1), and the "gate" e^{iφ_ZD} = e^{−0.2334 i}. The value is exact. What is not established: the difference of two ball volumes is a real number that has been given the **unit** of an angle; nothing makes a subtraction of volumes a phase. This is the same move as the mass-gap Δ = Ω − d*·ln 10, a difference named a physical quantity ([123](123_sigma_rb_mass_gap_calibration.md), [120](120_symmetry_breaking_is_the_instrument.md) §5). "The universe does not end at a zero divisor, it rotates" is the author's image for the gate and carries no derivation.

## 5. The 196,560 and the physical consequences

The Leech minimal vectors: 1,104 of shape (±4, ±4, 0²²) [C(24,2)·4], 97,152 of shape (±2⁸, 0¹⁶) on the 759 octads with an even number of minus signs [759·2⁷], 98,304 of shape (∓3, ±1²³) [24·2¹²]; total 196,560 (Listing 1). `ESTABLISHED`. **Correction (kept): the attribution.** The kissing number 196,560 in 24 dimensions is Odlyzko–Sloane and Levenshtein (1979, independently); Viazovska and co-authors proved the **sphere packing** optimality of E₈ (2016) and of the Leech lattice (Cohn–Kumar–Miller–Radchenko–Viazovska, 2017). "Proved by Viazovska 2022" is not the record.

Two further claims of the 2026-06-01 text do not survive a count:

- "The 195,456 non-pure Leech vectors are the backward x-affinities. **Each one is a zero-divisor pair (a, b) with a·b = 0 in 16D**": the sedenions have 336 ordered zero-product pairs (168 unordered), not 195,456. The map from Leech vectors to zero-divisor pairs is asserted, not constructed, and the counts do not match; kept as the original wrote it and marked `OPEN` until a map is exhibited.
- Forward and backward x-affinities, r → ±R_H²·r†/|r|², are the author's naming of two conformal inversions; the assignment of the 1,104 to "forward" and the 195,456 to "backward" is by shape and has no further derivation.

Consequences listed in the original, all **`CONJECTURE`**, none tested by this page: Hawking radiation as the flux from the Leech lattice into the sedenion; the CMB as the thermal sum of 195,456 activations over 13.8 Gyr × N_Planck; the bare vacuum energy Λ_bare = 195,456·φ_ZD ≈ −45,620 (arithmetic reproduced, −45,619.64; with all 196,560, −45,877.31), "before Noether renormalisation drives it to Ω_ZS" (the Noether premise is retired, §2; and the number is dimensionless, not an energy density); and cancer as zero divisors firing without a source, the drug as "the Leech source". The medical statement is outside the scope of the maths and is **not** a result; it is kept so the record of what was written stays complete and is not to be cited as evidence about disease.

## 6. Summary table (the original, with tiers)

| Old reading | 2026-06-01 reading | 2026-11-13 tier |
|---|---|---|
| a·b = 0: information terminates | a·b = 0: a throat to 24D | `CONJECTURE` (no flow defined) |
| zero divisor = permanent sink | divergence-inverted source | `THEORETICAL`, premise retired (§2) |
| Pauli exclusion = death | Pauli exclusion = phase gate = rotation | `INTERPRETATION` |
| 196,560 Leech roots = packing | = backward x-affinities / saddle points | counts `ESTABLISHED`; the identification `OPEN` |
| Vₙ = abstract geometry | Vₙ = Lagrangian phase at level n | `INTERPRETATION`; "maximum at n = 4" false |
| cancer = zero-divisor block | ZD fires without Leech source | outside the maths; not a result |

## 7. Related pages

[25](25_sedenion_manual.md) · [120](120_symmetry_breaking_is_the_instrument.md) · [123](123_sigma_rb_mass_gap_calibration.md) · [131](131_riemann_canonical_maths.md) · [133](133_canonical_maths.md) · [135](135_engine_findings_ledger.md)
