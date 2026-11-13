# 132 — Ptycho-Weak-Lensing

**Written 2026-11-12.** Engine `ValaQuenta/modules/ptycho_weak_lensing/` (v0.1), notebook 21, tests `ValaQuenta/tests/test_ptycho_weak_lensing.py`. Pointer, not authority: the code and Cody's current statement win.

**Why it exists.** The telescope experiment (ptychography of the space) needs a *calculated* mass map to match against a published shear / dark-matter layer (the control), and a polarization vector field as a separate image of the same experiment. Cody's question (2026-11-12): is weak lensing "already a type of implemented ptychography"?

**Answer, as built.** Not by itself: weak lensing is a direct linear inversion of a spin-2 field; the shear's phase is measured, not lost. The ptychographic structure is (1) overlapping pointings as probe windows over one real field κ with the object constraint B = 0 (ePIE/Kaczmarz), and (2) achromatic lensing — every band images the same ψ with a different PSF/source population — and (3) an intensity-only variant (|γ| alone), the genuine phase-retrieval case, which is OPEN here.

**Results (synthetic).** Gaussian-halo closed form 1e-3; KS round trip 1.5e-4; mass-sheet invisible 4e-16; rotation null moves the lens E → B; Q+iU from a scalar potential is pure E. With 3 of 9 pointings missing the ptychographic iteration beats naive stacking (corr 0.923 vs 0.864 at density 12; 0.825 vs 0.701 at density 3); at full coverage they are the same fixed point. Modulus-only retrieval stalls from uninformed starts and cannot fix the sign.

**Labels.** Lensing algebra ESTABLISHED (Kaiser & Squires 1993; Seitz & Schneider 2001; Bartelmann & Schneider 2001). Pointings-as-probes ePIE reading and modulus variant: THEORETICAL:CALCULATED. A link between spin-2 shear and J₂ / 0_RB is a hypothesis, untested.

**Targets.** Euclid DR1-Foundation (released 2026-11-12) covers MACS J0416 only among 20 tested lens fields; JWST has no polarimeter, so the polarization field must come from radio / HST polarizers / SOFIA / Planck. See `RiemannHypothesisProof` primer `PRIMER_2026-11-12_ENGINE_PAUSE_ALL_FINDINGS.md` for the RHP side and the browser page of candidates (session scratchpad).
