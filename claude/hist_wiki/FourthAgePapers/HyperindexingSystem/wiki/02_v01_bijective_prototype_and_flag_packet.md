# v01 · Bijective base-N prototype and the flag-byte packet

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/infinite-data.py` (95 lines). Notebook: [`v01_flag_packet/`](../notebooks/v01_flag_packet/).*

**Dating.** Git: 2026-04-18 (initial commit). Its place before v02 is inferred from the code: the docstring reads "store data without needing a physical location behind a multilayered 256 bit", characters are looked up with `list.index` (later files use a dict), and its method names (`point_to_text`, `regenerate_text`) are the ones v02 keeps.

## What it is

- `HyperWebster`: **bijective** base-N (no zero digit): address = `Σ (index+1)·Nⁱ − 1`. Address 0 is the first character; addresses run in shortlex order over all strings. Charset: 97 symbols in keyboard-row order.
- `UniversalCoordinateSystem.decode_packet`: a 256-bit packet = **8-bit flag + 248-bit coordinate**. Flag 0 = text, 1 = bitmap ("indexing … on the XZ plane"), 2 = irrational-constant mode, otherwise undefined.

## Measured

- The file cannot be imported: it reads `PTOL_ROOT` (undefined) at module level. The notebook executes the classes above that line unchanged.
- `` ` `` → 0, `1` → 1, `` `1 `` → 98, `` `` `` → 97: the last one-character string plus one is the first two-character string. Round trips exact on 13-, 7- and 500-character samples.
- Capacity of the 248-bit coordinate: every string up to **37** characters fits, not all 38-character strings (log₂97 = 6.5999 bits/char gives 37.58 by division).
- `decode_packet` calls `text_engine.locate_text`, which the class does not have (`AttributeError`). Flags 1 and 2 return placeholder strings.

## Under permutation of the string

Bijective and order-sensitive. A transposition of two positions changes the address by a closed-form offset (checked in v04).

## Status

Prototype. The bijection, the API names and the 256-bit idea continue into v02; the flag byte does not appear again in the code base.
