"""P6 — the Riemann-Fermat heartbeat in the image: zeta on the critical line, lobe by lobe.
Fact (Riemann-Siegel): zeta(1/2+it) = e^{-i theta(t)} Z(t), Z real, theta = Riemann-Siegel theta.  So the image is the polar curve r = Z(t), phi = -theta(t).
Leading Riemann-Siegel term: Z ~ 2 cos(theta)  ->  r = 2 cos(phi): a CIRCLE through the origin, diameter 2, radius 1, AREA pi.
Measure each lobe (origin to origin, between consecutive zeros): area (Green), max radius D, area/(pi D^2/4) [circle=1], area/(3 pi D^2/8) [cardioid=1]."""
import numpy as np, mpmath as mp, math
mp.mp.dps = 15
N = 40
gam = [float(mp.zetazero(n).imag) for n in range(1, N+2)]
def lobe(a, b, m=600):
    t = np.linspace(a, b, m)
    z = np.array([complex(mp.zeta(0.5 + 1j*float(x))) for x in t])
    return t, z
rows = []
print(f"{'lobe':>4} {'t from':>8} {'t to':>8} {'D=max|z|':>9} {'area':>9} {'area/pi':>8} {'A/(piD²/4)':>11} {'A/(3piD²/8)':>12} {'theta advance/pi':>17}")
t0 = 0.0
edges = [0.0] + gam                                     # first lobe: t=0 (zeta(1/2) = -1.46) to gamma_1
for k in range(N):
    a, b = edges[k], edges[k+1]
    t, z = lobe(a, b)
    # signed area by Green: 1/2 ∮ (x dy - y dx)
    area = 0.5*np.trapezoid(z.real*np.gradient(z.imag, t) - z.imag*np.gradient(z.real, t), t)
    D = np.abs(z).max()
    th = float(mp.siegeltheta(b) - mp.siegeltheta(a))
    rows.append((k+1, a, b, D, abs(area), th/math.pi))
    print(f"{k+1:4d} {a:8.3f} {b:8.3f} {D:9.4f} {abs(area):9.4f} {abs(area)/math.pi:8.4f} {abs(area)/(math.pi*D*D/4):11.4f} {abs(area)/(3*math.pi*D*D/8):12.4f} {th/math.pi:17.4f}")
A = np.array([r[4] for r in rows]); Dd = np.array([r[3] for r in rows])
print(f"\nmean lobe area {A.mean():.4f} (π = {math.pi:.4f});  median A/(πD²/4) = {np.median(A/(math.pi*Dd**2/4)):.4f};  median A/(3πD²/8) = {np.median(A/(3*math.pi*Dd**2/8)):.4f}")
print("each lobe: theta advances by ~pi between consecutive zeros (Gram): the polar angle phi=-theta sweeps a half-turn per lobe")
# leading Riemann-Siegel term as the circle: compare Z(t) with 2cos(theta(t)) on lobe 1..6 (N=sqrt(t/2pi)<1.3 -> one-term regime)
for k in (1, 2, 3):
    a, b = edges[k], edges[k+1]; t = np.linspace(a, b, 200)
    Z = np.array([float(mp.siegelz(x)) for x in t]); th = np.array([float(mp.siegeltheta(x)) for x in t])
    resid = Z - 2*np.cos(th)
    print(f"   lobe {k+1}: max|Z - 2cos(theta)| = {np.abs(resid).max():.3f} vs amplitude {np.abs(Z).max():.3f}  (1-term RS circle has D=2)")
