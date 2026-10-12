# v18 · The Blackjack subgroup F₂₁ as an indexer

*Claude Sonnet 5.5, 2026-09-29. Documents `VAPMIP/benchmarks/blackjack_vs_horner_bench.py` (164 lines). Notebook: [`v18_blackjack_f21/`](../notebooks/v18_blackjack_f21/).*

**Dating.** Git: **2026-09-25**.

## What it is

The question put to the benchmark: "how would the boxkite work instead of Horner-summing". F₂₁ = {x ↦ ax + b mod 7 : a ∈ {1, 2, 4}, b ∈ Z/7}, the normaliser of a Sylow-7 subgroup of PSL(2, 7), 21 permutations of 7 points. Two ways to use it are tested.

## Measured

- **Group check:** size 21, closed, every element has an inverse.
- **Composition.** Composing a word of group elements into a single element cannot be injective: only 21 results exist. The brute-force search finds the first collision at length 1 versus 2: the sequences `(0,)` and `(0, 0)` both compose to the identity permutation `(0, 1, 2, 3, 4, 5, 6)` (element 0 is the identity). That is the trivial collision; the pigeonhole bound guarantees others at every length.
- **21 elements as a digit alphabet** (lossless, since the digit sequence is kept), against base 97, exact round trips:

| chars | base-21 digits | bits | base-97 digits | bits | bits₂₁ ÷ bits₉₇ |
|---:|---:|---:|---:|---:|---:|
| 140 | 255 | 1,119 | 140 | 924 | 1.21 |
| 500 | 911 | 3,999 | 500 | 3,300 | 1.21 |
| 1,000 | 1,821 | 7,999 | 1,000 | 6,600 | 1.21 |
| 2,000 | 3,643 | 15,999 | 2,000 | 13,200 | 1.21 |

The base-21 numeral is built from the UTF-8 **bytes** of the text (8 bits per character), so its size is the raw size (1,119 bits for 140 characters); base 97 costs 6.6 bits per character. Encoding and decoding are also slower (more digits, an extra byte-to-base-21 step).

## Under permutation of the string

Composition in a group of order 21 forgets the order of most of a word; keeping the digits keeps it.

## Status

A recorded negative result: F₂₁ is not a viable replacement for Horner-summing as an exact per-chunk indexer. A smaller alphabet never shortens an exact address; it lengthens the digit string.
