# 03 — INVERSION ENGINE  (I|O)

**Module:** `inversion`  **Version:** 0.111  **Confidence floor:** ESTABLISHED

## What it computes

The (I|O) inversion map J_N — the 2-stroke engine at the core of SMNNIP.

```
J_N: (r, θ) → (1/r, θ + π/2)
```

### Properties
- **Involution:** J_N ∘ J_N: r → r, θ → θ + π  (two applications = full rotation)
- **Fixed point:** r = 1 (the inversion horizon)
- **Recursion attractor:** r = φ = (1+√5)/2 via r_{n+1} = 1 + 1/r_n
- **Step at φ-crossing:** Δr|_φ = H/4 = (π/2)·ħ_NN
- **Sedenion:** top dead center — the expansion stroke fails here

### Physical interpretations (four horizons)
| Depth | Interpretation |
|-------|---------------|
| d=0 | Ptolemy inversion (coordinate) |
| d=1 | Dirac sea (particle/antiparticle) |
| d=2 | Hawking radiation (thermal inversion) |
| d=3 | Schwarzschild horizon (gravitational) |

## Equations

| Name | Status | Description |
|------|--------|-------------|
| `inversion_map` | ESTABLISHED ✓ | J_N: (r,θ) → (1/r, θ+π/2) |
| `involution_check` | ESTABLISHED ✓ | J_N∘J_N returns (r, θ+π) |
| `gradient_flow` | ESTABLISHED ✓ | r → 1+1/r convergence to φ (v0.112 fix) |
| `phi_crossing_step` | ESTABLISHED ✓ | Δr = H/4 = (π/2)·ħ_NN |
| `d_star_gap` | OPEN ? | d*×ln(10) vs Ω — gap = 0.000707 |
| `four_horizons` | THEORETICAL ◈ | Four physical interpretations of J_N |

## Open problems from this module

**FLAG-4 (RESOLVED v0.112):** `gradient_flow` convergence fixed by replacing tiny hbar step with phi-recursion r → 1+1/r. Formal derivation from first principles still open.

**d* gap:** See [07_berry_keating_engine.md](07_berry_keating_engine.md).

## Key constants
```
D_STAR_SPEC = 0.24600
OMEGA_ZS    = 0.56714329040978384
GAP         = 0.000707
PHI         = 1.6180339887...
HBAR_NN     = from constants.py
```

## Shell commands
```python
io(r=2.0, t=0.0)   # apply J_N once
flow(r0=1.0)        # gradient flow trajectory
phi_step()          # H/4 value
gap()               # d* gap report
```
