# 07 — Berry–Keating Engine H_NN

| | |
|---|---|
| Module | `berry_keating` — `ValaQuenta/modules/berry_keating/` |
| Class | `BerryKeatingModule` |
| Version | 0.111 |
| Confidence floor | OPEN |
| API page | `ValaQuenta/wiki/berry_keating.md` |
| Notebook | `ValaQuenta/notebooks/core/07_berry_keating.ipynb` |
| Last verified | 2026-11-13, against the live registry (6 equations, all OPEN) |

## 1. Scope

A workbench for the Red channel of the RedBlue Hamiltonian ([14](14_redblue_hamiltonian.md)):
the Berry–Keating xp operator, the spectral coordinate d*, the T coordinate
map, and the d* gap. Every equation here is registered OPEN. Nothing in this
module proves anything about the Riemann zeros; it is where the open
quantities are held and evaluated.

## 2. The gap

```
d*_spec · ln 10  =  0.5664359…
Ω_ζΣ             =  0.5671432…
gap              =  0.000707357533…   (≈ 1/(1000√2))
```

`d_star_gap_report` is computed with **d*_spec = 0.24600**, the measured
spectral value. It also reports d*_taut = Ω_ζΣ / ln 10 = 0.246307201473…,
whose gap is 0 by construction, so it is a reference value and not a result.

Neither is the Boundary value d* = 0.24631 of the four named faces; the four
faces, their status, and the closing of d*_RG are in
[17](17_alpha_omega_d_star.md) and [133 §2.2](133_canonical_maths.md).
In the code, `D_STAR` is d*_spec.

Candidate closed forms. `gap_candidates` evaluates a list of expressions and
sorts them by the gap |Ω_ζΣ − x·ln 10| (values from the 2026-11-13 run):

| Expression | Value x | Gap | Outcome |
|---|---|---|---|
| Ω_ζΣ / ln 10 | 0.24631 | 0 | tautology, by construction |
| 1 / ln(10²) | 0.21715 | 0.0671 | no |
| 1 / (π + φ) | 0.21010 | 0.0834 | no |
| 1 / (2e) | 0.18394 | 0.1436 | no |

`d_star_gap_report` also records two further candidates in its notes:
1/(φ · ln 10) = 0.2418 ("close but gap remains") and 1/W(e³), rejected
(off by a factor of about 643). No closed form for d*_spec is known.
An earlier version of this page listed 1/(π + φ) as 0.2386 with gap 0.0102;
those numbers do not reproduce, and are withdrawn.

## 3. H_NN and its spectrum

```
H_NN = −i ħ_NN ( x ∂_x + ∂_x x ) / 2          (symmetric xp)
E_n  = ħ_NN ( n + ½ )                          (harmonic approximation)
```

The code uses the harmonic-oscillator approximation only, and says so in
every result (`'Harmonic oscillator approx — full xp spectrum is open'`). The
Berry–Keating conjecture is that the Riemann zeros are eigenvalues of an
operator of this form; the full xp spectrum is not computed. `xp_spectrum`
returns the classical torus x·p = d*·ħ_NN.

## 4. The T coordinate map

```
T : x ↦ x · exp( i d* ln x )      T_re = x cos(d* ln x),  T_im = x sin(d* ln x)
```

T(1) = 1, and |T(x)| = x. The map is a scaffold: whether T is unitary and
what its spectrum is are open. The code's own note records that the
interior/exterior T transform is Eichler–Shimura (Wiles 1995), which is a
statement about a different T; the xp T coordinate is unproven.

**Listing 1 — the T map at one point** (`modules/berry_keating/maths.py`,
the arithmetic of `T_map`; extracted, runs cold)

```python
import math

def T_map(x, d_star=0.246):
    phase = d_star * math.log(x)
    return x * math.cos(phase), x * math.sin(phase)

print(T_map(2.0))
```

```
(1.9709952839307414, 0.33937824138087525)
```

(These are the `T_re`, `T_im` the registry returns for x = 2.0.)

## 5. Equations

| Name | Tier | Parameters |
|---|---|---|
| `d_star_gap_report` | OPEN | — |
| `gap_candidates` | OPEN | — |
| `h_nn_eigenvalues` | OPEN | `hbar_nn`, `n_max` |
| `xp_spectrum` | OPEN | `hbar_nn` |
| `T_map` | OPEN | `x` |
| `T_map_trajectory` | OPEN | `x_min`, `x_max` |

## 6. Session

```
>>> registry.run('berry_keating.h_nn_eigenvalues', {'hbar_nn': 0.1, 'n_max': 3})
{'hbar_nn': 0.1, 'eigenvalues': [0.05, 0.15000000000000002, 0.25, 0.35000000000000003], 'spacings': [0.10000000000000002, 0.09999999999999998, 0.10000000000000003], 'mean_spacing': 0.10000000000000002, 'n_max': 3, ...}
>>> registry.run('berry_keating.d_star_gap_report', {})
{'d_star_spec': 0.246, 'd_star_taut': 0.24630720147342253, 'ln_10': 2.302585092994046, 'omega_zs': 0.5671432904097838, 'd_star_x_ln10': 0.5664359328765353, 'gap': 0.000707357533248576, 'gap_taut': 0.0, ...}
```

## 7. Related pages

[03 Inversion](03_inversion_engine.md) · [14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) ·
[17 α · Ω · d*](17_alpha_omega_d_star.md) · [102 Berry–Keating and Hilbert–Pólya](102_berry_keating_hilbert_polya.md) ·
[133 Canonical maths](133_canonical_maths.md)
