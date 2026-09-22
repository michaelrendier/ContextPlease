"""
03_wobble_across_struts.py

"A tilted axis always leads to a wobble" -- Cody. If the ZD locus's real
(lambda=0) focal direction is genuinely tilted relative to e0, moving
across the 7 struts / 42 Assessors should show it PRECESSING -- sweeping
around, not sitting at one fixed random-looking direction each time.
Tested directly: one canonical ZD pair per strut (s = a XOR b, a,b in
1..7, Assessor = span(e_a, e_{b+8})), track (a) angle to e0 (is it always
90 degrees, or does IT wobble too), (b) the null space's own orientation
drift from strut to strut (principal angles between consecutive struts'
null spaces -- a genuine precession signature would show smooth, small
consecutive angles, not random ones).
"""
from __future__ import annotations
import sys
sys.path.insert(0, '/home/rendier/Projects/ThePlace/ValaQuenta')
import numpy as np
from zero_lattice import multiply, e_k   # noqa: E402

np.set_printoptions(precision=4, suppress=True)


def L_matrix(vec: np.ndarray) -> np.ndarray:
    M = np.zeros((16, 16))
    for k in range(16):
        M[:, k] = multiply(vec, e_k(k))
    return M


def null_space_real(M: np.ndarray, tol=1e-9) -> np.ndarray:
    U, S, Vt = np.linalg.svd(M)
    return Vt[S < tol * S.max()].T


def principal_angles(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Principal angles (degrees) between two subspaces given as
    orthonormal-column bases A, B (both already orthonormal from SVD)."""
    Qa, _ = np.linalg.qr(A)
    Qb, _ = np.linalg.qr(B)
    _, s, _ = np.linalg.svd(Qa.T @ Qb)
    s = np.clip(s, -1, 1)
    return np.degrees(np.arccos(s))


# One canonical Assessor per strut s=1..7: pick a=s, b=1 (a!=b required by
# the Assessor definition a != b in the canonical-maths file's box-kite
# section) -- if a==b use b=2 instead, still inside the same strut family.
e0 = e_k(0)
results = {}
for s in range(1, 8):
    a_idx, b_idx = s, (1 if s != 1 else 2)
    zd = (e_k(a_idx) + e_k(b_idx + 8)) / np.sqrt(2)
    M = L_matrix(zd)
    N = null_space_real(M)
    proj_norm = np.linalg.norm(N @ (N.T @ e0))
    angle_to_e0 = np.degrees(np.arccos(np.clip(proj_norm, -1, 1)))
    results[s] = (zd, N, angle_to_e0)
    print(f"strut {s}: Assessor (e{a_idx}, e{b_idx+8})  null_dim={N.shape[1]}  "
          f"angle(e0, null)={angle_to_e0:.4f} deg")

print()
print("=" * 78)
print("Consecutive-strut principal angles between null spaces -- a genuine")
print("precession/wobble should show a SMOOTH, non-random walk; if the")
print("angles jump around with no pattern, it's noise, not a wobble.")
print("=" * 78)
for s in range(1, 7):
    N1 = results[s][1]
    N2 = results[s + 1][1]
    pa = principal_angles(N1, N2)
    print(f"  strut {s} -> strut {s+1}:  principal angles = {pa}")

print()
print("wrap-around (strut 7 -> strut 1):")
pa = principal_angles(results[7][1], results[1][1])
print(f"  principal angles = {pa}")
