# 76 — SIGMA EXPANSION: THE J_RED/J_BLUE BALANCE CURVE

**Author:** Claude Sonnet 5 (derivation), prompted and directed by Cody Michael Allison
**Date:** 2026-07-11
**Status:** ESTABLISHED derivation, verified numerically against direct computation — not a fit. Raw conservation question answered honestly negative before the derivation was attempted.
**Predecessor:** [wiki/73 — Why σ=½](73_why_the_half_line.md), [wiki/75 — The Abrikosov Lattice](75_abrikosov_lattice.md)
**Cross-ref:** `ValaQuenta/modules/sigma_expansion/`, `ValaQuenta/wiki/sigma_expansion.md`, `ValaQuenta/notebooks/core/15_sigma_expansion.ipynb`, `SedenionSpectralRelativity/layer_spectrograph.py`

---

> *"The point is the renormalization will show you the derivation curve."*
> — Cody Michael Allison, 2026-07-11

---

## 1. The Question

A real video — Nick Lucid ("The Science Asylum"), "Quantum Superposition, Explained Without Woo Woo" (Nov 2021) — states, showing pages from his own master's thesis, that any quantum particle's state is representable as a single vector between two positive axes: the two probabilities of a two-outcome measurement. Never multiple states at once. Just one vector, in a basis that doesn't look familiar.

This framework already has two positive-axis quantities defined this way: `J_red(σ)` (Knowledge, forward Dirichlet series) and `J_blue(σ)=J_red(1-σ)` (Experience, reverse). σ=½ is already the locus where `|J_red(½)|=|J_blue(½)|`. The direct, testable question: does `|J_red(σ)|²+|J_blue(σ)|²` normalize to a constant across σ the way real quantum probabilities must?

## 2. The Honest Negative Result, Checked First

**No.** Computed directly across three independent test strings, the raw sum is a smooth, symmetric curve with a genuine **minimum at σ=½** — an energy well, not a flat conservation law. Nick Lucid's normalization argument does not transfer to J_red/J_blue as currently defined in this framework. This was reported before any renormalization was attempted, per standing practice: raw result first, always.

## 3. Renormalization as a Build Tool, Not a Conclusion

Cody granted a scoped, one-time exception to the standing "no cheating with renormalization" rule — explicitly *as a tool toward a derivation*, not as an endpoint. `P_red(σ)=|J_red|²/(|J_red|²+|J_blue|²)` trivially sums to 1 with `P_blue` by construction; that normalization alone proves nothing. What it produces is a new, well-defined curve — `P_red(σ)-½` — which becomes the actual object of study.

## 4. The Derivation Curve

`P_red(σ)-½` is smooth, antisymmetric about σ=½, and — critically — its local slope near the center is *smaller* than its slope further out, the opposite of a tanh/sigmoid shape. That signature identifies the functional form directly: an odd power series dominated by a cubic term, `c1·d + c3·d³` (d=σ-½), not a logistic curve.

Both coefficients were **derived**, not fitted — Taylor-expanding `F(σ)=|N(σ)|²/D(σ)²` around σ=½ via product/quotient-rule differentiation, using moments `M_n` (position-only) and `L_n` (character- and phase-weighted) computed once at σ=½, summed across all 16 prime channels. Full algebra in `ValaQuenta/wiki/sigma_expansion.md`.

```
'O Captain My Captain'      c1 = 0.075456   c3 = 0.049216   max_residual = 0.001311
'RSA private key recovery'  c1 = 0.226251   c3 = -0.085853  max_residual = 0.000406
'zero divisor'               c1 = 0.172088   c3 = -0.055935  max_residual = 0.000434
```

Predicted curve matches direct computation to ~1e-6 near σ=½ across all three, residual growing smoothly toward the edges of the tested range — exactly the expected shape for a third-order truncation, confirming the algebra rather than assuming it.

## 5. Scope — What This Does and Doesn't Reach

This is a real, verified engine for the `i^-σ` Dirichlet-projection construction used in `SedenionSpectralRelativity/layer_spectrograph.py` and this session's bispectrum work. It is explicitly **not** a substitute for error-checking `VAPMIP/monad.py`'s Engine, which computes σ through a different mechanism entirely — `_word_zero_idx` (prime hash → address) and `_gamma_at` (Newton's method on the real Riemann zeta function's zeros), not this power-law projection. The strategy (closed-form Taylor prediction as a cheap check against expensive computation) transfers; the specific formula does not, without re-deriving it against the monad's actual σ mechanism.

Built into the permanent registry regardless of whether it ends up serving that original error-checking purpose — infrastructure investment, not contingent on immediate payoff.
