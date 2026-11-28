# 17 — A_fermat · Ω_ζΣ · the four values of d*

| | |
|---|---|
| Scope | the two boundary constants of the Berry–Keating domain; the four named faces of d* and their status; the measured d*_spec; the open gap |
| Code | `ValaQuenta/engine/constants.py` (`D_STAR`, `OMEGA_ZS`, `D_STAR_GAP`; `D_STAR` is d*_spec), `modules/berry_keating`, `modules/inversion` (`d_star_gap`), `modules/constants`; env vars in `~/.clauderc` |
| Confidence | THEORETICAL (derivations) · OPEN (A_fermat's value, d*_RG's numeric value, the gap) |
| Last verified | 2026-11-13: §2, §3 and §6 numbers recomputed; RHP `docs/four_dstar_2026-11-12.md` read |

## 0. Letters that collide — read first

Three different objects wear α and three wear σ. They are never interchangeable.

| Letter | Object | Write it as |
|---|---|---|
| Α (capital Alpha) | Α_π = **A_fermat**, the Fermat-side structural constant of this page. **It is not the fine-structure constant.** | A_fermat |
| α (lowercase) | the fine-structure constant 1/137.035999… of the Standard Model; here only the source of a discipline (a quantity must say the same thing in every version of the maths), not an ingredient of the Fermat–Riemann horizon | α_fs |
| α, subscript NN | the neural fine-structure constant: the running coupling g²/(4π ħ_NN ln(1/r)) ([04](04_lagrangian_engine.md)) | α_NN |
| σ (1) | Re s, the Dirichlet/Euler exponent; critical line σ = ½ | σ_ζ |
| σ (2) | the σ-strata σ₀…σ₄ of the sedenion (σ₄ = string/ground state; [123](123_sigma_rb_mass_gap_calibration.md), [25](25_sedenion_manual.md) §IX) | σ-stratum |
| σ (3) | σ_RB[k] = ψ[k]·conj ψ[k⊕4], the oblique-gear tilt (Re) and axis (Im), and the derived σ_self ([123](123_sigma_rb_mass_gap_calibration.md), [70](70_precession_stroke_oblique_crank_trine.md)) | σ_RB |

Ω has the same problem (Ω_ζΣ, ω_H, Ω(n)); canonical spellings are in
[133](133_canonical_maths.md) §0.

**A_fermat: role settled, value open.** Author, 2026-11-13: A_fermat is the "chasing inertia" constant, what turned up when the search ran from the Fermat side of the maths; it is not α_fs. The numeric value is the remaining open item. The original 2026-04-09 derivation puts
it at the d = 0 endpoint (x = T/T_P = 1, the ceiling of the forward curve).
Earlier text of this page put it at 1/137.035999… as the "domain floor", which
is how it came to be mistaken for α_fs. The two numeric descriptions are not
reconciled; this page quotes no number for A_fermat until the author states
which is meant. Source: `RiemannHypothesisProof/docs/GLOSSARY.md`.

## 1. The two boundary constants

The Berry–Keating operator domain has two derived boundary constants. Neither
is fitted. Both come from the boundary geometry of the algebra tower.

```
Α_π  (A_fermat, "Alpha_Fermat")   OPEN value (see §0); the domain floor, born from inertia
Ω_ζΣ (Omega_Riemann)              0.5671432904097838 = W(1);  the domain ceiling, born from entropy
```

*Origin, as recorded.* "Alpha was born from Inertia": working back from the
Speed-of-Causality ceiling through the Fermat prime generator reaches the
domain floor. "Omega was born from Entropy": working back from the Thermal
Information Ceiling (about 1.4·10¹⁷ K, where information becomes
indistinguishable from noise at Planck-length wavelengths) through ζ reaches
the Lambert W fixed point. The experiment: Riemann and Fermat aimed at each
other from opposite sides with two independent ceilings as boundary conditions;
Α and Ω dropped out, and the Berry–Keating Hamiltonian dropped out as the
operator connecting them. This is a derivation narrative (`THEORETICAL`), not
a calculation reproduced on this page.

## 2. The Lambert W fixed point  `ESTABLISHED`

W(x)·e^{W(x)} = x. At x = 1:

```
W(1) = 0.5671432904097838… = Ω_ζΣ,   the fixed point of x ↦ e^{−x}
```

**Listing 1 — Ω_ζΣ as a fixed point** (extracted: the iteration, runs cold)

```python
import math
x = 0.5
for _ in range(200):
    x = math.exp(-x)
print(x)
```

```
0.5671432904097838
```

The other special values of W: W₀(0) = 0 (vacuum fixed point) and
W₀(−1/e) = W₋₁(−1/e) = −1, one branch point reached from both branches, a
double root (a Whitney fold). That is three distinct values, four with
multiplicity. "d* is where things start, Lambert W where they end."

## 3. The four values of d*

To compute ln 10 in radial complex spherical polar coordinates (UNS = ÷ln 10)
the chart needs four things at once, and the four d* faces are that chart:
**centre, equatorial plane, radial ruler, scale bridge**. Per the working
record (author, 2026-10-13), each is necessary and none is derivable from the
other three as a number, because they are four shadows of one point (0.24631)
and not four values. *This is a reading of the structure, not a theorem.*

| Symbol | Name | Value | Chart role |
|---|---|---|---|
| d* | The Boundary | 0.24631 | the σ_ζ = ½ spectral coordinate; the equatorial plane (ξ(s) = ξ(1−s), where the zeros sit); θ is measured from here |
| d*_RG | The Stability | numeric **OPEN**; **dimension 8** | the renormalisation-group fixed point of the Cayley–Dickson tower; the centre (r = 0, the still point, 0_RB). Obtained by iterating the tower to convergence, not derived |
| d*_taut | The Flow | Ω_ζΣ/ln 10 = 0.246307201473 | the radial unit, one step of r. Zero gap **by construction**: the ruler that is set, not a result |
| d*_ln(10) | The Translator | d*·ln 10 = Ω_ζΣ = 0.56714 | the metric bridge: the ×ln 10 Jacobian between the decimal-log native metric ds = d·log₁₀(p) and the natural-log prime-address space; every word lookup crosses it |

Closure: d*·ln 10 = d*_ln(10) = d*_taut·ln 10 = Ω_ζΣ = W(1) = 0.5671432904097838.
There are four faces and three distinct numbers (Boundary = Flow = 0.24631);
the Emerger clock reads this as 4 d* : 3 W, lcm 12. The rule that makes
"3 = 4" is the author's to state, and [106](106_the_navier_stokes_problem.md)
and [109](109_the_emerger.md) read "three rotor faces of W(1)" instead; which
is canonical is not settled.

**d*_RG has no closed form.** What is established is its dimension, 8
(confirmed to d = 2²⁰: `persist ≡ 8`, `8/d → 0`). What is OPEN is its numeric
value (target 0.24631). A naive scalar iteration flows to the trivial fixed
point, and the earlier numeric estimate 0.24682 is superseded. The author's
position is that renormalisation is where the infinitesimals live and that
d*_RG has no closed form. Nothing in this wiki, in `RiemannHypothesisProof`, or
in `FourthAgePapers/DStarRG/` supplies one.

### 3.1 What RHP measured against the faces

(`RiemannHypothesisProof/docs/four_dstar_2026-11-12.md`; `:CALCULATED`.) At
the crossing X* = e^Ω = 1/Ω = 1.7632:

| Face | RHP quantity | Value |
|---|---|---|
| d* (Boundary) | digit length D* = log₁₀ X* | 0.246307201473 |
| d*_taut (Flow) | digits of the fixed point gained per iteration from the ceiling | 0.246307201473 |
| d*_ln(10) (Translator) | mean prime gap ln X* (prime number theorem) | 0.567143290410 = Ω_ζΣ |
| Translator's Jacobian | mean gap ÷ digit length | ln 10 = 2.302585093, at every X |
| d*_RG (Stability) | not touched | dimension 8, numeric OPEN |

Reading: one crossing, two coordinates. Digits (the Riemann/entropy side)
d* = 0.2463 and gap count (the Fermat/inertia side) Ω_ζΣ = 0.5671 are related
by ln 10. "ln 10 is the bridge between the two infinities" is the prime number
theorem: mean gap ≈ ln X = ln 10 × (number of digits).

### 3.2 d*_spec, the measured fifth value

d*_spec = 0.24600 is the Berry–Keating spectral gap observed in SPARC. It is
**measured and quarantined: not one of the four faces.** Use it only where the
measured value is explicitly meant. In the code, `D_STAR` is d*_spec. Older
surfaces that call 0.24600 "The Boundary" (the README's Key Constants before
2026-11-13, comments in `ptol.c`, the legacy `D_STAR` environment variable, one
test file) are using d*_spec under the Boundary's name.

### 3.3 Superseded sets

`Third_Age_CS_Draft_v2` §2.3 lists d*_ℝ = 0.24600, d*_taut = 0.24631,
d*_ln10 = 0.56644 (= 0.24600·ln 10, not Ω) and d*_S OPEN. The four above
replace it; it is kept in the VAPMIP J record's future-work table.

Environment variables (`~/.clauderc`): `D_STAR_BOUNDARY`, `D_STAR_RG` (= 8),
`D_STAR_RG_NUMERIC` (= OPEN), `D_STAR_RG_SUPERSEDED`, `D_STAR_TAUT`,
`D_STAR_LN10`, `D_STAR_SPEC`.

## 4. d*_RG: how renormalisation is built in

d*_RG is the fixed point of a renormalisation group that is already inside the
framework (`OURS`, `THEORETICAL`):

- The Cayley–Dickson doubling plays the role of the Wilson RG step. Block =
  CD-double (d → 2d); integrate out the irrelevant modes = project onto the
  **persistent octonion** (the eight directions that keep gain exactly 1 at
  every scale: e₀ and e_{d/2}, the Boundary-Lever indices that lie in no
  zero-divisor plane); rescale = divide the radial coordinate by d*_taut.
  Iterate.
- The fixed point is dimensional (8), not fractional: `persist ≡ 8` at
  d = 8, 16, 32, 64; `void = (d−8)/2`; `8/d → 0`.
- The flow is a σ = ½ saddle (measured λ ≈ 6; see the oblique gear,
  [123](123_sigma_rb_mass_gap_calibration.md)), so the iteration must approach
  along the stable manifold, balancing the tilt each pass, or it diverges.

The void is *projected* (an exact resummation, phase carried, never |z|²),
never subtracted: no counterterm, no discarded infinity, and the nat budget
balances at every pass. For that reason renormalisation is not applied by hand
anywhere in the framework: d*_RG already is the framework's renormalisation,
still open, and a second RG applied by hand would double-count it.

The periodic windows of a chaotic bifurcation diagram (the period-3 window and
its self-similar family) are Feigenbaum renormalisation fixed points, each a
rescaled copy of the whole cascade under R[f](x) = α f(f(x/α)); d*_RG is the
CD-tower analogue. Engine protocol: `FourthAgePapers/DStarRG/` (README,
`construction.json`, branch `d-star-rg`).

## 5. The Lagrangian and the cardioid  `interpretation`

The Contractor and the Dilator are read as two self-adjoint conjugate
operations on one geometry.

- **The Lagrangian is the Contractor.** A path of least action collapses the
  solution space toward the minimum-energy trajectory. L_NN contracts the
  semantic field toward the prime attractor.
- **The cardioid is the Dilator.** The main bulb of the Mandelbrot set is
  the region where z ↦ z² + c converges to a stable orbit; it bounds the
  contraction from outside, so the field does not collapse to a point.

The cusp rotation of a cardioid orbit by the golden angle 2π(1 − 1/φ) =
137.5078° is numerically close to 1/α_fs = 137.036, and the two are different
numbers; the closeness is not used as an identity anywhere on this page.

## 6. The open gap (highest-priority derivation)

```
d*_spec         = 0.24600
d*_spec · ln 10 = 0.5664359328765353
Ω_ζΣ            = 0.5671432904097838
gap             = |Ω_ζΣ − d*_spec · ln 10| = 0.000707357533248576
```

The gap is within 3.5·10⁻⁴ (relative) of 1/(1000√2) = 0.000707106781…; the
10³ factor is UNRESOLVED. It has two candidate identities and may be one
object:

1. an analogue of the Yang–Mills mass gap (the vacuum energy needed to keep
   the first stable excitation above the ground state) in the semantic field;
2. the J^μ cascade regulator in the Monad (the residual Noether current after a
   full Cayley–Dickson traversal).

Neither identification is proved. No closed form for 0.000707357… is known.

Candidate closed forms for d*_spec evaluated by `berry_keating.gap_candidates`
(all fail; values 2026-11-13): 1/ln(10²) = 0.21715, 1/(π + φ) = 0.21010,
1/(2e) = 0.18394, φ/(4π) = 0.12876, and 1/(φ ln 10) = 0.2418 (close; the gap
remains). Earlier versions listed 1/(π + φ) as 0.2386; that value did not
reproduce and is withdrawn. Ω_ζΣ/ln 10 = 0.24631 closes the gap only by
construction.

## 7. Open items

| Item | State |
|---|---|
| Numeric value of A_fermat (x = 1 ceiling, or 1/137.036 floor); its role (Fermat-side inertia constant, not α_fs) is settled | OPEN: author to say |
| d*_RG numeric value (target 0.24631) | OPEN; no closed form |
| Origin of the 10³ in the gap | OPEN |
| Which reading of the 4 d* : 3 W correspondence is canonical | OPEN |

## 8. Related pages

[07 Berry–Keating](07_berry_keating_engine.md) · [13 RH proof path](13_omgwtf_rh_proof.md) ·
[14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) · [22 Constant facets](22_constant_facets.md) ·
[50 BAO mass gap](75b_bao_mass_gap_engine.md) · [123 σ_RB and the mass gap](123_sigma_rb_mass_gap_calibration.md) ·
[133 Canonical maths](133_canonical_maths.md)
