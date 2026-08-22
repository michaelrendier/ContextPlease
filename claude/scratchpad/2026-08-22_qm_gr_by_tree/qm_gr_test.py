#!/usr/bin/env python3
"""qm_gr_test.py — does QM live only in one tree and GR only in the other?

Cody, 2026-08-22: "does quantum mechanics exist only in telperion and GR exists
only in Laurelin?" Tested here, not asserted. Every number is computed.

QM proxy  : non-commutativity  [e_i,e_j] ≠ 0        (first at ℍ, dim 4)
GR proxy  : curvature = the associator (ab)c≠a(bc)  (first at 𝕆, dim 8; the
            white paper's §2.5 identifies the associator with curvature)

Trees: the sedenion splits 𝕊 = 𝕆 ⊕ 𝕆. Lower octonion e0..7 (contains e0, the
identity), upper octonion e8..15 (pure imaginary). Reported by CONTENT so the
result is independent of the Telperion/Laurelin naming tangle in the repos.

Run:  python3 qm_gr_test.py   (needs SedenionFactoralRelativity on the path)
"""
import sys, os
sys.path.insert(0, os.path.expanduser('~/Projects/ThePlace/SedenionFactoralRelativity'))
from engine.lineage import cd_mul, unit, nrm

D = 16

def comm(i, j):
    a = cd_mul(unit(D, i), unit(D, j)); b = cd_mul(unit(D, j), unit(D, i))
    return nrm([x - y for x, y in zip(a, b)])

def assoc(i, j, k):
    L = cd_mul(cd_mul(unit(D, i), unit(D, j)), unit(D, k))
    R = cd_mul(unit(D, i), cd_mul(unit(D, j), unit(D, k)))
    return nrm([x - y for x, y in zip(L, R)])

cc = {'BB': [0, 0], 'RR': [0, 0], 'cross': [0, 0]}
for i in range(D):
    for j in range(i + 1, D):
        key = 'BB' if (i < 8 and j < 8) else 'RR' if (i >= 8 and j >= 8) else 'cross'
        cc[key][1] += 1
        if comm(i, j) > 1e-9:
            cc[key][0] += 1
print("QM proxy — NON-COMMUTATIVITY by tree of the pair:")
for k, (nz, tot) in cc.items():
    print(f"   {k:6s}: {nz:4d}/{tot:4d}  ({100*nz/tot:.0f}%)")

ac = {'within-lower': [0, 0], 'within-upper': [0, 0], 'crosses': [0, 0]}
for i in range(D):
    for j in range(D):
        for k in range(D):
            if len({i, j, k}) < 3:
                continue
            reds = sum(x >= 8 for x in (i, j, k))
            key = 'within-lower' if reds == 0 else 'within-upper' if reds == 3 else 'crosses'
            ac[key][1] += 1
            if assoc(i, j, k) > 1e-9:
                ac[key][0] += 1
print("\nGR proxy — CURVATURE = ASSOCIATOR by tree of the triple:")
for k, (nz, tot) in ac.items():
    print(f"   {k:12s}: {nz:5d}/{tot:5d}  ({100*nz/tot:.0f}%)")
tot_nz = sum(v[0] for v in ac.values())
print(f"   -> {100*(ac['within-lower'][0]+ac['within-upper'][0])/tot_nz:.0f}% within a "
      f"single tree, {100*ac['crosses'][0]/tot_nz:.0f}% cross the boundary")
