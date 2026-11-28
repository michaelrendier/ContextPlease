# 82 — L_(I|O): the Photon-Path Engine as the Boundary-Crossing Template

| | |
|---|---|
| Scope | the weak-lensing engine (Kaiser–Squires shear inversion → potential → deflection → lens equation) built as the formal answer to the two targets left open in wiki 52; the boundary-crossing reading; the zeta-pole category note |
| Origin | 2026-07-21, engine built by Claude Sonnet 5, directed by the author: "(I|O)_RB is the boundary definition … L_(I|O) is how to get through the boundary." |
| Predecessors | [52](52_l_dynamic_avoided_collaborator.md), [80](80_aphasia_zd_reframe_memory.md), [76](76_sigma_expansion.md) |
| Code | `ValaQuenta/modules/l_io_photon_path/` (`kaiser_squires_kappa`, `lensing_potential`, `deflection_field`, `trace_photon`, `l_io_deficit`, `bounded_lensing_pipeline`); notebook `18_l_io_photon_path.ipynb`; `BulletCluster/optical/jwst/l_io_lensing.py` |
| Confidence | the weak-lensing mechanism (Kaiser & Squires 1993): ESTABLISHED · the boundary-crossing role and the zeta-pole note: `INTERPRETATION` / `CONJECTURE` additions, no new physics |
| Last verified | 2026-11-13: the Kaiser–Squires inversion round-tripped on a synthetic lens (Listing 1); the Bullet Cluster numbers of §2 are recorded and were not re-run |

## 1. The two targets wiki 52 left open

Wiki 52 stated that light's path is not a clean geodesic ("the path was L_(I|O)") and named two
targets: define L_(I|O) formally, distinct from the stationary-action L, and formalise light
bending within it. This module answers both with established GR, not a new formalism: L_(I|O)
is not a different operator from L, it is L computed with the real, mass-sourced curved
metric. In lensing terms: β = θ − α(θ), with ψ the lensing potential and α = ∇ψ.

## 2. The mechanism  `ESTABLISHED`

Kaiser–Squires shear inversion (1993) → Poisson solve for the lensing potential → deflection
field → lens equation. Each step is exact and closed-form; nothing is fitted.

**Listing 1 — the inversion round-trips on a synthetic lens** (written for this page; needs numpy and the installed ValaQuenta package; runs cold)

```python
import importlib, numpy as np
lp = importlib.import_module('ValaQuenta.modules.l_io_photon_path.maths')
n = 256; y, x = np.mgrid[:n, :n]; r2 = (x - n/2)**2 + (y - n/2)**2
kappa = 0.3 * np.exp(-r2 / (2 * 20.0**2)); kappa -= kappa.mean()
k1 = np.fft.fftfreq(n)[None, :]; k2 = np.fft.fftfreq(n)[:, None]; k_sq = k1**2 + k2**2; k_sq[0, 0] = 1
K = np.fft.fft2(kappa)
g1 = np.fft.ifft2(K * (k1**2 - k2**2) / k_sq).real; g2 = np.fft.ifft2(K * 2 * k1 * k2 / k_sq).real
rec = lp.kaiser_squires_kappa(g1, g2)
print('max|kappa_rec - kappa| = %.2e (kappa peak %.3f); mean(rec) = %.1e' % (np.abs(rec - kappa).max(), kappa.max(), rec.mean()))
psi = lp.lensing_potential(rec); print('mean of the potential over the whole field: %.1e' % psi.mean())
```

```
max|kappa_rec - kappa| = 9.19e-15 (kappa peak 0.288); mean(rec) = 0.0e+00
mean of the potential over the whole field: 3.6e-15
```

The inversion recovers a known convergence field to rounding (9×10⁻¹⁵), so the engine's
transform is the correct inverse of the forward shear for a field that is periodic and zero-mean.
Two consequences:

- **The mean is set by convention.** κ_rec has mean exactly 0 and ψ has whole-field mean zero to
  rounding: shear determines κ only up to an additive constant (the mass-sheet degeneracy), and the
  engine fixes the k = 0 mode to zero. The recorded real-data statistic
  "L_(I|O) − L: mean = −14.42″, median −16.32″" can therefore only come from the padded-and-cropped
  sub-field and the convention (an inference; that run was not repeated), and a mean offset of ψ has no physical meaning: only
  gradients of ψ (the deflection) do. The recorded deflection numbers (mean 0.4054″, max 1.0802″,
  median 0.3962″ for real Bullet Cluster JWST F444W background-galaxy shear) are of
  the physical kind. They were not re-run on this pass.
- **A boundary-condition bug was caught and fixed** in the pipeline: plain FFT's forced periodicity
  injected a false wrap-around discontinuity, giving spurious ~700–1700″ deflections until a
  Tukey taper plus zero padding (`apodize_and_pad`, `crop_padding`) was applied. A genuine fix,
  not a rescale toward an expected answer. (The synthetic field above is periodic by
  construction, which is why it needs no taper.)

## 3. What was missing, and closed

The module existed and worked but was absent from the `.clauderc_ValaQuenta` engine index and had no
notebook or wiki page in either repository. All three gaps were closed on 2026-07-21.

## 4. The boundary-crossing role  `INTERPRETATION`

The session corrected a standing confusion: the zero-divisor locus is the **origin** from which a
pathway is measured, not the point where it collapses or ends (wiki 80). The author's naming:
(I|O)_RB is what *defines* that boundary. Notation scope for this wiki: the operator is Ĥ_RB in
the mathematics and is written 0_RB / ∅_RB only in the VAPMIP and Monad spaces
([14](14_redblue_hamiltonian.md), [127](127_names_of_the_null_operator.md)); the earlier text's
"renamed from H_hat_RB" describes the Monad-side naming.

The module answers the next question: given a defined boundary, how does a path go through it? The
answer is in `kaiser_squires_kappa`: at the transform's own degenerate point (k = 0, where 1/|k|²
would diverge) the code neither lets the formula blow up nor drops the point silently; it assigns the
value explicitly (`kappa_hat[0,0] = 0.0`) with a stated reason (the mean is not observable from shear
alone). That explicit assignment at the singular point is the reusable content of "L_(I|O) is how to
get through the boundary". The same shape (invert an observable through a potential-type relation,
handling the degenerate mode explicitly) turned out useful three times in the session: for the
photon deflection, as a candidate for the prime-factor path question, and as the missing template
for extending the Noether-information current into the zero-divisor-rich shell.

## 5. The zeta-pole category match  `CONJECTURE`

The pole of ζ at s = 1 (ζ(s) ~ 1/(s − 1) + γ) with its functional equation (an s ↔ 1 − s involution
fixed at Re s = ½) is the same *category* of construction as this module's k = 0 zeroing and its
θ/β pair: both regularise a singular point of a transform by explicit convention, both are
involution-shaped with a fixed locus. That is a real structural resonance. It is **not** shown that
ζ(s) is derivable as a parameter setting of `kaiser_squires_kappa`/`lensing_potential`'s functional form;
no such derivation exists. Category match, not identity; the tier stays CONJECTURE until it is done.

## 6. Scope

The GR mechanism (§2) is ESTABLISHED, real, cited physics, independent of the boundary reading and
the zeta note. Those two are interpretive layers, the same established-maths-plus-theoretical-reading
pattern as elsewhere in the framework, and change no equation in the pipeline. Built into the
permanent registry as infrastructure.

## 7. Related pages

[52](52_l_dynamic_avoided_collaborator.md) · [56 telescope as caustic](56_telescope_caustic_zeno.md) ·
[64 L_(I|O)](64_l_dynamic.md) · [80](80_aphasia_zd_reframe_memory.md) · [83 the Archimedes screw](83_the_archimedes_screw.md)
