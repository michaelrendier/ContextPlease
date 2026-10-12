# v11 · Semantic address: surface form → Riemann-zero ordinal

*Claude Sonnet 5.5, 2026-09-29. Documents `SemanticWordEngine/hyperwebster.py` (506 lines). Notebook: [`v11_semantic_ordinal/`](../notebooks/v11_semantic_ordinal/).*

**Dating.** Git: **2026-05-12**. This is the "Hyperwebster" of the `hyperwebster` skill: not the exact bijection, a many-to-one map into a lexicon indexed by zero ordinal.

## What it is

`Lexicon` maps `(zero ordinal n, domain)` to surface forms and counts (`global_index`, `domain_index`). `_hash(text) → (mean token length, (Σ ord(c)) mod 360 / 360)`; `snap(t, zeros)` maps t ∈ [0, 1] to one of N zeros (`N_ZEROS = 200` in the file). "The same concept in different languages maps to the same (n, domain) address."

## Measured (first 50 zeros from `VAPMIP/monad.py`)

- `listen`, `silent`, `enlist`, `tinsel` all give `_hash = (6.0, 0.8194…)` and the same address (ordinal 41, γ = 124.2568); `Listen` differs (ordinal 37).
- 206 distinct corpus words → 149 distinct t values (at most 360 exist) → 48 of the 50 ordinals used, largest bucket 10.

## Under permutation of the string

`Σ ord` is unchanged by any permutation of the characters, so the address is **constant on every anagram class**: the opposite of the exact address of v02, which separates every string. Synonym-sharing is the intended many-to-one behaviour; anagram invariance is a side effect of the choice of a sum.

## Status

Distinct; kept separate in the paper from the exact address. Not a storage address: a lookup key into the zeros.
