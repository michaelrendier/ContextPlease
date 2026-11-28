# 10 — JWST Engine (spectral pixel → 𝕆)

| | |
|---|---|
| Module | `jwst` — `ValaQuenta/modules/jwst/` |
| Class | `JWSTModule` |
| Version | 0.111 |
| Confidence floor | THEORETICAL |
| API page | `ValaQuenta/wiki/jwst.md` |
| Notebook | `ValaQuenta/notebooks/core/10_jwst.ipynb` |
| Last verified | 2026-11-13, against the live registry (5 equations) and `maths.py` |

## 1. What it does

Eight NIRCam filter intensities become the eight components of one
octonion, one 𝕆 element per sky pixel. Wavelength is mapped linearly to a
radial coordinate r; the pixel also receives a full Cayley–Dickson address
(its ℝ, ℂ, ℍ and 𝕆 views) and an integer position code.

This module is a mapping and a test fixture. It reads no telescope data: the
two spectra it generates are synthetic. Real JWST data work is in the
telescope tooling (`ptycho_weak_lensing`, and the data pipelines in the
VAPMIP and ValaQuenta repositories), not here.

## 2. Filters and radial coordinate

`lambda_to_r(λ) = (λ − λ_min) / (λ_max − λ_min + 10⁻⁹)`, with
λ_min = 900 nm and λ_max = 4440 nm. Values from `FILTER_LAMBDA`:

| Filter | λ (nm) | r |
|---|---|---|
| F090W | 900 | 0.000 |
| F115W | 1150 | 0.071 |
| F150W | 1500 | 0.169 |
| F200W | 2000 | 0.311 |
| F277W | 2770 | 0.528 |
| F356W | 3560 | 0.751 |
| F410M | 4100 | 0.904 |
| F444W | 4440 | 1.000 |

(An earlier version of this table listed 0.072, 0.171, 0.314, 0.537, 0.763
and 0.914 for six of these rows. Those do not reproduce under the formula
above and are replaced.) The mapping is linear in wavelength, not
logarithmic.

## 3. Spectrum → octonion → address

```
Ψ = I₀·e₀ + I₁·e₁ + … + I₇·e₇ ∈ 𝕆,      |Ψ| = √(Σ I_k²)
```

Fewer than eight intensities are padded with zeros. The pixel address
(`cd_spectral_address`) is:

| Layer | Content |
|---|---|
| ℝ | mean of the eight intensities |
| ℂ | (mean of I₀…I₃, mean of I₄…I₇): short-wave and long-wave means |
| ℍ | (I₀, I₂, I₄, I₆) |
| 𝕆 | all eight |
| position | `pixel_x · 10000 + pixel_y` |
| Fano path | `int(|I_k| · 7) mod 7` for each component |

The position code is base 10⁴. (One docstring in the module says "base-100";
the code is base 10⁴, and this page follows the code.) For intensities of all
1.0 at pixel (3, 7): `pixel_addr = 30007`, ℝ = 1.0, ℂ = [1.0, 1.0],
norm = 2.828…, Fano path = [0]×8.

**Listing 1 — the pixel's four layers** (`modules/jwst/maths.py`,
`cd_spectral_address`; extracted: docstring removed, the octonion packing
inlined, runs cold)

```python
def cd_address(intensities, pixel_x=0, pixel_y=0):
    comps = (list(intensities) + [0.0] * 8)[:8]
    return {
        'pixel_addr': pixel_x * 10000 + pixel_y,
        'alg_R': sum(comps) / 8.0,
        'alg_C': [sum(comps[:4]) / 4.0, sum(comps[4:]) / 4.0],
        'alg_H': [comps[i] for i in (0, 2, 4, 6)],
        'alg_O': comps,
    }

print(cd_address([1.0] * 8, 3, 7))
```

```
{'pixel_addr': 30007, 'alg_R': 1.0, 'alg_C': [1.0, 1.0], 'alg_H': [1.0, 1.0, 1.0, 1.0], 'alg_O': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}
```

## 4. Synthetic spectra, and a defect found while checking this page

`synthetic_spectrum(kind)` supports `'hydrogen'`, `'stellar'` and `'flat'`.

- **Stellar:** the Planck function at T = 5000 K at each filter wavelength,
  normalised to its maximum.
- **Flat:** eight 1.0s.
- **Hydrogen:** meant to peak near the Paschen lines Pa-α 1875 nm, Pa-β
  1282 nm, Pa-γ 1094 nm and Pa-δ 1005 nm, as a Gaussian (width 200 nm) of the
  distance to the *nearest* line. **The code takes `min` over the four
  Gaussians, not `max`, which gives the Gaussian of the *farthest* line.**

  Measured output of `synthetic_spectrum('hydrogen')` (2026-11-13):
  4.8·10⁻¹¹, 2.0·10⁻⁶, 2.2·10⁻³, 1.8·10⁻¹¹, 1.5·10⁻³⁴, … — the largest value
  is 2·10⁻³. With `max` the first four values would be 0.76, 0.93, 0.31, 0.68.

  Status: **defect, not fixed** (ValaQuenta was not edited during the wiki
  overhaul). The registered equation `synthetic_hydrogen` is labelled
  ESTABLISHED; until the `min` is corrected that label overstates it.
  Logged for the next ValaQuenta change.

## 5. Equations

| Name | Tier | Parameters |
|---|---|---|
| `spectral_to_octonion` | THEORETICAL | `intensities` |
| `cd_spectral_address` | THEORETICAL | `intensities`, `pixel_x`, `pixel_y` |
| `synthetic_hydrogen` | ESTABLISHED (see §4) | — |
| `synthetic_stellar` | ESTABLISHED | — |
| `lambda_to_r` | ESTABLISHED | `wavelength_nm` |

Console commands: `jwst_oct(intensities)`, `jwst_H()`, `jwst_star()`, `lambda_r(nm)`.

## 6. Session

```
>>> registry.run('jwst.lambda_to_r', {'wavelength_nm': 2000.0})
{'wavelength_nm': 2000.0, 'r': 0.31073446327674836, 'lambda_back': 1999.9999999996892}
```

## 7. Not in this module

A FITS reader, ingestion of real NIRCam pixels, spectral-line identification
through the HyperWebster Fano address, and multi-pixel (N×M) fields. These
were listed as planned in earlier versions of this page; none exists in
`modules/jwst/`.

## 8. Related pages

[09 HyperWebster](09_hyperwebster_engine.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md) ·
[132 Ptycho weak lensing](132_ptycho_weak_lensing.md)
