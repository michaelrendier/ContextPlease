"""
Cody's Bell theory (2026-08-28):

  "when John Bell was explicitly adding a rotation upon an already-established
   angle, the sum was NOT the same as without it. It was not at the end of a
   circle's edge — it was another superfluous unintentional component which
   returned it to 'above or below' the original spot."

Restated: Bell puts the analyser settings on a CIRCLE (a great circle of S²,
colatitude θ = π/2) and treats 'add rotation δ' as  φ → φ + δ  — planar angle
addition, correlation a function of (φ_a − φ_b) only.

If the settings actually live on the SPHERE (Universal Native Space: spherical
complex radial polar, radial part ln(10)·log10 r — irrelevant to an ANGULAR
correlation), then 'add rotation δ on top of an established orientation' is a
COMPOSITION of rotations. Compose two rotations about non-parallel axes and the
result is NOT a rotation by the sum: the image vector leaves the great circle —
it lands 'above or below'. That out-of-plane displacement is the 'superfluous
unintentional component'. A pure (φ_a − φ_b) analysis cannot see it.

TEST:
  A  flat CHSH,  E(a,b) = −cos(a−b)                      → control, expect 2√2
  B  native-space CHSH, settings as unit 3-vectors on
     the EQUATOR, E = −â·b̂                                → expect 2√2 (native
                                                            space alone changes
                                                            nothing)
  C  native-space CHSH where 'add δ' = quaternion compose
     R(n̂, δ) ∘ (current orientation), n̂ tilted off ẑ by
     ε.  Scan ε.  Report S(ε) and max |b̂_z| (the
     superfluous component).
  D  the composition defect itself:  q(ẑ',δ)∘q(ẑ,α)  vs
     q(ẑ, α+δ)  — show the residual vector, show it is
     zero iff the axes are parallel (the flat circle).
"""
import numpy as np

# ── quaternion helpers (SU(2) — the native rotation rep, ℍ level of the CD tower)
def quat(axis, angle):
    axis = np.asarray(axis, float); axis = axis / np.linalg.norm(axis)
    return np.concatenate([[np.cos(angle/2)], np.sin(angle/2) * axis])

def qmul(p, q):
    w1, x1, y1, z1 = p; w2, x2, y2, z2 = q
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2,
    ])

def qrot(q, v):
    w, x, y, z = q
    R = np.array([
        [1-2*(y*y+z*z),   2*(x*y-z*w),   2*(x*z+y*w)],
        [  2*(x*y+z*w), 1-2*(x*x+z*z),   2*(y*z-x*w)],
        [  2*(x*z-y*w),   2*(y*z+x*w), 1-2*(x*x+y*y)],
    ])
    return R @ np.asarray(v, float)

SQRT2 = np.sqrt(2.0)

# ── A. flat CHSH ─────────────────────────────────────────────────────────
def E_flat(a, b): return -np.cos(a - b)
a, ap, b, bp = 0.0, np.pi/2, np.pi/4, -np.pi/4
S_flat = E_flat(a,b) + E_flat(a,bp) + E_flat(ap,b) - E_flat(ap,bp)
print("A. flat CHSH   E(a,b) = −cos(a−b)")
print(f"   settings  a=0  a'=90°  b=45°  b'=−45°")
print(f"   S = {S_flat:+.6f}   |S| = {abs(S_flat):.6f}   (2√2 = {2*SQRT2:.6f})")

# ── B. native space, settings on the EQUATOR, E = −â·b̂ ───────────────────
def vec(theta, phi):
    return np.array([np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)])
def E_vec(u, w): return -float(np.dot(u, w))
th = np.pi/2
va, vap, vb, vbp = (vec(th,a), vec(th,ap), vec(th,b), vec(th,bp))
S_equ = E_vec(va,vb) + E_vec(va,vbp) + E_vec(vap,vb) - E_vec(vap,vbp)
print("\nB. native space, settings on the equator (θ=90°), E = −â·b̂")
print(f"   S = {S_equ:+.6f}   |S| = {abs(S_equ):.6f}   → native space ALONE changes nothing")

# ── C. 'add δ' = quaternion compose about an axis tilted off ẑ by ε ──────
#    reference orientation r̂ = x̂.  each setting angle γ is applied as
#    r̂ →  R(n̂(ε), γ) · x̂,   n̂(ε) = (sin ε, 0, cos ε)   (tilted pole)
print("\nC. 'add rotation γ' = compose R(n̂,γ), pole n̂ tilted off ẑ by ε")
print(f"   {'ε (deg)':>8s} {'S':>12s} {'|S|−2√2':>12s} {'max|b̂_z|':>12s}  (superfluous component)")
xhat = np.array([1.0, 0.0, 0.0])
rows = []
for eps_deg in [0, 1, 2, 5, 10, 20, 30, 45]:
    eps = np.radians(eps_deg)
    n = np.array([np.sin(eps), 0.0, np.cos(eps)])
    def setting(gamma):
        return qrot(quat(n, gamma), xhat)
    va, vap, vb, vbp = setting(a), setting(ap), setting(b), setting(bp)
    S = E_vec(va,vb) + E_vec(va,vbp) + E_vec(vap,vb) - E_vec(vap,vbp)
    zmax = max(abs(va[2]), abs(vap[2]), abs(vb[2]), abs(vbp[2]))
    rows.append((eps_deg, S, abs(S) - 2*SQRT2, zmax))
    print(f"   {eps_deg:>8d} {S:>12.6f} {abs(S)-2*SQRT2:>12.6f} {zmax:>12.6f}")
print("   ε=0  → exactly 2√2, all b̂_z = 0 (flat circle).")
print("   ε>0  → |S| drops below 2√2, AND the settings acquire a z-component")
print("          they were never given — the vector is 'above/below' the circle.")

# ── D. the composition defect, explicitly ───────────────────────────────
print("\nD. composition defect:  R(n̂,δ)∘R(ẑ,α)  vs  R(ẑ,α+δ)   applied to x̂")
print(f"   {'axis tilt ε':>12s} {'|Δ residual|':>14s} {'Δ_z (out of plane)':>18s}")
alpha, delta = np.radians(35.0), np.radians(25.0)
for eps_deg in [0, 5, 15, 30, 60, 90]:
    eps = np.radians(eps_deg)
    n = np.array([np.sin(eps), 0.0, np.cos(eps)])
    v_compose = qrot(qmul(quat(n, delta), quat([0,0,1], alpha)), xhat)
    v_sum     = qrot(quat([0,0,1], alpha + delta), xhat)
    d = v_compose - v_sum
    print(f"   {eps_deg:>12d} {np.linalg.norm(d):>14.6f} {d[2]:>18.6f}")
print("   ε=0 (parallel axes = the flat circle): residual = 0, sum IS the sum.")
print("   ε≠0: R(n̂,δ)∘R(ẑ,α) ≠ R(ẑ,α+δ) — a residual with an out-of-plane (z)")
print("        part. That z-part is the 'superfluous unintentional component'")
print("        that returns the point to above/below its intended spot.")

# ── does the geometric defect EVER reproduce the local bound |S| = 2? ───
#   CORRECTED 2026-08-28 (Cody: "something is wrong there"): the earlier
#   bisection on [0°, 89°] just walked to its own ceiling because |S| > 2 for
#   every ε < 90°. There is NO threshold tilt. What actually happens:
print("\nE. scan the tilt toward 90° — does |S| ever reach 2 non-trivially?")
print(f"   {'ε (deg)':>8s} {'|S|':>10s} {'setting spread':>15s}  (max angle between the 4 analyser vectors)")
for eps_deg in [0, 30, 60, 80, 85, 89, 89.9]:
    eps = np.radians(eps_deg)
    n = np.array([np.sin(eps), 0.0, np.cos(eps)])
    setting = lambda g: qrot(quat(n, g), xhat)
    V = [setting(a), setting(ap), setting(b), setting(bp)]
    S = abs(E_vec(V[0],V[2]) + E_vec(V[0],V[3]) + E_vec(V[1],V[2]) - E_vec(V[1],V[3]))
    spread = max(np.degrees(np.arccos(np.clip(np.dot(u,w), -1, 1)))
                 for i,u in enumerate(V) for w in V[i+1:])
    print(f"   {eps_deg:>8.1f} {S:>10.6f} {spread:>15.4f}")
print("   |S| → 2 ONLY as ε → 90°, where all four analyser vectors collapse")
print("   onto the tilt axis (spread → 0): every correlation → −1, S → −2.")
print("   ⇒ there is NO non-trivial tilt that reproduces local realism. The")
print("     defect DEGRADES the measurement toward triviality; it never")
print("     'explains' the violation. Real contamination, not a loophole.")

# ── F. 'the reverse of iterating a list while removing items' ────────────
#    remove-while-iterating  → you SKIP items, the list shrinks under you.
#    the reverse             → each stacked rotation ADDS a component you did
#    not put in; the list GROWS under you, you over-carry.
#    Model: 'add δ on the established angle' where the rotation axis is defined
#    in the BODY frame (tilted ε from the current local vertical) — so the axis
#    moves with the point. Stack N of them.
print("\nF. stacking N body-frame rotations of δ each  (axis tilted ε from the")
print("   CURRENT local vertical — 'add δ onto where you already are')")
print(f"   {'N':>4s} {'flat azimuth':>13s} {'actual φ':>10s} {'φ error':>10s} {'z (accreted)':>13s}")
delta = np.radians(30.0); eps = np.radians(12.0)
v = xhat.copy()
up = np.array([0.0, 0.0, 1.0])
for N in range(1, 13):
    # body axis: the analyser knob is tilted ε toward the CURRENT pointing
    # direction (a real mis-alignment that tracks the moving frame)
    radial = v / np.linalg.norm(v)
    axis = np.cos(eps) * up + np.sin(eps) * radial      # tilted, body-referenced
    axis = axis / np.linalg.norm(axis)
    v = qrot(quat(axis, delta), v)
    phi = np.degrees(np.arctan2(v[1], v[0]))
    flat = np.degrees(N * delta) % 360
    if flat > 180: flat -= 360
    err = phi - flat
    print(f"   {N:>4d} {flat:>13.3f} {phi:>10.3f} {err:>10.3f} {v[2]:>13.5f}")
print("   flat model: z ≡ 0, φ = N·δ, forever — a fixed-length component list.")
print("   body-frame stack: z accretes and φ drifts off N·δ — every added")
print("   rotation deposits a new component. The list GROWS as you iterate it;")
print("   the sum is never 'just the sum'. Angles+rotations COMPLICATE, they")
print("   do not simply add — and the complication is deterministic, not noise.")
