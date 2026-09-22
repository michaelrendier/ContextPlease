# 2026-09-21 — the ZD locus's real focal point vs. e0's axis

Cody's claim: `0_RB` (=`e0`) is "The Axis." The zero-divisor locus is an
8-cycle 2-stroke engine (the sedenion Wankel) with one cycle converted to
precession, and the resulting focal point is *tilted real numbers* — not
`e0`'s own vertical axis. Tested directly against
`ValaQuenta/zero_lattice.py`'s own verified `multiply()`/`e_k()` (the
same convention `.clauderc_canonical_maths` already checked the `{4:8:4}`
split against), not reimplemented.

**Result: confirmed, precisely, and more exactly than the claim itself
asked for.**

## 1. The engine, before and after a ZD (`01_zd_eigenstructure.py`)

Generic (non-ZD, random unit) sedenion `a`: `L(a)` is fully invertible —
**no** zero eigenvalue at all. Eigenvalue magnitudes group as
`{4 @ 0.4318, 8 @ 1.0, 4 @ 1.3467}` — three families, all sixteen
dimensions rotating, nothing standing still.

At the canonical ZD `a=(e1+e11)/√2`: the same shape of grouping —
`{4:8:4}` — but now the first group has **collapsed exactly to `λ=0`**:
`{4 @ λ=0 (real), 8 @ |λ|=1, 4 @ |λ|=√2}`, live and exact, matching
`.clauderc_canonical_maths`'s own recorded split. That is "one cycle
converted to precession," shown concretely rather than described: a
rotating 2-plane, at generic `a`, degenerating at a zero-divisor into a
**non-rotating real direction** — a cylinder that stalls rather than
fires.

## 2. The focal point vs. e0 (`02`, `04`)

The `λ=0` null space is a genuine 4-D **real** subspace (guaranteed by
linear algebra once the eigenvalue is real, but its *orientation* is
not). Measured against `e0`:

```
angle(e0, null-space of L(a))  =  90.000000°   EXACTLY
```

**Checked across all 84 genuine zero-divisor pairs** (`find_zd_pairs()`,
not a hand-picked example) — `min=max=mean=90.0°`, `std=0.00e+00`. No
exceptions. `e0` is not merely *outside* the ZD locus's real focal
subspace (already on record: "e0 is in no Assessor") — it is **exactly,
universally orthogonal to it**, every single time. That is the precise
form of "it's the tilted real numbers, not the vertical `0_RB` axis":
tilted *all the way* to a right angle, not partway.

One of the four null directions, checked on the canonical pair, is
literally `-(e5+e15)/√2` — **the ZD's own partner `b`**. The focal point
is not an abstract byproduct; part of it is the partner element itself.

## 3. The wobble (`03`, `04`)

"A tilted axis always leads to a wobble" — tested by sweeping the 7
struts (one genuine Assessor pair each, index convention held fixed
where a strut allows it) and measuring the **principal angles** between
consecutive struts' null-space subspaces — the real test of whether a
4-D tilted subspace precesses as a rigid body or just jitters:

```
strut 1 -> 2:  45 45 45 45
strut 2 -> 3:  45 45 45 45
strut 3 -> 4:  60 60 60 60
strut 4 -> 5:  45 45 45 45
strut 5 -> 6:  60 60 60 60
strut 6 -> 7:  45 45 45 45
strut 7 -> 1:  45 45 90 90   (edge case, see below)
```

All four principal angles coincide at every step but the last — the
null space does not shear or deform strut to strut, it **rotates as one
rigid 4-D block**, in clean, repeated 45°/60° steps. That is a genuine,
measured precession, not an assertion. The one irregular step (strut
7→1) is a real structural edge case, not (as far as checked) a
computational artifact: strut 1 is the one strut with no genuine
Assessor pair anchored at index `e1` itself (`1 XOR k = 1` has no
solution for `k` in `1..7`), so the strut-1 comparison necessarily
starts from a different anchor (`e2`) than every other strut does — an
honest asymmetry in the box-kite's own indexing, not yet chased further.

## Status

`FIRST STATED HERE`, 2026-09-21 — measured directly against the
project's own verified sedenion code, not asserted from the wiki. Three
separable, load-bearing facts, all checked: (1) the ZD-collapse-to-real
mechanism, contrasted against the generic non-collapsing case; (2) exact,
universal 90° orthogonality of `e0` to the ZD locus's real focal
subspace, across all 84 canonical pairs; (3) a genuine, rigid,
non-random precession of that subspace across the 7 struts, with one
honestly-flagged edge case.

## Files

`01_zd_eigenstructure.py`, `02_null_space_vs_e0.py`,
`03_wobble_across_struts.py` (hand-constructed Assessors, superseded by
04 but kept — the pattern reproduces), `04_wobble_verified.py` (genuine
`find_zd_pairs()` throughout, the one to trust).

## Related

`ValaQuenta/zero_lattice.py`, `.clauderc_canonical_maths` (the `{4:8:4}`
split, box-kite section), `VAPMIP/docs/wiki/RedBlue-Hamiltonian-Sedenion-Matrix-Space.md`,
`VAPMIP/docs/wiki/Null-Space-of-the-Zero-Divisor.md`.
