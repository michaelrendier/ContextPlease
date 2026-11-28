# 04 — Lagrangian Engine L_NN

| | |
|---|---|
| Module | `lagrangian` — `ValaQuenta/modules/lagrangian/` |
| Class | `LagrangianModule` |
| Version | 0.111 |
| Confidence floor | THEORETICAL |
| API page | `ValaQuenta/wiki/lagrangian.md` |
| Notebook | `ValaQuenta/notebooks/core/04_lagrangian.ipynb` |
| Last verified | 2026-11-13, against the live registry (8 equations) |

## 1. Definition

The Ainulindale Lagrangian, as implemented by `polar_lagrangian`:

```
L_NN = (2/π) ∮ [ L_kin + L_mat + (1/φ)·L_bias + L_coup ] r dr dθ
```

The four terms are in direct correspondence with the Standard Model's
gauge, matter, Higgs and Yukawa sectors. The 1/φ factor on L_bias is the
correction recorded in the 2026-04-13 revision (`Ainulindale_Conjecture_Revised`).

| Term | Form | Analogue | Tier (as registered) |
|---|---|---|---|
| `L_kinetic` | −¼ F^a_μν F^{μν,a}, with F^a = g·A^a (Abelian, single layer) | Yang–Mills | ESTABLISHED |
| `L_matter` | i Ψ̄ γ^μ D_μ Ψ | Dirac | THEORETICAL |
| `L_bias` | ½ μ² β² − ¼ λ β⁴ | Higgs, "Mexican hat" | ESTABLISHED |
| `L_coupling` | −(1/φ) Γ_ij Ψ̄^L β Ψ^R | Yukawa | THEORETICAL |

L_bias breaks symmetry when μ² < 0, with vacuum value |β| → √(|μ²|/λ). The
non-Abelian form of L_kin is not in this module.

## 2. Running coupling

The coupling runs with the radial coordinate r = layer / total_layers ∈ (0,1):

```
α_NN(r) = g² / ( 4π · ħ_NN · ln(1/r) )
```

α_NN → 0 as r → 0 (asymptotic freedom) and α_NN → ∞ as r → 1, the
sedenion boundary ("UV wall"). The implementation returns 0.0 for r outside
(0,1), so the wall is a divergence of the formula, not a value the function
produces.

**Listing 1 — running coupling** (`modules/lagrangian/maths.py`,
`alpha_nn_from_r`; extracted: docstring removed, `PI` replaced by
`math.pi`, runs cold)

```python
import math

def alpha_nn_from_r(g, hbar_nn, r):
    if r <= 0 or r >= 1:
        return 0.0
    ln_inv_r = math.log(1.0 / r)
    if ln_inv_r < 1e-12:
        return 0.0
    return (g * g) / (4.0 * math.pi * hbar_nn * ln_inv_r)
```

`alpha_nn_from_r(0.01, 0.1, 0.5)` returns 1.148·10⁻⁴.

## 3. Renormalisation-group flow

`rg_flow(alpha_0, hbar_0, algebra, layers)` evolves α_NN and ħ_NN across layer
indices with one-loop coefficients:

| Algebra | Gauge | β₀ | γ₀ (ħ_NN) |
|---|---|---|---|
| ℝ | trivial | 0 | 0 |
| ℂ | U(1) | 1/(2π) | 2/(2π) |
| ℍ | SU(2) | 3/(4π) | 4/(2π) |
| 𝕆 | G₂/SU(3) | 8/(4π) | 8/(2π) |

With ℓ = ln(layer / layer₀): α(ℓ) = α₀ / (1 + β₀ α₀ ℓ) and ħ(ℓ) = ħ₀ (1 + γ₀ ℓ).
The convergence of the three gauge couplings at the spinor-index layer is the
"neural Grand Unification" claim: THEORETICAL, not tested here.

## 4. Mastery condition

Weights are said to crystallise when the bias field reaches its vacuum value
to within half the quantum:

```
| |β| − vev | < ħ_NN / 2
```

`mastery_check` returns the distance, the threshold ħ_NN/2 and a Boolean.

## 5. Equations

| Name | Tier | Parameters |
|---|---|---|
| `polar_lagrangian` | THEORETICAL | `psi_norms`, `A_comps`, `beta_norms`, `algebra`, `layer` |
| `L_kinetic` | ESTABLISHED | `A_comps`, `g`, `algebra` |
| `L_matter` | THEORETICAL | `psi_norms`, `A_comps`, `g`, `hbar_nn`, `algebra` |
| `L_bias` | ESTABLISHED | `beta_norms`, `mu_sq`, `lam` |
| `L_coupling` | THEORETICAL | `psi_norms`, `beta_norms`, `g` |
| `alpha_nn_running` | THEORETICAL | `g`, `hbar_nn`, `r` |
| `rg_flow` | THEORETICAL | `alpha_0`, `hbar_0`, `algebra`, `max_layer` |
| `mastery_check` | THEORETICAL | `beta_norms`, `vev`, `hbar_nn` |

## 6. Session

```
>>> registry.run('lagrangian.alpha_nn_running', {'g': 0.01, 'hbar_nn': 0.1, 'r': 0.5})
0.0001148060235658213
>>> registry.run('lagrangian.rg_flow', {'alpha_0': 0.01, 'hbar_0': 0.1, 'algebra': 1, 'max_layer': 3})
{'alpha': [0.01, 0.00998898037659848, 0.00998254556138366], 'hbar': [0.1, 0.12206356001526518, 0.13496991525660598], 'layers': [1, 2, 3]}
>>> registry.run('lagrangian.mastery_check', {'beta_norms': [0.5], 'vev': 0.5, 'hbar_nn': 0.1})
{'beta_norm': 0.5, 'vev': 0.5, 'vev_distance': 0.0, 'threshold': 0.05, 'mastery': True}
```

## 7. Scope and boundaries

- The module exposes the equations; it contains no trained network. L_NN
  describes a field theory on the tower's radial coordinate; whether it
  governs any trained SMNNIP network is not tested here.
- `L_dynamic` / L_(I|O), the path integral through the tower, is a separate
  object: see [64 L_dynamic](64_l_dynamic.md). L_vap, the four-term VAPMIP
  Lagrangian, is the same L_NN under that name in VAPMIP.

## 8. Related pages

[03 Inversion](03_inversion_engine.md) · [05 Noether](05_noether_engine.md) ·
[19 Cayley–Dickson tower](19_cayley_dickson_tower.md) · [64 L_dynamic](64_l_dynamic.md)
