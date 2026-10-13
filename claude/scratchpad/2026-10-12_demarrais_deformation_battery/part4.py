#!/usr/bin/env python3
"""PART 4 — the exact live deformations of a De Marrais box kite: flow the whole kite along the derivation algebra (G2).
Orientation: each vertex = native (d+,d-) of its Assessor plane at the start, then free in R^16 as it flows.
Aperture: continuous flows exp(tD) at several t, on all 6 vertices of chart 1 simultaneously, and ALL 7 charts."""
import sys, math
import numpy as np
from scipy.linalg import expm
from cdalg import *
T = table(STD)
unk = 256
rows = []
for i in range(16):
    for j in range(16):
        for k in range(16):
            row = np.zeros(unk)
            for m in range(16):
                if T[i, j, m] != 0: row[k * 16 + m] += T[i, j, m]
                if T[m, j, k] != 0: row[m * 16 + i] -= T[m, j, k]
                if T[i, m, k] != 0: row[m * 16 + j] -= T[i, m, k]
            rows.append(row)
A_ = np.array(rows)
u, s, vt = np.linalg.svd(A_)
null = vt[np.sum(s > 1e-9):]
Ders = [n.reshape(16, 16) for n in null]
print("dim Der =", len(Ders), flush=True)
rng = np.random.default_rng(11)
def rand_der(scale=1.0):
    c = rng.normal(size=len(Ders)); D = sum(ci * Di for ci, Di in zip(c, Ders)); return D * scale / np.linalg.norm(D)
asr = bk.assessors(); K = bk.box_kites()
def kite_vertices(s):    # the 6 vertices' diagonals: for each Assessor, the pair (d+, d-); a ZD relation list is built from the 84
    return [(a, b) for (a, b) in K[s]]
DV = {(a, b, sg): diag_vec(a, b, sg) / math.sqrt(2) for (a, b) in asr for sg in (1, -1)}
pairs = [(k1, k2) for k1 in DV for k2 in DV if np.linalg.norm(mul(DV[k1], DV[k2])) < 1e-9]
print("ZD relations (ordered diagonal pairs):", len(pairs), flush=True)
print("\nDM-20  flow the WHOLE set of 84 diagonals along exp(tD), D a random derivation (unit norm):", flush=True)
print("   t      max ||x(t) y(t)|| over the 336 relations   max angular distance of a diagonal from its lattice line (deg)   still unit norm?")
D = rand_der()
for t in (0.05, 0.3, 1.0, 2.5):
    G = expm(t * D)
    mx = max(np.linalg.norm(mul(G @ DV[k1], G @ DV[k2])) for k1, k2 in pairs)
    ang = 0.0
    for (a, b, sg), v in DV.items():
        w = G @ v; w = w / np.linalg.norm(w)
        ang = max(ang, math.degrees(math.acos(min(1.0, abs(float(w @ v))))))
    print("   %.2f   %.2e                                  %6.2f                                             %s" % (t, mx, ang, abs(np.linalg.norm(G @ DV[(2, 3, 1)]) - 1) < 1e-9), flush=True)
print("\nDM-21  control: flow along a RANDOM orthogonal generator (not a derivation), same t:")
for t in (0.05, 0.3):
    B = rng.normal(size=(16, 16)); B = (B - B.T); B = B / np.linalg.norm(B)
    G = expm(t * B)
    mx = max(np.linalg.norm(mul(G @ DV[k1], G @ DV[k2])) for k1, k2 in pairs)
    print("   t=%.2f  max ||x(t) y(t)|| = %.3f" % (t, mx), flush=True)
print("\nDM-22  dimension of the family of exactly-deformed kites:")
for s_ in range(1, 8):
    vs = [DV[(a, b, 1)] for (a, b) in K[s_]] + [DV[(a, b, -1)] for (a, b) in K[s_]]
    Gm = np.array([np.concatenate([Di @ v for v in vs]) for Di in Ders])
    print("   chart %d: 12 diagonals (6 vertices x 2): orbit rank under Der = %d of 14" % (s_, np.linalg.matrix_rank(Gm, tol=1e-8)), flush=True)
vs = list(DV.values()); Gm = np.array([np.concatenate([Di @ v for v in vs]) for Di in Ders])
print("   all 84 diagonals together: orbit rank %d of 14  (stabiliser dimension %d)" % (np.linalg.matrix_rank(Gm, tol=1e-8), 14 - np.linalg.matrix_rank(Gm, tol=1e-8)), flush=True)
print("\nDM-23  Der sub-structure: which derivations fix a given vertex (stabiliser) and do they fix its partners?")
x = DV[(2, 3, 1)]
Gx = np.array([Di @ x for Di in Ders]).T            # 16 x 14
u_, s_, vt_ = np.linalg.svd(Gx); stab = vt_[np.sum(s_ > 1e-9):]
print("   stabiliser of one diagonal: dim %d" % stab.shape[0], flush=True)
partners = [k2 for (k1, k2) in pairs if k1 == (2, 3, 1)]
Dst = [sum(c * Di for c, Di in zip(row, Ders)) for row in stab]
print("   it has %d partners; derivations fixing x also fix how many of them (rank of their action on the partners): %s" % (
      len(partners), [int(np.linalg.matrix_rank(np.array([np.concatenate([Dd @ DV[p] for p in partners]) for Dd in Dst]), tol=1e-8))]), flush=True)
