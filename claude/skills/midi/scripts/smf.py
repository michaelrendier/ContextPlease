"""smf.py: stdlib Standard MIDI File reader/writer for the midi skill (no dependencies).
read(path) -> dict(fmt, ppq, tracks=[[ev,...]]) ; ev = dict(t=abs ticks, kind, ch, a, b, data)  kind: on off cc pc bend pressure meta sysex
notes(mid)  -> list of dict(t0, t1, ch, key, vel, track) sorted by t0 (note-on with vel 0 = off; unmatched ons closed at the track end)
tempo_map(mid) -> [(tick, microsec_per_quarter)] ; seconds(mid, tick) converts using the map
write(path, fmt, ppq, tracks) writes events back (same ev dicts; sorted by t; meta end-of-track added)"""
import struct, bisect
def _vlq(b, i):
    v = 0
    while True:
        c = b[i]; i += 1; v = (v << 7) | (c & 0x7F)
        if not c & 0x80: return v, i
def read(path):
    b = open(path, "rb").read(); i = b.index(b"MThd"); fmt, n, ppq = struct.unpack(">HHH", b[i + 8:i + 14]); i += 8 + struct.unpack(">I", b[i + 4:i + 8])[0]
    tracks = []
    while i < len(b) and len(tracks) < n:
        if b[i:i + 4] != b"MTrk":
            i += 1; continue
        ln = struct.unpack(">I", b[i + 4:i + 8])[0]; j = i + 8; end = min(j + ln, len(b)); t = 0; run = None; evs = []
        try:
            while j < end:
                d, j = _vlq(b, j); t += d; s = b[j]
                if s == 0xFF:
                    ty = b[j + 1]; l, j = _vlq(b, j + 2); evs.append(dict(t=t, kind="meta", ch=-1, a=ty, b=0, data=bytes(b[j:j + l]))); j += l
                elif s in (0xF0, 0xF7):
                    l, j = _vlq(b, j + 1); evs.append(dict(t=t, kind="sysex", ch=-1, a=0, b=0, data=bytes(b[j:j + l]))); j += l
                else:
                    if s & 0x80: run = s; j += 1
                    st = run; hi, ch = st & 0xF0, st & 15
                    if hi in (0xC0, 0xD0): a, bb = b[j], 0; j += 1
                    else: a, bb = b[j], b[j + 1]; j += 2
                    k = {0x80: "off", 0x90: "on", 0xA0: "pressure", 0xB0: "cc", 0xC0: "pc", 0xD0: "pressure", 0xE0: "bend"}[hi]
                    if k == "on" and bb == 0: k = "off"
                    evs.append(dict(t=t, kind=k, ch=ch, a=a, b=bb, data=b""))
        except (IndexError, KeyError): pass
        tracks.append(evs); i = end
    return dict(fmt=fmt, ppq=ppq, tracks=tracks)
def notes(m):
    out = []
    for ti, evs in enumerate(m["tracks"]):
        open_ = {}
        for e in evs:
            if e["kind"] == "on": open_.setdefault((e["ch"], e["a"]), []).append(e)
            elif e["kind"] == "off":
                st = open_.get((e["ch"], e["a"]))
                if st: o = st.pop(0); out.append(dict(t0=o["t"], t1=e["t"], ch=e["ch"], key=e["a"], vel=o["b"], track=ti))
        last = evs[-1]["t"] if evs else 0
        for (ch, k), st in open_.items():
            for o in st: out.append(dict(t0=o["t"], t1=last, ch=ch, key=k, vel=o["b"], track=ti))
    return sorted(out, key=lambda n: (n["t0"], n["key"]))
def tempo_map(m):
    tm = sorted((e["t"], int.from_bytes(e["data"], "big")) for evs in m["tracks"] for e in evs if e["kind"] == "meta" and e["a"] == 0x51 and len(e["data"]) == 3)
    return tm if tm and tm[0][0] == 0 else [(0, 500000)] + tm
def seconds(m, tick, tm=None):
    tm = tm or tempo_map(m); s = 0.0
    for (t0, us), nxt in zip(tm, tm[1:] + [(10 ** 12, 0)]):
        if tick <= t0: break
        s += (min(tick, nxt[0]) - t0) * us / 1e6 / m["ppq"]
    return s
def _enc_vlq(v):
    o = [v & 0x7F]; v >>= 7
    while v: o.append((v & 0x7F) | 0x80); v >>= 7
    return bytes(reversed(o))
def write(path, fmt, ppq, tracks):
    out = b"MThd" + struct.pack(">IHHH", 6, fmt, len(tracks), ppq)
    for evs in tracks:
        body = b""; t = 0
        for e in sorted(evs, key=lambda e: (e["t"], e["kind"] == "on")):
            body += _enc_vlq(max(0, e["t"] - t)); t = max(t, e["t"]); k = e["kind"]
            if k == "meta": body += bytes([0xFF, e["a"]]) + _enc_vlq(len(e["data"])) + e["data"]
            elif k == "sysex": body += b"\xF0" + _enc_vlq(len(e["data"])) + e["data"]
            else:
                hi = {"off": 0x80, "on": 0x90, "pressure": 0xA0, "cc": 0xB0, "pc": 0xC0, "bend": 0xE0}[k]; body += bytes([hi | e["ch"], e["a"]]) + (b"" if k == "pc" else bytes([e["b"]]))
        if not (evs and evs[-1]["kind"] == "meta" and evs[-1]["a"] == 0x2F): body += b"\x00\xFF\x2F\x00"
        out += b"MTrk" + struct.pack(">I", len(body)) + body
    open(path, "wb").write(out)
