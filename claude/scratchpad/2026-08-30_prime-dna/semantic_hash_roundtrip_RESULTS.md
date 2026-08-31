# Semantic / context hash — round trip against the live vocabulary

**2026-08-31 · Claude Sonnet 5.** Engine: `semantic_hash_roundtrip.py`
(+ `_steps56.txt` for the sampled parts). Store:
`VAPMIP/PtolC/monad3_c.bin` — version 1, **347 119 words**, 164 283 with a
β-field row, **146 743 carrying a stored 19-relation context vector**,
123 455 with phonetics.

Layers (Cody's model): letters = primes ≤ 71, words = composites, context =
primes > 71, held in **separate numbers**.

| # | test | result | verdict |
|---|---|---|---|
| 1 | `context_code(v)` → factor over CONTEXT_PRIMES → `v` | **146 743 / 146 743 = 100.000 %** | **lossless.** every stored vector factors back exactly; all CP-smooth (0 residue); largest code 98 bits |
| 2 | `context_addr = (code, next_prime(code), δ)`; `code = addr − δ` → `v` | **100.000 %** | the stored (addr, δ) pair recovers the code, hence the exact relation counts |
| 3 | `compress_count(c) = round(log₂(c+1))` — raw count → bucket | lossy **by design**; buckets: 2→[2‥4], 5→[22‥44], 8→[181‥361], 9→[362‥723]. Live: **91.9 % of slots = 0, 7.0 % = 1** (both exact, width 1); lossy buckets ≥2 hold **1.1 %**; max seen = 9 | **the only lossy step.** recovers the bucket not the raw count. Deliberate (keeps `tree.n.01` from a 364-digit code). Touches ~1 % of data — the hyponym-heavy synsets |
| 4 | γ fold: `\|γ\| = tanh(½ ln(log_code/ANCHOR))`, invert log_code | round-trip rel err **8.0 × 10⁻¹⁶**; **1 114 distinct log_code for 137 533 words, 0 collisions** | **lossless.** `log_code = Σ vᵢ ln pᵢ` is injective by unique factorisation of `∏ pᵢ^vᵢ`; float precision holds to 9 dp. `arg(γ)` carries the phonetic √SIGN (`record` vs `reCORD`) |
| 5 | `spelling_code(w)` (Gödel positional, `LETTER_PRIMES[i mod 20]`) → `w` | 30 k sample: **96.9 % for words ≤ 20 chars**; > 20 chars lossy (prime cycle wraps mod 20 → exponents add); ~3 % of ≤ 20 are non-ASCII letters (é, ñ → exponent > 26) | lossless for **ASCII words ≤ 20 chars ≈ 97 % of vocab**; the rest are the docstring's own "PROVISIONAL, not a locked design" gaps |
| 6 | `spelling_code(w) · context_code(v)`, factor, split at 71 → recover **both** | **800 / 800 = 100 %** | the "two numbers, not one" design holds exactly. `LETTER_PRIMES ≤ 71 ⟂ CONTEXT_PRIMES > 71`; the product never mixes the halves |
| x | stored 19-vec vs `context_vector(wn.synsets(w)[0])` today | 372 / 400 = **93 %** | store is substantially current; 7 % drift = a different synset was indexed, or nltk/WordNet version. A **freshness** note, not a round-trip failure |

## What this says about the model

- **The context / semantic layer round-trips exactly.** `context_code` and the
  `(addr, δ)` pair are 100 % invertible on all 146 743 live context-carrying
  words. The γ fold's magnitude is a **faithful scalar** — injective by unique
  factorisation, empirically zero collisions. **The semantic hash passes.**
- **The single lossy step is `compress_count`**, it is deliberate, and it
  touches ~1 % of the live data (only the high-degree hyponym relations).
  Everything downstream of the compressed vector is lossless.
- **The two-number separation is exact** (800/800). Word-number and
  context-number never contaminate each other — Cody's "keep the two
  distinguishable" is arithmetic, not aspiration.
- **The context space is heavily degenerate:** only **1 114 distinct relational
  shapes** across 146 743 words. That is *why* one real scalar is safe to fold
  to — there is very little to collide, and unique factorisation guarantees the
  rest.
- **The letters layer** (`spelling_code`) is lossless for ASCII ≤ 20 chars
  (~97 %); > 20 chars and non-ASCII are known provisional gaps — a positional
  base or a per-position distinct prime (drop the `mod 20`) closes them.

## Where it could land

ScalarContextPropagation desk-rejection gate **G1** ("lossless of what? show a
bit-exact round trip on real data") and **G2** (hash injectivity) — this is
that test, on 146 743 real entries: context layer 100 %, one documented lossy
compression step at ~1 % mass, separation 100 %.
