#!/usr/bin/env python3
"""Which parts of the box kite respond to a windspeed, and does that depend on HOW the
windspeed enters?  Uses the scalar-context-propagation paper's own tension proxy (not Phi_w,
which is unbuilt): H = Re(Pi), Pi = ordered product of the 7 pencil-station generators,
each a continuous point on the great circle between e_a and e_b (appendix 07).
H plays the role of string tension.  The baseline law is the paper's Noether path
phi_k = t*(pi/2)*(k+1)/7.  Everything here is a PROXY; station != Assessor vertex.
"""
import sys, math, random
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.box_kite import maths as bk

HP = math.pi / 2
def gen(a, b, phi):
    v = [0.0] * 16; v[a] = math.cos(phi); v[b] = math.sin(phi); return v
def prod(stations, phis):
    p = gen(*stations[0], phis[0])
    for k in range(1, 7):
        p = bk.multiply(p, gen(*stations[k], phis[k]))
    return p
def H(s, phis):  return prod(bk.pencil(s), phis)[0]
def imnorm(s, phis):
    p = prod(bk.pencil(s), phis); return math.sqrt(sum(x*x for x in p[1:]))
def noether(t):  return [t * HP * (k + 1) / 7 for k in range(7)]

T = [i / 10 for i in range(11)]
print("1. BASELINE  H(t) along the Noether path, every strut  (tension swing = max-min)")
print("   strut  swing(H)   H(0)     H(1)     |Im Pi|(t=0.5)")
for s in range(1, 8):
    hs = [H(s, noether(t)) for t in T]
    print("   %d      %.6f  %+.5f  %+.5f  %.5f" % (s, max(hs) - min(hs), hs[0], hs[-1], imnorm(s, noether(0.5))))

print("\n2. RESPONSE OF EACH STATION  |dH/dphi_k| at t=0.5 on the Noether path (central difference)")
print("   strut | " + "  ".join("st%d  " % k for k in range(1, 8)))
for s in range(1, 8):
    base = noether(0.5); row = []
    for k in range(7):
        up = list(base); dn = list(base); up[k] += 1e-5; dn[k] -= 1e-5
        row.append(abs(H(s, up) - H(s, dn)) / 2e-5)
    print("   %d     | " % s + "  ".join("%.3f" % x for x in row))

print("\n3. NON-UNIFORM WIND  rates r_k = (k+1)/7 * (1 + d*u_k), u_k random in [-1,1], 60 draws/strut")
print("   mean tension swing of H over t in [0,1]; d=0 is the Noether path")
random.seed(7)
draws = [[random.uniform(-1, 1) for _ in range(7)] for _ in range(60)]
Ds = (0.0, 0.05, 0.15, 0.4)
print("   strut | " + "  ".join("d=%-5g" % d for d in Ds))
for s in range(1, 8):
    cells = []
    for d in Ds:
        sw = []
        for u in (draws if d else draws[:1]):
            hs = [H(s, [t * HP * (k + 1) / 7 * (1 + d * u[k]) for k in range(7)]) for t in T]
            sw.append(max(hs) - min(hs))
        cells.append(sum(sw) / len(sw))
    print("   %d     | " % s + "  ".join("%.4f " % c for c in cells))

print("\n4. SCALAR WIND, TIME-VARYING  (gusts): t(tau) = tau + 0.2*sin(2*pi*tau)/(2*pi)  vs steady t=tau")
for s in (1, 2):
    gust = [H(s, noether(tau + 0.2 * math.sin(2 * math.pi * tau) / (2 * math.pi))) for tau in T]
    steady = [H(s, noether(tau)) for tau in T]
    sg = set(round(h, 9) for h in gust); ss = set(round(h, 9) for h in steady)
    print("   strut %d: max|H_gust(tau) - H_steady(tau)| = %.4f   range gust=[%.4f,%.4f] steady=[%.4f,%.4f]" % (
        s, max(abs(a - b) for a, b in zip(gust, steady)), min(gust), max(gust), min(steady), max(steady)))

print("\n5. IS H A FUNCTION OF ONE SIGNED PHASE?  fit H = -cos(sum_k eps_k*phi_k), best of 128 sign patterns,")
print("   200 random phi vectors per strut; also the signed rate sum on the Noether path")
import itertools
random.seed(11)
phis_list = [[random.uniform(0, HP) for _ in range(7)] for _ in range(200)]
for s in range(1, 8):
    hs = [H(s, p) for p in phis_list]
    best = None
    for eps in itertools.product((1, -1), repeat=7):
        err = max(abs(h + math.cos(sum(e * x for e, x in zip(eps, p)))) for h, p in zip(hs, phis_list))
        if best is None or err < best[0]: best = (err, eps)
    err, eps = best
    rate_sum = sum(e * (k + 1) / 7 for k, e in enumerate(eps)) * HP
    print("   strut %d: max|H + cos(sum eps*phi)| = %.2e   eps=%s   signed Noether rate sum = %+.5f rad" % (
        s, err, "".join("+" if e > 0 else "-" for e in eps), rate_sum))
