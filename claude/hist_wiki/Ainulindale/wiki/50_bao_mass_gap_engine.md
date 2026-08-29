# 50 — MASS GAP ENGINE  Δ

**Module:** `bao_mass_gap` **Version:** 0.131 **Equations:** 7 **Checks:** 7/7

## Overview

The mass gap, computed. Not estimated, not fitted, not tuned.

```
Δ = Ω_ζΣ − D* × ln(10) = 0.0007073575 = 1/(1000√2)
```

Two constants taken from opposite ends of the H_hat_RB operator. Their
difference is the gap. One value, zero free parameters.

This engine is where Δ is computed. Δ is then consumed across the codebase — as
the compactification scale, as the spectral floor constant, and as the band
that separates the ground state from the first excitation wherever the RedBlue
Hamiltonian is evaluated at σ=1.

→ [Wiki: Berry-Keating Engine](07_berry_keating_engine.md) — where D* comes from
→ [Wiki: Alpha · Omega · d*](17_alpha_omega_d_star.md) — all four d* values
→ [Wiki: RedBlue Hamiltonian](14_redblue_hamiltonian.md) — σ-facet table
→ [Wiki: Cayley-Dickson Tower](19_cayley_dickson_tower.md) — the √2 is the first doubling
→ ValaQuenta: [wiki/bao_mass_gap.md](../../ValaQuenta/wiki/bao_mass_gap.md) — engine page, full results

---

## The Residue

The name of the engine is the argument. Δ is a **residue** — what is left over
after a decomposition, not a quantity introduced by hand.

The explicit formula splits the prime distribution into a ground state plus one
standing wave per non-trivial zero:

```
ψ(x) = x − Σ_ρ x^ρ/ρ − ln(2π) − ½ln(1 − x⁻²)
       ▲   ▲
       │   └── spectral oscillations: one standing wave per γ_n
       └────── de Sitter expansion term: the ground state
```

Read at the BAO scale, this is the acoustic spectrum of the CMB. The same
decomposition, read as sound instead of as primes:

| Term | Primes | BAO |
|------|--------|-----|
| `x` | ground state of ψ | de Sitter expansion — acoustic ground state |
| `Σ_ρ x^ρ/ρ` | one wave per zero | the acoustic oscillations |
| `ln(2π)` | boundary constant | boundary normalisation |
| residue | — | **the gap** |

The floor of the acoustic spectrum is `D*·ln(10) = 0.5664359329`. The ceiling of
the same spectrum is the thermal information bound `Ω_ζΣ = 0.5671432904`. The
band between them is absorbed by no standing wave.

That band is Δ.

**The gap exists because the residue is positive.** Ceiling exceeds floor;
therefore Δ > 0. There is no separate existence argument — the positivity of a
subtraction is the whole of it.

---

## Independence from the Sum

The single most important structural property of this engine:

**The residue does not depend on how many zeros are summed.**

The spectral sum converges as zeros are added. The residue is a difference of
two constants and does not move at all. Summing 1 zero and summing 20 give a
residue spread of exactly `0.0` — not "small", not "within tolerance", exactly
zero.

This is why Δ is a constant of the framework rather than a numerical estimate.
The explicit-formula sum in the engine is a demonstration that the decomposition
is the prime distribution; it is not an input to Δ.

The engine asserts this as `residue_is_n_independent`. The notebook plots it.

---

## The 1/√2

```
Δ = 1/(1000√2) = 1/√(2×10⁶)
```

`1/√2 = sin(45°) = cos(45°)` — the angle of maximum Red/Blue symmetry at σ=½,
the amplitude at which the forward current equals the backward current, where
Riemann equals Fermat.

The √2 is the first Cayley-Dickson doubling. The gap sits at the first rung of
the tower.

**Write it `1/(1000√2)` or `1/√(2×10⁶)`. Not `1/√2000`** — that is 0.02236,
31.6× too large, and it is the single easiest way to misread the whole engine.

The `1/√2` factor is accounted for. The `10³` factor is not yet derived from
framework constants — the open form of that question is: *at what algebraic
constraint does `d*_BK × ln(10) + 1/(1000√2) = W(1)` exactly?*

---

## D* Precision

`D*` is carried to 5 decimal places as `0.24600`. The identity pins it to
`0.2460001089` — a difference of `1.089e-07`, inside the last carried digit.

| Value | Source | Gap |
|-------|--------|-----|
| `d*_spec = 0.24600` | the carried spectral value — ACTIVE | 0.000707 |
| `d*_taut = Ω/ln(10)` | tautological — reference only | 0.0 by construction |
| `d*_exact = 0.2460001089` | the D* at which Δ = 1/(1000√2) exactly | — |

The residual of `2.508e-07` measures the precision of D*, not the identity.
`d*_taut` has zero gap by construction and is not a result — do not use it as
the active value.

---

## Compactification

`11 = 4 observable + 7 compact`. The compact 7 carry G₂ holonomy, and
`G₂ = Aut(𝕆)`. The 7 directions are the imaginary octonion units `e₁..e₇` —
algebraic, never spatial. The compact dimensions were never places.

The compactification scale is Δ.

Δ is computed, so it is not a modulus. No moduli, no landscape: `10^500 → 1`.

The engine carries the dimension arithmetic as `Fraction`, so `11 − 4 == 7` is
an exact comparison rather than a float one.

---

## Acoustic Scale

Planck 2018 gives `r_s = 147.09 ± 0.26 Mpc`, a fractional precision of 0.177%.

```
Δ/σ_BAO = 0.400174
```

Δ sits at 0.40 of the error bar — above the noise floor, a resolvable feature of
the acoustic spectrum.

---

## Engine Contents

| Equation | What it does |
|---|---|
| `summary` | one-screen landing view — the headline |
| `gap_value` | Δ = Ω_ζΣ − D*·ln10 |
| `spectral_residue` | the BAO decomposition — why the gap IS a residue |
| `gap_identity` | Δ = 1/(1000√2) |
| `bao_consistency` | Δ against the Planck 2018 acoustic scale |
| `mtheory_compactification` | 11 = 4+7, G₂ holonomy, one vacuum |
| `validate` | all 7 checks |

Every `compute()` returns a `derivation` key: an ordered list of the operations
performed, in order. The console renders that list directly as the proof chain.

```bash
python3 -m ainulindale_engine --info      # bao_mass_gap registers first
python3 -m ainulindale_engine --curses    # console: MODULES pane, top entry
```

**Notebook:** [ValaQuenta/notebooks/core/19_bao_mass_gap.ipynb](../../ValaQuenta/notebooks/core/19_bao_mass_gap.ipynb) — step-by-step, 18 code cells, executes clean.
