import sys, itertools, math, random
import numpy as np
from cdalg import *
T = table(STD)
def m(x, y): return np.einsum('i,j,ijk->k', x, y, T)
asr = bk.assessors(); K = bk.box_kites()
DV = {(a, b, s): diag_vec(a, b, s) for (a, b) in asr for s in (1, -1)}
def mat_apply(A, i):
    r = 0
    for b in range(4):
        if (i >> b) & 1: r ^= A[b]
    return r
planes = {frozenset((a, b + 8)) for (a, b) in asr}
G = [c for c in itertools.product(range(1, 16), repeat=4)
     if len({0}.union(*[]) ) == 1 and True]
# (re)build the 168
G = []
for cols in itertools.product(range(1, 16), repeat=4):
    span = {0}; ok = True
    for c in cols:
        if c in span: ok = False; break
        span |= {s ^ c for s in span}
    if ok and mat_apply(cols, 8) == 8 and {frozenset((mat_apply(cols, a), mat_apply(cols, b + 8))) for (a, b) in asr} == planes: G.append(cols)
tsign = np.array([[T[i, j, i ^ j] for j in range(16)] for i in range(16)])
# (a2) Blackjack = the sign-free (pure permutation) automorphisms?
free = [A for A in G if all(abs(tsign[mat_apply(A, i), mat_apply(A, j)] - tsign[i, j]) < 1e-12 for i in range(16) for j in range(16))]
print("(a2) index maps A that are AUTOMORPHISMS with all signs +1 (pure relabelling): %d of 168" % len(free))
# characters times A ; which A have a sign lift whose signs are all +1 up to a character?
# (b2) for every diagonal y, which Hadamard character separates its gain-1 block (indices) from the 4+4?
print("\n(b2) for each of the 84 diagonals: the character u such that  gain-1 block = coordinate subspace {i : chi_u(i)=+1}")
def chi(u): return np.array([(-1) ** bin(u & i).count('1') for i in range(16)])
us = {}
for (a, b, s), y in DV.items():
    R = Rmat(y); w, V = np.linalg.eigh(R.T @ R)
    B1 = V[:, (w > 1e-9) & (w < 2.5 * 1.0)]
    d1 = np.round(np.diag(B1 @ B1.T), 6)
    hit = [u for u in range(1, 16) if np.allclose(d1, (chi(u) == 1).astype(float))]
    us.setdefault(tuple(hit), []).append((a, b, s))
for k, v in us.items(): print("   u = %s : %d diagonals, e.g. %s" % (k, len(v), v[:3]))
print("   by strut of the plane (a XOR b) -> u :")
bystrut = {}
for k, v in us.items():
    for (a, b, s) in v: bystrut.setdefault(a ^ b, set()).add(k)
for st in sorted(bystrut): print("      strut %d -> u %s" % (st, sorted(bystrut[st])))

# (c) bracketing and firing order of the pencil product
def trees(n):                      # all full binary trees over leaves 0..n-1 in order
    if n == 1: yield 0; return
    for k in range(1, n):
        for L in trees(k):
            for R_ in trees(n - k): yield (L, R_)
def shift(t, off): return t + off if isinstance(t, int) else (shift(t[0], off), shift(t[1], off))
def all_trees(lo, hi):
    if hi - lo == 1: yield lo; return
    for mid in range(lo + 1, hi):
        for L in all_trees(lo, mid):
            for R_ in all_trees(mid, hi): yield (L, R_)
TR = list(all_trees(0, 7)); print("\n(c) %d bracketings of 7 factors (Catalan(6) = 132)" % len(TR))
def ev(tree, fs):
    if isinstance(tree, int): return fs[tree]
    return m(ev(tree[0], fs), ev(tree[1], fs))
def gen(a, b, phi): v = np.zeros(16); v[a] = math.cos(phi); v[b] = math.sin(phi); return v
def Hval(st, ph, tree, order=None):
    idx = order if order is not None else range(7)
    fs = [gen(*st[k], ph[k]) for k in idx]
    return ev(tree, fs)[0]
rng = np.random.default_rng(5)
HP = math.pi / 2
def analyse(st, tree, order=None, npt=10):
    P = rng.uniform(0, HP, size=(npt, 7)); Gm = []
    for ph in P:
        g = []
        for k in range(7):
            u = ph.copy(); d = ph.copy(); u[k] += 1e-6; d[k] -= 1e-6
            g.append((Hval(st, u, tree, order) - Hval(st, d, tree, order)) / 2e-6)
        Gm.append(g)
    Gm = np.array(Gm); sv = np.linalg.svd(Gm, compute_uv=False)
    rank = int(np.sum(sv > 1e-3 * sv[0])) if sv[0] > 1e-9 else 0
    pat = None
    if rank == 1:
        v = np.linalg.svd(Gm)[2][0]
        if np.allclose(np.abs(v), np.abs(v[0]), atol=1e-4): pat = "".join('+' if x * v[0] > 0 else '-' for x in v)
    return rank, pat
print("   pencil r : bracketings giving rank 1 (single-phase law) / total 132 ; distinct sign patterns among them")
H8 = {}
for r in (1, 2, 4, 8, 9, 10, 12, 15):
    st = bk.pencil(r); rk1 = 0; pats = set(); ranks = {}
    for t in TR:
        rank, pat = analyse(st, t)
        ranks[rank] = ranks.get(rank, 0) + 1
        if rank == 1: rk1 += 1; pats.add(pat)
    print("   r=%2d : rank1 %3d/132 ; rank histogram %s ; patterns %d" % (r, rk1, dict(sorted(ranks.items())), len(pats)), flush=True)
    H8[r] = pats
# is the sign pattern for r<=7 always +/- a Hadamard row (on j=k-1) regardless of bracketing?
def had(i): return "".join('+' if bin(i & j).count('1') % 2 == 0 else '-' for j in range(7))
rows = {had(i) for i in range(8)} | {"".join('-' if c == '+' else '+' for c in had(i)) for i in range(8)}
for r, pats in H8.items():
    print("      r=%2d patterns that are +/- Hadamard rows: %d of %d ; non-Hadamard e.g. %s" % (r, sum(1 for p in pats if p in rows), len(pats), [p for p in pats if p not in rows][:3]))
# firing order: permute the 7 stations, left bracketing
left = TR[[i for i, t in enumerate(TR) if t == ((((((0, 1), 2), 3), 4), 5), 6)][0]]
print("\n   firing order (permuting the 7 stations, left-bracketed product), 300 random permutations per pencil:")
for r in (1, 9, 10):
    st = bk.pencil(r); r1 = 0; pats = set(); rks = {}
    for _ in range(300):
        perm = list(range(7)); random.shuffle(perm)
        rank, pat = analyse(st, left, order=perm, npt=8); rks[rank] = rks.get(rank, 0) + 1
        if rank == 1: r1 += 1; pats.add(pat)
    print("   r=%2d : rank histogram %s ; rank-1 orders %d/300 ; sign patterns %d distinct" % (r, dict(sorted(rks.items())), r1, len(pats)), flush=True)

# (d) the kernel fiber as a BRACKET: psi = c e0 + d/sqrt2 (e_a + e_b), a^b = s
print("\n(d) kernel fiber as written: support {e0, e_a, e_b}; strut s = a XOR b -> the Fano line {a, b, s}")
import importlib
for strut in (1, 2, 5):
    a, b = K[strut][0]; s = a ^ b
    idx = [0, a, b, s]
    closed = all(np.count_nonzero(np.abs(m(np.eye(16)[i], np.eye(16)[j])) > 1e-12) == 1 and int(np.argmax(np.abs(m(np.eye(16)[i], np.eye(16)[j])))) in idx for i in idx for j in idx)
    # Assessor version support {a, b+8}: closure
    idx2 = [0, a, b + 8]; closed2 = all(int(np.argmax(np.abs(m(np.eye(16)[i], np.eye(16)[j])))) in idx2 for i in idx2 for j in idx2)
    print("   strut %d : (a,b)=(%d,%d), s=%d : span{e0,e_a,e_b,e_s} closed under products (a quaternion subalgebra)? %s ; span{e0,e_a,e_{b+8}} closed? %s" % (strut, a, b, s, closed, closed2))
try:
    em = importlib.import_module('ValaQuenta.modules.emerger.maths')
    for strut in (1, 2, 5):
        a, b = K[strut][0]
        print("   emerger.domain_of({a,b,s}) strut %d = %s ; domain_of({a, b+8}) = %s" % (strut, em.domain_of({a, b, a ^ b}), em.domain_of({a, b + 8})))
except Exception as e:
    print("   (emerger.domain_of not callable here:", repr(e)[:100], ")")
