# v17 · The layered (calendrical) index: baseline benchmark and layer inflation

*Claude Sonnet 5.5, 2026-09-29. Documents `VAPMIP/benchmarks/hyperwebster_baseline_bench.py` and the audit script `bench_layers2.py` (`ContextPlease/claude/scratchpad/2026-09-29_hyperwebster_overhead/`). Notebooks: [`v17_layered_index/`](../notebooks/v17_layered_index/).*

**Dating.** Baseline benchmark git: **2026-09-25**. Layer-inflation script: 2026-09-29.

## What it is

The claim of the paper's stub: a hierarchical day → month → year index that gives lossless conversational memory whose reconstruction cost "depends only on the size of the few index layers actually touched". Each layer is a small JSON text of child pointers, addressed with the same class (v02); decoding follows a fixed number of hops.

## Measured

**Baseline benchmark, run unmodified (this machine):** full 97-symbol charset, chars → address bits: 140 → 924, 500 → 3,300, 1,000 → 6,600, 2,000 → 13,200, 4,000 → 26,400; encode 0.69 → 364.6 ms, decode 0.33 → 34.2 ms. With a per-chunk minimal charset (33 symbols): 649 → 20,176 bits. Four-layer chunk/day/month/year reconstruction: **40.2 ms**, exact (56.9 ms in the 2026-09-25 log). The benchmark's text is one paragraph repeated to each size, so its minimal charset has about 33–35 symbols at every size. The encode column is `point_to_text` (about n^2.5); the forward Horner loop gives the same addresses about 13–96 times faster between 1,000 and 16,000 characters (page 03), so every time in this table is an upper bound for the address.

**Layer inflation** (corpus sample, 4,000 chars = 32,000 raw bits, chunk 200, 4 chunks/day, 5 days/month; every row restores the text exactly), address bits ÷ raw bits at chunk / day / month:

| layer format | charsets | chunk / day / month | top pointer ÷ raw |
|---|---|---|---:|
| shipped 97 symbols, JSON layers | 97 / 97 / 97 | 0.824 / 1.480 / **2.472** | 2.472 |
| per-layer restricted charset, JSON layers | 65 / 27 / 27 | 0.752 / 0.981 / 1.188 | 1.188 |
| restricted charset + compact (hex, `,` `;`) layers | 65 / 18 / 18 | 0.751 / 0.803 / **0.842** | 0.842 |

## Result

**Time per layer is flat; size per layer is not, unless the layer format is chosen for it.** With the shipped charset each layer multiplies the address by about 1.7 (the JSON overhead written in a 6.6-bit alphabet), so the top pointer is 2.5 times the corpus. Restricting the charset per layer and using a compact non-JSON layer format brings it below the raw size. Reconstruction time depends on the four hops, not on how much history exists.

## Under permutation of the string

Ordering the charset by frequency (audit variant A) changes nothing: the size of a bijective address is set by length and alphabet size; frequency order moves only the leading digits.

## Status

The version whose claim this paper states. The measurements above are its content.
