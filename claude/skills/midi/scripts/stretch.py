"""stretch.py: astronomy-style stretches applied to MIDI (the JWST image stretch idea: map an envelope through asinh/log/sqrt/gamma to bring out faint structure).
  vel   velocity envelope:  v' = 127 * f(v/127),  f in asinh(a) | log(a) | sqrt | gamma(a)       (a = softening; bigger a lifts quiet notes more)
  warp  time envelope:      t' = T * asinh(a t/T) / asinh(a)   (slow start, compressed end; a > 0), or  --inv  to reverse it
  time  uniform duration stretch by factor F (tempo meta events scaled too, so the notes keep their pitch and the piece just takes F times longer)
usage: python3 stretch.py IN.mid OUT.mid vel asinh 8 | vel gamma 0.6 | vel sqrt | warp 5 [--inv] | time 2.0"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import smf
def f_vel(mode, a):
    return {"asinh": lambda x: math.asinh(a * x) / math.asinh(a), "log": lambda x: math.log1p(a * x) / math.log1p(a), "sqrt": lambda x: math.sqrt(x), "gamma": lambda x: x ** a}[mode]
def main(argv):
    src, dst, op = argv[0], argv[1], argv[2]; m = smf.read(src); T = max((e["t"] for evs in m["tracks"] for e in evs), default=1) or 1
    if op == "vel":
        f = f_vel(argv[3], float(argv[4]) if len(argv) > 4 else 1.0)
        for evs in m["tracks"]:
            for e in evs:
                if e["kind"] == "on": e["b"] = max(1, min(127, round(127 * f(e["b"] / 127))))
    elif op == "warp":
        a = float(argv[3]); inv = "--inv" in argv; g = (lambda t: T * math.asinh(a * t / T) / math.asinh(a)) if not inv else (lambda t: T * (1 - math.asinh(a * (T - t) / T) / math.asinh(a)))
        for evs in m["tracks"]:
            for e in evs: e["t"] = round(g(e["t"]))
    elif op == "time":
        F = float(argv[3])
        for evs in m["tracks"]:
            for e in evs:
                e["t"] = round(e["t"] * F)
                if e["kind"] == "meta" and e["a"] == 0x51 and len(e["data"]) == 3: e["data"] = int(int.from_bytes(e["data"], "big")).to_bytes(3, "big")   # tick scaling already slows it; tempo untouched
    else: raise SystemExit(__doc__)
    smf.write(dst, m["fmt"], m["ppq"], m["tracks"]); n = len(smf.notes(smf.read(dst))); print(f"{op}: {n} notes written to {dst}")
if __name__ == "__main__": main(sys.argv[1:])
