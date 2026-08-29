# 06 — NOETHER INFORMATION ENGINE  J_info

**Module:** `noether_information`  **Version:** 0.111  **Confidence floor:** CONJECTURE

## Information Current

The Noether current for information-translation symmetry of L_NN.

```
J_info^μ = ∂L/∂(∂_μΦ) · δΦ
```

Components:
- J_info^0 = I_info / layer  (temporal — entropic arrow)
- J_info^1 = Φ_flux          (spatial — information flux through boundary)

## Information Content

```
I_information = -Σ_i p_i · log₂(p_i)   (Shannon entropy, bits)
p_i = |Ψ_i|² / Σ_j|Ψ_j|²
```

## Information Flux

```
Φ_flux = dim(algebra) · |Ψ̄·Ψ| / n_neurons
```

The flux scales with the algebra dimension — higher strata carry more information per neuron.

## Entropic Arrow

```
∂_l I_info ≥ 0
```

Information grows monotonically with layer depth until the sedenion boundary. Violations of this inequality indicate pathological training dynamics.

## Information Capacity

```
C_max = n_neurons × log₂(dim_algebra)  bits
```

| Stratum | bits/neuron | Note |
|---------|-------------|------|
| ℝ | 0 | no info storage |
| ℂ | 1 | 1 bit |
| ℍ | 2 | 2 bits |
| 𝕆 | 3 | 3 bits |
| 𝕊 | — | excluded: zero-divisors break norm |

## Equations

| Name | Status | Description |
|------|--------|-------------|
| `information_current` | CONJECTURE ◇ | J_info^μ, I_info, Φ_flux, t_e |
| `entropic_arrow` | CONJECTURE ◇ | ∂_l I ≥ 0 verification |
| `delta_J_info` | CONJECTURE ◇ | cycle-averaged violation |
| `information_capacity` | THEORETICAL ◈ | C_max bits per stratum |

**Status note:** The identification of information current as a Noether current is a conjecture. The Shannon entropy calculation is established; the symmetry interpretation is not yet formally derived.
