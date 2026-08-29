# 11 — VIEWER  Qt + Curses

## Overview

The viewer is a display skin. It is fixed. Modules are tailored to the viewer, not the other way around. Each module delivers `viewer_data()` shaped for its display mode; the viewer renders what it receives.

## Qt Viewer (`console_qt.py`)

**Launch:** `python3 -m ainulindale_engine --qt`

### Layout

```
+-----------------------------+------------------+
|  VisPy Canvas               |  MODULE LIST     |
|  [fano/complex/3d/soni/text]|  equation select |
|                             |  param controls  |
+-----------------------------+------------------+
|  QTermWidget shell          |  OUTPUT / INFO   |
+-----------------------------+------------------+
```

### Components

**VispyCanvas** — renders 5 display modes:
- `complex_plane` — polar trajectory plot (r, θ)
- `3d_cartesian` — 3D flow, VisPy scatter/line
- `fano` — Fano plane (7 points, 7 lines, G2/SU(3) structure)
- `sonification` — waveform preview from module's omega data
- `text` — structured text overlay

**SonificationPanel** — visible only in `sonification` mode. Shows ω, frequency, play/stop buttons. Plays via `sounddevice` (optional).

**SelectorPanel** — module list → equation list → display mode → params → Run. Display mode options filter automatically to what each equation supports.

**OutputPanel** — always receives text result regardless of display mode.

**ShellPanel** — QTermWidget when available, fallback Python REPL. All module `shell_commands()` injected into REPL namespace at startup.

### Dependencies

| Dependency | Required | Fallback |
|-----------|----------|---------|
| PyQt5 | yes | falls back to curses |
| VisPy | no | text fallback in canvas |
| QTermWidget | no | built-in Python REPL |
| numpy | no | VisPy renders disabled |
| sounddevice | no | play button disabled |

### Graceful Degradation

```
Qt available → Qt viewer
Qt missing   → curses console
Qt + curses missing → headless text
```

## Curses Console (`console_curses.py`)

**Launch:** `python3 -m ainulindale_engine --curses`

**Ptolemy shortcut:** `/derivation` in Ptolemy shell runs this mode.

### Layout

```
+----------------------------------+
| AINULINDALE  v0.111              |
+----------------+-----------------+
| MODULE LIST    | EQUATION LIST   |
+----------------+-----------------+
| PARAMS         | OUTPUT          |
+----------------------------------+
| [ status bar ]                   |
+----------------------------------+
```

### Keys

| Key | Action |
|-----|--------|
| Tab | cycle focus (modules / equations / output) |
| ↑ ↓ | navigate lists |
| Enter | run selected equation |
| d | cycle display mode |
| q / Esc | quit |

### Display Modes in Curses

`text` mode only (curses cannot render VisPy). All other modes fall back to text output. The curses console is the `/derivation` shortcut — full VisPy rendering requires the Qt viewer.
