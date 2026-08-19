# 2026-08-18 — The three faces, the Fermat ladder, and monad_identity.bin

## What was asked

Catch up on the two 2026-08-17 primers, repair the harness, then design the
prime hashing algorithm and a binary format unifying the three faces of
language. Session ran the length of the stack.

## What is here

| File | What it is |
|---|---|
| `boxkite_prime_hash.py` | the **first** prototype — capped letters at 313 and encoded 35 PG(3,2) lines. Superseded, kept because the correction is the story: 313 is the 65th prime, not the 21st. |
| `sizecheck.c` | verifies the C struct layout against the ctypes mirror — `sizeof` and `offsetof` for every field that matters |
| `c_sizes.txt` | its output, which the python side diffs against |
| `monad_identity.bin` | a real build (3,081 entries, 594 KB). **Gitignored** — the format's whole design is that it stores positions and is regenerable, so versioning it would contradict the point. `address_recomputed 3081/3081` is the guarantee. |

The finished code moved into VAPMIP and is versioned there:
`lineage_hash.py`, `prime_hash.py`, `monad_identity.py`, `PtolC/monad_identity.h`.

## What was measured

- **Layouts agree byte for byte** — header 384 B, entry 96 B, chan 8 B, edge
  12 B, every probed offset matching between gcc and ctypes. Python writes the
  bytes, C reads them, no serialisation layer.
- **73,457 words → 73,457 distinct spell codes**, zero collisions, round-trip
  exact.
- **`gcd` IS the LCA** — the descent is one division, never a tree walk.
- **`address_recomputed 3081/3081`** — the discardability test. The address is
  never stored; only the sparse channel list plus a fingerprint.

## The correction that matters

The letter cap is the **20th prime (71)**, not 313. `313` is the 65th prime and
is the *sieve's* regime boundary — two unrelated facts had been fused. But the
ladder underneath is real: `F_n = 2^(2^n)+1` **is** the Cayley–Dickson doubling
index, `3·5·17·257 = 65535 = 2^16 − 1`, and the 15 nonempty subsets of
`{3,5,17,257}` are the 15 points of PG(3,2).

**Budget consequence:** with the cap corrected, 42 assessors = 94 digits and fit
under 100, where at 313 they were 112 and did not. The error was costing the
encoding its entire assessor layer.

## The bug worth remembering

The first `monad_identity.py` masked the spell code with
`& 0xFFFFFFFFFFFFFFFF`. Base-27 overflows uint64 past 13 letters, so that was a
**silent truncation** — and a truncated spell is not bijective, which would have
made the file quietly lie about its central property. Now flagged
(`MI_FLAG_SPELL_OVERFLOW`) and excluded from the claim rather than wrapped:
`spell_roundtrip 2591/2591, spell_overflow 490 (flagged, not truncated)`.

## Written up

`VAPMIP/docs/wiki/Tuning-the-Engine/28_the_three_faces_the_fermat_ladder_and_executable_structure.md`
and `VAPMIP/PRIMER_2026-08-18_THREE_FACES_AND_EXECUTABLE_STRUCTURE.md`.
