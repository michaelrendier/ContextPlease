"""
04_orthogonality_at_the_half.py

The direct question: does Smith's own sigma=1/2 (script 01, a genuine
fixed point of |Gamma(s)|=|Gamma(1-s)|, forced by Gamma's fixed points
+-1) coincide with anything independently special on the Apollonian
gasket's own discrete (generation, move_index) address (script 03) --
OR is any apparent coincidence just Smith's symmetry propagating into
the discrete side because the discrete lookup was DRIVEN by Gamma's own
output? Distinguishes the two honestly, rather than reporting only
whichever one looks like a positive result.
"""
from __future__ import annotations
from typing import Dict, Tuple
import sys
sys.path.insert(0, '.')
from gasket_addresses_lib import smith_fold, gasket_addresses  # noqa: E402


def nearest_curvature(mag: float, addr: Dict[int, Tuple[int, int]]) -> int:
    rungs = sorted(k for k in addr if k > 0)
    return min(rungs, key=lambda k: abs(k - mag))


addr = gasket_addresses(400)

print("=" * 78)
print("TEST 1 (confounded, reported honestly as such): discrete lookup")
print("DRIVEN BY |Gamma(s)| itself -- symmetry is inherited, not independent")
print("=" * 78)
t = 14.134725
print(f"{'sigma':>8}{'|Gamma(s)|':>13}{'nearest_k':>11}{'generation':>12}{'move':>7}")
for sigma_x100 in (0, 25, 45, 50, 55, 75, 100):
    sigma = sigma_x100 / 100.0
    s = complex(sigma, t)
    g = smith_fold(s)
    k = nearest_curvature(abs(g), addr)
    gen, mv = addr[k]
    print(f"{sigma:>8.2f}{abs(g):>13.6f}{k:>11}{gen:>12}{mv:>7}")
print()
print("  As expected: symmetric about sigma=0.5 by construction, because")
print("  |Gamma(s)|=|Gamma(1-s)| was already proven exactly (script 01) and")
print("  THIS test just relabels that same number through a monotone lookup.")
print("  This is NOT independent confirmation -- flagged, not claimed as one.")

print()
print("=" * 78)
print("TEST 2 (the real test): does the gasket's OWN (generation, move)")
print("structure show anything special at its OWN natural midpoint,")
print("with NO Gamma involved at all?")
print("=" * 78)
gens = sorted(set(g for g, m in addr.values()))
print(f"  generations present: {gens}")
print(f"  max generation: {max(gens)}")
mid_gen = max(gens) / 2
print(f"  arithmetic midpoint generation: {mid_gen}")
counts_by_gen = {g: sum(1 for gg, mm in addr.values() if gg == g) for g in gens}
print(f"  curvature-count by generation: {counts_by_gen}")
print()
print("  No reflection symmetry is defined on (generation, move_index) at")
print("  all -- generation only increases (it is a BFS depth, not a signed")
print("  coordinate), and move_index in {0,1,2,3} has no natural involution")
print("  making move i <-> move (3-i) meaningful (the four Descartes moves")
print("  are not paired by any symmetry of the seed (-1,2,2,3), which has")
print("  only a 2-fold symmetry from its two equal k=2 members, not a full")
print("  4-fold one).")
print()
print("  VERDICT: no independent sigma=1/2 (or any reflection midpoint) was")
print("  found on the discrete side under its own steam. Test 1's symmetry")
print("  is entirely inherited from Smith; Test 2 finds nothing to inherit")
print("  it from.")

print()
print("=" * 78)
print("HONEST FINAL VERDICT for this leg of the question")
print("=" * 78)
print("""
  The two 1/2's do NOT independently coincide. There is exactly one 1/2 in
  this picture -- Smith's (and, separately, zeta's own, via the already-
  verified pi-factored equator) -- and the Apollonian gasket, searched
  three ways (definitional radius, Hausdorff-dimension symmetry, Ford-
  circle analogy) plus a direct structural check here, contributes no
  second, independent one for it to meet. Where the earlier
  sedenion_locus_orthogonality() found "coincide," it was because BOTH
  sides were secretly one-dimensional functions of one shared input
  (Degrees-of-Freedom Principle). Here, with genuine 2-D coordinates on
  both sides, the same coincidence does NOT reappear except where it is
  manufactured by feeding one side's output into the other (Test 1) --
  which is honest to say plainly, not a discovery.

  This does not close the door on Smith-Apollonian orthogonality
  producing something UFT-shaped -- it closes THIS specific door (a
  shared 1/2). What remains open and untested: whether the TILT between
  the two charts (scale.py's own unbuilt quantity) -- not their shared
  fixed point, but their DIFFERENCE at a fixed sigma -- has structure
  matching 0_RB's R_p tensor d_dM + h.c. shape. That is a different,
  not-yet-attempted test.
""")
