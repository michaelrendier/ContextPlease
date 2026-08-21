# 2026-08-19 — Calibration of the box-kite prime hash, and composites + context

## What was asked

Calibrate the new prime hashing algorithm; test the resulting generational
composites; then composites + context. Design notes toward filling a box kite
with context per word use, inside a 16-word sedenion window, in the refining
pass.

## Provenance of every number below

CALIBRATION tests the pipeline. RESULT tests a hypothesis, and only with its
control already run. Nothing here is SYNTHETIC — every corpus is real
(`/usr/share/dict/words`, 73,445 words; `crawford_thesis_clean.txt`, 68,241
tokens / 2,908 types).

## Files

| file | pass | what it does |
|---|---|---|
| `cal_01_ladder.py` | 1-3 | Fermat ladder, letter map, spell bijection, strut distribution |
| `cal_02_composites.py` | 4 | generational composites, parentage recovery, gcd as letter-LCA |
| `cal_03_context.py` | 5a-d | three prime ladders, box_kite as reducer, refining pass, the pencil |
| `cal_04_channels.py` | — | PPMI channel descent, control first |
| `cal_05_fixed_reducer.py` | — | cal_04 re-measured after its statistic proved invalid on gated data |

`.out` beside each is the captured run.

## What verified exactly (CALIBRATION)

- `F_n = 2^(2^n)+1` for n=0..3 → `[3,5,17,257]`; product `= 65535 = 2¹⁶−1`.
- 15 nonempty subsets = PG(3,2) points; 8 contain 257; 7 after removing the
  no-free-bit case. **The struts are counted, not assigned.**
- Spell bijection: 73,445 words → 73,445 distinct codes, **0 collisions**,
  `unspell` round-trip 73,445/73,445. 1,448 words exceed 13 letters and
  overflow uint64 — already flagged in `monad_identity.py`, not silently wrapped.
- **Composite parentage: 73,445/73,445 factor back to the exact letter
  multiset.** Largest composite 80 bits.
- **`gcd(comp a, comp b)` == componentwise-min letter multiset: 20,000/20,000.**
  One division. No tree walk, no search.
- The pencil: every one of the 15 XOR relations factors **exactly 7 ways**;
  105 incidences / 15 relations = 7. **One string → 7 strings is exact.**

## Three faults found

### 1. Three incompatible prime ladders in live code

| module | letters | context channel 0 |
|---|---|---|
| `lineage_hash.py` | 2..101 (cap 313) | **317** |
| `prime_hash.py` | 2..71 (cap 71) | **73** |
| `context_fill.py` | — | kite primes 2..17 |

- `prime_hash` context channels 0-5 = `{73,79,83,89,97,101}` = `lineage_hash`
  letters **`vkjxqz`**.
- `context_fill`'s 7 kite primes `{2,3,5,7,11,13,17}` = the letters **`etaoins`**.
- Channel index `c` means 317-based in one module and 73-based in the other, so
  an address written by one and read by the other decodes silently to different
  channels. `monad_identity.bin` is safe — it stores `letter_cap` in its header.

`prime_hash.py` is the outlier at 71. Its `LETTER_PRIMES` is also dead code —
`spell()` there uses base-26 letter indices, never the primes.

### 2. `box_kite()` is a degenerate reducer

Returns `None` for **991 words in two opposite classes**:

- **547 BELOW division** — alphabet `aeinost`, i.e. ETAOINS. Never reach the
  zero-divisor generation, so they have no kite.
- **444 PURE division** — alphabet `bcdfghjklmpqruvwxyz`. Reach division and
  have no free bits, so they sit at the kite origin.

Disjoint, exact complements, opposite ends of the annihilation gradient — and
one label for both. Codomain is 8 states where the state space has 9.

### 3. The letter→generation map is 73% one generation

Fermat bands are doubly exponential; the prime ladder is ~linear. So band 3
absorbs 19 of 26 letters:

    gen 0 ranking   2  (e t)
    gen 1 factors   1  (a)
    gen 2 GROUPING  4  (o i n s)
    gen 3 division 19  (everything else)

Measured consequence over 73,445 words: kites 5 and 7 hold **72%** of the
vocabulary. `H(box_kite) = 2.18` bits of a possible 3.00.

And the OR that makes the strut discards most of what the letters carry:
`H(profile) = 8.75` bits (1,544 distinct generation multisets) vs
`H(strut) = 2.21` bits (15 sets). **6.54 bits, 75%, thrown away at the
face-1 → face-3 handoff.**

## The context result (RESULT — control run first, on the identical pipeline)

`context_fill._kites_for` is a base-131 rolling hash over `word + context`,
bits 1..7. It is a placeholder, and it measures as one:

| kite map | real ctx | shuffled ctx | verdict |
|---|---|---|---|
| `hash` (current stub) | 0.1540 | 0.1545 | **no contextual signal at all** |
| `letters` (word's own strut) | 1.0000 | 1.0000 | context-blind by construction |
| `descent` on letter composites | 0.9956 | 0.9961 | **saturates** — gcd over 15 words keeps every common letter |

Both failures are the same method error from opposite directions: **letters
cannot supply a context channel.** `prime_hash.py`'s own docstring names it —
"addressing by spelling is provenance addressing" — and predicted the failure
before it was measured.

A channel map built from what a word *licenses* (top-8 PPMI associates,
distributional) does separate, decisively, on a paired per-word test:

    |shared| real-ctrl    mean +1.4644   611 words better /  47 worse   z = +21.99
    empty%   real-ctrl    mean -0.3843    33 words better / 575 worse   z = -21.98
    agreement real-ctrl   mean -0.0321   216 words better / 209 worse   z =  +0.34

**Connection: decisive. Stability: null.** The descent reliably says *whether*
a word binds to this window and how strongly, and does not produce a
reproducible channel set across occurrences.

That is a placement result, and it could have come out the other way: binding
is an ACTION (Mind's Eye), a stable address is POTENTIAL (Paper's Hands). The
measurement puts the fill in the Mind's Eye independently of the argument that
put it there.

### Cost — the bottleneck is not the arithmetic

    co-occurrence table, whole 68k corpus, one pass     0.36 s
    channel codes for 2,908 types (computed ONCE)       0.14 s
    refining pass, per 16-word sedenion window          0.45-0.58 ms
    whole thesis, 4,265 windows                         ~0.5 s

Against a 30 s budget that is ~60,000x headroom. Nothing here needs optimising;
the cost will be in the definition *fetch*, which does not exist yet.

## Two corrections made to my own method, mid-run

1. `cal_02` PASS 4e conflated the two `None` classes — the fault it was
   measuring was the fault it committed. Split in `cal_03` 5b.
2. `cal_04`'s coherence statistic took an argmax over readings 33.6% of which
   were the empty set, so the mode collapsed onto the gate and returned
   "control beats real" with confidence. Re-measured in `cal_05` with empties
   reported separately and a paired sign test.

## Generational lineage report

    operation          tier  descends from              status
    -----------------  ----  -------------------------  ---------------------------
    spell (Horner)      0    ADD, SCALE (positional)    bijective, verified
    comp (prime prod)   0    SCALE (commutative)        factors back, verified
    gcd                 0    ADD, SCALE, SIGN via       == letter LCA, verified
                             min(a,b)=(a+b-|a-b|)/2
    strut (OR of bits)  2    fixed set                  DERIVED
    box_kite            2    fixed set (strut & 7)      DERIVED — codomain short
    generation(p)       3    count of Fermat thresholds DERIVED
    pencil (XOR fact.)  0    ADD in char 2; count -> t3 DERIVED, exactly 7
    PPMI                 -   instrumentation, not a claimed geometry

**No new generator required.** Two section-5 signatures fired and both resolve
to method errors, not emergence:

- *fixed set of the wrong dimension* → `box_kite`'s 8-state codomain over a
  9-state space.
- *a collision that unpacks where the encoder should have made it impossible*
  → the ladder overlaps. By the encoder's own standard ("every collision is a
  method error, deductively") one occurrence is proof. There are 13.

## Open, for Cody

1. Which `LETTER_CAP` is canonical — 313 or 71? Everything downstream of the
   context ladder depends on it and the three modules disagree.
2. Does the strut keep the OR (2.21 bits) or move to the generation profile
   (8.75 bits)? The box kite is only 3 bits wide, so the profile needs a
   projection, not a widening.
3. The context channel map has **no data source**. WordNet dir is empty, nltk
   is ABI-broken against the installed numpy. Distributional channels work and
   need nothing installed.

---

# Addendum 2026-08-19 — "how is the prime ladder linear?" (`cal_06_zeno.py`)

Two objects were conflated in one sentence. Separated and measured:

**(1) The ladder** — `p_n ~ n ln n`. Measured `p_n/(n ln n)` = 2.00, 1.37, 1.26,
1.19, 1.19, 1.15 for n = 1,5,10,20,26,65. **Quasi-linear**, within ~1.2 across
the whole range. Cutting it at doubly-exponential Fermat thresholds is the
entire source of the 2/1/4/19 band lopsidedness. That claim stands.

**(2) The occupancy** — NOT linear, and Cody is right that this is where the
structure is. But it is not geometric either:

    'e' (prime 2)  P(v>=k)   0.6565  0.2203  0.0423  0.0038  0.0002
    random integer P(v>=k)   0.5000  0.2500  0.1250  0.0625  0.0312
    successive ratios, 'e'   0.336   0.192   0.090   0.047

A geometric law holds that ratio constant at 1/p = 0.5. It **falls**, so word
composites are **sub-geometric**: extinction is FASTER than Zeno, because a
word is finite (mean Omega 8.09) while an integer's valuation is unbounded.

And E[v] / random E[v] climbs with rank — e 0.92, a 2.55, i 6.96, s 11.27,
r 12.70. **The map assumes occupancy ~ 1/p; reality is Zipf ~ 1/rank.** Since
p_n ~ n ln n, 1/p_n decays faster than 1/n, so the mismatch grows with rank.
That is the real defect, and it is a mismatch of LAWS, not of linearity.

## Where the information actually goes

    encoding                          bits   classes   kept
    spell (Horner, ordered)         16.164     73445  100.0%
    valuation vector (multiset)     15.985     67460   98.9%
    support (which letters)         14.890     40711   92.1%
    generation profile               8.750      1544   54.1%
    strut (generation OR)            2.211        15   13.7%
    box kite                         2.184         8   13.5%

**Order costs 0.179 bits of 16.164 — 1.1%.** The central design decision of
`lineage_hash.py` (positional for faces 1-2 because "order matters", commutative
for face 3) buys 1.1% at the letter level, and pays for it by giving up gcd.
English has too few anagrams for spelling order to carry weight: 73,445 words
occupy 67,460 distinct multisets.

The two big losses are `support -> profile` (6.14 bits) and `profile -> strut`
(6.54 bits). **The letter -> generation collapse is where the information goes,
not the OR of the exponents.** Fixing the band widths matters more than
enriching the strut.
