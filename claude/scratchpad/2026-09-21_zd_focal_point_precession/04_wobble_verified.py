"""
04_wobble_verified.py

Same test as 03, but using ONLY genuine ZD pairs pulled directly from
ValaQuenta's own find_zd_pairs() (not hand-constructed indices), grouped
by strut = i XOR k for Assessor form (e_i + e_{k+8}), i,k in 1..7. Rules
out an indexing artifact in the earlier pass.
"""
from __future__ import annotations
import sys
sys.path.insert(0, '/home/rendier/Projects/ThePlace/ValaQuenta')
import numpy as np
from zero_lattice import multiply, e_k, find_zd_pairs   # noqa: E402

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
    Qa, _ = np.linalg.qr(A)
    Qb, _ = np.linalg.qr(B)
    _, s, _ = np.linalg.svd(Qa.T @ Qb)
    return np.degrees(np.arccos(np.clip(s, -1, 1)))


pairs = find_zd_pairs()
by_strut = {}
for a_vec, b_vec, (i, j), (k, l) in pairs:
    if i in range(1, 8) and j - 8 in range(1, 8):
        strut = i ^ (j - 8)
        by_strut.setdefault(strut, []).append((a_vec, (i, j)))

e0 = e_k(0)
results = {}
for s in sorted(by_strut):
    zd, (i, j) = by_strut[s][0]     # first genuine pair for this strut
    M = L_matrix(zd)
    N = null_space_real(M)
    proj_norm = np.linalg.norm(N @ (N.T @ e0))
    angle_to_e0 = np.degrees(np.arccos(np.clip(proj_norm, -1, 1)))
    results[s] = (zd, N, angle_to_e0, (i, j))
    print(f"strut {s}: Assessor (e{i}, e{j})  null_dim={N.shape[1]}  "
          f"angle(e0, null)={angle_to_e0:.4f} deg")

print()
print("=" * 78)
print("Consecutive-strut principal angles, GENUINE ZD pairs only")
print("=" * 78)
strut_list = sorted(results)
for idx in range(len(strut_list) - 1):
    s1, s2 = strut_list[idx], strut_list[idx + 1]
    pa = principal_angles(results[s1][1], results[s2][1])
    print(f"  strut {s1} -> strut {s2}:  principal angles = {pa}")
pa = principal_angles(results[strut_list[-1]][1], results[strut_list[0]][1])
print(f"  strut {strut_list[-1]} -> strut {strut_list[0]} (wrap): principal angles = {pa}")

print()
print("=" * 78)
print("Cross-check: EVERY genuine ZD pair (all 84), not just one per strut --")
print("does angle(e0, null-space) stay exactly 90 in general, or was that")
print("specific to the small sample above?")
print("=" * 78)
angles = []
for a_vec, b_vec, (i, j), (k, l) in pairs:
    M = L_matrix(a_vec)
    N = null_space_real(M)
    proj_norm = np.linalg.norm(N @ (N.T @ e0))
    ang = np.degrees(np.arccos(np.clip(proj_norm, -1, 1)))
    angles.append(ang)
angles = np.array(angles)
print(f"  n={len(angles)}  min={angles.min():.6f}  max={angles.max():.6f}  "
      f"mean={angles.mean():.6f}  std={angles.std():.2e}")
