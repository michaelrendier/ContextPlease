#!/usr/bin/env python3
"""Does w >> w* tear the box kite off the zero-divisor surface?
Claim under test (ValaQuenta/wiki/pencil_hyperstring.md, CONJECTURE, test 5):
   w >> w*  =>  chart_of(...).outside_share -> 1 and is_zero_divisor -> False.
Phi_w is NOT implemented anywhere in the repo, so this builds the most literal
reading of the page: Joukowsky  z -> z + c/z,  c = H/q(w),  q = (1/2) rho w^2,
applied to each Assessor vertex z = d+ + i*d-  (the (d+,d-) pair the page names),
then reassembled with the exact inverse of diagonal_amplitudes. H = rho = 1.
Every choice that the page leaves open is marked CHOICE.
"""
import sys, math, itertools
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.box_kite import maths as bk

S2 = math.sqrt(2.0)
def c_of_w(w, H=1.0, rho=1.0):            # CHOICE: H = rho = 1
    return H / (0.5 * rho * w * w)
def jouk(z, c):
    return z + c / z

# ---------- TEST A: the map itself, pure arithmetic ----------
print("A. Joukowsky as written, one vertex z = 0.7+0.4j  (|z|^2 = %.3f)" % abs(0.7+0.4j)**2)
print("   %8s %12s %14s %s" % ("w", "c=H/q(w)", "|z'-z|", "note"))
z = 0.7 + 0.4j
for w in (0.01, 0.1, 1, 2, 3, 10, 100, 1e3, 1e4):
    c = c_of_w(w); zp = jouk(z, c)
    note = ""
    if abs(c - abs(z)**2) / abs(z)**2 < 0.2: note = "<- near c=|z|^2 (flat-plate collapse)"
    print("   %8g %12.5g %14.6g %s" % (w, c, abs(zp - z), note))

# ---------- reassembly (exact inverse of diagonal_amplitudes) ----------
def deform(v, assessors, c):
    out = list(v)
    for (a, b) in assessors:
        dp, dm = bk.diagonal_amplitudes(v, a, b)
        z = complex(dp, dm)
        if abs(z) < 1e-15: continue
        zp = jouk(z, c)
        out[a]     = (zp.real + zp.imag) / S2
        out[b + 8] = (zp.real - zp.imag) / S2
    return out

def report(v):
    r = bk.chart_of(v, check_zd=True)
    return r['is_zero_divisor'], r['outside_share'], r['norm']

# ---------- TEST B: one real zero divisor (a single Assessor diagonal) ----------
kites = bk.box_kites()
s = 1
ass = kites[s]
print("\nB. single zero divisor = diagonal of Assessor", ass[0], "in strut", s)
a, b = ass[0]
for sign, name in ((1, "d+ diagonal"), (-1, "d- diagonal")):
    v0 = bk.basis_vector((1/S2, a), (sign/S2, b + 8))
    print("   start (%s): is_ZD=%s outside=%.3g" % ((name,) + report(v0)[:2]))
    for w in (0.01, 0.3, 1, 3, 30, 1e3):
        z_ = report(deform(v0, ass, c_of_w(w)))
        print("     w=%-6g  is_ZD=%-5s outside_share=%.3g  norm=%.4g" % (w, z_[0], z_[1], z_[2]))
print("   control: a MIXED vector in the same plane (both diagonals occupied)")
v0 = bk.basis_vector((0.8, a), (0.1, b + 8))
print("   start: is_ZD=%s outside=%.3g" % report(v0)[:2])

# ---------- TEST C: the six-vertex kite vector, exhaustive over signs ----------
print("\nC. six-vertex kite vector in strut %d: sum of one diagonal per Assessor," % s)
print("   all 4^6 = 4096 diagonal/sign choices; which are zero divisors at w=baseline?")
base = []
for ch in itertools.product((1, -1, 2, -2), repeat=6):
    v = [0.0] * 16
    for (a_, b_), k in zip(ass, ch):
        sg = 1 if abs(k) == 1 else -1       # which diagonal
        sc = 1 if k > 0 else -1             # overall sign
        v[a_] += sc / S2; v[b_ + 8] += sc * sg / S2
    n = bk.norm(v); v = [x / n for x in v]
    if bk.chart_of(v, check_zd=True)['is_zero_divisor']:
        base.append(v)
print("   baseline zero-divisor kite vectors found: %d of 4096" % len(base))
# structural fact, not a measurement: every candidate uses only indices 1..7 and 9..15
print("   e0/e8 are never populated by any assessor-plane map (indices 0 and 8 belong to no Assessor),")
print("   so outside_share = 0 for every candidate and for every deformation of it, by construction.")
rows = []
for v in base[:8]:
    for w in (0.3, 1, 3, 30, 1e3):
        rows.append((w,) + report(deform(v, ass, c_of_w(w))))
if rows:
    print("   deformed (first up to 8 baseline ZDs), w, is_ZD, outside, norm:")
    seen = {}
    for w, zd, out, nm in rows:
        seen.setdefault(w, []).append((zd, out))
    for w, lst in seen.items():
        print("     w=%-6g  still ZD: %d/%d   max outside_share=%.3g" %
              (w, sum(1 for zd, _ in lst if zd), len(lst), max(o for _, o in lst)))
