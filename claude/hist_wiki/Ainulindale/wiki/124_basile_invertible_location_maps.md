# 124 — Basile: Invertible Location Maps

**Built 2026-09-30.** Follows [[09_hyperwebster_engine]] and [[16_semantic_word_engine]] (the ordered address) and the Library-of-Babel premise placed under the title of `FourthAgePapers/HyperindexingSystem`. Engine: `ValaQuenta/modules/basile/`. Every number below is computed there; the published files were read, not summarised.

---

## Origin

**Citation status (Cody, 2026-09-30):** the site `libraryofbabel.info` is the progenitor of the hyperindexing system (built against, no tag). Basile as its author, and his theory pages, repositories and algorithm, are `Post-Hoc:` (found 2026-09-29, after the code).

The instruction, 2026-09-30: use the algorithm that libraryofbabel.info uses as the jump-off point, lead into the Hyperwebster, and build "the Basile engine", with the full engine protocol for every engine Basile has published.

The paper's opening needed the actual algorithm, so the site was read. Its "Grains of Sand" page says only that the mechanism is an invertible pseudo-random number generator ("for any block of text, the program can work backwards to calculate its location") and that early attempts with Halton sequences failed because division made inversion impossible. The site links Basile's own repository, and there the recipe is written out.

## What is published

Jonathan Basile's public repositories (`librarianofbabel`), checked 2026-09-30:

- **`libraryofbabel.info-algo`** (CC BY-SA-NC, uploaded 2019-01-02). Not the text library: the README says the published algorithm is "significantly more efficient than the one I wrote for libraryofbabel.info" and belongs to the image library, **Babelia**. `PRNG` is `babelia.cpp` (location → a 640×416, 12-bit image), `imagesearch.cpp` is the inverse (image → location), `Euclid's Extended` is the modular-inverse helper. The README gives the recipe: an LCG `(a·p + c) mod m`, then four shift/XOR steps, inverted with `a⁻¹` and the shifts undone in reverse.
- **`LoB-API`**: a CC0 licence file; no code.
- **`LobThis`, `LoBThis-Firefox`**: browser extensions, a fork of another author's, five small files. The one request it makes is reproduced as data.
- **`newsometimesatdawn`, `Dezmediah-site`**: web sites.

So there is exactly one published engine, and it is not the text library's.

## What the engine does

`basile` implements the recipe **generically** (no published text or constant; the published files are CC BY-SA-NC and ValaQuenta is GPL-3.0-only), checks a small library exhaustively, and runs Basile's own engine on his own constants, read from a local copy at run time.

The ordered address of [[09_hyperwebster_engine]] and the scrambled address of Babel hold the same set of texts; they differ in order. In the ordered one a prefix is a place value and neighbouring pages are neighbouring integers (1.036 of 3 characters differ at the toy scale); in the scrambled one they are unrelated (2.910, against 2.897 for independent pages). Both are computed from the page and neither stores a table.

## What running the published constants showed

- `PRNG` and `imagesearch.cpp` share `m, c, maskone, masktwo`; `a · a⁻¹ ≡ 1 (mod m)`; the three masks are exact powers of two, so `% maskone` is a bit mask.
- **`m` is exactly `3^2,015,755`.** With `gcd(c, m) = 1` and `3 | a − 1` the Hull–Dobell conditions hold, so the published LCG alone is a single cycle of length `m`: on ℤ/3ᵏ an affine map with `a ≡ 1 (mod 3)` and `c` a unit is the 3-adic odometer. The shift/XOR steps are what break that single cycle.
- `m` has 3,194,897 bits; the image has 3,194,880. Seventeen bit positions of the transformed value are never read by the image. For sixteen of them, flipping the bit and inverting gives a **different location that shows the identical image**. An image is shown at about 6.95×10⁴ locations on average (`m / 2^3,194,880`), and the search returns one of them.
- `Euclid's Extended` is a template with empty `m` and `a` and a 25-entry array: it holds 23 divisions. Random 64-bit operands need about 36; the published `a` (1.6 million bits) would need on the order of 10⁶.
- The README advises `a` and `c` "fairly close to but less than m"; the published ones are about half the size of `m`.

## Honest boundaries

- Only the published source was read; the live image service was not observed.
- The text library's algorithm is not published and is not reproduced. The toy scrambler is this project's own realisation of the recipe.
- The multiplicity result is about the published code and its constants, not a claim about the site's behaviour.

## Links

Engineering page: `ValaQuenta/wiki/basile.md`. Toolbox: `ValaQuenta/wiki/toolbox/39_basile.md`. Notebooks: `ValaQuenta/notebooks/basile/`. The paper's opening (Listings 1 and 2, §1–§3): `FourthAgePapers/HyperindexingSystem/paper/00_sections_1_to_4_draft.md`. Local copy of the published files (not for redistribution): `Ainulindale/references/babel/`.
