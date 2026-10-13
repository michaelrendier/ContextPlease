#!/usr/bin/env python3
"""GENEALOGY 2 — corrected subalgebra census; Assessor = ordered pair of distinct points of the lower Fano plane;
kite = punctured Fano plane; the sign gauge on the octahedron; why zero divisors begin at the sedenions."""
import itertools, math
import numpy as np
from common import *
E = np.eye(16)
def span(S):
    G = {0}
    for s in S: G |= {g ^ s for g in G}
    return frozenset(G)
al = np.array([[T_[i, j, i ^ j] for j in range(16)] for i in range(16)])
phi = np.zeros((16, 16, 16), int)
for i in range(16):
    for j in range(16):
        for k in range(16):
            l = m(m(E[i], E[j]), E[k]); r = m(E[i], m(E[j], E[k])); phi[i, j, k] = 1 if np.allclose(l, r) else -1
indep = [(i, j, k) for i in range(1, 16) for j in range(1, 16) for k in range(1, 16) if i != j and k not in (i, j, i ^ j)]
print("A. proper accounting of the 4096 ordered index triples")
print("   rank<=2 (dependent) triples: %d ; of those nonassociative: %d" % (4096 - len(indep), sum(1 for i in range(16) for j in range(16) for k in range(16) if (i, j, k) not in set(indep) and phi[i, j, k] == -1)))
print("   rank-3 (independent) ordered triples: %d (= 15*14*12); nonassociative: %d" % (len(indep), sum(1 for t in indep if phi[t] == -1)))
def rnd(idx, seed):
    r = np.random.default_rng(seed); v = np.zeros(16); v[list(idx)] = r.normal(size=len(idx)); return v
def comp(H):
    return max(abs(np.linalg.norm(m(rnd(H, s), rnd(H, 50 + s))) - np.linalg.norm(rnd(H, s)) * np.linalg.norm(rnd(H, 50 + s))) for s in range(25))
def altern(H):
    w = 0
    for s in range(15):
        x, y = rnd(H, s), rnd(H, 90 + s); w = max(w, np.linalg.norm(m(m(x, x), y) - m(x, m(x, y))), np.linalg.norm(m(m(y, x), x) - m(y, m(x, x))))
    return w
hyp = sorted({span([i, j, k]) for (i, j, k) in indep}, key=lambda h: sorted(h))
print("\nB. the 15 order-8 subgroups (hyperplanes ker chi_u, plus the 0): subalgebra type")
def chi(u): return [(-1) ** bin(u & i).count('1') for i in range(16)]
rows = []
for H in hyp:
    u = [u for u in range(1, 16) if all(chi(u)[i] == 1 for i in H)][0]
    triples = [t for t in indep if set(t) <= H]; na = sum(1 for t in triples if phi[t] == -1)
    c = comp(H) < 1e-9; a = altern(H) < 1e-9
    kind = "OCTONION (composition, alternative, nonassociative)" if c and a and na == len(triples) else \
           "composition-failing, alternative" if (not c) and a else "composition-failing, NOT alternative" if (not c) else "other"
    rows.append((u, sorted(H), c, a, na, len(triples), kind))
for r in sorted(rows): print("   u=%2d %-34s composition=%-5s alternative=%-5s nonassoc %3d/%d  -> %s" % r)
print("   counts:", {k: sum(1 for r in rows if r[6] == k) for k in {r[6] for r in rows}})
print("\nC. the oriented Fano plane P (lower octonion): e_a e_b = alpha(a,b) e_{a^b} on its 7 lines")
P = list(range(1, 8)); linesP = sorted({tuple(sorted((a, b, a ^ b))) for a in P for b in P if a != b})
print("   lines of P:", linesP)
print("   orientation signs alpha(a,b) for (a<b) on each line: ", {l: int(al[l[0], l[1]]) for l in linesP})
print("\nD. Assessor = ordered pair (a,b) of DISTINCT points of P ; strut s = third point of the line ; kite_s = the 6 other points")
print("   ordered pairs of distinct points of P: %d = 7*6 = 42 = number of Assessors: %s" % (7 * 6, {(a, b) for (a, b) in asr} == {(a, b) for a in P for b in P if a != b}))
print("   the 7x7 grid P x P has 49 cells; the diagonal (a,a) is the CD pair (e_a, e_{a+8}) which has no zero divisors (normed C-like plane) -> 49 - 7 = 42")
ok = True
for s in P:
    vs = K[s]; pts = {a for a, b in vs} | {b for a, b in vs}
    L = [tuple(sorted((a, b, s))) for a, b in vs]
    if pts != set(P) - {s} or len(set(L)) != 3: ok = False
print("   kite_s's 6 vertices are exactly the 6 points of P other than s, grouped by the 3 lines through s: %s" % ok)
def adjacent(u, v): return (u[0] ^ u[1]) == (v[0] ^ v[1]) and u != v and v != (u[1], u[0])
print("   octahedron edges = pairs of vertices on DIFFERENT lines through s: 12 edges, each vertex adjacent to the 4 vertices on the other two lines; the 3 non-edges = the 3 lines through s (reversal pairs)")
# stabiliser of strut s in GL(3,2) acting on the 6 vertices
def gl3():
    out = []
    for cols in itertools.product(range(1, 8), repeat=3):
        sp = {0}; ok_ = True
        for c in cols:
            if c in sp: ok_ = False; break
            sp |= {x ^ c for x in sp}
        if ok_: out.append(cols)
    return out
def app(A, i):
    r = 0
    for b in range(3):
        if (i >> b) & 1: r ^= A[b]
    return r
G3 = gl3(); st = [A for A in G3 if app(A, 1) == 1]
verts = K[1]
def act(A, v): return (app(A, v[0]), app(A, v[1]))
perms = {tuple(verts.index(act(A, v)) for v in verts) for A in st}
axes = {frozenset((v, (v[1], v[0]))) for v in verts}
def axperm(p):
    pair = lambda v: frozenset((v, (v[1], v[0])))
    ax = [pair(v) for v in verts]; uniq = list(dict.fromkeys(ax)); 
    return tuple(uniq.index(pair(verts[p[verts.index(v)]])) for v in verts)
print("   |GL(3,2)| = %d ; stabiliser of strut 1 has order %d ; its action on the 6 vertices is faithful with image of order %d" % (len(G3), len(st), len(perms)))
print("   the induced permutation group on the 3 axes (lines through s) has order %d" % len({tuple(sorted(set((axperm(p)[i]) for i in range(6)))) + (axperm(p),) for p in perms}))
print("   (order 24 acting faithfully, with S3 on the 3 axes and kernel of order 4 = the rotation group S4 of the octahedron/cube)")
# sign gauge: for each adjacent plane pair, which sign combos (sigma,tau) annihilate?
print("\nE. the SIGN GAUGE on the octahedron (a Z2 field on the edges)")
c_ = {}
for u in K[1]:
    for v in K[1]:
        if adjacent(u, v):
            combos = [(su, sv) for su in (1, -1) for sv in (1, -1) if np.linalg.norm(m(DV[(u[0], u[1], su)], DV[(v[0], v[1], sv)])) < 1e-9]
            c_[(u, v)] = combos
cs = {k: sorted({a * b for a, b in v}) for k, v in c_.items()}
print("   for each ordered adjacent pair: annihilating (sigma_u, sigma_v) combos have sigma_u*sigma_v in:", sorted({tuple(v) for v in cs.values()}))
cu = {k: v[0] for k, v in cs.items() if len(v) == 1}
print("   edge constraint sigma_u sigma_v = c_uv : constant c on each edge (single value): %s ; c=+1 on %d, c=-1 on %d of %d ordered pairs" % (len(cu) == len(cs), sum(1 for v in cu.values() if v == 1), sum(1 for v in cu.values() if v == -1), len(cu)))
import networkx as nx
Gk = nx.Graph()
for (u, v), c in cu.items(): Gk.add_edge(u, v, c=c)
faces = [t for t in itertools.combinations(K[1], 3) if all(Gk.has_edge(x, y) for x, y in itertools.combinations(t, 2))]
prods = [math.prod(Gk[x][y]['c'] for x, y in itertools.combinations(t, 2)) for t in faces]
print("   triangle (face) products of c around the 8 faces: %s  -> +1 (consistent) faces %d, -1 (frustrated) faces %d" % (prods, prods.count(1), prods.count(-1)))
best = 0
for sg in itertools.product((1, -1), repeat=6):
    sat = sum(1 for x, y in Gk.edges if sg[K[1].index(x)] * sg[K[1].index(y)] == Gk[x][y]['c']); best = max(best, sat)
print("   best sign assignment of the 6 diagonals satisfies %d of 12 edge constraints (12 = a consistent gauge, <12 = frustrated)" % best)

print("\nF. why zero divisors begin at the sedenions: the doubling step as projective geometry P_{n+1} = P_n + pivot + shadow(P_n)")
def cdtable(levels):
    n = 2 ** levels; mus = (-1.0,) * levels; E_ = np.eye(n); Tn = np.zeros((n, n, n))
    for i in range(n):
        for j in range(n): Tn[i, j] = cd_mul(E_[i], E_[j], mus)
    return Tn
for lev in (3, 4, 5):
    n = 2 ** lev; h = n // 2; Tn = cdtable(lev)
    mm = lambda x, y: np.einsum('i,j,ijk->k', x, y, Tn)
    cross = [(a, b) for a in range(1, h) for b in range(1, h) if a != b]
    diag = {(a, b, s): np.eye(n)[a] + s * np.eye(n)[b + h] for (a, b) in cross for s in (1, -1)}
    ks = list(diag); zero = 0
    for k1 in ks:
        for k2 in ks:
            if np.linalg.norm(mm(diag[k1], diag[k2])) < 1e-9: zero += 1
    lowpts = h - 1
    maxlines = (h // 2) - 1 if h > 2 else 0
    print("   level %d (dim %2d): lower index group has %2d nonzero points, %d lines through each point; cross pairs (a,b), a!=b: %3d ; diagonals %3d ; ordered annihilating diagonal pairs: %d" % (lev, n, lowpts, maxlines, len(cross), len(ks), zero))
