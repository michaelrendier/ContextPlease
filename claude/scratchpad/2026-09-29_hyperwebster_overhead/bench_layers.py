#!/usr/bin/env python3
"""
The layered calendrical hyperindex, built exactly as Cody described it (2026-09-29):

  chunks of ingested text  --hyperindex-->  (address_hex, length, timestamp) entries
  a JSON list of those entries (one 'day')  --hyperindex (in JSON characters)-->  next entry
  a JSON list of day entries (one 'month')  --hyperindex-->  next entry ... up to ONE top pointer

Question measured: how big is the TOP pointer relative to the raw corpus, per layer added?
Uses the shipping hyperwebster.py unmodified. Every layer is rebuilt back down to the text
by date to prove exactness. Nothing tuned.
"""
import importlib.util, json, math, sys, time

ROOT = "/home/rendier/Projects/ThePlace"
HW_PATH = ROOT + "/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py"
spec = importlib.util.spec_from_file_location("hw", HW_PATH)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
hw = m.HyperWebster()


def corpus(n):
    raw = open(ROOT + "/VAPMIP/english_corpus.txt", encoding="utf-8", errors="replace").read()
    return "".join(c for c in raw if c in hw._char_index)[:n]


def index(text):
    """(address_hex, length) via the shipping index_text; timestamp is fixed for repeatability."""
    a, n, _ = hw.index_text(text)
    return a, n


def build(text, chunk, per_day, days_per_month):
    entries = []
    for i in range(0, len(text), chunk):
        a, n = index(text[i:i + chunk]); entries.append({"a": a, "n": n, "t": "day-%d" % (i // chunk)})
    layers = [("chunks", entries)]
    level = entries
    for name, k in (("day", per_day), ("month", days_per_month)):
        nxt = []
        for j in range(0, len(level), k):
            js = json.dumps(level[j:j + k], separators=(",", ":"))
            a, n = index(js)
            nxt.append({"a": a, "n": n, "t": "%s-%d" % (name, j // k), "_json_chars": n})
        layers.append((name, nxt)); level = nxt
    return layers


def restore(layers):
    """Walk the top entries back down to text; return the recovered text."""
    top = layers[-1][1]
    def down(entry, depth):
        s = hw.regenerate_from_address(entry["a"], entry["n"])
        if depth == 0:
            return s
        return "".join(down(e, depth - 1) for e in json.loads(s))
    return "".join(down(e, len(layers) - 1) for e in top)


def main():
    print("layered calendrical hyperindex  |  %s  |  Python %s" % (time.strftime("%Y-%m-%d"), sys.version.split()[0]))
    for total, chunk in ((4000, 200), (8000, 400)):
        text = corpus(total)
        raw_bits = 8 * len(text)
        t0 = time.perf_counter(); layers = build(text, chunk, per_day=4, days_per_month=5); tb = time.perf_counter() - t0
        t0 = time.perf_counter(); back = restore(layers); tr = time.perf_counter() - t0
        print("=" * 96)
        print("corpus %d chars = %d raw bits | chunk %d | 4 chunks/day | 5 days/month | build %.1fs restore %.1fs | exact: %s"
              % (len(text), raw_bits, chunk, tb, tr, back == text))
        print("  %-8s %-8s %-22s %-16s %-14s" % ("layer", "entries", "sum address bits", "= x raw corpus", "chars indexed"))
        for name, ents in layers:
            bits = sum(int(e["a"], 16).bit_length() for e in ents)
            chars = sum(e["n"] for e in ents)
            print("  %-8s %-8d %-22d %-16.3f %-14d" % (name, len(ents), bits, bits / raw_bits, chars))
        top = layers[-1][1]
        tbits = sum(int(e["a"], 16).bit_length() for e in top)
        print("  TOP pointer(s): %d entries, %d address bits total = %.2fx the raw corpus; one 256-bit pointer would need <= 38 chars"
              % (len(top), tbits, tbits / raw_bits))


if __name__ == "__main__":
    main()
