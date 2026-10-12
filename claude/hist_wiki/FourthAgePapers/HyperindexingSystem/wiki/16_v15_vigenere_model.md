# v15 · The reference model: Vigenère, and sorted rotations

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Kryptos/Ciphers/Vigenere.py` and `PtolemyDesktop/Kryptos/analysis.py`. Notebooks: [`v15_vigenere_model/`](../notebooks/v15_vigenere_model/).*

**Dating.** `Vigenere.py` git: **2026-08-25**, after the addressing versions; it is the model they are read against, not one of their ancestors. Source of the model: Singh, *The Code Book* (built against).

## What it is

- `Vigenere.py`: `encrypt`/`decrypt` on the 26-letter alphabet, and `quaternion_trace`, which returns for each ciphertext letter the record `(w | line i, position on line j, key letter k)`: w is the observable, `(i, j, k)` the generative coordinates. The file states the limit: one letter cannot recover three unknowns; the way back needs the key.
- `analysis.py`: `kasiski`, `index_of_coincidence`, `ioc_by_period`, `vigenere_key_from_period`, `break_vigenere`, `pattern_signature`, `dictionary_attack`.

## Measured

- `encrypt("ATTACKATDAWN", "LEMON") = LXFOPVEFRNHR`.
- The tabula recta is the cyclic group Z₂₆ acting on the alphabet: all 26 rows are permutations and `row(a)∘row(b) = row(a+b)` for all 676 pairs. Embedding Z₂₆ as the 26th roots of unity, a Caesar shift by k is multiplication by e^(2πik/26).
- **Breaking it.** On the corpus letters (3,085, IoC 0.0636): key `LEMON` → ciphertext IoC 0.0412, period 5, key and plaintext recovered exactly. Key `HYPERINDEX` (length 10) → period **2**, key `RE`, plaintext wrong. Kasiski votes: 2 → 2,017; 5 → 1,985; 10 → 1,950. `break_vigenere` takes the top-voted factor; every gap between repeats is a multiple of 10 and so also of 2. With the true period, `vigenere_key_from_period(ct, 10)` returns `HYPERINDEX`. The breaker fails on keys whose length has small factors.
- **Substitution keeps the pattern.** A private charset (v10) applied to an address is a per-symbol relabelling of its digits. On the corpus sample all 304 whitespace-delimited words have an identical repeat pattern before and after relabelling (word boundaries taken from the plaintext). In a dictionary of 167 distinct words of length ≥ 4, 97 of 109 patterns pick out a single word: the attack of al-Kindi.
- **Sorted rotations (Burrows–Wheeler, SRC-RR-124, read in full).** The N rotations of a string are the rows of a tabula recta laid over it. Sorted and reduced to the last column: `bwt("abraca")` → `L = "caraab"`, `I = 1`, the paper's own example; the inverse returns `abraca`; 200 random strings round-trip. The transform is a permutation of the input plus one index.

## Under permutation of the string

The Vigenère cipher applies a position-dependent rotation to the symbols; the address applies a fixed one (the charset order). A private charset is the fixed case, which is why it falls to statistics on the digits. A position-dependent relabelling is the Vigenère case.

## Status

The model. The rotations, the group and the breaking tools bound what a permutation-keyed address can promise.
