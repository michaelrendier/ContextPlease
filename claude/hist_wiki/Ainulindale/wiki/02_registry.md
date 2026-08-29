# 02 — MODULE REGISTRY CONTRACT

## The Contract

Every module in `ainulindale_engine/modules/` implements `EquationModule` from `engine/registry.py`.

The engine and viewer never import module internals. They call only the contract methods. The module never imports the viewer. They communicate only through this registry contract.

## Required Properties

```python
@property
def name(self) -> str:           # short identifier, e.g. 'inversion'
def display_name(self) -> str:   # human-readable, e.g. 'Inside-Out Inversion Engine'
def version(self) -> str:        # e.g. '0.111'
def description(self) -> str:    # one paragraph
def confidence_floor(self) -> str: # minimum confidence tier
```

## Required Methods

### `formulary() -> List[Equation]`
Returns all equations this module contributes. Called once at registration, cached.

Each `Equation` has:
- `name`: short identifier
- `display`: human-readable
- `latex`: LaTeX string for viewer
- `radian_form`: equation in radian-primary units
- `confidence`: one of `ESTABLISHED / THEORETICAL / CONJECTURE / OPEN`
- `code_verified`: bool
- `params`: list of parameter names
- `compute`: callable or None
- `display_options`: list of viewer mode strings

### `run(equation_name, params) -> Dict`
Execute a named equation. Returns `{equation, params, result, module}`.

### `viewer_data(equation_name, params, display_mode) -> Dict`
Return data formatted for a specific display mode. Structure is mode-dependent.

Display modes: `text | complex_plane | 3d_cartesian | fano | sonification`

## Optional Methods

```python
def on_register(self, registry)  # called at registration
def shell_commands(self) -> Dict # injected into QTermWidget REPL
```

## Confidence Tiers

| Symbol | Tier | Meaning |
|--------|------|---------|
| ✓ | ESTABLISHED | Verified by code and/or established mathematics |
| ◈ | THEORETICAL | Defined test or derivation path exists |
| ◇ | CONJECTURE | Named direction; no formal derivation yet |
| ? | OPEN | Active open problem |

## How to Add a Module

1. Create `ainulindale_engine/modules/your_module/`
2. Add `__init__.py`, `maths.py`, `tools.py`
3. `maths.py`: pure mathematics, no I/O, no GUI imports
4. `tools.py`: `YourModule(EquationModule)` — implements the contract
5. `__init__.py`: `from .tools import YourModule`
6. In `__main__.py`: import and `register(YourModule())`

## Viewer Data Shapes

### `text`
```python
{'text': str}
```

### `complex_plane`
```python
{
  'type': 'polar_trajectory',
  'trajectory': [(r, theta), ...],
  'cartesian':  [(x, y), ...],
  'fixed_point': (x, y),   # optional
  'phi':         (x, y),   # optional
}
```

### `3d_cartesian`
```python
{
  'type':   '3d_flow',
  'points': [(x, y, z), ...],
  'axes':   ('x_label', 'y_label', 'z_label'),
}
```

### `fano`
```python
{
  'type':      'fano',
  'highlight': [int, ...],  # generator indices to highlight
  'labels':    [str, ...],  # 7 point labels
  'text':      str,
}
```

### `sonification`
```python
{
  'omega':      float,   # angular frequency rad/s
  'freq_hz':    float,
  'label':      str,
  'waveform':   [float, ...],  # 512-point preview
  'duration_s': float,
}
```
