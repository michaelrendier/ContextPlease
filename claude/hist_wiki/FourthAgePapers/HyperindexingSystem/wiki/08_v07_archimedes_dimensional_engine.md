# v07 · Archimedes dimensional engine

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster_archimedes.py` (631 lines). Notebooks: [`v07_archimedes/`](../notebooks/v07_archimedes/).*

**Dating.** Git: 2026-04-18. Placed after v06: it builds on the word-token idea of `VocabFactorizer` and carries only the `COMPONENT_BASE` constant of the limb class.

## What it is

Four estimators around the word-level address:
- `ArchimedesGeometry`: n-ball volume `π^(n/2)/Γ(n/2+1)` in log space, the fraction of the address cube that is "round", a dimensional scale factor between letter space and word space.
- `SVDDimensionReducer`: SVD of the bigram transition matrix; keeps the k most frequent characters.
- `DiscreteCalcShift`: "integration" (letters → word tokens) and "differentiation" (back). `integrate`/`differentiate` are the vocabulary factorization of v06.
- `BoundaryFilter`: entropy and frequency-deviation bounds that decide whether a text is inside the "readable basin".

## Measured

- **Geometry.** The unit n-ball volume peaks at n = **5.2569** (golden-section search). The file gives three statements of the peak: "n~5" (module docstring), "~4.93" (method docstring), and `2π − 1 = 5.2832` as the return value of `peak_dimension()`. log₁₀(ball/cube) at n = 97 is −67.03; `readable_fraction_estimate(1000)` = −632.1 (assumes 4.5 bits/char).
- **SVD.** On 2,000 characters: 43 of 64 dimensions kept (1.5×); the pipeline estimate is 13,230 → 1,187 bits (11.1×). The kept basis covers 97% of the text's characters, so the reduction is lossy; it is an estimate (`_estimate_total_savings`) and no encoder in the file uses it.
- **Boundary filter.** `zzz…` is outside (entropy 0, "too repetitive"); the corpus sample is inside (4.94); a string using every symbol once is outside (6.59 > 5.5, "too random/encrypted"). All three are valid strings with valid addresses.
- **Letter ↔ word shift.** Exact round trip: 200 chars → 26 tokens, vocabulary 25, reported 10.9×; 1,000 → 121, 97, 8.3×; 2,000 → 238, 171, 7.5×. As in v06, the reported factor omits the vocabulary.

## Under permutation of the string

`char_entropy` and `freq_deviation` are functions of the symbol counts only, so the boundary filter is **constant on each anagram class**: it prunes or keeps whole orbits. The SVD reducer uses bigrams and is order-sensitive.

## Status

Distinct: the only version that introduces geometric estimators. Nothing downstream imports it.
