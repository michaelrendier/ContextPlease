#!/usr/bin/env python3
"""How the 16 components transform under the continuous symmetry group G2 (= exp of the 14 derivations)."""
import numpy as np
from common import *
Ds = derivations()
print("derivations found:", len(Ds), "; max |D + D^T| (skew-symmetry) =", max(np.abs(D + D.T).max() for D in Ds))
# fixed subspace
M = np.vstack(Ds); u, s, vt = np.linalg.svd(M); fix = vt[np.sum(s > 1e-9):]
print("FIXED subspace of all 14 derivations: dim %d ; spanned by indices %s" % (fix.shape[0], sorted({int(np.argmax(np.abs(r))) for r in fix})))
Cas = -sum(D @ D for D in Ds); w = np.linalg.eigvalsh(Cas)
vals = {}
for x in np.round(w, 6): vals[x] = vals.get(x, 0) + 1
print("Casimir (-sum D^2) eigenvalues with multiplicities:", dict(sorted(vals.items())))
# block structure: do derivations preserve the lower/upper halves?
low = list(range(8)); up = list(range(8, 16))
off = max(np.abs(D[np.ix_(up, low)]).max() for D in Ds), max(np.abs(D[np.ix_(low, up)]).max() for D in Ds)
print("max |off-diagonal block| (lower<->upper) of the derivations: %.1e, %.1e  -> halves preserved: %s" % (off[0], off[1], max(off) < 1e-9))
print("derivation matrices touching e0 or e8 at all: %.1e" % max(np.abs(D[[0, 8], :]).max() for D in Ds))
# commutant dimension
n = 16; rows = [np.kron(np.eye(n), D) - np.kron(D.T, np.eye(n)) for D in Ds]
A = np.vstack(rows); sv = np.linalg.svd(A, compute_uv=False); print("commutant of the 14 derivations (matrices commuting with all): dim %d" % int(np.sum(sv < 1e-9) + (n * n - len(sv))))
# lower and upper imaginary 7-blocks: same rep? intertwiner dimension
Dl = [D[1:8, 1:8] for D in Ds]; Du = [D[9:16, 9:16] for D in Ds]
rows = [np.kron(np.eye(7), Dl_) - np.kron(Du_.T, np.eye(7)) for Dl_, Du_ in zip(Dl, Du)]
sv = np.linalg.svd(np.vstack(rows), compute_uv=False); print("intertwiners from the lower 7 to the upper 7: dim %d" % int(np.sum(sv < 1e-9)))
irr = [np.linalg.matrix_rank(np.array([D[1:8, 1:8].flatten() for D in Ds]), tol=1e-9)]
print("the 14 derivations restricted to the lower 7 span a space of dimension", irr[0], "(so0(7) would be 21; g2 is 14)")
