#!/usr/bin/env python3
"""PART 6 — (a) the Blackjack (21-element) subgroup, (b) the {4:8:4} blocks and the kite's edges,
(c) does the tension-law change with the BRACKETING and FIRING ORDER of the pencil product?  (d) the kernel fiber as a bracket.
Orientation: pairs (d+,d-) native; Aperture: all 168 group elements / all 84 diagonals / all 132 bracketings, exhaustive."""
import sys, itertools, math, random
import numpy as np
from cdalg import *
T = table(STD)
def m(x, y): return np.einsum('i,j,ijk->k', x, y, T)
asr = bk.assessors(); K = bk.box_kites()
DV = {(a, b, s): diag_vec(a, b, s) for (a, b) in asr for s in (1, -1)}
keys = list(DV)
nz = lambda v, t=1e-9: np.linalg.norm(v) < t
pairs = [(k1, k2) for k1 in keys for k2 in keys if nz(m(DV[k1], DV[k2]))]
print("ordered ZD pairs", len(pairs), flush=True)

# ---------- (a) Blackjack ----------
def mat_apply(A, i):
    r = 0
    for b in range(4):
        if (i >> b) & 1: r ^= A[b]
    return r
planes = {frozenset((a, b + 8)) for (a, b) in asr}
G = []
for cols in itertools.product(range(1, 16), repeat=4):
    span = {0}; ok = True
    for c in cols:
        if c in span: ok = False; break
        span |= {s ^ c for s in span}
    if ok and mat_apply(cols, 8) == 8 and {frozenset((mat_apply(cols, a), mat_apply(cols, b + 8))) for (a, b) in asr} == planes:
        G.append(cols)
print("(a) frame-preserving index maps:", len(G))
def perm_vec(A, v):
    w = np.zeros(16)
    for i in range(16): w[mat_apply(A, i)] = v[i]
    return w
def action_on_struts(A):
    return tuple(mat_apply(A, s) for s in range(1, 8))
orders = {}
def compose(A, B): return tuple(mat_apply(A, mat_apply(B, 1 << b)) for b in range(4))
ident = (1, 2, 4, 8)
def order(A):
    n, X = 1, A
    while X != ident: X = compose(A, X); n += 1
    return n
cnt = {}
for A in G: cnt[order(A)] = cnt.get(order(A), 0) + 1
print("    element orders in the 168:", dict(sorted(cnt.items())), " (PSL(2,7): 1x1, 2x21, 3x56, 4x42, 7x48)")
# UNSIGNED permutation matrices: which preserve ALL 336 ZD pairs (as x,y -> P x, P y)?
def preserves_unsigned(A):
    for k1, k2 in pairs:
        if not nz(m(perm_vec(A, DV[k1]), perm_vec(A, DV[k2]))): return False
    return True
good = [A for A in G if preserves_unsigned(A)]
print("    unsigned permutation matrices (no sign lift) that keep ALL 336 pairs: %d of 168" % len(good), flush=True)
cg = {}
for A in good: cg[order(A)] = cg.get(order(A), 0) + 1
print("    their element orders:", dict(sorted(cg.items())))
closed = all(compose(A, B) in set(good) for A in good for B in good)
print("    closed under composition (a subgroup)?", closed)
orb = {s: set() for s in range(1, 8)}
for A in good:
    for s in range(1, 8): orb[s].add(mat_apply(A, s))
print("    orbit of strut 1 under it:", sorted(orb[1]), " -> transitive on the 7 struts?", len(orb[1]) == 7)
# generic characterisation: all 21-element subgroups of the 168 and which one(s) are 'the' preserving one
# ---------- (b) the {4:8:4} blocks ----------
print("\n(b) {4:8:4}: eigen-blocks of R_y^T R_y for each of the 84 diagonals y (x -> x y)")
y = DV[(2, 3, 1)]
R = Rmat(y); w, V = np.linalg.eigh(R.T @ R)
blk = {'null (gain 0)': V[:, w < 1e-9], 'gain |y|': V[:, (w > 1e-9) & (w < 2.5)], 'gain sqrt2|y|': V[:, w > 2.5]}
print("    eigenvalues of R^T R:", sorted(set(np.round(w, 6))), "dims:", {k: v.shape[1] for k, v in blk.items()})
def proj(B): return B @ B.T
Pn, P1, P2 = proj(blk['null (gain 0)']), proj(blk['gain |y|']), proj(blk['gain sqrt2|y|'])
print("    index weight of each block (diag of projector, indices 0..15):")
for name, P in (('null', Pn), ('gain 1', P1), ('gain sqrt2', P2)):
    print("      %-11s" % name, np.round(np.diag(P), 3).tolist())
# neighbours (edges) of y: the 4 diagonals x with x y = 0
nbrs = [k1 for (k1, k2) in pairs if k2 == (2, 3, 1)]
print("    the 4 edge-partners x (x y = 0):", nbrs)
sp = np.array([DV[k] / np.linalg.norm(DV[k]) for k in nbrs]); rk = np.linalg.matrix_rank(sp, tol=1e-9)
inN = [np.linalg.norm(Pn @ (DV[k] / np.linalg.norm(DV[k]))) for k in nbrs]
print("    they span rank %d; fraction of each lying in the null block: %s" % (rk, np.round(inN, 6).tolist()))
# classify all 84 diagonals by block
print("    where the 84 diagonals sit relative to y=(2,3,+): (norm in null / gain1 / gain-sqrt2)")
rows = []
for k in keys:
    x = DV[k] / np.linalg.norm(DV[k]); rows.append((k, np.linalg.norm(Pn @ x), np.linalg.norm(P1 @ x), np.linalg.norm(P2 @ x)))
kinds = {}
for k, a, b, c in rows:
    key = (round(a, 3), round(b, 3), round(c, 3)); kinds.setdefault(key, []).append(k)
for key, ks in sorted(kinds.items(), key=lambda t: -len(t[1])):
    tag = "y itself" if (2, 3, 1) in ks else ""
    print("      (%.3f %.3f %.3f) x%-3d e.g. %s %s" % (key + (len(ks), ks[0], tag)))
# the same chart: opposite vertex?
chart1 = set(K[1]); 
print("    chart 1 assessors:", K[1], " y=(2,3): opposite vertex is the reversal (3,2)")
for k in ((3, 2, 1), (3, 2, -1)):
    x = DV[k] / np.linalg.norm(DV[k]); print("      reversal %s : null %.3f, gain1 %.3f, gain-sqrt2 %.3f" % (k, np.linalg.norm(Pn @ x), np.linalg.norm(P1 @ x), np.linalg.norm(P2 @ x)))
# left annihilator vs right
L = Lmat(y); wl, Vl = np.linalg.eigh(L.T @ L); NL = Vl[:, wl < 1e-9]
print("    left-annihilator {x : y x = 0} dim %d ; principal-angle overlap with the right-annihilator: %.3f" % (NL.shape[1], np.linalg.norm(Pn @ NL) ** 2 / NL.shape[1]))
print("    gain-sqrt2 block vs left-annihilator overlap: %.3f" % (np.linalg.norm(P2 @ NL) ** 2 / NL.shape[1]))
# emerger's fixed index assignment {4..7}/{1,2,3,8..11}/{12..15} vs the real blocks
def idxproj(idx): 
    P = np.zeros((16, 16)); 
    for i in idx: P[i, i] = 1
    return P
EM = {'{4..7}': [4, 5, 6, 7], '{1,2,3,8..11}': [1, 2, 3, 8, 9, 10, 11], '{12..15}': [12, 13, 14, 15]}
print("    overlap of the emerger's fixed index sets with the real blocks of this diagonal (tr(P_idx P_block)/dim):")
for n, idx in EM.items():
    Pi = idxproj(idx); print("      %-14s null %.2f  gain1 %.2f  gain-sqrt2 %.2f" % (n, np.trace(Pi @ Pn) / 4, np.trace(Pi @ P1) / 8, np.trace(Pi @ P2) / 4))
