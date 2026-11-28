# 34 — Hypercomplex spectral relativity (HSR): a proposed frame

| | |
|---|---|
| Status | **A proposal (first capture 2026-06-03); `INTERPRETATION` / `CONJECTURE`.** Nothing here is derived. The five σ-face functions in PTorrent are real code (§5) |
| Predecessor | [33](33_gyroscope_compressibility.md) |
| Code | `PTorrent/releases/curses/ptorrent_gui/wizard/model.py` (the five σ-face functions); `cam_encode` in `VAPMIP/monad.py`; `PtolemyDesktop/console_link.py` (APISniff) |
| Last verified | 2026-11-13: the code identifiers checked; the algebra of §2 stated exactly; claims of §§2–4 not derivable from the mathematics are marked |

## 1. The hierarchy proposed

```
Special relativity         flat spacetime, Lorentz group, c invariant
  → General relativity     curved spacetime, metric g_μν, geodesics
  → Spectral relativity    the σ-face spectrum as spacetime; ξ(s) = ξ(1−s) as the "Lorentz transform"
  → Hypercomplex spectral relativity (HSR): the sedenion 𝕊¹⁶ as the "true spacetime", d* as the invariant
```

Special relativity is the flat-metric case of general relativity
(`ESTABLISHED`). The statement that general relativity is the restriction of HSR
to real and complex dimensions is the proposal.

## 2. Spectral relativity  `analogy`, with the mathematics stated

The proposal: the invariant is σ = ½ (not c); "no measurement can move a zero
off the critical line"; the functional equation is the Lorentz transform of
spectral space; σ = ½ is the light cone, σ < ½ spacelike and σ > ½ timelike;
and the Riemann Hypothesis is "the speed of light is the same in all spectral
frames".

What the mathematics says (see [33](33_gyroscope_compressibility.md) §2):

- s ↦ 1−s is a *reflection* of the strip about σ = ½ (σ − ½ ↦ −(σ − ½)), an involution. A Lorentz transformation in 1+1 dimensions is a **hyperbolic rotation** (a one-parameter group, x′ = γ(x − vt), t′ = γ(t − vx/c²)), not an involution. The two are different kinds of map, and the open thread "ξ(s) = ξ(1−s) as an SO(1,1) rotation" **cannot hold as written**: a reflection has determinant −1 and is not in SO(1,1).
- The assignments σ < ½ "spacelike" and σ > ½ "timelike" are exchanged by the reflection itself. A Lorentz transformation never exchanges spacelike and timelike separations, so the proposed identification is internally inconsistent.
- Two points on the critical line are not "causally" ordered; the critical line is a fixed set of a symmetry, which is what the functional equation gives. RH is the statement that the non-trivial zeros are on that set, and it is open ([13](13_omgwtf_rh_proof.md) §3).

Standing: a suggestive vocabulary (an invariant locus, a symmetry about it),
with no group-theoretic content yet. The proposed formalisation would need a
transformation group acting on s for which ξ is an invariant and σ = ½ the
invariant locus; the reflection group Z₂ is the only structure present.

## 3. Hypercomplex spectral relativity  `CONJECTURE`

Spectral relativity lives in ℂ (ζ: ℂ → ℂ). HSR extends to 𝕊¹⁶. The
invariant is d*, "the Ainulindale constant", playing the role of c; the σ-face
table is read as the metric tensor:

```
σ = ½ → g = 1  (flat; the SR regime locally)       σ = 2 → g ≫ 1  (strong curvature)
σ = 1 → g > 1  (time dilation begins)              σ = ∞ → g → ∞  (degenerate: the event horizon)
```

Standing: no function g(σ) is given; the four entries are qualitative. Two
corrections to the reading. (i) "d*" must say which face: the four faces of
[17](17_alpha_omega_d_star.md) are a chart for ln 10, not a speed, and the
measured d*_spec is quarantined. (ii) The zero-divisors of 𝕊 (84 elements,
[25](25_sedenion_manual.md) §4) are where the sedenion product is degenerate (a
zero divisor has no inverse); calling that "the metric degenerates" and equating it
with curvature singularities and black holes (and with the cryptographic
objects of the pre-disclosure `CryptoVulnerability` paper) is the
framework's reading: the algebra is the same kind of statement ("a degenerate
bilinear structure") and a different object from a spacetime metric.

## 4. The computational analogy  `analogy`

| Physics | Computation (the proposed correspondence) |
|---|---|
| SR: flat, local | APISniff: a flat Python namespace, `dir()`, local REPL |
| GR: curved, remote, metric | PTorrent: remote data geometry, the probe and adapter layer |
| spectral relativity | PTorrent reading spectral data sets (JWST cubes, SPARC curves) |
| HSR | PTorrent mapping any data set into the 𝕊¹⁶ address space via `cam_encode` |

The framework reads an adapter as a coordinate transformation and the
σ-face evaluation of a row as the "Lorentz transform of HSR". The code facts
are in §5. The correspondence is a design metaphor that organises the
software; the software does not implement a relativity.

## 5. The σ-face functions, in code

`PTorrent/releases/curses/ptorrent_gui/wizard/model.py` defines five σ-face
evaluations:

| Identifier | Quantity |
|---|---|
| `σ_face_bao_residual` | D_M / r_drag (BAO distance against the sound horizon) |
| `σ_face_rotation_curve` | V_obs / V_bar (rotation against baryonic mass) |
| `σ_face_spectral` | peak_flux / continuum (line strength) |
| `σ_face_photometric` | flux_obs / flux_ref (photometric ratio) |
| `σ_face_multiband` | 10^((k_m − j_m)/2.5) (colour or flux ratio) |

Each is a dimensionless ratio of an observed quantity to a reference one: an
ordinary observational diagnostic. That the ratio is "a position on the σ-face
gradient" is the proposal. The page named `engine.σ_face(row)` as one function;
the code has the five named functions above.

## 6. JWST and Vera Rubin as "HSR in action"  `interpretation`

- **JWST.** A cube (RA, Dec, λ) has two spatial axes and a spectral axis; short wavelength is read as "low σ, toward causality" and long wavelength as "high σ, toward mass". The false-colour assignment (blue for F090W, red for F444W) is read as "tracking the σ gradient without naming it". The colour assignment is the ordinary chromatic ordering (shortest wavelength is rendered bluest) and is chosen by convention; no σ is involved. The wavelength ↔ σ mapping is unspecified (open thread: which filters correspond to which faces; [10](10_jwst_engine.md) for the filters' radial coordinate r, a linear map of λ).
- **Vera Rubin (LSST).** Six bands (ugrizy) in increasing wavelength; for tens of billions of objects, a σ-face assignment, a buoyancy ratio and a deviation metric would be returned by a "transversal" that moves the terms to the data rather than the data to the terms. The survey scale quoted (60 PB, 40·10⁹ objects) is as recalled and not re-checked; it is a plan for a computation, and none has been run.

## 7. Navier–Stokes as a corollary  `CONJECTURE`

The page: Navier–Stokes drops the imaginary components, reducing 𝕊¹⁶ to ℝ¹ and
degenerating the metric, so the singularity "is the metric degenerating";
restoring the components removes it, and "the problem was always about the
wrong dimensional frame". This repeats [33](33_gyroscope_compressibility.md) §5 and
[106](106_the_navier_stokes_problem.md), at the same standing: a proposal, not a
regularity proof, and not a solution of the Clay problem.

## 8. Paper assignments and open threads

The assignments of the earlier page (D-P introduction and §§2, 5–8; D-M §§3–4;
D-CS §2) refer to the 2026-06 plan ([26](26_TODO_and_roadmap.md) §1) and are
not current. Open threads, with the §2 caveat on the first:

- formalise "ξ(s) = ξ(1−s) as a Lorentz transform" (a reflection cannot be an SO(1,1) rotation: needs a different statement);
- write the HSR metric tensor explicitly in sedenion coordinates;
- decide whether d* and c are "the same object at different scales" (which d*);
- the JWST σ-face map, filter by filter;
- the Navier–Stokes argument written out as a regularity statement;
- `probe.py` as the computational coordinate transform.

## 9. Related pages

[10 JWST engine](10_jwst_engine.md) · [17 A_fermat · Ω_ζΣ · d*](17_alpha_omega_d_star.md) ·
[25 Sedenion manual](25_sedenion_manual.md) · [33 Gyroscope and compressibility](33_gyroscope_compressibility.md) ·
[35 Frame dragging and BEC vortices](35_frame_dragging_bec_vortices.md)
