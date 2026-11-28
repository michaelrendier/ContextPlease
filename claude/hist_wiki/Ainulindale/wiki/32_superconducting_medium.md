# 32 — The superconducting medium: the Bang as a phase transition

| | |
|---|---|
| Status | **First capture (2026-06-03), continuation of [31](31_cavitation_causality_fermat.md); `CONJECTURE`.** Every claim below is a model statement; the one place it contradicts measurement (§2) is stated and kept |
| Code | none specific; engines 21 (`bang_superconductor`) and 22 (`bec_coherence`) named by the earlier page do not exist (searched `ValaQuenta/modules`) |
| Related data | `FourthAgePapers/CMB_FractalBoundary` and `CMB_PlasmaBoundary` (Planck and WMAP temperature spectra; ptychographic reconstruction): these do **not** test the zeros-in-the-CMB claim of §5 |
| Last verified | 2026-11-13: the deceleration parameter recomputed (below); the CMB directories read for any test of §5 |

## 1. The thesis, as the model states it  `CONJECTURE`

The spacetime medium is a *superconducting Bose–Einstein condensate*:
non-shear, zero resistance, refractory; the Big Bang is its first and largest
cavitation, and the "mushroom cloud" still expands because nothing stops it.
Three words carry the model:

| Word | Meaning in the model | Consequence claimed |
|---|---|---|
| superconductor | zero resistance to waveform propagation | the expansion has no drag, so it does not slow |
| condensate | one macroscopic wavefunction | entanglement is structural: two excitations of one condensate |
| refractory | resists phase reversal | no global recondensation; only local nodes recondense, and those are stars |

## 2. "The expansion was never decelerating": contradicted by measurement

The model says the expansion was not decelerating and that the observed
acceleration "is the observation that the current is stable". The measured and
standard picture is different, and the numbers are easy to state. With flat ΛCDM
(Ω_m = 0.3111, Ω_Λ = 0.6889), the deceleration parameter
q(z) = [½Ω_m(1+z)³ − Ω_Λ] / [Ω_m(1+z)³ + Ω_Λ] is

| z | 0 | 0.3 | 0.645 | 1 | 2 |
|---|---|---|---|---|---|
| q | −0.533 | −0.253 | 0 | +0.175 | +0.386 |

i.e. the expansion decelerated (q > 0) before z ≈ 0.645 and has accelerated
since; the transition is constrained by supernova and BAO data. A model in which
the expansion never decelerated is in tension with that, and the page's
claim is recorded as **failing this comparison**; the model would have to
reproduce the early-time deceleration (matter domination) as well. This is
kept in the page, not removed.

## 3. Dark energy as a superconducting current  `CONJECTURE`

Claim: Λ is the amplitude of a persistent current established by the Bang
cavitation; it does not decay. The observed value is Λ ≈ 1.1·10⁻⁵² m⁻²
(`ESTABLISHED` as the fitted standard value). A derivation from the model is
the open problem: j_s = n_s·e·v_s with n_s the condensate density (related to the
Planck density at t = 0), e the coupling (the p^(−½) terms of Ĥ_RB) and v_s = c,
giving Λ = f(n_s, p^(−½), c) "without fitting". No such f is given, and the
analogy leaves the usual difficulty (the small size of Λ against Planck
density) untouched. `OPEN`.

## 4. Condensate, entanglement, and refractoriness  `interpretation`

- **Entanglement.** Two excitations of one condensate are correlated "by construction", the EPR "paradox" dissolves, and Bell-inequality violation is expected because particles are not classically independent. This is a statement of interpretation. Bell's theorem constrains *local* hidden-variable models, and any non-local picture, including this one, is consistent with the violations; the page does not offer a prediction that distinguishes it from standard quantum mechanics. (The earlier text's "this is not a new interpretation" is accurate in that sense.)
- **Refractoriness.** The Bang broke a symmetry, and spontaneous symmetry breaking is one-directional on cosmological timescales; the Goldstone mode is massless and runs along the trough at σ = ½. Stars are read as local recondensation nodes, and stellar black holes as local re-cavitation events (echoes of the Bang at smaller scale). Standard astrophysics explains stars by gravitational collapse and the Jeans criterion; the page's recondensation threshold is an open problem (6 below).

## 5. The Bang as a phase transition; σ = ½ as the order parameter

| Phase | State |
|---|---|
| pre-Bang | normal phase (above T_c): "fixed-point space", acausal, no σ = ½ structure |
| t = 0 | the transition: cavitation of the normal phase instantiates the condensate |
| post-Bang | the superconducting phase; σ = ½ is the order parameter and governs causal structure |

Reading (`CONJECTURE`): the critical line is the order parameter of the
condensate; the Riemann Hypothesis says the condensate never fully loses
coherence on any off-line point ("the zeros of the order parameter are only on
the critical line"); the σ-facet table gains a column (σ = ½: order
parameter; σ = 1: normal-phase boundary; σ = 2: the medium itself). The same
caution as [13](13_omgwtf_rh_proof.md) applies: RH is open, and this reading
does not bear on it.

The proposed observational test is that "Riemann zero structure should appear
in the CMB power spectrum". **No test of this exists in the repository.** The
CMB directories use the Planck and WMAP spectra for a ptychographic
reconstruction (ePIE converged in 31 iterations to a loss of 5.7·10⁻¹³), which
concerns reconstruction of the spectrum, not zeros in it. `OPEN`.

"The Bang was necessarily acausal": causality is created by the Bang and cannot
itself be a causal event. The model identifies the acausal negative space with the
pre-Bang normal phase and with the interior of every black hole (σ → ∞,
Fermat-forbidden, [31](31_cavitation_causality_fermat.md) §6) and with the
"other side" of an ER = EPR wormhole. This is a philosophical statement about
the model, not a derivation.

## 6. Connections the earlier page drew

| Statement | Standing |
|---|---|
| the witches hat is the Mexican-hat potential of the condensate; the trough at Ω_ζΣ is its ground state; the brim at D* = 1 the phase boundary | `interpretation` ([29](29_witches_hat_paper.md) §3; [30](30_lambda_paper.md) §2 for the potential's features) |
| the flat rotation curve is the DC mode of the BEC at galactic scale, as in a type-II superconductor | `CONJECTURE`; no calculation; the inversion route to a halo fails ([29](29_witches_hat_paper.md) §4) |
| j_s is conserved by Noether's theorem for the U(1) symmetry of the condensate; the Goldstone mode is the Nambu–Goldstone boson | standard for a superfluid; the identification with the spacetime medium is the model |
| ER = EPR wormholes are Abrikosov flux tubes; black holes are vortex cores; flux quantisation gives the Bekenstein area spectrum | `CONJECTURE`; compare the Abrikosov lattice picture of the zeros ([75](75_abrikosov_lattice.md)); not computed |

## 7. Open problems (unchanged in substance)

1. Derive Λ from condensate properties, with zero free parameters.
2. The coherence length ξ: is ξ = c/H₀?
3. T_c in Planck units (the Planck temperature is ≈ 1.4·10³² K).
4. Abrikosov-vortex topology of black holes: does flux quantisation reproduce the Bekenstein area quantisation, and does the 168-pair structure ([31](31_cavitation_causality_fermat.md) §3) enter?
5. The Goldstone-mode dispersion ω(k): does it reproduce the CMB power spectrum at large scales?
6. The density threshold for local recondensation, in terms of V(n) and d*, and its relation to the Jeans condition.
7. (added 2026-11-13) Reproduce the observed deceleration–acceleration history, q(z) in §2, within the model.

## 8. Related pages

[29 The witches hat](29_witches_hat_paper.md) · [30 Lambda paper](30_lambda_paper.md) ·
[31 Cavitation, causality, Fermat](31_cavitation_causality_fermat.md) · [75 Abrikosov lattice](75_abrikosov_lattice.md) ·
[33 Gyroscope and compressibility](33_gyroscope_compressibility.md)
