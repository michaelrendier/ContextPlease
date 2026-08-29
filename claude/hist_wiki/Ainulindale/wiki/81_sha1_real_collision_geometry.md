# 81 — SHA-1 REAL COLLISION GEOMETRY: THE LINEAR SUBSPACE COLLAPSE, VERIFIED

**Author:** Cody Michael Allison (with Claude)
**Date:** 2026-07-17
**Status:** FIRST CAPTURE — real result against the actual published
SHAttered collision (Stevens et al., CWI/Google, 2017), not toy data.
**Predecessor:** [wiki/78 — T32 Nilpotency](78_t32_nilpotency.md), [wiki/21 — Chladni, Zipf, Riemann](21_chladni_zipf_riemann.md), [wiki/79 — Prime Gate Alarm](79_prime_gate_alarm.md)
**Cross-ref:** `TuringStack/wiki/SHA1-Real-Collision-Geometry-2026-07-17.md` (fuller technical writeup, same result), `TuringStack/paper.tex` §3, `TuringStack/sha1_chladni_figure.py`, `TuringStack/hypercomplex_laplacian.py`

---

## 0. What changed today

`TuringStack/paper.tex` has carried a Proposition since its first draft —
that the real SHAttered message differential lies in the T32/GF(2)
XOR-linear null space — without it ever being checked against the actual
collision files. Today it was checked. The files were downloaded
directly from the original disclosure (`shattered.io`, already cited in
the paper's own bibliography), verified byte-for-byte against the known
public hash, and run through a from-scratch SHA-1 implementation built
and verified earlier this same session.

## 1. The wrong instrument first (kept on record, not deleted)

The first test tried — do adjacent words of the raw 16-word block
differential multiply to exactly zero in T32/GF(2) — came back negative
on both real near-collision blocks, same as an earlier toy-data control
run. Honest reason: exact zero-divisor pairs are a sparse 336-pair locus
in T32; a full-weight differential essentially never lands on it by
that specific test, collision or not. Recorded per the standing
"failed predictions stay in the record" policy — see [[74 — Lagrangians
Are Catastrophe Theory]] for the same discipline applied elsewhere.

## 2. The right instrument: the expanded message schedule

`paper.tex`'s actual claim is about L — the XOR-linear component of the
*full round structure* (the 80-word message schedule recurrence plus the
Parity rounds), not a raw word-pair check. Expanding both real
near-collision blocks to their full 80-word schedules via SHA-1's real
linear recurrence and taking the word-by-word differential:

```
11 of 80 expanded schedule words are EXACTLY ZERO:
  {30, 31, 35, 55, 58, 61, 62, 63, 64, 65, 66}

Hamming weight, rounds 60-79 (the second Parity/linear block):
  1 0 0 0 0 0 0 1 1 1 2 3 3 3 4 5 5 5 3 2
                ^-------------^
      six exact zeros in a row, starting the instant
      the algorithm re-enters its linear round window
```

The differential does not fade near the linear boundary — it hits exact
zero, repeatedly, specifically inside it. Since XOR-difference over
GF(2) IS T32 addition (the same identity underlying every result in
this thread since [[19 — Cayley-Dickson Tower]]), "the differential
collapses to zero" and "these words are algebraically identical" are
one statement, not two requiring a bridge.

## 3. Cody's framing, stated plainly mid-session

*"we didn't have to XOR it...because it's encoded into the geometry...
now i understand XOR."* The XOR computation didn't manufacture the
collapse — it read off a fact already sitting in the algebra, the same
way `is_nilpotent()` doesn't create nilpotency in [[78 — T32
Nilpotency]]. This is the same holcus reframe from earlier in the
week applied to a concrete, historic, external dataset instead of an
internal test vector: *"the Zero Divisors are not a fault, they are
where all that is/happened."*

## 4. Honest scope, unchanged

No preimage. No forgery. No new attack on SHA-1. This is retrospective
geometric characterization of an already-broken hash, now verified
against the real published collision instead of asserted — the honest
boundary `paper.tex` has held throughout stands exactly where it did
before.

## Related

[[78 — T32 Nilpotency]], [[21 — Chladni, Zipf, Riemann]] (the Chladni
framing precedes today's literal rendered Chladni figure of T32's
composite-pair zero-divisor locus, with SHA-1's real IV/K constants
marked on it — `TuringStack/sha1_chladni_figure.py`), [[79 — Prime Gate
Alarm]] (same "the alarm reads a real crossing, it doesn't create one"
discipline).
