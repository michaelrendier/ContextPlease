# v04 · VectorAddress limbs, OrbitCache, GLSL regeneration

*Claude Sonnet 5.5, 2026-09-29. Documents `PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/infinite-data-vector-shaders.py` (459 lines). Notebooks: [`v04_vector_orbit/`](../notebooks/v04_vector_orbit/).*

**Dating.** Git: 2026-04-18. Placed before v05 and v06 because its `VectorAddress` is the smallest form of a class that reappears with more fields there (`meta`, `from_label(..., meta)`).

## What it is

- `VectorAddress`: the integer address as little-endian **uint32 limbs** (`components`), label = limbs as 8-hex-digit words joined by `_`. `num_uvec4s = ⌈words/4⌉`: sized for a GPU buffer.
- `OrbitCache`: "partition the string space into orbits under character permutation; canonical form `sorted(string)`".
- `GLSLAddressEngine`: emits GLSL compute-shader source that regenerates a string from a limb buffer (big-integer divide by N in place, bijective shift `scratch += 1`, extract right to left).

## Measured

| chars | address bits | limbs | uvec4 | label chars |
|---:|---:|---:|---:|---:|
| 140 | 924 | 29 | 8 | 260 |
| 1,000 | 6,600 | 207 | 52 | 1,862 |
| 4,000 | 26,399 | 825 | 207 | 7,424 |

- The `_`-joined label is **larger** than plain hex of the same integer (1,862 characters against 1,650 hex digits at 1,000 chars).
- `OrbitCache` is an exact-string cache. Fed `listen, silent, enlist, listen, tinsel, listen` it reports 6 lookups, 2 hits, 4 misses (33.3%, exact repeats only) and one multi-member orbit. Each anagram has its own address computed by the full bijection (`listen` 311,118,541,415; `silent` 251,013,532,199; `enlist` 150,001,668,071; `tinsel` 165,148,453,895). The module docstring promises reaching other orbit members "by a cheap integer offset"; that offset is not implemented.
- The offset that does exist is a **transposition**: swapping positions i < j changes the address by `(d_j − d_i)·(N^(L−1−i) − N^(L−1−j))` with `d = index + 1`. Verified on a 500-character string. The offset is 3,188 bits against a 3,299-bit address: cheap in the number of operations, not in size.
- The generated GLSL (51 lines) contains the bijective shift. It also contains **10 lines with doubled braces** (`{{`, `}}`), e.g. `for (int i = int(u_num_words) - 1; i >= 0; i--) {{`: the escape form of a `str.format` template filled with `str.replace`. That is not valid GLSL as generated. No GL context exists here, so the shader is inspected and not run.

## Under permutation of the string

The orbit is the anagram class (all permutations of positions). This version names the orbit and canonicalises it (sorted string) but computes no address from the canonical form.

## Status

Distinct: the only version with a limb representation and a GPU regeneration path. Limbs continue into v05 and v06.
