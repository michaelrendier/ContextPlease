# v06 · Character manifold and vocabulary factorization

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster_manifold.py` (537 lines). Notebooks: [`v06_manifold/`](../notebooks/v06_manifold/).*

**Dating.** Git: 2026-04-18. Placed after v05 by the `VectorAddress` evidence (see v04, v05).

## What it is

- `CharacterManifold`: decomposes a string into **per-symbol position sub-addresses**. For symbol c occurring k times in a string of length L, the sub-address is the combinadic rank of its position set among the C(L, k) subsets. Only symbols present are active dimensions. `reconstruct` interleaves the position sets back.
- `VocabFactorizer`: tokenises into words and non-word spans, builds a local vocabulary, and addresses the **token-id sequence** in base V (vocabulary size) instead of the character sequence in base 97. `VocabAddress.bit_report` gives a "reduction factor".
- `HyperWebsterManifold`: both behind one API.

## Measured

**Manifold** (round trip exact at every size):

| L | naive bits (L·log₂97) | Σ sub-address bits | log₂ multinomial | active symbols |
|---:|---:|---:|---:|---:|
| 140 | 924 | 775 | 564 | 30 |
| 1,000 | 6,600 | 6,086 | 4,662 | 54 |
| 4,000 | 26,400 | 25,819 | 20,146 | 65 |

Each symbol's positions are ranked among all L positions, ignoring positions the other symbols already occupy, so the sum exceeds the number of distinct arrangements. The exact count is the multinomial L!/∏cₖ!.

**Vocabulary** (round trip exact; vocabulary and punctuation costed as text over the 97-symbol charset, an estimate):

| L | reported reduction | naive bits | token-address bits | + vocabulary | + punctuation | total | real ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 47 | 25.9× | 311 | 12 | 297 | 58 | 367 | 0.85 |
| 1,000 | 8.3× | 6,600 | 799 | 4,897 | 2,369 | 8,065 | 0.82 |
| 4,000 | 7.2× | 26,400 | 3,668 | 13,682 | 9,833 | 27,183 | 0.97 |

The reported factor counts only the token-sequence address; the vocabulary and the punctuation spans are needed to decode and are not in it.

**Exact form** (written in notebook 03; not in the repo): a string is an arrangement of a multiset; its address is the pair (count vector, rank among the distinct arrangements). All 30 arrangements of `aabbc` receive ranks 0…29. On the corpus sample: L=140 → 789 bits (0.854 of naive); L=1,000 → 5,126 (0.777); L=4,000 → 20,798 (0.788), round trips exact. This is the order-0 entropy of the text; it wins because the text is not uniform over 97 symbols.

## Under permutation of the string

This is the version that treats a string as a multiset arrangement. The manifold is an inexact (overcounting) form of the (count vector, rank) address of the anagram class.

## Status

Distinct. The exact multiset rank in notebook 03 is the corrected form of this version's manifold.
