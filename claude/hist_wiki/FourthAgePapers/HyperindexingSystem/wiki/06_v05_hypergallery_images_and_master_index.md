# v05 · HyperGallery: images, spectral cubes, the JSON master index

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hypergallery.py` (459 lines). Notebooks: [`v05_gallery/`](../notebooks/v05_gallery/).*

**Dating.** Git: 2026-04-18. Placed after v04 (its `VectorAddress` adds `meta`) and before v06 (v06's adds `from_label(..., meta)`).

## What it is

- `HyperGallery(spec)`: the bijection over **pixel values** instead of characters. `ImageSpec` modes: BINARY (1 bit), GRAY8, RGB24, SPECTRAL (n bands × bit depth). An image with n values at depth D is a base-D numeral with n digits.
- `HyperIndex`: image and text records serialised to JSON; the JSON string is itself indexed, giving one master address ("moving all data = moving one address").
- `SpectralCube` and `spectral_address_range(band_constraints)`: the JWST-oriented search, described as bounding "the candidate image subspace" for pre-recombination images.

## Measured

- Exact round trips: binary 106×17 (1,802 values, 57 limbs), gray8 64×64 (4,096 values, 1,024 limbs), spectral IFU 16×16×50 bands at 16 bits (12,800 values, 6,400 limbs = 204,800 bits).
- Master index: 68,161 JSON characters → 14,090 limbs = 450,880 bits = **0.827** of the JSON's raw bits, i.e. log₂97/8 again. One address for many records, at the size of the records.
- **Defect 1 — `spectral_address_range` (the JWST search).** It returns one interval `[addr_mid − δ, addr_mid + δ]`. Checked exhaustively on 2×2 pixels, 2 bands, 2-bit depth (65,536 images) with band 0 constrained to [1, 2]: 4,096 images satisfy the constraint; the returned range (47,802 to 48,314, width 513) contains **129** of them; of the 513 images in the range only 129 satisfy the constraint; the satisfying set is **512 disjoint runs**. Cause: values are laid out pixel-major, band-minor, and the address is lexicographic in that order, so a band constraint fixes digits spread through the whole string including the leading ones. The satisfying set is a product set, not an interval.
- **Defect 2 — `index_image` cache key.** The cache keys on `values[:16]`. Two 8×8 images differing only in the last pixel receive the same label, and `regenerate(b)` returns `a`.

## Under permutation of the string

Permuting the pixels is permuting the digits; the address order is lexicographic in the digit order chosen. Defect 1 is what happens when a constraint is placed on a non-leading coordinate of a lexicographic address: it is not an interval. A correct search returns a union of intervals, or reorders the digits so the constrained band leads.

## Status

Distinct: the only image and spectral version. Continues, with the same two defects, in Callimachus v09 (v09 notebook 02 reproduces the cache defect).
