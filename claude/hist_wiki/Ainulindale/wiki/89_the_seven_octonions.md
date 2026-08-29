# 89 — The Seven Octonions

**Measured 2026-08-15/16.** Every result on this page was computed, not asserted.
Where something failed, the failure is recorded too — that is the more useful half.

---

## The question

A **sedenion** is a 16-dimensional number. You build it by doubling: real numbers (1)
→ complex (2) → quaternions (4) → octonions (8) → sedenions (16). Each doubling buys
you something and costs you something.

| Step | Dimension | What you lose |
|---|---|---|
| ℝ → ℂ | 1 → 2 | ordering (no "less than") |
| ℂ → ℍ | 2 → 4 | commutativity (`ab ≠ ba`) |
| ℍ → 𝕆 | 4 → 8 | associativity (`(ab)c ≠ a(bc)`) |
| 𝕆 → 𝕊 | 8 → 16 | **division** — zero divisors appear |

That last loss is the interesting one. In a sedenion you can have two non-zero numbers
whose product is zero: `a·b = 0` with `a ≠ 0` and `b ≠ 0`. These are **zero divisors**,
and at dimension 16 there are exactly **84** of them (as normalised diagonals).

The question this page answers: *what shape do those 84 make?*

---

## The three channels

For a zero divisor `a`, look at what multiplying by `a` does to the whole space. Written
as a matrix `L_a`, it has exactly three distinct gains:

```
gain 0      4 dimensions      CONTRACT   the kernel — what `a` annihilates
gain 1      8 dimensions      PRESERVE   in equals out
gain √2     4 dimensions      DILATE     what `a` amplifies

0²·4 + 1²·8 + (√2)²·4  =  16  =  the dimension
```

This split is **forced**. The counting law `Σ gain² = dimension` admits no other answer.
You do not get to choose `{4, 8, 4}` — it is the only spectrum available.

### PRESERVE is the octonions

The middle 8 dimensions are **closed under multiplication** (leakage 9.5×10⁻¹⁶ — zero to
machine precision), contain the number 1, have a multiplicative norm, and are
alternative but not associative. No zero divisors live inside it.

By **Hurwitz's theorem** — the only composition algebras over ℝ are ℝ, ℂ, ℍ, 𝕆 in
dimensions 1, 2, 4, 8 — an 8-dimensional closed subalgebra with a multiplicative norm
*must be* the octonions. So this is measured, not assumed.

### The wings are not algebras

An earlier reading called `{4; 8; 4}` "an octonion wrapped by its constituent
quaternions." **Half of that is wrong.** CONTRACT and DILATE both leak badly (1.39 and
1.41) and are *not* closed. Neither are they closed jointly. They cannot be constituent
algebras because they are not algebras.

The correct picture is a **clathrate**: a cage that is not itself the guest, holding
something complete on its own.

---

## Where the quaternions actually are

There are **7 distinct PRESERVE octonions** among the 84 diagonals, 12 diagonals each.

Every pair of them intersects in exactly **4 dimensions** — all 21 pairs, no exceptions.
Each intersection is closed, contains 1, and is 4-dimensional, so by Hurwitz again it is
**the quaternions ℍ**. But the 21 pairs do **not** give 21 distinct quaternions: the three
pairs on a Fano line all intersect in the *same* 4-space, so there are exactly **7**.

> The quaternions were always there. They are the *pairwise intersections* of the
> octonions, not the wings of the gain spectrum. Same picture, different location.

```
 7  OCTONIONS     dim 8
 7  QUATERNIONS   dim 4, one per Fano LINE
```

> **CORRECTED 2026-08-16.** This originally read "21 QUATERNIONS ... 21 = C(7,2)".
> **That is wrong.** There are 21 *pairs* of octonions, but only **7 distinct
> quaternions**: all three pairs on a given Fano line intersect in the **same**
> 4-space (joint span dim 4, not 12; leak ~2e-15). Each line has **one quaternion at
> its core**, shared by all three of its octonions. The structure is **7–7–7**:
> 7 octonions, 7 struts, 7 quaternions.

---

## The Fano plane

Each zero divisor lies on a **strut** — the label `i XOR j` from its two indices. There
are 7 struts, matching the 7 box-kites.

Cross-tabulate struts against octonions:

| strut | octonions present |
|---|---|
| 9 | 0, 1, 2 |
| 10 | 0, 3, 4 |
| 11 | 0, 5, 6 |
| 12 | 1, 3, 5 |
| 13 | 1, 4, 6 |
| 14 | 2, 3, 6 |
| 15 | 2, 4, 5 |

7 struts, 7 octonions, 3 octonions per strut, 3 struts per octonion, **any two struts
share exactly one octonion, and any two octonions lie on exactly one strut.**

That is the definition of the **Fano plane** — `PG(2,2)`, the smallest projective plane,
7 points and 7 lines. Every axiom checks.

```
OCTONIONS   =  the 7 POINTS
STRUTS      =  the 7 LINES
QUATERNIONS =  the 7 LINE-CORES (one per line, shared by its 3 octonions)
21 FLAGS    =  the point-on-line incidences, and the V4 orbit count
```

And it is the *same* Fano plane that governs octonion multiplication itself — the lines
extracted from the multiplication table are identical, entry for entry, to the table
above.

The Fano plane is also the **Steiner system S(2,3,7)**, which puts this structure in
design theory — the same apparatus that builds the Golay code, the Leech lattice, and
the Mathieu groups.

---

## The valve group

The 84 diagonals carry three natural pairings, each splitting them into 42 pairs:

| name | what it does | example |
|---|---|---|
| `sA` | flip the sign | `e₁+e₁₀` ↔ `e₁−e₁₀` |
| `sC` | XOR-translate both indices, keep sign | `e₂+e₁₁` ↔ `e₃+e₁₀` |
| `sN` | same annihilation behaviour | `e₁+e₁₀` ↔ `e₂−e₉` |

All three are **free** (no fixed points), all three **commute**, and:

```
sA · sC = sN
sA · sN = sC
sC · sN = sA
```

They generate the **Klein four-group V₄** — order 4, not 8. The three pairings are the
three non-identity elements of one group; **there is no third independent binary
choice.**

### Two valves, and the blind spot is both at once

`sN` is the pairing that annihilation testing **cannot see through**. Probing which
diagonals annihilate each other resolves the 84 down to 42 signatures and then stops —
permanently, because `sN` is a genuine symmetry of annihilation, not a limitation of
probing.

And `sN = sA · sC`. **The invisible thing is exactly the two visible things done
together.** Operate both valves and you land somewhere no annihilation test can
distinguish from where you started.

This is why one bit of the address is unreachable from inside the algebra. It is an
**orientation** — the same way ℂ cannot tell you whether you picked `i` or `−i`, because
conjugation is an automorphism. The choice has to come from outside and be made once,
globally.

### The counting closes

V₄ acts freely, so the orbits all have size 4:

```
84 / 4 = 21
```

and 21 is two things on this page — the Fano **flags** (7 lines × 3 points) and the
orbits. **Not the quaternions**: there are 7 of those, one per line. The earlier text
claimed a triple identity; it is a double identity plus an error, corrected above. **One rotor face per flag, two valves per face, three faces per strut**, with
nothing left over.

---

## What was refuted

Recorded because the failures constrain the structure more tightly than the successes.

**`E8³` is unreachable.** Three octonions × 8 dimensions = 24 = the rank of the Niemeier
lattices, and `E8³` is one of them. But every PRESERVE octonion **contains the number 1**,
so no two of them can ever be orthogonal. Measured at dimension 32: 35 octonions, 595
pairs, **zero orthogonal pairs**, minimum intersection 2. Adding sedenions adds octonions
but never separates them. Not "not yet found" — structurally closed.

**E8 does not require 48 dimensions.** The octonion is 8-dimensional at depth 0 at every
level of the tower. It is already whole inside one sedenion.

**Orientation cannot be made an independent invariant.** The sign is locked to the
XOR-translation — degenerate partners differ in position *and* sign together. Fixing the
sign does not remove the pairing. Worst-case search stays at 11 probes either way. The
invariant that *does* work is the **strut**, which survives all 42 degeneracies.

**The strut/octonion structure is `PG(2,2)` only at dimension 16.** At dimension 32 it
becomes 35 octonions on 15 struts with skew pairs appearing (`|line ∩ line| ∈ {0,1}`) —
a projective *space*, not a plane.

---

## See also

- [[84_the_box_kite_debugger]] — the 7 box-kites and the negative space
- [[86_the_16d_oscilloscope]] — the gain spectrum as an instrument
- [[87_the_boundary_lever]] — the lineage recursion and generational depth
