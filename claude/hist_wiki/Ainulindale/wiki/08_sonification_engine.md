# 08 — SONIFICATION ENGINE  ω = pitch

**Module:** `sonification`  **Version:** 0.111  **Confidence floor:** ESTABLISHED

## Philosophy

Every sound is a derivation. ω (angular frequency) = pitch.

No floating point in the signal chain until the WAV render boundary. All frequencies are exact `fractions.Fraction` ratios of concert A = 440 Hz. Just intonation throughout.

This module feeds the viewer's `sonification` display mode. The standalone **Ainulindale Synthesizer** is a separate repo (not yet created — see TODO).

## Particle-Frequency Table (Just Intonation)

All frequencies are exact rational multiples of A = 440 Hz.

| Particle | Frequency | Ratio | Instrument |
|----------|-----------|-------|------------|
| Higgs | 110 Hz | 1/4 | cello (ground state) |
| Photon | 1760 Hz | 4/1 | flute (massless) |
| Electron | 550 Hz | 5/4 | oboe |
| W+ | 660 Hz | 3/2 | french horn (ascending) |
| W- | 587 Hz | 4/3 | french horn (descending) |
| Z0 | 55 Hz | 1/8 | tuba (neutral, massive) |
| Gluon_1 | 220 Hz | 1/2 | percussion voice 1 |
| φ attractor | 733 Hz | 5/3 | — |
| d* | 137.5 Hz | 5/16 | — |
| Stratum ℝ | 110 Hz | 1/4 | — |
| Stratum ℂ | 275 Hz | 5/8 | — |
| Stratum ℍ | 330 Hz | 3/4 | — |
| Stratum 𝕆 | 880 Hz | 2/1 | — |

## Quasi-Particle Rests (Exact Integer Samples)

| Rest | Samples | Duration | Meaning |
|------|---------|----------|---------|
| Phonon | SR/4 | 0.25 beats | medium vibrating after note |
| Exciton | SR/2 | 0.5 beats | particle/antiparticle gap |
| Magnon | SR×3/8 | 0.375 beats | spin settling (ℍ layer) |
| Roton | SR×3/4 | 0.75 beats | deep breath before 𝕆 |
| Plasmon | SR | 1 beat | collective dissolving |
| **Gravinon** | SR×144/89 | **phi convergent** | layer crossing rest |

The Gravinon rest duration 144/89 beats converges to φ (Fibonacci ratio). This is exact integer arithmetic — no irrational numbers.

## Wavetables

| Name | Description |
|------|-------------|
| `sine` | pure sine |
| `rydberg` | hydrogen Rydberg superposition: Σ sin(2πn²t)/n² |
| `higgs_hat` | oscillation around Mexican hat minimum |
| `phi_recursion` | r_{n+1} = 1+1/r_n deviation from φ |
| `fano` | 7-harmonic Fano plane superposition |

## Viewer Integration

The `sonification` display mode is a first-class viewer mode alongside `complex_plane`, `3d_cartesian`, `fano`, and `text`. The `SonificationPanel` in `console_qt.py` handles play/stop via `sounddevice` (optional dependency).

## Standalone Synthesizer

The standalone Ainulindale Synthesizer (`ainulindale_sonification_mv1.py`) is a separate repo (not yet created). It receives from the sonification module but is architecturally independent. Peter-and-the-Wolf structure: each particle introduced alone.

## Shell commands
```python
tone('higgs')         # ω for Higgs particle
wavetable('rydberg')  # Rydberg wavetable
```
