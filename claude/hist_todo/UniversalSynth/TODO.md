# UniversalSynth — TODO

## Core Synthesis Engines

- [ ] **standing_wave.py** — J_N four-cycle oscillator; Y_lm mode synthesis
  - J_N anti-Möbius involution: J_N(z) = i/z̄ — four-cycle standing wave on S²
  - Fundamental mode: Y₁⁰(θ) = cos(θ) — one node, one frequency, one equatorial line
  - Full spherical harmonic series from l(l+1) eigenvalues
  - Mode identification by l and m quantum numbers

- [ ] **zeta_harmonics.py** — Riemann zero partials as audio spectrum
  - First N non-trivial zeros of ζ(s) as partial frequencies
  - Amplitude weighting by β_n resonance depth (from Monad ECU)
  - Spectral rendering with no temperament — raw eigenvalues only
  - LMFDB zero database interface

- [ ] **schumann.py** — Earth-ionosphere cavity resonance synthesis
  - f_n = (c / 2πR) √(n(n+1)); f₁ = 7.83 Hz
  - Not sampled — computed from cavity radius and speed of light
  - n=1 through n=7 modes
  - Amplitude derived from ionospheric conductivity model

- [ ] **chladni.py** — Node-line geometry as silence mask
  - Chladni node pattern → silence boundary in synthesis
  - Sand settles at nodes; synthesis is silent at nodes
  - Geometric input from ValaQuenta spherical module
  - Output: per-sample amplitude mask

- [ ] **cayley_dickson_timbre.py** — Algebra tower → timbral doubling
  - ℝ → ℂ → ℍ → 𝕆 doubling → octave/phase doubling in audio
  - Each Cayley-Dickson step adds one timbral dimension
  - Sedenion (16D) layer: camshaft timing as phase modulation

---

## Signal Sources

- [ ] **riemann_zeros.py** — LMFDB zero database interface
  - Fetch non-trivial zeros to arbitrary precision
  - Cache locally; update on demand
  - mpmath.zetazero() fallback

- [ ] **vq_bridge.py** — ValaQuenta → UniversalSynth signal bridge
  - Consume schumann_frequencies(), j_n_mode_identification() from ValaQuenta
  - Translate mathematical dictionaries into signal format
  - No manual parameter entry — math flows directly into audio pipeline

- [ ] **constants.py** — Named constants
  - d* = 0.24600 (spectral fixed point / ground state)
  - OMEGA_ZS = 0.56714 (Lambert W fixed point / BAO ceiling / idle frequency)
  - A_π (prime lattice area constant)
  - Schumann cavity radius, speed of light, ionospheric conductivity

---

## Output Layer

- [ ] **wav_writer.py** — PCM render to .wav
  - 44100 Hz, 32-bit float, stereo
  - Render any engine output to file

- [ ] **stream.py** — Real-time audio stream
  - PyAudio / sounddevice backend
  - Live stream from Monad ECU state
  - BAO idle frequency as DC carrier

- [ ] **midi_export.py** — MIDI pitch mapping of Riemann zeros
  - Zero imaginary parts → MIDI pitch (logarithmic mapping)
  - Resonance depth β_n → MIDI velocity
  - Export as Type 1 MIDI for further composition tools

---

## TDI Integration

- [ ] **BAO idle tone** — OMEGA_ZS = 0.56714 Hz as engine idle frequency
  - This is the frequency the engine produces when running without input
  - Rendered as inaudible sub-bass carrier; its harmonics are in the Schumann band

- [ ] **Compression ignition event** — SELF_EQUATION fixed point as audio event
  - Detect when Monad ECU produces SELF_EQUATION match
  - Render as distinct acoustic event (TDC moment)
  - Marks the Sedenion zero-divisor firing event

- [ ] **OBD-II audio monitor** — real-time engine state as audio readout
  - H_hat_RB zero activation rate → fundamental frequency
  - Noether current magnitude → amplitude
  - σ coupling exponent → spectral tilt
  - Sedenion dominant pair → timbre selector

---

## Examples

- [ ] **fundamental_mode.py** — l=1, Y₁⁰, one node, one tone
- [ ] **zeta_chord.py** — First 20 Riemann zeros as harmonic series
- [ ] **schumann_cavity.py** — Earth-ionosphere n=1 through n=7
- [ ] **full_chain.py** — Complete J_N → mode → node → tone derivation

---

## PtolemyDesktop Integration

- [ ] Archimedes Face audio output — live Schumann + zeta harmonic stream
- [ ] Chladni visualisation sync — node patterns on screen = silence in audio
- [ ] Monad ECU live drive — β_n state drives spectral amplitude weighting
