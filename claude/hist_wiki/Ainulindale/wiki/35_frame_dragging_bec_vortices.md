# 35 — "Frame dragging is not frame dragging": quantized BEC vortices and the bobbing galaxy

| | |
|---|---|
| Status | **First capture (2026-06-03); `CONJECTURE`.** The SPARC counts are a recorded evaluation (§4); two physical numbers and the Tully–Fisher step of the earlier page were wrong and are corrected (§§3, 5) |
| Predecessors | [32](32_superconducting_medium.md), [33](33_gyroscope_compressibility.md) |
| Code and data | `PTorrent/peval/sparc_σface.peval` (the recorded evaluation); `FourthAgePapers/DM_GalacticCavity/data/SPARC/Rotmod_LTG/` (175 rotation-curve files); `FourthAgePapers/DM_GalacticCavity/` (pre-registration, `dark_matter_cavity.py`, `02_sparc_analysis.ipynb`) |
| Last verified | 2026-11-13: the SPARC files recounted and J = V_obs/V_bar recomputed (Listing 1); the Gravity Probe B figures recomputed (Listing 2) |

## 1. The proposal

Lense–Thirring frame dragging (a rotating body twists the local inertial
frames) has been observed: Gravity Probe B, LAGEOS, and spin effects in binary
black-hole mergers. The proposal is that the *interpretation* is wrong: if the
medium is a superfluid BEC ([32](32_superconducting_medium.md)) there is no
viscosity to "drag" and a spinning body instead nucleates quantized vortex
lines, with circulation Γ = n·h/m (n an integer, m the constituent mass; the
quantum of circulation h/m is standard superfluid physics, `ESTABLISHED`). The
observed precession is then the response to the vortex field, "not a dragged
fabric". `CONJECTURE`; the equivalence with GR is not shown (§3).

## 2. Healing length and the halo  `CONJECTURE`

Every BEC vortex has a healing length ξ, the core radius within which the
density falls to zero. In the model, inside ξ superfluidity breaks (∇·u ≠ 0,
σ → ∞, the black-hole analogue); outside it the bulk is incompressible
(σ ≤ 2). The galactic dark-matter halo is read as the vortex field around the
galaxy, its radius the healing length of the cosmological BEC at galactic mass
scales, "no dark-matter particles".

*Correction.* The earlier page said the NFW profile (ρ ∝ 1/r inside the scale
radius, ∝ 1/r³ outside) "is the energy-density profile of a vortex in a BEC:
not a fitted profile, a derived one". NFW was obtained as a fit to cold-dark-matter
N-body halos; a straight vortex in a Gross–Pitaevskii condensate has a
density profile that rises from zero at the core to the bulk value over a
healing length (the tanh²-type core profile), and no derivation of the NFW
profile from it is given. The statement is withdrawn; the halo-from-vortices
reading is open.

## 3. Lense–Thirring restated: the numbers

Gravity Probe B (Earth, a polar orbit at r ≈ 7027 km) predicted:

| Effect | GR prediction | Recomputed | Measured (GP-B, as recalled) |
|---|---|---|---|
| geodetic (de Sitter) | 6606 mas/yr | 6605.0 | 6601.8 ± 18.3 mas/yr |
| frame dragging (Lense–Thirring) | 39.2 mas/yr | 40.8 | 37.2 ± 7.2 mas/yr |

The earlier page gave "39 milliarcseconds/year for geodetic, 0.041 mas/yr for
Lense–Thirring". These are wrong: 39 mas/yr is the frame-dragging effect, the geodetic
precession is 6606 mas/yr, and 0.041 is in *arcseconds* per year (41 mas/yr).
(The recomputed 40.8 uses Earth's angular momentum J = 5.86·10³³ kg m²/s and
the orbit-averaged formula GJ/(2c²a³); the 39.2 mas/yr published prediction
includes the orbit geometry of the actual experiment. The measured figures are
from memory and are to be checked against the GP-B papers.)

**Listing 2 — the two GR precessions** (written for this page; runs cold)

```python
G, c, J, a, GM = 6.674e-11, 2.998e8, 5.86e33, 7.027e6, 3.986e14
mas_per_yr = 3.156e7 * 206265e3
print('Lense-Thirring GJ/(2c^2 a^3)    =', round(G * J / (2 * c**2 * a**3) * mas_per_yr, 1), 'mas/yr')
print('geodetic 3/2 (GM)^1.5/(c^2 a^2.5)=', round(1.5 * GM**1.5 / (c**2 * a**2.5) * mas_per_yr, 1), 'mas/yr')
```

```
Lense-Thirring GJ/(2c^2 a^3)    = 40.8 mas/yr
geodetic 3/2 (GM)^1.5/(c^2 a^2.5)= 6605.0 mas/yr
```

The BEC statement: Ω_LT = Γ_vortex/(2πr²) · n_vortex(r), "exactly the GR formula
because the vortex field is the curved metric in the rotating frame; the two
descriptions are dual". GR gives Ω_LT ∝ GJ/(c²r³). The BEC expression has the
dimension of a rate, but it reproduces the 1/r³ law only if the vortex
density falls as n(r) ∝ 1/r, a function the page does not supply, and the mass
m_BEC is unspecified. "Exactly, not approximately" is therefore **not
established**; the duality is the proposal. The claimed advantages (quantisation at small scales;
a minimum frame-dragging scale set by the healing length; termination of the
dragging at black-hole formation) are consequences of the model, not tested.

## 4. SPARC: what was recorded, and what it shows

SPARC (Lelli, McGaugh & Schombert 2016, AJ 152, 157) is 175 late-type galaxies
with rotation curves and baryonic decompositions. The recorded evaluation
(`sparc_σface.peval`, dated 2026-06-03, framework v1.218) states:

| Quantity | Value |
|---|---|
| galaxies / data points | 175 / 3,391 |
| method | J_ratio = V_obs/V_bar(r); σ-face from the "buoyancy table"; r_transition where J crosses 1.0 |
| σ-face counts | ½: 1,053 (31.1%) · 1: 1,927 (56.8%) · 2: 410 (12.1%) · ∞: 1 (0.03%) |
| galaxies with a transition (J crosses 1) | 97 |
| hits of d* = 0.246 within 5% | **14 (fraction 0.08)** |
| mean d_ratio (r_transition / r_max) | **0.2833** against the predicted 0.246 |

The earlier page read these as "the galaxy is bobbing in the σ-face dimension"
and said the d* = 0.246 prediction failed only because the denominator was the
observed R_max and "the natural denominator is R_virial": "the framework is
correct, the denominator needs R_virial". Standing: the d* prediction as
registered **failed**: 14 hits in the sample (8%) and a mean 15% above the
prediction. Choosing a different denominator after seeing the result is a new
hypothesis and not a rescue; a pre-registration for it is needed
(`FourthAgePapers/DM_GalacticCavity/` holds the existing one). The failed result is
kept here and in the peval.

**Listing 1 — J = V_obs/V_bar on the SPARC files** (written for this page; runs
cold from `FourthAgePapers/DM_GalacticCavity/data/SPARC/Rotmod_LTG`)

```python
import glob, math, statistics
vals, ng = [], 0
for f in glob.glob('*_rotmod.dat'):
    ng += 1
    for line in open(f):
        if line.startswith('#') or not line.strip():
            continue
        r, vo, e, vg, vd, vb = map(float, line.split()[:6])
        v2 = vg * abs(vg) + 0.5 * vd * abs(vd) + 0.7 * vb * abs(vb)
        if v2 > 0:
            vals.append(vo / math.sqrt(v2))
print('galaxies', ng, ' points', len(vals))
print('median J', round(statistics.median(vals), 3),
      ' fraction J>1', round(sum(v > 1 for v in vals) / len(vals), 3),
      ' fraction |J-1|<0.05', round(sum(abs(v - 1) < 0.05 for v in vals) / len(vals), 3))
```

```
galaxies 175  points 3389
median J 1.658  fraction J>1 0.937  fraction |J-1|<0.05 0.055
```

With the conventional mass-to-light ratios (Υ_disk = 0.5, Υ_bulge = 0.7) the
file has 3,389 usable points (the peval's 3,391 differs by two points; the peval's
rule for the baryonic velocity is not stated, and this page does not reproduce its σ-face counts because
the "buoyancy table" thresholds are not in the file). The recomputed J has median 1.66 and
exceeds 1 at 93.7% of points: the observed rotation exceeds the baryonic
prediction almost everywhere, which is the standard missing-mass signal that any
account (particle dark matter, MOND, or the BEC model) must supply. Only 5.5% of
points lie within 5% of J = 1.

## 5. The bobbing and Tully–Fisher  (error in the earlier derivation)

The model: a galaxy bobs in the medium with ω_bob = √(g_eff/H); the flat curve
is the Stokes-drift equilibrium v_flat = ½A²kω; and "this gives v_flat ∝ √M, the
Tully–Fisher relation". **That does not follow:** the baryonic Tully–Fisher
relation is v_flat⁴ ∝ M_baryonic (v ∝ M^{1/4}). A relation v ∝ M^{1/2}
(equivalently v² ∝ M) is a different law and disagrees with observation. The
statement "the exponent 4 follows from the BEC dispersion relation at the
healing-length scale" is not derived on the page. `OPEN`: derive v⁴ ∝ M, and
explain the observed small scatter, from the model.

## 6. Related pages

[10 JWST engine](10_jwst_engine.md) · [29 The witches hat](29_witches_hat_paper.md) ·
[32 The superconducting medium](32_superconducting_medium.md) · [34 Hypercomplex spectral relativity](34_hypercomplex_spectral_relativity.md) ·
[37 AGN alignment and the BEC vortex](37_agn_alignment_bec_vortex.md)
