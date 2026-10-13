import sys, itertools
import numpy as np
from cdalg import *
T = table(STD)
asr = bk.assessors()
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
    if ok and mat_apply(cols, 8) == 8 and {frozenset((mat_apply(cols, a), mat_apply(cols, b + 8))) for (a, b) in asr} == planes: G.append(cols)
ts = np.array([[T[i, j, i ^ j] for j in range(16)] for i in range(16)])
free = {A for A in G if all(abs(ts[mat_apply(A, i), mat_apply(A, j)] - ts[i, j]) < 1e-12 for i in range(16) for j in range(16))}
DV = {(a, b, s): diag_vec(a, b, s) for (a, b) in asr for s in (1, -1)}
def m(x, y): return np.einsum('i,j,ijk->k', x, y, T)
pairs = [(k1, k2) for k1 in DV for k2 in DV if np.linalg.norm(m(DV[k1], DV[k2])) < 1e-9]
def perm_vec(A, v):
    w = np.zeros(16)
    for i in range(16): w[mat_apply(A, i)] = v[i]
    return w
zdkeep = {A for A in G if all(np.linalg.norm(m(perm_vec(A, DV[k1]), perm_vec(A, DV[k2]))) < 1e-9 for k1, k2 in pairs)}
print("(i) pure-relabelling automorphisms == unsigned maps keeping all 336 ZD pairs ?  sizes %d, %d ; identical sets: %s" % (len(free), len(zdkeep), free == zdkeep))
# (ii) rule u(y) = the unique nonzero u in F2^3 orthogonal to both a and b
def dot(u, x): return bin(u & x).count('1') % 2
def chi(u): return np.array([(-1) ** bin(u & i).count('1') for i in range(16)])
bad = 0; seen = {}
for (a, b, s), y in DV.items():
    R = Rmat(y); w, V = np.linalg.eigh(R.T @ R); B1 = V[:, (w > 1e-9) & (w < 2.5)]
    d1 = np.round(np.diag(B1 @ B1.T), 6)
    cand = [u for u in range(1, 8) if dot(u, a) == 0 and dot(u, b) == 0]
    u = cand[0]; ok = np.allclose(d1, (chi(u) == 1).astype(float)); bad += (not ok) or len(cand) != 1
    seen.setdefault(u, 0); seen[u] += 1
print("(ii) rule 'u = the unique nonzero u in F2^3 with u.a = u.b = 0' reproduces the 8-block for all 84 diagonals: failures = %d ; diagonals per u: %s" % (bad, seen))
# (iii) the 8-block as a subalgebra: indices {i : chi_u(i)=+1}
for u in (4, 2, 1):
    idx = [i for i in range(16) if chi(u)[i] == 1]
    cl = all((i ^ j) in idx for i in idx for j in idx)
    print("(iii) u=%d : 8-block indices %s closed under XOR (a subalgebra): %s" % (u, idx, cl))
# which characters appear at all
print("(iv) characters u in 1..15 that arise as a diagonal's {4:8:4} split: %s ; never: %s" % (sorted(seen), sorted(set(range(1, 16)) - set(seen))))
