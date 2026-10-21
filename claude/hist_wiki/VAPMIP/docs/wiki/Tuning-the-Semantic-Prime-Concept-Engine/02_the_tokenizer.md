# 02 — The tokenizer

**Job.** Text → tokens → the units that take slots. `SemPriCon/src/PtolC_unicode/{tokenizer.c, filter.c, unicode.c, unicode_tables.h}`; port `SemPriCon/tools/monad_pyu.py`.

## Rules (`tok_split`)
- A **word character** is a Unicode letter or combining mark (General_Category `L*`, `M*`), the apostrophe `'`, or U+2019 (read as `'`). Tables are generated from Python's `unicodedata` (Unicode 15.0.0, `tools/gen_unicode_tables.py`): behaviour does not depend on the C locale.
- Tokens are lower-cased code point by code point (simple one-to-one lower-case mappings only; `İ` stays `İ`).
- **Han:** every Han character (CJK Unified Ideograph blocks, extensions A–G, compatibility) is a token by itself. No word segmenter. A two-character word is two tokens; their adjacency is what the link table (A) learns.
- A token needs ≥ 2 code points (a Han character is one), and must not start with an apostrophe.
- Anything else (digits, punctuation, spaces, invalid UTF-8 bytes) ends a token.
- **Input is expected in NFC.** The engine does not normalise; the ingest step does.

## Sentence ends (`monad_learn_ex`)
`.` `!` `?` newline, `…` `‼` `⁇` `⁈` `⁉` `。` `！` `？` `．`.

## The filter (`token_accept`, prose rules)
Length ≤ 24 **code points**; no pure digits, UUIDs, `=`, `://`, hex strings, slashes, base-64-looking chunks, long all-caps; no trailing apostrophe. The **vowel gate** (≥ 1 vowel; ≥ 15 % for tokens of 6+ letters) applies **only to Latin-script tokens**; vowels include accented Latin vowels (`ä ö é ú …`). Han, Cyrillic, Greek, Arabic and other tokens skip it.

| text | tokens |
|---|---|
| `Hänen äänensä oli kaunis.` | hänen, äänensä, oli, kaunis |
| `我們喝水。你叫什麼名字？` | 我, 們, 喝, 水, 你, 叫, 什, 麼, 名, 字 |
| `ÉCOLE İstanbul Ünlü naïve` | école, İstanbul, ünlü, naïve |
| `Don’t stop — it’s ‘fine’… really‽` | don't, stop, it's, **fine'**, really |

## Known behaviour (specified, not endorsed)
- A word inside curly single quotes becomes `fine'` (U+2019 read as an apostrophe), which `token_accept` rejects: **it is lost**. The 2026-05 build lost words inside straight quotes the same way. Normalise quotes at ingest if it matters.
- `İ`, final sigma and other special lower-casings are not mapped.
- Non-NFC input is tokenised as given (a decomposed `ä` is `a` + a combining mark, a different address from `ä`).

**Check:** `monad_pyu.tok_split` against the binary: `tools/verify_unicode_against_c.py` (8 texts, six scripts).


## Language alphabets
With `-DALPHABET_ASCII95` a word is a run of `[A-Za-z']`; with `-DALPHABET_TABLE` a letter is any character of the language's alphabet (U+2019 counts as the apostrophe). Every other code point separates words. A Han character is a token by itself. See [09](09_the_test_bins.md).
