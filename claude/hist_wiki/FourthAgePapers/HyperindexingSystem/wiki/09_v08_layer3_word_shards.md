# v08 · Layer 3: word records filed under their own address

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/hyperwebster_layer3.py` (329 lines). Notebooks: [`v08_layer3_shards/`](../notebooks/v08_layer3_shards/).*

**Dating.** Git: **2026-04-24**, commit `3a5d7e6` ("Phase 2-5: … HyperWebster Layer3"). The first dated use of the v02 class.

## What it is

`HyperWebsterLayer3` drains a context buffer's eviction queue (`(word, timestamp, snippet)` tuples) into a directory store: `words_root/words_<first letter>/<address_hex>.json`, where `address_hex` is v02's `index_text(word)` address. One JSON record per word: `word`, `address_hex`, `length`, `shard`, `snippets` (≤ 8), `timestamps` (≤ 32), `first_encountered`, `hit_count`, `incomplete`. Writes are atomic (temp file, rename). The Rabies Principle: `first_encountered` is written once and never overwritten.

## Measured

- `sedenion` is filed at `words_s/0000…8603286d52cc3.json`, and that name equals `address_of("sedenion") + ".json"`. Three ingests of two words → 3 records written/updated; the second `sedenion` hit gives `hit_count = 2`, `first_encountered = 1000.0` (unchanged), 2 snippets.
- Eight different words (including `a`, `aa`, `Sedenion`, `sedenion␠`, `0`, `00`) give eight different filenames: **lookup is a computation, not a search**; within the 97 symbols no collision handling is needed because the address is a bijection.
- **Outside the charset** the address is `None` and the path falls back to `re.sub(r'[^\w]', '_', word)`. `naïve` keeps its spelling (Python's `\w` is Unicode-aware) and gets its own file, but `a€b` and `a£b` both become `a_b.json`: one file, `hit_count = 2`. The exact bijection covers only the 97 symbols.

## Under permutation of the string

The shard letter is the first symbol; the address encodes it again in its leading digit, so the shard directory repeats information the address already carries. (The "volume A without its initial letter" of the Vsauce presentation of the Hyperwebster would drop it; this store does not.)

## Status

Deployed use of the exact address as a filing key. The Unicode public charset of v09 is the later answer to the charset limit.
