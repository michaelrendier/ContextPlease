# 08 — Sonification Engine (ω = pitch)

| | |
|---|---|
| Module | `sonification` — `ValaQuenta/modules/sonification/` |
| Class | `SonificationModule` |
| Version | 0.111 |
| Confidence floor | ESTABLISHED |
| API page | `ValaQuenta/wiki/sonification.md` |
| Notebook | `ValaQuenta/notebooks/core/08_sonification.ipynb` |
| Last verified | 2026-11-13, against the live registry (19 equations, all ESTABLISHED) |

## 1. Definition

A derivation is made audible by taking its angular frequency ω as pitch.
Every frequency is an exact rational multiple of concert A = 440 Hz
(`fractions.Fraction`, just intonation); a float appears only where a WAV
sample is written. The module feeds the viewer's `sonification` display mode
([11](11_viewer.md)).

"ESTABLISHED" here means the arithmetic is exact and reproducible. It does
not assert that the chosen particle-to-ratio assignments are physics: they
are a mapping, fixed by the code's `FREQ` table.

## 2. The frequency table (`FREQ`)

Selected rows, exactly as stored (Hz = 440 × ratio):

| Name | Frequency (Hz) | Ratio to 440 | Name | Frequency (Hz) | Ratio |
|---|---|---|---|---|---|
| `higgs` | 110 | 1/4 | `W_plus` | 660 | 3/2 |
| `Z0` | 55 | 1/8 | `W_minus` | 1760/3 ≈ 586.7 | 4/3 |
| `photon` | 1760 | 4 | `gluon_1` | 220 | 1/2 |
| `electron`, `positron` | 550 | 5/4 | `phi_attractor` | 2200/3 ≈ 733.3 | 5/3 |
| `stratum_R` | 110 | 1/4 | `d_star` | 275/2 = 137.5 | 5/16 |
| `stratum_C` | 275 | 5/8 | `stratum_H` | 330 | 3/4 |
| `stratum_O` | 880 | 2 | | | |

The table also holds the three neutrinos, gluons 2–8 and the six quarks
(`up` 1100, `down` 3520/3, `strange` 2475/4, `charm` 1320, `bottom` 2200/3,
`top` 3520). `d_star` here is the stored tone 137.5 Hz, a pitch assignment,
not a statement of d*'s value.

## 3. Quasi-particle rests

A rest is an exact integer number of samples. The unit is the **beat**,
`BEAT_SAMPLES = 22050` (half a second at `SAMPLE_RATE = 44100`).

| Rest | Beats | Samples (as computed) |
|---|---|---|
| phonon | 1/4 | 5512 |
| exciton | 1/2 | 11025 |
| magnon | 3/8 | 8268 |
| roton | 3/4 | 16537 |
| plasmon | 1 | 22050 |
| gravinon | 144/89 ≈ 1.6180 | 35676 |

The gravinon is the Fibonacci convergent 144/89 of φ, in whole samples:
`GRAVINON_SAMPLES = (BEAT_SAMPLES * 144) // 89`. (Earlier wording gave the
rests as multiples of the sample rate; the unit is the half-second beat.)

**Listing 1 — the rests** (`modules/sonification/maths.py`, constants and
`QUASIPARTICLE_RESTS`; extracted, runs cold)

```python
BEAT_SAMPLES = 22050
FIB_NUM, FIB_DEN = 144, 89
rests = {
    'phonon':   BEAT_SAMPLES // 4,
    'exciton':  BEAT_SAMPLES // 2,
    'magnon':   BEAT_SAMPLES * 3 // 8,
    'roton':    BEAT_SAMPLES * 3 // 4,
    'plasmon':  BEAT_SAMPLES,
    'gravinon': (BEAT_SAMPLES * FIB_NUM) // FIB_DEN,
}
print(rests)
```

```
{'phonon': 5512, 'exciton': 11025, 'magnon': 8268, 'roton': 16537, 'plasmon': 22050, 'gravinon': 35676}
```

## 4. Wavetables

`wavetable(name)` for `name` in:

| Name | Waveform |
|---|---|
| `sine` | pure sine |
| `rydberg` | hydrogen Rydberg superposition, 1/n² weights |
| `higgs_hat` | oscillation about the Mexican-hat minimum |
| `phi_recursion` | the r → 1 + 1/r spiral |
| `fano` | seven-harmonic Fano-plane superposition |

## 5. Equations

19 equations, all ESTABLISHED: 13 tones (`tone_higgs`, `tone_photon`,
`tone_electron`, `tone_W_plus`, `tone_W_minus`, `tone_Z0`, `tone_gluon_1`,
`tone_phi_attractor`, `tone_d_star`, `tone_stratum_R`, `tone_stratum_C`,
`tone_stratum_H`, `tone_stratum_O`), 5 wavetables (`wavetable_sine`,
`wavetable_rydberg`, `wavetable_higgs_hat`, `wavetable_phi_recursion`,
`wavetable_fano`), and `quasiparticle_rests`. Each tone returns
`{'omega', 'freq_hz', 'label'}`.

## 6. Session

```
>>> registry.run('sonification.tone_higgs', {})
{'omega': 691.1503837897545, 'freq_hz': 110.0, 'label': 'higgs'}
>>> registry.run('sonification.quasiparticle_rests', {})
{'phonon': 5512, 'exciton': 11025, 'magnon': 8268, 'roton': 16537, 'plasmon': 22050, 'gravinon': 35676}
```

Console commands: `tone(name)`, `wavetable(name)`.

## 7. Playback and the synthesizer

`SonificationPanel` in `engine/console_qt.py` plays the ω tone through
`sounddevice`, which is optional; without it the play button is disabled.
The standalone Ainulindale Synthesizer is a separate program that consumes
this module's output; it is not part of this repository.

## 8. Related pages

[11 Viewer](11_viewer.md) · [21 Chladni–Zipf–Riemann](21_chladni_zipf_riemann.md) ·
[22 Constant facets](22_constant_facets.md)
