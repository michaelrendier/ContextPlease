# 124 — Basile: Invertible Location Maps

| | |
|---|---|
| Scope | the published algorithm of Jonathan Basile's image library (Babelia) as an invertible location map: its recipe, the arithmetic of its published constants, and what running them showed; its relation to the ordered address of the Hyperwebster |
| Built | 2026-09-30; follows [09](09_hyperwebster_engine.md) and [16](16_semantic_word_engine.md) (the ordered address) and the Library-of-Babel premise under the title of `FourthAgePapers/HyperindexingSystem` |
| Engine | `ValaQuenta/modules/basile/`; engineering page `ValaQuenta/wiki/basile.md`; toolbox `ValaQuenta/wiki/toolbox/39_basile.md`; notebooks `ValaQuenta/notebooks/basile/`; the paper's opening (Listings 1 and 2, §1–§3): `FourthAgePapers/HyperindexingSystem/paper/00_sections_1_to_4_draft.md`; local copy of the published files (not for redistribution): `Ainulindale/references/babel/` |
| Citation status | the author, 2026-09-30: the site `libraryofbabel.info` is the progenitor of the hyperindexing system (built against, no tag); Basile as its author, and his theory pages, repositories and algorithm, are **Post-Hoc** (found 2026-09-29, after the code) |
| Confidence | the arithmetic of the published constants: ESTABLISHED (re-run, Listing 1) · the structure of the recipe: as read from the published files (not re-read in this pass) · the toy-scale address statistics (§3): recorded |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The local copy of the repository files and the engine were not re-read |

## 1. Origin

The instruction, 2026-09-30: use the algorithm that libraryofbabel.info uses as the jump-off point, lead into the Hyperwebster, and build "the Basile engine", with the full engine protocol for every engine Basile has published. The paper's opening needed the actual algorithm, so the site was read. Its "Grains of Sand" page says only that the mechanism is an invertible pseudo-random number generator ("for any block of text, the program can work backwards to calculate its location") and that early attempts with Halton sequences failed because division made inversion impossible. The site links Basile's own repository,
where the recipe is written out.

## 2. What is published  (checked 2026-09-30)

Basile's public repositories (`librarianofbabel`):

- **`libraryofbabel.info-algo`** (CC BY-SA-NC, uploaded 2019-01-02): *not* the text library. The README says the published algorithm is "significantly more efficient than the one I wrote for libraryofbabel.info" and belongs to the image library, **Babelia**. `PRNG` is `babelia.cpp` (location → a 640×416, 12-bit image), `imagesearch.cpp` is the inverse (image → location), and `Euclid's Extended` is the modular-inverse helper. The README's recipe: a linear congruential generator (a·p + c) mod m, then four shift/XOR steps, inverted with a⁻¹ and the shifts undone in reverse.
- **`LoB-API`**: a CC0 licence file; no code. **`LobThis`, `LoBThis-Firefox`**: browser extensions, a fork of another author's, five small files (the one request they make is reproduced as data). **`newsometimesatdawn`, `Dezmediah-site`**: web sites.

So there is exactly one published engine, and it is not the text library's.

## 3. What the engine does

`basile` implements the recipe **generically** (no published text or constant; the published files are CC BY-SA-NC and ValaQuenta is GPL-3.0-only), checks a small library exhaustively, and runs Basile's own engine on his own constants, read from a local copy at run time. The ordered address of [09](09_hyperwebster_engine.md) and the scrambled address of Babel hold the same set of texts and differ in order. In the ordered one a prefix is a place value and neighbouring pages are neighbouring integers (recorded: 1.036 of 3 characters differ at the toy scale); in the scrambled one they are unrelated (2.910, against 2.897 for independent pages). Both are computed from the page and neither stores a table. (The toy-scale
figures are the engine's recorded output and were not re-run.)

## 4. What running the published constants showed

- `PRNG` and `imagesearch.cpp` share m, c, maskone, masktwo; a·a⁻¹ ≡ 1 (mod m); the three masks are exact powers of two, so `% maskone` is a bit mask.
- **m is exactly 3^2,015,755.** With gcd(c, m) = 1 and 3 | a − 1 the Hull–Dobell conditions hold, so the published LCG alone is a single cycle of length m: on ℤ/3ᵏ an affine map with a ≡ 1 (mod 3) and c a unit is the 3-adic odometer. The shift/XOR steps are what break that single cycle. (Listing 1 checks the single-cycle statement on ℤ/3ᵏ for k = 1…8.)
- m has **3,194,897 bits**; the image has **3,194,880** (640 × 416 × 12). Seventeen bit positions of the transformed value are never read by the image; for sixteen of them, flipping the bit and inverting gives a different location that shows the **identical image**. An image is shown at about **6.95×10⁴** locations on average (m/2^3,194,880 = 2^16.0856), and the search returns one of them.
- `Euclid's Extended` is a template with empty m and a and a 25-entry array: it holds 23 divisions. Random 64-bit operands need about 36; the published a (1.6 million bits) would need on the order of 10⁶.
- The README advises a and c "fairly close to but less than m"; the published ones are about half the size of m.

**Listing 1 — the arithmetic of the published constants, and the single-cycle statement** (written for this page; python3 standard library; runs cold)

```python
import math, random
from decimal import Decimal, getcontext
getcontext().prec = 40
k = 2015755; bits_m = Decimal(k) * Decimal(3).ln() / Decimal(2).ln()
img = 640 * 416 * 12
print('log2(3^2015755) = %s  -> %d bits' % (str(bits_m)[:16], int(bits_m) + 1))
print('image bits 640*416*12 = %d ; bits of m not read by the image = %d' % (img, int(bits_m) + 1 - img))
mult = bits_m - img; print('locations per image m / 2^%d = 2^%s = %.3e' % (img, str(mult)[:7], float(Decimal(2) ** mult)))
print('average Euclid steps for a random operand of b bits ~ (12 ln2 / pi^2) ln n = 0.8428 ln n: 64-bit -> %.1f ; 1.6M-bit -> %.3e' % (0.8428 * 64 * math.log(2), 0.8428 * 1.6e6 * math.log(2)))
print('published a ~ half the size of m: 1.6e6 / 3.19e6 = %.2f' % (1.6e6 / 3.194897e6))
random.seed(2); ok = True
for kk in range(1, 9):
    m = 3 ** kk
    for _ in range(5):
        a = 1 + 3 * random.randrange(1, 3 ** (kk - 1) + 1) if kk > 1 else 1 + 3 * 0; c = random.choice([x for x in range(1, m) if x % 3])
        x, seen = 0, set()
        while x not in seen: seen.add(x); x = (a * x + c) % m
        ok &= (len(seen) == m)
print('LCG x -> a x + c mod 3^k with a = 1 (mod 3), c a unit: a single cycle of length 3^k for every case tested, k = 1..8:', ok)
```

```
log2(3^2015755) = 3194896.08564117  -> 3194897 bits
image bits 640*416*12 = 3194880 ; bits of m not read by the image = 17
locations per image m / 2^3194880 = 2^16.0856 = 6.954e+04
average Euclid steps for a random operand of b bits ~ (12 ln2 / pi^2) ln n = 0.8428 ln n: 64-bit -> 37.4 ; 1.6M-bit -> 9.347e+05
published a ~ half the size of m: 1.6e6 / 3.19e6 = 0.50
LCG x -> a x + c mod 3^k with a = 1 (mod 3), c a unit: a single cycle of length 3^k for every case tested, k = 1..8: True
```

Reproduced: the 3,194,897 bits, the 17 unread positions, the 6.95×10⁴ locations per image, and (to the accuracy of the average-step formula) the "about 36" Euclid steps for 64-bit operands (37.4 predicted) and "the order of 10⁶" for the 1.6-million-bit a (9.3×10⁵); the single-cycle (odometer) statement holds in every small case tested.

## 5. Honest boundaries (kept)

- Only the published source was read; the live image service was not observed.
- The text library's algorithm is not published and is not reproduced; the toy scrambler is this project's own realisation of the recipe.
- The multiplicity result is about the published code and its constants, not a claim about the site's behaviour.

## 6. Related pages

[09](09_hyperwebster_engine.md) · [16](16_semantic_word_engine.md) · [57](57_boundary_ascending.md) (the many-to-one hash and the word-index map) · [98](98_provenance_and_citations.md)
