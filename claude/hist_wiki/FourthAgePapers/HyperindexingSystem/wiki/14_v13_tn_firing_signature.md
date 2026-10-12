# v13 · Hyperindexing in T_N: the firing signature

*Claude Sonnet 5.5, 2026-09-29. Documents `VAPMIP/engines/e17_hyperindexing.py` (149 lines) and `VAPMIP/engines/_sedenion.py` (`project`). Notebooks: [`v13_tn_signature/`](../notebooks/v13_tn_signature/).*

**Dating.** Git: **2026-06-14**.

## What it is

A text is projected onto n prime-indexed dimensions, `project(text, k, primes) = Σᵢ byteᵢ · i^(−½) · cos(2πi/p_k)` (a Dirichlet sum at σ = ½), normalised; the **firing signature** is the permutation of the n dimensions sorted by |value|. The file's claim: "lossless hash in T_N when N ≥ data dimensions", tested by the collision rate of signatures at n = 8…128 on a corpus of ten sentences and by "index discriminability" at n = 16.

## Measured

- The file's own experiment, run as written: collision rate 0.000000 at every n from 8 to 128, "effectively injective at N = 8". The corpus is ten sentences of 23–44 characters (45 pairs). The mean pairwise cosine distance falls from 0.2595 (n = 8) to 0.0039 (n = 128): added dimensions bring the vectors closer together.
- **Exhaustive, every lowercase word of length ≤ 3 (18,278 words):** distinct signatures **7** at n = 4 and **8** at n = 8, 16 and 32; the largest class holds 14,702 words. At n = 8, `silent` and `hello` already share a signature.
- Random 25-character strings (2,000): 667 distinct signatures at n = 8, **1,862 at both n = 16 and n = 32**: doubling the dimensions from 16 to 32 adds nothing, and 138 strings still collide.

## Under permutation of the string

The address is itself a permutation (an argsort of n values), from a space of n! signatures, far larger than the 18,278 words tested. The map from string to signature is order-dependent (the weights i^(−½) differ per position) and many-to-one. The count of signatures is not the limit; the projection is.

## Status

Distinct: the only version whose address is a permutation. Its "lossless" claim holds for neither short words nor long sentences in this measurement; what the file measured is discrimination among ten long sentences.
