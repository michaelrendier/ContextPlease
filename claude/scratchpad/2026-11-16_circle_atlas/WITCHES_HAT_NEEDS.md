# What I need to write a cursory cs-paper-code-conventions draft of each Witch's Hat part (2026-11-16)

Branch `witches-hat`; parent register `WitchesHat/README.md`; the Circle Atlas (`ValaQuenta/modules/circle_atlas`) is the CS paper for The Interface and the machinery under every part below. Each draft = assistant note first, Notation and Disambiguation (five labels, Post-Hoc rule), cold-running listings, `:CALCULATED` results, failures kept, a GenerationalLineage section before any GL results, ContextPlease appendix.

| Part | Can start now | What I still need from you |
|---|---|---|
| A. The hat as geometry (wiki 29, `ArdaQuenta/modes/witches_hat.py`) | yes: run the engine, record its output, keep the failed halo test (ρ ∝ r⁻⁶) | nothing; say if the animation should be regenerated |
| B. The dynamic path / L_(I\|O) (wiki 51, `l_io_photon_path`, `BulletCluster/L_IO_SPECIFICATION.md`) | the listing already runs | the observable to compare with data: which measured quantity is the photon path's signature, and the predicted sign/size, written before the test |
| C. The galactic cavity (SPARC; scripts 03–10, results on disk) | yes: all data and results exist | repair notebook 02 (invalid JSON, line 243): your call whether to repair or replace; which result you want as the headline |
| D. Dark matter is a shape (Bullet, Einstein crosses) | scaffold image, Chandra map, convergence code exist | (1) the exact RM-ratio test: ratio of what to what, predicted value; (2) real Stokes Q/U for a lens: none on disk. The Crab full-pol VLA set (requested, `CrabNebula/VLA_REQUEST_2026-11-16.md`) and the HST polarizers are the control; (3) which Einstein cross first (HE0435, Q2237, RX J1131, SDSS J1004 dirs exist) |
| E. CMB / BAO medium (CMB_FractalBoundary, CMB_PlasmaBoundary) | Planck TT and WMAP TT files are on the branch; notebooks need rerun | your go to rerun the five "confirmed" predictions; whether to fetch Planck SMICA maps (public, Mozilla UA) for the 2-D boundary test |
| F. Brim as turbulence (Crawford_NavierStokes) | no code: notes only | the computation: what D\* is operationally and which flow dataset (e.g. a public DNS set) the Ro = 1 test runs on |
| G. Medium's origin (cavitation, Bang, scar) | stubs | the claims you want tested, each with its number |
| H. Constants (d\*, Ω, four faces) | yes (arithmetic) | nothing |

## Telescope-data papers (the sub-papers that are mostly code on data)
For each: the data path on `/media/rendier/Telescope Data/`, the script that makes every figure (extracted verbatim into the paper), the scaffold image, and the table row in `WitchesHat/README.md`. Already on disk: SPARC (full), Bullet (BCData), EinsteinCrosses ×4, Dust (Pillars, Orion), JWST_SPARC_IFU, Planck foreground validation. New tonight: CrabNebula (JWST NIRCam F480M, HST WFPC2/NICMOS/ACS polarizers; VLA pending your links).

## The JWST background scaffold algorithm (so each paper can print it)
Recorded in `BulletCluster` git history, commit 8e482d2, file `optical/jwst/make_background.py` (later removed from the tree by a cleanup commit; I will restore it as a tracked, tested module):
1. take each filter's level-3 `i2d` mosaic (MJy/sr) from the SCI extension, NaN → 0;
2. reproject every filter onto one WCS grid (the longest-wavelength native grid, binned 2×) by `map_coordinates` order 1 through world coordinates;
3. chromatic assignment: shortest wavelengths → blue, middle → green, longest → red; filters sharing a channel are averaged;
4. white-balance each channel by its 99th-percentile positive value, set the black point to the 1st-percentile of positives;
5. Lupton et al. (2004, PASP 116, 133) asinh stretch through `astropy.visualization.make_lupton_rgb` (Q = 8, stretch = 99.5th percentile of R+G+B divided by 6): an intensity I = (R+G+B)/3 is compressed by asinh and each channel is scaled by f(I)/I, which keeps colour while compressing range;
6. optional overlay (Chandra gas, in pink, alpha-blended by a gamma-stretched percentile map); flip so north is up; trim the empty rotation border.
For the Crab I have ONE NIRCam image (F480M, grayscale): true colour needs ≥ 2–3 filters; the F150W2+F162M mosaic is 8.9 GB (tell me if you want it) and the MIRI mosaics are on MAST.
Where else a scaffold was made: Bullet (above); Pillars of Creation and HE 0435 under `BulletCluster/already_evaluated/`. Tell me if the Gemini-era scaffold scripts are somewhere other than git history.
