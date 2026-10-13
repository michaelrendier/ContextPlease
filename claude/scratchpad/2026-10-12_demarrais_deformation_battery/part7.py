#!/usr/bin/env python3
"""PART 7 — the pencil convention and the mechanism of the tension law (checks that were first run inline; saved here).
(a) Assessor planes vs pencil(r)  (b) rank of the phase-dependence of H for every pencil r=1..15 (left bracketing)
(c) alternativity / associator counts (negative results)  (d) mechanism: e_a^-1 e_b = eta e_r, product of bare e_a = -1."""
import sys, math, random, itertools
import numpy as np
from cdalg import *
T = table(STD)
def m(x, y): return np.einsum('i,j,ijk->k', x, y, T)
E = np.eye(16); asr = bk.assessors(); planes = {frozenset((a, b + 8)) for (a, b) in asr}
print("(a) Assessor planes of each strut have index XOR s+8; pencil(r) stations that are Assessor planes:")
for s in range(1, 8):
    pl = [(a, b + 8) for (a, b) in bk.box_kites()[s]]
    print("   strut %d: XOR set %s ; pencil(%d) = %s" % (s, sorted({x ^ y for x, y in pl}), s + 8, bk.pencil(s + 8)))
for r in range(1, 16):
    print("   pencil(%2d): %d of 7 stations are Assessor planes" % (r, sum(1 for p in bk.pencil(r) if frozenset(p) in planes)))
HP = math.pi / 2
def gen(a, b, phi): v = np.zeros(16); v[a] = math.cos(phi); v[b] = math.sin(phi); return v
def Hf(r, ph):
    st = bk.pencil(r); p = gen(*st[0], ph[0])
    for k in range(1, 7): p = m(p, gen(*st[k], ph[k]))
    return p[0]
random.seed(2)
print("\n(b) rank of the gradient set of H(phi) over 60 random points (left bracketing, natural station order):")
RK = {}
for r in range(1, 16):
    G = []
    for _ in range(60):
        ph = [random.uniform(0, HP) for _ in range(7)]; g = []
        for k in range(7):
            u = list(ph); d = list(ph); u[k] += 1e-6; d[k] -= 1e-6; g.append((Hf(r, u) - Hf(r, d)) / 2e-6)
        G.append(g)
    sv = np.linalg.svd(np.array(G), compute_uv=False); RK[r] = int(np.sum(sv > 1e-3 * sv[0]))
    print("   r=%2d  singular values %s -> rank %d" % (r, np.round(sv, 3).tolist(), RK[r]))
print("\n(c) negative results: is it alternativity or associator counts?")
bad = [(r, a) for r in range(1, 16) for a in range(1, 16) if a != r and not np.allclose(m(E[r], m(E[r], E[a])), -E[a])]
print("   e_r(e_r e_a) = -e_a fails for %d (r,a) pairs" % len(bad))
def assoc(i, j, k): return np.linalg.norm(m(m(E[i], E[j]), E[k]) - m(E[i], m(E[j], E[k])))
for r in (1, 8, 9, 10, 15):
    A = [a for a, b in bk.pencil(r)]
    n1 = sum(1 for k, l in itertools.combinations(range(7), 2) if assoc(A[k], A[l], r) > 1e-9)
    n2 = sum(1 for k, l in itertools.combinations(range(7), 2) if assoc(A[k], r, A[l]) > 1e-9)
    print("   pencil %2d: nonzero [e_ak,e_al,e_r] in %2d/21 ; [e_ak,e_r,e_al] in %2d/21 ; rank %d" % (r, n1, n2, RK[r]))
print("\n(d) mechanism: each station = e_a * exp(eta e_r phi) with e_a^-1 e_b = eta e_r ; product of the bare e_a (phi=0):")
def conj(v): w = -v.copy(); w[0] = v[0]; return w
for r in range(1, 16):
    st = bk.pencil(r); etas = []
    for a, b in st:
        u = m(conj(E[a]), E[b]); k = int(np.argmax(np.abs(u))); etas.append((k, int(round(u[k]))))
    P = E[st[0][0]]
    for a, b in st[1:]: P = m(P, E[a])
    t = int(np.argmax(np.abs(P)))
    print("   r=%2d : all stations +/- e_r: %-5s  eta=%s  prod(e_a) = %+d e_%d" % (r, all(k == r for k, _ in etas), "".join('+' if s > 0 else '-' for _, s in etas), int(round(P[t])), t))
