# midi

**Skill:** `~/.claude/skills/midi/` · mirror `ContextPlease/claude/skills/midi/` · **Created:** 2026-11-20 (author: Cody Michael Allison): "make yourself a midi skill... the core should be the NES video game MIDI directory, contemporary to Mega Man 2... i use midi as sheet music... also to generative ai some things up for me later... sample manipulation similar to JWST envelope stretching... a connection to the universal synth wavetable."

Stdlib Standard MIDI File reader/writer, a corpus survey, astronomy-style stretches on velocity and time envelopes, a wavetable renderer bridging to `UniversalSynth/wavetables/`, and Yamaha P-105 helpers.

**Findings at creation (measured):**
- `~/Music/Video Game Music/Midi/` is zero-filled (472 files, none with an `MThd` header). The intact copy is `~/Desktop/Desktop Archive/thisonemine/Music/Video Game Music/` (515 valid files). Nothing was overwritten.
- There is no Mega Man 2 MIDI in either copy; the Mega Man material is MP3.
- 80 of 515 files are NES-voiced (≤ 4 voices at the 95th percentile, ≤ 5 channels), 79 of them in `Midi/`; the rest are General MIDI arrangements.
- Keyboard: Yamaha P-105, `0499:160f`, ALSA card `Digital Piano`. Official manuals saved in `claude/references/yamaha_p105/`.
