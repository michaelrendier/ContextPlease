#!/usr/bin/env python3
"""
Minimal-charset layering (Cody, 2026-09-29):  same calendrical hyperindex as bench_layers.py, but each layer
is indexed with a layer-wide charset chosen by
   A) frequency order  -- most used characters first (whitespace included)
   B) restriction      -- only the characters that occur in that layer's text
   A+B                 -- both
plus a 'compact' variant (not JSON: hex digits with , and ; separators, numeric labels) to show the floor.
The layer charset is treated as a STANDARDISED, shared object (like a .perm file): its cost is reported both
ways -- free, and listed explicitly at 8 bits per symbol, once per layer.
Shipping hyperwebster.py is used unmodified (its `characters` constructor argument is the charset).
"""
import collections, importlib.util, json, sys, time

ROOT = "/home/rendier/Projects/ThePlace"
HW_PATH = ROOT + "/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py"
spec = importlib.util.spec_from_file_location("hw", HW_PATH)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
HyperWebster = m.HyperWebster
DEFAULT = HyperWebster()          # the shipped 97-symbol keyboard-order charset


def corpus(n):
    raw = open(ROOT + "/VAPMIP/english_corpus.txt", encoding="utf-8", errors="replace").read()
    return "".join(c for c in raw if c in DEFAULT._char_index)[:n]


def charset_for(mode, texts):
    joined = "".join(texts)
    cnt = collections.Counter(joined)
    if mode == "M0 shipped 97":
        return DEFAULT.characters
    if mode == "A freq-ordered 97":
        rest = [c for c in DEFAULT.characters if c not in cnt]
        return "".join(c for c, _ in cnt.most_common()) + "".join(rest)
    if mode == "B restricted":
        return "".join(sorted(cnt, key=ord))
    return "".join(c for c, _ in cnt.most_common())      # A+B  (also used by 'compact')


def chunk_texts(text, chunk):
    return [text[i:i + chunk] for i in range(0, len(text), chunk)]


def build(text, chunk, mode, compact):
    """Return per-layer records: charset, list of texts indexed, list of (int address, length)."""
    layers = []
    texts = chunk_texts(text, chunk)
    depth_sizes = (4, 5)                                  # 4 chunks/day, 5 days/month
    for lvl in range(3):                                  # chunks, day, month
        cs = charset_for(mode, texts)
        h = HyperWebster(cs)
        ents = [(h.point_to_text(t), len(t)) for t in texts]
        layers.append({"cs": cs, "texts": texts, "ents": ents})
        if lvl == 2:
            break
        k = depth_sizes[lvl]
        nxt = []
        for j in range(0, len(ents), k):
            grp = ents[j:j + k]
            if compact:
                nxt.append(";".join("%x,%d,%d" % (a, n, j + i) for i, (a, n) in enumerate(grp)))
            else:
                nxt.append(json.dumps([{"a": "%x" % a, "n": n, "t": "L%d-%d" % (lvl, j + i)} for i, (a, n) in enumerate(grp)],
                                      separators=(",", ":")))
        texts = nxt
    return layers


def restore(layers, compact):
    def parse(s):
        if compact:
            return [(int(a, 16), int(n)) for a, n, _ in (e.split(",") for e in s.split(";"))]
        return [(int(d["a"], 16), d["n"]) for d in json.loads(s)]

    def down(addr_len, lvl):
        a, n = addr_len
        h = HyperWebster(layers[lvl]["cs"])
        s = h.regenerate_text(a)
        assert len(s) == n
        return s if lvl == 0 else "".join(down(e, lvl - 1) for e in parse(s))
    return "".join(down(e, 2) for e in layers[2]["ents"])


def main():
    print("minimal-charset layering  |  %s  |  Python %s" % (time.strftime("%Y-%m-%d"), sys.version.split()[0]))
    for total, chunk in ((4000, 200), (8000, 400)):
        text = corpus(total); raw = 8 * len(text)
        print("=" * 108)
        print("corpus %d chars = %d raw bits | chunk %d | 4 chunks/day | 5 days/month" % (len(text), raw, chunk))
        print("  %-20s %-9s | %-30s | %-9s %-9s %-9s | %-11s %-8s" % (
            "mode", "|charset|", "address bits x raw: chunk/day/month", "top ptr", "+cs list", "growth", "exact", "secs"))
        for mode, compact in (("M0 shipped 97", False), ("A freq-ordered 97", False), ("B restricted", False),
                              ("A+B restricted+freq", False), ("A+B compact (hex,;)", True)):
            t0 = time.perf_counter()
            L = build(text, chunk, mode if mode != "A+B compact (hex,;)" else "A+B", compact)
            ok = restore(L, compact) == text
            tsec = time.perf_counter() - t0
            bits = [sum(a.bit_length() for a, _ in l["ents"]) for l in L]
            cslist = sum(8 * len(l["cs"]) for l in L) if mode != "M0 shipped 97" else 0
            ns = [len(l["cs"]) for l in L]
            growth = (bits[2] / bits[0]) ** 0.5             # per-layer inflation (two steps up)
            print("  %-20s %-9s | %.3f / %.3f / %.3f            | %-9.3f %-9.3f %-9.3f | %-11s %-8.1f" % (
                mode, "/".join(map(str, ns)), bits[0] / raw, bits[1] / raw, bits[2] / raw,
                bits[2] / raw, (bits[2] + cslist) / raw, growth, ok, tsec))


if __name__ == "__main__":
    main()
