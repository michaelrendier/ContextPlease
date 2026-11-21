"""render.py: render a MIDI file with a single-cycle WAVETABLE (UniversalSynth/wavetables/*.wav, e.g. hermite_psi0..7, zeta_partials) to a 16-bit mono WAV. numpy + stdlib wave.
usage: python render.py IN.mid OUT.wav [WAVETABLE.wav] [--sr 44100] [--morph B.wav]  (--morph crossfades table A -> B over the piece: the wavetable-morph picture of UniversalSynth)
Envelope per note: 5 ms attack, exponential decay to 35% of velocity-scaled level while held, 40 ms release. Pitch = 440 * 2^((key-69)/12)."""
import sys, os, wave, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import smf
def load(p):
    w = wave.open(p); x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(float); x = x.reshape(-1, w.getnchannels())[:, 0]; x -= x.mean(); return x / (np.abs(x).max() or 1)
def main(a):
    src, dst = a[0], a[1]; sr = int(a[a.index("--sr") + 1]) if "--sr" in a else 44100
    tabs = [x for x in a[2:] if x.endswith(".wav") and x != dst]; wtA = load(tabs[0]) if tabs else np.sin(np.linspace(0, 2 * np.pi, 2048, endpoint=False)); wtB = load(tabs[1]) if len(tabs) > 1 and "--morph" in a else None
    m = smf.read(src); tm = smf.tempo_map(m); ns = smf.notes(m); end = max(smf.seconds(m, n["t1"], tm) for n in ns) + 0.5; out = np.zeros(int(end * sr) + 1)
    for n in ns:
        t0, t1 = smf.seconds(m, n["t0"], tm), smf.seconds(m, n["t1"], tm); d = max(t1 - t0, 0.03); L = int((d + 0.04) * sr); t = np.arange(L) / sr
        f = 440 * 2 ** ((n["key"] - 69) / 12); ph = (t * f) % 1.0; idx = ph * len(wtA); s = np.interp(idx, np.arange(len(wtA) + 1), np.append(wtA, wtA[0]))
        if wtB is not None: mix = min(1, t0 / end); s = (1 - mix) * s + mix * np.interp(ph * len(wtB), np.arange(len(wtB) + 1), np.append(wtB, wtB[0]))
        env = np.minimum(t / 0.005, 1) * (0.35 + 0.65 * np.exp(-t / max(d, .05) * 2)); env[t > d] *= np.maximum(0, 1 - (t[t > d] - d) / 0.04)
        i = int(t0 * sr); out[i:i + L] += s * env * (n["vel"] / 127) * 0.2
    out /= max(1.0, np.abs(out).max()); w = wave.open(dst, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((out * 32767).astype("<i2").tobytes()); w.close(); print(f"{len(ns)} notes, {end:.1f} s -> {dst}")
if __name__ == "__main__": main(sys.argv[1:])
