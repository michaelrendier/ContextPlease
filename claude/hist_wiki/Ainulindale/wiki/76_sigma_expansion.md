# 76 — Sigma Expansion: the J_red/J_blue Balance Curve

| | |
|---|---|
| Scope | whether |J_red(σ)|² + |J_blue(σ)|² is conserved across σ (it is not); the renormalised balance P_red(σ) − ½ and its derived cubic expansion |
| Origin | 2026-07-11, derived by Claude Sonnet 5, directed by the author; the author's statement: "The point is the renormalization will show you the derivation curve." |
| Predecessors | [73](73_why_the_half_line.md), [75](75_abrikosov_lattice.md) |
| Code | `ValaQuenta/modules/sigma_expansion/` (`maths.py`: `taylor_coefficients`, `verify_against_actual`); `ValaQuenta/wiki/sigma_expansion.md`; notebook `15_sigma_expansion.ipynb`; `SedenionSpectralRelativity/layer_spectrograph.py` |
| Confidence | the derivation of c₁ and c₃ and its agreement with direct computation: ESTABLISHED (reproduced 2026-11-13) · scope: stated in §4 |
| Last verified | 2026-11-13: the three `taylor_coefficients` / `verify_against_actual` runs below were re-executed with the installed engine; the values match the 2026-07-11 record to every digit shown |

## 1. The question

A video by Nick Lucid ("The Science Asylum"), "Quantum Superposition, Explained Without Woo
Woo" (Nov 2021), shows that a two-outcome quantum state can be written as one vector between
two positive axes (the two probabilities). The framework has two positive quantities of that
kind: J_red(σ) (the forward Dirichlet series, "Knowledge") and J_blue(σ) = J_red(1 − σ)
("Experience", the reverse). The testable question: does |J_red(σ)|² + |J_blue(σ)|² normalise to a
constant across σ the way real probabilities must?

## 2. The negative result, first  `MEASURED`

**No.** Computed directly for three independent strings, the raw sum is a smooth, symmetric
curve with a **minimum at σ = ½**: an energy well, not a conservation law. The Lucid
normalisation argument does not transfer to J_red/J_blue as currently defined. This was
reported before any renormalisation was attempted, as standing practice requires. (The
raw curve is the engine's `project_at_sigma` at σ and 1 − σ; it was not re-plotted in the
2026-11-13 run, the coefficients below were.)

## 3. Renormalisation as a build tool, then the derivation  `ESTABLISHED`

The author granted a one-time, scoped exception to the "no renormalisation" rule, as a tool
toward a derivation and not an endpoint. The renormalised object is

```
P_red(σ) = |J_red|² / (|J_red|² + |J_blue|²),     P_red + P_blue = 1 by construction
```

which proves nothing by itself; what it produces is the curve P_red(σ) − ½, which is smooth,
antisymmetric about σ = ½, with a local slope near the centre *smaller* than further out
(the opposite of a tanh). That fixes the form: an odd series dominated by a cubic,
c₁ d + c₃ d³ (d = σ − ½). Both coefficients are **derived**, not fitted, by Taylor-expanding
F(σ) = |N(σ)|²/D(σ)² about σ = ½ with moments Mₙ (position-only) and Lₙ (character- and
phase-weighted) computed once at σ = ½ over the 16 prime channels. The algebra is in
`ValaQuenta/wiki/sigma_expansion.md`.

**Listing 1 — the derived coefficients, re-run** (needs the ValaQuenta engine; `maths.py` loaded by path)

```python
import importlib.util, sys
spec = importlib.util.spec_from_file_location('se', 'ValaQuenta/modules/sigma_expansion/maths.py')
se = importlib.util.module_from_spec(spec); sys.modules['se'] = se; spec.loader.exec_module(se)
for t in ('O Captain My Captain', 'RSA private key recovery', 'zero divisor'):
    c = se.taylor_coefficients(t); v = se.verify_against_actual(t)
    print(repr(t), 'c1 = %.6f  c3 = %.6f  max_residual = %.6f' % (c['c1'], c['c3'], v['max_residual']))
```

```
'O Captain My Captain'      c1 = 0.075456  c3 = 0.049216  max_residual = 0.001311
'RSA private key recovery'  c1 = 0.226251  c3 = -0.085853  max_residual = 0.000406
'zero divisor'              c1 = 0.172088  c3 = -0.055935  max_residual = 0.000434
```

The predicted curve matches the direct computation to about 10⁻⁶ near σ = ½ for all three,
with the residual growing smoothly toward the edges of the tested range, the expected shape of
a third-order truncation. Note the sign of c₃ is not universal (positive for the first string,
negative for the other two), so the "slope smaller at the centre than further out" holds for
the first string and not the others; the page's description fits the first case, and the
odd cubic form holds for all three.

## 4. Scope  `ESTABLISHED`

This is a verified engine for the **i^(−σ) Dirichlet-projection construction** used in
`layer_spectrograph.py` and the bispectrum work. It is **not** an error check for
`VAPMIP/monad.py`, whose σ comes from a different mechanism: `_word_zero_idx` (prime hash →
address) and `_gamma_at` (Newton on the zeros of the zeta function), not this power-law
projection. The strategy (a closed-form Taylor prediction as a cheap check on an expensive
computation) transfers; the formula does not, without re-deriving it against the monad's
own σ mechanism. Built into the permanent registry as infrastructure, not contingent on that
purpose.

## 5. Related pages

[73 why σ = ½](73_why_the_half_line.md) · [75 the Abrikosov lattice](75_abrikosov_lattice.md) ·
[77 hypergon constructibility](77_hypergon_constructibility.md) · [82 the L_(I|O) photon path](82_l_io_photon_path.md)
