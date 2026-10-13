#!/usr/bin/env python3
"""GENEALOGY of the sedenion box-kite, bottom-up.  Every level is computed from the multiplication table."""
import itertools, math, random
import numpy as np
from common import *
E = np.eye(16)
print("LEVEL 1  index group  Z2^4 = F2^4 under XOR  (16 elements; 15 nonzero)")
print("LEVEL 2  sign cocycle alpha(i,j) in {+-1}:  e_i e_j = alpha(i,j) e_{i xor j}   [twisted group algebra R^alpha[Z2^4]]")
al = np.array([[T_[i, j, i ^ j] for j in range(16)] for i in range(16)])
offmag = max(np.abs(T_[i, j]).sum() - 1 for i in range(16) for j in range(16))
print("   every basis product is +-1 times a single basis element: %s (max extra mass %.1e)" % (offmag < 1e-12, offmag))
beta = al * al.T
print("   commutator sign beta(i,j) = alpha(i,j)alpha(j,i): -1 for distinct nonzero i,j: %s ; +1 when i=0, j=0 or i=j: %s" % (
      all(beta[i, j] == -1 for i in range(1, 16) for j in range(1, 16) if i != j), all(beta[i, j] == 1 for i in range(16) for j in range(16) if i == 0 or j == 0 or i == j)))
print("   (the 'braiding' data; beta is NOT a bicharacter on Z2^4: beta(i^j,k) vs beta(i,k)beta(j,k) for independent i,j,k:", end=" ")
bad = sum(1 for i in range(1, 16) for j in range(1, 16) for k in range(1, 16)
          if len({i, j, k}) == 3 and (i ^ j) != k and (i ^ j) != 0 and beta[i ^ j, k] != beta[i, k] * beta[j, k])
print("%d violations)" % bad)
phi = np.zeros((16, 16, 16), int)
for i in range(16):
    for j in range(16):
        for k in range(16):
            a = np.einsum('i,j->ij', E[i], E[j]); l = m(m(E[i], E[j]), E[k]); r = m(E[i], m(E[j], E[k]))
            phi[i, j, k] = 1 if np.allclose(l, r) else (-1 if np.allclose(l, -r) else 0)
print("LEVEL 3  associator sign phi(i,j,k) = (e_i e_j) e_k / e_i (e_j e_k) in {+-1}: values seen %s ; phi=-1 in %d of 4096 triples (catalog: 1848 nonzero associators)" % (sorted(set(phi.flatten().tolist())), int((phi == -1).sum())))
def span(S):
    G = {0}
    for s in S: G |= {g ^ s for g in G}
    return frozenset(G)
dep = lambda i, j, k: k in span([i, j])
nd = [(i, j, k) for i in range(1, 16) for j in range(1, 16) for k in range(1, 16) if not dep(i, j, k)]
print("   nonassociative (phi=-1) among DEPENDENT triples (k in span{i,j}): %d of %d ; among INDEPENDENT triples: %d of %d" % (
      sum(1 for i in range(16) for j in range(16) for k in range(16) if dep(i, j, k) and phi[i, j, k] == -1), sum(1 for i in range(16) for j in range(16) for k in range(16) if dep(i, j, k)),
      sum(1 for t in nd if phi[t] == -1), len(nd)))
print("\nLEVEL 4  subalgebras = subgroups of Z2^4:")
def comp(H, n=30):
    idx = sorted(H); worst = 0
    for _ in range(n):
        x = np.zeros(16); y = np.zeros(16)
        x[idx] = np.random.default_rng(len(idx) + _).normal(size=len(idx)); y[idx] = np.random.default_rng(100 + _).normal(size=len(idx))
        worst = max(worst, abs(np.linalg.norm(m(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)))
    return worst
lines = {span([i, j]) for i in range(1, 16) for j in range(i + 1, 16)}
print("   order 2 (C):  15 subgroups {0,i}")
print("   order 4 (H): %d subgroups = the %d lines of PG(3,2); composition (norm-multiplicative) holds in all: %s" % (len(lines), len(lines), all(comp(H) < 1e-9 for H in lines)))
planes = {span([i, j, k]) for (i, j, k) in nd}
oct_ = []
for H in sorted(planes, key=lambda h: sorted(h)):
    nonassoc = all(phi[i, j, k] == -1 for (i, j, k) in nd if {i, j, k} <= H)
    oct_.append((sorted(H), comp(H) < 1e-9, nonassoc))
print("   order 8: %d subgroups = the 15 hyperplanes ker chi_u (+0); octonion-like (composition AND every independent triple nonassociative): %d of %d" % (len(planes), sum(1 for _, c, n in oct_ if c and n), len(planes)))
for idx, c, n in oct_: print("      %-34s composition=%s  all-independent-triples-nonassociative=%s" % (idx, c, n))
print("   order 16: the sedenions; composition fails (zero divisors): worst |xy|-|x||y| on random pairs = %.3f" % comp(set(range(16))))

print("\nLEVEL 5  projective geometry PG(3,2):  15 points, 35 lines, 15 planes (=hyperplanes), each point on 7 lines")
print("   |GL(4,2)| = 20160 (= A8). Antiflag (point 8, plane P={1..7}): 15 x 8 = 120 antiflags -> stabiliser order 20160/120 = %d (= |PSL(2,7)|)" % (20160 // 120))
print("   Klein correspondence count: lines of PG(3,2) = %d = points of the Klein quadric Q+(5,2) (q^2+1)(q^2+q+1) = %d" % (len(lines), (2 ** 2 + 1) * (2 ** 2 + 2 + 1)))

print("\nLEVEL 6  Assessors from the antiflag (point e8, plane P = {1..7}):")
asr_lines = {}
for (a, b) in asr:
    L = span([a, b + 8]); asr_lines.setdefault(L, []).append((a, b))
print("   each Assessor plane span(e_a, e_{b+8}) lies on a unique PG line {a, b+8, (a^b)+8}: %d Assessors on %d distinct lines, %s Assessors per line" % (len(asr), len(asr_lines), sorted({len(v) for v in asr_lines.values()})))
types = {}
for L in lines:
    P = [i for i in L if 1 <= i <= 7]; Q = [i for i in L if i >= 8]
    key = ("in P" if len(P) == 3 else "1 point of P, 2 outside" if len(P) == 1 else "0 points of P")
    thru8 = 8 in L
    types.setdefault((key, "through e8" if thru8 else "not through e8"), []).append(L)
for k, v in sorted(types.items()): print("      %-45s %-16s %2d lines%s" % (k[0], k[1], len(v), "   <- the Assessor lines" if k == ("1 point of P, 2 outside", "not through e8") else ""))
print("   struts (chart label) s = a xor b  = a point of the lower plane P:  chart s holds the Assessors (a, a^s), a not in {0,s}:  6 each, 7 charts, 42 total")
adj = {}
for (a, b, s1) in DV:
    for (c, d, s2) in DV:
        if np.linalg.norm(m(DV[(a, b, s1)], DV[(c, d, s2)])) < 1e-9: adj.setdefault(((a, b), (c, d)), 0); adj[((a, b), (c, d))] += 1
pairs_pl = set(adj)
pred = {((a, b), (c, d)) for (a, b) in asr for (c, d) in asr if (a ^ b) == (c ^ d) and (c, d) != (a, b) and (c, d) != (b, a)}
print("   EDGE RULE: Assessors (a,b),(c,d) are joined by a vanishing product iff  a^b = c^d (same strut)  and (c,d) != (b,a) (not the reversal): predicate == measured adjacency: %s (%d ordered pairs)" % (pairs_pl == pred, len(pred)))
print("   the necessary identity: basis products of x=e_a+-e_{b+8}, y=e_c+-e_{d+8} cancel in pairs only if  a^c = b^d  (and  a^d = b^c),  i.e.  a^b^c^d = 0;  the signs alpha then pick which 2 of the 4 sign choices annihilate: %s sign choices per adjacent plane pair" % sorted(set(adj.values())))

print("\nLEVEL 7  one box-kite (chart 1): vertices, edges, faces")
import networkx as nx
V = K[1]; Gk = nx.Graph(); Gk.add_nodes_from(V)
for u, v in itertools.combinations(V, 2):
    if (u, v) in pairs_pl or (v, u) in pairs_pl: Gk.add_edge(u, v)
faces = [t for t in itertools.combinations(V, 3) if all(Gk.has_edge(x, y) for x, y in itertools.combinations(t, 2))]
print("   vertices %d, edges %d, triangular faces %d, non-edges (the 3 'struts' in De Marrais's sense = axes joining opposite vertices): %s" % (len(V), Gk.number_of_edges(), len(faces), [(u, v) for u, v in itertools.combinations(V, 2) if not Gk.has_edge(u, v)]))
sails = 0; vents = 0
for t in faces:
    ok = False
    for sg in itertools.product((1, -1), repeat=3):
        ds = [DV[(a, b, s)] for (a, b), s in zip(t, sg)]
        if all(np.linalg.norm(m(ds[i], ds[j])) < 1e-9 for i in range(3) for j in range(3) if i != j): ok = True; break
    sails += ok; vents += (not ok)
print("   faces whose three vertices can carry diagonals that ALL mutually annihilate (both orders): %d ; faces where they cannot: %d" % (sails, vents))
cyc = 0
for t in faces:
    for sg in itertools.product((1, -1), repeat=3):
        ds = [DV[(a, b, s)] for (a, b), s in zip(t, sg)]
        if all(np.linalg.norm(m(ds[i], ds[(i + 1) % 3])) < 1e-9 for i in range(3)): cyc += 1; break
print("   faces carrying a one-direction cycle x1 x2 = x2 x3 = x3 x1 = 0: %d" % cyc)
