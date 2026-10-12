# v12 · Prime zero index: Horner base-95 → next prime → π(p)

*Claude Sonnet 5.5, 2026-09-29. Documents `VAPMIP/monad.py` (`_horner_hash`, `_next_prime`, `_word_zero_idx`). Notebook: [`v12_prime_zero_index/`](../notebooks/v12_prime_zero_index/).*

**Dating.** `monad.py` git: **2026-05-19**. `_word_zero_idx` byte-identical since commit `204c75d` (2026-05-27).

## What it is

`_horner_hash(w)`: `v = v·95 + max(0, ord(ch) − 32)`, returned as `abs(v)`. `_next_prime(v)`: reduce `v` modulo the prime cap + 1 (65,537), then the smallest prime ≥ that, clamped to [2, 65,537]. `_word_zero_idx(w)`: `π(p)` from a precomputed table, floored at 1: the index of the word's zero in [1, 6,543].

## Measured

- `a` → Horner 65 → prime 67 → zero index 19; `listen` → 594,091,334,983 → 2,879 → 417; `silent` → 648,249,864,469 → 761 → 135 (anagrams get different indices); `Listen` → 3,262.
- Exhaustive over every lowercase word of length ≤ 3 (18,278 words): **2,409 distinct zero indices**, largest bucket 34. By length: the 26 one-letter words use 7 indices, the 676 two-letter words 101, the 17,576 three-letter words 2,304.

Two things make it many-to-one: the round-up to the next prime (neighbouring integers share an index, even for single letters) and the reduction modulo the cap (a word of three or more characters already exceeds it).

## Under permutation of the string

Order-sensitive before the reduction (unlike v11's sum), then many-to-one. Cannot be inverted.

## Status

Successful as the Monad's spelling address: a lookup key into the zeros, deliberately lossy. Not a storage address.
