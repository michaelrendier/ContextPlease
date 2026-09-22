"""
02_null_space_vs_e0.py

The real question: is the lambda=0 null space (the "real numbers" the
claim points at) the SAME as e0's own axis, or a genuinely different,
tilted 4-D real locus? And within it, is there a single preferred
direction -- a "focal point" -- or is it a flat, undistinguished
subspace?
"""
from __future__ import annotations
import sys
sys.path.insert(0, '/home/rendier/Projects/ThePlace/ValaQuenta')
import numpy as np
from zero_lattice import multiply, e_k   # noqa: E402

np.set_printoptions(precision=4, suppress=True)


def L_matrix(a: np.ndarray) -> np.ndarray:
    M = np.zeros((16, 16))
    for k in range(16):
        M[:, k] = multiply(a, e_k(k))
    return M


def null_space_real(M: np.ndarray, tol=1e-9) -> np.ndarray:
    """Real orthonormal basis for the lambda=0 eigenspace, via SVD (more
    numerically stable than eig() for a near-singular real matrix)."""
    U, S, Vt = np.linalg.svd(M)
    null_mask = S < tol * S.max()
    # SVD of a singular matrix: right-singular vectors for near-zero
    # singular values span the (right) null space, real by construction
    # since M is real.
    return Vt[null_mask].T   # columns are basis vectors, shape (16, k)


a = (e_k(1) + e_k(11)) / np.sqrt(2)
M = L_matrix(a)
N = null_space_real(M)
print("=" * 78)
print(f"lambda=0 null space of L(a), a=(e1+e11)/sqrt2 -- dimension {N.shape[1]}")
print("=" * 78)
e0 = e_k(0)
proj = N @ (N.T @ e0)             # projection of e0 onto the null space
resid = e0 - proj
print(f"  e0 = {e0}")
print(f"  |e0|  = {np.linalg.norm(e0):.6f}")
print(f"  |proj of e0 onto null(L(a))|      = {np.linalg.norm(proj):.6f}")
print(f"  |residual (e0 minus that proj)|   = {np.linalg.norm(resid):.6f}")
angle = np.degrees(np.arccos(np.clip(np.linalg.norm(proj) / np.linalg.norm(e0), -1, 1)))
print(f"  angle between e0 and null(L(a)) subspace: {angle:.4f} degrees")
print()
if np.linalg.norm(proj) < 1e-9:
    print("  e0 is COMPLETELY ORTHOGONAL to the null space -- e0's own axis")
    print("  and the ZD's real locus do not overlap AT ALL. Confirms the")
    print("  'not the vertical e0 axis' half of the claim directly.")
elif angle < 1e-6:
    print("  e0 LIES INSIDE the null space -- the ZD locus's real axis IS e0.")
else:
    print(f"  e0 is PARTIALLY in the null space -- {angle:.2f} degrees off, ")
    print("  neither fully aligned nor fully orthogonal.")

print()
print("=" * 78)
print("What basis directions actually make up the null space")
print("=" * 78)
for i in range(N.shape[1]):
    v = N[:, i]
    nz = [(k, round(v[k], 4)) for k in range(16) if abs(v[k]) > 1e-6]
    print(f"  null vector {i}: {nz}")
