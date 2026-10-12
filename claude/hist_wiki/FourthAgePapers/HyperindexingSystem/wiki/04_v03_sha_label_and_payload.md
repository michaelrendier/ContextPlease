# v03 · SHA-256 label + base-N payload

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster-hash.py` (214 lines). Notebook: [`v03_sha_label/`](../notebooks/v03_sha_label/).*

**Dating.** Git: 2026-04-18. Placed after v02 by the code: its docstring answers the width problem ("an 11,000-char file sits at a ~73,000-bit integer … to keep addresses a *fixed* 64 characters we split the concept in two"), and its internal names (`_str_to_int`, `IndexRecord(label, payload, length, timestamp)`) are the ones v09 keeps.

## What it is

- `label` = SHA-256 of the integer address: always 64 hex characters; the stable lookup key.
- `payload` = the integer address written as a base-N string over the same charset: what regeneration needs.
- `IndexRecord(label, payload, length, timestamp)`; `regenerate(payload, length)`.

## Measured

| chars | label chars | payload chars | payload / raw (8 bits per stored char) |
|---:|---:|---:|---:|
| 140 | 64 | 140 | 1.000 |
| 1,000 | 64 | 1,000 | 1.000 |
| 4,000 | 64 | 4,000 | 1.000 |

- The label is fixed width. The payload has **as many characters as the text**: a fixed-width key was added in front of an address that still grows with the input.
- The label regenerates nothing. Passed to `regenerate` as a payload it raises a length error; with its own length supplied it decodes to an unrelated 64-character string without complaint.

## Under permutation of the string

The label is a hash of a bijective address, so it separates every string but cannot be inverted; the payload is the v02 address.

## Status

The label-as-key / payload split is the scheme v09 adopts as its primary-key design.
