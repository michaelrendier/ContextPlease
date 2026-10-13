import sys, os
sys.path.insert(0, '/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-10-12_demarrais_deformation_battery')
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
import numpy as np
from cdalg import *
HERE = os.path.dirname(os.path.abspath(__file__))
def derivations():
    """Orthonormal basis (Frobenius) of Der(sedenions): list of 14 16x16 matrices; cached."""
    f = os.path.join(HERE, 'ders.npy')
    if os.path.exists(f): return list(np.load(f))
    T = table(STD); rows = []
    for i in range(16):
        for j in range(16):
            for k in range(16):
                row = np.zeros(256)
                for m in range(16):
                    if T[i, j, m] != 0: row[k * 16 + m] += T[i, j, m]
                    if T[m, j, k] != 0: row[m * 16 + i] -= T[m, j, k]
                    if T[i, m, k] != 0: row[m * 16 + j] -= T[i, m, k]
                rows.append(row)
    u, s, vt = np.linalg.svd(np.array(rows)); null = vt[np.sum(s > 1e-9):]
    Ds = [n.reshape(16, 16) for n in null]; np.save(f, np.array(Ds)); return Ds
asr = bk.assessors(); K = bk.box_kites()
DV = {(a, b, s): diag_vec(a, b, s) for (a, b) in asr for s in (1, -1)}
T_ = table(STD)
def m(x, y): return np.einsum('i,j,ijk->k', x, y, T_)
