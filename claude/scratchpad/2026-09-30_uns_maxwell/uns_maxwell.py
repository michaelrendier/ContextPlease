"""What Maxwell says about the Sacks/UNS prime structure.  Integers n sit at r = sqrt(n), phi = 2*pi*sqrt(n) (one Archimedean spiral).
Prime charges q=+1 (2D Coulomb: E = sum q (x - x_n)/|x - x_n|^2, so Gauss: flux = 2*pi*Q_enc, mean E_r on radius R = Q_enc/R).
T1  integer density per unit area is uniform (1/pi).
T2  Gauss: mean radial field on a ring of radius R equals pi(R^2)/R exactly; deviation from li(R^2)/R vs the RH-conditional bound.
T3  multipole moments M_m = sum_{p<=R^2} exp(i m 2 pi sqrt p)  vs a random-selection (Cramer) model.
T4  angular structure of the field on the ring: rms(E_r - mean)/mean, primes vs Cramer, and composites.
T5  magnetostatics of the counter-twist: rotate primes by +Theta, composites by -Theta; net magnetic moment sign and size."""
import numpy as np, math, sys
import sympy
rng = np.random.default_rng(1)
def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]
NMAX = 4_000_000
P = primes_upto(NMAX)
def pos(n): r = np.sqrt(n.astype(float)); ph = 2 * np.pi * r; return r * np.cos(ph), r * np.sin(ph)
print("== T1  integers per unit area in the Sacks plane ==")
for R in (100, 300, 1000):
    N = R * R; print("R=%4d  integers inside %d  area pi R^2 = %.0f  density*pi = %.4f" % (R, N, math.pi * R * R, N / (math.pi * R * R) * math.pi))
def ring_field(xs, ys, R, m=720):
    th = np.linspace(0, 2 * np.pi, m, endpoint=False); px, py = R * np.cos(th), R * np.sin(th)
    Ex = np.zeros(m); Ey = np.zeros(m)
    for a in range(0, len(xs), 20000):
        dx = px[:, None] - xs[None, a:a + 20000]; dy = py[:, None] - ys[None, a:a + 20000]; d2 = dx * dx + dy * dy + 1e-9
        Ex += (dx / d2).sum(1); Ey += (dy / d2).sum(1)
    Er = Ex * np.cos(th) + Ey * np.sin(th); Et = -Ex * np.sin(th) + Ey * np.cos(th)
    return Er, Et
def li(x): return float(sympy.li(x)) if x > 2 else 0.0
print("\n== T2  Gauss: mean E_r on the ring == pi(R^2)/R   (charges up to 2R^2, exterior charges average to zero on the ring) ==")
print("   R     pi(R^2)   mean E_r   pi/R      li(R^2)/R   (pi-li)/R   RH bound ln(R)/(4 pi)")
for R in (100, 316, 1000):
    N = R * R; sel = P[P <= 2 * N]; xs, ys = pos(sel); Er, Et = ring_field(xs, ys, R)
    piN = int((P <= N).sum()); print("%5d %9d %10.4f %9.4f %10.4f %11.4f %14.4f" % (R, piN, Er.mean(), piN / R, li(N) / R, (piN - li(N)) / R, math.log(R) / (4 * math.pi)))
print("\n== T3  multipole moments |M_m| / sqrt(pi(N)) for primes, and the random (Cramer) model, N = R^2 ==")
for R in (316, 1000, 2000):
    N = R * R; pr = P[P <= N]; n = np.arange(2, N + 1); prob = 1 / np.log(n)
    line = "R=%4d pi=%6d |" % (R, len(pr))
    for m in (1, 2, 3, 5):
        Mp = abs(np.exp(1j * m * 2 * np.pi * np.sqrt(pr)).sum()) / math.sqrt(len(pr))
        Mr = np.mean([abs(np.exp(1j * m * 2 * np.pi * np.sqrt(n[rng.random(len(n)) < prob])).sum()) / math.sqrt(len(pr)) for _ in range(5)])
        line += "  m=%d primes %.2f random %.2f" % (m, Mp, Mr)
    print(line)
print("\n== T4  angular structure of E_r on the ring: rms(E_r - mean)/mean ==")
for R in (316, 1000):
    N = R * R; sel = P[P <= 2 * N]; xs, ys = pos(sel); Er, _ = ring_field(xs, ys, R); sp = Er.std() / Er.mean()
    n = np.arange(2, 2 * N + 1); prob = 1 / np.log(n); sr = []
    for _ in range(5):
        s2 = n[rng.random(len(n)) < prob]; x2, y2 = pos(s2); E2, _ = ring_field(x2, y2, R); sr.append(E2.std() / E2.mean())
    comp = np.setdiff1d(np.arange(4, 2 * N + 1), P); comp = comp[::max(1, len(comp) // len(sel))]
    x3, y3 = pos(comp); E3, _ = ring_field(x3, y3, R)
    print("R=%4d  primes %.3f | random same density %.3f +- %.3f | composites(thinned to same count) %.3f" % (R, sp, np.mean(sr), np.std(sr), E3.std() / E3.mean()))
print("\n== T5  counter-twist: primes rotate +Theta, composites -Theta (one plane, Theta = 22.5 deg per k): net magnetic moment of rotating charge ==")
# a charge q at radius r rotating at angular rate w has moment (q w r^2 / 2) z; take w = +Theta for primes and -Theta for composites, each charge +1
N = 1_000_000; pr = P[P <= N]; r2p = pr.astype(float); allr = np.arange(2, N + 1).astype(float); r2c = np.setdiff1d(allr, r2p)
mp_, mc_ = 0.5 * r2p.sum(), 0.5 * r2c.sum()
print("sum r^2 primes/2 = %.4g | composites/2 = %.4g | net (primes - composites) = %.4g  ->  net moment sign %s, composites dominate by factor %.1f" % (mp_, mc_, mp_ - mc_, "NEGATIVE" if mp_ < mc_ else "positive", mc_ / mp_))
