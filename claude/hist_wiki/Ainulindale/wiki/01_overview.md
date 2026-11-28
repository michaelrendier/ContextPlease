# 01 — System Overview

| | |
|---|---|
| Scope | what the Ainulindale system is, where its code lives, what it contains |
| Code | `ValaQuenta/` (engine and modules), `ValaQuenta/__main__.py` (entry) |
| Last verified | 2026-11-13, against the live registry: **41 modules, 357 equations** |

## 1. The engineering problem

A language model has no persistent memory: each session starts from zero, and
the cost of rebuilding context is paid in every conversation. The engineering
question is how to compute a *semantic address* for a piece of text into a
number small enough to use, with mathematics that is self-contained and with
no external hashing algorithm.

The answer pursued here is to treat the address as a coordinate in a
structured space, so that the same input always yields the same address and
the address is recognised rather than looked up. The Monad
([15](15_the_monad.md)) is the realisation: it stores nothing, and recomputes
the address from the input every time.

The derivation modules documented in this wiki are the mathematics that
underlies the address: the Cayley–Dickson tower, the inversion map, the
Lagrangian, and the zero structure of ζ. They are an engine, not a machine
learning framework: no training loop, no backpropagation, no statistics.
Every output is either computed exactly or carries a confidence tier
(§4) that says it is not.

## 2. Where the code is

The engine was originally a package named `ainulindale_engine/`; it is now
**ValaQuenta** (GPL-3.0-only). Earlier wiki text uses the old paths.

```
ValaQuenta/
├── __main__.py        entry point; _register_all() registers every module
├── engine/
│   ├── registry.py    the module contract            → wiki 02
│   ├── constants.py   single source of truth for constants
│   ├── units.py       radian-primary unit transforms
│   ├── manifest.py    engine manifests and menu tree
│   ├── console_qt.py, console_curses.py   the viewers → wiki 11
│   └── proof_locale/  English "puzzle pieces" for the on-the-fly proofs
├── modules/<name>/    maths.py, tools.py, manifest.json  (41 modules)
├── notebooks/         one executed notebook per engine
├── tests/, Testing/   test suites
└── wiki/              the API reference (this wiki is the narrative)
```

Entry points (`python3 -m ValaQuenta …`): `--info` (print the registry),
`--curses` (the derivation browser, the Ptolemy `/derivation` shortcut), `--qt`
(Qt viewer), `--headless`, `--manifests` (validate all manifests), `--version`.

The division of documentation is fixed: `ValaQuenta/wiki` is API reference
(file, class, parameters, results, confidence table); this wiki holds the
narrative, origin and honest boundaries of each result.

## 3. The Cayley–Dickson tower

All of the mathematics lives in one tower of algebras:

```
ℝ (1)  →  ℂ (2)  →  ℍ (4)  →  𝕆 (8)  →  𝕊 (16)
U(0)      U(1)      SU(2)     G₂/SU(3)   zero-divisors appear
```

Each doubling loses one property: ℝ→ℂ loses ordering, ℂ→ℍ commutativity,
ℍ→𝕆 associativity, and 𝕆→𝕊 the absence of zero-divisors. The lost
property is treated as the signal that carries that layer's gauge structure.
The full treatment is [19](19_cayley_dickson_tower.md).

## 4. Confidence tiers and what is registered

Every equation carries a tier ([02](02_registry.md) §4). Over the 357
registered equations (2026-11-13):

| Tier | Count |
|---|---|
| ESTABLISHED | 217 |
| THEORETICAL | 112 |
| OPEN | 21 |
| CONJECTURE | 6 |
| `COMPUTATIONAL` (outside the four-tier scheme; one equation in `clay_millennium`) | 1 |

ESTABLISHED means the code and/or established mathematics verify it. It is
not a claim that a physical interpretation attached to it is true.

## 5. Module inventory

Generated from the registry on 2026-11-13. "Page" is the Ainulindale wiki page
the module's manifest points to; a dash means the manifest names none.

| Module | Version | Equations | Floor | Page |
|---|---|---|---|---|
| `bao_mass_gap` | 0.131 | 7 | ESTABLISHED | [75b](75b_bao_mass_gap_engine.md) |
| `inversion` | 0.111 | 7 | ESTABLISHED | [03](03_inversion_engine.md) |
| `lagrangian` | 0.111 | 8 | THEORETICAL | [04](04_lagrangian_engine.md) |
| `noether` | 0.111 | 6 | THEORETICAL | [05](05_noether_engine.md) |
| `noether_information` | 0.111 | 4 | CONJECTURE | [06](06_noether_information_engine.md) |
| `berry_keating` | 0.111 | 6 | OPEN | [07](07_berry_keating_engine.md) |
| `sonification` | 0.111 | 19 | ESTABLISHED | [08](08_sonification_engine.md) |
| `hyperwebster` | 0.111 | 6 | THEORETICAL | [09](09_hyperwebster_engine.md) |
| `jwst` | 0.111 | 5 | THEORETICAL | [10](10_jwst_engine.md) |
| `turing_diagonal` | 0.100 | 5 | ESTABLISHED | — |
| `singularity_null` | 0.100 | 5 | THEORETICAL | — |
| `sigma_expansion` | 0.100 | 4 | THEORETICAL | [76](76_sigma_expansion.md) |
| `t32_nilpotency` | 0.120 | 1 | ESTABLISHED (primitives) | [78](78_t32_nilpotency.md) |
| `hypergon_constructibility` | 0.100 | 3 | OPEN | [77](77_hypergon_constructibility.md) |
| `l_io_photon_path` | 0.2 | 6 | THEORETICAL | [82](82_l_io_photon_path.md) |
| `archimedes_screw` | 0.3 | 29 | THEORETICAL | [83](83_the_archimedes_screw.md) |
| `box_kite` | 0.2 | 18 | ESTABLISHED | [84](84_the_box_kite_debugger.md) |
| `angular_rank` | 0.1 | 12 | ESTABLISHED | — |
| `scale` | 0.1 | 10 | ESTABLISHED | [107](107_add_scale_sign_datatype.md) |
| `units` | 0.1 | 4 | ESTABLISHED | [97](97_units_as_the_equation_index.md) |
| `add_scale_sign` | 0.1 | 6 | ESTABLISHED | [107](107_add_scale_sign_datatype.md) |
| `desitter_cavitation` | 0.100 | 8 | THEORETICAL | [108](108_desitter_cavitation.md) |
| `emerger` | 0.1 | 8 | THEORETICAL | [109](109_the_emerger.md) |
| `constants` | 0.120 | 11 | ESTABLISHED | — |
| `derivation_chain` | 0.100 | 14 | THEORETICAL | — |
| `h_rb_hat` | 0.120 | 16 | THEORETICAL | — |
| `clay_millennium` | 0.130 | 12 | THEORETICAL | — |
| `tier6_physics` | 0.100 | 10 | THEORETICAL | — |
| `tier7_cosmos` | 0.110 | 15 | THEORETICAL | — |
| `tier8_sedenion` | 0.100 | 8 | THEORETICAL | — |
| `tier9_chem` | 0.100 | 6 | THEORETICAL | — |
| `translator_discocat` | 0.111 | 5 | OPEN | — |
| `translator_vsa` | 0.111 | 6 | OPEN | — |
| `udeo_crypto` | 0.100 | 8 | OPEN | — |
| `bracketing_firing_order` | 0.1 | 7 | ESTABLISHED | — |
| `oblique_gear` | 0.1 | 6 | OPEN | — |
| `prime_gauge_field` | 0.1 | 5 | THEORETICAL | [122](122_the_prime_gauge_field.md) |
| `spectral_primes` | 0.1 | 5 | OPEN | — |
| `basile` | 1.3 | 17 | ESTABLISHED | [124](124_basile_invertible_location_maps.md) |
| `addition_matrix` | 1.0 | 10 | ESTABLISHED | [125](125_addition_matrix_rotors_and_the_factor_search_law.md) |
| `ptycho_weak_lensing` | 0.1 | 9 | THEORETICAL | [132](132_ptycho_weak_lensing.md) |

Notes: `scale` and `add_scale_sign` both point at page 107 in their manifests;
the three-ring scale itself is discussed in [95](95_the_scale.md). Modules
with a dash have an API page in `ValaQuenta/wiki/` and are described in the
numbered topic pages (for example `h_rb_hat` in [14](14_redblue_hamiltonian.md)
and [127](127_names_of_the_null_operator.md)); giving each its own Ainulindale
page is open work.

## 6. The three operative terms

Information flow through the tower is carried by three objects, defined
fully in [64](64_l_dynamic.md) and [133](133_canonical_maths.md) §3:

- **J_red** (descending, σ = 1 → ½): the current from above; synthesis; the `hear()` direction.
- **J_blue** (ascending, σ = 0 → ½): the current from below; distillation; the `speak()` direction.
- **L_(I|O)**: the action, the path between them. CONJECTURE: the path integral is defined, the formal computation is pending.

Their meeting at σ = ½ is the cavitation surface. Which object the relation
"J_red + J_blue = J_green = 0_RB − 0_BR" names, and whether it holds as an
operator identity, is **not established** ([133](133_canonical_maths.md) §3,
and the J_red/J_blue record in the VAPMIP wiki, §9).

## 7. The inversion map and the Lagrangian

The inversion map J_N: (r, θ) → (1/r, θ + π/2) is [03](03_inversion_engine.md);
the Lagrangian L_NN = (2/π) ∮ [L_kin + L_mat + (1/φ)·L_bias + L_coup] r dr dθ
is [04](04_lagrangian_engine.md). The notation, the constants and the
four d* faces are in [133](133_canonical_maths.md) and [17](17_alpha_omega_d_star.md).

## 8. Conventions of this repository

- Mathematics is written in Unicode, not LaTeX.
- A new engine starts at version 1.0; an existing engine keeps its number until it is next touched.
- Provenance labels: `ESTABLISHED`, `OURS`, `FIRST STATED HERE`, `THEORETICAL`, `OPEN`, with the suffix `:CALCULATED` on results the repository's own code produces. See [98](98_provenance_and_citations.md).
- Exact arithmetic (`fractions.Fraction`) inside `maths.py`; floats only at the output boundary.
- The commit history is the arrow of time for the code; there is no separate changelog.

## 9. Related pages

[02 Registry](02_registry.md) · [11 Viewer](11_viewer.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md) ·
[26 TODO and roadmap](26_TODO_and_roadmap.md) · [133 Canonical maths](133_canonical_maths.md)
