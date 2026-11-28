#!/usr/bin/env python3
"""Is the kernel's as-written fibre  psi = sqrt(1-d^2) e0 + d/sqrt2 (e_a + e_b)  inside the NOW (gain-1, isometric) block of the Assessor (a,b) it names?
Test: for y = e_a +- e_{b+8} (both diagonals of the Assessor), |x y| = |x||y| for x = psi  (right multiplication acts isometrically on the gain-1 block),
and the block's polar character u (unique nonzero u in F2^3 with u.a = u.b = 0) has chi_u(0)=chi_u(a)=chi_u(b)=+1."""
import numpy as np, math
from common import *
def chi(u, i): return (-1) ** bin(u & i).count('1')
print("strut  Assessor(a,b)  polar u   chi_u(0,a,b)   |psi y|/(|psi||y|) for y=e_a+e_{b+8}, e_a-e_{b+8}   (1.0000 => psi is in the isometric 'now' block)   vs the Assessor diagonal itself")
for s in range(1, 8):
    for (a, b) in K[s][:2]:
        u = [u for u in range(1, 8) if bin(u & a).count('1') % 2 == 0 and bin(u & b).count('1') % 2 == 0][0]
        out = []
        for d in (0.3, 0.6, 1.0):
            psi = np.zeros(16); psi[0] = math.sqrt(1 - d * d); psi[a] = d / math.sqrt(2); psi[b] = d / math.sqrt(2)
            r = [np.linalg.norm(m(psi, DV[(a, b, sg)])) / (np.linalg.norm(psi) * np.linalg.norm(DV[(a, b, sg)])) for sg in (1, -1)]
            out.append("%.4f/%.4f" % tuple(r))
        diag = np.zeros(16); diag[a] = 1; diag[b + 8] = 1
        rd = np.linalg.norm(m(diag, DV[(a, b, 1)])) / (np.linalg.norm(diag) * np.linalg.norm(DV[(a, b, 1)]))
        print("  %d     (%d,%d)          u=%d      %s     d=.3 %s | d=.6 %s | d=1 %s      diag*diag %.4f" % (s, a, b, u, (chi(u, 0), chi(u, a), chi(u, b)), out[0], out[1], out[2], rd))
# is psi in the quaternion line {a,b,s} subset of the now octonion?
print("\nthe fibre's support {0,a,b,s=a^b} is the quaternion line of the Assessor's Fano line; chi_u(s) = chi_u(a) chi_u(b) = +1, so the line sits inside ker chi_u = the NOW octonion.")
