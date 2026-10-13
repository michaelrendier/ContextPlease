"""Generalised Cayley-Dickson algebra on R^16 with a parameter mu at each doubling level.
(a,b)(c,d) = (a c + mu * d* b ,  d a + b c*)       mu = -1 at every level = the standard sedenions.
Levels: 1 R->C, 2 C->H, 3 H->O, 4 O->S.  mus = (mu1, mu2, mu3, mu4).
Basis product is always  e_i e_j = s(i,j) * m(i,j) * e_{i xor j}  (sign s, magnitude m from the mus).
"""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.box_kite import maths as bk

def _conj(x):
    y = -x.copy(); y[0] = x[0]; return y

def cd_mul(x, y, mus):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    mu = mus[int(np.log2(n)) - 1]
    a, b = x[:h], x[h:]; c, d = y[:h], y[h:]
    sub = mus
    left  = cd_mul(a, c, sub) + mu * cd_mul(_conj(d), b, sub)
    right = cd_mul(d, a, sub) + cd_mul(b, _conj(c), sub)
    return np.concatenate([left, right])

STD = (-1.0, -1.0, -1.0, -1.0)
def mul(x, y, mus=STD):
    return cd_mul(np.asarray(x), np.asarray(y), mus)

_tabs = {}
def table(mus=STD):
    """T[i,j,:] = e_i e_j as a 16-vector."""
    key = tuple(mus)
    if key not in _tabs:
        cplx = any(np.iscomplexobj(m) and np.imag(m) != 0 for m in mus)
        T = np.zeros((16, 16, 16), dtype=complex if cplx else float)
        E = np.eye(16)
        for i in range(16):
            for j in range(16):
                T[i, j] = cd_mul(E[i], E[j], mus)
        _tabs[key] = T
    return _tabs[key]

def Rmat(y, mus=STD):   # x -> x y   (16x16)
    T = table(mus); return np.einsum('ijk,j->ki', T, np.asarray(y))
def Lmat(x, mus=STD):   # y -> x y
    T = table(mus); return np.einsum('i,ijk->kj', np.asarray(x), T)

def diag_vec(a, b, sign):   # e_a + sign e_{b+8}  (unnormalised, as in the catalog)
    v = np.zeros(16); v[a] = 1.0; v[b + 8] = sign; return v

if __name__ == '__main__':
    # compare with the repo's multiply on all basis pairs (and on random vectors)
    E = np.eye(16); bad = 0
    for i in range(16):
        for j in range(16):
            if not np.allclose(mul(E[i], E[j]), bk.multiply(list(E[i]), list(E[j]))): bad += 1
    rng = np.random.default_rng(0)
    badr = sum(not np.allclose(mul(x, y), bk.multiply(list(x), list(y)))
               for x, y in (rng.normal(size=(2, 16)) for _ in range(50)))
    print("basis-pair mismatches vs bk.multiply:", bad, "/ 256 ; random-vector mismatches:", badr, "/ 50")
