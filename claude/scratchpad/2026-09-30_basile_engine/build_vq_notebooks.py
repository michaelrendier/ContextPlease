import nbformat as nbf, os
OUT = "/home/rendier/Projects/ThePlace/ValaQuenta/notebooks/basile"
md = lambda s: nbf.v4.new_markdown_cell(s.strip("\n"))
code = lambda s: nbf.v4.new_code_cell(s.strip("\n"))
PRE = '''import sys, os, importlib.util, math, time, random
sys.path.insert(0, os.path.abspath('../..'))
def load_maths():
    spec = importlib.util.spec_from_file_location("basile_maths", "../../modules/basile/maths.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
M = load_maths()
CACHE = M.default_cache_dir()
HAVE = os.path.exists(os.path.join(CACHE, "PRNG")) and os.path.exists(os.path.join(CACHE, "imagesearch.cpp"))
print("engine loaded; published files in cache:", HAVE, "| gmpy2 accelerator:", M._gmpy2 is not None)'''
def write(name, cells):
    nb = nbf.v4.new_notebook(); nb.cells = cells
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nbf.write(nb, os.path.join(OUT, name))

write("01_recipe_and_toy_library.ipynb", [
md("# Basile engine 1 · The recipe, and a toy library checked exhaustively\n**Engine:** `ValaQuenta.modules.basile` · confidence floor ESTABLISHED.\n\nThe Library of Babel family joins a *location* (a number) to a *page* (a numeral) by an invertible pseudo-random map, so nothing is stored. Basile's published README gives the recipe: an LCG `(a·p + c) mod m`, then shift/XOR steps; inverse = undo the steps in reverse, then `a⁻¹(p − c) mod m`. This notebook exercises the **generic** recipe (written from the README, no published code or constant used) on a library small enough to check every location."),
code(PRE),
md("## The ordered address: the same set of pages in rank order\nBijective base-N (shortest first). `ordered_address` and `ordered_text_at` are inverses."),
code('''A = "abcdefghijklmnopqrstuvwxyz"
print([(n, M.ordered_text_at(n, A)) for n in (0, 25, 26, 701, 702)])
assert all(M.ordered_address(M.ordered_text_at(n, A), A) == n for n in range(20000))
print("round trip exact for 20,000 addresses")'''),
md("## The two xorshift steps have exact inverses\nRight xorshift: `y ⊕ (y≫s) ⊕ (y≫2s) ⊕ …`. Masked left xorshift: ⌈k/s⌉ fixed-point iterations, each fixing `s` more low bits."),
code('''rnd = random.Random(1)
for width, s in ((64, 7), (257, 11), (1000, 13), (5000, 1)):
    for _ in range(300):
        x = rnd.getrandbits(width); k = width - s
        assert M.xorshift_right_inverse(M.xorshift_right(x, s), s) == x
        assert M.xorshift_left_masked_inverse(M.xorshift_left_masked(x, k, s), k, s) == x
print("both inverses exact on 1,200 random words at four widths")'''),
md("## The scrambler of [0, N): LCG modulo 2^e + two xorshifts + cycle-walking\nN = 29³ = 24,389 pages (29 symbols, 3-character pages). **Every** location is checked."),
code('''N = 29 ** 3
sc, un = M.power_of_two_scrambler(N)
vals = [sc(x) for x in range(N)]
assert sorted(vals) == list(range(N)) and all(un(sc(x)) == x for x in range(N))
print("N =", N, "| a bijection on [0, N): True | every location round-trips: True")
print("Hull-Dobell (m = 2^15, a = 1664525, c = 1013904223, prime factors [2]):", M.hull_dobell(1 << 15, 1664525, 1013904223, [2]))'''),
md("## A page and its location, both directions"),
code('''print("loc   scrambled  ordered")
for loc in range(8): print("%-5d %-10r %r" % (loc, M.babel_page(loc), M.page_at(loc, M.BABEL_ALPHABET, 3)))
assert all(M.babel_location(M.babel_page(l)) == l for l in (0, 1, 777, N - 1))'''),
md("## Neighbouring locations\nMean number of the 3 characters that differ between the pages at L and L+1, over all 24,388 pairs."),
code('''d = lambda a, b: sum(x != y for x, y in zip(a, b))
o = sum(d(M.page_at(i, M.BABEL_ALPHABET, 3), M.page_at(i + 1, M.BABEL_ALPHABET, 3)) for i in range(N - 1)) / (N - 1)
s = sum(d(M.page_at(sc(i), M.BABEL_ALPHABET, 3), M.page_at(sc(i + 1), M.BABEL_ALPHABET, 3)) for i in range(N - 1)) / (N - 1)
print("ordered %.3f | scrambled %.3f | independent pages would give %.3f" % (o, s, 3 * 28 / 29))'''),
md("## Cycle structure: which part is cyclic\nThe LCG modulo 2^e is one full cycle (Hull–Dobell). The scrambler built on it is a permutation with several cycles; its spectrum is the roots of unity of each cycle length present."),
code('''c = M.permutation_cycles(sc, N)
big = 1 << 15
lcg = M.permutation_cycles(lambda x: (1664525 * x + 1013904223) % big, big)
xs = M.permutation_cycles(lambda x: M.xorshift_left_masked(M.xorshift_right(x, 7), 10, 5) & (big - 1), big)
print("pure LCG mod 2^15  : cycles", len(lcg), "| longest", lcg[0])
print("scrambler (N=%d)   : cycles %d | longest %d | fixed points %d | top lengths %s" % (N, len(c), c[0], c.count(1), c[:8]))
assert lcg == [big] and len(c) > 1'''),
md("## Open items, stated\n* This is **our** realisation of the recipe. It is not the text library's algorithm, which is not published (Basile's README: the published one is the more efficient rewrite for the image library).\n* Bijectivity here comes from a power-of-two modulus (Hull–Dobell for `2^e`) and cycle-walking. The published Babelia code uses a different modulus (a 3.19-million-bit `m`, not a power of two); notebook 2 audits it."),
])

write("02_published_babelia.ipynb", [
md("# Basile engine 2 · The published Babelia engine on its published constants\nBasile's repository `librarianofbabel/libraryofbabel.info-algo` (CC BY-SA-NC, uploaded 2019-01-02) holds the image library's forward transform (`PRNG`, i.e. `babelia.cpp`) and its inverse (`imagesearch.cpp`). **The files are not part of ValaQuenta** (GPL-3.0-only); the engine reads them from a local cache at run time. To fetch them once (network, about 7 MB): `M.fetch_published()`.\n\nBoth programs are C++ with 3.19-million-bit integers; the engine runs them in Python integers (gmpy2 when present, plain Python otherwise: identical results)."),
code(PRE + "\nassert HAVE, 'published files not in the cache: run M.fetch_published() (network) and re-run'\npub = M.Published(CACHE)"),
md("## The constants, audited\nEverything below is measured on the parsed constants, not asserted."),
code('''au = pub.audit()
for k in ("bit_lengths", "shared_constants_identical", "a_times_ainverse_mod_m_is_1", "gcd_a_m_is_1", "gcd_c_m_is_1", "m_mod_4", "a_mod_4", "m_prime_power", "hull_dobell", "a_over_m_bits",
          "maskone_is_power_of_two", "masktwo_is_power_of_two", "divver_is_power_of_two", "chunk_bits", "drawn_bits_per_chunk", "image_bits", "m_bits", "palette_entries", "palette_is_hex_of_index"):
    print("%-32s %s" % (k, au[k]))
print("forward chain read from the PRNG file:", au["forward_steps"])
assert au["a_times_ainverse_mod_m_is_1"] and all(au["shared_constants_identical"].values())'''),
md("**Reading it.** `PRNG` and `imagesearch.cpp` carry the same `m, c, maskone, masktwo`; `a·a⁻¹ ≡ 1 (mod m)` holds; the three masks are exact powers of two, so `% maskone` is a bit mask and `% divver` keeps the low 399,361 bits. `m` is exactly a power of 3 (`3^2,015,755`), so Hull–Dobell is decidable: `gcd(c, m) = 1` and `3 | a − 1` hold, the published LCG alone is one cycle of length `m`. `a` and `c` are about half the size of `m` (the README advises values close to `m`). The palette table is exactly `#%03X` of its index."),
md("## Geometry: what the image reads\n640×416 = 8 quarters of 160×208 = 33,280 pixels each; 12 bits per pixel; each quarter is a 399,361-bit chunk of which 399,360 bits are drawn."),
code('''print("image bits          :", au["image_bits"], "= 640*416*12")
print("bits of m           :", au["m_bits"], "(", au["m_bits"] - au["image_bits"], "more than the image )")
print("bits the chunks span:", pub.chunk_bits * 8)
print("unread positions    :", pub.unread_positions())'''),
md("## Forward and inverse, on a random location"),
code('''rnd = random.Random(1)
loc = rnd.getrandbits(au["m_bits"] - 2) % int(pub.m)
t0 = time.perf_counter(); p = pub.forward(loc); t1 = time.perf_counter(); back = pub.inverse(p); t2 = time.perf_counter()
print("forward %.2fs | inverse %.2fs | inverse(forward(loc)) == loc: %s" % (t1 - t0, t2 - t1, back == loc))
assert back == loc'''),
md("## An image: pixels, and the location the search returns\nThe first five pixels of the first quarter at that location, as the site's `#RGB` codes."),
code('''quarters = pub.pixels(p)
print("quarters:", len(quarters), "| pixels each:", len(quarters[0]), "| first five:", ["#%03X" % c for c in quarters[0][:5]])
loc2 = pub.search(quarters)
same = pub.pixels(pub.forward(loc2)) == quarters
print("search(image) returns a location whose image is this image:", same, "| that location equals the one we started from:", loc2 == loc)'''),
md("**The search returns a location, not the location.** The image reads fewer bits than the location space holds (17 unread positions), so several locations show one image; the search sets the unread bits to zero and returns one of them."),
md("## Several locations, one image\nFor each unread bit position: flip it in the transformed value, invert, and check whether a *different* location gives the *same* image."),
code('''print("position   distinct-location  forward(location)==value  same-image")
for pos in pub.unread_positions():
    w = pub.sibling(loc, pos)
    print("%-10d %-18s %-25s %s" % (pos, w["sibling_differs"], w["forward_matches"], w["same_image"]))
print(pub.mean_locations_per_image())'''),
md("Sixteen of the seventeen unread positions give a second, valid location for the same image. The seventeenth, the highest, produces a value that no location transforms to (`forward_matches` is False), so it is not a witness. The average number of locations per image is `m / 2^3,194,880`, about 6.95×10⁴ (2¹⁶ × 1.06)."),
md("## The fibre of an image: additive within a location, different between locations\nFor each valid unread bit the offset from a location to its sibling is `inverse(forward(L) ^ 2^b) - L (mod m)`."),
code('''rnd = random.Random(9)
la = rnd.getrandbits(au["m_bits"] - 2) % int(pub.m); lb = rnd.getrandbits(au["m_bits"] - 2) % int(pub.m)
a = pub.sibling_offsets(la, pairs=6, seed=1)
print({k: v for k, v in a.items() if k != "offset_bit_lengths"})
pos = pub.unread_positions()[0]
o = [(pub.inverse(pub.forward(L) ^ (1 << pos)) - L) % int(pub.m) for L in (la, lb)]
print("same bit, two locations: offsets equal:", o[0] == o[1])
assert a["pairs_additive"] and a["all_bits_together_additive"] and o[0] != o[1]'''),
md("Within a location the sixteen offsets add (six random pairs and all sixteen together), so the fibre is `{L + a subset sum of the offsets}`, a box of 2¹⁶ points in Z_m. The offset for a given bit **differs** between the two locations: the generators of the box depend on the location, so the fibre is not a fixed coset of a subgroup. The Fourier transform of the fibre's indicator is `e^(2πikL/m) · ∏_b (1 + e^(2πik·o_b/m))`."),
md("## What this notebook does not establish\n* Whether the live site serves images by exactly this code: only the published source was read.\n* The text library: its algorithm is not published."),
])

write("03_smaller_published_pieces.ipynb", [
md("# Basile engine 3 · The smaller published pieces\nBasile's public repositories, checked 2026-09-30: **libraryofbabel.info-algo** (the Babelia PRNG, its search, and `Euclid's Extended`; CC BY-SA-NC) · **LoB-API** (a CC0 licence file only; no code) · **LobThis** and **LoBThis-Firefox** (browser extensions; LobThis is a fork of `rik-degraaff/LobThis`, licence not stated) · **newsometimesatdawn**, **Dezmediah-site** (web sites)."),
code(PRE),
md("## `Euclid's Extended` (lcgreverse.cpp): a template with a 25-entry array\nThe file's `m` and `a` are empty strings (`mpz_int m(\"\")`), so it is a template. It keeps the running coefficients in `qarray[25]` and writes `qarray[i]` for `i = 2, 3, …`: it holds 23 divisions. The port raises `OverflowError` where the C++ would write past the array."),
code('''print("3^-1 mod 7 =", M.euclid_inverse_qarray(3, 7), "| 17^-1 mod 3120 =", M.euclid_inverse_qarray(17, 3120), "(divisions:", M.euclid_steps(17, 3120), ")")
rnd = random.Random(2); over = 0; steps = []
for _ in range(200):
    m = rnd.getrandbits(64) | (1 << 63) | 1; a = rnd.getrandbits(63) | 1
    steps.append(M.euclid_steps(a, m))
    try: M.euclid_inverse_qarray(a, m)
    except OverflowError: over += 1
print("random 64-bit inputs: overflow in %d of 200 | mean divisions %.1f | the array allows %d" % (over, sum(steps) / 200, M.EUCLID_QARRAY_SIZE - 2))
a_bits = 1597519
print("published a has %d bits: about 0.843*ln(a) = %.0f divisions (ESTIMATE), against 23 in the array" % (a_bits, 0.843 * a_bits * math.log(2)))
assert over > 150'''),
md("`pow(a, -1, m)` (used by the engine) has no such limit."),
md("## LobThis: one request, built as data\nThe extension submits the current page's HTML as the `extension` field of a POST form to `resourcelocator.cgi`. The engine returns that request and sends nothing."),
code('''print(M.resource_locator_request("some page text"))'''),
md("## Site addresses\n`<hexagon>-w<wall>-s<shelf>-v<volume>[:<page>]`; per the site's Reference Hex page: 4 walls, 5 shelves per wall, 32 volumes per shelf, 410 pages per volume, 40 lines of about 80 characters."),
code('''r = M.parse_babel_address("jeb0110jlb-w2-s4-v16:19"); print(r)
print("volumes per hexagon:", M.WALLS_PER_HEXAGON * M.SHELVES_PER_WALL * M.BOOKS_PER_SHELF, "| characters per volume:", M.PAGES_PER_BOOK * M.LINES_PER_PAGE * M.CHARS_PER_LINE)
print("volume index is the last volume of the last shelf of the last wall:", M.parse_babel_address("x-w4-s5-v32")["volume_index"])'''),
md("## The scale of the text library, recomputed"),
code('''s = M.library_scale(); print(s)
assert round(s["log10_books"]) == 4677'''),
])

write("04_registry_formulary.ipynb", [
md("# Basile engine 4 · The formulary, end to end\nEvery equation of `BasileModule`, run through the registry with its defaults. The three `published_*` equations need the local copy of Basile's files and say so when it is missing."),
code('''import sys, os, time
sys.path.insert(0, os.path.abspath('../../..'))
from ValaQuenta.__main__ import _register_all
reg = _register_all(); mod = reg.get_module("basile")
print(mod.display_name, "| version", mod.version, "| floor", mod.confidence_floor, "|", len(mod.formulary()), "equations")'''),
code('''for e in mod.formulary():
    t0 = time.perf_counter()
    try:
        r = reg.run("basile." + e.name, {})["result"]; status = "ok"
    except FileNotFoundError as ex:
        r, status = None, "needs the published files: M.fetch_published()"
    keys = list(r)[:4] if isinstance(r, dict) else r
    print("%-24s %-9s %5.1fs  %s" % (e.name, status[:9], time.perf_counter() - t0, keys))'''),
md("## The result of one equation, formatted for the viewer"),
code('''print(mod.viewer_data("toy_library", {"location": 5}, "text")["text"])
print(mod.viewer_data("neighbour_statistics", {}, "text")["text"])'''),
])
print("written")
