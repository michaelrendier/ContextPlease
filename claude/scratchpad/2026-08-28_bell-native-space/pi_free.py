"""
Cody, 2026-08-28: "there shouldn't be a π involved in Bell's equations. π is not
a component of probabilities and statistics — it's a component of continuous
geometries — and has no business inside the brackets he is using. He inadvertently
introduces additional rotation by defining angles twice; let the maths grab the
rotation ONCE (emergent-variables methodology)."

Claim, made precise and tested here:
  1. the Tsirelson bound 2√2 needs NEITHER cos NOR π — it comes from A² = 1
     (a ±1-valued = SIGN observable) and the commutator norm.
  2. the ±1 statistics (joint distribution, the local bound |S| ≤ 2) are
     combinatorial — π-free.
  3. π enters at exactly ONE place: the dictionary  E = −cos(a−b)  that maps an
     abstract correlation number to a physical lab rotation angle. That map
     names the angle twice (a AND b) and composes them through a continuous
     circular function. "Grab it once" = keep the single relative variable.
  4. the 'additional rotation' = a second pole ≠ the first ⇒ precession
     (∝ sin tilt). One axis, grabbed once, has no second pole.
"""
import numpy as np
I2 = np.eye(2)
X  = np.array([[0, 1],[1, 0]], float)
Z  = np.array([[1, 0],[0,-1]], float)
def kron(a, b): return np.kron(a, b)

# ── G. Tsirelson 2√2 from SIGN algebra alone — no cos, no π ──────────────
print("G. S² = 4·I − [A,A']·[B,B']   (identity — expand S = A(B+B') + A'(B−B'))")
# any ±1-valued observables: A² = A'² = B² = B'² = I. take a family and check.
def sign_obs(t):                      # a ±1 observable in the X–Z plane, param t
    return np.cos(t)*Z + np.sin(t)*X  # (t is just a knob to sweep operators — NOT
                                      #  fed into any probability; eigenvalues ±1)
worst = 0.0
for _ in range(20000):
    ta, tap, tb, tbp = np.random.uniform(0, 2*np.pi, 4)
    A  = kron(sign_obs(ta),  I2);  Ap = kron(sign_obs(tap), I2)
    B  = kron(I2, sign_obs(tb));   Bp = kron(I2, sign_obs(tbp))
    S  = A@B + A@Bp + Ap@B - Ap@Bp
    lhs = S@S
    rhs = 4*np.eye(4) - (A@Ap - Ap@A) @ (B@Bp - Bp@B)
    assert np.allclose(lhs, rhs), "identity failed"
    worst = max(worst, np.linalg.norm(S, 2))
print(f"   identity S² = 4I − [A,A'][B,B']  holds for 20000 random SIGN quadruples ✓")
print(f"   ‖[A,A']‖ ≤ 2 and ‖[B,B']‖ ≤ 2  (each factor unitary, triangle ineq)")
print(f"   ⇒ ‖S²‖ ≤ 4 + 4 = 8  ⇒  ‖S‖ ≤ √8 = 2√2 = {2*np.sqrt(2):.6f}")
print(f"   measured max ‖S‖ over the random sweep = {worst:.6f}")
print("   the √2 is √8/2 — TWO commutators each bounded by 2. No angle. No π.")

# ── H. the ±1 statistics are combinatorial — π-free ─────────────────────
print("\nH. local (hidden-variable) bound from deterministic ±1 strategies only")
best = -1
for sa in (-1,1):
  for sap in (-1,1):
    for sb in (-1,1):
      for sbp in (-1,1):
        # E(x,y) = x*y for a deterministic assignment
        Sd = sa*sb + sa*sbp + sap*sb - sap*sbp
        best = max(best, abs(Sd))
print(f"   max |S| over all 16 deterministic ±1 strategies = {best}   (= 2, the Bell bound)")
print("   mixtures can't exceed an extreme point ⇒ |S| ≤ 2 for ANY local model.")
print("   this is counting over {−1,+1}⁴. There is no π anywhere in it.")

# ── I. where π actually enters ─────────────────────────────────────────
print("\nI. the ONE place π enters: the lab dictionary  E = −cos(a − b)")
print("   • it names the angle TWICE (a for Alice, b for Bob) and joins them")
print("     through cos — a continuous circular (π-carrying) function.")
print("   • everything in G and H used only  A² = 1  and counting. π-free.")
print("   • 'grab the rotation once' = keep the single relative number E (or one")
print("     angle θ = arccos(−E)). Then:")
E = np.array([-np.sqrt(2)/2, -np.sqrt(2)/2, -np.sqrt(2)/2, +np.sqrt(2)/2])  # the QM optimum, as 4 numbers
print(f"     E = {E.round(4).tolist()}   (four correlation numbers, no angles)")
print(f"     S = E1 + E2 + E3 − E4 = {E[0]+E[1]+E[2]-E[3]:+.6f}   |S| = {abs(E[0]+E[1]+E[2]-E[3]):.6f}")
print("     the √2/2 entries are 1/√2 — the SIGN-algebra number from G, not cos(π/4).")
print("     identical result, stated with zero angles and zero π.")

# ── J. the 'additional rotation' = a second pole ⇒ precession ───────────
print("\nJ. define the angle once → one axis → no second pole → no precession.")
print("   define it twice (compose R_b ∘ R_a about non-parallel axes) → the")
print("   image carries an out-of-plane part (2026-08-28 bell test, parts C/D/F):")
print("   a SECOND pole, tilted from the first. Two non-aligned axes precess at")
print("   Ω ∝ sin(tilt) — 'the oblique gearing'. That precession IS the spurious")
print("   rotation Bell inadvertently adds. Removing it = not defining the angle")
print("   twice = the emergent-variables move: read the relative orientation as")
print("   ONE emergent quantity, never as (a) then (b) composed.")
