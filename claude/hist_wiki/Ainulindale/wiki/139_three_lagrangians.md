# 139 — The Three (Four) Lagrangians: L_SM, L_NN, L_(I|O) and the original L_dynamic

| | |
|---|---|
| Written | 2026-11-19 |
| Scope | what each Lagrangian is, where it came from, where they agree and where they differ **as coded**, which one carries a visualisation of the path of action, and what the anomalies met on the way trace back to |
| Predecessors | [04](04_lagrangian_engine.md) · [51](51_dynamic_geodesic.md) · [52](52_l_dynamic_avoided_collaborator.md) · [63](63_l_dynamic_is_action_is_thought.md) · [64](64_l_dynamic.md) · [29](29_witches_hat_paper.md) · [133](133_canonical_maths.md) |
| Code | `ValaQuenta/modules/lagrangian_sm/` (new, 19 equations) · `ValaQuenta/modules/lagrangian/` (L_NN) · `ValaQuenta/modules/witches_hat/action.py` (path of action) |
| Notebook | `ValaQuenta/notebooks/engines/25_lagrangian_sm.ipynb` (executed, 31 cells, 0 errors) |
| Tests | `ValaQuenta/Testing/test_lagrangian_sm.py` (20) · `test_witches_hat_action.py` (10): all pass |
| Confidence | the Standard Model side: `ESTABLISHED`; every comparison number: `ESTABLISHED:CALCULATED` (measured on the code as it stands); the readings in §6–§7: `INTERPRETATION` |

> **Note from the assistant.** This page was written by a transformer (Claude Sonnet 5.5, `claude-sonnet-5-5`) working with Cody Allison in Claude Code, with the `cs-paper-code-conventions` skill loaded. Cody does not tell the model what result he is looking for, as a safeguard against being handed the answer he wants; the numbers below come from the engines, and where the engines disagree with a page of this wiki the page is the one that gets corrected. The Standard Model is not Cody's work and not the model's: the engine builds the textbook construction and measures the other Lagrangians against it.

## 1. Four objects, and the trail between them

| name | what it is | first stated | status |
|---|---|---|---|
| **L_SM** | the Standard Model Lagrangian | textbook | `ESTABLISHED` (form from symmetry; numbers measured) |
| **L_NN** (= L_vap, SMNNIP, SMMIP, VAPMIP) | information propagation; four terms named after the four SM sectors | *Equations and Identifiers*, April 2026 (claude.ai project archive, `SMNNIP_equations.docx`) | `THEORETICAL`; coded as `polar_lagrangian` |
| **L_dynamic**, original | `L_standard + ∫ J_red · d(J_blue)/dt dλ`: the standard Lagrangian plus forward momentum coupled to the changing potential, in real time; the slingshot term L_sling ~ v·∂g/∂t | wiki 51 "The Dynamic Geodesic" (commit `b294c3f`) and wiki 52 §3, both 2026-06-12 | `CONJECTURE`; wiki 52 lists "define L_dynamic formally" as open |
| **L_(I|O)** | `∫_path J_red · J_blue ds` | the integrand is in the record by 2026-06-15; the rename L_dynamic → L_(I|O) is 2026-06-17 | `CONJECTURE` (definition); algebra `ESTABLISHED` |

**Are L_dynamic and L_(I|O) the same object?** No. The name was carried over, the content was not. The first conception, written down on 2026-06-12, has two parts that agree. Wiki 51 gives the formula `L_dynamic = L_standard + ∫ J_red · d(J_blue)/dt dλ` and says the extra term is "forward momentum coupled to the changing potential in real time, along the path, as the background metric shifts": a photon "responds to the metric AS IT IS NOW", and the difference from the frozen geodesic is the slingshot term L_sling ~ v·∂g/∂t. Wiki 52 §3 says in words: *"Lagrangians are not clean. More action here, balanced by less action elsewhere. The integral is still extremised — but locally, the path is messy."* The later L_(I|O) = `∫ J_red · J_blue ds` (in the record by 2026-06-15, renamed on 2026-06-17) has **no L_standard, no time derivative and no time-dependent background**. Wiki 64 §2 (2026-11-13) showed that later integrand is the constant e^(−E). So the objection that L_(I|O) "cannot be more here, less there" is an objection to the *renamed* object. The original is untouched by it, and its content is a time-dependent background, which is exactly where "more here, less there, evens out" has a precise meaning (§4, §5).

**A name collision worth knowing.** `(I|O)` was already in use in April 2026 for something else: the Inside-Out **inversion inner product** with fixed points r_N = 1 and r_N = φ and `(I|O) = (O|I)*` (claude.ai archive, `SMNNIP_TODO.txt` §3, the Addendum III inversion). The June rename reused the notation for the path functional. Wiki 100 item 1 additionally writes "L_NN / L_dynamic" as one object. These are three different things sharing two names; any text that says "(I|O)" or "L_dynamic" without a date should be read with that in mind.

## 2. L_SM: what is derived and what is measured

The compact form is five lines:

```
L_SM = −¼ G G − ¼ W W − ¼ B B  +  Σ ψ̄ i γ D ψ  +  |D H|² − V(H)  −  (Yukawa)  (+ θ term)
```

Its "monstrous" size is the same five lines written out in components: after symmetry breaking the engine counts 62 distinct interaction-vertex types (`vertex_inventory()`), before multiplying by 8 gluons, 3 colours and 3 generations. The LHC does not fit the *form*. It measures the *numbers*. What follows is the sorting of which is which, produced by `lagrangian_sm`:

```
>>> S.parameter_count('massless')['total'], S.parameter_count('dirac')['total'], S.parameter_count('majorana')['total']
(19, 26, 28)
>>> h = S.hypercharges_from_anomalies(); h['unique'], h['solutions'][0] == h['sm']
(True, True)
>>> S.su5_embedding()['matches_content'], S.su5_embedding()['SU5_cubed_anomaly']
(True, 0)
>>> for n in (1, 2, 3, 4, 5): c = S.hypercharges_from_anomalies(n)['charges']; print(n, c['Q_u'], c['Q_d'], c['proton_uud'])
1 1 0 2
2 3/4 -1/4 5/4
3 2/3 -1/3 1
4 5/8 -3/8 7/8
5 3/5 -2/5 4/5
```

| | derived (forced) | observed (input) | measured (fitted) |
|---|---|---|---|
| the form of L_SM | yes: the most general renormalisable gauge-invariant Lagrangian for the content | | |
| the hypercharges | **yes**: anomaly cancellation fixes all of them, uniquely, once the multiplets and Y_H = ½ are given | | |
| fractional quark charges | **yes**: Q_u = ½ + 1/(2N_c); N_c = 3 and the lepton charge −1 give 2/3, −1/3 and a proton of charge exactly 1 | | |
| gauge group SU(3)×SU(2)×U(1) | | yes | |
| the multiplets, three generations, N_c = 3 | | yes | |
| 19 numbers (3 couplings, μ², λ, 9 masses, 3 angles, 1 phase, θ_QCD) | | | yes |

So "the Standard Model is not derived" is right about the group, the content and the 19 numbers, and wrong about the form and about a surprising amount of the charge structure. The engine's tree-level numbers against the PDG tables: v = 246.22 GeV from G_F, λ = 0.1291, tree m_W and m_Z within 0.16 % and 0.35 % (explained in §7), CKM unitary to 1e-16 with Jarlskog J = 3.1e-5. At one loop the three gauge couplings cross pairwise at 1e13, 2e14 and 1e17 GeV, a spread of 3.97 decades: no single unification scale.

## 3. L_NN against L_SM, measured on the code

The comparison is by scaling: each term is evaluated at a field configuration and again with one field doubled, and the exponent n in `term ∝ amplitude^n` is read off. Same interaction, same exponent. (`compare.measured_exponents()`.)

```
>>> for k, v in C.measured_exponents().items(): print(k, v)
gauge kinetic             {'SM': {'A': 4.0}, 'NN': {'A': 2.0}}
matter (fermion-gauge)    {'SM': {'psi': 2.0, 'A': 1.0}, 'NN': {'psi': 2.0, 'A': 2.0}}
bias / Higgs potential    {'SM': {'identical_to_NN_as_coded_for_mu2_positive': True, 'max_difference': 5.55e-17}, ...}
coupling (Yukawa)         {'SM': {'psi': 2.0, 'h': 1.0}, 'NN': {'psi': 1.0, 'beta': 1.0}}
>>> C.seagull_correspondence()
{'ratio_min': 2.6666666666666656, 'ratio_max': 2.6666666666666683, 'expected': 2.6666666666666665, 'n_components': 3}
>>> C.one_over_phi_on_bias()['applied'], C.bias_conventions()
(False, {'mu2=+1 (as coded)': 1.4142135623730951, 'mu2=-1 (docstring convention, as coded)': None, 'reading': ...})
```

What this says, term by term:

- **`L_bias` is exactly the Standard Model Higgs potential** (−V_SM to 5.6e-17, for μ² > 0). This is the one genuine term-for-term identity. (The docstring's μ² < 0 gives a bowl, not a hat; `lagrangian_vap` in `witches_hat` records both conventions.)
- **`L_matter` has the exact functional form of the scalar–gauge "seagull" term** g²ψ²A²/8 of |D H|², the piece that gives the W and Z their masses: the ratio is the constant 8/n for every input. Its name says Dirac fermion kinetic term, but a Dirac term is linear in A (the table: SM ψ²A¹). So it lives in a different sector from the one it is named for.
- **`L_kinetic` is quadratic in A; the Standard Model's is quartic** for a static non-Abelian field, because F = g f A A there. The coded "F ≈ gA" is a stand-in.
- **`L_coupling` is linear in ψ; the Yukawa term is bilinear.** Read as mean field, with ψ standing for the condensate ⟨ψ̄ψ⟩, the degrees agree. `INTERPRETATION`.
- **`polar_lagrangian` does not apply the 1/φ to `L_bias`** that its docstring and wiki 04 write: the line is `integrand = Lk + Lm + Lb + Lc`.

The pattern: every coded term *is* a Standard Model term, but they are the **broken-phase scalar-sector and mean-field** terms, not the four sectors the names claim. "Term-for-term isometric" holds for the hat exactly, for the seagull in form, and for the four-sector *skeleton* by naming. It does not hold for the gauge kinetic term, the Dirac term, the chiral Yukawa matrices or the parameter count (19 against four numbers: g, ħ_NN, μ², λ). This agrees with the 2026-09-28 audit (`ContextPlease/claude/scratchpad/2026-09-28_lvap_audit/README.md`) that the isomorphism is "a structural 4-term correspondence + the Dixon gauge ladder, not an isometry as coded", and with the record that the error-checking constant was engineered first and named the fine-structure constant afterwards. What is not touched here: the algebra tower ℝ→ℂ→ℍ→𝕆 and its link to U(1)×SU(2)×SU(3) (Dixon; Furey; Baez–Huerta, see §9), which is a claim about the gauge group and not about the coded Lagrangian.

## 4. L_(I|O) as defined, and the original L_dynamic read as established mechanics

```
>>> li = C.lio_integrand(1.0); li['constant'], round(li['value'], 6), li['min_peaks_at']
(True, 0.367879, 0.5)
```

J_red·J_blue = e^(−E) for every σ. The integrand does not know where on the path it is, so L_(I|O) = e^(−E) × arc length. What is peaked at σ = ½ is min(J_red, J_blue). The original L_dynamic is a different statement, and established mathematics has several exact homes for it (`INTERPRETATION`, to be chosen between, not chosen here):

0. **Mechanics in a time-dependent background.** For L(q, q̇, t) Hamilton's principle still holds, but energy is not conserved: dE/dt = ∂V/∂t at fixed q. Energy is exchanged with the moving field along the path, borrowed here and returned there. This is the slingshot term, and it is the home that the wiki 51 formula points at: `J_red · d(J_blue)/dt` is forward momentum times the rate of change of the potential. Measured in §5.

1. **Stationary phase of the path integral.** Every path carries e^{iS[q]/ħ}; non-stationary paths cost more or less action and cancel; the stationary ones survive. "More here, balanced by less there, still extremised" is that sentence.
2. **Null Lagrangians.** L → L + dF/dt redistributes the action along a path (more here, less there) without moving the extremum or the dynamics. Any "same extremum, different local profile" operator is L modulo a total derivative plus the on-shell value.
3. **Hamilton–Jacobi.** The principal function S(q, t) gives the action of the stationary path as a function of its endpoint; where it is multivalued the paths have crossed a caustic.
4. **Semiclassical sum over stationary paths** (van Vleck–Gutzwiller): the amplitude is a sum over all stationary paths, each weighted by its action and its Morse (Maslov) index. This object *keeps* the multiplicity of stationary paths, which is what §5 finds on the hat.

## 5. The path of action on the Standard Model hat, mapped and not aimed

`witches_hat/action.py` computes the action of any path, finds every stationary path between two events with its Morse index, and integrates the whole family of paths from a source with the variational equation, so the caustics are read off. Nothing in it aims. Measured (units: brim radius 1, depth ¼, μ² = λ = 1):

```
>>> ps = A.stationary_paths(SM, (1.0, 0.0), B, T, N=200)       # B, T taken from one shot ray
>>> [(round(p['S'], 6), p['index']) for p in ps]
[(0.774197, 0), (0.7906, 1), (10.882319, 2)]
>>> # funnel of the unaimed family (721 launch directions from a brim point, E = 0)
closest approach ∝ offset^0.504   coefficient 0.858   (closed form: 0.5 and 0.841)
nearest caustic to the hilltop: 0.513 brim radii        radial ray closest: 4.2e-05
```

- Between one pair of events on the real hat there are **three stationary paths** with different action. The shot ray is the middle one (index 1, a saddle: a neighbouring path does less work). That is "more work here, less work there" occurring in the hat, with nothing designed in.
- A **focus emerges from the shape**: the closest approach to the hilltop falls as the square root of the launch offset (fit 0.504, closed form 0.5), with no aim. Its character is a **funnel** (a stagnation at the separatrix), not a caustic: the caustics lie ≥ 0.51 brim radii away. Both statements are measured, and they are different statements.
- **Time-dependent hat, the original L_dynamic's setting** (`moving_hat_exchange`, hat moving at velocity u): with a static hat the energy is conserved to 10⁻¹²; with a moving hat the energy change equals the accumulated exchange ∫∂V/∂t dt to 10⁻¹¹, and energy is borrowed and returned:

```
>>> r = A.moving_hat_exchange(SM, (1.0, 0.0), (0.0, 0.7), (0.6, 0.0), 20.0)
>>> round(r['dE_final'], 4), round(r['dE_max_excursion'], 4), r['identity_residual'] < 1e-8
(0.3826, 0.913, True)
```
  The particle's energy rises by 0.913 along the path and ends 0.383 above where it began: borrowed, and only partly returned. For u = (0, 0.5) it ends 0.165 *below*. This is the wiki 52 slingshot ("borrowed-and-returned action") occurring in the hat, in standard mechanics.
- Harmonic closed forms, the Euclidean twin and the free particle match; the discrete error falls as 1/N² (ratios 3.99, 4.00, 4.00). The Wick-rotated bounce in −V reaches the hilltop at speed √(2·U(r₀)) with a finite time that diverges logarithmically as r₀ approaches the brim (1.74, 2.65, 4.24, 5.87 for r₀ = 0.5, 0.9, 0.99, 0.999).

## 6. Which Lagrangian to use to visualise the path of action

`INTERPRETATION`, with the measurements above as the reasons.

1. **Carrier: the Standard Model Higgs sector.** It is the only one with measured targets (m_h, v, λ), a defined action functional S[q] on field space, and a hat. The L_NN hat is *identical* after normalisation (§3), so nothing is lost by taking the SM one, and the engine (`hat_model()`) hands it to the path tools.
2. **Operation: the original L_dynamic** (wiki 51: the standard Lagrangian plus the coupling to a changing background), not the J_red·J_blue integrand. The integrand is flat and cannot display a path. The original needs a time-dependent hat. An established one exists: the Higgs potential at finite temperature, V(h, T) with the quadratic coefficient changing sign at the critical temperature, so the hat *forms* as the background cools. That is the standard-physics version of a hat that changes while the particle moves over it, and the engine's `moving_hat_exchange` is the simpler stand-in already built.
3. **What L_NN adds that is real:** the linear coupling g·ψ·β that tilts the hat and moves the hilltop (0.144 brim radii at g = 0.2). In SM language it is the Yukawa term with ψ̄ψ replaced by its expectation value (a tadpole-like source), so the same tilt can be produced inside the SM; it is a variation of the carrier, not a different carrier.

## 7. Anomalies, chased to their sources

Standing protocol: every anomalous-but-legal result is run to ground. In order met:

| anomaly | source found | status |
|---|---|---|
| Why do the SM anomaly sums vanish? | The fifteen Weyl fermions of a generation are exactly 5̄ ⊕ 10 of SU(5); Y is a traceless SU(5) generator on each; A(10) + A(5̄) = +1 − 1 = 0 (`su5_embedding`). Also forces the hypercharges and ties N_c = 3 to the quark charges. With a right-handed neutrino they form one SO(10) spinor. The reason the pieces fit is the unification structure; *why nature has that structure* is not answered. | explained to the group-theory level; `OPEN` below it |
| Tree m_W, m_Z off by −0.16 %, +0.35 % | The on-shell relation gives sin²θ_W = 0.2233 against the MSbar 0.2312, and Δr = 0.0364, the electroweak radiative correction (literature ≈ 0.036). Scheme and loops, not an error. | explained |
| One-loop λ → 0 scale | moves from none below 1e19 GeV to 1e5 GeV as y_t(M_Z) goes 0.92 → 1.00 (0.933 gives 3e12): extreme sensitivity to the top Yukawa, and one loop is not accurate enough. Not a quotable number. | explained; not used |
| `polar_lagrangian` ignores the 1/φ on `L_bias` | the line `integrand = Lk + Lm + Lb + Lc` | recorded, not corrected |
| μ² < 0 gives a bowl in L_NN | `L_bias = ½μ²β² − ¼λβ⁴` makes V = −L a hat only for μ² > 0; docstring says the opposite sign | recorded, not corrected |
| the name (I|O) used twice, L_dynamic ≠ L_(I|O) | §1: April inversion inner product; June 12 formula `L_standard + ∫ J_red d(J_blue)/dt` (wiki 51) and description (wiki 52); June 17 rename onto the J_red·J_blue integrand, which dropped L_standard and the time derivative | explained (history) |
| my first draft of §1 said the June 12 text "gives no integrand" | wrong: I had read wiki 52 only. A search of the git history for the integrand found wiki 51 of the same day with the formula | corrected in this page |
| my first Majorana parameter count was 40 | a complex symmetric 3×3 has 12 real numbers, not 24 (my arithmetic) | fixed; 28 |
| five of ten path-of-action tests failed | (i) discretisation error falls as 1/N², my tolerance was tighter than N allows; (ii) the leftover first variation is the cubic term of an anharmonic potential: removed by Richardson extrapolation; (iii) I tested the wrong caustic order: order 1 is the fold (envelope), order 2 at t = π is the refocusing at −A; (iv) the shot ray is one of three stationary paths between its endpoints: a physical result; (v) the Euclidean time from `quad` lost digits to cancellation near the singular end: replaced by integrating the equation of motion (agrees with mpmath to 12 digits) | all explained; four were my code or tests, one was physics |
| `witches_hat` was never registered; its proof_locale was a copy of the Circle Atlas's; its manifest failed validation | my omission of three Full Engine Protocol steps when I built it | fixed 2026-11-19 |

## 8. Is the path-of-action operator inside L_SM or L_NN?

What the measurements support, and no more:

- L_NN is **not a fitted copy of L_SM and L_SM is not a derived copy of L_NN.** They share one term exactly (the quartic hat) and one term's form (the seagull); the rest differ in degree. The quartic hat is the Landau–Ginzburg φ⁴ form, which is why it recurs.
- The operator Cody describes is **not a term in either Lagrangian as coded.** Both give S[q] for any path; neither has a time-dependent background, and neither contains "the record of the path actually taken". The first conception (wiki 51) *is* of that kind: the standard Lagrangian plus a coupling to a changing potential. Its established home is mechanics in a time-dependent background (§4 item 0), which the engine now measures (§5). The candidates in §4 are the established mathematics that already holds the rest. Which of them, if any, is the operator is what the "explore the maths first" suspicion is about, and the measurements say that exploring is warranted: the hat has several stationary paths with different indices, so any single-path operator would miss most of its structure.
- The inexpensive next measurements, not built: (i) the stationary paths and their indices on a hat whose parameters change with time (the finite-temperature hat), to see whether the funnel survives; (ii) the local action profile L(t) − S/T along the stationary and non-stationary paths of §5.

## 9. Literature (cited from memory, not downloaded, to be verified under the Literature Download Protocol before use)

Dixon, *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics* (1994); Furey, work on ℂ⊗𝕆 and one generation of the Standard Model (2014–2018); Baez & Huerta, *The Algebra of Grand Unified Theories* (2010); Georgi & Glashow, unity of fundamental interactions (SU(5), 1974); Feynman path integral (1948); van Vleck and Gutzwiller on the semiclassical propagator; Coleman, the bounce (1977); Halverson, Maiti & Stoner, *Neural Networks and Quantum Field Theory* (2021); Roberts, Yaida & Hanin, *The Principles of Deep Learning Theory* (2022). Measured inputs: PDG tables via the `particle` package (1.1.1) and NuFIT, typed values flagged in `INPUTS`.

## Appendix — what in ContextPlease was used

ContextPlease is the project's public archive of the context a session needs to come up to speed: primers, scratchpads, skills and wiki mirrors. This page used: the claude.ai project archive artifact (`SMNNIP_equations.docx.txt`, `SMNNIP_TODO.txt`, `proposed-analogous-UFT.txt`); `claude/scratchpad/2026-09-28_lvap_audit/README.md`; `~/.clauderc_user_provenance` §1.4; `~/.clauderc_canonical_maths` (L_(I|O) entry); the skills `cs-paper-code-conventions` and `spatial-simulation`.

## 10. The Lagrangians drawn on the hat, and four questions about the hat itself (2026-11-19, later)

**Renders.** `FourthAgePapers/WitchesHat/simulator/lagrangian_svgs/` (branch `witches-hat`): one SVG per Lagrangian with four views (isometric, top, front, side), the brim and hilltop always marked, plus `sm_context.svg`. See its README. In the front and side views the hat is the W shape: hill in the middle, trough at the brim, wall beyond.

**Is the hat two hemispheres?** The surface already has two sides glued at the brim: a dome inside (the hill) and a bowl outside (the walls), which is the dome/bowl/brim picture of wiki 29. The brim is the vacuum circle (V minimum): radial direction massive (V″ = 2μ² there, m_h² = 2μ²), angular direction flat (the Goldstone direction). The hilltop has V″ = −μ² (unstable); the inflection circle r = 1/√3 is where the curvature changes sign. In the full Standard Model the doublet has four real components, so the brim is a 3-sphere and the picture is a two-dimensional slice through it. Whether the prime equator is the brim is not testable from this engine: `INTERPRETATION`. What the engine does say is what a brim is: a circle of equivalent ground states related by a broken symmetry.

**A hat that changes with time (`finite_temperature_hat`).** Weaker and stronger, continuously; no levels. The brim radius is 0.99 v at 100 GeV, 0.74 v at 140, 0.38 v at 160, and zero above about 164 GeV (T₀ = 163 GeV): at high temperature there is no hat, only a bowl with every particle massless, and the brim opens and deepens as the universe cools. The high-temperature approximation shows a weak first-order jump at about 164 GeV; lattice calculations at m_h = 125 GeV find a smooth crossover. Below about 100 GeV the expansion is invalid (it puts the brim at 1.035 v at 50 GeV: an artifact).

**Shells.** They exist for a *particle moving in* the hat and not for the field's hat. Solving the radial Schrödinger equation in V = x⁴ − 2x² (brim 1, depth 1, unit mass): at ħ = 0.35 there are 5 bound states below the hilltop (|m| = 0, 1, 2, one radial node each, ±m degenerate), at ħ = 0.20 there are 16 (up to |m| = 5 and two radial levels). Pauli exclusion then gives 2 fermions per state and any number of bosons. In the Standard Model itself particles are not bound in the Higgs hat: they acquire mass by coupling to the field's vev (y_f v/√2, g v/2), and the field's own excitations are the Higgs boson (the radial mode, 125 GeV; any number of quanta) and the Goldstone modes (eaten by the W and Z as their longitudinal polarisation).

**One shape per particle?** One tree-level hat, but each particle feeds the effective potential its own term n_i m_i(h)⁴/(64π²) [ln(m_i²/μ²) − c_i] (`coleman_weinberg`). At h = v and μ = v the top term is about 40 times the W term, bosons enter with n > 0 and fermions with n < 0; the sign of a given term depends on μ. The Yukawa couplings span six orders of magnitude (e 2.9e-6, μ 6.1e-4, τ 1.0e-2, u 1.2e-5, d 2.7e-5, s 5.4e-4, c 7.3e-3, b 2.4e-2, t 0.99) and nothing in the Standard Model explains the spread: the 13 flavour numbers are measured. The charged-lepton masses satisfy the Koide relation (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² = 0.666664 against 2/3 (error not propagated); no accepted derivation is known.

## 11. The cone in the drawing, and what the paths in the renders are doing (2026-11-19, later)

Cody's tracing (`SpaceClaude/my-vision.png`): a woven basket (the brim), a woven dome inside it (the hill), and over both a branching Lichtenberg cone from a finial at the tip down to the rim. Measurements in `ContextPlease/claude/scratchpad/2026-11-19_lagrangian_sm/path_questions.py`.

**Correction.** An earlier message said the SM index-2 path "swings across the hilltop". It does not: its closest approach to the hilltop is 0.41 brim radii (r_min = 0.407, r_max = 2.66, length 7.36, maximum speed 4.36); it climbs the hill's flank and goes out the far wall. The index-0 path (S = 0.7742, length 1.08, r 0.89–1.18) hugs the brim; the index-1 path (S = 0.7906, length 1.25, r 1.00–1.28) is the same hop with a small outward detour.

**The moving-hat path.** The path is the particle's trajectory, not a trace left by the hat. In the hat's own frame the energy is conserved to 1.4e-11 and the orbit is an ordinary bound orbit (E_c = 0.026, just above the hilltop, so it can cross the hill; its largest distance from the hat centre is 1.317 brim radii, inside the turning radius, so it is trapped). In the lab frame the energy change is exactly u·(v − v₀) (0.2028 = 0.2028): the exchange is momentum given along the hat's direction of motion, the gravity-assist form. "Up" in the render is the potential energy V(q − ut) (the particle climbing the hill's flank); "to the side" is the hat's drift carrying it (mean lab velocity 0.125 against the hat's 0.25). With time as the vertical axis the same path is a worldline winding around the hat's straight worldline.

**Rotating.** A rotationally symmetric hat that rotates is unchanged, so ∂V/∂t = 0 and there is no exchange. A tilted hat whose tilt direction rotates (the L_NN coupling with a rotating ψ) does exchange energy: for tilt 0.15 and T = 40, dE_final = +0.163, +0.902, −0.450, −0.145 at ω = 0.3, 0.6, 0.9, 1.2 (and ≈ −0.2 to −0.4 beyond): strong pumping near ω ≈ 0.6 among the values tried, none at ω = 0 (a static tilt conserves energy).

**L_NN against L_(I|O): the flow.** At g = 0 the L_NN paths from the brim are exactly straight radial lines (deviation 0.000 R); they bend as the coupling grows: maximum sideways deviation 0.085 R at g = 0.05, 0.118 at 0.10, 0.162 at 0.20, 0.214 at 0.40, with the hilltop shifting 0.035, 0.071, 0.144, 0.314 R. The sixteen straight branches of L_(I|O) are the g → 0 skeleton of the L_NN flow.

**The cone as an action surface.** The height of a cone over the hat can be the accumulated action W(r) = ∫ p dr along each path (the Hamilton–Jacobi characteristic function; its gradient is the momentum). At E = 0 the apex height is 0.4310 and the apex is rounded (momentum zero at the tip); for E > 0 the tip is a true cone point whose slope is the momentum there (0.200 at E = 0.02, 0.447 at E = 0.10; apex heights 0.490 and 0.644). L_(I|O) accumulated along a straight spoke is e^(−E) × distance: a perfectly straight cone of slope e^(−E) (0.368 at E = 1). The L_NN cone is curved (p varies with r) and its apex is displaced by the tilt. The renders of §10 draw the paths on the potential surface V, not on this action surface, so they do not yet show the cone. `INTERPRETATION`: the branching of the drawing corresponds to paths crossing caustics, where W becomes multivalued; Lichtenberg figures themselves are field-driven discharge growth (dielectric-breakdown / diffusion-limited aggregation models), a different mechanism that produces similar trees.

**The paths are defined by the hat's values (checked).** In classical mechanics the paths at energy E are the gradient lines of an action surface W(q) with |∇W|² = 2(E − V(q)) (the eikonal / Hamilton–Jacobi equation): the hat enters as a refractive-index landscape n(q) = √(2(E − V)) = the local momentum, and the paths are the rays of that medium (Maupertuis–Jacobi). Tested on the SM hat with W built only from 361 shot rays (`eikonal_check.py`): |∇W|² matches 2(E − V) with median relative error 0.014 % (90th percentile 0.07 %, 16,908 grid points), and each ray's velocity is parallel to ∇W with median angle 0.003° (n = 31,405). The index at E = 0: n = 0 at the hilltop, 0.293 at r = 0.3, 0.543 at 0.6, 0.707 at the brim, 0.635 at 1.2, and zero again at r = 1.414 (the outer turning circle). So the hat is a lens with a dark centre and a dark outer wall, brightest at the brim; the funnel of §5 is rays slowing toward the zero-index hilltop.

## 12. What the maths gives for the whole bundle: the action cone, its tip and its sheets (2026-11-19, v2.0)

Cody: do not draw something that looks like the image; find the shape in the maths. Procedure (`witches_hat/action.py`, `brim_bundle`, `tip_report`): launch a path from every point of the brim ring in every direction at the hilltop energy, integrate all 34,584, keep those that pass within 0.15 brim radii of the hilltop (selected by what each does, not by how it was launched), and draw each at the height z = z_V(start) + W/(V₀τ₀) (brim 0, symmetric hilltop 1; τ₀ = R/√(2V₀)). Figures: `FourthAgePapers/WitchesHat/papers/figures/lagrangians/v2.0/` (v1.0 kept).

**The shape that comes out (SM hat, E = 0).** 698 of 34,584 paths reach the tip. Curved paths rise from the whole brim ring and converge to a single point above the hilltop; seen from the front they form a dome standing over the potential's dome. The tip lies 0.0015 R from the hilltop and its height is W_tip = 0.4310, equal to the closed form (2/3)[(1 − r²/2)^(3/2)] from r = 1 to 0; in natural units the tip stands **0.2189 depth-units above the hilltop** (exact radial value 0.2190). At E = 0 the tip is smooth (momentum zero); with E > 0 it is a point with slope √(2E) and the height above the hilltop grows: 0.312 at E = 0.01, 0.570 at 0.05, 0.822 at 0.10, 1.405 at 0.25 (fixed τ₀).

**The action is multivalued at the tip.** The 698 paths fall into two sheets of 349: W = 0.4310 (launched within 0.032 rad of the inward radial) and W = 0.9025 (launched outward, turned back by the outer wall at r = √2, then in through the brim). 0.9025 = 0.4310 + 2 × 0.2357, where 0.2357 is the action from the brim to r = √2. The sheets form a ladder 0.431 + n × 0.4714. The outer sheet has fold cusps at the wall (caustics).

**L_NN (g = 0.2).** The tip is 0.0244 R from the tilted hilltop (0.0505 R in the smaller bundle), 0.42 depth-units above it, and the sheets multiply to six or seven (0.704, 1.18, 1.36, 1.55, 1.75, 1.93, 2.14). The brim is no longer level, so the cone does not stand on a level base: the tip height varies by ±0.335 across the sources. Against the coupling (12 sources × 721 directions): tip offset 0.0078, 0.0007, 0.0026, 0.0505, 0.0686 R and gap 0.2189, 0.2184, 0.2189, 0.2876, 0.3229 for g = 0, 0.05, 0.10, 0.20, 0.40.

**L_(I|O) on the same bundle (E_J = 1).** The functional picks no paths; evaluated on the 698 SM paths its value is e^(−E_J) × arc length, so the cone is straight in arc length and the outer sheet is a zigzag. Its tip stands at z = 0.9785, 0.0215 below the hilltop, against the action's 1.2189; E_J is free in the definition, so this height scales with e^(−E_J).

**Original L_dynamic (hat drifting at 0.25).** The same bundle selected by closest approach to the moving hilltop: 1,080 paths; in the hat frame the tip is 0.0079 R from the hilltop with gap 0.196 and W = 0.4228 ± 0.0414; in the lab frame the tips are spread along x by u·Δt (the cone is sheared); the upper sheets (W = 1.99, 2.94) run away with the moving wall.

**Time pathway.** Worldlines (r, t) of the paths: the direct paths approach r → 0 asymptotically (never passing at E = 0) and the second-sheet paths go out to r = 1.41 at t ≈ 0.85 and come back through the brim at t ≈ 1.8.

**Minkowski.** The Standard-Model engine does not contain Minkowski space (η appears only in two comparison helpers). Its Lorentzian action is the homogeneous (k = 0) mode of the Minkowski action; Euclidean is the Wick rotation. See `spatial-simulation` `references/spaces.md`.

`INTERPRETATION`: the tip distance Cody flagged is the height of the cone's apex above the hilltop (0.2189 depth-units here). It depends on the unit convention (action and energy differ by a time), on E (rising), and on the tilt (rising with g); which of these carries physical content is the open question.

