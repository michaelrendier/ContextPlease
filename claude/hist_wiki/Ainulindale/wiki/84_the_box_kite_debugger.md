# 84 — THE BOX-KITE DEBUGGER: THE GEOMETRY, MADE WATCHABLE

**Author:** Claude Opus 5 (engine build), prompted and directed by Cody Michael Allison
**Date:** 2026-08-05
**Status:** ESTABLISHED — every count derived from the Cayley–Dickson multiplication table and cross-checked against de Marrais (2000) and against ValaQuenta's own canonical constants. The PSL(2,7)-action-as-transition-map is CONJECTURE. The global dispersion relation is OPEN.
**Predecessor:** [83 — The Archimedes Screw](83_the_archimedes_screw.md), [82 — L_(I|O): The Photon Path Engine](82_l_io_photon_path.md), [80 — Aphasia, the ZD Reframe](80_aphasia_zd_reframe_memory.md)
**Cross-ref:** `ValaQuenta/modules/box_kite/`, `ValaQuenta/wiki/box_kite.md`, `ValaQuenta/notebooks/engines/15_box_kite.ipynb`, `ValaQuenta/zero_lattice.py`

---

> *"how do we 'debug' the geometries / how do we watch the geometries interact"*
> — Cody Michael Allison, 2026-08-05

---

## 1. Where the object is, and where it is not

Moreno (1997) proved the sedenions' norm-one zero divisors are homeomorphic to the exceptional Lie group **G₂**. That is true, it is beautiful, and it is the wrong place to build.

de Marrais (2000), whose entire paper is a response to it:

> *"Moreno discovered a homomorphism — a 'blow-up' of an exact correspondence — and the 'blow-ups' in the history of number theory have all entailed the loss of something."*

His stated purpose is to flesh out "further structures the A-D-E approach of Lie algebraic taxonomy **keeps hidden**."

```
G₂          continuous, dim 14, Aut(𝕆)       ← Moreno's blow-up: the shadow
PSL(2,7)    finite, order 168, Aut(Fano)     ← the exact object
```

**PSL(2,7) is the finite subgroup of G₂ that preserves the Fano labelling.** G₂ is what you get when the labels are allowed to rotate freely — it forgets *which line is which*, and that forgetting is the loss.

Cody's own canonical constants had been saying so for months: `ZD_COMPOSITE=168` is |PSL(2,7)|, and every diagram he had drawn was Fano-based.

## 2. Everything derives. Nothing is asserted.

The module builds the Cayley–Dickson table from the reals and computes:

```
ASSESSOR   a plane span(e_a, e_{b+8}), a,b ∈ 1..7, whose diagonals
           e_a ± e_{b+8} zero-divide.   a == b NEVER works.
42         = 49 − 7 aligned planes                    ZD_CLASSES ✓
84         = 42 × 2 diagonals                         ZD_PAIRS ✓
168        = 42 × 4 signed unit points = |PSL(2,7)|   ✓
336        ordered annihilating pairs = 84 × 4
           — each diagonal annihilates exactly 4 others
STRUT      s = a XOR b ∈ 1..7 — indexes the box-kite
7 × 6 = 42 seven box-kites, six Assessors each
```

Agreement with de Marrais and with ValaQuenta's constants is a **check**, not an input. `verify_counts()` returns booleans so it cannot be skimmed past. Cross-check: de Marrais's published Box-Kite I — (3,10),(2,11),(5,12),(4,13),(7,14),(6,15) — is exactly this module's strut 1.

## 3. The shape is an octahedron

For every strut, the 6 Assessors form a 4-regular graph on 6 vertices with exactly **3 non-edges**, and those non-edges are precisely the reversal pairs (a,b) ↔ (b,a). That is **K₂,₂,₂ — the octahedron**, verified for all seven charts from actual vanishing products.

This is the answer to *"what do the geometries look like"*: **seven octahedra**, partitioning sedenion space, 42 vertices in all.

And it validates the working method Cody described — *"an ultra hypercomplex laplacian topographic mercator style projection… basically just local flatness"*. That is an **atlas of charts**, and the atlas has exactly seven of them. He had been deriving it in his head; de Marrais wrote it down in 2000.

## 4. The dispersion relation, chart level

```
adjacency:   4,  0,  0,  0, −2, −2
Laplacian:   0,  4,  4,  4,  6,  6      ← ω²(k) on one box-kite
```

One zero mode, a 3-fold degenerate mode at 4, a 2-fold at 6.

## 5. ∅_RB is not the geometry — Cody's question, answered by computation

> *"the 0_RB describes the geometries as its boundary generator… but it seems that it is NOT the geometries… am i correct in this one?"*

**Correct**, and the module checks it rather than asserting it (`e0_is_outside`):

- e₀ is **not a point of PG(3,2)** — the projective skeleton is the 15 pure imaginaries.
- e₀ is **in no Assessor** — Assessors are planes spanned by pure imaginaries, and e₀ spans none.
- e₀ is **a vertex of no box-kite.**
- **[e₀, ·, ·] = 0 always** — the identity is central and associates with everything.

It generates the boundary and does not live on it, the way d generates ∂ without being a manifold, or a Hamiltonian generates the flow without being the phase space.

And it shows up in the spectrum: **the zero mode is e₀'s signature** — the mode that exists everywhere and propagates nowhere. That falls out of the graph. It is not put in.

## 6. The curvature is the associator

```
[a,b,c] = (ab)c − a(bc)     curvature
[a,b]   = ab − ba           torsion
```

**1848 of 4096** basis triples curve. `associator_field(s)` paints the defect onto a box-kite's vertices and edges: where the field is large, the geometry is bending. That is the debug view — the thing that makes the geometry *watchable* instead of inferred.

## 7. THE FINDING: the charts do not touch

Assembling all 42 Assessors into one graph gives **84 edges and zero cross-strut edges.** The seven box-kites are mutually disconnected under zero-divisor adjacency; the glued Laplacian carries seven zero modes, one per component.

This is a result, and it **changes the shape of the open problem.** A disturbance cannot propagate between charts along ZD adjacency, so either:

1. the medium genuinely is seven disconnected octahedra, and there is no global dispersion relation to find — the hydrocline is seven separate ponds; or
2. the connection between charts is the **PSL(2,7) action permuting the struts** — the transition maps are *group elements*, not edges.

(2) is where to look, and it is consistent with §1: if the exact object is PSL(2,7), then its action is the structure, and adjacency was always the wrong place to expect the gluing.

Also: **84 is both ZD_PAIRS and the atlas edge count** — 42 vertices at degree 4 gives 42×4/2 = 84. One number, two readings.

## 7b. Do the Charts Touch? — yes, in the skeleton (v0.2, 2026-08-05)

Cody: *"i'm pretty sure that those 'surfaces' do actually touch somewhere… they are all from the fixed point anyway… but now we have a clue that 0_RB only points to 'fixed point space'… where the boundary and the geometries are the same thing, right?"*

**Correct**, and it does not contradict the zero-cross-strut-edges finding. They are two structures on one object:

| structure | relation | result |
|---|---|---|
| **adjacency** | zero-divisor products | 7 components, 7 zero modes — disconnected |
| **skeleton** | shared basis indices | every usable index in **6 of 7** charts — almost totally overlapping |

For strut s an Assessor is (a, (a XOR s)+8), valid whenever a ≠ s — so index a sits in every chart *except* s = a. Every chart pair shares exactly **10** skeleton points. The charts touch everywhere in the skeleton and nowhere in the products.

**And exactly two basis elements are in no Assessor: e₀ and e₈.** e₀ is the identity — ∅_RB, the fixed point. e₈ is the Cayley–Dickson doubling generator. Each chart carries one zero mode, and a zero mode is the constant function — **seven copies of one object.** Identify them and the atlas connects, and that identification happens at e₀ and nowhere else.

That is the precise sense in which ∅_RB points to fixed-point space *where the boundary and the geometries are the same thing*: at the fixed point the boundary generator and the geometry's own mode are the same vector. Away from it they separate.

Functions: `index_chart_membership`, `skeleton_overlap`, `fixed_point_gluing`.

## 7c. The Chart of Addresses

The connector to the monad. Its hyperindexing addresses each surface form to a 16-vector (`VAPMIP/monad_sedenion_addresses.pkl`, `book[name]["sedenion"]`); `chart_of(v)` reports exhaustively where that address sits:

```
norm, peak_dim, fixed_point_weight, energy_split (e₀ / e₈ / lower / upper)
chart_energy (all 7), dominant_chart, chart_share
nearest_assessor, d_plus, d_minus, dominant_diagonal
local_curvature (associator defect at the dominant directions)
is_zero_divisor, outside_share
```

`address_census(addresses)` runs it over a whole corpus — descriptive only, counts and distributions, nothing scored against an expectation.

### Census over the monad book (3288 entries)

```
all 42 Assessors occupied
mean fixed-point weight   0.6435    (min 0.0583, max 1.0000)
mean outside share e₀+e₈  0.6537
peak_dim = 0              2751 of 3288  (84%)
dominant chart            strut 2: 30.1%  …  strut 7: 2.2%
mean local curvature      8.37
```

**About two thirds of the average address's energy sits outside the ZD geometry entirely.** Cody's "they are all from the fixed point anyway", measured.

Worth connecting to Phase 23's independent finding that the monad's projections carry ~85% common mode with 2–3% content: this **localises the common mode to e₀ + e₈** — the two basis elements belonging to no Assessor. The part of an address living outside the geometry is exactly the part carrying no discriminating signal.

Descriptive. Not a result about translation.

## 8. Honest boundaries

- The 84 edges are within-strut only. `glued_graph()`/`glued_spectrum()` are an **instrument reading, not a derivation** of the global medium, and say so in their own docstrings.
- The PSL(2,7)-as-transition-map is a **conjecture**, named as the next step, not a result.
- `is_assessor()` is O(4·49) products per call — fine at this scale, and the scale is fixed at 16 dimensions. No claim is made about T₃₂ and above.

## Summary

The object is PSL(2,7), order 168, not G₂ — G₂ is the blow-up that forgets the labelling. The geometry is seven octahedral charts on 42 Assessors, every count derived from the multiplication table and agreeing with both the literature and ValaQuenta's own constants. Each chart's dispersion relation is {0,4,4,4,6,6}, and its zero mode is ∅_RB's signature: everywhere, propagating nowhere — confirming that the boundary generator is not the boundary. The associator is the curvature and is now paintable.

And the charts do not touch. The gluing is not an edge problem. It is a group-action problem.
