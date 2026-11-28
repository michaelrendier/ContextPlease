# 02 — Module Registry Contract

| | |
|---|---|
| Source | `ValaQuenta/engine/registry.py` (classes `Equation`, `EquationModule`, `ModuleRegistry`; `CONFIDENCE`; `weakest_tier`) |
| Registration site | `ValaQuenta/__main__.py::_register_all()` |
| Tests | `ValaQuenta/tests/test_registry.py`, `tests/test_docstrings.py` |
| Last verified | 2026-11-13, against `registry.py` and the live registry (41 modules, 357 equations) |

## 1. Rule

The engine and the viewer reach a module only through the registry. A module
never imports the viewer; the viewer never imports a module's internals. The
mathematics lives in `maths.py` (plain functions, no I/O, no GUI imports); the
contract lives in `tools.py` (an `EquationModule` subclass).

## 2. The `Equation` descriptor

Constructed as `Equation(name, display, latex, radian_form, confidence,
code_verified, params, compute=None, display_options=None, process=None)`.

| Field | Meaning |
|---|---|
| `name` | short identifier, unique within the module |
| `display` | human-readable title |
| `latex` | string for the viewer (the maths pages themselves are written in Unicode) |
| `radian_form` | the equation in radian-primary units |
| `confidence` | the **weakest tier named** in the authored label (see §4) |
| `confidence_note` | the label exactly as authored |
| `code_verified` | `True` if executable code backs it |
| `params` | parameter names |
| `compute` | callable taking the parameters, or `None` |
| `display_options` | viewer modes it supports |
| `process` | a plain-English, outside-observer line: "Given X, computes Y by Z". It feeds the proof-on-the-fly in the curses console. A missing `process` renders as a visible TODO (`[process= not set]`) |

`Equation.declaration()` returns all of this as a dict for the derivation
browser.

## 3. The `EquationModule` base class

Abstract members a module must define:

| Member | Kind | Content |
|---|---|---|
| `name` | property | short id, e.g. `'inversion'` |
| `display_name` | property | human-readable |
| `version` | property | e.g. `'0.111'` |
| `description` | property | one paragraph |
| `confidence_floor` | property | the lowest tier of any claim in the module |
| `formulary()` | method | the list of `Equation` objects |
| `run(equation_name, params)` | method | returns a dict with at least `result`, `equation`, `params` |
| `viewer_data(equation_name, params, display_mode)` | method | data shaped for a display mode ([11](11_viewer.md)) |

Provided with defaults: `process_description` (first sentence of
`description`), `manifest()` (loads `modules/<name>/manifest.json`, or builds a
live scaffold), `on_register(registry)` (hook, no-op), `shell_commands()`
(dict of console commands, empty by default), `summary()`.

## 4. Confidence tiers

| Mark | Tier | Meaning |
|---|---|---|
| ✓ | ESTABLISHED | verified by code and/or established mathematics |
| ◈ | THEORETICAL | a defined test or derivation path exists |
| ◇ | CONJECTURE | a named direction; no formal derivation |
| ? | OPEN | an active open problem |

A label may name several tiers (`ESTABLISHED+THEORETICAL`: established parts
plus a theoretical operator identity). `weakest_tier(label)` reduces it to the
**weakest** tier named, strongest-first order ESTABLISHED, THEORETICAL,
CONJECTURE, OPEN, so an equation is never carried stronger than its weakest
part. A label that names no tier is returned unchanged.

**Listing 1 — reducing a label to one tier** (`engine/registry.py`,
`weakest_tier`; extracted: docstring removed, runs cold)

```python
CONFIDENCE = {'ESTABLISHED': '✓', 'THEORETICAL': '◈', 'CONJECTURE': '◇', 'OPEN': '?'}
_TIER_ORDER = ('ESTABLISHED', 'THEORETICAL', 'CONJECTURE', 'OPEN')

def weakest_tier(label):
    if label in CONFIDENCE:
        return label
    named = [t for t in _TIER_ORDER if t in label]
    return named[-1] if named else label

print(weakest_tier('ESTABLISHED+THEORETICAL'))
print(weakest_tier('COMPUTATIONAL'))
```

```
THEORETICAL
COMPUTATIONAL
```

The second line is a live inconsistency: `clay_millennium` registers one
equation with the label `COMPUTATIONAL`, which names none of the four tiers,
so it passes through unchanged and appears in the registry as a fifth tier.
Tier counts over all 357 equations (2026-11-13): ESTABLISHED 217,
THEORETICAL 112, OPEN 21, CONJECTURE 6, `COMPUTATIONAL` 1.

## 5. The registry

`ModuleRegistry`: `register(module)` (rejects a duplicate name with
`ValueError`; indexes every equation as `module.equation`), `get_module(name)`,
`get_equation('module.equation')`, `list_modules()` (registration order),
`list_equations(module=None)`, `run('module.equation', params)` (raises
`KeyError` for an unknown module, `ValueError` for a name without a dot) and
`summary()`.

```
>>> registry.run('inversion.inversion_map', {'r': 2.0, 'theta_rad': 0.0})
(0.5, 1.5707963267948966)
```

## 6. Adding an engine: the Full Engine Protocol

An engine is not finished when its code runs. Six artifacts are required,
because code alone is undiscoverable from a cold context.

| # | Artifact | Where |
|---|---|---|
| 1 | Engine | `modules/<name>/{__init__,maths,tools}.py`; registered in `__main__.py::_register_all()`; listed in `modules/__init__.py` |
| 2 | Notebook | `notebooks/…/NN_<name>.ipynb`; exercises the formulary and shows open items |
| 2b | Proof locale | `engine/proof_locale/<name>.json`: operators, ordering and per-equation overrides for the proof-on-the-fly |
| 2c | Manifest | `modules/<name>/manifest.json`: provenance, environment constants, UI registration. `python3 -m ValaQuenta --manifests` validates all of them |
| 3 | Ainulindale wiki page | `Ainulindale/wiki/NN_<name>.md`: origin, what changed, boundaries |
| 4 | ValaQuenta wiki page | `ValaQuenta/wiki/<name>.md`: file, class, claim, mechanism, confidence table |
| 5 | `.clauderc_ValaQuenta` entry | `export CTX_<NAME>=…` and the name appended to `VALAQUENTA_ENGINE_INDEX` |
| 6 | Toolbox page | `ValaQuenta/wiki/toolbox/NN_<name>.md`, generated from the registry; required for every new tool |

Standing rules from `registry.py`:

- Pure Python in `maths.py`; ratios as `fractions.Fraction`; floats only at the output boundary.
- Every equation carries a confidence tier, a radian-primary form and `process=`.
- A new engine starts at version 1.0 and is incremented each time it is touched; older engines keep their numbers until next touched (nothing is renumbered retroactively).
- All ValaQuenta code and mathematics are GPL-3.0-only. Material under an incompatible licence is never vendored.
- ValaQuenta's own wiki is strictly API reference; narrative and origin belong to this wiki.

## 7. Viewer data shapes

See [11](11_viewer.md) §2.

## 8. Related pages

[01 Overview](01_overview.md) · [11 Viewer](11_viewer.md) · [03 Inversion](03_inversion_engine.md) (a worked module)
