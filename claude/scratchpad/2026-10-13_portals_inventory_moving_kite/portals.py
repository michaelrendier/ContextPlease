#!/usr/bin/env python3
"""PORTALS — are the struts separate, or one continuous ZD variety?  And what is INSIDE a zero divisor."""
import sys, math, itertools
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from common import *
Ds = derivations(); rng = np.random.default_rng(21)
nz = lambda v, t=1e-9: np.linalg.norm(v) < t
UD = {k: v / np.linalg.norm(v) for k, v in DV.items()}
d1k = (2, 3, 1); d1 = UD[d1k]
def Gc(c): return expm(sum(ci * Di for ci, Di in zip(c, Ds)))
def reach(target, tries=25):
    best = (9.0, None)
    for _ in range(tries):
        c0 = rng.normal(size=14) * 1.2
        for sgn in (1, -1):
            r = least_squares(lambda c: Gc(c) @ d1 - sgn * target, c0, method='lm', xtol=1e-14, ftol=1e-14, max_nfev=400)
            if np.linalg.norm(r.fun) < best[0]: best = (np.linalg.norm(r.fun), r.x)
            if best[0] < 1e-9: return best
    return best
print("1. REACHABILITY: from the diagonal %s can a continuous G2 flow (which preserves EVERY zero-divisor relation) carry it onto each of the other 83 diagonals?" % (d1k,), flush=True)
res = {}
for k in UD:
    if k == d1k: continue
    a, b, s = k; same_plane = (a, b) == (2, 3); same_chart = (a ^ b) == 1
    rel = "same plane" if same_plane else ("same chart, reversal" if same_chart and (a, b) == (3, 2) else ("same chart, neighbour" if same_chart else "OTHER CHART"))
    r, c = reach(UD[k]); res[k] = (rel, r, c)
tab = {}
for k, (rel, r, c) in res.items(): tab.setdefault(rel, [0, 0]); tab[rel][1] += 1; tab[rel][0] += (r < 1e-7)
for rel, (ok, n) in tab.items(): print("   %-24s reachable %2d of %2d" % (rel, ok, n))
print("   residual of the best attempts: max over reachable = %.1e ; min over unreachable = %s" % (max([r for _, r, _ in res.values() if r < 1e-7] or [0]), "%.3f" % min([r for _, r, _ in res.values() if r >= 1e-7]) if any(r >= 1e-7 for _, r, _ in res.values()) else "none"), flush=True)
# 2. a path to another chart
tgt = next((k for k, (rel, r, c) in res.items() if rel == "OTHER CHART" and r < 1e-7), None)
print("\n2. THE PATH from %s (chart 1) to %s (chart %d)" % (d1k, tgt, tgt[0] ^ tgt[1]) if tgt else "\n2. no other-chart target reached")
if tgt:
    r, c = res[tgt][1], res[tgt][2]
    y0 = UD[(4, 5, -1)]   # a neighbour of d1 in chart 1
    print("   d1 = %s is annihilated by its neighbour (4,5,-)  : |d1 y0| = %.1e" % (d1k, np.linalg.norm(m(d1, y0))))
    print("   tau   |x(tau) y(tau)|   angle(x, nearest lattice diagonal) deg   dominant chart (share)   smallest singular value of L_x   straight-line |x y_min|")
    xt = lambda t: expm(sum(ci * Di for ci, Di in zip(c, Ds)) * t) if False else Gc(t * np.array(c))
    tg = UD[tgt]
    # use the flow tau -> Gc(tau c)
    for tau in (0.0, 0.25, 0.5, 0.75, 1.0):
        g = Gc(tau * np.array(c)); x = g @ d1; y = g @ y0
        ang = min(math.degrees(math.acos(min(1, abs(float(x @ v))))) for v in UD.values())
        ch = bk.chart_of(list(x), check_zd=False); smin = np.linalg.svd(Lmat(x), compute_uv=False)[-1]
        line = (1 - tau) * d1 + tau * tg; line /= np.linalg.norm(line); lsm = np.linalg.svd(Lmat(line), compute_uv=False)[-1]
        print("   %.2f  %.1e          %6.2f                              %d (%.2f)                 %.1e                       %.3f" % (tau, np.linalg.norm(m(x, y)), ang, ch['dominant_chart'], ch['chart_share'], smin, lsm))
# 3. inside a zero divisor
print("\n3. INSIDE a zero divisor y = (2,3,+): the annihilator N(y) = {x : x y = 0}")
y = UD[d1k]; R = Rmat(y); u_, s_, vt = np.linalg.svd(R); N = vt[np.sum(s_ > 1e-9):]
print("   dim N(y) = %d ; every nonzero element of N(y) is itself a zero divisor (x y = 0, x != 0)" % N.shape[0])
nb = [UD[k] for k in UD if np.linalg.norm(m(UD[k], y)) < 1e-9]
G = np.array(nb) @ np.array(nb).T
print("   the %d lattice neighbours of y inside N(y): Gram matrix (cosines) =\n%s" % (len(nb), np.round(G, 3)))
def inN(x): return np.linalg.norm(R @ x) < 1e-9
w = np.cos(0.6) * nb[0] + np.sin(0.6) * nb[1]; print("   a great-circle arc from neighbour 1 to neighbour 2 stays in N(y) (arc point annihilates y): |w y| = %.1e" % np.linalg.norm(m(w, y)))
rr = [rng.normal(size=4) for _ in range(30)]; pr = []
for a_ in rr:
    x1 = N.T @ a_; x2 = N.T @ rng.normal(size=4); p = m(x1, x2)
    pr.append((np.linalg.norm(p) / (np.linalg.norm(x1) * np.linalg.norm(x2)), np.linalg.norm(N.T @ (N @ p)) / max(np.linalg.norm(p), 1e-12)))
print("   products inside N(y): |x1 x2|/(|x1||x2|) range %.3f..%.3f ; fraction of the product that stays in N(y): %.3f..%.3f  (1.0 = N(y) is closed under multiplication)" % (min(a for a, b in pr), max(a for a, b in pr), min(b for a, b in pr), max(b for a, b in pr)))
Dst = None
Gx = np.array([Di @ y for Di in Ds]).T; u2, s2, vt2 = np.linalg.svd(Gx); stab = vt2[np.sum(s2 > 1e-9):]
St = [sum(c * Di for c, Di in zip(row, Ds)) for row in stab]
mv = np.array([np.concatenate([S @ v for v in nb]) for S in St]); print("   stabiliser of y has dim %d and acts on the 4 neighbours with rank %d (it rotates them inside N(y) = S^3, fixing y)" % (len(St), np.linalg.matrix_rank(mv, tol=1e-9)))
