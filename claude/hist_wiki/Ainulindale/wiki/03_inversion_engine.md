# 03 — Inversion Engine (I|O)

| | |
|---|---|
| Module | `inversion` — `ValaQuenta/modules/inversion/` (`maths.py`, `tools.py`, `manifest.json`) |
| Class | `InversionModule` (registered in `ValaQuenta/__main__.py::_register_all`) |
| Version | 0.111 (module); `maths.py` header says 0.120 |
| Confidence floor | ESTABLISHED |
| API page | `ValaQuenta/wiki/inversion.md` |
| Notebook | `ValaQuenta/notebooks/core/03_inversion.ipynb` |
| Last verified | 2026-11-13, against the live registry (7 equations) |

## 1. What it computes

The map J_N sends a point (r, θ) of the plane to (1/r, θ + π/2). It is the
"2-stroke engine" of the framework: the compression stroke is r → 1/r, the
expansion stroke is 1/r → r, and r = 1 is the fixed circle (the horizon).

Two properties need stating exactly, because older wiki text blurred them:

- **J_N is an involution in r, not in θ.** J_N∘J_N sends (r, θ) to (r, θ + π).
  r returns to its start after two applications; the point itself returns
  after four. This is why the code's `is_involution` returns the triple
  `(r_closes, r_after_2, theta_after_2)` and does not return a single Boolean
  for "J_N∘J_N = identity".
- **The rotation angle π/2 is derived, not assumed.** `derive_horizon_rotation`
  divides a full turn (2π, from the Basel sum ζ(2) = Σ 1/n², π = √(6ζ(2)))
  by 4, the number of normed division algebras (Hurwitz, 1898). It reuses
  Basel's π; it is not a third independent derivation of π's value.
  Status: ESTABLISHED (residual 2.4·10⁻⁶ at the default 200,000 terms).

Fixed point of J_N: r = 1 at every angle. A separate object, the recursion
attractor r_{n+1} = 1 + 1/r_n, converges to φ = (1+√5)/2 from any r₀ > 0.
The two are different: J_N fixes r = 1; the recursion attracts to φ.
How the flow from one to the other is derived is OPEN.

Four physical readings of the horizon, by depth (`four_horizons`,
THEORETICAL): d = 0 Ptolemy inversion (coordinate), d = 1 Dirac sea,
d = 2 Hawking radiation, d = 3 Schwarzschild horizon. In the code's own
status line, three of the four are ESTABLISHED and the second (Dirac sea) is
THEORETICAL; the equation as a whole is carried at the weaker tier.

## 2. Mechanism

The recursion attractor is seven lines. It is the whole of the φ claim at the
level of mechanism, so it is shown as code.

**Listing 1 — the recursion attractor** (`modules/inversion/maths.py`,
`RecursionAttractor.iterate`; extracted: docstring removed, `self` dropped,
seven lines, runs cold)

```python
def iterate(r0, steps=50):
    trajectory = [r0]
    r = r0
    for _ in range(steps):
        r = 1.0 + 1.0 / r
        trajectory.append(r)
    return trajectory
```

Listing 1 converges to φ from any positive start: `iterate(1.0, 10)[-1]` is
1.61797…, against φ = 1.61803…. The step at the φ crossing is
H_NN/4 = (π/2)·ħ_NN; this equality holds numerically to 10⁻¹² (ESTABLISHED
numerically), and its formal derivation is OPEN.

The map itself (`InversionMap.apply`) is one line, delegating to
`engine/units.py::inversion_transform`; it is described by the formula above
and not reproduced.

## 3. Equations

| Name | Tier | Parameters | What it returns |
|---|---|---|---|
| `inversion_map` | ESTABLISHED | `r`, `theta_rad` | (1/r, θ + π/2) |
| `derive_horizon_rotation` | ESTABLISHED | — | π/2 derived from Basel and Hurwitz, with residual |
| `involution_check` | ESTABLISHED | `r`, `theta_rad` | (r closes, r after 2, θ after 2) |
| `gradient_flow` | ESTABLISHED | `r0`, `max_steps` | r → 1 + 1/r flow to φ |
| `phi_crossing_step` | ESTABLISHED | — | H_NN/4 against (π/2)·ħ_NN, with match flag |
| `d_star_gap` | OPEN | — | d*_spec·ln 10 against Ω_ζΣ, and their gap |
| `four_horizons` | THEORETICAL | — | the four physical readings |

`d_star_gap` is computed with `C.D_STAR`, which in the code is the **measured**
d*_spec = 0.24600, not the Boundary value 0.24631. See §5.

## 4. Session

Literal registry calls and their printed results (2026-11-13):

```
>>> registry.run('inversion.inversion_map', {'r': 2.0, 'theta_rad': 0.0})
(0.5, 1.5707963267948966)
>>> registry.run('inversion.involution_check', {'r': 2.0, 'theta_rad': 0.0})
(True, 2.0, 3.141592653589793)
>>> registry.run('inversion.phi_crossing_step', {})
{'H_NN_over_4': 0.025, 'pi_over_2_times_hbar': 0.024999999999999998, 'match': True, 'status': 'ESTABLISHED numerically — formal derivation OPEN'}
>>> registry.run('inversion.d_star_gap', {})
{'d_star': 0.246, 'd_star_x_ln10': 0.5664359328765353, 'OMEGA_ZS': 0.5671432904097838, 'gap': 0.000707357533248576, 'status': 'OPEN — highest priority derivation'}
```

Shell commands injected into the console (`InversionModule.shell_commands`):
`io(r, t)`, `flow(r0)`, `phi_step()`, `gap()`, `observer()`, `horizons()`.

## 5. Open items

| Item | State |
|---|---|
| Formal derivation of the φ-crossing step H_NN/4 = (π/2)·ħ_NN | OPEN (numerical match only) |
| Derivation of the flow from r = 1 to φ | OPEN |
| The gap 0.000707357533… between d*_spec·ln 10 and Ω_ζΣ | OPEN. It is ≈ 1/(1000√2). The measured d*_spec = 0.24600 is not one of the four named d* faces; see [wiki 17](17_alpha_omega_d_star.md) and [wiki 133](133_canonical_maths.md) §2.2 |
| Fixed-point status of r = 1 with "A_π and Ω_ζΣ as domain boundary" (code docstring) | the A_π value is OPEN; see wiki 17 |

## 6. Related pages

[02 Registry](02_registry.md) · [07 Berry–Keating](07_berry_keating_engine.md) (same gap) ·
[17 α · Ω · d*](17_alpha_omega_d_star.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md) ·
[133 Canonical maths](133_canonical_maths.md)
