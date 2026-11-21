"""piano_reduction.py: a playable piano reduction (grand staff: treble + bass) of a multi-track MIDI file, written as MusicXML.
Rules (stated on the page): notes are quantised to 16ths; right hand = the melody track (top line) plus the highest harmony note under it at each onset;
left hand = the bass track plus the lowest harmony note at each onset; hands split at middle C only for harmony notes; drums are left out (they are in the full score below).
usage: python piano_reduction.py IN.mid OUT.musicxml MELODY_TRACK BASS_TRACK HARMONY_TRACKS(comma) TITLE
Needs music21 (this directory's .venv)."""
import sys, collections
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import smf
from music21 import stream, note, chord, meter, tempo, key, clef, layout, metadata, instrument, duration

src, dst, mel, bass, harm, title = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), [int(x) for x in sys.argv[5].split(",")], sys.argv[6]
m = smf.read(src); ns = smf.notes(m); tm = smf.tempo_map(m); Q = m["ppq"] // 4      # ticks per 16th
bpm = round(6e7 / tm[0][1])
def grid(tr):
    out = collections.defaultdict(list)
    for n in ns:
        if n["track"] == tr:
            on = round(n["t0"] / Q); d = max(1, round((n["t1"] - n["t0"]) / Q)); out[on].append((n["key"], d))
    return out
M, B = grid(mel), grid(bass); H = [grid(t) for t in harm]
onsets = sorted(set(M) | set(B) | {o for g in H for o in g})
RH, LH = {}, {}
for o in onsets:
    rh, lh = [], []
    if o in M: rh += M[o]
    if o in B: lh += B[o]
    hs = sorted({(k, d) for g in H for (k, d) in g.get(o, [])})
    top = max((p for p in rh), default=None, key=lambda p: p[0])
    cand = [h for h in hs if (top is None or h[0] < top[0] - 2)]
    if cand and rh:
        rh.append(max(cand, key=lambda h: h[0]))
    low = [h for h in hs if h[0] < 66 and h not in rh]
    if low and lh: lh.append(min(low, key=lambda h: h[0]))
    elif hs and not rh and not lh:
        (rh if hs[-1][0] >= 60 else lh).append(hs[-1])
    if rh: RH[o] = rh
    if lh: LH[o] = lh
def build(events, c, name):
    p = stream.PartStaff(); p.insert(0, c); p.partName = name
    keys = sorted(events)
    for i, o in enumerate(keys):
        nxt = keys[i + 1] if i + 1 < len(keys) else o + 16
        d = max(1, min(max(d for _, d in events[o]), nxt - o)); ps = sorted({k for k, _ in events[o]})
        el = note.Note(ps[0]) if len(ps) == 1 else chord.Chord(ps)
        el.duration = duration.Duration(d / 4.0); p.insert(o / 4.0, el)
    return p
rh = build(RH, clef.TrebleClef(), "Right hand"); lh = build(LH, clef.BassClef(), "Left hand")
s = stream.Score(); s.insert(0, metadata.Metadata()); s.metadata.title = title; s.metadata.composer = "Creepy Nuts, octet arr. Kino Geno / piano reduction"
for p in (rh, lh):
    p.insert(0, meter.TimeSignature("4/4"))
rh.insert(0, tempo.MetronomeMark(number=bpm))
s.insert(0, rh); s.insert(0, lh); s.insert(0, layout.StaffGroup([rh, lh], name="Piano", abbreviation="Pno.", symbol="brace", barline=True))
k = s.analyze("key"); 
for p in (rh, lh): p.insert(0, key.KeySignature(k.sharps))
for p in (rh, lh): p.makeNotation(inPlace=True)
s.write("musicxml", fp=dst)
print("key", k, "bpm", bpm, "right-hand onsets", len(RH), "left-hand onsets", len(LH))
