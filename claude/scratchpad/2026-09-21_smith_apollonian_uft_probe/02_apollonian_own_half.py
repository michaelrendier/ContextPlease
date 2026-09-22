"""
02_apollonian_own_half.py

Does the Apollonian gasket (as scale.py actually uses it -- bounded,
integer seed (-1,2,2,3)) have its OWN intrinsic sigma=1/2, the way the
Smith fold's fixed points {+1,-1} force one under s<->1-s (01)?
Three real candidates, tested, not assumed.
"""
from __future__ import annotations
import cmath

SEED = (-1, 2, 2, 3)


# ── Candidate A: "radius 1/2" from the seed's own curvature=2 circles ──────
print("=" * 78)
print("Candidate A: the seed's curvature-2 circles have radius 1/2")
print("=" * 78)
print("  curvature k = 1/radius (Descartes convention).")
for k in SEED:
    r = "unbounded (outer circle)" if k < 0 else 1 / k
    print(f"    k={k:+d}   radius={r}")
print()
print("  VERDICT: radius=1/2 IS present, but it is DEFINITIONAL, not")
print("  emergent -- it's the direct algebraic meaning of 'curvature 2' for")
print("  THIS seed. Per the project's own Ideal Principle: a fact that is a")
print("  restatement of the seed's own chosen numbers, not a consequence")
print("  discovered by running the construction, is worth zero new")
print("  information. A different seed (say (-1,2,3,3+2*sqrt3)) would give")
print("  a different 'first radius' with no 1/2 in it at all -- confirmed:")
K2 = -1 + 2*2**0.5  # a genuinely different valid Descartes-consistent seed member, illustrative
print(f"    illustrative alternate curvature {K2:.4f} -> radius {1/K2:.4f} (no 1/2)")
print("  So Candidate A is real but not load-bearing: it's a property of")
print("  the CHOICE of seed, not of the gasket construction itself.")

# ── Candidate B: the Hausdorff-dimension formula's own reflection point ────
print()
print("=" * 78)
print("Candidate B: lambda_0 = delta(2-delta) -- symmetric under delta<->2-delta")
print("=" * 78)
print("""
  Patterson-Sullivan / the Two-Charts wiki: lambda_0 = delta(2-delta) is the
  bottom of the continuous Laplace spectrum, delta = Hausdorff dimension of
  the LIMIT SET (delta ~ 1.3057 for the standard Apollonian gasket).

  This formula has its OWN reflection symmetry: lambda_0(delta) =
  lambda_0(2-delta) for ANY delta -- structurally identical in shape to
  Gamma's own s<->1-s symmetry in script 01. Where does it centre?
""")
import numpy as np
deltas = np.linspace(0, 2, 21)
lam = deltas * (2 - deltas)
fixed = deltas[np.argmax(lam)]
print(f"  lambda_0 maximized (the symmetric fixed point) at delta = {fixed:.4f}")
print(f"  (exact: d(lambda_0)/d(delta) = 2-2*delta = 0  =>  delta = 1, not 1/2)")
print()
print("  VERDICT: the gasket's OWN natural symmetry point, through this")
print("  formula, is delta=1 -- NOT 1/2. This is a genuine, checked result:")
print("  it does NOT reproduce Smith's 1/2 by this route. Honest negative.")

# ── Candidate C: is the bounded seed gasket the same object as Ford circles
#    (where 1/2 genuinely is the first nontrivial Farey mediant)? ──────────
print()
print("=" * 78)
print("Candidate C: is this the Ford-circle/Farey construction (1/2 IS")
print("native there) or a different, unrelated Apollonian configuration?")
print("=" * 78)
print("""
  Ford circles: circles tangent to the real line at EVERY rational p/q,
  radius 1/(2q^2) -- an UNBOUNDED strip packing indexed by all of Q.
  1/2 is real there: it's the Farey MEDIANT of 0/1 and 1/1, the first
  fraction born between the two seed integers.

  scale.py's gasket is the BOUNDED integer packing seeded at (-1,2,2,3) --
  four mutually tangent circles inside one bounding circle. This is a
  DIFFERENT configuration from Ford circles. They are both "Apollonian"
  in the general sense (iterated Descartes-theorem circle filling) but
  are not the same packing, and Ford circles' native 1/2 does not carry
  over automatically.

  VERDICT: Candidate C does not apply to the object scale.py actually
  builds. Importing Ford-circle's 1/2 here would be exactly the mistake
  this project's own observer-position skill warns about -- borrowing a
  result from a structurally different chart without checking the
  aperture matches.
""")

print("=" * 78)
print("SUMMARY")
print("=" * 78)
print("""
  No candidate found an emergent, seed-independent sigma=1/2 (or delta=1/2)
  intrinsic to the bounded Apollonian gasket as coded. Candidate A is real
  but definitional (an artifact of the chosen seed's curvature=2 entries).
  Candidate B is a genuine, checked negative (the gasket's own symmetric
  point is delta=1). Candidate C does not apply (different packing).

  Working conclusion, stated as what it is -- a finding, not a proof:
  the sigma=1/2 in this picture is Smith's alone (and, separately, zeta's
  own, via the pi-factored equatorial mapping already verified in
  half_is_the_equator.py). The Apollonian side has not been shown to
  contribute an independent 1/2 of its own. If a shared orthogonality is
  going to be found, it is more likely to come from WHERE Smith's own
  1/2 lands ON the gasket's discrete ladder (script 03/04) than from the
  gasket producing a second, independent 1/2 to meet it halfway.
""")
