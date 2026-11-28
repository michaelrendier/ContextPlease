# 11 — Viewer (Qt and curses)

| | |
|---|---|
| Source | `ValaQuenta/engine/console_qt.py`, `ValaQuenta/engine/console_curses.py` |
| Launch | `python3 -m ValaQuenta --qt` · `--curses` · `--headless` · `--info` · `--manifests` · `--version` |
| Last verified | 2026-11-13, against the source of both consoles and `__main__.py::main` |

## 1. Rule

The viewer is a display skin and does not change. Modules conform to it: a
module returns `viewer_data(equation_name, params, display_mode)` shaped for
the requested mode, and the viewer draws what it receives. The viewer never
imports a module's internals; a module never imports the viewer. The
contract between them is [02](02_registry.md).

With no flag, `__main__.py` chooses the best interface available (Qt, then
curses, then headless text).

## 2. Display modes and data shapes

| Mode | Payload | Drawn by |
|---|---|---|
| `text` | `{'text': str}` | both consoles |
| `complex_plane` | `{'type': 'polar_trajectory', 'trajectory': [(r,θ)…], 'cartesian': [(x,y)…], 'fixed_point'?, 'phi'?}` | Qt: `VispyCanvas._render_complex_plane` |
| `3d_cartesian` | `{'type': '3d_flow', 'points': [(x,y,z)…], 'axes': (…)}` | Qt: `_render_3d` |
| `fano` | `{'type': 'fano', 'highlight': [int…], 'labels': [str…], 'text': str}` | Qt: `_render_fano` |
| `sonification` | `{'omega', 'freq_hz', 'label', 'waveform': [512 floats], 'duration_s'}` | Qt: `_render_sonification_waveform` and `SonificationPanel` |

The curses console draws `text` only; the other modes fall back to text
output. Full rendering needs the Qt viewer.

## 3. Qt viewer (`console_qt.py`)

Classes: `VispyCanvas` (the five modes above), `SonificationPanel`
(ω, frequency, play/stop), `SelectorPanel` (module → equation → display mode
→ parameters → Run), `OutputPanel` (always receives the text result),
`ShellPanel` (a Python REPL with every module's `shell_commands()` injected),
and `AinulindalWindow`, the main window (the class name is spelled this way in
the source). Entry point: `run_qt(registry)`.

Optional dependencies, each imported inside `try/except ImportError`:

| Dependency | Needed for | Without it |
|---|---|---|
| PyQt5 | the window | `--qt` reports the viewer unavailable and falls back to curses |
| VisPy, numpy | the canvas | text fallback in the canvas |
| qtermwidget | the terminal widget | the built-in REPL |
| sounddevice | audio playback | the play button is disabled |

## 4. Curses console (`console_curses.py`)

Title bar "ValaQuenta · DERIVATION BROWSER". It is the `/derivation` shortcut in
Ptolemy. The browser is a tree: modules → equations → result or proof. The
left pane lists the current level; the right pane shows the result, the
proof-on-the-fly (built from each module's `process=` strings and its
`engine/proof_locale/<name>.json`), or the module information.

| Key | Action |
|---|---|
| ↑ ↓ | move in the list, or scroll the right pane when it has focus |
| → / Enter | open, or run an equation |
| ← / Backspace / h | up one level |
| Tab | switch focus between the lists and the right pane |
| `/` | filter the current list |
| `a` | toggle the analysis-lens view |
| `i` | toggle module information |
| `d` | cycle the display mode |
| `p` | enter proof inputs |
| `r` | run the selected equation (at equation level) |
| `q` / Esc | quit |

(The keys and layout in earlier versions of this page — a four-pane layout
with "cycle focus (modules / equations / output)" and `d` as the only
extra key — described the first console; the keys above are the ones in the
source today.)

## 5. Degradation chain

```
Qt available            → Qt viewer
Qt missing              → curses console
curses unavailable      → headless: registry summary to stdout
```

## 6. Related pages

[02 Registry](02_registry.md) · [08 Sonification](08_sonification_engine.md) ·
[01 Overview](01_overview.md)
