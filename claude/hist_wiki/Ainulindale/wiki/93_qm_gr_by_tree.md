# 93 — QM and GR by Tree: A Tested Conjecture

**Measured 2026-08-22.** Continues [[92_ring_theory_spine]]. Every number here was
computed (`ContextPlease/claude/scratchpad/2026-08-22_qm_gr_by_tree/qm_gr_test.py`,
run against `SedenionFactoralRelativity/engine/lineage.py`). The conjecture it
tests was **refuted as stated** — and the refutation is kept, because what it
turned up in its place is worth more than the guess.

---

## The conjecture

Cody, 2026-08-22:

> *"Does quantum mechanics exist only in Telperion and GR exist only in
> Laurelin?"*

A sharp, testable claim. QM's signature is **non-commutativity** (`[x,p] ≠ 0`);
GR's is **curvature**, which [[90_divisors_are_definers]] and the UDEO white
paper (§2.5) identify with the **associator** `(ab)c − a(bc)`. The sedenion
splits `𝕊 = 𝕆 ⊕ 𝕆` into two octonions — the two trees — so the test is direct:
does non-commutativity segregate to one tree and curvature to the other?

(Reported by *content* — lower octonion `e₀..₇` vs upper octonion `e₈..₁₅` —
because the Telperion/Laurelin label is applied inconsistently across the repos:
the generational-lineage skill calls Telperion "Blue/lower," the engine comment
calls the upper octonion Telperion. That tangle is flagged at the end and does
not affect the result.)

## The measurement

**QM proxy — non-commutativity**, over unordered basis pairs:

| pair | non-commuting |
|---|---|
| both lower (e₀..₇) | 21/28 (75%) |
| both upper (e₈..₁₅) | 28/28 (100%) |
| across the boundary | 56/64 (88%) |

**GR proxy — curvature (associator ≠ 0)**, over distinct ordered triples:

| triple | associator ≠ 0 |
|---|---|
| within lower | 168/336 (50%) |
| within upper | 336/336 (100%) |
| crosses the boundary | 1344/2688 (50%) |

Of **all 1848 curvature events: 27% lie within a single tree, 73% cross the
boundary.**

## Verdict: the literal conjecture is FALSE

Both signatures live in **both** trees. Each octonion is a complete copy of 𝕆,
so each carries the full non-commutative *and* non-associative structure. QM is
not confined to one tree; GR is not confined to the other.

But three true things fell out, and each is sharper than the guess.

### 1 — QM and GR are different *rungs*, not different trees

    QM  (non-commutativity)    first appears at dim 4  — ℍ, quaternions
    GR  (curvature/associator) first appears at dim 8  — 𝕆, octonions

They are **consecutive generations in the tower**: QM the parent (loss of
commutativity, ℂ→ℍ), GR the child (loss of associativity, ℍ→𝕆). So QM-vs-GR is a
**radial** distinction — the σ / tower-depth axis, matching the engine's facet
ladder (QM/Riemann at σ=½, GR at σ=2) — while Telperion-vs-Laurelin is an
**angular** one (which octonion). The conjecture conflated the two axes. Both
are "the generational lineage," pointing different ways: one up the tower, one
around it.

### 2 — GR is a *boundary* phenomenon: gravity is the curvature of the seam

**73% of every curvature event crosses the boundary between the trees.** Only
27% is intra-tree. So curvature does not belong to either tree — it belongs to
the **coupling** between them, which is the zero-divisor boundary, σ=½, the
corpus callosum ([[80_aphasia_zd_reframe_memory]]).

> **Gravity is the curvature of the seam where the two trees couple** — not the
> geometry of either sheet.

A measured reading of "spacetime is the boundary": GR lives in the interface,
exactly where QM (an intra-tree phenomenon — each octonion is a self-consistent
quantum world) does not.

### 3 — the trees are asymmetric, and the reason is e₀

The upper octonion is **100% / 100%** (maximally non-commuting, maximally
curved — pure dynamics); the lower is only **75% / 50%**. The cause is the
identity. The lower octonion contains **e₀** — the real axis, gain 1, ∅_RB, the
vacuum ([[89_the_seven_octonions]]) — and e₀ commutes and associates with
everything, softening that whole tree. The upper octonion is pure imaginary,
all active.

So the real split between the trees is not QM vs GR. It is
**classical-anchored vs pure-dynamics** — one tree holds the identity (the flat,
"what is" direction), the other is pure imaginary (the curved, active
direction). This is where the **structure constants** show their invariance:
it is the *same* octonion multiplication table read in both trees; all that
differs is whether e₀ is in the room.

## Summary

| claim | status |
|---|---|
| QM only in one tree, GR only in the other | **FALSE** — both in both |
| QM and GR are consecutive tower rungs (dim 4, dim 8) | measured |
| GR/curvature is 73% a boundary phenomenon | measured |
| the trees split by e₀ (classical anchor) vs pure imaginary | measured |

**QM is intra-tree; GR is the curvature of the boundary between trees; and the
trees themselves split by whether they hold the identity.**

## Loose end flagged — the naming tangle

The Telperion/Laurelin ↔ lower/upper octonion assignment is inconsistent across
the repos (skill: Telperion = Blue/lower; engine: Telperion = upper). This page
sidesteps it by reporting by content. It should be reconciled once, everywhere,
against a single source of truth — recorded here as an open cleanup, not fixed in
passing.
