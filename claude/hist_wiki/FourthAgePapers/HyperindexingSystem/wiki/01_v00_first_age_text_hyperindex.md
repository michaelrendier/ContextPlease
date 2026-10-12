# v00 · First Age text hyperindex

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Archive/ainulindale_first_age/FA_smnnip_hyperindex.py` (1,053 lines). Notebooks: [`v00_first_age/`](../notebooks/v00_first_age/).*

**Archive anchor (2026-10-02).** The claude.ai Project archive (artifact `SMNNIP Project Archive`, 51 files) carries `FA_smnnip_hyperindex.py` byte-identical to this file (38,734 bytes, sha256 `11ba64cc…472c7d`), and its `SMNNIP_TODO.txt` (Sections 7–8, "Added: 2026-04-16") already names `TextHyperIndex` and `MultiChannelTupper`. The classes therefore existed by 2026-04-16, two days before the git commit below.

**Dating.** In-file header: "April 2026 — First Age". Git: first commit 2026-04-18 (the clean initial commit of `PtolemyDesktop`, which imports every file at once; the commit date bounds the file, it does not date its writing).

## What it is

A text index and an image index sharing one tower, plus an append-only ledger. The text part is the earliest code in the repository that turns a string into an integer:

- `USKeyboardMap`: 97 symbols in the order `a–z A–Z 0–9 ! " # … ~ space tab newline` (index of `a` is 0, of space 94, of newline 96).
- `TextHyperIndex.encode_text`: base-97 mixed radix, `idx = idx·97 + index(char)`. `encode_fano`: the same loop over `index mod 7` (a path of octonion generators).
- `index_record(seq) → (text_index, fano_index, length)`.
- `BlockchainLedger`: SHA-256 chain, one block per training step, `.jsonl` plus `.chain`; `verify()` walks the chain.
- Also in the file, not covered here: a spherical colour system, a generalised multi-channel Tupper encoding for images, a polar Lagrangian wrapper, a sedenion-boundary guard.

## Measured (notebooks)

- The file's own `run_self_test()` passes 9 of 9.
- `encode_text("a"·k) = 0` for every k: the address is **not a bijection over strings**; `length` is part of the address.
- Fano index over the corpus sample: 1,908 distinct 4-character windows map to 1,061 Fano indices; up to 10 windows share one.
- Ledger: 3 blocks verify; editing block 1's `step` on disk makes `verify()` return `(False, 1, 'Chain broken at block 1: hash mismatch')`.

## Under permutation of the string

Order-sensitive (positional weights 97ᵏ). The Fano index keeps the order of the sequence but merges symbols congruent mod 7.

## Status

Ancestor. The charset order and the `(index, Fano index, length)` triple pass unchanged into the ValaQuenta module (v14). The bijective form (v01 onward) removes the need for `length`.
