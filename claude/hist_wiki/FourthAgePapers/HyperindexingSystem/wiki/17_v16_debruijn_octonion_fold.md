# v16 · de Bruijn traversal and the Cayley–Dickson fold to a fixed-width address

*Claude Sonnet 5.5, 2026-09-29. Documents branch `data-storage-no-location` of `FourthAgePapers`: `DataStorageNoLocation/{README.md, construction.json, engine/bench_tower.py, bench/*}` (local, not pushed). Notebook: [`v16_debruijn_octonion_fold/`](../notebooks/v16_debruijn_octonion_fold/).*

**Dating.** Branch commit **2026-08-30** (per `VAPMIP/benchmarks/hyperwebster_baseline_bench.py`'s reference to it). That paper is the sibling of this one; it folds the address down where this one keeps it exact.

## What it is

The branch README's construction: the traversal of the address space is a **de Bruijn sequence** (each length-n window once, so neighbouring addresses differ by one symbol shift instead of a walk down a factorial tree); each ingested item is a ledger row `(index, timestamp)`; the ledger is text and is indexed in turn, recursively; the octonion carries the recursion's depth so that the fold reaches 256 bits. `bench_tower.py` runs one document at each rung of the Cayley–Dickson tower ℝ → ℂ → ℍ → 𝕆 → 𝕊 and reports address, width, forward (Red) and backward (Blue) time and the divergence between them.

## Measured (the branch script, run unmodified via `git show`, on the 3,360-byte cover letter; total run 100 s)

| rung | algebra | dim | address bits | t_forward ms | t_backward ms | Red ≠ Blue | reversible |
|---:|:---:|---:|---:|---:|---:|---:|:---:|
| 0 | ℝ | 1 | 26,879 | 5.8 | 25.6 | 0 | yes |
| 1 | ℂ | 2 | 64 | 29.2 | 29.6 | 3.75e-15 | yes |
| 2 | ℍ | 4 | 64 | 160.8 | 159.8 | 1.02e-04 | yes |
| 3 | 𝕆 | 8 | 64 | 707.6 | 716.5 | 1.16e-04 | yes |
| 4 | 𝕊 | 16 | 64 | 3,007 | 4,037 | 1.18e-04 | yes |

Time per data size (this machine, 512 → 32,768 bytes): Horner 0.31 → 364 ms; ℂ 4.7 → 291 ms; ℍ 24 → 1,539 ms; 𝕆 107 → 8,319 ms; 𝕊 440 → 34,873 ms. Rung 0 is the raw bijection (26,879 bits for 3,360 bytes); rungs 1–4 give a **fixed 64-bit** address whatever the document length; cost grows with the rung, and Red ≠ Blue first becomes non-zero at ℍ.

The fold has 2⁶⁴ outputs against unboundedly many documents, so it identifies what was stored; it does not invert for arbitrary input. "Reversible" in the table is the script's own check.

## Under permutation of the string

The de Bruijn traversal orders windows so that consecutive addresses are related by a shift. v19's notebook verifies the property on the 36-symbol alphabet (each 2-window exactly once, length 36² = 1,296).

## Status

Distinct and successful as an engineering result on its own terms; the 256-bit root remains a construction with open gates in that paper. Not part of this paper's claim, which keeps the address exact.
