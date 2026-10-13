#!/usr/bin/env python3
"""PART 1 — the De Marrais box kite as pure algebra: what preserves it exactly, what is open, first-order response.
Orientation: Assessor = native pair (d+,d-); anchor e0/e8. Aperture: exact symmetry groups AND continuous tangent
analysis at every one of the 84 diagonals (not a lattice pick)."""
import sys, itertools, json, math
import numpy as np
from cdalg import *
R = {}
asr = bk.assessors()                                   # 42 ordered (a,b)
DIAG = [(a, b, s) for (a, b) in asr for s in (1, -1)]  # 84
DV = np.array([diag_vec(a, b, s) for (a, b, s) in DIAG])
nz = lambda v, t=1e-10: np.linalg.norm(v) < t

# ---- DM-00 baseline ----
pairs = [(i, j) for i in range(84) for j in range(84) if nz(mul(DV[i], DV[j]))]
kills = {}
for i, j in pairs: kills[i] = kills.get(i, 0) + 1
R['DM-00'] = dict(assessors=len(asr), diagonals=84, ordered_zd_pairs=len(pairs),
                  kills_per_diagonal=sorted(set(kills.values())), diagonals_with_a_partner=len(kills))
print("DM-00 baseline:", R['DM-00'])

# ---- DM-01 characters (Sylvester-Hadamard rows) are automorphisms ----
rng = np.random.default_rng(1)
def chi(u): return np.array([(-1) ** bin(u & i).count('1') for i in range(16)], float)
worst = 0.0
for u in range(16):
    c = chi(u)
    for _ in range(40):
        x, y = rng.normal(size=(2, 16))
        worst = max(worst, np.linalg.norm(mul(c * x, c * y) - c * mul(x, y)))
R['DM-01'] = dict(characters=16, max_homomorphism_error=worst)
print("DM-01 all 16 Hadamard-row sign flips are automorphisms: max error %.2e" % worst)

# ---- DM-02 which of ALL 65536 diagonal sign operators are automorphisms ----
T = table(STD); tsign = np.zeros((16, 16))
for i in range(16):
    for j in range(16):
        tsign[i, j] = T[i, j, i ^ j]
assert all(abs(abs(tsign[i, j]) - 1) < 1e-12 for i in range(16) for j in range(16))
bits = ((np.arange(65536)[:, None] >> np.arange(16)) & 1)       # sigma_i = (-1)^bit
ok = np.ones(65536, bool)
for i in range(16):
    for j in range(16):
        ok &= ((bits[:, i] ^ bits[:, j] ^ bits[:, i ^ j]) == 0)
R['DM-02'] = dict(sign_operators=65536, automorphisms=int(ok.sum()))
print("DM-02 of 65536 diagonal sign operators, automorphisms: %d (expected 16 = the characters)" % ok.sum())

# ---- DM-03 monomial automorphisms: signed index maps  e_i -> eta_i e_{A i},  A in GL(4,2) ----
def mat_apply(A, i):                                   # A: 4 column bitmasks
    r = 0
    for b in range(4):
        if (i >> b) & 1: r ^= A[b]
    return r
GL = []
for cols in itertools.product(range(1, 16), repeat=4):
    seen, ok_ = set(), True
    # invertible iff the 4 columns are independent
    span = {0}
    for c in cols:
        if c in span: ok_ = False; break
        span |= {s ^ c for s in span}
    if ok_: GL.append(cols)
# equation (i,j): x_{i^j} + x_i + x_j = ctilde(i,j), i,j in 1..15, unknown x_1..x_15 ; (-1)^x = eta
eqs = [(i, j) for i in range(1, 16) for j in range(1, 16)]
def lhs_mask(i, j):
    m = 0
    for k in (i, j, i ^ j):
        if k: m ^= (1 << (k - 1))
    return m
M = [lhs_mask(i, j) for (i, j) in eqs]
# left null space of M over GF(2): dependencies among equations
rows = [(M[e], 1 << e) for e in range(len(eqs))]
piv, deps = {}, []
for m, tag in rows:
    while m:
        h = m.bit_length() - 1
        if h in piv:
            pm, pt = piv[h]; m ^= pm; tag ^= pt
        else:
            piv[h] = (m, tag); break
    if m == 0: deps.append(tag)
rankM = len(piv)
def ctilde(A):
    mask = 0
    for e, (i, j) in enumerate(eqs):
        ai, aj = mat_apply(A, i), mat_apply(A, j)
        c = tsign[i, j] * tsign[ai, aj]            # = eta-cocycle needed
        if c < 0: mask |= (1 << e)
    return mask
good = [A for A in GL if all(bin(d & ctilde(A)).count('1') % 2 == 0 for d in deps)]
R['DM-03'] = dict(GL42=len(GL), rank_of_cocycle_system=rankM, characters=2 ** (15 - rankM),
                  A_admitting_a_sign_lift=len(good), monomial_automorphism_group_order=len(good) * 2 ** (15 - rankM))
print("DM-03 |GL(4,2)|=%d ; A that lift to an automorphism: %d ; each lifts in %d sign ways -> monomial Aut order %d" % (
      len(GL), len(good), 2 ** (15 - rankM), len(good) * 2 ** (15 - rankM)))

# frame-preserving: maps the 84 diagonals onto themselves (as lines)
planes = {frozenset((a, b + 8)) for (a, b) in asr}
fp = [A for A in good if {frozenset((mat_apply(A, a), mat_apply(A, b + 8))) for (a, b) in asr} == planes]
R['DM-03']['frame_preserving_A'] = len(fp)
R['DM-03']['frame_preserving_order'] = len(fp) * 16
print("      of those, preserving the set of 42 Assessor planes: %d  (x16 characters = %d)" % (len(fp), len(fp) * 16))
fixes8 = [A for A in fp if mat_apply(A, 8) == 8]
R['DM-03']['frame_preserving_fixing_e8'] = len(fixes8)
print("      frame-preserving AND fixing e8: %d" % len(fixes8))

# ---- DM-04 derivations: the CONTINUOUS exact deformations ----
rowsD = []
E = np.eye(16)
for i in range(16):
    for j in range(16):
        for k in range(16):
            pass
# D unknown 16x16 with D e_i = sum_k D[k,i] e_k.  eq: D(e_i e_j) - D(e_i) e_j - e_i D(e_j) = 0
unk = 256
A_ = np.zeros((16 * 16 * 16, unk))
r = 0
for i in range(16):
    for j in range(16):
        # D(e_i e_j) = sum_m T[i,j,m] D e_m
        for k in range(16):
            row = np.zeros(unk)
            for m in range(16):
                if T[i, j, m] != 0: row[k * 16 + m] += T[i, j, m]            # D[k,m]
            for m in range(16):
                if T[m, j, k] != 0: row[m * 16 + i] -= T[m, j, k]            # (D e_i)_m e_m e_j -> coefficient on e_k
            for m in range(16):
                if T[i, m, k] != 0: row[m * 16 + j] -= T[i, m, k]            # e_i (D e_j)_m e_m
            A_[r] = row; r += 1
u, sv, vt = np.linalg.svd(A_, full_matrices=True)
null = vt[np.sum(sv > 1e-9):]
dimDer = null.shape[0]
Ders = [n.reshape(16, 16) for n in null]
R['DM-04'] = dict(dim_derivation_algebra=dimDer)
print("DM-04 dimension of Der(sedenions) = %d  (g2 would be 14)" % dimDer)

# orbit of each diagonal under Der: tangent dimension, stabiliser dimension
orb = []
for v in DV:
    G = np.array([D @ v for D in Ders])
    orb.append(np.linalg.matrix_rank(G, tol=1e-8))
R['DM-04']['orbit_tangent_dims_of_84_diagonals'] = sorted(set(orb))
R['DM-04']['stabiliser_dims'] = sorted(set(dimDer - o for o in orb))
print("      tangent dim of the Der-orbit through each diagonal: %s ; stabiliser dims %s" % (sorted(set(orb)), sorted(set(dimDer - o for o in orb))))
# derivations keep the frame? dimension of {D in Der : D d in span(d) for ALL 84 diagonals}
rows_ = []
for v in DV:
    vn = v / np.linalg.norm(v)
    P = np.eye(16) - np.outer(vn, vn)
    rows_.append(np.array([ (P @ (D @ v)) for D in Ders]).T)    # 16 x dimDer
big = np.vstack(rows_)
fr = dimDer - np.linalg.matrix_rank(big, tol=1e-8)
R['DM-04']['derivations_preserving_every_diagonal_line'] = int(fr)
print("      derivations that keep ALL 84 diagonal lines invariant: %d  (0 => every continuous exact deformation moves the kite off its lattice)" % fr)

# ---- DM-05 tangent space of the zero-divisor PAIR variety, per ordered pair ----
nul, rk_orbit, extra = [], [], []
for (i, j) in pairs[:336]:
    x, y = DV[i] / np.linalg.norm(DV[i]), DV[j] / np.linalg.norm(DV[j])
    J = np.hstack([Rmat(y), Lmat(x)])                    # 16 x 32 : d(xy) = R_y dx + L_x dy
    nullity = 32 - np.linalg.matrix_rank(J, tol=1e-9)
    G = np.array([np.concatenate([D @ x, D @ y]) for D in Ders])
    ro = np.linalg.matrix_rank(G, tol=1e-8)
    nul.append(nullity); rk_orbit.append(ro)
R['DM-05'] = dict(pair_tangent_nullity=sorted(set(nul)), derivation_orbit_rank=sorted(set(rk_orbit)))
print("DM-05 tangent space (all directions preserving xy=0 to 1st order) of the pair, per ordered ZD pair: dims %s ; of which derivation (G2) directions: %s" % (sorted(set(nul)), sorted(set(rk_orbit))))
print("      => on the unit spheres: variety dim >= %s ; scaling x,y accounts for 2" % [n - 2 for n in sorted(set(nul))])

# ---- DM-06 first-order response: annihilators and singular values ----
nulls, svs = [], []
for j in range(84):
    s_ = np.linalg.svd(Rmat(DV[j]), compute_uv=False)
    nulls.append(int(np.sum(s_ < 1e-9))); svs.append(tuple(np.round(sorted(s_[s_ >= 1e-9]), 4)))
R['DM-06'] = dict(right_annihilator_dim=sorted(set(nulls)), distinct_nonzero_singular_value_sets=[list(x) for x in sorted(set(svs))][:3])
print("DM-06 dim of {x : x y = 0} for each of the 84 diagonals y: %s ; nonzero singular values of x->xy: %s" % (sorted(set(nulls)), sorted(set(svs))[:2]))
# Walsh probe: delta = Hadamard row u as a perturbation of x, response ||R_y delta||/||delta||
probe = np.zeros((16, 3))
for u in range(16):
    c = chi(u); resp = [np.linalg.norm(Rmat(DV[j]) @ c) / np.linalg.norm(c) for j in range(84)]
    probe[u] = [min(resp), np.mean(resp), max(resp)]
R['DM-06']['walsh_probe_min_mean_max'] = probe.round(4).tolist()
print("      Walsh-row perturbations of x: response ||R_y chi_u||/||chi_u||  (min / mean / max over the 84 y):")
for u in range(16): print("        u=%2d  %.4f  %.4f  %.4f" % ((u,) + tuple(probe[u])))
json.dump(R, open('results_part1.json', 'w'), indent=1, default=str)
