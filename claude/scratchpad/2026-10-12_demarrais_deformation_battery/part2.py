#!/usr/bin/env python3
"""PART 2 — operators on the 336 ordered zero-divisor pairs, and the algebra-parameter scan with the UNS constants.
Orientation: the plane P=(a,b) is span(e_a, e_{b+8}); a ZD direction in it is (c,s)=(cos,sin) in that plane (native pair).
Aperture: continuous -- the ZD directions are SOLVED for (null space + rank-1 condition), never assumed to be 45 deg."""
import sys, json, math, itertools
import numpy as np
from cdalg import *
R = {}
asr = bk.assessors()
DV = np.array([diag_vec(a, b, s) for (a, b) in asr for s in (1, -1)])
nz = lambda v, t=1e-9: np.linalg.norm(v) < t
pairs = [(i, j) for i in range(84) for j in range(84) if nz(mul(DV[i], DV[j]))]
print("pairs", len(pairs), flush=True)
rng = np.random.default_rng(3)
def chi(u): return np.array([(-1) ** bin(u & i).count('1') for i in range(16)], float)
def perm_op(f):                       # unsigned index relabel e_i -> e_{f(i)}
    def op(v):
        w = np.zeros(16); 
        for i in range(16): w[f(i)] = v[i]
        return w
    return op
def conj(v): w = -v.copy(); w[0] = v[0]; return w
def Lt(t): return lambda v: mul(np.eye(16)[t], v)
def Rt(t): return lambda v: mul(v, np.eye(16)[t])
H16 = np.array([[(-1) ** bin(i & j).count('1') for j in range(16)] for i in range(16)], float) / 4.0
gray = lambda i: i ^ (i >> 1)
bitrev = lambda i: int(format(i, '04b')[::-1], 2)
def plane_rot(theta):                 # rotate in the (e_a, e_{b+8}) plane of ... applied per-vector: rotate every (k, k+8) pair
    def op(v):
        w = v.copy()
        for k in range(8):
            w[k] = math.cos(theta) * v[k] - math.sin(theta) * v[k + 8]
            w[k + 8] = math.sin(theta) * v[k] + math.cos(theta) * v[k + 8]
        return w
    return op
def frac(pred):
    return sum(1 for (i, j) in pairs if pred(DV[i], DV[j])) / len(pairs)
ops = {
 'identity': lambda v: v.copy(),
 'scale x2.5': lambda v: 2.5 * v,
 'conjugation (e_k -> -e_k, k>0)': conj,
 'WHT (dense Hadamard transform / 4)': lambda v: H16 @ v,
 'Gray-code index map (unsigned)': perm_op(gray),
 'bit-reversal index map (unsigned)': perm_op(bitrev),
 'swap halves e_i <-> e_{i+8}': perm_op(lambda i: i ^ 8),
 'rotate every (k,k+8) pair by 0.3 rad': plane_rot(0.3),
 'rotate every (k,k+8) pair by pi/4': plane_rot(math.pi / 4),
}
for u in (1, 4, 5, 9, 15): ops['character chi_%d (Hadamard row %d)' % (u, u)] = (lambda uu: (lambda v: chi(uu) * v))(u)
for t in (1, 3, 8): ops['XOR-translate index by %d (unsigned)' % t] = perm_op(lambda i, t=t: i ^ t)
for k in (0, 3, 8, 11): ops['flip sign of e_%d only' % k] = (lambda kk: (lambda v: np.where(np.arange(16) == kk, -v, v)))(k)
for t in (1, 5, 8): ops['left-multiply by e_%d' % t] = Lt(t)
rows = []
print("\nDM-10  operators on the 336 ordered ZD pairs (x,y), xy=0.   fraction with the stated product still zero", flush=True)
print("   %-42s %8s %8s %8s %10s" % ("operator T", "T(x)T(y)", "T(x) y", "x T(y)", "T(y)T(x)"), flush=True)
for name, T_ in ops.items():
    r1 = frac(lambda x, y: nz(mul(T_(x), T_(y))))
    r2 = frac(lambda x, y: nz(mul(T_(x), y)))
    r3 = frac(lambda x, y: nz(mul(x, T_(y))))
    r4 = frac(lambda x, y: nz(mul(T_(y), T_(x))))
    rows.append((name, r1, r2, r3, r4))
    print("   %-42s %8.3f %8.3f %8.3f %10.3f" % (name, r1, r2, r3, r4), flush=True)
R['DM-10'] = rows
# random orthogonal control
vals = []
for _ in range(10):
    Q, _ = np.linalg.qr(rng.normal(size=(16, 16)))
    vals.append(frac(lambda x, y: nz(mul(Q @ x, Q @ y))))
R['DM-10-control'] = dict(random_orthogonal_both=max(vals))
print("   random orthogonal 16x16 (10 draws), best fraction preserved: %.3f" % max(vals), flush=True)

# ---- DM-11 within one assessor plane: rotate a diagonal off the line, defect vs angle ----
print("\nDM-11  ZD defect of x(theta)=cos e_a + sin e_{b+8} against its best partner diagonal (standard algebra):")
a, b = asr[0]
for th in (0, 0.1, 0.5, math.pi / 4 - 0.01, math.pi / 4, math.pi / 4 + 0.01, 1.0, math.pi / 2):
    x = np.zeros(16); x[a] = math.cos(th); x[b + 8] = math.sin(th)
    d = min(np.linalg.norm(mul(x, DV[j])) for j in range(84))
    print("   theta=%.4f  min_y ||x y|| = %.5f" % (th, d), flush=True)

# ---- DM-12 algebra-parameter scan: where do ZDs live when the algebra itself is deformed? ----
def zd_planes(mus):
    T = table(mus); planes = [(a, b + 8) for (a, b) in asr]
    cap, info = [], []
    for p1 in range(42):
        i1, i2 = planes[p1]
        for p2 in range(42):
            j1, j2 = planes[p2]
            M = np.stack([T[i1, j1], T[i1, j2], T[i2, j1], T[i2, j2]], axis=1)       # 16 x 4
            u_, s_, vh = np.linalg.svd(M)
            k = int(np.sum(s_ < 1e-9)) + (4 - len(s_))
            null = vh[4 - k:].conj().T if k else None                                 # 4 x k
            if k == 0: continue
            sols = []
            if k == 1:
                n = null[:, 0]; Dt = n[0] * n[3] - n[1] * n[2]
                if abs(Dt) < 1e-9: sols.append(n)
            elif k == 2:
                N1, N2 = null[:, 0], null[:, 1]
                f = lambda t1, t2: (t1 * N1[0] + t2 * N2[0]) * (t1 * N1[3] + t2 * N2[3]) - (t1 * N1[1] + t2 * N2[1]) * (t1 * N1[2] + t2 * N2[2])
                A = f(1, 0); C = f(0, 1); B = f(1, 1) - A - C
                if abs(A) < 1e-12 and abs(C) < 1e-12 and abs(B) < 1e-12: sols.append(('family', None))
                else:
                    disc = B * B - 4 * A * C
                    if abs(A) > 1e-12:
                        for rt in np.roots([A, B, C]):                                # t1/t2 ratio
                            if abs(np.imag(rt)) < 1e-9 or np.iscomplexobj(mus) or any(np.iscomplex(m) and np.imag(m) != 0 for m in mus):
                                sols.append(rt * N1 + N2)
                    elif abs(B) > 1e-12:
                        sols.append(N2); sols.append(-C / B * N1 + N2 if False else N1)
                    else:
                        sols.append(N1)
            else:
                sols.append(('family', None))
            if sols:
                cap.append((p1, p2)); info.append((k, sols))
    return planes, cap, info
def summarise(mus):
    planes, cap, info = zd_planes(mus)
    deg = np.zeros(42, int)
    for (p1, p2) in cap: deg[p1] += 1
    strut = lambda p: asr[p][0] ^ asr[p][1]
    within = sum(1 for (p1, p2) in cap if strut(p1) == strut(p2))
    nulls = {}
    for k, _ in info: nulls[k] = nulls.get(k, 0) + 1
    kap = set()
    for (p1, p2), (k, sols) in zip(cap, info):
        for s in sols:
            if isinstance(s, tuple): kap.add('family'); continue
            n = s
            if abs(n[0]) > 1e-9:
                kx = n[2] / n[0]
                kap.add(complex(np.round(kx, 4)) if np.iscomplexobj(kx) and abs(np.imag(kx)) > 1e-9 else float(np.round(np.real(kx), 4)))
    return dict(capable_ordered_plane_pairs=len(cap), planes_with_a_partner=int((deg > 0).sum()),
                degree_set=sorted(set(deg.tolist())), within_chart=within, nullity_hist=nulls,
                kappa_x=sorted(kap, key=lambda z: (abs(z) if not isinstance(z, str) else 1e9))[:8])
std = summarise(STD)
R['DM-12-std'] = std
print("\nDM-12  standard sedenions: ", std, flush=True)

phi = (1 + 5 ** 0.5) / 2; W1 = 0.5671432904097838
CONST = [('0', 0.0), ('1', 1.0), ('1/2', 0.5), ('sqrt2', 2 ** 0.5), ('2', 2.0), ('e', math.e), ('pi', math.pi), ('phi', phi),
         ('ln10', math.log(10)), ('Omega_ZS=d*_ln10', W1), ('d*=d*_taut', W1 / math.log(10)), ('d*_spec', 0.24600),
         ('GAP', 1 / (1000 * 2 ** 0.5)), ('i', 1j)]
scan = []
print("\nDM-13  deform ONLY the sedenion doubling  mu4 = +/- c   (mu1..3 = -1).  c from the UNS list", flush=True)
print("   %-18s %5s  %-8s %-9s %-14s %-12s %s" % ("c", "sign", "pairs", "planes", "degrees", "within-chart", "kappa_x (ZD slope in plane)"), flush=True)
for name, c in CONST:
    for sg in ((1,) if name == '0' else (-1, 1)):
        mus = (-1.0, -1.0, -1.0, sg * c)
        if name == 'i' and sg == -1: pass
        sm = summarise(mus)
        scan.append((name, sg, sm))
        print("   %-18s %+5d  %-8d %-9d %-14s %-12d %s" % (name, sg, sm['capable_ordered_plane_pairs'], sm['planes_with_a_partner'],
              sm['degree_set'], sm['within_chart'], sm['kappa_x'][:4]), flush=True)
R['DM-13'] = scan
print("\nDM-14  deform ALL four doubling levels together  mu_k = -c   (k=1..4)", flush=True)
for name, c in CONST:
    mus = (-c, -c, -c, -c)
    sm = summarise(mus); R.setdefault('DM-14', []).append((name, sm))
    print("   %-18s pairs=%-5d planes=%-3d degrees=%s within=%d kappa=%s" % (name, sm['capable_ordered_plane_pairs'], sm['planes_with_a_partner'], sm['degree_set'], sm['within_chart'], sm['kappa_x'][:3]), flush=True)
print("\nDM-15  deform ONE lower level (others standard)", flush=True)
for lvl in (0, 1, 2):
    for val in (0.0, 1.0, 2.0, -2.0):
        mus = [-1.0, -1.0, -1.0, -1.0]; mus[lvl] = val
        sm = summarise(tuple(mus)); R.setdefault('DM-15', []).append((lvl + 1, val, sm))
        print("   mu%d=%+.1f  pairs=%-5d planes=%-3d degrees=%s within=%d" % (lvl + 1, val, sm['capable_ordered_plane_pairs'], sm['planes_with_a_partner'], sm['degree_set'], sm['within_chart']), flush=True)
json.dump(R, open('results_part2.json', 'w'), indent=1, default=str)
