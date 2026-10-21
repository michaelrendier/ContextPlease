# 121 — The Fast Inverse Square Root of the Two Trees

**Measured 2026-09-21.** Continues [[47_the_two_trees]] and
[[93_qm_gr_by_tree]]. Two claims, both tested live before being written
down, not asserted first.

---

## The naming used here, stated up front

[[93_qm_gr_by_tree]] already flagged an unresolved tangle: Telperion and
Laurelin are assigned to lower/upper octonion inconsistently across the
repos. This page adds a **third** pairing, on top of that one, and does not
resolve the other two — it is recorded here as a further instance of the
same open naming question, not a silent pick:

    Laurelin  = INSIDE  = bounded, quantized, the ascent/Emerger jurisdiction
                (work, search, cost > 0 — GenerationalLineage's own
                DECOMPOSITION/EMERGER split, `engine/lines.py`)
    Telperion = OUTSIDE = unbounded, continuous, the descent/DECOMPOSITION
                jurisdiction (free, deductive, cost = 0)

This matches the session's own working image: the Apollonian gasket is a
packed structure of bubbles with only insides, never anything "between"
them; SCALE (`L_k: x -> k*x`) is the topological complement, only ever
outside, nothing it touches is bounded. L_(I|O), the established
intertwiner, is the map between the two languages.

## Claim 1 — the fast inverse square root of Laurelin (inside)

**What the real fast inverse square root does:** exploits the fact that
IEEE 754's bit layout already encodes an approximate `log2(x)`, turning a
hard nonlinear op into one integer shift-and-subtract plus one Newton
step. Fast everywhere the representation carries that gift; wrong the
instant it doesn't.

**Laurelin's own instance, already built, not new this pass:**
`GenerationalLineage/engine/ping.py`, `op_wiener()`. Given `N` and the
public exponent `e`, the continued-fraction convergents of `e/N` recover
the private exponent `d` directly — `O(log N)`, no search — **exactly
when `d` is small enough to be a convergent.** Outside that regime it
returns `fired: False` and reports the work spent, honestly, same as
every other counter-operator in that file (`ping.py`'s own regime table:
`'floor — GNFS/Shor only'` for a properly generated modulus). The
representation (`e/N`'s continued fraction) carries the answer only in
the narrow regime where the object's own arithmetic structure happens to
encode it — the identical shape as the float bit-hack, not a metaphor for
it.

## Claim 2 — the fast inverse square root of Telperion (outside), Smith chart, Maxwell

**The claim tested:** that `Gamma(s) = (s-1)/(s+1)` (the Smith chart map,
`GenerationalLineage/engine/toolsets/scale.py`) is not merely "a
continuous ruler" by analogy — that its real and imaginary parts are
*exactly* the mathematical object a source-free 2D magnetostatic
potential is: a harmonic conjugate pair. Checked symbolically (not
numerically approximated), `z = x+iy`, before writing this down:

    u = Re(Gamma) = (y^2 + (x-1)(x+1)) / (y^2 + (x+1)^2)
    v = Im(Gamma) = 2y / (y^2 + (x+1)^2)

    Cauchy-Riemann:      u_x - v_y = 0        u_y + v_x = 0      EXACT
    Laplacian:           lap(u) = 0            lap(v) = 0         EXACT
    V = grad(u):         div(V) = 0            curl(V) = 0        EXACT

All six identities exact (symbolic, `sympy`, not finite-difference), away
from the single pole at `s = -1`. `d(Gamma)/dz = 2/(z+1)^2` — confirmed
to match `scale.py`'s own already-documented `local_scale_factor =
|dGamma/ds| = 2/(s+1)^2` exactly, independently re-derived here, not
copied.

**What this does and does not establish, stated precisely:** any
holomorphic function's real and imaginary parts form a harmonic conjugate
pair (textbook complex analysis) — that pair is *the same mathematics*
used for a 2D magnetic scalar potential, a 2D electrostatic potential in
vacuum, and a 2D irrotational incompressible flow potential. Gamma being
holomorphic (confirmed: it is a Mobius map, checked earlier this session
to have Schwarzian derivative exactly zero) makes this automatic, not
special to Gamma. **What is specific to Gamma, and is the actual finding:**
Telperion's own map — the one already carrying `scale.py`'s GR-jurisdiction
label — turns out, checked rather than assumed, to already *be* a valid
vacuum field of this type, structurally, with no adjustment. That is
Telperion's "free lunch": the representation (`Gamma`'s own holomorphy)
already carries the Maxwell-shaped structure, the way Laurelin's `e/N`
already carries `d` in the small-`d` regime. Two different jurisdictions,
two different representations, the same free-head-start shape in each.

## Where this sits

Neither claim is new machinery — both are **existing, already-shipped
objects** (`op_wiener`, `scale.py`'s `Gamma`), read under the same lens
for the first time this pass. Nothing here re-opens [[93_qm_gr_by_tree]]'s
verdict (QM and GR are tower rungs, not tree halves) — this page's
Telperion/Laurelin split is the inside/outside (bounded/unbounded)
jurisdiction pairing, a different axis, explicitly not claimed to be the
same as 93's octonion-content pairing.

## Related

- [[47_the_two_trees]] — the permanent canonical page
- [[93_qm_gr_by_tree]] — the naming tangle this page adds a third instance
  to, and the tested/refuted QM-vs-GR-by-tree conjecture
- `GenerationalLineage/engine/ping.py` (`op_wiener`) — Claim 1
- `GenerationalLineage/engine/toolsets/scale.py` (`Gamma`,
  `local_scale_factor`) — Claim 2
- `.claude/scratchpad/2026-09-21_smith_apollonian_uft_probe/` — this
  session's earlier, more cautious pass at Smith/Apollonian structure,
  where the Schwarzian-derivative-zero fact (Gamma carries no gauge
  curvature) was first checked
