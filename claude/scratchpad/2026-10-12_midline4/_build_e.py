from _nb import md, code, write

# ------------------------------------------------------------- S1 taxonomy
write("w01_taxonomy/01_every_kind_one_input_set.ipynb", "# S1 · Every kind of hyperindex, one input set\nEach version's address function is run on the same two inputs: **(A)** all 18,278 lowercase words of length ≤ 3 (collision counts are exact, not sampled) and **(B)** the first 1,000 characters of the corpus sample (size). Versions are loaded by path, unmodified.", [
code('''import sys, string, re, math
from itertools import product
sys.path.insert(0, os.path.join(PROJ, "PtolemyDesktop")); sys.path.insert(0, os.path.join(PROJ, "VAPMIP", "engines")); sys.path.insert(0, PROJ)
D = "PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/"
fa   = load("PtolemyDesktop/Archive/ainulindale_first_age/FA_smnnip_hyperindex.py", "fa")
hw2  = load(D + "hyperwebster.py", "hw2").HyperWebster()                    # v02
hh   = load(D + "hyperwebster-hash.py", "hh").HyperWebster()                # v03
from Callimachus.v09.core.hyperwebster import HyperWebster as HW9           # v09
hw9  = HW9()
sw   = load("SemanticWordEngine/hyperwebster.py", "sw"); mo = load("VAPMIP/monad.py", "mo")
lex  = sw.Lexicon({k: v for k, v in mo._ZERO_CACHE.items() if k <= 50}, path="/dev/null")   # v11 with 50 zeros
e17  = load("VAPMIP/engines/e17_hyperindexing.py", "e17"); prim16 = e17.primes_up_to_n(16)
vq   = load("ValaQuenta/modules/hyperwebster/maths.py", "vq")
mi   = load("PtolemyDesktop/Archimedes/Maths/MidlineIndex.py", "mi")
words = ["".join(p) for n in (1, 2, 3) for p in product(string.ascii_lowercase, repeat=n)]
print(len(words), "words; modules loaded")'''),
md("## The address function of each version, as one callable\nSix of the versions are exact or nearly so; three are deliberately many-to-one. The **multiset** address (v06 notebook 03) is written out here so the row can be measured."),
code('''from collections import Counter
idx = {c: i for i, c in enumerate(hw2.characters)}
def multiset_rank(text):
    c = Counter(text); syms = sorted(c, key=lambda ch: idx[ch]); m = len(text)
    P = math.factorial(m)
    for k in c.values(): P //= math.factorial(k)
    r = 0
    for ch in text:
        r += P * sum(c[x] for x in syms if idx[x] < idx[ch]) // m
        P = P * c[ch] // m; c[ch] -= 1; m -= 1
    return r
def fsig(w):
    raw = [e17.project(w, k, prim16) for k in range(16)]; nm = math.sqrt(sum(x*x for x in raw)); v = [x/nm for x in raw]
    return tuple(sorted(range(16), key=lambda k: abs(v[k])))
KINDS = [  # (version, kind, function word -> hashable address)
 ("v00", "mixed radix, length NOT included",   lambda w: fa.TextHyperIndex.encode_text(w)),
 ("v00", "mixed radix + stored length",         lambda w: (fa.TextHyperIndex.encode_text(w), len(w))),
 ("v02", "exact bijection (shortlex rank)",     lambda w: hw2.point_to_text(w)),
 ("v03", "SHA-256 label of the bijection",      lambda w: hh.index_text(w).label),
 ("v09", "SHA-256 label, Unicode order",        lambda w: hw9.label_of(w)),
 ("v14", "mixed radix + stored length",         lambda w: (vq.horner_encode(w), len(w))),
 ("v06", "(count vector, rank in anagram class)", lambda w: (tuple(sorted(Counter(w).items())), multiset_rank(w))),
 ("v11", "semantic zero ordinal (50 zeros)",    lambda w: lex.address_of(w)[0]),
 ("v12", "prime zero index",                    lambda w: mo._word_zero_idx(w)),
 ("v13", "firing signature, n = 16",            fsig),
 ("v19", "Midline base-96 (case exact)",         lambda w: mi.encode_text(w)),
]
rows = []
for ver, kind, f in KINDS:
    t0 = time.perf_counter(); vals = [f(w) for w in words]; dt = time.perf_counter() - t0
    d = len(set(vals))
    rows.append((ver, kind, d, len(words) - d, f("listen") == f("silent"), dt))
print("%-4s %-42s %9s %10s %-18s %s" % ("ver", "kind", "distinct", "collisions", "listen==silent?", "secs"))
for ver, kind, d, c, an, dt in rows: print("%-4s %-42s %9d %10d %-18s %.1f" % (ver, kind, d, c, an, dt))'''),
md("**Reading the table.** *Distinct* counts addresses among 18,278 words (the exact rows reach 18,278). Rows with **collisions > 0** cannot be inverted. v00's integer alone collides because symbol 0 is `a`; with the length it is exact. v19 is exact on these words (case is kept, the 96-symbol domain covers lowercase)."),
code('''assert dict((k, d) for _, k, d, *_ in rows)["exact bijection (shortlex rank)"] == len(words)
ex = {kind: (d == len(words)) for _, kind, d, *_ in rows}
print("exact on this set:", [k for k, v in ex.items() if v])
print("many-to-one on this set:", [k for k, v in ex.items() if not v])'''),
md("## Size, on 1,000 characters of the corpus sample\nBits of the address (where the address grows with the input) or bits of its range (where it is fixed width)."),
code('''t = CORPUS[:1000]; n = len(t); N = 97
mult = math.factorial(n)
for k in Counter(t).values(): mult //= math.factorial(k)
dom = "".join(c for c in mi.normalise(t) if 0x20 <= ord(c) <= 0x7E or c == chr(10))
sizes = [
 ("raw, 8 bits per character",                     8 * n, "grows"),
 ("v02 exact bijection",                            hw2.point_to_text(t).bit_length(), "grows"),
 ("v00/v14 mixed radix + length",                   fa.TextHyperIndex.encode_text(t).bit_length() if False else vq.horner_encode(t).bit_length(), "grows"),
 ("v03/v09 label (SHA-256)",                        256, "fixed (key only; payload is the v02 address)"),
 ("v06 (count vector, rank)",                       (mult.bit_length() - 1) + (math.comb(n + N - 1, N - 1).bit_length() - 1), "grows (order-0 entropy)"),
 ("v11 zero ordinal (of 50)",                       round(math.log2(50), 2), "fixed"),
 ("v12 zero index (of 6,543)",                      round(math.log2(6543), 2), "fixed"),
 ("v13 signature, n = 16 (16! values)",             round(math.log2(math.factorial(16)), 2), "fixed"),
 ("v19 Midline, %d characters" % len(dom),          mi.encode_text(dom).bit_length(), "grows (domain 96)"),
 ("v16 fold, rungs ℂ…𝕊 (from v16 notebook)",        64, "fixed"),
]
print("%-46s %10s   %s" % ("address", "bits", "behaviour"))
for name, b, beh in sizes: print("%-46s %10s   %s" % (name, b, beh))'''),
md("Two families follow from the table: **addresses that grow with the input** (exact; the size is the text's information content in another radix; the only ones smaller than raw are those that give up part of the alphabet or spend the text's non-uniformity) and **addresses of fixed width** (v03/v09 label, v11, v12, v13, v16), which are keys, not stores: they identify or locate, and none of them inverts. This is the paper's classification."),
])

# ------------------------------------------------------------- S2 permutation structure
write("w02_permutation_structure/01_the_permutation_facts.ipynb", "# S2 · The permutation structure of a hyperindex, in one place\nFour exact facts, each checked here (the versions that first showed them are named).", [
code('''import random, itertools
from collections import Counter
hw2 = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "hw2"); HW = hw2.HyperWebster()
N = HW.N; idx = HW._char_index'''),
md("## 1. A string is an arrangement; its address among the arrangements of the same multiset is a permutation rank (v06)\nFor a string of **distinct** symbols the rank within its anagram class is exactly its lexicographic permutation rank. Checked for all 720 arrangements of 6 symbols and all 5,040 of 7."),
code('''def multiset_rank(text):
    c = Counter(text); syms = sorted(c, key=lambda ch: idx[ch]); m = len(text)
    P = math.factorial(m)
    for k in c.values(): P //= math.factorial(k)
    r = 0
    for ch in text:
        r += P * sum(c[x] for x in syms if idx[x] < idx[ch]) // m
        P = P * c[ch] // m; c[ch] -= 1; m -= 1
    return r
for base in ("qwerty", "qwertyu"):
    syms = sorted(base, key=lambda ch: idx[ch])
    ok = all(multiset_rank("".join(p)) == k for k, p in enumerate(itertools.permutations(syms)))
    print(base, "->", math.factorial(len(base)), "arrangements; rank == lexicographic permutation rank for all:", ok)
    assert ok
print("anagram classes over all lowercase words of length <= 3:")
cls = Counter(tuple(sorted(w)) for w in ("".join(p) for n in (1, 2, 3) for p in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=n)))
print("  ", len(cls), "classes; sizes:", sorted(Counter(cls.values()).items()))'''),
md("## 2. A transposition of two positions changes the address by a closed form (v04)\nExhaustive over every pair of positions of a 12-character string."),
code('''rnd = random.Random(3)
t = "".join(rnd.choice(HW.characters) for _ in range(12)); L = len(t)
a0 = HW.point_to_text(t); d = lambda c: idx[c] + 1
ok = True
for i, j in itertools.combinations(range(L), 2):
    u = list(t); u[i], u[j] = u[j], u[i]; u = "".join(u)
    off = (d(t[j]) - d(t[i])) * (N ** (L - 1 - i) - N ** (L - 1 - j))
    ok &= HW.point_to_text(u) == a0 + off
print(len(list(itertools.combinations(range(L), 2))), "transpositions; offset formula exact for all:", ok); assert ok'''),
md("## 3. A charset order is a permutation of the digits; the address of a string under charset π is the public address of the relabelled string (v09, v10)\n200 random strings, 5 random charset orders. The key space is 97! ≈ 2⁵⁰⁵; `rank1`/`unrank1` (Myrvold & Ruskey 2001) give the integer key of an order."),
code('''def unrank1(n, r):
    pi = list(range(n))
    while n > 0:
        pi[n-1], pi[r % n] = pi[r % n], pi[n-1]; r //= n; n -= 1
    return pi
def rank1(pi):
    pi = list(pi); n = len(pi); inv = [0]*n
    for i, v in enumerate(pi): inv[v] = i
    r, mult = 0, 1
    for m in range(n, 1, -1):
        s = pi[m-1]; pi[m-1], pi[inv[m-1]] = pi[inv[m-1]], pi[m-1]; inv[s], inv[m-1] = inv[m-1], inv[s]
        r += s * mult; mult *= m
    return r
rnd = random.Random(11); base = HW.characters
for trial in range(5):
    key = rnd.randrange(math.factorial(97)); pi = unrank1(97, key); assert rank1(pi) == key
    priv = hw2.HyperWebster("".join(base[i] for i in pi))
    for _ in range(40):
        s = "".join(rnd.choice(base) for _ in range(rnd.randint(1, 30)))
        relabelled = "".join(base[pi.index(idx[c])] if False else base[pi.index(idx[c])] for c in s) if False else "".join(base[pi.index(idx[c])] for c in s)
        assert priv.point_to_text(s) == HW.point_to_text(relabelled)
print("private address == public address of the relabelled string: 200 checks; key rank round trip: 5 of 5; 97! has", math.factorial(97).bit_length(), "bits")'''),
md("## 4. The count of distinct hyperindex addresses is the count of strings; the count of permutations of a string is the multinomial\nFor a string of length L over 97 symbols, the number of strings with a given multiset is L!/∏cₖ!, and summed over multisets it is 97ᴸ. Checked exactly for L = 4.") ,
code('''from itertools import product
L = 4; alphabet = "abcd"                          # 4-symbol check of the identity over ALL strings
tot = 0
for comp in product(range(L + 1), repeat=len(alphabet)):
    if sum(comp) == L:
        tot += math.factorial(L) // math.prod(math.factorial(c) for c in comp)
print("sum over multisets of L!/prod(c!) =", tot, "| 4^4 =", 4 ** L); assert tot == 4 ** L'''),
])

# ------------------------------------------------------------- S3 Babel scale
write("w03_babel_scale/01_babel_scale.ipynb", "# S3 · Library of Babel scale, computed\nThe premise cited under the paper's title: Basile, libraryofbabel.info, About page: the site holds all pages of 3,200 characters (\"approximately 10^4677 books\"); the complete library would hold every combination of 1,312,000 characters. Below, those numbers are recomputed and the exact shipped class is run on a 29-symbol charset. The site's own numbering algorithm is not examined here; the numbering below is this paper's.", [
code('''LOG10_29 = math.log10(29)
page_chars, book_chars, pages_per_book = 3200, 1_312_000, 410
log_pages = page_chars * LOG10_29
print("pages of 3,200 characters over 29 symbols: 10^%.2f" % log_pages)
print("divided by 410 pages per book:            10^%.2f  (the site says ~10^4677)" % (log_pages - math.log10(pages_per_book)))
print("books of 1,312,000 characters:            10^%.0f" % (book_chars * LOG10_29))
print("1,312,000 = 410 x 3,200 =", pages_per_book * page_chars, "; = 410 pages x 40 lines x 80 chars =", 410 * 40 * 80)
assert round(log_pages - math.log10(pages_per_book)) == 4677'''),
md("## The shipped class on the Babel alphabet\n29 symbols: 26 letters, space, comma, period. A page is a 3,200-character string; its address is a base-29 numeral."),
code('''import random
hw2 = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "hw2")
B = hw2.HyperWebster("abcdefghijklmnopqrstuvwxyz ,.")
print("N =", B.N)
rnd = random.Random(1)
page = "".join(rnd.choice(B.characters) for _ in range(page_chars))
t0 = time.perf_counter(); a = B.point_to_text(page); t1 = time.perf_counter(); back = B.regenerate_text(a); t2 = time.perf_counter()
assert back == page
print("page of %d chars -> address of %d bits (= %.1f bits/char; log2(29) = %.3f) | encode %.0f ms, decode %.0f ms" % (page_chars, a.bit_length(), a.bit_length()/page_chars, math.log2(29), 1000*(t1-t0), 1000*(t2-t1)))
print("relative to 8-bit text: %.3f" % (a.bit_length() / (8 * page_chars)), "= log2(29)/8 =", round(math.log2(29)/8, 3))'''),
md("## A page's location is one integer: fixed-length pages and shortlex ranks\nAmong *all* strings the class ranks by length first; among the 3,200-character pages the location is the plain base-29 numeral of the page. The offset between the two numberings is the count of shorter strings, (29³²⁰⁰ − 29)/28."),
code('''plain = 0
for ch in page: plain = plain * 29 + B._char_index[ch]
shorter = (29 ** page_chars - 29) // 28
print("shortlex address - number of shorter strings == plain base-29 value:", a - shorter == plain); assert a - shorter == plain
print("first page (3,200 x 'a') has location 0; last page (3,200 x '.') has location", 29**page_chars - 1 == B.point_to_text("." * page_chars) - shorter)'''),
md("## Neighbouring pages are neighbouring integers\nChanging only the last character by one step in the charset order moves the location by exactly 1; changing the first moves it by 29³¹⁹⁹."),
code('''chars = B.characters
i = chars.index(page[-1]); j = (i + 1) % 29
p2 = page[:-1] + chars[j]
if j > i: print("last character +1 step -> location difference:", B.point_to_text(p2) - a); assert B.point_to_text(p2) - a == 1
q = chars.index(page[0]); r = (q + 1) % 29
if r > q:
    p3 = chars[r] + page[1:]; print("first character +1 step -> location difference == 29^3199:", B.point_to_text(p3) - a == 29 ** 3199)
else: print("first character wraps; skipped")'''),
md("## One book: size is exact, time is an extrapolation (stated as such)\nA 1,312,000-character book has an address of 1,312,000 · log₂29 bits. Encoding time is measured at four sizes, the exponent is fitted, and the time for a book is extrapolated from the fit."),
code('''sizes = [2000, 4000, 8000, 16000]; ts = []; tf = []
def forward(t, N=29, idx=B._char_index):
    a = 0
    for c in t: a = a * N + idx[c] + 1
    return a - 1
for s in sizes:
    txt = "".join(rnd.choice(B.characters) for _ in range(s))
    t0 = time.perf_counter(); x = B.point_to_text(txt); t1 = time.perf_counter(); y = forward(txt); t2 = time.perf_counter()
    assert x == y; ts.append(t1 - t0); tf.append(t2 - t1)
import math as m
fit = lambda v: m.log(v[-1] / v[0]) / m.log(sizes[-1] / sizes[0])
book_bits = book_chars * m.log2(29)
print("chars  point_to_text s  forward Horner s")
for s, a, b in zip(sizes, ts, tf): print("%5d  %15.3f  %16.4f" % (s, a, b))
print("fitted exponents: point_to_text %.2f | forward Horner %.2f" % (fit(ts), fit(tf)))
print("book address: %.0f bits = %.0f KiB" % (book_bits, book_bits / 8 / 1024))
for name, v in (("point_to_text", ts), ("forward Horner", tf)):
    est = v[-1] * (book_chars / sizes[-1]) ** fit(v)
    print("ESTIMATE, not measured: encoding one book with %-14s ~ %10.0f s (%.1f h)" % (name, est, est / 3600))'''),
])
