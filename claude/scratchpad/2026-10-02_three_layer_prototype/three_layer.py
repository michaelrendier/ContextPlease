"""Scratch prototype (not the engine): three append-only JSON-Lines layers over Dante's Inferno (Longfellow, PG #1001).
 L1 ROWS.jsonl    one line per ingested canto: {a: hex address of the canto text, n: length, t: timestamp}
 L2 TABLES.jsonl  one line per ingest: {c: category, a: label of ROWS prefix, n: ROWS length, t}   (label = SHA-256 of the prefix bytes)
 L3 TOP.jsonl     one line per ingest: {a: 8 x uint32 octonion label of TABLES prefix, n: TABLES length, t}
Top changes once per ingest. Measures what the exact-address alternative would cost at L2/L3."""
import re, json, hashlib, time, math, os, tempfile, sys
SRC = "/home/rendier/Projects/ThePlace/FourthAgePapers/HyperindexingSystem/corpus/pg1001.txt"
t = open(SRC, encoding="utf-8").read()
body = t[t.index("\n", t.index("*** START OF THE PROJECT GUTENBERG EBOOK")) + 1: t.index("*** END OF THE PROJECT GUTENBERG EBOOK")]
heads = list(re.finditer(r"^Inferno: Canto ([IVXL]+)\s*$", body, re.M)); ends = [m.start() for m in heads[1:]] + [len(body)]
cantos = [(m.group(1), body[m.end():e].strip("\n")) for m, e in zip(heads, ends)]
contents = {m.group(1): m.group(0) for m in re.finditer(r"^Canto ([IVXL]+)\..*$", body[:heads[0].start()], re.M)}
ORD = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth"]
cat, circle = {}, "Prologue"
for num, _ in cantos:
    m = re.search(r"(%s) Circle" % "|".join(ORD), contents.get(num, ""))
    if m: circle = m.group(1) + " Circle"
    cat[num] = circle
alphabet = "".join(sorted(set("".join(c for _, c in cantos) )))                      # the corpus's own 68 symbols, in codepoint order (a reduced set)
N = len(alphabet); idx = {c: i for i, c in enumerate(alphabet)}
def address(s):                       # forward Horner, bijective base-N (the engine's Listing 1, forward form)
    a = 0
    for ch in s: a = a * N + idx[ch] + 1
    return a - 1
def text_at(a):
    out = []; a += 1
    while a > 0: a, r = divmod(a - 1, N); out.append(alphabet[r])
    return "".join(reversed(out))
def octonion_label(data: bytes):       # SHA-256 split into 8 x uint32 = an octonion-shaped 256-bit label
    h = hashlib.sha256(data).digest(); return [int.from_bytes(h[i:i + 4], "big") for i in range(0, 32, 4)]
d = tempfile.mkdtemp(); P = {k: os.path.join(d, k + ".jsonl") for k in ("ROWS", "TABLES", "TOP")}
for p in P.values(): open(p, "wb").close()
def append(path, obj): 
    line = (json.dumps(obj, separators=(",", ":"), sort_keys=True) + "\n").encode(); 
    with open(path, "ab") as f: f.write(line)
    return len(line)
print("alphabet N =", N, "| cantos:", len(cantos), "| categories:", sorted(set(cat.values())))
tops, rows_len_hist, tables_len_hist = [], [], []
rows_addr = 0; rows_text_len = 0                      # exact address of the ROWS file as it grows (incremental shift-add) -- for the cost comparison only
ROWCH = "".join(sorted(set('{}":,.0123456789abcdefnat\n')))
t_all = time.perf_counter()
for i, (num, text) in enumerate(cantos):
    ts = "2026-10-%02dT00:00:00Z" % (2 + i) if i < 29 else "2026-11-%02dT00:00:00Z" % (i - 28)
    a = address(text); assert text_at(a) == text
    append(P["ROWS"], {"a": "%x" % a, "n": len(text), "t": ts})
    rows_bytes = open(P["ROWS"], "rb").read(); rows_len_hist.append(len(rows_bytes))
    append(P["TABLES"], {"a": octonion_label(rows_bytes), "c": cat[num], "n": len(rows_bytes), "t": ts})
    tab_bytes = open(P["TABLES"], "rb").read(); tables_len_hist.append(len(tab_bytes))
    top = {"a": octonion_label(tab_bytes), "n": len(tab_bytes), "t": ts}; tops.append(top["a"]); append(P["TOP"], top)
dt = time.perf_counter() - t_all
sz = {k: os.path.getsize(v) for k, v in P.items()}; corpus_chars = sum(len(c) for _, c in cantos)
print("ingest of all %d cantos: %.1f s | file sizes: %s | corpus %d chars" % (len(cantos), dt, sz, corpus_chars))
print("top label changes at every ingest (34 distinct):", len(set(map(tuple, tops))) == len(tops), "| last top:", ["%08x" % x for x in tops[-1]])
# reconstruct: from the files alone
rows = [json.loads(l) for l in open(P["ROWS"], "rb")]
ok = all(text_at(int(r["a"], 16)) == c for r, (_, c) in zip(rows, cantos)); print("every canto reconstructs from ROWS.jsonl alone:", ok)
# verify a PAST state through the layers: take ingest 10's top, check the prefix chain
k = 9; tl = [json.loads(l) for l in open(P["TOP"], "rb")]; tabs = [json.loads(l) for l in open(P["TABLES"], "rb")]
prefix_tab = open(P["TABLES"], "rb").read()[:tl[k]["n"]]; print("past top #%d matches the label of the TABLES prefix of its recorded length:" % (k + 1), octonion_label(prefix_tab) == tl[k]["a"])
prefix_rows = open(P["ROWS"], "rb").read()[:tabs[k]["n"]]; print("   TABLES line #%d matches the label of the ROWS prefix:" % (k + 1), octonion_label(prefix_rows) == tabs[k]["a"])
print("   rows recoverable at that past state:", len([l for l in prefix_rows.split(b"\n") if l]), "of", k + 1)
# cost of making L2/L3 EXACT addresses instead of labels (character set restricted to what the JSON lines use)
for name, path in (("ROWS", P["ROWS"]), ("TABLES", P["TABLES"])):
    s = open(path, encoding="utf-8").read(); n_ = len(set(s)); bits = len(s) * math.log2(n_)
    print("exact address of %-6s file: %d chars over %d symbols = %.0f kbit (%.2f x its bytes)" % (name, len(s), n_, bits / 1000, bits / 8 / len(s.encode())))
print("ROWS file vs corpus: %d bytes vs %d chars = %.2f x (hex text of exact addresses)" % (sz["ROWS"], corpus_chars, sz["ROWS"] / corpus_chars))
print("exact corpus address at N=%d: %.0f kbit = %.2f x corpus bytes" % (N, corpus_chars * math.log2(N) / 1000, corpus_chars * math.log2(N) / 8 / corpus_chars))
print("TOP line:", open(P["TOP"], "rb").read().splitlines()[-1].decode())
