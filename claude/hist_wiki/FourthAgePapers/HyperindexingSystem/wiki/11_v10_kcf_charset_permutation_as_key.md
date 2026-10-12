# v10 · KCF-1: address → key material; the permutation index that does not exist

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Kryptos/kcf.py`. Notebooks: [`v10_kcf/`](../notebooks/v10_kcf/).*

**Dating.** Git: **2026-05-03** (`6b987e4`), one day after v09.

## What it is

`KCF(face_id, charset)`: `hw_address(label)` → integer; `_permute(addr)` XORs with 64 bits of SHA-256(charset), multiplies by 2⁶¹−1 and reduces mod 2⁸⁹−1; HKDF-SHA256 expands the result to 32 key bytes (`KCF_KEY_AES`, `KCF_KEY_HMAC`, `KCF_KEY_ADDR`). Per-Face salt from the face id. The docstring: "apply charset permutation as cryptographic offset … asymmetric trapdoor".

## Measured

- `derive("hiraeth")` is deterministic (32 bytes) and a trailing space changes it.
- **`hw_address` is not the bijection.** It is a plain base-N numeral with a zero digit (the first charset symbol, a space here, is digit 0) and an out-of-charset fallback `ord(ch) % N`. So `hw_address(" x") == hw_address("x")`, and `hw_address("é") == hw_address("I")` (233 mod 97 = 39).
- `_permute` output is below 2⁸⁹ whatever the label length (a 200-character label has a 1,317-bit address and an 88-bit permuted value). Reversing the charset changes the key. The construction is a hash of the charset string, not the permutation of the charset.
- **The permutation index `charset.py` names is not in the repository.** Notebook 02 writes it from Myrvold & Ruskey (IPL 79, 2001; read in full): `unrank1` reproduces the rows 0–7 of the paper's Fig. 1 for n = 4, and `rank1∘unrank1` is a bijection on all 24. At N = 97 there are 97! ≈ 2⁵⁰⁵ orders; a random order has a 504-bit rank. With the v02 class and a charset built from `unrank1(97, r)` the public address and the private address of the same string differ, and the private one round-trips.

## Under permutation of the string

A private charset is a permutation applied to the digits of the address (v15 shows this is a monoalphabetic substitution and what follows from it). `rank1`/`unrank1` are O(N) steps plus one big integer; they supply the missing bijection between the integer key and the charset order.

## Status

Distinct as the version where the permutation is the secret. The bijection between key integer and charset order is in notebook 02; KCF itself derives keys from a hash of the charset instead.
