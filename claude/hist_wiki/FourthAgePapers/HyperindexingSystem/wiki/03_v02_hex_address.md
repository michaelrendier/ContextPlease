# v02 · The 64-hex address `(address_hex, length, timestamp)`

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py` (215 lines). Notebook: [`v02_hex_address/`](../notebooks/v02_hex_address/).*

**Dating.** Git: 2026-04-18. First **dated** downstream use: `hyperwebster_layer3.py` imports it (2026-04-24). It is the class the VAPMIP baseline benchmark loads by path (2026-09-25) and the class every measurement in this paper uses.

## What it is

`HyperWebster(characters)`: bijective base-N, dictionary lookup per character, `point_to_text(text) → int`, `regenerate_text(int) → str`, `index_text(text) → (address_hex, length, ctime)`. The address is the integer written in hex, zero-padded to 64 digits ("256-bit"); longer strings give wider hex. `regenerate_from_address(hex, length)` checks the length on the way back.

## Measured (corpus sample, N = 97)

| chars | address bits | address / raw 8-bit | encode ms | decode ms |
|---:|---:|---:|---:|---:|
| 38 | 250 | 0.822 | 0.08 | 0.06 |
| 140 | 924 | 0.825 | 0.39 | 0.22 |
| 500 | 3,300 | 0.825 | 4.34 | 1.78 |
| 1,000 | 6,600 | 0.825 | 24.44 | 6.89 |
| 2,000 | 13,199 | 0.825 | 80.71 | 8.69 |
| 4,000 | 26,399 | 0.825 | 250.73 | 32.93 |

- Address / raw = log₂97 / 8 = 0.825 at every size: **the address is the string in another radix.**
- The "256-bit" width is a minimum. 38 characters fit (97³⁸ ≤ 2²⁵⁶ < 97³⁹); 39 give 65 hex digits, 200 give 330.
- Every round trip is exact.
- **Two loops, one address.** `point_to_text` computes `N ** i` for every position (`address += index * N**i`). A forward Horner loop (`address = address * N + index`) returns the identical integer with one small multiplication per character. Measured, same random strings, this machine:

| chars | `point_to_text` s | forward Horner s | ratio |
|---:|---:|---:|---:|
| 1,000 | 0.0095 | 0.0007 | 13 |
| 4,000 | 0.2762 | 0.0084 | 33 |
| 16,000 | 10.3623 | 0.1085 | 96 |

Fitted growth between 1,000 and 16,000 characters: about **n^2.5** for `point_to_text` (2.4–2.6 across runs), **n^1.8** for the forward loop. The forward form is the one used by v05's `HyperIndex`, v09 and the ValaQuenta module. The 4.7–5.3× per doubling recorded by the VAPMIP baseline benchmark, which runs this class, is the first exponent.
- The smoke-test in `__main__` references undefined `PTOL_ROOT`; the class is unaffected.

## Under permutation of the string

Bijective and order-sensitive: the rank of a string in shortlex order. Under a permutation π of the *charset* the address of a string becomes the public address of its relabelled string (v09, v10).

## Status

The shipping baseline. Later versions wrap it (v03 label, v04 limbs, v08 shards, v17 layers), replace its charset (v09), or measure it (v17, v18).
