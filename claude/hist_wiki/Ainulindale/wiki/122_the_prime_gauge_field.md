# 122 — The Prime Gauge Field

**Measured 2026-09-21.** Continues [[121_fast_inverse_square_root_of_the_two_trees]].
Engine: `ValaQuenta/modules/prime_gauge_field/`. Every number below is
computed there, not asserted, checked against a finite-difference
derivative and a 2000-point random sample before being written down.

---

## The question 121 left open

121 named the actual open thread precisely: the Smith-chart Schwarzian-
derivative check (`.claude/scratchpad/2026-09-21_smith_apollonian_uft_probe/`)
found `Γ(s)=(s−1)/(s+1)` carries no classical gauge curvature — true, and
narrower than it looks, because it tested one fixed, global Möbius map.
Weyl's own 1918 move — the origin of the word "gauge" — was to make
**scale itself** a local, position-dependent freedom, and read the
curvature of *that* connection. That version was never run. This page
runs it.

## Two connections, one provably flat, one not

`A = ∇(log|Γ|)` — flat everywhere, for any holomorphic scalar at all
(Poincaré lemma). This isn't a fact about `Γ`; it's forced by any object
of that shape. Confirms 121's negative result was never Γ-specific.

`A = (Re Γ(s), Im Γ(s))` — `Γ` itself, read as a genuine `ℝ²` connection
rather than collapsed to one complex value. Exact closed form:

    F(s) = 2·Im(Γ'(s))

verified against finite differences, error `~1e-11`. **This one is not
flat.** It carries real curvature almost everywhere on the `s`-plane.

## The prediction, checked, partial

121's stated prediction, before this was computed: the flat locus is the
construction's vacuum — where the local gauge freedom does nothing. The
measured zero locus of `F(s)`, exact, confirmed on 2000 random points
with zero mismatches:

- **the real axis** (`t=0`) — `Γ` is real-valued here; the "phase"
  degree of freedom the connection is built from is doing nothing. A
  legitimate reading of "vacuum," and it matches.
- **`σ=−1`** — the vertical line through `Γ`'s own pole. Not named in
  the prediction. New. Reported as new, not retrofitted.

So: **half right.** The trivial-phase locus behaves the way the vacuum
was expected to. The pole line is a second, unpredicted flat locus, and
the honest record keeps it separate rather than declaring victory on
the whole prediction.

## What this does and doesn't settle

Settles: a genuinely local reading of Telperion's own scale connection
*can* carry curvature — the flat Schwarzian result was about a
particular (global) construction, not a ceiling on what any local-scale
object built from `Γ` can do. Does not settle: whether this specific
connection (`(Re Γ, Im Γ)` as a 1-form) is *the* right local-gauge
object, or one convenient candidate among several — no uniqueness
argument was made for this choice over another; it is the most direct
reading of "Γ itself as a connection" and nothing more was claimed for
it going in.

## Related

- [[121_fast_inverse_square_root_of_the_two_trees]] — the Weyl citation, the naming, the open thread this page closes one layer of.
- [[93_qm_gr_by_tree]] — the same GR-is-a-boundary-phenomenon theme, different mechanism.
- `ValaQuenta/wiki/prime_gauge_field.md` — the engine-side page, reproduction instructions.
- `GenerationalLineage/engine/toolsets/scale.py` — `Γ`, unmodified, the object this whole page is built on.
- `FourthAgePapers/FastInverse/README.md` — the paper this engine's pre-registered prediction came from.
