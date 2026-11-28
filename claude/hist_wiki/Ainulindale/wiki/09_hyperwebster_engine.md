# 09 — HyperWebster Engine (Horner and Fano addresses)

| | |
|---|---|
| Module | `hyperwebster` — `ValaQuenta/modules/hyperwebster/` |
| Class | `HyperWebsterModule` |
| Version | 0.111 |
| Confidence floor | THEORETICAL |
| API page | `ValaQuenta/wiki/hyperwebster.md` |
| Notebook | `ValaQuenta/notebooks/core/09_hyperwebster.ipynb` |
| Last verified | 2026-11-13, against the live registry (6 equations) and by running Listings 1–2 |

## 1. What it is

A coordinate system for text. A string is mapped to two integers: a
**Horner address** (the string, read as a number in base 97) and a **Fano
address** (the string's path through the seven octonion generators, read as a
number in base 7). No pointers and no dictionary: the address is computed from
the characters.

This is the earliest form of the address idea. The later engines `basile`
(Library of Babel addressing), `add_scale_sign` and the `monad` word-to-zero
mapping extend it; see [107](107_add_scale_sign_datatype.md),
[124](124_basile_invertible_location_maps.md) and [15](15_the_monad.md).

## 2. The character map

`US_KEYBOARD_CHARS` has exactly 97 characters, asserted at import:

| Group | Count |
|---|---|
| a–z | 26 |
| A–Z | 26 |
| 0–9 | 10 |
| punctuation `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~` | 32 |
| space, tab, newline | 3 |

Index 0 is `a`. `VOCAB_BASE = 97`, `FANO_BASE = 7`.

## 3. The two addresses

**Listing 1 — Horner address** (`modules/hyperwebster/maths.py`, `horner_encode`;
extracted: docstring removed, the character map and `char_to_idx` inlined,
runs cold)

```python
CHARS = ('abcdefghijklmnopqrstuvwxyz' 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
         '0123456789' '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' ' \t\n')
IDX = {c: i for i, c in enumerate(CHARS)}

def horner_encode(sequence):
    idx = 0
    for char in sequence:
        idx = idx * 97 + IDX.get(char, 0)
    return idx

print(horner_encode('hello'))
```

```
623460239
```

**Listing 2 — Fano address** (`fano_encode`; same extraction conventions)

```python
CHARS = ('abcdefghijklmnopqrstuvwxyz' 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
         '0123456789' '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' ' \t\n')
IDX = {c: i for i, c in enumerate(CHARS)}

def fano_encode(sequence):
    idx = 0
    for char in sequence:
        idx = idx * 7 + IDX.get(char, 0) % 7
    return idx

print(fano_encode('hello'))
```

```
1596
```

Both are first-character-most-significant. The generator sequence for
`hello` is [0, 4, 4, 4, 0], and 0·7⁴ + 4·7³ + 4·7² + 4·7 + 0 = 1596.

## 4. Exact properties

These were checked by running the code; they correct earlier wording.

| Property | Holds? | Evidence |
|---|---|---|
| `horner_decode(horner_encode(s), len(s)) == s` for s in the 97-character map | Yes, for a **known length** | `hello` round-trips |
| The Horner address identifies the string | **No, across lengths.** `a` is index 0, so leading `a`s vanish: `horner_encode('a') == horner_encode('aa') == 0`. The length must travel with the address | verified |
| Characters outside the map are rejected | **No.** They map to index 0: `horner_encode('é') == horner_encode('a') == 0` | verified |
| The Fano address is invertible | **No.** It is many-to-one (97 characters onto 7 generators): `fano_encode('hello') == fano_encode('aeeea') == 1596`. `fano_path_to_word` returns the canonical representative `aeeea` | verified |
| Arbitrary length | Yes, Python `int` | — |

The Fano address is therefore a path address (which generators were
traversed), not a string address. The Horner address plus the length is the
string address.

## 5. Objects

`SemanticWord(text)` carries `.horner_idx`, `.fano_idx`, `.length` and a
SHA-256 `_hash`; `.fano_generators()` returns the generator list and `.verify()`
re-decodes. `HyperGallery` navigates a set of such words (consecutive
Horner addresses, Fano-distance neighbours). `address_range('hello', 3)`
returns `hello`, `hellp`, `hellq` at Horner addresses 623460239, …240, …241.

`monad_address` distributes the Horner index over the tower dimensions
(ℝ, ℂ, ℍ, 𝕆). It is the scaffold for the "Tongue" (output reverse lookup);
the Tongue itself is not built here. See [12](12_smnnip_distribution_engine.md).

## 6. Equations

| Name | Tier | Parameters |
|---|---|---|
| `horner_encode` | ESTABLISHED | `text` |
| `fano_encode` | ESTABLISHED | `text` |
| `semantic_word` | THEORETICAL | `text` |
| `monad_address` | THEORETICAL | `text`, `algebra` |
| `address_range` | ESTABLISHED | `text`, `n` |
| `fano_path` | THEORETICAL | `text` |

## 7. Session

```
>>> registry.run('hyperwebster.horner_encode', {'text': 'hello'})
{'text': 'hello', 'horner_idx': 623460239, 'length': 5, 'verify': True}
>>> registry.run('hyperwebster.fano_encode', {'text': 'hello'})
{'text': 'hello', 'fano_idx': 1596, 'generators': [0, 4, 4, 4, 0], 'length': 5}
```

Console commands: `hw(text)`, `horner(text)`, `fano(text)`, `monad(text)`.

## 8. Related pages

[15 The Monad](15_the_monad.md) · [16 Semantic word engine](16_semantic_word_engine.md) ·
[124 Basile](124_basile_invertible_location_maps.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md)
