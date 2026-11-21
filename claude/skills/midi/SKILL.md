---
name: midi
description: Cody's MIDI skill. MIDI is his sheet music and a generative-AI raw material. Reads/writes Standard MIDI Files (stdlib), surveys his NES/video-game MIDI corpus (the style foundation, Mega Man 2 era), drives the Yamaha P-105 keyboard over USB, applies astronomy-style stretches (asinh/log/gamma, JWST-like) to velocity and time envelopes, and renders MIDI through UniversalSynth single-cycle wavetables. Load for any MIDI, sheet-music, NES-music, keyboard, wavetable or sonification task.
---

# midi

Built 2026-11-20. Cody uses MIDI as **sheet music** and as the material for **generative work later**. The foundation to build everything else on is his video-game MIDI corpus (NES era, contemporary with Mega Man 2, widely held to be the best 8-bit soundtrack). Pieces added later (generators, other instruments) should extend this skill, not replace it.

## 1. THE CORPUS: read this before trusting any path
- **`~/Music/Video Game Music/Midi/` is zero-filled.** All 472 files there are the right size but every byte is `00` (checked 2026-11-20: no `MThd` header in any). Not repaired, not overwritten (his data; ask first).
- **The intact copy is `~/Desktop/Desktop Archive/thisonemine/Music/Video Game Music/`** (`Midi/` 88 files, 85 valid; plus FF Music, OC Remix, etc.): 515 valid files in the tree, 4 zero-filled (`ff1_dungeon`, `ff1_ending_theme`, `ff1_opening_theme`, `ff1_prelude`). `scripts/survey.py` defaults to it and skips any file with no `MThd`.
- **There is no Mega Man 2 MIDI in either copy.** The era is the reference, not a file. The Mega Man material he has is MP3 (Powerglove "Dr. Wily's Theme", Video Games Live "Megaman Montage", two OC ReMix tracks). If asked for "the Mega Man 2 sound", say so and work from the era's traits below, or ask him for the files.
- Also valid MIDI: `UniversalSynth/lineage/FirstAge_audio/midi` (40), `~/.ptolemy/music/` (5, e.g. `sedenion_orchestra_*.mid`), `/usr/share/doc/pianobooster/courses/*` (beginner sheet music).

## 2. What the corpus is like (MEASURED by `scripts/survey.py` → `corpus_index.csv`)
515 files; median 104 s, median 120 bpm (many files carry no tempo event), median 1,160 notes, median 7 channels, 310 with a channel-10 drum track.
**NES-voiced subset (≤ 4 simultaneous voices at the 95th percentile and ≤ 5 channels): 80 files, 79 of them from `Midi/`**: median 67 s, 451 notes, key range 44 to 82, only 13 with drums. This is the foundation style: the 2A03 has two pulse channels, one triangle, one noise and a DPCM channel, so music written for it is at most four sounding lines, mostly monophonic each, no chords except arpeggios, short loops. Everything else in the tree is a General MIDI arrangement or remix.
When writing "in the style of" this corpus: ≤ 4 voices, bass on the triangle (low register), lead on pulse 1, harmony or counter-line on pulse 2, drums as short noise hits; arpeggiate chords; loop 8 or 16 bars; ranges per the NES subset.

## 3. Tools (`scripts/`, all stdlib except render.py which needs numpy: use `ValaQuenta/.venv`)
- `smf.py`: `read(path)`, `notes(mid)`, `tempo_map`, `seconds(mid, tick)`, `write(path, fmt, ppq, tracks)`. Tolerates leading junk before `MThd`, running status, truncated tracks.
- `survey.py [DIR] [OUT.csv]`: index a directory. Columns: voices_max, voices_p95, channels, drums, lo, hi, notes, programs, seconds, tempo.
- `stretch.py IN OUT vel asinh|log|sqrt|gamma [a]` / `warp a [--inv]` / `time F`: the JWST-style envelope stretch. `vel`: v' = 127·f(v/127) lifts quiet notes (a bigger = more lift). `warp`: t' = T·asinh(a·t/T)/asinh(a), slow start, compressed end. `time`: uniform F× duration. NES files have almost flat velocity (a stretch of a Castlevania file moved 986 of 1,002 notes from 100ish to 119), so stretch the **time** and **pitch** envelopes there and use `vel` on arrangements with dynamics.
- `render.py IN OUT.wav [TABLE.wav] [--morph B.wav]`: render through a single-cycle wavetable from `UniversalSynth/wavetables/` (`hermite_psi0..7.wav`, `zeta_partials_oneshot_110Hz.wav`). `--morph` crossfades A to B over the piece. This is the bridge to the Universal Synth: equation → wavetable → note.
- `p105.sh ports|record OUT.mid|play IN.mid|monitor`: the keyboard.

## 4. The keyboard: Yamaha P-105 (verified 2026-11-20)
- `lsusb`: `Bus 001 Device 006: ID 0499:160f Yamaha Corp. P-105`. ALSA: card `Digital Piano`, rawmidi `hw:1,0,0`, sequencer client 20 port 0. (Card number can change on replug: use `aconnect -l`.)
- Manuals (official, saved in `ContextPlease/claude/references/yamaha_p105/`, ledger row in `INDEX.md`): `p105_en_om_a0.pdf` (Owner's Manual, 28 pp) and `p105_en_mr_a0.pdf` (MIDI Reference, 8 pp, includes the MIDI Implementation Chart). Source: usa.yamaha.com/files/download/other_assets/6/328146/p105_en_om_a0.pdf and …/4/328154/p105_en_mr_a0.pdf.
- Panel chords (MIDI Reference): hold DEMO/SONG, press and hold METRONOME/RHYTHM, then: transmit channel = keys E0 to G#1; receive channel = A#1 to D#3; **Local Control on/off = D6**; **Program Change on/off = D#6**. USB TO HOST needs an AB cable under 3 m (not USB 3.0). It transfers User Song data as SMF and sends/receives MIDI.
- Typical use: `p105.sh record take.mid` to capture a performance as sheet music; with Local Control off, the keyboard becomes a pure controller and the computer's synth sounds (FluidSynth is installed; `timidity` too).

## 5. Directions he has named (not built yet)
Generative composition seeded by the corpus (style model over the NES subset: transitions, loop structure); sample manipulation by envelope stretching (JWST-style); a connection to the UniversalSynth wavetables (`render.py` is the first step: next would be equation-driven wavetables per voice and MIDI-to-`.ptorrent` addressing). Register predictions before measuring any style claim; report fits against shuffled controls, as with the catalog compression.

## 6. Pitfalls
- Never trust `~/Music/Video Game Music/Midi/` (zeroed). Verify the `MThd` magic before parsing anything from a copied archive.
- A MIDI file with no tempo event plays at 120 bpm.
- `note on` with velocity 0 is a note off (handled).
- Do not assume channel 10 (index 9) is drums outside General MIDI files.
