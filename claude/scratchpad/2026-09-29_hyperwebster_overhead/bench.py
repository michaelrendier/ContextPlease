#!/usr/bin/env python3
"""
HyperWebster overhead benchmark (2026-09-29) -- what the SHIPPING code actually gives.

Imports the canonical, unmodified indexer by path (same as VAPMIP/benchmarks) and
measures, on real text already in the repo:

  A. address size vs raw size, whole-document and chunked (the "256-bit" question)
  B. the largest string a 256-bit address can hold at the shipped charset (N=97)
  C. minimal-charset per chunk, charset cost included
  D. the 8 x 32-bit "octonion limb" view of a 256-bit address: is it exact?
  E. ordinary compressors on the same chunks (zlib, lzma) as the fair baseline
  F. the wiki's "frequency-sorted charset saves ~5-6 decimal digits at length 8" claim
  G. timing and round-trip exactness

Nothing is tuned. Run: python3 bench.py
"""
import importlib.util, math, os, sys, time, zlib, lzma, collections

ROOT = "/home/rendier/Projects/ThePlace"
HW_PATH = ROOT + "/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py"
spec = importlib.util.spec_from_file_location("hyperwebster_canon", HW_PATH)
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
HyperWebster = mod.HyperWebster

CORPORA = {
    "english_corpus.txt (prose)": ROOT + "/VAPMIP/english_corpus.txt",
    "PROVENANCE.md (prose)":      ROOT + "/Ainulindale/PROVENANCE.md",
    "hyperwebster.py (python)":   HW_PATH,
}
CAP_CHARS = 40000
hw = HyperWebster()
N = hw.N
BITS_PER_CHAR = math.log2(N)


def load(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    kept = "".join(c for c in raw if c in hw._char_index)
    return raw, kept[:CAP_CHARS]


def chunks(text, k):
    return [text[i:i + k] for i in range(0, len(text), k)]


def addr_bits(chunk_list, h):
    """Return (sum of bit_length, sum of fixed-width bits where each is >=256, all round-trip ok, seconds enc, dec)."""
    t0 = time.perf_counter(); addrs = [h.point_to_text(c) for c in chunk_list]; te = time.perf_counter() - t0
    t0 = time.perf_counter(); back = [h.regenerate_text(a) for a in addrs]; td = time.perf_counter() - t0
    ok = back == chunk_list
    var = sum(max(1, a.bit_length()) for a in addrs)
    fixed = sum(max(256, a.bit_length()) for a in addrs)
    return var, fixed, ok, te, td, addrs


def main():
    print("HyperWebster overhead benchmark  |  %s  |  Python %s" % (time.strftime("%Y-%m-%d"), sys.version.split()[0]))
    print("charset N = %d  ->  %.3f bits/char  (raw = 8 bits/char)\n" % (N, BITS_PER_CHAR))

    # B. capacity of a 256-bit address
    cap = math.floor(256 / BITS_PER_CHAR)
    worst_ok = (N ** cap) <= 2 ** 256
    print("B. capacity: a 256-bit address holds strings up to %d chars at N=%d  (N^%d <= 2^256: %s; N^%d <= 2^256: %s)\n"
          % (cap, N, cap, worst_ok, cap + 1, N ** (cap + 1) <= 2 ** 256))

    for name, path in CORPORA.items():
        if not os.path.exists(path):
            print("SKIP", name); continue
        raw, text = load(path)
        dropped = len(raw) - len("".join(c for c in raw if c in hw._char_index))
        print("=" * 100)
        print("%s   kept %d chars (cap %d); %d chars outside the 97-symbol set dropped from the whole file"
              % (name, len(text), CAP_CHARS, dropped))
        raw_bits = 8 * len(text.encode("utf-8"))
        distinct = sorted(set(text))
        cnt = collections.Counter(text)
        H0 = -sum(c / len(text) * math.log2(c / len(text)) for c in cnt.values())
        print("   raw %d bits | order-0 entropy %.3f bits/char (=%d bits) | distinct symbols %d"
              % (raw_bits, H0, int(H0 * len(text)), len(distinct)))
        print("   %-8s %-10s %-10s %-10s %-9s %-9s %-9s %-8s %-8s %-6s"
              % ("chunk", "addr_var", "addr_256+", "min-cset", "zlib", "lzma", "var/raw", "fix/raw", "enc_ms", "ok"))
        for k in (32, 38, 64, 128, 256, 500, 1000, 4000):
            cl = chunks(text, k)
            var, fixed, ok, te, td, addrs = addr_bits(cl, hw)
            # minimal charset per chunk: address over only the chunk's own symbols (+ cost of listing them, 8 bits each)
            mb = 0; ok2 = True
            for c in cl:
                cs = "".join(sorted(set(c)))
                h2 = HyperWebster(cs); a = h2.point_to_text(c)
                ok2 &= (h2.regenerate_text(a) == c)
                mb += max(1, a.bit_length()) + 8 * len(cs)
            zb = sum(8 * len(zlib.compress(c.encode(), 9)) for c in cl)
            lb = sum(8 * len(lzma.compress(c.encode())) for c in cl)
            print("   %-8d %-10d %-10d %-10d %-9d %-9d %-9.3f %-8.3f %-8.1f %-6s"
                  % (k, var, fixed, mb, zb, lb, var / raw_bits, fixed / raw_bits, te * 1e3, ok and ok2))
        # whole document as ONE address (capped at 4000 chars; encode cost is super-linear)
        one = text[:4000]
        a = hw.point_to_text(one)
        print("   whole 4000-char doc as one address: %d bits (raw %d) -> %.3f of raw"
              % (a.bit_length(), 8 * len(one.encode()), a.bit_length() / (8 * len(one.encode()))))

        # D. 8 x 32-bit octonion limbs of a 256-bit chunk address
        c38 = text[:cap]
        a38 = hw.point_to_text(c38)
        limbs = [(a38 >> (32 * i)) & 0xFFFFFFFF for i in range(8)]
        back = sum(l << (32 * i) for i, l in enumerate(limbs))
        print("   D. 38-char chunk -> address %d bits -> 8 limbs x 32 bits -> recombine exact: %s ; text round-trip: %s"
              % (a38.bit_length(), back == a38, hw.regenerate_text(back) == c38))

    # F. the wiki's frequency-sorted-charset claim at length 8
    print("=" * 100)
    _, prose = load(CORPORA["english_corpus.txt (prose)"])
    words = [w for w in "".join(c if c.isalpha() or c == " " else " " for c in prose.lower()).split() if len(w) == 8]
    words = words[:2000]
    if words:
        keyb = HyperWebster()
        letters = collections.Counter(prose)
        freq_full = "".join(c for c, _ in letters.most_common()) + "".join(c for c in hw.characters if c not in letters)
        hf = HyperWebster(freq_full)
        freq_min = "".join(c for c, _ in collections.Counter("".join(words)).most_common())
        hm = HyperWebster(freq_min)
        def avg_digits(h): return sum(len(str(h.point_to_text(w))) for w in words) / len(words)
        print("F. %d distinct-position 8-letter words: mean decimal digits of the address" % len(words))
        print("   keyboard-order N=%d: %.2f | frequency-sorted N=%d: %.2f | frequency-sorted letters-only N=%d: %.2f"
              % (keyb.N, avg_digits(keyb), hf.N, avg_digits(hf), hm.N, avg_digits(hm)))
        print("   wiki claim: frequency sorting saves ~5-6 digits at length 8 (compare col 1 vs col 2, and vs col 3)")


if __name__ == "__main__":
    main()
