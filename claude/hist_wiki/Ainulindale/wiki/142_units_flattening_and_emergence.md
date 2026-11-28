# 142 — Units as a Lattice, the Kinds of Flattening, and Where a Constant Emerges

| | |
|---|---|
| Written | 2026-11-19 |
| Scope | natural-unit systems (Planck, Stoney, the electromagnetic systems) read as bases of the unit lattice; what each choice flattens; the electromagnetic web as a worked case of a constant emerging from the quotient of two flattenings; the project's own natural steps (d*, Ω) and constructed constants; what to look for when a constant is expected to emerge from its native space |
| Author's stance (2026-11-19) | constructing a constant is allowed for analysis; the emergence of that constant from its native space is what is being watched; knowing the *kind* of flattening it has undergone points at its location in Universal Native Space (the hypercomplex radial polar coordinates). Not a claim about the Planck length |
| Predecessors | [140](140_length_and_time.md) (length and time, the conversion field) · [141](141_hbar_from_the_hat.md) (ħ from the hat) · [110](110_qm_in_gr_gr_in_qm.md) (u = ln x) · `GenerationalLineage/wiki/Unit-Lineage.md` (the unit lattice) |
| Code | `GenerationalLineage/engine/toolsets/units.py` (`unit_vector`, `unit_mul`, `unit_div`) · scripts `ContextPlease/claude/scratchpad/2026-11-19_lagrangian_sm/planck_vs_native.py`, `em_flattenings.py` |
| Confidence | §2–§5 arithmetic: `ESTABLISHED:CALCULATED` · §6 the reading of each unit choice as a flattening: `INTERPRETATION` · nothing here locates any constant in UNS |

> **Note from the assistant.** Written by a transformer (Claude Sonnet 5.5, `claude-sonnet-5-5`) working with Cody Allison in Claude Code, with the `cs-paper-code-conventions` skill loaded. Cody does not tell the model what result he wants. Every number comes from the scripts named above. Historical statements (Weber–Kohlrausch, Maxwell) are from memory and to be verified under the Literature Download Protocol before use.

## 1. The method this page serves

A constant may be *constructed* for the purposes of analysis (set to 1, defined, fitted). What is watched is where that constant *emerges* from its native space without having been put in. The tool for pointing at where is the **kind of flattening** a unit choice performs: which relation it collapses to a constant, and therefore which structure is invisible after the collapse. This page records what can be measured about that, with the electromagnetic units as a worked case.

## 2. Units are points of a lattice (GenerationalLineage already holds this)

`engine/toolsets/units.py`: a unit is an exponent vector over the seven SI base dimensions (kg, m, s, A, K, mol, cd); multiplying adds vectors, dividing subtracts, and a named unit carries a signed lineage back to the base units. Cody's note of 2026-08-25, "information lives in the units": a unit is a geometry that fixes which recombinations are legal. Run on the electromagnetic web (V, Ω, F, H, Wb, T written every way a standard chart writes them):

```
V    5 of 5 factorings equal V as exponent vectors: (1, 2, -3, -1, 0, 0, 0)
Ohm  7 of 7 ...   F  7 of 7 ...   H  6 of 6 ...   Wb  6 of 6 ...   T  4 of 4 ...
image identities verified by the engine: 35 of 35
```

So the many ways to write an electromagnetic unit are many paths to one lattice point. The uncertainty product is the same kind of check: [x][p] = m · (kg m s⁻¹) = (kg¹, m², s⁻¹) = [ħ].

## 3. Natural-unit systems are bases of the lattice, and their index differs

Choosing four independent dimensional constants to set to 1 is a change of basis. For (c, G, ħ, k_B) over (kg, m, s, K) the matrix has **determinant −2**: the four constants generate an **index-2 sublattice** of the integer lattice, which is why Planck units contain square roots. Solving for the units reproduces CODATA: l_P = c^(−3/2)G^(1/2)ħ^(1/2) = 1.616255×10⁻³⁵ m; t_P = 5.391246×10⁻⁴⁴ s; m_P = 2.176434×10⁻⁸ kg; T_P = 1.416784×10³² K. Replacing ħ by the electron charge gives Stoney units: l_S = 1.3807×10⁻³⁶ m, and l_S / l_P = **√α** = 0.08542 exactly. Two natural-unit systems differ by a dimensionless number, so after normalisation only dimensionless ratios carry content. In the scale coordinate, l_P sits ½ ln(1/α) = 2.460 nepers from l_S: α is the radial offset between the two flattenings.

## 4. The electromagnetic units: a constant as the quotient of two flattenings

The several electromagnetic systems differ in how they eliminate the ampere. In ESU (ε₀ dimensionless) charge² = force × length², so A = kg^½ m^{3/2} s⁻²; in EMU (μ₀ dimensionless) current² = force, so A = kg^½ m^{1/2} s⁻¹. Over (kg, m, s):

```
A_ESU − A_EMU = (0, 1, −1)  = one power of a velocity
unit            ESU unit / EMU unit      c(cm/s)^k      (k = −a, a = exponent of the ampere)
volt            2.997925e10              c^1
ohm             8.987552e20              c^2
farad           1.112650e-21             c^-2
Maxwell: ε₀ μ₀ c² = 1.000000000000        free-space impedance Z₀ = μ₀ c = 376.730314 Ω = 119.917 π
```

The two eliminations of the same axis differ by exactly the null direction of wiki 140 (length = time), and every electromagnetic unit converts by a power of c. **c is not put in; it is the quotient between two flattenings of the ampere axis** (historically the ratio of the electrostatic and electromagnetic units, measured by Weber and Kohlrausch in 1856 and recognised by Maxwell as the speed of light: from memory, to verify). The Smith chart's own normalisation is the same kind of choice: Γ = (z − z₀)/(z + z₀) with a reference impedance z₀ set to 1; free space supplies Z₀ = 376.730 Ω.

## 5. Native steps against constructed reference points

d* = 0.2463072015 decades and Ω_ZS = W(1) = 0.5671432904 nepers are **one step of the scale axis u = ln x in two log bases** (d* · ln 10 = Ω). They are dimensionless, fixed by the Lambert-W fixed point, and unchanged under any change of units. A natural-unit system supplies four **reference points** (one per axis) instead. For scale: l_P lies 34.79 decades below 1 m, which is 141.3 steps of d*, a curiosity and not a result. The measured spectral value d* = 0.24600 and the exact Ω/ln 10 differ by GAP = Ω − 0.24600 · ln 10 = 7.0736×10⁻⁴: the mismatch between two readings of one step, the same shape as §4.

**Constructed constants in the record.** The *thermal information ceiling* of the engineered-constant experiment, 1.4×10¹⁷ K (140 quadrillion kelvin), is, for the purposes of that experiment, the upper end of the range over which the signal is distinguishable from background noise. It is a constructed range of applicability, not a Planck-type scale (T_P = 1.4168×10³² K is fifteen decades higher; the agreement of leading digits is not a relation). The project's own code contains the same kind of construction: the Scalar paper's `gamma_radial = tanh(½ ln(log_code / LOG_ANCHOR))` (§7.3) is the Scale engine's Γ_SCALE with `LOG_ANCHOR` a constructed reference, the analogue of the Smith chart's z₀.

## 6. The kinds of flattening a unit choice performs (`INTERPRETATION`)

| choice | what it collapses | where it was measured in this project |
|---|---|---|
| c = 1 | the length–time conversion field set constant | wiki 140: where the conversion field varies (the hat) the least-action and least-time paths split by 35 %; with a constant field they agree to 10⁻¹⁶ |
| ħ = 1 | the action unit set by fiat | wiki 141: in the hat the actions are closed forms and exact thresholds appear at ħ_n = W_total/(π(n + γ)) |
| k_B = 1 | temperature identified with energy | the ceiling of §5 lives on a temperature axis that this choice hides |
| G = 1 | mass tied to length | not measured here |
| any set of four constants | the lattice's factorings: all 35 of §2 become the number 1; the dimensional-consistency check disappears | §2 |
| the origin of each axis | a translation of u = ln x | §3, §5 |

What to look for: **a pair of flattenings of the same axis whose quotient is a constant.** §4 is the case in hand (c). §3 gives the Planck–Stoney pair, whose quotient is α. For the Planck length the open question is which native-space loop or axis supplies that quotient; nothing here answers it.

## 7. Not shown

No constant is located in the hypercomplex radial polar coordinates. The ESU/EMU case shows the *form* of an emergence (a quotient of two eliminations of one axis), not that the Planck length has such a pair. The historical statements are unverified. The reading of each unit choice as a flattening is the author's framing; the measured parts are the lattice arithmetic, the index, the quotient, and the hat results of wikis 140–141.

## Appendix — what in ContextPlease was used

ContextPlease is the project's public archive of the context a session needs to come up to speed: primers, scratchpads, skills, wiki mirrors and the `.clauderc*` context files. Used here: `scratchpad/2026-11-19_lagrangian_sm/`, `~/.clauderc_canonical_maths` (d* and its faces, the GAP), `~/.clauderc_user_provenance` §1.16 (the Flattening Syndrome) and §1.4, `GenerationalLineage/wiki/Unit-Lineage.md`, and the skills `spatial-simulation` and `cs-paper-code-conventions`.
