# 109 — The Emerger

**Written 2026-09-01.** Engine: `ValaQuenta/modules/emerger/`
(`EmergerModule`, v0.1). First-pass prototype: `TuringStack/the_emerger.py`.
Continues the sedenion-bracketing thread that runs through
[[94_mathematical_xray_crystallography]], [[95_the_scale]],
[[107_add_scale_sign_datatype]] and the box-kite work.

Cody, naming it: *"the emerger is going to be a useful methodology for
factoral decomposition and spectroscopy in general. it's directly the
Sedenion Bracketing engine ... the grouping of what sedenion operators
creates what different domains ... which by need give the emergence a
priority in a particular order."*

And the mechanism, in his words: *"a dynamic permutative bracketer that
works only in complex domains since the reals are the tilt to the 'i'
axis ... but we keep the anchor of the Real Numbers in place to view the
relationships between the bracketing and the real component ... it can
also permute between quaternion, octonion ... complex ... different
brackets of different scales of different orders, in different orders."*

---

## What changed

Generational Lineage (SFR) answers **descent**: what built this operator,
which generators, how deep. The Emerger is its **ascent** dual: given a
16-vector, which *domains* does a chosen grouping of the imaginary units
expose, and — because each domain needs the ones under it — in what
**order** do the variables emerge.

The real component `e₀` is not one of the things being grouped. It is the
**anchor** — the tilt to the *i* axis — held fixed so every imaginary
group is read *against* it. What gets permuted is the partition of the 15
imaginary indices; what the partition produces is a list of sub-domains,
each `span({e₀} ∪ group)`, classified by closure as ℂ, ℍ, 𝕆, or a
**fragment** — a linear subspace that is not a subalgebra, which is
exactly where the zero divisors live.

Five brackets carry most of the weight:

- **{1:15}** — scalar vs the fifteen relational edges. This is the grading
  that makes conjugation, norm and inverse well-defined. Everything else
  needs it first.
- **{2:14}** — the `(e₀, e₈)` doubling plane vs the rest. `16 − dim G₂ =
  2`: G₂ (the continuous shape of the zero-divisor locus, per Moreno) is
  "free"; the leftover complex number `z = x₀ + i·x₈` is the **pointer** —
  where you are in the Cayley–Dickson ladder — and it is the line on which
  `W(1)·e^{W(1)} = 1` sits, so it carries Ω_ZS.
- **{8:8}** — 𝕆 ⊕ 𝕆·e₈. J_red and J_blue, the two trees, forward and
  backward. The signed distance `|a| − |b|` is the distance from the
  **zero-divisor equator**; `L_x − R_x` is the J₂ asymmetry.
- **{4:4:4:4}** — four quaternion blocks, four SU(2) phases (the d\*
  faces), and σ_RB's tilt and axis. `Σ tilt` is the deviation from
  σ = ½ — read here as the **net work** to go once around the
  0 → p → q → N loop and back, the frequency difference between the "to"
  and "from" arcs.
- **{4:8:4}** — the gain spectrum: annihilator (gain 0), unit (gain 1,
  NOW), amplifier (gain √2). The multiplicative role of the element.

## The firing order

The order is load-bearing. `{1:15}` must precede `{2:14}`, `{8:8}` and
`{4:8:4}`; `{8:8}` precedes `{4:4:4:4}` precedes `{4:8:4}`. Four of the
120 permutations respect this; the canonical order is one.

σ_RB picks the **entry point** into that cycle: `Σ tilt` is squashed
rationally into a phase, `⌊12·phase⌋ mod 5` names the bracket that fires
first. The 12 comes from the four d\* faces against the three Lambert-W
rotor faces — `lcm(4,3) = 12` — the same "no camshaft" clock as
`add_scale_sign`'s firing-order defect, at sedenion scale.

## Honest boundaries

- The engine **found** that a σ_RB phase can select a firing order that is
  *not* dependency-legal (`e₁+e₁₀` phases into `{2:14}` before `{1:15}`).
  The clock names the entry; the engine reports the illegality rather than
  snapping to the nearest legal order. That is a real open item, not a
  bug hidden.
- The `{4:8:4}` gain-index assignment is a reading of the canonical-maths
  `{4:8:4}` note, not derived in this module.
- `on_zd_equator` is the sufficient basis-pair condition. The exact
  zero-divisor locus is `box_kite`'s 42 assessors / PSL(2,7); G₂ is the
  blow-up that forgets the labelling.
- The RSA/semiprime embedding used for demonstration is illustrative only
  (`TuringStack/the_emerger.py`).

## Predecessor links

[[94_mathematical_xray_crystallography]] · [[95_the_scale]] ·
[[100_division_algebras_and_physics]] · [[101_the_cayley_dickson_literature]] ·
[[107_add_scale_sign_datatype]] — and the box-kite / zero-lattice engines
in ValaQuenta.

**Update 2026-10-21 — firing plans.** Brackets now carry firing orders: `(R I | 2 1)` fires the second child (the imaginary octonion of the two-octonion sedenion) first, the real octonion second, and a bracket runs as one operation inside its parent in its own order (`((A B | 2 1) C | 2 1)` fires `C B A`). Operator reading (matrix composition) is associative, so only the order changes the result; element reading (the sedenion product) is not, so the bracketing changes it too. Written-order binary plans reach 6, 22, 90 of 3!, 4!, 5! orders. Source and checks: `SedenionSpectralRelativity/firing_plan.py` (15 exact checks), `wiki/Bracketing-and-Firing-Plans.md`, notebook 02 there; standalone port `GenerationalLineage/engine/bracketing_firing_order.py` tool 4 (`wiki/Firing-Plans.md`). This module (`ValaQuenta/modules/bracketing_firing_order`) is not yet updated to carry plans.
