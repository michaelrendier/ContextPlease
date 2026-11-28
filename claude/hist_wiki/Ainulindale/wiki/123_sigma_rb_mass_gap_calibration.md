# 123 — σ_RB Mass-Gap Calibration: Three Sigmas, and What Does Not Conflate

> d* faces (all four are needed to chart ln(10) in Universal Native Space):  
>   d*         = 0.24600          the value the code runs with (Boundary, σ_ζ=½ plane)  
>   d*_taut    = 0.246307201473  A_π/ln10, the Flow (radial unit)  
>   d*_RG      = dimension 8; numeric OPEN, no closed form  the Stability (centre r=0)  
>   d*_ln(10)  = 0.5671432904   d*_taut·ln10 = A_π, the Translator (log bridge)  
> Full story of d*: Ainulindale/wiki/17_alpha_omega_d_star.md; ~/.clauderc_canonical_maths @RCCM_FOUR_DSTAR; FourthAgePapers/DStarRG  


| | |
|---|---|
| Scope | a cross-test of `bao_mass_gap.py` against `oblique_gear_test.py`: the three objects named σ in the codebase; Δ fed into σ_RB's tilt; the strut-blindness of σ_self; a T7 mean-sensitivity anomaly; the "rectifier law" |
| Measured | 2026-09-23; continues [75b](75b_bao_mass_gap_engine.md), [14](14_redblue_hamiltonian.md), [25](25_sedenion_manual.md) |
| Code | `ValaQuenta/bao_mass_gap.py`; `ContextPlease/claude/scratchpad/2026-08-31_oblique-gear/oblique_gear_test.py` (`sigma_rb`, `tilt_axis`, `p_red_blue`, `sigma_self`) and `ANOMALY_CHASE.md` |
| Confidence | the algebra of strut-blindness and the rectifier law: ESTABLISHED (re-derived and re-run, Listing 1) · **one number of the 2026-09-23 record does not reproduce** (§2) · T7: OPEN |
| Last verified | 2026-11-13: Listing 1 executed; the formulas of `sigma_rb`, `p_red_blue` and `sigma_self` were read from the source; the T7 drift runs were not repeated |

## 1. The problem this page exists to prevent

"σ" names three different objects in the codebase; each is correct in its own file, and the risk is carrying a result from one into a sentence about another ([85](85_the_apex_path.md) §8 tabulates the wider collision):

| Name | Where | What it is |
|---|---|---|
| **σ_ζ** | `ValaQuenta/modules/h_rb_hat/maths.py`, `sigma` parameter | Re(s), the Dirichlet/Euler coupling exponent; a single float. Facets 0, ½, 1, 2, real-only ([14](14_redblue_hamiltonian.md) §4). **No string/M-theory facet at this level.** |
| **σ-strata** | [25](25_sedenion_manual.md) §IX, σ₀ … σ₄ | ordinal nested-inclusion levels of the sedenion (how many of the 16 components are switched on); not a continuous exponent. σ₄ = all 16 active, "String / ground state" |
| **σ_RB** | `oblique_gear_test.py` | σ_RB[k] = ψ[k]·conj(ψ[k⊕4]), ψ ∈ ℂ¹⁶; tilt = Re (an 8-vector, driven), axis = Im (an 8-vector, the conserved anchor). `σ_self` (red/(red + blue), the code's name) is a separate derived scalar built from σ_RB |

Where "mass gap → string theory" already lives: [25](25_sedenion_manual.md) §VII at the σ-strata level, **not** the other two: GAP = the e₁₅ component → the zero-divisor boundary → 7 imaginary octonion units → G₂ holonomy → 11D = 4 observable + 7 compact → M-theory, one vacuum; the same chain (11 = 4 + 7, G₂ = Aut 𝕆) as `bao_mass_gap/maths.py`'s `mtheory_compactification()`. It is a compactification-scale argument (Δ sets a geometric scale), not a σ-facet assignment. The module's own docstring makes the stronger claims "GAP eliminates the string landscape (10⁵⁰⁰ → 1 vacuum)" and "GAP ≈ 1/(1000√2) (the identity holds to 3 significant figures)"; the first is the framework's reading and the second is the 0.035 % agreement of [120](120_symmetry_breaking_is_the_instrument.md) §5.

## 2. The calibration test  `ESTABLISHED` (algebra), one number corrected

Forward propagation, not derivation: Δ = 0.000707357533 (`bao_mass_gap.py`'s residue Ω_ζΣ − D\*·ln 10, with D\* = 0.246; Listing 1 reproduces 0.000707357533) is typed into σ_RB's real part as the mean tilt across all 8 struts; what is tested is whether the machinery accepts it and what it does. Re(σ_RB) = tilt = Δ on all 8 struts by construction (the input, not a finding).

**σ_self is strut-blind** once each pair's energy is held fixed at a constant E. From the source: `red = Σₖ|ψ[k] + ψ[k⊕4]|²/2`, `blue = Σₖ|ψ[k] − ψ[k⊕4]|²/2` over the 8 pair representatives, so red − blue = 2Σ Re(ψ[k]·conj ψ[k⊕4]) = 2 Σ tilt and red + blue = Σ|ψ|². With each pair's energy |ψ[k]|² + |ψ[k⊕4]|² = E, red + blue = 8E and red = 4E + Σtilt, hence

```
σ_self = ½ + Σtilt/(8E) = ½ + mean(tilt)/E = ½ + Δ/E
```

independent of how the tilt is distributed across the struts (exact algebra). Listing 1 builds three different strut distributions with the same mean Δ and the same pair energy E = 1 and reads σ_self from `red/(red + blue)`: all three give **0.500707357533** (= ½ + Δ). That lands deep in the **σ_ζ = ½ (Quantum Mechanics / Riemann)** facet, nowhere near string theory: the string/M-theory route belongs to the σ-strata / compactification mechanism above and does not emerge from feeding Δ into σ_RB's tilt; the two should not be merged into one claim.

**A number that does not reproduce.** The 2026-09-23 record gives σ_self = 0.500707357179 at E = 1 and says it was "verified to 12 digits". The arithmetic above gives ½ + Δ = 0.500707357533, a difference of 3.5×10⁻¹⁰ at the tenth digit; the algebra and Listing 1 agree with each other and not with the recorded digits. The cause was not located (a different D\*/Ω value or an embedding detail in the original run are candidates); the qualitative result (strut-blind, σ_self = ½ + Δ/E) is unaffected, and the recorded "12 digits" is not reproduced.

## 3. The rectifier law  `ESTABLISHED` (derived)

An energy-unnormalised embedding, ψ[k] = ψ[k⊕4] = √|tilt_k| (signed so that the tilt is reproduced), let strut information leak into σ_self; flagged under the chase-every-anomaly discipline and resolved to an exact law. Derivation: for a pair with tilt tₖ > 0, a = b = √tₖ gives |a + b|²/2 = 2tₖ to red and nothing to blue; for tₖ < 0, a = −b gives 2|tₖ| to blue; so red = 2Σ_{t>0} t, blue = 2Σ_{t<0}|t|, red + blue = 2Σ|tₖ|, and with Σtₖ = 8Δ:

```
σ_self = ½ + 4Δ / Σₖ |Δ + λ·uₖ|        (tₖ = Δ + λ uₖ, u a fixed unit strut direction, λ the strut scale)
```

Two regimes (Listing 1): below the first sign-flip threshold all tₖ share Δ's sign, blue = 0 and **σ_self = 1.0 exactly**, flat (the struts are invisible); above threshold the deviation σ_self − ½ falls as an **inverse first power** of λ (log–log slope −1.00 over λ = 10²…10⁵; the record's −0.9985), matching the closed form's large-λ asymptote 4Δ/(λΣ|uₖ|); inverse-square is ruled out.

**Listing 1 — strut-blindness and the rectifier law** (written for this page; needs numpy; runs cold)

```python
import numpy as np, math
O = 0.5671432904097838; D = O - 0.246 * math.log(10); print('Delta = %.12f' % D)
rng = np.random.default_rng(0); E = 1.0
for trial in range(3):
    tilt = rng.uniform(-0.3, 0.3, 8); tilt += D - tilt.mean()                     # mean tilt = Delta, |tilt_k| <= E/2
    phi = 0.5 * np.arcsin(np.clip(2 * tilt / E, -1, 1)); a = np.sqrt(E) * np.cos(phi); b = np.sqrt(E) * np.sin(phi)   # pair energy E, Re(a conj b) = tilt
    red = np.sum(np.abs(a + b) ** 2) / 2; blue = np.sum(np.abs(a - b) ** 2) / 2
    print('distribution %d: strut spread %.3f  sigma_self = red/(red+blue) = %.12f ; 1/2 + Delta/E = %.12f' % (trial, tilt.std(), red / (red + blue), 0.5 + D / E))
u = rng.normal(size=8); u -= u.mean(); u /= np.linalg.norm(u)
def rect(lam):
    t = D + lam * u; a = np.sign(t) * np.sqrt(np.abs(t)); b = np.sqrt(np.abs(t)); red = np.sum(np.abs(a + b) ** 2) / 2; blue = np.sum(np.abs(a - b) ** 2) / 2
    return red / (red + blue), 0.5 + 4 * D / np.sum(np.abs(D + lam * u))
for lam in (1e-6, 1e-5, 1e-4, 1e-3, 1e-1, 1e2, 1e5):
    s_emb, s_law = rect(lam); print('lambda = %8.0e : sigma_self (embedding) = %.12f ; closed form = %.12f' % (lam, s_emb, s_law))
lams = np.logspace(2, 5, 13); dev = np.array([rect(l)[0] - 0.5 for l in lams]); print('log-log slope of (sigma_self - 1/2) against lambda over 1e2..1e5: %.4f' % np.polyfit(np.log(lams), np.log(dev), 1)[0])
```

```
Delta = 0.000707357533
distribution 0: strut spread 0.195  sigma_self = red/(red+blue) = 0.500707357533 ; 1/2 + Delta/E = 0.500707357533
distribution 1: strut spread 0.216  sigma_self = red/(red+blue) = 0.500707357533 ; 1/2 + Delta/E = 0.500707357533
distribution 2: strut spread 0.161  sigma_self = red/(red+blue) = 0.500707357533 ; 1/2 + Delta/E = 0.500707357533
lambda =    1e-06 : sigma_self (embedding) = 1.000000000000 ; closed form = 1.000000000000
lambda =    1e-05 : sigma_self (embedding) = 1.000000000000 ; closed form = 1.000000000000
lambda =    1e-04 : sigma_self (embedding) = 1.000000000000 ; closed form = 1.000000000000
lambda =    1e-03 : sigma_self (embedding) = 1.000000000000 ; closed form = 1.000000000000
lambda =    1e-01 : sigma_self (embedding) = 0.511803986118 ; closed form = 0.511803986118
lambda =    1e+02 : sigma_self (embedding) = 0.500011803986 ; closed form = 0.500011803986
lambda =    1e+05 : sigma_self (embedding) = 0.500000011804 ; closed form = 0.500000011804
log-log slope of (sigma_self - 1/2) against lambda over 1e2..1e5: -1.0000
```


## 4. A real correction, filed against T7  `OPEN`

`oblique_gear_test.py`'s T7 docstring claims drift tracks the 7 tilt struts only ("the axis holds, mean doesn't matter"). Measured otherwise on the 2026-09-23 run (not repeated here): same struts, three means, a 200-step gain = 0.05 gear-train run: drift 3.6640 (mean Δ), 3.9194 (mean 0), 3.9303 (mean −Δ): the mean moves the drift, asymmetrically in ±Δ and outside an 8-sample same-scale control's spread (0.006–0.04). **Open**: not yet distinguished from the ordinary chaotic sensitivity of a 200-step nonlinear iterated rotation against a genuinely Δ-specific effect; it needs many more trials or a local-sensitivity (Lyapunov) measurement. Background: `ANOMALY_CHASE.md` (the balanced-ψ drift is a growth from a 10⁻¹⁶ residual at rate λ ≈ 5.9–6.1 per unit flow time, the hyperbolic saddle of [110](110_qm_in_gr_gr_in_qm.md) §5).

## 5. Status

**OPEN / THEORETICAL.** An ad hoc cross-test between two existing scripts; neither is wired into ValaQuenta's `EquationModule`/engine formulary, so nothing here earns `:CALCULATED` (that suffix requires the machinery to reproduce a result from its own construction, not accept an injected input unchanged). **Solid:** the strut-blindness of σ_self (exact algebra, re-run); the rectifier's inverse-first-power law (exact derivation, re-run). **Open:** whether T7's mean-sensitivity is Δ-specific or generic chaotic noise; whether σ_RB has any principled, non-injected route to *producing* Δ rather than accepting it without contradiction. **Corrected:** the recorded digits 0.500707357179 (§2).

## 6. Related pages

[75b](75b_bao_mass_gap_engine.md) · [14](14_redblue_hamiltonian.md) · [25](25_sedenion_manual.md) · [85](85_the_apex_path.md) · [120](120_symmetry_breaking_is_the_instrument.md)
