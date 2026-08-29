# 04 — LAGRANGIAN ENGINE  L_NN

**Module:** `lagrangian`  **Version:** 0.111  **Confidence floor:** THEORETICAL

## The Lagrangian

```
L_NN = (2/π) ∮ [L_kin + L_mat + (1/φ)·L_bias + L_coup] r dr dθ
```

This is the corrected Ainulindale Lagrangian (Ainulindale_Conjecture_Revised.docx, April 13 2026). The 1/φ prefactor on L_bias is the correction from the original form.

## Four Terms

### L_kinetic — Yang-Mills
```
L_kin = -1/4 · F_μν^a · F^{μν,a}
```
Field strength F^a = g·A^a (single-layer Abelian approximation). Full non-Abelian form is in the derivation engine (smnnip_derivation_pure_patched.py).

### L_matter — Dirac
```
L_mat = i · Ψ̄ · γ^μ · D_μ · Ψ
```
Activation propagation. The Neural Dirac equation emerges from δL_mat/δΨ̄ = 0.

### L_bias — Higgs / Mexican hat
```
L_bias = (1/2)·μ²·β² - (1/4)·λ·β⁴
```
μ² < 0 → spontaneous symmetry breaking. Bias field β plays the role of the Higgs field. VEV: |β| → √(|μ²|/λ) at mastery.

### L_coupling — Yukawa
```
L_coup = -(1/φ) · Γ_ij · Ψ̄^L · β · Ψ^R
```
The 1/φ scaling is the Ainulindale correction. Generates effective mass from the bias VEV.

## Running Coupling

```
α_NN(r) = g² / (4π · ħ_NN · ln(1/r))
```

where r = layer/total_layers ∈ (0,1).

- At r → 0 (shallow layers): α_NN → 0 (asymptotic freedom)
- At r → 1 (sedenion boundary): ln(1/r) → 0, α_NN → ∞ (UV wall)

This maps exactly to QFT asymptotic freedom with the radial coordinate r replacing the energy scale.

## RG Flow

Beta functions (one-loop):

| Stratum | β₀ | Gauge |
|---------|-----|-------|
| ℝ | 0 | trivial |
| ℂ | 1/(2π) | U(1) |
| ℍ | 3/(4π) | SU(2) |
| 𝕆 | 8/(4π) | G₂/SU(3) |

Convergence of all three couplings at the spinor-index layer = neural Grand Unification.

## Mastery Condition

```
| |β| - vev | < ħ_NN / 2
```

Weights crystallize when VEV distance falls below the uncertainty bound ħ_NN/2.

## Equations

| Name | Status | Description |
|------|--------|-------------|
| `polar_lagrangian` | THEORETICAL ◈ | Full L_NN polar integral |
| `L_kinetic` | ESTABLISHED ✓ | -1/4 F² |
| `L_matter` | THEORETICAL ◈ | i·Ψ̄·D·Ψ |
| `L_bias` | ESTABLISHED ✓ | Mexican hat |
| `L_coupling` | THEORETICAL ◈ | (1/φ)·Yukawa |
| `alpha_nn_running` | THEORETICAL ◈ | α_NN(r) running coupling |
| `rg_flow` | THEORETICAL ◈ | RG flow across layers |
| `mastery_check` | THEORETICAL ◈ | crystallization condition |

## Shell commands
```python
lagrangian(layer=1, g=0.01)   # full L_NN at layer
alpha_r(r=0.5)                 # running coupling at r
rg(alg=1, n=10)               # RG flow, n layers
```
