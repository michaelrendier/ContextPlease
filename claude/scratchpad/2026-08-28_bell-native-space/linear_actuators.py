"""
Cody, 2026-08-28: "does that change his results if we look at it without the π
and extra rotations... can they be represented as linear actuators?"

Two questions, answered:

Q1  Does stripping π + the composed rotation change Bell's RESULTS?
    NO. 2√2 and 2 are both coordinate-free. The violation stands. What changes:
    the excess over 2 is revealed as EXACTLY the operator non-commutativity
    ‖[A,A'][B,B']‖ — a SIGN-algebra fact, with no geometry attached.

Q2  Can the measurements be linear actuators instead of rotary?
    YES. A ±1 observable (A² = 1) is a REFLECTION / SIGN operator, not a
    rotation. Its setting can be swept by a LINEAR coordinate t via the
    stereographic (Cayley / Smith) fold  t = tan(a/2). In t-coordinates the
    correlation is a RATIONAL function — algebraic, no cos, no π. "Grab the
    rotation once" = one relative linear coordinate t_rel.
"""
import numpy as np
Z = np.array([[1, 0],[0,-1]], float)
X = np.array([[0, 1],[1, 0]], float)

# ── A ±1 observable is a REFLECTION (SIGN), not a rotation ───────────────
def A_angle(a):  return np.cos(a)*Z + np.sin(a)*X      # rotary parametrisation
print("Q2a.  the observable A(a) = cos a·Z + sin a·X:")
for a in [0.3, 1.1, 2.7]:
    M = A_angle(a)
    ev = np.linalg.eigvalsh(M)
    print(f"   a={a:.2f}:  A² = I? {np.allclose(M@M, np.eye(2))}   det = {np.linalg.det(M):+.3f}"
          f"   eigenvalues = {ev.round(3).tolist()}   → a REFLECTION (SIGN), det −1")

# ── LINEAR-ACTUATOR parametrisation:  t = tan(a/2),  linear sweep of t ───
#   stereographic: the linear throw t maps to rotary angle a = 2·arctan(t),
#   with cos a = (1−t²)/(1+t²),  sin a = 2t/(1+t²)  — all RATIONAL in t.
def A_lin(t):
    c = (1.0 - t*t) / (1.0 + t*t)
    s = (2.0 * t)   / (1.0 + t*t)
    return c*Z + s*X
print("\nQ2b.  linear-actuator parametrisation  A_lin(t),  t = tan(a/2):")
print("   sweep t on a straight line; a = 2·arctan(t) hits every rotary setting once.")
for a in [0.0, np.pi/4, np.pi/2, 3*np.pi/4]:
    t = np.tan(a/2)
    print(f"   a={a: .4f}  ↔  t={t: .4f}   ‖A_angle(a) − A_lin(t)‖ = "
          f"{np.linalg.norm(A_angle(a) - A_lin(t)):.2e}   (A_lin uses only ratios of t)")

# ── the correlation in t-coordinates: a RATIONAL function, no cos, no π ──
def E_angle(a, b):  return -np.cos(a - b)
def E_lin(ta, tb):
    # −cos(a−b) with cos a = (1−t²)/(1+t²), sin a = 2t/(1+t²)
    num = (1 - ta*ta)*(1 - tb*tb) + 4*ta*tb
    den = (1 + ta*ta)*(1 + tb*tb)
    return -num/den
print("\nQ2c.  correlation as a rational function of the linear coordinates:")
print("   E_lin(ta,tb) = −[(1−ta²)(1−tb²) + 4 ta tb] / [(1+ta²)(1+tb²)]")
rng = np.random.default_rng(0)
err = max(abs(E_lin(np.tan(a/2), np.tan(b/2)) - E_angle(a, b))
          for a, b in rng.uniform(-2, 2, (500, 2)))
print(f"   max |E_lin − E_angle| over 500 random (a,b) = {err:.2e}   (identical)")
print("   E_lin is a ratio of polynomials in ta,tb — algebraic. No cos. No π.")

# ── "grab the rotation once": ONE relative linear coordinate ────────────
def t_rel(ta, tb):  return (ta - tb) / (1 + ta*tb)     # Möbius addition
def E_rel(tr):      return -(1 - tr*tr) / (1 + tr*tr)
print("\nQ2d.  grab it ONCE — one relative linear actuator  t_rel = (ta−tb)/(1+ta tb):")
err = max(abs(E_rel(t_rel(np.tan(a/2), np.tan(b/2))) - E_angle(a, b))
          for a, b in rng.uniform(-2, 2, (500, 2)))
print(f"   E_rel(t_rel) matches −cos(a−b) to {err:.2e}.  One linear coordinate,")
print("   one rational function, ±1 outcomes. The rotation appears exactly once.")

# ── CHSH in linear coordinates — same 2√2, no π ────────────────────────
# optimal settings a=0, a'=π/2, b=π/4, b'=−π/4  →  their t = tan(a/2):
ta, tap = np.tan(0.0), np.tan(np.pi/4)                 # 0 , 1
tb, tbp = np.tan(np.pi/8), np.tan(-np.pi/8)            # √2−1 , −(√2−1)
S = E_lin(ta,tb) + E_lin(ta,tbp) + E_lin(tap,tb) - E_lin(tap,tbp)
print("\nQ1.  CHSH from the rational form, linear coordinates:")
print(f"   t = [0, 1, √2−1, −(√2−1)]  (these are LINEAR-ACTUATOR throws)")
print(f"   S = {S:+.6f}   |S| = {abs(S):.6f}   = 2√2  — unchanged.")
print("   the √2−1 throws are algebraic (silver-ratio conjugate), not 'π/8'.")

# ── Q1: the excess over 2 IS the non-commutativity, nothing else ───────
def kron(a,b): return np.kron(a,b)
A  = kron(A_lin(ta),  np.eye(2));  Ap = kron(A_lin(tap), np.eye(2))
B  = kron(np.eye(2), A_lin(tb));   Bp = kron(np.eye(2), A_lin(tbp))
Smat = A@B + A@Bp + Ap@B - Ap@Bp
comm = (A@Ap - Ap@A) @ (B@Bp - Bp@B)
print("\nQ1 (cont).  S² − 4·I  =  −[A,A'][B,B']   (exactly):")
print(f"   ‖S² − 4I + [A,A'][B,B']‖ = {np.linalg.norm(Smat@Smat - 4*np.eye(4) + comm):.2e}")
print(f"   ‖S‖ = √(4 + ‖[A,A'][B,B']‖) = √(4 + {np.linalg.norm(comm,2):.4f}) = {np.linalg.norm(Smat,2):.6f}")
print("   the entire excess of |S| over 2 is the operator non-commutativity.")
print("   strip π and the composed rotation → the violation is unchanged and")
print("   now reads as one fact: the two SIGN observables on each side don't")
print("   commute. ADD (the linear throw t) + SIGN (the ±1 outcome); SCALE lives")
print("   in the √(1+t²) fold. Ground-state form, no π.")
