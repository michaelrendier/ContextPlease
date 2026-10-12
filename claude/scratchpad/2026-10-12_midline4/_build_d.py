from _nb import md, code, write
import re

# ---------------------------------------------------------------- v13 e17
write("v13_tn_signature/01_firing_signature.ipynb", "# v13 · Hyperindexing in T_N: the *firing signature*, an argsort permutation as the address\n`VAPMIP/engines/e17_hyperindexing.py` (git 2026-06-14). A text is projected onto n prime-indexed dimensions; the address is the permutation that sorts the dimensions by |value|.", [
code('''import sys
sys.path.insert(0, os.path.join(PROJ, "VAPMIP", "engines"))
e17 = load("VAPMIP/engines/e17_hyperindexing.py", "e17")
sd = sys.modules["_sedenion"]
for w in ["listen", "silent", "hello"]:
    v, raw = e17.geometry_n(w, 8)
    print("%-7s firing_sig(8) = %s" % (w, e17.firing_sig_n(w, 8)))'''),
md("## The file's own experiment, run as written"),
code('''t0 = time.perf_counter(); res = e17.run(); dt = time.perf_counter() - t0
for n in (8, 16, 32, 64, 128):
    r = res["n=%d" % n]; print("n=%-4d collision_rate=%.6f  mean_pair_dist=%.4f  injective=%s" % (n, r["collision_rate"], r["mean_pairwise_dist"], r["effectively_injective"]))
print("crossover:", res["crossover"]["interpretation"], "| corpus size:", len(e17.CORPUS), "sentences | %.1f s" % dt)'''),
md("The corpus is ten sentences: 45 pairs. Zero collisions among 45 pairs says little about injectivity. Below: an exhaustive test."),
])
write("v13_tn_signature/02_exhaustive_injectivity.ipynb", "# v13 · Is the firing signature injective? Exhaustive over every lowercase word of length ≤ 3", [
code('''import sys, string
from itertools import product
sys.path.insert(0, os.path.join(PROJ, "VAPMIP", "engines"))
e17 = load("VAPMIP/engines/e17_hyperindexing.py", "e17")
words = ["".join(p) for n in (1, 2, 3) for p in product(string.ascii_lowercase, repeat=n)]
print(len(words), "words")
for n in (4, 8, 16, 32):
    prim = e17.primes_up_to_n(n)
    sigs = Counter()
    for w in words:
        raw = [e17.project(w, k, prim) for k in range(n)]
        norm = math.sqrt(sum(x*x for x in raw))
        v = [x / norm for x in raw]
        sigs[tuple(sorted(range(n), key=lambda k: abs(v[k])))] += 1
    print("n=%-3d distinct signatures: %6d of %d words | largest class: %d | n! = %s" % (n, len(sigs), len(words), max(sigs.values()), math.factorial(n) if n <= 16 else "%.2e" % math.factorial(n)))'''),
md("## Longer texts do separate\nThe file's experiment used sentences of 23 to 44 characters. The same test on random 25-character strings:"),
code('''import random
rnd = random.Random(5)
long_words = ["".join(rnd.choice(string.ascii_lowercase + " ") for _ in range(25)) for _ in range(2000)]
for n in (8, 16, 32):
    prim = e17.primes_up_to_n(n)
    sg = set()
    for w in long_words:
        raw = [e17.project(w, k, prim) for k in range(n)]
        nm = math.sqrt(sum(x*x for x in raw)); v = [x / nm for x in raw]
        sg.add(tuple(sorted(range(n), key=lambda k: abs(v[k]))))
    print("n=%-3d distinct signatures among 2000 random 25-char strings: %d" % (n, len(sg)))'''),
md("The number of possible signatures is n!, far above 18,278 from n = 8 on, so injectivity is not blocked by counting. What limits it is the projection: the value in dimension k is a real sum and the signature keeps only the order of magnitudes. On words of length ≤ 3 the signature takes 7–8 values in total at every n from 4 to 32, so it is far from injective there; on 25-character strings (the cell above) it separates much more. The file's 'effectively injective at N = 8' is a statement about ten long sentences, not about the map."),
])

# ---------------------------------------------------------------- v14 ValaQuenta
write("v14_valaquenta_module/01_horner_fano_semanticword.ipynb", "# v14 · ValaQuenta `hyperwebster`: Horner index + Fano path + `SemanticWord`\n`ValaQuenta/modules/hyperwebster/maths.py` (git 2026-06-28). The same construction as v00 (`a–z A–Z 0–9…` order, base-97 mixed radix, `char_index % 7` Fano path), packaged as a module.", [
code('''vq = load("ValaQuenta/modules/hyperwebster/maths.py", "vq")
w = vq.SemanticWord("hello")
print(w.horner_idx, w.fano_idx, w.length, w.verify())
assert vq.horner_decode(vq.horner_encode("Hello, World!"), 13) == "Hello, World!"'''),
md("## Not a bijection over strings: the length is part of the address\nSymbol 0 is `a`; `a`, `aa`, `aaa` all have index 0."),
code('''print({k: vq.horner_encode("a"*k) for k in (1, 2, 3)})
assert vq.horner_encode("a") == vq.horner_encode("aaa") == 0'''),
md("## An unknown character silently becomes symbol 0"),
code('''print("é ->", vq.char_to_idx("é"), "| horner_encode('é') == horner_encode('a'):", vq.horner_encode("é") == vq.horner_encode("a"))
assert vq.horner_encode("é") == vq.horner_encode("a")
# v02 (bijective, shipped) rejects it instead
hw = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "hw").HyperWebster()
try: hw.point_to_text("é")
except ValueError as e: print("v02:", e)'''),
md("## The Fano index: seven classes"),
code('''import re
words = sorted(set(re.findall(r"[a-z]+", CORPUS.lower())))
fano = Counter(vq.fano_encode(w) for w in words)
print(len(words), "distinct words ->", len(fano), "distinct Fano indices | largest class:", max(fano.values()))
sw = [vq.SemanticWord("listen"), vq.SemanticWord("silent")]
print("anagrams: horner differ:", sw[0].horner_idx != sw[1].horner_idx, "| fano differ:", sw[0].fano_idx != sw[1].fano_idx)'''),
md("The Fano index keeps the sequence of `index mod 7` values, so it distinguishes anagrams (order is kept) but merges symbols that are congruent mod 7. The Horner index is exact once the length is stored and the text stays inside the 97 symbols."),
])

# ---------------------------------------------------------------- v15 Vigenere model
VIG = '''import sys
sys.path.insert(0, os.path.join(PROJ, "PtolemyDesktop"))
vg = load("PtolemyDesktop/Kryptos/Ciphers/Vigenere.py", "vg")
an = load("PtolemyDesktop/Kryptos/analysis.py", "an")'''
write("v15_vigenere_model/01_tabula_recta.ipynb", "# v15 · The reference model: Vigenère\n`PtolemyDesktop/Kryptos/Ciphers/Vigenere.py` (git 2026-08-25). One ciphertext letter as `(w | line, position, charset)`; the tabula recta as the 26 rotations of one cycle.", [
code(VIG),
md("## The textbook example and the `(w, i, j, k)` view"),
code('''ct = vg.encrypt("ATTACKATDAWN", "LEMON")
print(ct); assert ct == "LXFOPVEFRNHR" and vg.decrypt(ct, "LEMON") == "ATTACKATDAWN"
for q in vg.quaternion_trace("ATTACKATDAWN", "LEMON")[:6]: print(q)'''),
md("## The tabula recta is the cyclic group Z₂₆ acting on the alphabet\nEach row is a permutation (a rotation); composing two rows is the row of the sum; so the 26 rows are a group of order 26. Checked exhaustively."),
code('''A = vg.ALPHABET
rows = {k: tuple((i + k) % 26 for i in range(26)) for k in range(26)}
assert all(sorted(r) == list(range(26)) for r in rows.values())
compose = lambda p, q: tuple(p[q[i]] for i in range(26))
assert all(compose(rows[a], rows[b]) == rows[(a + b) % 26] for a in range(26) for b in range(26))
print("26 rows: all permutations; row(a)∘row(b) = row(a+b) for all 676 pairs")
# as complex multiplication on the 26th roots of unity
import cmath
w = [cmath.exp(2j * cmath.pi * i / 26) for i in range(26)]
k = 5
assert all(abs(w[i] * cmath.exp(2j * cmath.pi * k / 26) - w[(i + k) % 26]) < 1e-12 for i in range(26))
print("a Caesar shift by 5 = multiplication by e^(2πi·5/26) on the 26th roots of unity")'''),
])
write("v15_vigenere_model/02_breaking_it.ipynb", "# v15 · Breaking it: Kasiski, index of coincidence, per-column Caesar solve\n`PtolemyDesktop/Kryptos/analysis.py`. The same tools attack the PRIVATE-charset construction (v10).", [
code(VIG),
md("## Vigenère on the corpus letters"),
code('''plain = an.clean(CORPUS)
print("plaintext letters:", len(plain), "| IoC:", round(an.index_of_coincidence(plain), 4))
for key in ["LEMON", "HYPERINDEX"]:
    ct = vg.encrypt(plain, key)
    res = an.break_vigenere(ct)
    print("key %-11s -> ciphertext IoC %.4f | recovered period %d, key %s, plaintext exact: %s" % (key, an.index_of_coincidence(ct), res["period"], res["key"], res["plaintext"] == plain))'''),
md("## When the key length has small factors, the breaker's period vote picks the wrong one\nFor `HYPERINDEX` (length 10) the recovered period is 2: every gap between repeated trigrams is a multiple of 10, hence also of 2, and `break_vigenere` takes the top-voted factor. Given the true period the per-column solve is exact."),
code('''ct = vg.encrypt(plain, "HYPERINDEX")
votes, _ = an.kasiski(ct)
print("Kasiski votes (factor, votes):", votes[:6])
print("key from true period 10:", an.vigenere_key_from_period(ct, 10))
assert an.vigenere_key_from_period(ct, 10) == "HYPERINDEX"'''),
md("## The PRIVATE charset (v10) is a monoalphabetic substitution on the address digits\nA private address is the public address of the substituted text. A reader who knows only the base reads the substituted text off the integer. Substitution preserves the *repeat pattern* of every word — the key of al-Kindi's pattern-dictionary attack."),
code('''import random, re
hw2 = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "hw2")
pub = hw2.HyperWebster(); base = pub.characters
rnd = random.Random(2026); perm = list(base); rnd.shuffle(perm)
priv = hw2.HyperWebster("".join(perm))
text = CORPUS[:3000]
seen = pub.regenerate_text(priv.point_to_text(text))          # what an observer reconstructs from the integer
assert len(seen) == len(text)
def pattern(w):
    m, out = {}, []
    for c in w: out.append(m.setdefault(c, len(m) + 1))
    return tuple(out)
spans = [(m.start(), m.end()) for m in re.finditer(r"\\S+", text)]
same = sum(pattern(text[a:b]) == pattern(seen[a:b]) for a, b in spans)
print("words:", len(spans), "| repeat pattern identical after substitution:", same)
assert same == len(spans)
# how much does the pattern alone narrow a word? candidate set = dictionary words with the same pattern
dictionary = sorted({text[a:b].lower() for a, b in spans if b - a >= 4})
by_pat = {}
for w in dictionary: by_pat.setdefault(pattern(w), []).append(w)
unique = sum(len(v) == 1 for v in by_pat.values())
print("dictionary of", len(dictionary), "distinct words (length >= 4):", len(by_pat), "distinct patterns;", unique, "patterns pick out a single word")'''),
md("The word boundaries here are taken from the plaintext; an observer would locate them from the substituted space symbol, which is one more symbol to identify. What the numbers show is the general fact: **a per-symbol relabelling of the digits leaves the pattern structure of the text intact**, which is what the pattern-dictionary attack uses."),
])
write("v15_vigenere_model/03_sorted_rotations.ipynb", "# v15 · Sorted rotations of a string: the Burrows–Wheeler transform\nBurrows & Wheeler (SRC-RR-124, 1994; read in full): 'forms the N rotations of S, sorts them lexicographically, extracts the last character'. The rotations of a string are the rows of a tabula recta laid over the string. Reproduced against the paper's own worked example.", [
code('''def bwt(s):
    rows = sorted(s[i:] + s[:i] for i in range(len(s)))
    return "".join(r[-1] for r in rows), rows.index(s)
def ibwt(L, I):
    n = len(L); table = [""] * n
    for _ in range(n):
        table = sorted(L[i] + table[i] for i in range(n))
    return table[I]
L, I = bwt("abraca")
print("L =", L, " I =", I)
assert (L, I) == ("caraab", 1)               # the paper's example: L = 'caraab', I = 1
assert ibwt(L, I) == "abraca"
rows = sorted("abraca"[i:] + "abraca"[:i] for i in range(6)); print(rows)'''),
md("The transform is a permutation of the input (`L` is a rearrangement of `abraca`) plus one index, and it is reversible. It is the same object as v15/01's tabula recta rows, sorted."),
code('''import random
rnd = random.Random(1)
for _ in range(200):
    s = "".join(rnd.choice("ab c") for _ in range(rnd.randint(1, 12)))
    Lx, Ix = bwt(s); assert ibwt(Lx, Ix) == s
print("200 random strings: bwt/ibwt round trip exact")'''),
])

# ---------------------------------------------------------------- v16 debruijn / octonion fold
write("v16_debruijn_octonion_fold/01_tower_benchmark.ipynb", "# v16 · de Bruijn traversal + Cayley–Dickson fold to a fixed-width address\nBranch `data-storage-no-location` of `FourthAgePapers` (2026-08-30; local, unpushed): `DataStorageNoLocation/engine/bench_tower.py`. The files are read out of the branch with `git show`, unmodified, and run as a script.", [
code('''import subprocess, tempfile, pathlib, re
repo = os.path.join(PROJ, "FourthAgePapers")
def show(path): return subprocess.run(["git", "-C", repo, "show", "data-storage-no-location:" + path], capture_output=True, text=True, check=True).stdout
d = pathlib.Path(tempfile.mkdtemp()); (d / "engine").mkdir(); (d / "bench").mkdir()      # the script writes ../bench/rung0_address.txt
(d / "engine" / "bench_tower.py").write_text(show("DataStorageNoLocation/engine/bench_tower.py"))
(d / "bench" / "cover_letter.txt").write_text(show("DataStorageNoLocation/bench/cover_letter.txt"))
print("branch files:", subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", "data-storage-no-location", "DataStorageNoLocation"], capture_output=True, text=True).stdout.split())
print("document:", len((d / "bench" / "cover_letter.txt").read_bytes()), "bytes")'''),
code('''t0 = time.perf_counter()
out = subprocess.run([sys.executable, "bench_tower.py", "../bench/cover_letter.txt"], cwd=d / "engine", capture_output=True, text=True, timeout=900)
print("exit", out.returncode, "| %.0f s" % (time.perf_counter() - t0))
assert out.returncode == 0, out.stderr[-300:]
lines = out.stdout.splitlines()
i0 = next(i for i, l in enumerate(lines) if "time per data size" in l)
print("\\n".join(lines[i0:i0 + 13]))
start = next(i for i, l in enumerate(lines) if l.startswith("rung  alg"))
print("\\n".join(lines[start:start + 8]))'''),
md("Rung 0 (ℝ) is the raw bijection: its address grows with the document. Rungs ℂ → 𝕊 fold the same document into a **fixed 64-bit** address by the Cayley–Dickson product of the de Bruijn window sequence; time grows with the rung. The fold is not lossless for arbitrary documents (2⁶⁴ outputs, unbounded inputs); it is an *address* of the document that identifies what was stored. The 'reversible' column of the script refers to running the fold's own inverse on the stored windows."),
])

# ---------------------------------------------------------------- v17 layered calendrical index
src = open("/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/2026-09-29_hyperwebster_overhead/bench_layers2.py").read()
body = src[src.index("def charset_for"):src.index("def main")]
write("v17_layered_index/01_baseline_bench.ipynb", "# v17 · Layered calendrical index: the VAPMIP baseline benchmark, run unmodified\n`VAPMIP/benchmarks/hyperwebster_baseline_bench.py` (git 2026-09-25). It loads the canonical `hyperwebster.py` by path.", [
code('''bb = load("VAPMIP/benchmarks/hyperwebster_baseline_bench.py", "bb")
HW = bb._load_canonical_hyperwebster()
rows = bb.bench_chunk_sizes(HW, sizes=(140, 500, 1000, 2000, 4000))
print("chars  N_full bits_full  enc_ms   dec_ms | N_min bits_min")
for r in rows: print("%5d  %6d %9d %8.2f %8.2f | %5d %8d" % (r["chars"], r["N_full"], r["addr_bits_full"], r["enc_ms_full"], r["dec_ms_full"], r["N_min"], r["addr_bits_min"]))
ml = bb.bench_multilayer_reconstruction(HW)
print("4-layer chunk/day/month/year reconstruction: %.3f ms, exact: %s" % (ml["total_ms"], ml["roundtrip_ok"]))
assert ml["roundtrip_ok"]'''),
md("The benchmark's sample is one paragraph *repeated* to reach each size, so the 'minimal charset' columns describe a text with ~35 distinct symbols at every size. The reconstruction time is for a chain of four hops through one entry per level: it does not depend on how much history exists. The next notebook measures what the *size* of the address does across layers."),
])
write("v17_layered_index/02_layer_inflation.ipynb", "# v17 · Address size across layers: shipped charset vs. per-layer restricted charset vs. compact format\nThe calendrical index as described for this paper: chunk entries `{a, n, t}` → JSON day → JSON month, each layer addressed with the same class. Code below is extracted verbatim from the audit script `bench_layers2.py` (only the corpus source is replaced by the fixed 4000-character sample).", [
code('''hw_mod = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "hw_mod")
HyperWebster = hw_mod.HyperWebster
DEFAULT = HyperWebster()
import collections, json
''' + body.replace("\\", "\\\\").replace("'''", '"""') if False else '''hw_mod = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "hw_mod")
HyperWebster = hw_mod.HyperWebster
DEFAULT = HyperWebster()
import collections, json
_src = open(os.path.join(PROJ, "ContextPlease/claude/scratchpad/2026-09-29_hyperwebster_overhead/bench_layers2.py")).read()
exec(_src[_src.index("def charset_for"):_src.index("def main")])       # build(), restore(), charset_for(), chunk_texts()
print("extracted:", [n for n in ("charset_for", "chunk_texts", "build", "restore") if n in globals()])'''),
code('''text = CORPUS; raw = 8 * len(text); chunk = 200
print("corpus %d chars = %d raw bits | chunk %d | 4 chunks/day | 5 days/month" % (len(text), raw, chunk))
print("%-22s %-10s %-26s %-9s %-7s %s" % ("mode", "|charset|", "chunk/day/month (x raw)", "top ptr", "exact", "secs"))
for mode, compact in (("M0 shipped 97", False), ("B restricted", False), ("A+B compact (hex,;)", True)):
    t0 = time.perf_counter()
    L = build(text, chunk, mode if not compact else "A+B", compact)
    ok = restore(L, compact) == text
    bits = [sum(a.bit_length() for a, _ in l["ents"]) for l in L]
    print("%-22s %-10s %.3f / %.3f / %.3f      %-9.3f %-7s %.1f" % (mode, "/".join(str(len(l["cs"])) for l in L), bits[0]/raw, bits[1]/raw, bits[2]/raw, bits[2]/raw, ok, time.perf_counter()-t0))
    assert ok'''),
md("Every row restores the original text exactly. With the shipped 97-symbol charset the address of each layer is written in the same charset and grows by the JSON overhead each time (≈1.7× per layer here): the top pointer exceeds the size of the corpus. Restricting each layer to the symbols it contains, and using a compact non-JSON layer format, brings it below 1. This is the measured content of the 'layered index' claim: **time per layer is flat; size per layer is not, unless the layer format is chosen for it.**"),
])

# ---------------------------------------------------------------- v18 blackjack F21
write("v18_blackjack_f21/01_group_and_alphabet.ipynb", "# v18 · The Blackjack subgroup F₂₁ as an indexer: a negative result, with both halves measured\n`VAPMIP/benchmarks/blackjack_vs_horner_bench.py` (git 2026-09-25). F₂₁ = {x ↦ ax + b mod 7 : a ∈ {1, 2, 4}}, the normaliser of a Sylow-7 subgroup of PSL(2,7).", [
code('''bj = load("VAPMIP/benchmarks/blackjack_vs_horner_bench.py", "bj")
print(bj.verify_group())
c = bj.find_collision()
print("composing digits collapses to one of 21 states: sequences", c["seq_a"], "and", c["seq_b"], "both give", c["final_state"])
assert c and c["seq_a"] != c["seq_b"]'''),
md("**Half 1 (composition).** A word of group elements composed into one element has at most 21 possible results, so it cannot be an injective address for arbitrarily many strings. The collision above is found by brute force, not argued."),
md("**Half 2 (use the 21 elements as a digit alphabet).** Lossless again, since the digit sequence is kept. Cost against base 97:"),
code('''rows = bj.bench_sizes(sizes=(140, 500, 1000, 2000))
print("chars | base21 digits bits  enc_ms  dec_ms | base97 digits bits  enc_ms  dec_ms | bits21/bits97")
for r in rows: print("%5d | %13d %5d %7.2f %7.2f | %13d %5d %7.2f %7.2f | %.2f" % (r["chars"], r["n_digits_21"], r["bits_21"], r["enc_ms_21"], r["dec_ms_21"], r["n_digits_97"], r["bits_97"], r["enc_ms_97"], r["dec_ms_97"], r["bits_21"]/r["bits_97"]))
print("log2(97)/log2(21) =", round(math.log2(97)/math.log2(21), 3))'''),
md("Base 21 needs about 1.2× the bits here (the byte-to-base-21 step works on UTF-8 bytes, 8 bits per character, against 6.6 for base 97) and more digit operations. A smaller alphabet never shortens an exact address; it only lengthens the digit string."),
])

# ---------------------------------------------------------------- v19 Midline
write("v19_midline_index/01_mechanism.ipynb", "# v19 · Midline index: the 4-digit code T S DD over 96 characters, packed in base 96\n`PtolemyDesktop/Archimedes/Maths/MidlineIndex.py` (git 2026-09-27; rules revised 2026-10-12). One character is a decimal `type*1000 + sign*100 + step`: type 0 Uppercase, 1 Lowercase, 2 Digit, 3 Punctuation (line feed and space lead it); sign is the side of the anchor `M`/`m` for letters, always 0 for digits, the half for punctuation (two halves of 17); step is the distance from the anchor (never more than 13), the digit itself, or the index in the half. 96 codes are valid; the whole text is a base-96 Horner number over each code's index in that sorted list.", [
code('''import sys
sys.path.insert(0, PROJ)
mi = load("PtolemyDesktop/Archimedes/Maths/MidlineIndex.py", "mi")
for ch in "AMZamz05\\n !/:~":
    c = mi.encode_char(ch)
    print(repr(ch), "-> code %04d" % c, "->", repr(mi.decode_char(c)))
    assert mi.decode_char(c) == ch
addr = mi.encode_text("Hello, World -3!"); print(addr, mi.decode_text(addr, 16)); assert mi.verify("Hello, World -3!")'''),
md("## The valid codes: exactly 96, nothing else decodes"),
code('''from collections import Counter
print("VALID_CODES:", len(mi.VALID_CODES), "| K =", mi.K, "| by type:", dict(Counter(c // 1000 for c in mi.VALID_CODES)))
assert len(mi.VALID_CODES) == 96 == mi.K
assert sorted(mi.decode_char(c) for c in mi.VALID_CODES) == ["\\n"] + [chr(x) for x in range(0x20, 0x7F)]
bad = 0
for code_ in range(10000):
    if code_ not in mi.CODE_INDEX:
        try: mi.decode_char(code_); raise AssertionError(code_)
        except ValueError: bad += 1
print("codes 0000..9999 rejected by decode_char:", bad, "(= 10000 - 96)")
print("digits: sign always 0 ->", [mi.encode_char(d) for d in "0123456789"])
print("line feed and space lead the punctuation codes:", mi.encode_char("\\n"), mi.encode_char(" "), "| two halves of", mi.PUNCT_HALF, "characters:", repr(mi.PUNCT[:17]), repr(mi.PUNCT[17:]))'''),
md("## What it covers: case is exact, tab is four spaces, line feed is a code"),
code('''print("case exact:", mi.decode_text(mi.encode_text("hello"), 5), mi.decode_text(mi.encode_text("HeLLo"), 5))
print("tab -> four spaces:", repr(mi.normalise("a\\tb")))
for bad_ in ["a\\rb", "caf\\u00e9"]:
    try: mi.encode_text(bad_)
    except ValueError as e: print(repr(bad_), "->", e)
dom = "".join(c for c in mi.normalise(CORPUS) if 0x20 <= ord(c) <= 0x7E or c == "\\n")
a = mi.encode_text(dom)
print("corpus (tabs to four spaces, line feeds kept):", len(dom), "chars | address bits:", a.bit_length(), "| bits/char:", round(a.bit_length()/len(dom), 3))
print("log2(96) =", round(math.log2(96), 3), "| log2(97) =", round(math.log2(97), 3), "| four decimal digits as written =", round(math.log2(10000), 3))
assert mi.decode_text(a, len(dom)) == dom'''),
md("The address is base 96, so it costs log₂ 96 = 6.585 bits per character: the minimum for 96 equally likely symbols, just under the 97-symbol Horner (6.60) because only tab is out of the domain. Storing the four decimal digits as written would cost 13.29 bits per character. Ordering the 95 symbols as T S DD makes the list a fixed permutation like any other base-96 `.perm`: it does not change the size, only which characters sit near each other."),
code('''print(mi.overhead_report())'''),
])
write("v19_midline_index/02_de_bruijn_and_pathway.ipynb", "# v19 · De Bruijn sequence over the 96 valid codes, and the pointer pathway over 97 symbols", [
code('''import sys
sys.path.insert(0, PROJ)
mi = load("PtolemyDesktop/Archimedes/Maths/MidlineIndex.py", "mi")
print("VALID_CODES:", len(mi.VALID_CODES), "= K =", mi.K)
r = mi.verify_de_bruijn(2, k=mi.ALPHABET_SIZE); print({k: r[k] for k in ("k", "n", "sequence_length", "all_windows_exactly_once")})
s = mi.de_bruijn_text(2)
wins = Counter(s[i] + s[(i + 1) % len(s)] for i in range(len(s)))
print("96-symbol text, n=2: length", len(s), "| distinct cyclic 2-windows:", len(wins), "| each exactly once:", set(wins.values()) == {1})
assert len(s) == 96**2 and set(wins.values()) == {1}'''),
md("Every 2-symbol window over the 96 characters occurs exactly once, cyclically, in a string of 96² = 9,216 characters. Moving from one window to the next is a one-symbol shift: this is the traversal order that the `DataStorageNoLocation` branch (v16) uses in place of walking a factorial tree."),
md("## The pointer pathway: first pointer absolute, then deltas (97 symbols)"),
code('''for w in ["THIS", "hello", "Ptolemy"]:
    p = mi.pathway(w); print(w, p, "->", mi.reconstruct_from_pathway(p)); assert mi.reconstruct_from_pathway(p) == w
allp = [d for w in CORPUS.split() for d in mi.pathway(w)[1:]]
print("deltas over the corpus words: min", min(allp), "max", max(allp), "| distinct:", len(set(allp)), "of a possible", 2*96 + 1)'''),
md("The delta between two pointers lies in −96..96, so a delta alone is not bounded by 13 as it is for the letter-from-M step; the bound in the letter encoding comes from the fixed anchor M, not from adjacency."),
])
