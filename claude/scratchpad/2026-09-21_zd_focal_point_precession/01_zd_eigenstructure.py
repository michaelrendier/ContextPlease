"""
01_zd_eigenstructure.py

Cody's claim, 2026-09-21: 0_RB (=e0) is "The Axis" -- fixed, vertical.
The zero-divisor locus produces "the Real Numbers at a precessional
angle" -- a focal point that is TILTED real numbers, not the vertical
e0 axis. Structurally: an 8-cycle 2-stroke engine (the sedenion Wankel)
with one cycle converted to precession.

Uses ValaQuenta/zero_lattice.py's own verified multiply()/e_k() --
the same convention .clauderc_canonical_maths already checked the
{4:8:4} split against -- not a reimplementation.
"""
from __future__ import annotations
import sys
sys.path.insert(0, '/home/rendier/Projects/ThePlace/ValaQuenta')
import numpy as np
from zero_lattice import multiply, e_k, find_zd_pairs   # noqa: E402

np.set_printoptions(precision=4, suppress=True)


def L_matrix(a: np.ndarray) -> np.ndarray:
    """The 16x16 real regular representation of left-multiplication by a:
    L(a) @ v == multiply(a, v), built column by column."""
    M = np.zeros((16, 16))
    for k in range(16):
        M[:, k] = multiply(a, e_k(k))
    return M


# ── canonical ZD element, the one already in the record ────────────────────
a = (e_k(1) + e_k(11)) / np.sqrt(2)
b = (e_k(5) + e_k(15)) / np.sqrt(2)
prod = multiply(a, b)
print("=" * 78)
print("Sanity: canonical ZD pair (e1+e11)/sqrt2 . (e5+e15)/sqrt2")
print("=" * 78)
print(f"  a.b = {prod}  (should be ~0)   max|a.b| = {np.abs(prod).max():.2e}")

M = L_matrix(a)
eigvals, eigvecs = np.linalg.eig(M)
# group eigenvalues by rounded magnitude/type
real_mask = np.abs(eigvals.imag) < 1e-9
lam0 = np.where(real_mask & (np.abs(eigvals.real) < 1e-9))[0]
lam_i = np.where(~real_mask & (np.isclose(np.abs(eigvals), 1.0, atol=1e-6)))[0]
lam_isqrt2 = np.where(~real_mask & (np.isclose(np.abs(eigvals), np.sqrt(2), atol=1e-6)))[0]

print()
print("=" * 78)
print("Eigenvalue structure of L(a), a = canonical ZD element")
print("=" * 78)
print(f"  lambda=0        count={len(lam0):2d}   (real, non-rotational -- 'the water')")
print(f"  lambda=+-i      count={len(lam_i):2d}   (rotational pairs, |lambda|=1)")
print(f"  lambda=+-i*sq2  count={len(lam_isqrt2):2d}   (rotational pairs, |lambda|=sqrt(2))")
print(f"  TOTAL accounted: {len(lam0)+len(lam_i)+len(lam_isqrt2)} / 16")
unaccounted = 16 - (len(lam0)+len(lam_i)+len(lam_isqrt2))
if unaccounted:
    remaining = [eigvals[i] for i in range(16)
                 if i not in lam0 and i not in lam_i and i not in lam_isqrt2]
    print(f"  UNACCOUNTED: {unaccounted}  values: {remaining}")
print()
print(f"  As 2-D ROTATION PAIRS (each +-lambda pair is one 'cylinder'/cycle):")
print(f"    {len(lam_i)//2} pairs at |lambda|=1, {len(lam_isqrt2)//2} pairs at |lambda|=sqrt(2)")
print(f"    = {len(lam_i)//2 + len(lam_isqrt2)//2} rotational cycles, "
      f"{len(lam0)} real (non-cycling) dimensions left over.")
print(f"    16 dims total = {len(lam0)} real + {len(lam_i)+len(lam_isqrt2)} rotational")
print(f"    -> could be read as '8 cycles' (4 pairs @i + 2 pairs @isqrt2 = 6... let's")
print(f"       see the real count above rather than presuming 8 or 16.)")
