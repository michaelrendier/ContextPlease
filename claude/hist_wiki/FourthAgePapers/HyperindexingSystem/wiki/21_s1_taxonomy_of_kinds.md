# S1 · Taxonomy: every kind of hyperindex, one input set

*Claude Sonnet 5.5, 2026-09-29. Synthesis of v00–v19. Notebook: [`w01_taxonomy/`](../notebooks/w01_taxonomy/).*

Each version's address function was run on the same inputs, loaded by path and unmodified: **(A)** all 18,278 lowercase words of length ≤ 3 (collision counts are exact) and **(B)** the first 1,000 characters of the corpus sample.

## Collisions and anagram behaviour on set A

| Version | Kind | Distinct addresses | Collisions | `listen` = `silent`? |
|---|---|---:|---:|:---:|
| v00 | mixed radix, length **not** included | 17,576 | 702 | no |
| v00 | mixed radix + stored length | 18,278 | 0 | no |
| v02 | exact bijection (shortlex rank) | 18,278 | 0 | no |
| v03 | SHA-256 label of the bijection | 18,278 | 0 | no |
| v09 | SHA-256 label, Unicode order | 18,278 | 0 | no |
| v14 | mixed radix + stored length | 18,278 | 0 | no |
| v06 | (count vector, rank in anagram class) | 18,278 | 0 | no |
| v11 | semantic zero ordinal (50 zeros) | 23 | 18,255 | **yes** |
| v12 | prime zero index | 2,409 | 15,869 | no |
| v13 | firing signature, n = 16 | 8 | 18,270 | no |
| v19 | Midline base-96 (case exact) | 18,278 | 0 | no |

v00's integer alone takes only 26³ = 17,576 values: leading `a` is digit 0, so every shorter word coincides with a 3-letter word (702 = 26 + 676 collisions); the stored length removes them. v19 shows no collisions because it keeps case and its 96-symbol domain covers lowercase.

## Size on 1,000 characters (set B)

| Address | Bits | Behaviour |
|---|---:|---|
| raw, 8 bits/char | 8,000 | grows |
| v02 exact bijection | 6,600 | grows |
| v00 / v14 mixed radix + length | 6,600 | grows |
| v03 / v09 label (SHA-256) | 256 | fixed: a key only; the payload is the v02 address |
| v06 (count vector, rank) | 5,126 | grows (order-0 entropy) |
| v11 zero ordinal (of 50) | 5.64 | fixed |
| v12 zero index (of 6,543) | 12.68 | fixed |
| v13 signature, n = 16 (16! values) | 44.25 | fixed |
| v19 Midline, 1,000 characters | 6,585 | grows (96-symbol domain) |
| v16 fold, rungs ℂ…𝕊 | 64 | fixed (taken from the v16 notebook, not re-run) |

## Result

Two families:

- **Addresses that grow with the input.** Exact. The size is the information content of the text in another radix. The only ones below the raw size are those that give up part of the alphabet (here v19, at 6,585 bits against 6,600 for the 97-symbol bijection) or spend the text's non-uniformity (v06); no exact address is smaller than the text's entropy.
- **Addresses of fixed width** (label, v11, v12, v13, v16). Keys, not stores: they identify or locate, none inverts.

Exact means collision-free on set A; six of the eleven rows are.
