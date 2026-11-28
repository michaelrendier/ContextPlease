# 36 — Gravity is time: the transversal, rotational "up", and the Great Wall

| | |
|---|---|
| Status | **First capture (2026-06-03); `INTERPRETATION`/`CONJECTURE`.** One exact weak-field statement is isolated and checked (§1); the sheet-and-void table is a proposal with no test run |
| Predecessor | [35](35_frame_dragging_bec_vortices.md) |
| Code | none; Listing 1. (The Vera Rubin and WMAP "ptorrents" the page says were about to be run have not been run: no result exists) |
| Last verified | 2026-11-13: Listing 1 executed |

## 1. "Gravity is the gradient of the time rate"  (the exact form)

Standard GR says gravity affects time; the page says they are one thing. The
precise, correct version of that statement is the weak-field limit
(`ESTABLISHED`): for a slowly moving test body the acceleration is
a = −c²∇√(−g_tt) = −∇Φ, with Φ the Newtonian potential, because the rate of a
clock at rest is dτ/dt = √(1 − 2GM/rc²) ≈ 1 + Φ/c². So the Newtonian "force"
of gravity on slow bodies is the spatial gradient of the clock rate. That is the
content of "σ is the time rate; dσ/dr is gravity" once σ is replaced by
dτ/dt. For fast bodies (light) the spatial metric contributes equally
(the factor of 2 in light deflection), so "gravity is only the time gradient" is
not exact beyond the slow limit.

**Listing 1 — the clock-rate gradient reproduces g** (written for this page;
runs cold)

```python
import math
G, M, c, r = 6.674e-11, 5.972e24, 2.998e8, 6.371e6   # Earth
rs = 2 * G * M / c**2
rate = math.sqrt(1 - rs / r)
g_from_gradient = c**2 * (rs / (2 * r**2)) / rate      # c^2 d/dr sqrt(1 - rs/r)
print('clock-rate offset 1 - dtau/dt =', f'{1 - rate:.3e}')
print('c^2 d(rate)/dr               =', round(g_from_gradient, 4), 'm/s^2')
print('GM/r^2                       =', round(G * M / r**2, 4), 'm/s^2')
```

```
clock-rate offset 1 - dtau/dt = 6.960e-10
c^2 d(rate)/dr               = 9.8195 m/s^2
GM/r^2                       = 9.8195 m/s^2
```

*Correction.* The page says bodies fall toward slower time because that path
is "shorter in proper time" and is the path of least action. Free fall
**maximises** the proper time between two events (a geodesic is a maximal-τ
path for timelike curves); the body is not minimising its proper time. "Toward
slower clocks" is right for the direction of the force on a slow body, as the
gradient above shows. The sentence "ds² = −c²dt² + dx² makes time and space
interchangeable, so curvature is the time gradient" is not a derivation: that
flat metric has no curvature.

## 2. Time dilation as "traversal cost" in the vortex field  `CONJECTURE`

The model: light always moves at c; near a mass the BEC vortex density per
coordinate unit is higher, so a photon traverses more medium per unit coordinate
distance and appears slower from outside; time dilation = traversal cost per
coordinate unit. The standard formula √(1 − r_s/r) = √(1 − 2GM/rc²) is read as
the ratio of free to vortex-threaded traversal speed, vanishing at r_s. This
reproduces the formula by definition and predicts nothing new; the "Data
Transversal" language (terms go to the data) is the software metaphor of
[34](34_hypercomplex_spectral_relativity.md) §4. "Singularity" is replaced by a
diverging traversal cost; the coordinate-to-proper-distance mapping, not the
medium, breaks at the horizon (§7). No calculation distinguishes this from the
Schwarzschild coordinate picture.

## 3. A self-organising neutral-buoyancy surface  `CONJECTURE`

In the BEC medium there is a direction (up = decreasing vortex density =
decreasing σ) but no pre-existing surface; the σ = ½ isosurface (time at the
reference rate, J_ratio = V_obs/V_bar = 1, buoyancy cancelling gravity) is said
to emerge as a fixed point of the dynamics, with stars, flat-rotation-curve
galaxies and the Sloan Great Wall "at σ = ½". Test of the galactic claim: the
SPARC J = V_obs/V_bar exceeds 1 at 93.7% of points and lies within 5% of 1 at
5.5% ([35](35_frame_dragging_bec_vortices.md) §4), so J = 1 is not where
flat-rotation-curve galaxies sit under the standard mass-to-light convention. A
"surface at every scale" table (Planck: vacuum; stellar: equilibrium; galactic:
flat curve; cluster: pressure balance; cosmic: sheets) is a classification and
not a result.

## 4. Rotational "up" and why disks are flat  `interpretation`

The model: a rotating body nucleates vortex lines along its axis, densest on
the axis and lowest in the equatorial plane, so rotational "up" is toward the
equator and the disk is the equatorial σ = ½ surface; spheroidal (pressure-
supported) galaxies have no preferred axis and a spheroidal surface. The
standard account is angular-momentum conservation with dissipation (a rotating
gas cloud collapses along the axis, not across it); that spirals are thin and
ellipticals are pressure-supported is observed. The vortex reading predicts the
same morphology and does not yet add a distinguishing quantity.

## 5. The Sloan Great Wall  `CONJECTURE`

The Sloan Great Wall is a sheet of galaxies and clusters about 1.37 billion
light-years long (Gott et al. 2005: 1.38 Gly; one of the largest known
structures; whether it is a gravitationally bound structure is debated). Standard
cosmology: an early density fluctuation that collapsed into a sheet. The model:
the cosmic BEC has vortex structure (voids vortex-free and "fast"; filaments
vortex-dense, σ = 1–2; cluster cores σ → ∞; sheets at σ = ½ as "the attractor"),
and the Great Wall *is* the σ = ½ isosurface, with matter accumulating there
"as water at a surface". No position of the Wall has been computed from this
model; the open thread asks whether it sits at the predicted isosurface given
ΛCDM matter distribution. The table (voids σ < ½; sheets σ = ½; filaments σ = 1–2;
clusters σ → ∞) is a proposal.

## 6. Coordinate compression versus medium compression  `interpretation`

Extending [33](33_gyroscope_compressibility.md): "more space in shorter distance"
is the coordinate mapping, not compression of the medium; the medium stays
incompressible, and the event horizon is where the coordinate-to-proper mapping
fails (coordinate distance → 0 while medium-threaded distance → ∞), not where the
medium is destroyed. In GR terms this is the familiar statement that the horizon
is a coordinate singularity of the Schwarzschild chart and not a curvature
singularity (`ESTABLISHED`); the BEC reading adds the claim that the medium
continues through. Standing: restatement, not new content.

## 7. Planned evaluations (none run)

- **Vera Rubin (LSST), ~40·10⁹ objects:** the σ-face map expected to show the cosmic web (voids σ < ½, Wall σ = ½, filaments σ = 1, cores σ = 2).
- **WMAP/Planck:** acoustic peaks "are the σ = ½ crossings in the primordial BEC"; the cold spot (an apparent supervoid association, itself debated) as a vortex-free region.

The page says both "will, when run, produce" these. Neither has been run, so
they are predictions to be registered (the σ-face rule must be fixed before looking;
[35](35_frame_dragging_bec_vortices.md) §4 for the one place such a rule was
recorded and what it gave).

## 8. Open threads (kept)

1. Derive the Sloan Great Wall position from a BEC-vortex cosmological model.
2. CMB acoustic peaks as BEC standing-wave nodes: are the peak positions the σ = ½ crossings in k-space?
3. Vera Rubin evaluation when available.
4. The self-similar σ = ½ surface across scales as a single figure.
5. Formalise "coordinate compression ≠ medium compression" (chart degeneration versus physical singularity).
6. The SMIG as the σ = ½ surface of the observable universe projected onto S¹⁵.

## 9. Related pages

[25 Sedenion manual](25_sedenion_manual.md) §9 (the SMIG) · [33 Gyroscope and compressibility](33_gyroscope_compressibility.md) ·
[35 Frame dragging and BEC vortices](35_frame_dragging_bec_vortices.md) · [37 AGN alignment](37_agn_alignment_bec_vortex.md) ·
[72 The cosmic telescope](72_the_cosmic_telescope.md)
