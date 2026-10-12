# v09 · Callimachus v0.9: Unicode public charset, SHA label as primary key, SQLite

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/v09/` (`core/{charset,hyperwebster,lsh_datatype}.py`, `database/hyperdatabase.py`, `gallery/hypergallery.py`, `acquire/acquire.py`). Notebooks: [`v09_callimachus_v09/`](../notebooks/v09_callimachus_v09/).*

**Dating.** Git: **2026-05-02** (`4f708d8`).

## What it is

- `charset.py`: PUBLIC charset = Basic Latin printable (U+0020–U+007E, 95) + tab + newline = 97 symbols **in Unicode codepoint order** (`\t`, `\n`, space, `!`, …, `~`). PRIVATE = "a permutation of PUBLIC supplied as a permutation index (integer in [0, N!−1]) … generation/storage lives in Kryptos".
- `HyperWebster`: the v03 design. `IndexRecord(label, payload, length, timestamp)`; `label` = SHA-256 of the integer address (primary key), `payload` = the address in base N over the charset.
- `LSH_Datatype`: 12 spectral layers per word; layers 0–5 acquisition-only, 6–11 writable (`0x0FC0`); `first_encountered` immutable (raises `AttributeError`). The docstring lists as TODO a proof of the claim that the Horner bijection operator is self-adjoint.
- `HyperDatabase`: SQLite, `label` primary key, WAL journal.
- `HyperGallery`, `HyperIndex`: v05's classes over the new core; `HyperIndex.master_label` is the SHA-256 label of the JSON index.
- `acquire.py`: word acquisition from dictionary APIs (network; not run here).

## Measured

- `index("Hello, World!")` → label `41fdb0d8…`, length 13; exact round trips at 140, 1,000, 4,000 characters.
- Database: after one `put`, `exists` is true, `count = 1`, `count_incomplete = 1` (layers 6–11 empty). Writing `first_encountered` raises "immutable (Rabies Principle)"; writing layer 0 raises `PermissionError`; layer 7 accepts a value.
- **Three charset orders, three integers.** The same 97 symbols in keyboard-row order (v01–v08), Unicode order (this version) and `a–z A–Z 0–9 …` order (v00, v14) give `hello` → 2,937,323,952, 6,706,159,586 and 712,911,699. The permutation taking keyboard-row order to Unicode order has cycle type **[92, 3, 2]**, no fixed points, order 276. Word shards written by v08 use keyboard order and cannot be found by v09 addresses.
- `HyperGallery._pixels_to_int` carries a dead stub loop (`… if False else 1`); the image cache still keys on a prefix (here the first 32 values), so two images differing in the last pixel get the same label (`regenerate(b) == b` is false).
- **The Rabies trigger never fires.** `CREATE TRIGGER … BEFORE UPDATE OF first_encountered ON words`: the `words` table has columns `label, payload, length, indexed_at, metadata, incomplete` and no `first_encountered`. SQLite accepts the declaration; an `UPDATE` of `indexed_at` goes through (`'changed'`). `put`'s `ON CONFLICT … DO UPDATE` does not touch `indexed_at`, so in practice the timestamp is kept by that statement, not by the trigger.

## Under permutation of the string

Here the permutation is explicit: "the permutation (charset order) is the only variable" (docstring). PUBLIC is one fixed order that any party can reproduce; PRIVATE is a key. Which private construction that implies is examined in v10 and v15.

## Status

Successful and the design of record for storage: label as key, payload as content, Unicode order as the public standard.
