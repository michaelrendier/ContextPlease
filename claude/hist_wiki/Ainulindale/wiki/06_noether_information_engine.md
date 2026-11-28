# 06 — Noether Information Engine J_info

| | |
|---|---|
| Module | `noether_information` — `ValaQuenta/modules/noether_information/` |
| Class | `NoetherInformationModule` |
| Version | 0.111 |
| Confidence floor | CONJECTURE |
| API page | `ValaQuenta/wiki/noether_information.md` |
| Notebook | `ValaQuenta/notebooks/core/06_noether_information.ipynb` |
| Last verified | 2026-11-13, against the live registry (4 equations) |

## 1. Claim and status

The claim: information translation is a continuous symmetry of L_NN
([04](04_lagrangian_engine.md)), and so carries a Noether current

```
J_info^μ = ∂L / ∂(∂_μ Φ) · δΦ
```

with components J_info⁰ = I_info / layer (the temporal, entropic component)
and J_info¹ = Φ_flux (information flux through an algebra boundary).

**Status: CONJECTURE.** The arithmetic below is exact and runs; the
identification of this quantity as a Noether current of a symmetry has not
been derived. Three of the four equations are registered CONJECTURE for that
reason; the capacity table is THEORETICAL.

## 2. The quantities

| Quantity | Definition (as implemented) | Status of the definition |
|---|---|---|
| I_info | Shannon entropy in bits, −Σ pᵢ log₂ pᵢ, with pᵢ = |Ψᵢ|² / Σⱼ|Ψⱼ|²; terms with pᵢ < 10⁻¹² are dropped | ESTABLISHED (Shannon) |
| Φ_flux | dim(algebra) · |Ψ̄Ψ| / n_neurons | defined by the module; the dimension scaling is a design choice |
| Entropic arrow | ∂_ℓ I_info ≥ 0 along the layers, up to the sedenion boundary | CONJECTURE |
| C_max | n_neurons · log₂(dim algebra) bits | THEORETICAL |

**Listing 1 — information capacity per stratum** (`modules/noether_information/maths.py`,
`information_capacity`; the arithmetic extracted, the dictionary wrapper
omitted; runs cold)

```python
import math

def bits_per_neuron(dim):
    return math.log2(max(dim, 1))

for name, dim in (('R', 1), ('C', 2), ('H', 4), ('O', 8)):
    print(name, dim, bits_per_neuron(dim))
```

```
R 1 0.0
C 2 1.0
H 4 2.0
O 8 3.0
```

The sedenion shell (dimensions 8–15) adds no capacity: its zero-divisors
break the norm, so the module excludes it and says so in its result.

## 3. Equations

| Name | Tier | Parameters |
|---|---|---|
| `information_current` | CONJECTURE | `psi_norms`, `algebra`, `layer`, `total_layers` |
| `entropic_arrow` | CONJECTURE | `n_steps`, `algebra` |
| `delta_J_info` | CONJECTURE | `psi_norms`, `algebra`, `layer` |
| `information_capacity` | THEORETICAL | `algebra`, `n_neurons` |

## 4. Session

```
>>> registry.run('noether_information.information_capacity', {'algebra': 3, 'n_neurons': 100})
{'algebra': '𝕆', 'algebra_dim': 8, 'n_neurons': 100, 'bits_per_neuron': 3.0, 'C_max_bits': 300.0, 'sedenion_note': 'Sedenion shell excluded — zero-divisors break norm'}
```

## 5. Boundaries

- A monotone entropy along layers is a property one can check on a trained
  network; here `entropic_arrow` checks it on synthetic histories. A
  violation is reported as a number, not interpreted.
- Nothing in this module is used by another engine as an input.

## 6. Related pages

[05 Noether](05_noether_engine.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md) ·
[43 Emmy Noether and the sedenion](43_emmy_noether_sedenion.md)
