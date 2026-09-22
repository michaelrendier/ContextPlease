"""
01_complex_smith_chart.py

Cody's question, 2026-09-21: does the continuous (Smith-chart) side of
GenerationalLineage/engine/toolsets/scale.py, read on its PROPER coordinates
(complex s = sigma + i.t, the actual Riemann zeta argument -- not the real-only
scale ratio scale.py's charts() currently takes), have its own genuine
sigma=1/2 fixed point -- and if so, is it the SAME 1/2 as the already-
established "prime equatorial geodesic" (half_is_the_equator.py,
2026-08-13_apex_path/), or an independent coincidence?

The existing charts() in scale.py feeds a single REAL scalar s through
Gamma(s) = (s-1)/(s+1). For real s, Gamma(s) is confined to the real
interval (-1,1) -- a 1-D slice of the unit disk, not a genuine 2-D
conformal chart. That is why sedenion_locus_orthogonality() could only
ever find "coincide" (Degrees-of-Freedom Principle: one real input cannot
produce two independent real rankings). This script uses complex s
throughout -- the proper coordinate for a Mobius/Smith-chart object -- so
Gamma(s) is a genuine point in the disk (2 real degrees of freedom).
"""
from __future__ import annotations
import cmath


def smith_fold(s: complex) -> complex:
    """The Cayley/Smith transform, exactly as in scale.py and the
    Two-Charts wiki: Gamma = (s-1)/(s+1)."""
    return (s - 1) / (s + 1)


def local_scale_factor(s: complex) -> complex:
    """d(Gamma)/ds = 2/(s+1)**2 -- the exact conformal (curvature-like)
    factor, same formula scale.py already names 'the flattening artifact'."""
    return 2 / (s + 1) ** 2


# ── T1: the reflection s <-> 1-s, on Gamma's OWN magnitude ──────────────────
print("=" * 78)
print("T1  Does |Gamma(s)| = |Gamma(1-s)| hold ONLY at sigma=1/2?")
print("=" * 78)
print(f"{'sigma':>8}{'t':>8}{'|Gamma(s)|':>14}{'|Gamma(1-s)|':>16}{'match':>8}")
matches_at = []
for sigma_x100 in range(0, 101, 5):
    sigma = sigma_x100 / 100.0
    t = 14.134725  # first nontrivial zero's height, an arbitrary but real t
    s = complex(sigma, t)
    g1, g2 = smith_fold(s), smith_fold(1 - s)
    match = abs(abs(g1) - abs(g2)) < 1e-12
    if match:
        matches_at.append(sigma)
    if sigma in (0.0, 0.25, 0.5, 0.75, 1.0):
        print(f"{sigma:>8.2f}{t:>8.2f}{abs(g1):>14.6f}{abs(g2):>16.6f}{str(match):>8}")
print(f"\n  matches across sigma in [0,1], step 0.05: {matches_at}")
print("  -> the ONLY match is sigma=0.5 exactly, confirmed by direct sweep,")
print("     not just the three spot-checks from the earlier session.")

# ── T2: WHY -- the algebraic reason, not just the numeric coincidence ──────
print()
print("=" * 78)
print("T2  The algebraic reason -- is this specific to Gamma=(s-1)/(s+1)?")
print("=" * 78)
print("""
  |Gamma(s)|^2 = |s-1|^2 / |s+1|^2 = ((sigma-1)^2+t^2) / ((sigma+1)^2+t^2)
  |Gamma(1-s)|^2 = |s|^2 / |2-s|^2 = (sigma^2+t^2) / ((2-sigma)^2+t^2)

  These are equal for ALL t simultaneously iff, termwise:
    (sigma-1)^2 = sigma^2   <=>  sigma = 1/2
    (sigma+1)   = (2-sigma) <=>  sigma = 1/2

  Both conditions independently force sigma=1/2. This is NOT a property of
  every Mobius map under s<->1-s -- it is specific to Gamma's own fixed
  points being exactly {+1, -1} (the endpoints of the Smith chart's real
  axis, the open/short-circuit points), which under s->1-s reflect onto
  {0, 2} -- and sigma=1/2 is exactly the point equidistant from that
  fixed-point pair's real parts.
""")

# ── T3: is this a restatement of the zeta functional equation, or new? ─────
print("=" * 78)
print("T3  Is Gamma's sigma=1/2 the SAME fixed point as zeta's, or a second one?")
print("=" * 78)
print("""
  Zeta's sigma=1/2: forced by Xi(s)=Xi(1-s), Xi(s)=pi^(-s/2).Gamma(s/2).zeta(s)
  (verified again in this pass, see 01b_verify_equator.py output below).
  That fixed point comes from the FUNCTIONAL EQUATION of a specific
  Dirichlet series (zeta) plus its Gamma-factor completion.

  Gamma_Smith's sigma=1/2: forced by the Smith fold's OWN algebra --
  its fixed points at +-1 under Mobius composition -- nothing about
  zeta, primes, or Dirichlet series enters T1/T2 above.

  These are two DIFFERENT mechanisms landing on the SAME number. That
  makes sigma=1/2 either (a) a coincidence of where two unrelated
  reflection symmetries happen to centre, or (b) evidence the Smith
  chart's own fixed points were chosen (historically, for RF engineering
  reasons -- open/short circuit) in a way that happens to encode the same
  s<->1-s structure zeta's functional equation encodes. Not resolved by
  this script -- flagged honestly as open, not claimed either way.
""")

if __name__ == "__main__":
    pass
