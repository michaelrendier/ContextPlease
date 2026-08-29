# 10 — JWST ENGINE  Spectral Pixel → 𝕆

**Module:** `jwst`  **Version:** 0.111  **Confidence floor:** THEORETICAL

## Overview

JWST NIRCam spectral pixel module. 8 filter intensities → 8 octonion components → one 𝕆 element per sky pixel.

The Cayley-Dickson tower provides a natural address space for spectral data: wavelength λ maps to radial coordinate r ∈ (0,1), intensity maps to algebra element norm.

## NIRCam Filters

| Filter | λ (nm) | r |
|--------|--------|---|
| F090W | 900 | 0.000 |
| F115W | 1150 | 0.072 |
| F150W | 1500 | 0.171 |
| F200W | 2000 | 0.314 |
| F277W | 2770 | 0.537 |
| F356W | 3560 | 0.763 |
| F410M | 4100 | 0.914 |
| F444W | 4440 | 1.000 |

## Spectral → Octonion Mapping

```
Ψ = I_0·e₀ + I_1·e₁ + ... + I_7·e₇ ∈ 𝕆
|Ψ| = √(Σ I_k²)
```

8 filters → 8 octonion components. The Fano plane structure of 𝕆 means the 7 imaginary components (e₁..e₇) encode the wavelength relationships between filters.

## Cayley-Dickson Pixel Address

Each pixel has a full tower address:

```
alg_ℝ: mean intensity (scalar)
alg_ℂ: (short-wave mean, long-wave mean)
alg_ℍ: (I₀, I₂, I₄, I₆) alternating
alg_𝕆: all 8 components
```

Pixel coordinates (x,y) encoded as base-10000 integer: `addr = x·10000 + y`.

## Synthetic Spectra

Two synthetic spectra for testing (real FITS ingest is TODO):

**Hydrogen (Paschen series):** Gaussian proximity to Pa-α (1875nm), Pa-β (1282nm), Pa-γ (1094nm), Pa-δ (1005nm).

**Stellar (blackbody T=5000K):** Planck function evaluated at each filter wavelength, normalised.

## Equations

| Name | Status | Description |
|------|--------|-------------|
| `spectral_to_octonion` | THEORETICAL ◈ | 8 filters → 𝕆 element |
| `cd_spectral_address` | THEORETICAL ◈ | Full CD pixel address |
| `synthetic_hydrogen` | ESTABLISHED ✓ | Paschen series test spectrum |
| `synthetic_stellar` | ESTABLISHED ✓ | Blackbody T=5000K |
| `lambda_to_r` | ESTABLISHED ✓ | λ (nm) → r ∈ (0,1) |

## TODO

- FITS file reader for real NIRCam pixel data
- Ingest pipeline: FITS → 8-component intensity vector → 𝕆
- Spectral line identification via HyperWebster Fano address
- Multi-pixel field: NxM pixel array → NxM array of 𝕆 elements

## Shell commands
```python
jwst_oct([1.0]*8)    # 8 intensities → 𝕆 element
jwst_H()             # hydrogen test spectrum
jwst_star()          # blackbody test spectrum
lambda_r(2000.0)     # 2000nm → r
```
