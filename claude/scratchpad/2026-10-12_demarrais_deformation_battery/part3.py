#!/usr/bin/env python3
"""PART 3 — are the deformations of the two constructs the same as the maths'?
 scalar construct = the pencil-hyperstring proxy (stations -> product Pi -> H)
 scaled construct = the live 16-vector address (ptol.c projection) read through the box_kite lens, and the kernel's fiber.
Orientation: Assessor = native (d+,d-) pair; anchor e0/e8.  Aperture: continuous phases / generic prompt vectors, never only lattice picks."""
import sys, math, itertools, random, subprocess, json
import numpy as np
from cdalg import *
PTOL = '/home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptol'
asr = bk.assessors()
DV = np.array([diag_vec(a, b, s) for (a, b) in asr for s in (1, -1)])
nz = lambda v, t=1e-9: np.linalg.norm(v) < t
planes = {frozenset((a, b + 8)) for (a, b) in asr}
E = np.eye(16)
HP = math.pi / 2
def gen(a, b, phi): v = np.zeros(16); v[a] = math.cos(phi); v[b] = math.sin(phi); return v
def Pi(r, phis):
    st = bk.pencil(r); p = gen(*st[0], phis[0])
    for k in range(1, 7): p = mul(p, gen(*st[k], phis[k]))
    return p
def ptol(prompt):
    out = subprocess.run([PTOL, '-r', prompt], capture_output=True, text=True).stdout.split('\n')
    v, i = [], 0
    while out[i].strip() != '---': v.append(float(out[i])); i += 1
    g = [float(l.split(':')[1]) for l in out if l.startswith('gamma:')][0]
    return np.array(v[:16]), g
random.seed(4)

print("=== SCALAR CONSTRUCT (pencil hyperstring proxy) vs the maths ===", flush=True)
print("\nCS-01  are the stations Assessor planes?  (De Marrais Assessor planes of strut s have index XOR s+8)")
print("   stations of pencil(r) that are Assessor planes:  r=1..8: 0 of 7 ; r=9..15 (= strut s+8): 6 of 7 (+ the plane {s,e8})")
print("   => the paper's pencil(strut r<=7) never sits in the Assessor planes; pencil(s+8) does, and its H depends on 4-5 phase combinations for s=2..7 (rank 1 only for s=1)")

print("\nCS-02  is the product Pi(phi) ever a zero divisor?  (chart_of exact test; 12 phase vectors + the Noether path per pencil)")
for r in (1, 4, 9, 10, 12, 15):
    hits = 0; n = 0; best = 9.0
    pts = [[t * HP * (k + 1) / 7 for k in range(7)] for t in np.linspace(0, 1, 7)] + [[random.uniform(0, HP) for _ in range(7)] for _ in range(6)]
    for ph in pts:
        p = Pi(r, ph); n += 1
        zd = bk.chart_of(list(p), check_zd=True)['is_zero_divisor']
        hits += bool(zd)
        best = min(best, min(np.linalg.norm(mul(p, d)) / np.linalg.norm(d) for d in DV) / max(np.linalg.norm(p), 1e-12))
    print("   pencil(%2d): zero divisor at %d of %d points ; smallest ||Pi d||/(|Pi||d|) against the 84 diagonals = %.4f" % (r, hits, n, best), flush=True)

print("\nCS-03  the construct's deformation at an Assessor-plane station:  rotate d+ -> d-  (phi: pi/4 -> pi/4+delta)")
print("   first-order tear rate of a diagonal x(phi) against its best partner (DM-11):  |d||x y|/d phi| at pi/4")
a, b = asr[0]
for dlt in (1e-4, 1e-3):
    x = np.zeros(16); x[a] = math.cos(math.pi / 4 + dlt); x[b + 8] = math.sin(math.pi / 4 + dlt)
    d0 = min(np.linalg.norm(mul(x, DV[j])) for j in range(84))
    print("   delta=%g : defect %.6f  -> rate %.4f per radian   (exactly 2: the station flow is TRANSVERSAL to the zero-divisor set)" % (dlt, d0, d0 / dlt))

print("\nCS-04  functions of the pair z = d+ + i d-  applied to a diagonal x:  does the image stay a zero divisor (annihilate one of the 84 diagonals)?")
def apply_f(x, a, b, f):
    dp, dm = bk.diagonal_amplitudes(list(x), a, b); z = complex(dp, dm); w = f(z)
    y = x.copy(); y[a] = (w.real + w.imag) / math.sqrt(2); y[b + 8] = (w.real - w.imag) / math.sqrt(2); return y
import cmath
W1 = 0.5671432904097838
funcs = [
 ('identity', lambda z: z),
 ('scale by 2.5', lambda z: 2.5 * z),
 ('Joukowsky z + c/z, c=Omega_ZS', lambda z: z + W1 / z),
 ('Joukowsky z + c/z, c=0.3', lambda z: z + 0.3 / z),
 ('Moebius (z-z0)/(z+z0), z0=1 (Smith fold)', lambda z: (z - 1) / (z + 1)),
 ('exp(z)', lambda z: cmath.exp(z)),
 ('z^2', lambda z: z * z),
 ('tanh(z/2)', lambda z: cmath.tanh(z / 2)),
 ('rotate z by 0.3 rad (in-plane)', lambda z: z * cmath.exp(0.3j)),
 ('rotate z by pi/2 (swap d+ -> d-)', lambda z: z * 1j),
 ('complex conjugate (d- -> -d-)', lambda z: z.conjugate()),
 ('1/z (inversion)', lambda z: 1 / z),
]
print("   %-44s %-28s %-28s" % ("f", "x = d+ diagonal (z real)", "x = d- diagonal (z imaginary)"))
for name, f in funcs:
    res = []
    for sgn in (1, -1):
        keep = 0; tot = 0
        for (aa, bb) in asr[:42:3]:
            x = diag_vec(aa, bb, sgn) / math.sqrt(2)
            if np.linalg.norm(x) == 0: continue
            try: y = apply_f(x, aa, bb, f)
            except ZeroDivisionError: continue
            d0 = min(np.linalg.norm(mul(y, DV[j])) for j in range(84)) / max(np.linalg.norm(y), 1e-12)
            tot += 1; keep += d0 < 1e-9
        res.append("%d/%d stay zero divisors" % (keep, tot))
    print("   %-44s %-28s %-28s" % ((name,) + tuple(res)), flush=True)

print("\n=== SCALED CONSTRUCT (live address) vs the maths ===", flush=True)
prompts = ["neutron generation", "pressurized water reactor", "the cat sat on the mat", "neutron"]
V = {p: ptol(p) for p in prompts}
print("\nSC-01  ptol.c's Gamma = a Walsh coefficient of the energy distribution?   chi_4(k) = (-1)^(bit2 of k)  == the J_red/J_blue partition")
H16 = np.array([[(-1) ** bin(i & j).count('1') for j in range(16)] for i in range(16)], float)
for p, (v, g) in V.items():
    en = v * v; W = H16 @ en / en.sum()
    print("   %-28s Gamma(ptol)=%+.10f   W_4=sum chi_4 v^2/|v|^2=%+.10f   |diff|=%.1e   other W_u: %s" % (
          p, g, W[4], abs(g - W[4]), np.round(np.delete(W, [0, 4]), 3)[:6].tolist()), flush=True)

print("\nSC-02  covariance of the lens readings under the maths' symmetry group  (apply the signed monomial automorphism T to the address)")
# rebuild the 168 frame-preserving A in GL(4,2) (columns as bitmasks)
def mat_apply(A, i):
    r = 0
    for bb in range(4):
        if (i >> bb) & 1: r ^= A[bb]
    return r
good = []
for cols in itertools.product(range(1, 16), repeat=4):
    span = {0}; ok = True
    for c in cols:
        if c in span: ok = False; break
        span |= {s ^ c for s in span}
    if not ok: continue
    if mat_apply(cols, 8) != 8: continue
    # frame-preserving iff maps every assessor plane to an assessor plane
    if {frozenset((mat_apply(cols, aa), mat_apply(cols, bb + 8))) for (aa, bb) in asr} == planes: good.append(cols)
print("   frame-preserving index maps found (fixing e8): %d  (expected 168 = |GL(3,2)|; signs lift in 16 ways each)" % len(good), flush=True)
def permute(v, A): w = np.zeros(16); 
def apply_perm(v, A):
    w = np.zeros(16)
    for i in range(16): w[mat_apply(A, i)] = v[i]
    return w
strut_of = lambda aa, bb: aa ^ bb
for p, (v, g) in V.items():
    r0 = bk.chart_of(list(v), check_zd=False)
    ok_curv = ok_out = ok_fpw = ok_chart = 0
    for A in good:
        w = apply_perm(v, A)
        r1 = bk.chart_of(list(w), check_zd=False)
        ok_curv += abs(r1['local_curvature'] - r0['local_curvature']) < 1e-9
        ok_out += abs(r1['outside_share'] - r0['outside_share']) < 1e-12
        ok_fpw += abs(r1['fixed_point_weight'] - r0['fixed_point_weight']) < 1e-12
        # chart energies should permute: strut s -> A3(s) where A3 acts on indices 1..7
        perm = {s: mat_apply(A, s) for s in range(1, 8)}
        ok_chart += all(abs(r1['chart_energy'][perm[s]] - r0['chart_energy'][s]) < 1e-9 for s in range(1, 8))
    print("   %-28s over %d automorphic maps: local_curvature invariant %d, outside_share %d, fixed_point_weight %d, chart_energy permutes by s->A(s): %d" % (
          p, len(good), ok_curv, ok_out, ok_fpw, ok_chart), flush=True)
print("   control: 300 RANDOM index permutations of the 16 slots (not automorphisms):")
for p, (v, g) in list(V.items())[:2]:
    r0 = bk.chart_of(list(v), check_zd=False); inv = 0
    for _ in range(300):
        pr = list(range(16)); random.shuffle(pr); w = np.zeros(16)
        for i in range(16): w[pr[i]] = v[i]
        r1 = bk.chart_of(list(w), check_zd=False)
        inv += abs(r1['local_curvature'] - r0['local_curvature']) < 1e-9 and abs(r1['outside_share'] - r0['outside_share']) < 1e-12
    print("   %-28s curvature AND outside_share both unchanged in %d / 300" % (p, inv), flush=True)

print("\nSC-03  the kernel's fiber (scaled_mind_eye_boxkite_kernel_monad.throw_fiber):  psi = sqrt(1-d^2) e0 + d/sqrt2 (e_a + e_b), (a,b)=first Assessor of the strut")
print("   as written (indices a and b directly)  vs  the Assessor plane (a, b+8)")
for strut in (1, 2, 5):
    a, b = bk.box_kites()[strut][0]
    for depth in (0.6, 1.0):
        for lab, i2 in (("as written e_a+e_b", b), ("Assessor e_a+e_(b+8)", b + 8)):
            psi = np.zeros(16); psi[0] = math.sqrt(max(0, 1 - depth ** 2)); psi[a] = depth / math.sqrt(2); psi[i2] = depth / math.sqrt(2)
            r = bk.chart_of(list(psi), check_zd=True)
            print("   strut %d depth %.1f  %-22s dominant chart=%s (intended %d)  nearest assessor=%s  is_zero_divisor=%s" % (
                  strut, depth, lab, r['dominant_chart'], strut, r['nearest_assessor'], r['is_zero_divisor']), flush=True)
