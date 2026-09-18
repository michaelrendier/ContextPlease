# 2026-08-13_apex_path

An orphaned directory until 2026-09-17 — no README existed despite the
scratchpad's own convention requiring one. This entry only documents and
verifies `psl27_strut_action.py` in full (the file directly relevant to a
paper-writing question that session); the other files here are listed from
their own docstrings for reference, not run or verified as part of this pass.

## `psl27_strut_action.py` — verified 2026-09-17, output saved to `psl27_strut_action_output.txt`

**Question:** Phase 25's open conjecture — the box kite has zero cross-strut
edges (the 7 charts are mutually disconnected under zero-divisor adjacency);
either there is no global medium connecting them, or the transition maps
between the 7 charts are the **PSL(2,7) action on struts** (group elements,
not edges). Struts are `s = a XOR b` for `a,b in 1..7` — the 7 nonzero
vectors of `F_2^3`, the 7 points of the Fano plane, on which
`PSL(2,7) = GL(3,2) = Aut(Fano)` (order 168) acts.

**Test:** enumerate all 168 elements of `GL(3,2)`; check which of them,
acting on the sedenion basis indices, preserve the zero-divisor annihilation
relation among the 84 assessor diagonals (336 ordered annihilating pairs).

**Result:**
- `GL(3,2)` has order 168, confirmed against `|PSL(2,7)| = ZD_COMPOSITE`.
- The strut map is linear (`M(a) XOR M(b) = M(a XOR b)`) and the full group
  is transitive on the 7 struts, as expected.
- Only **21 of the 168** group elements preserve the zero-divisor structure —
  but that 21-element subset **is itself a subgroup** (closed under
  composition, sampled) and is **still transitive on all 7 struts**.
- **Conjecture holds**: every pair of the 7 box-kite charts is joined by a
  group element that carries the zero-divisor structure with it. The atlas
  is connected by group action — a genuine 21-element subgroup of
  `PSL(2,7)`, index 8 in the full group — not by an ad hoc per-chart
  construction.

This is a real, clean, reproducible result that had never been recorded
anywhere outside this uncommitted script until now.

## Other files in this directory (listed from their own docstrings, not run this pass)

- `cam_profile.py` — spec vs. engine check on Hermite-spaced CAM timing
  E-values (Tuning-the-Engine, "Hermite H16" calibration).
- `counter_rotation.py` — whether the Wankel's anti-rotation produces the
  off-critical-line Euler form claim (`σ ≠ 1/2` → not a pure phase rotation).
- `density_sweep.py` — a density-histogram fix to an escape-time CAM sweep
  that had gone monotone and flattened interior structure.
- `half_is_the_equator.py` — tests a specific claim about the `1/2` phase
  offset of an "equatorial geodesic" relative to the Riemann zeta function
  mapped to flat space.
- `half_radius_circle.py` — tests the claim that the relevant circle has
  radius `1/2`, not `1`.
- `hw_locate.py` — measures whether the Hyperwebster/Horner enumeration
  index is a scalar quantity landing on `e0` (the fixed point).
- `order_of_operations.py` — whether the sedenion basis carries an operation
  precedence, and whether `e0..e7` vs. `e8..e15` split "calculable" from
  "where opinion lives."
- `rb_boundary.py` — checks a specific eigenvalue-split claim
  (`{0, ±i, ±i√2}` at `{4,8,4}` multiplicity) against the Cayley–Dickson
  table directly.
- `shuffled_portrait_null.py` — a null test: does a "portrait" genuinely
  select words, or would any word list read as apt once wrapped in prose
  (real vs. shuffled-order vs. vocab-swapped controls).
- `two_tests.py` — an affix→morph-relation pass, and an `e0`-share-by-
  WordNet-degree test predicted by an earlier primer.
