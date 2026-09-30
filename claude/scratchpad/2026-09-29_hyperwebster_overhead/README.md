# HyperWebster overhead benchmark (2026-09-29)
bench.py imports the shipping PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py unmodified; output in bench_output_2026-09-29.txt.

Findings:
1. Horner address = 0.82-0.825 of raw 8-bit size at EVERY chunk size and corpus (log2(97)=6.6 bits/char) -> 17.5% reduction, constant.
2. A 256-bit address holds at most 38 chars at N=97 -> chunking. A 38-char chunk costs 256 bits vs 304 raw = 15.8% saving; 32-char chunks cost MORE than raw (1.001).
3. Minimal charset per chunk incl. charset cost: worse than raw below ~500 chars, ~0.78 at 1000-4000 (5.5% better than full charset at 4000).
4. 8x32-bit octonion limb split of a 256-bit address is exact (round-trip True) but is a re-coordinatisation, no reduction.
5. zlib/lzma on the same chunks: zlib 0.39 of raw at 1000-char chunks, 0.32 at 4000 -> ordinary compressors beat HyperWebster on size by far.
6. Wiki Layer 4/8 claim "frequency sorting saves ~5-6 decimal digits at length 8": measured 16.00 -> 15.35 digits (0.65) at N=97; the ~5 digit saving (16.00 -> 10.85) comes from restricting the charset to letters (N=23), not from ordering (n=263 words).
7. All round trips exact.
8. The 97% is not reproducible from the shipping code. The 256-bit root (branch data-storage-no-location, D7) is unbuilt and pigeonhole-limited: 2^256 outputs cannot losslessly encode arbitrary corpora; a Merkle-type root identifies stored leaves.

9. bench_layers.py (layered calendrical hyperindex exactly as Cody described: chunk entries {address,length,timestamp} -> JSON 'day' -> JSON 'month' -> top): restore by date exact, BUT each layer up inflates: address totals 0.82x -> 1.42-1.48x -> 2.37-2.50x the raw corpus (hex text re-indexed at 6.6 bits/char = ~1.65x per layer). A 256-bit top pointer would need a top JSON of <=38 chars. Prediction (UNTESTED): indexing the JSON layers in a minimal charset would cut per-layer inflation toward ~1.08x; it cannot go below 1.0.
10. PtolemyDesktop wiki/HyperWebster.md, docs/HYPERWEBSTER.md, README.md row 4 corrected (Layer 4/6/8 digit claims) 2026-09-29.

Open: the defensible reading of the reduction is per-instantiation payload (pointer + length vs replayed corpus); needs S = size of the JSON the Drive pointer indexed.

## Minimal-charset layering (bench_layers2.py, output bench_layers2_output_2026-09-29.txt)
Layer-wide charset per layer; restore exact in every mode. Top pointer as x raw corpus (4000 / 8000 chars):
- M0 shipped 97: 2.47 / 2.36 (per-layer growth 1.73 / 1.69)
- A freq-ordered 97: 2.47 / 2.36 -> frequency ordering alone changes NOTHING (leading-digit effect only)
- B restricted to chars present: chunk layer 0.752 / 0.792 raw; top 1.19 / 1.18 (growth 1.26 / 1.22); also ~4x faster (smaller ints)
- A+B: same as B
- A+B compact (hex digits + , ; separators, numeric labels, NOT JSON): top 0.84 / 0.87, growth 1.06 / 1.05 (floor ~1.0)
- listing the charset explicitly (8 bits/symbol/layer) adds 1.7-3%
No .perm files exist on disk. Standardised charset = PtolemyDesktop/Callimachus/v09/core/charset.py: PUBLIC = 97 symbols, Unicode order; PRIVATE = permutation index in [0,N!-1] supplied by Kryptos ("when Kryptos is live ... .perm files" per wiki/05, Pharos/FaceIdentity.py) -- planned, not present.
## Vsauce Banach-Tarski transcript (sites.google.com/site/vsaucetranscripts/scripts/the-banach-tarski-paradox; quotes as returned by the fetch tool)
"Ian Stewart famously proposed a brilliant dictionary. One that he called the Hyperwebster. The Hyperwebster lists every single possible word of any length formed from the 26 letters in the English alphabet." / "If they put all the words that begin with a in a volume titled "A," they wouldn't have to print the initial "a."" / "What if we turned an object, a 3D thing into a Hyperwebster?" / "...name the point we land on after the sequence that brought us there, we can name a countably infinite set of points on the surface." Origin of the term: Ian Stewart, From Here to Infinity (1996), per web search (not yet checked against the book).
