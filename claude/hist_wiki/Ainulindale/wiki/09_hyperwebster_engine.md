# 09 — HYPERWEBSTER ENGINE  Horner Bijection

**Module:** `hyperwebster`  **Version:** 0.111  **Confidence floor:** THEORETICAL

## Philosophy

The HyperWebster is a coordinate system, not a dictionary. Every word is an address. Every address is exact. No pointers — coordinates.

**"Ptolemy speaks because he knows."** Recognition, not construction. The Tongue performs reverse lookup from attractor coordinates to nearest SemanticWord. It does not assemble tokens.

## Character Map

Fixed US keyboard charset: 97 characters (a-z, A-Z, 0-9, punctuation, space, tab, newline). Bijection to integers 0..96. Built once at import time. Immutable.

## Horner Bijection (base-97)

```
idx = c₀·97^{k-1} + c₁·97^{k-2} + ... + c_{k-1}·97^0
```

- Lossless. Invertible. Any length.
- Pure Python `int` — arbitrary precision, no overflow.
- Two strings are the same if and only if their Horner indices are equal.

Round-trip: `decode(encode(text), len(text)) == text` always holds.

## Fano Index (base-7)

```
fano_idx = Σ_k (char_k % 7) · 7^{k}
```

Each character maps to one of 7 octonion generators: `char_idx % 7 → e_1..e_7`.

This is the algebra-native address: it encodes which octonion generators were traversed, not which characters. Different from the Horner index.

## SemanticWord

```python
SemanticWord(text)
  .horner_idx    # base-97 integer address
  .fano_idx      # base-7 octonion path address
  .fano_generators()  # list of generator indices
  .verify()      # round-trip check
```

## HyperGallery

A navigable address space of SemanticWords. Navigate by Horner address offset or Fano generator path. Nearest-neighbour search by Fano index distance.

```python
gallery = HyperGallery()
gallery.add('hello')
gallery.address_range('hello', n=8)    # 8 consecutive addresses
gallery.fano_neighbours(word, n=5)     # nearest by Fano distance
```

## Monad Integration

```
word → (coords_ℝ, coords_ℂ, coords_ℍ, coords_𝕆)
```

The Horner index is distributed across the algebra tower dimensions. This is the **Tongue scaffold** — the architecture for SMNNIP output to SemanticWord reverse lookup.

Full Tongue (not yet built): OctEl attractor coordinate → nearest SemanticWord via Fano neighbour search in HyperGallery.

## Equations

| Name | Status | Description |
|------|--------|-------------|
| `horner_encode` | ESTABLISHED ✓ | text → base-97 address |
| `fano_encode` | ESTABLISHED ✓ | text → base-7 octonion path |
| `semantic_word` | THEORETICAL ◈ | full SemanticWord record |
| `monad_address` | THEORETICAL ◈ | word → algebra tower coords |
| `address_range` | ESTABLISHED ✓ | n consecutive addresses |
| `fano_path` | THEORETICAL ◈ | Fano generators → canonical word |

## TODO

- Wire Tongue: OctEl → nearest SemanticWord via Fano distance
- Full monad: SemanticWord as output of SMNNIP inference
- GitNexus repurpose: HyperIndex visual as blockchain-style corpus map

## Shell commands
```python
hw('hello')       # full SemanticWord record
horner('hello')   # Horner index
fano('hello')     # Fano index
monad('hello')    # algebra tower coordinates
```
