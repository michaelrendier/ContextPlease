# v19 · Midline index: the 4-digit code T S DD over 96 characters, base-96 packing, de Bruijn over 96 symbols

*Claude Sonnet 5.5, 2026-09-29; rules revised 2026-10-12. Documents `PtolemyDesktop/Archimedes/Maths/MidlineIndex.py`. Notebooks: [`v19_midline_index/`](../notebooks/v19_midline_index/).*

**Dating.** Git: **2026-09-27**. The file's header says the design was reconstructed from earlier conversations and that no earlier committed source was found.

## What it is

A character is one 4-digit decimal code **T S DD** = `type·1000 + sign·100 + step`.

| Slot | Values | Rule |
|---|---|---|
| T type | 0 Uppercase, 1 Lowercase, 2 Digit, 3 Punctuation | the group |
| S sign | letters: 0 toward A/a (the anchor `M`/`m` itself takes 0), 1 toward Z/z. Digits: always 0. Punctuation: 0 first half, 1 second half | side, or half |
| DD step | letters: distance from the anchor, 00–13. Digits: the digit, 00–09. Punctuation: index in the half, 00–16 | position |

The punctuation group is line feed, space and the 32 symbols (34 characters) in ASCII order, split evenly: half 0 is `LF`, space, ``!"#$%&'()*+,-./`` and half 1 is ``:;<=>?@[\]^_`{|}~``. Exactly **96** codes are valid (26 + 26 + 10 + 34); `decode_char` raises `ValueError` on any other. Tab is not a code: `normalise` turns it into four spaces. The valid codes are a hardcoded sorted list `VALID_CODES`, and a text is a **base-96 Horner integer** over each character's index in that list. It is exactly one `ASS` (Add:Scale:Sign) element applied to 1 for the letters. The file also carries an FKM **de Bruijn** sequence generator over the 96 valid codes, a **pointer pathway** over the 97-symbol keyboard (first pointer absolute, then deltas), and an `overhead_report`.

**History of the rules.** The 2026-09-27 version packed `type·28 + sign·14 + step` (K = 56) over `A–Z 0–9` with letter-or-digit as the first slot and case folded. On 2026-10-12 the first slot was restored to its original three values (Uppercase, Lowercase, Digit), punctuation became a fourth type, the digit sign was dropped (a `-` before a digit is two characters), then space, then line feed were added.

## Specification found in the Project archive (2026-10-02)

The claude.ai Project's `SMNNIP_TODO.txt`, Section 0 ("Delta encoding, deferred to between ages"), specifies a `DeltaEncoder`: each character becomes `(modifier_idx 0–6, base-13 step 0–D)` with the step `abs(cset.index(char) − cset.index('m'))`; the seven modifiers are lowercase negative / positive / origin, uppercase negative / positive / origin, and digit (literal digit follows). The specification is **case-aware**. The 2026-09-27 `MidlineIndex.py` packed `type·28 + sign·14 + step` (K = 56) over `A–Z 0–9` and **folded case**, so it did not meet the specification's case distinction. The 2026-10-12 version keeps case exact (separate Uppercase and Lowercase types, each anchored at its own `M`/`m`).

## Measured (2026-10-12, notebooks `v19_midline_index/`)

- Codes: `A` → 0012, `M` → 0000, `Z` → 0113, `a` → 1012, `m` → 1000, `z` → 1113, `0` → 2000, `5` → 2005, line feed → 3000, space → 3001, `!` → 3002, `/` → 3016, `:` → 3100, `~` → 3116; all 96 round-trip, and the other 9,904 four-digit numbers are rejected. `HELLO2026` → 36,671,429,080,540,282 → `HELLO2026`; `Hello, World -3!` → 2,904,025,772,685,498,955,121,040,377,056 and back, case intact.
- **Domain.** Case is exact (`hello` and `HeLLo` both round-trip). A tab becomes four spaces; carriage return and non-ASCII (`é`) raise. On the 4,000-character corpus sample (spaces, line feeds and all) the address is 26,340 bits = **6.585 bits/char** = log₂96, the minimum for 96 equally likely symbols, just under Horner-97's 6.600 and against 13.29 bits/char for the four decimal digits stored as written. The order T S DD is a fixed ordering of the 96 symbols, like any base-96 `.perm`: it does not change the size, only which characters sit near each other.
- **De Bruijn.** All 96 codes are valid, so K = 96 = the alphabet size. `verify_de_bruijn(2, k=96)`: length **9,216** (96²), all 9,216 cyclic 2-windows present exactly once; n = 3 gives 884,736 (96³), also exact.
- **Pathway.** `THIS` → `[45, −12, 1, 10]`, `hello` → `[7, −3, 7, 0, 3]`, `Ptolemy` → `[41, −22, −5, −3, −7, 8, 12]`, each reconstructing exactly. Over the corpus words the deltas lie in −86…86 (130 of a possible 193 values): a delta between two pointers is not bounded by 13; the bound in the letter encoding comes from the fixed anchor M. The pathway layer is unchanged by the 2026-10-12 revision.

## Under permutation of the string

Order-sensitive. The de Bruijn traversal orders all n-windows so each occurs once and neighbours differ by a one-symbol shift; it is the traversal used by v16 in place of a factorial tree.

## Status

Distinct: a per-character code with a small hard-bounded letter step, a hardcoded list of 96 valid codes, and the only generator of a de Bruijn sequence in this repository. With punctuation, space and line feed in the domain it covers ordinary text exactly and costs log₂96 bits per character. The 2026-09-27 trade of case and punctuation for a smaller per-character cost (5.807 bits) no longer applies. The pointer pathway remains experimental (see `Archimedes/Maths/MidlineIndex.py` header).
