# v14 · ValaQuenta `hyperwebster`: Horner index + Fano path + SemanticWord

*Claude Sonnet 5.5, 2026-09-29. Documents `ValaQuenta/modules/hyperwebster/{maths,tools,manifest}.py` (version 0.111). Notebook: [`v14_valaquenta_module/`](../notebooks/v14_valaquenta_module/).*

**Dating.** Git: **2026-06-28**.

## What it is

The v00 construction as an engine module: `horner_encode/decode` (base 97, `a–z A–Z 0–9 …` order, length stored), `fano_encode/decode` (`index mod 7`), `SemanticWord(text)` holding both indices and a SHA-256 of the text, `monad_address(text, algebra)` (in `maths.py`, the Cayley–Dickson layer), and a `HyperWebsterModule` (formulary, run, viewer data). Its docstring: "The HyperWebster is a coordinate system, not a dictionary. Every word is an address."

## Measured

- `SemanticWord("hello")`: Horner index 623,460,239, Fano index 1,596, length 5, `verify()` true.
- `horner_encode("a")`, `("aa")`, `("aaa")` all 0: not a bijection over strings; the length is part of the address.
- An unknown character silently becomes symbol 0: `horner_encode("é") == horner_encode("a")`. The exact version (v02) raises `ValueError` instead.
- 206 distinct corpus words → 202 distinct Fano indices (largest class 2). Anagrams `listen`/`silent` differ under both indices (order is kept).

## Under permutation of the string

Order-sensitive; the length must travel with the address. The charset order differs from v01–v08 and v09 (see v09).

## Status

Successful as the packaged, documented form of v00 (Sphinx docs, manifest). It keeps v00's non-bijective form and adds silent folding of unknown characters.
