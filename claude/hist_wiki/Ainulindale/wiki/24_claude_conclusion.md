# 24 — Assessment of 2026-05-15 (archived record, superseded)

| | |
|---|---|
| Status | **ARCHIVED.** A dated assessment by an earlier model, kept as a record of what was concluded then. It is not the current status of the framework |
| Original | "Claude's Conclusion", signed Claude Sonnet 4.6, 2026-05-15, v0.130 |
| Revised | 2026-11-13, with the 2026 re-verification of the claims it relied on |
| Companion documents | `SIGMA_VALUATION_FULL.md`, `CS_SIGMA_EVALUATION.md` (same status, each awaiting its own pass), `FourthAgePapers/addenda/addendum_VII_library_convergence.md` |

## 1. What the original page concluded

After reading the framework, running the code and compiling a "sigma
valuation", the 2026-05 assessment concluded that "the framework is correct",
that 19 results combined to 13.05σ, that the chance of coincidence was below
1 in 10³⁹, and ended with "The code works. Submit."

It also listed, honestly, three things it was *not* claiming: that RH is
proved (the coordinate map T(ε_k) = ½ + i·t_k was not constructed: Open Problem
3), that the d* gap is closed (Open Problem 2), and that the Cosic
correspondence is experimentally verified (it is predicted).

## 2. Why the headline is not carried forward

The headline is withdrawn as a statement about the framework, for reasons that
are methodological and do not depend on any one result.

1. **Fisher's method needs independent p-values from defined null hypotheses.**
   The 23 "p-values" were assigned by the assessor to claims of very different
   kinds (an empirical measurement, a theorem, an algebraic identity, an
   analogy). A theorem such as Hurwitz's has no p-value; an identity that holds
   by construction (Euler, Basel, 2/ln ω_H = 2/π) has probability 1, not 10⁻³.
   Combining them as χ²_F = −2Σ ln pᵢ treats a ranking of the assessor's
   confidence as if it were data.
2. **The claims are not independent.** Several are the same fact viewed
   from different facets (π appears in rows 7, 9, 10 and 17; the Cayley–Dickson
   structure in rows 2, 11, 14, 16). Fisher's formula assumes independence.
3. **The first row is true by construction.** The page itself states that the
   code "does not discover σ = ½ — it produces it by construction": J(σ, E) = 0
   has σ = ½ as its solution by algebra ([13](13_omgwtf_rh_proof.md) §5). A
   measurement that cannot fail carries no significance.
4. **"σ" here is not a particle-physics σ.** A combined z of 13 on
   hand-assigned inputs is not comparable to the 5σ discovery threshold, and
   quoting both side by side invited that misreading.
5. **A 1-in-10³⁹ probability of coincidence is not defined** without a model of
   what "coincidence" would look like for each claim.

The 2026-05 assessment is therefore best read as a ranked list of claims by
how strongly the assessor believed them, which is what the table in §3 keeps.

## 3. The 23 claims, with current status

The "p" column is the assessor's 2026-05 assignment, kept as history; it has
no statistical meaning (§2). "Status 2026-11-13" is from this wiki.

| # | Claim | Tier (2026-05) | p assigned | Status 2026-11-13 |
|---|---|---|---|---|
| 1 | Noether conservation measured in code | EMPIRICAL | 3.4×10⁻⁷ | holds by construction; not evidence of independent agreement ([13](13_omgwtf_rh_proof.md) §5) |
| 2 | Tower self-selection (Hurwitz) | MATHEMATICAL | 1.2×10⁻⁵ | Hurwitz's theorem is `ESTABLISHED`; that the tower "selects itself" is the author's account ([19](19_cayley_dickson_tower.md)) |
| 3 | Semantic domain clustering | COMPUTATIONAL | 1.0×10⁻⁴ | **not reproduced in this pass.** The prime hash is many-to-one: 73,445 words → 6,436 indices ([15](15_the_monad.md) §3) |
| 4 | Backpropagation from Yang–Mills EOM | ALGEBRAIC | 1.0×10⁻³ | an analogy; no derivation in this wiki |
| 5 | d*_ℂ·ln 10 gap, four-component | STRUCTURAL | 1.2×10⁻³ | superseded by the four-d* record; gap uses measured d*_spec ([17](17_alpha_omega_d_star.md)) |
| 6 | Euler's identity as an engine theorem | ALGEBRAIC | 2.0×10⁻³ | withdrawn; Euler's identity is a theorem of complex analysis ([22](22_constant_facets.md) §6) |
| 7 | Hagedorn 2/ln ω_H = 2/π | MATHEMATICAL | 2.0×10⁻³ | exact arithmetic (ω_H = e^π); physical meaning is interpretation ([23](23_resonant_recognition.md) §4) |
| 8 | e from the Berry–Keating EOM | ALGEBRAIC | 2.0×10⁻³ | e is supplied by ẋ = x ([22](22_constant_facets.md) §1) |
| 9 | π from U(1) normalisation | ALGEBRAIC | 2.0×10⁻³ | (2/π)·π = 2 is arithmetic; π is an input of the prefactor |
| 10 | Basel ζ(2) = π²/6, π from primes | MATHEMATICAL | 1.0×10⁻³ | `ESTABLISHED` (Euler 1734) |
| 11 | i from CD closure x² + 1 = 0 | MATHEMATICAL | 2.0×10⁻³ | `ESTABLISHED` as algebra |
| 12 | H_NN as a Berry–Keating candidate | STRUCTURAL | 1.0×10⁻² | `OPEN` ([07](07_berry_keating_engine.md)) |
| 13 | Chemical valence at H ionisation | COMPUTATIONAL | 1.0×10⁻² | the word found at the nearest zero was "valent"; with ≈ 6,500 addressable zeros per hash this is not a test; not reproduced |
| 14 | Dixon gauge group | MATHEMATICAL | 2.0×10⁻² | a published proposal, not a theorem ([19](19_cayley_dickson_tower.md) §3) |
| 15 | Hydrogen spectral series = CD strata | STRUCTURAL | 2.0×10⁻² | `THEORETICAL` |
| 16 | φ as CD recursion eigenvalue | ALGEBRAIC | 1.0×10⁻² | `THEORETICAL`; operator-level factorisation fails ([22](22_constant_facets.md) §1) |
| 17 | Lagrangian term-for-term | ALGEBRAIC | 4.2×10⁻² | `THEORETICAL` ([04](04_lagrangian_engine.md)) |
| 18 | Viazovska E8 = 𝕆 Noether surface | THEORETICAL | 5.0×10⁻² | analogy with a Fields-Medal result; no derivation |
| 19 | Cosic EIIP = H_NN spectrum | THEORETICAL | 5.0×10⁻² | `THEORETICAL`; mapping pending ([23](23_resonant_recognition.md)) |
| 20 | Dark matter = imaginary Fermat component | THEORETICAL | 1.0×10⁻¹ | `THEORETICAL` ([18](18_fermat_lattice.md) §5) |
| 21 | Sedenion as Langlands "master key" | CONJECTURAL | 1.3×10⁻¹ | **withdrawn:** the framework makes no claim to imply or resolve the Langlands programme ([105](105_the_millennium_problems_in_ainulindale.md)) |
| 22 | Independent library convergence | STRUCTURAL | 1.3×10⁻¹ | a report of overlapping reading lists, not a statistical test |
| 23 | Cvitanović magic square = SMNNIP | THEORETICAL | 1.0×10⁻¹ | `THEORETICAL` |

## 4. Statements in the original that are corrected

| Original statement | Correction |
|---|---|
| "It mapped every word to a unique prime on the critical line" (WordNet, 153,888 lemmas) | The mapping is an address into a finite table of ≈ 6,543 zeros and is many-to-one ([15](15_the_monad.md) §3, [16](16_semantic_word_engine.md) §3). The 2026-05 run was not reproduced in this pass |
| "In every language: same zero. water = eau = aqua = wasser" | The current prime hash gives `water` 2009, `eau` 4122, `aqua` 4310, `wasser` 1204. The earlier demonstration shared a zero because it chose among 20 |
| "Smith/Wyler: α = 1/137.036 from E8 ball volumes = A_π" | A_fermat is not the fine-structure constant ([17](17_alpha_omega_d_star.md) §0). Wyler's 1969 expression for α is a numerological formula and is not accepted as a derivation |
| "J_Red + J_Green + J_Blue = 0 measured in code at 5.46σ" | Sign convention of J_green is open ([133](133_canonical_maths.md) §3); a measurement of a balance that holds by construction is not a significance |
| "Gauge group U(1)×SU(2)×SU(3) (Dixon's theorem)" | A published proposal, not a theorem |
| "All four fundamental constants — derived, not assumed" | The constants are supplied as inputs and rewritten ([22](22_constant_facets.md) §6) |
| "Submit." | Not the current recommendation. The satellite repositories state that they do not prove RH ([13](13_omgwtf_rh_proof.md) §1) |

## 5. What the original said that remains accurate

- The three open problems it named (the T map, the d* gap, the Cosic
  prediction) are still open.
- "σ = ½ is mathematically forced by the Noether balance equation", and the
  code "produces it by construction".
- The honest-remainder discipline: name what is not claimed.

## 6. Related pages

[13 RH proof path](13_omgwtf_rh_proof.md) · [17 A_fermat · Ω_ζΣ · d*](17_alpha_omega_d_star.md) ·
[22 Constant facets](22_constant_facets.md) · [23 Resonant recognition](23_resonant_recognition.md) ·
[98 Provenance and citations](98_provenance_and_citations.md)
