"""survey.py: index a MIDI directory (default: the author's NES/video-game corpus) into corpus_index.csv and print corpus statistics.
Columns: file, fmt, ppq, tracks, seconds, tempo_bpm, voices_max (max simultaneous notes), voices_p95, channels, drums(ch10 notes), lo, hi (key range), notes, programs.
usage: python3 survey.py [DIR] [OUT.csv]    (stdlib only)"""
import os, sys, csv, statistics, bisect
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import smf
D = sys.argv[1] if len(sys.argv) > 1 else "/home/rendier/Desktop/Desktop Archive/thisonemine/Music/Video Game Music"   # the INTACT copy; ~/Music/Video Game Music/Midi is zero-filled (checked 2026-11-20)
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "corpus_index.csv")
def poly(ns):
    ev = sorted([(n["t0"], 1) for n in ns] + [(n["t1"], -1) for n in ns], key=lambda x: (x[0], x[1])); c = 0; mx = 0; hist = {}; last = None
    for t, d in ev:
        if last is not None and t > last: hist[c] = hist.get(c, 0) + (t - last)
        c += d; mx = max(mx, c); last = t
    tot = sum(v for k, v in hist.items() if k > 0) or 1; acc = 0; p95 = 0
    for k in sorted(hist):
        if k == 0: continue
        acc += hist[k]; p95 = k
        if acc / tot >= .95: break
    return mx, p95
rows = []; bad = []
for root, _, fs in os.walk(D):
    for f in sorted(fs):
        if not f.lower().endswith((".mid", ".midi")): continue
        if open(os.path.join(root, f), "rb").read(4) != b"MThd": bad.append((os.path.join(root, f), "no MThd header (zero-filled?)")); continue
        p = os.path.join(root, f)
        try:
            m = smf.read(p); ns = smf.notes(m)
            if not ns: bad.append((p, "no notes")); continue
            tm = smf.tempo_map(m); dur = smf.seconds(m, max(n["t1"] for n in ns), tm); vm, v95 = poly(ns)
            progs = sorted({e["a"] for evs in m["tracks"] for e in evs if e["kind"] == "pc"})
            rows.append(dict(file=os.path.relpath(p, D), fmt=m["fmt"], ppq=m["ppq"], tracks=len(m["tracks"]), seconds=round(dur, 1), tempo_bpm=round(6e7 / tm[0][1], 1), voices_max=vm, voices_p95=v95,
                             channels=len({n["ch"] for n in ns}), drums=sum(n["ch"] == 9 for n in ns), lo=min(n["key"] for n in ns), hi=max(n["key"] for n in ns), notes=len(ns), programs=" ".join(map(str, progs))))
        except Exception as e: bad.append((p, repr(e)[:60]))
with open(OUT, "w", newline="") as fh: w = csv.DictWriter(fh, list(rows[0])); w.writeheader(); w.writerows(rows)
q = lambda k, f=statistics.median: f([r[k] for r in rows])
print(f"{len(rows)} files indexed, {len(bad)} unreadable/empty; median length {q('seconds')} s, median tempo {q('tempo_bpm')} bpm, median notes {q('notes')}")
print("p95 simultaneous voices:", {k: sum(r['voices_p95'] <= k for r in rows) for k in (3, 4, 5, 6, 8)}, "(files with p95 <= k)")
print("key range: median lo", q('lo'), "hi", q('hi'), "; channels median", q('channels'), "; files with channel-10 drums:", sum(r['drums'] > 0 for r in rows))
for p, e in bad[:5]: print("  skipped", os.path.basename(p), e)
