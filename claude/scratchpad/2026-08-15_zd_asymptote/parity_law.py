#!/usr/bin/env python3
"""
THE ZERO-DIVISOR PARITY LAW — the P6 test.

Derived (post hoc) from dim 32 and 64 in FourthAgePapers/BoundaryLever:

    NON-CROSSING zero divisor  <->  nullity an EVEN multiple of 4
    BOUNDARY-CROSSING          <->  nullity an ODD  multiple of 4

dim 128 was never parity-checked (the P1 run read only the orphan list).
dim 256 is the pre-registered P6 level.

Both are genuine tests: the law was fitted on 32 and 64 only.

Batched SVD — numpy takes a stacked (N, d, d) array, which removes the Python
per-matrix overhead. Chunked so memory stays bounded.
"""
import sys, math, time, json
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
import numpy as np
from ValaQuenta.modules.box_kite.maths import cd_multiplication_table

CHUNK = 400


def basis_ops(tab, dim):
    P = np.zeros((dim, dim, dim))
    for i in range(dim):
        for j in range(dim):
            s, k = tab[(i, j)]          # (SIGN, INDEX)
            P[i, k, j] = s
    return P


def parity_census(level, tol=1e-9, verbose=True):
    t0 = time.time()
    tab, dim = cd_multiplication_table(level)
    H = dim // 2
    P = basis_ops(tab, dim)
    r = 1 / math.sqrt(2)

    cands = [(i, j, sg)
             for i in range(dim) for j in range(i + 1, dim) for sg in (1.0, -1.0)]
    if verbose:
        print(f"  dim {dim}: {len(cands)} candidate diagonals, batched by {CHUNK}")

    rows = []
    for c0 in range(0, len(cands), CHUNK):
        block = cands[c0:c0 + CHUNK]
        M = np.empty((len(block), dim, dim))
        for n, (i, j, sg) in enumerate(block):
            M[n] = (P[i] + sg * P[j]) * r
        S = np.linalg.svd(M, compute_uv=False)          # (N, dim)
        nul = (S < tol).sum(axis=1)
        for n, (i, j, sg) in enumerate(block):
            if nul[n]:
                loc = 'lower' if j < H else ('upper' if i >= H else 'cross')
                rows.append((i, j, int(sg), int(nul[n]), loc))
        if verbose and (c0 // CHUNK) % 25 == 0:
            print(f"    {c0 + len(block)}/{len(cands)}  ({time.time()-t0:.0f}s)")

    if verbose:
        print(f"  done in {time.time()-t0:.0f}s — {len(rows)} zero divisors")
    return dim, H, rows


def report(dim, rows):
    nc = sorted({n for _, _, _, n, l in rows if l in ('lower', 'upper')})
    cr = sorted({n for _, _, _, n, l in rows if l == 'cross'})
    nc_ok = all(n % 4 == 0 and (n // 4) % 2 == 0 for n in nc)
    cr_ok = all(n % 4 == 0 and (n // 4) % 2 == 1 for n in cr)
    disjoint = set(nc).isdisjoint(set(cr))
    counts = {l: sum(1 for _, _, _, _, x in rows if x == l)
              for l in ('lower', 'cross', 'upper')}
    print()
    print(f"  dim {dim}")
    print(f"    census                 {counts}  total {len(rows)}")
    print(f"    non-crossing nullity   {nc}")
    print(f"                     /4 =  {[n // 4 for n in nc]}   all EVEN: {nc_ok}")
    print(f"    crossing nullity       {cr}")
    print(f"                     /4 =  {[n // 4 for n in cr]}   all ODD : {cr_ok}")
    print(f"    classes disjoint       {disjoint}")
    verdict = nc_ok and cr_ok and disjoint
    print(f"    PARITY LAW HOLDS       {verdict}")
    return {'dim': dim, 'non_crossing': nc, 'crossing': cr, 'counts': counts,
            'total': len(rows), 'holds': bool(verdict)}


if __name__ == '__main__':
    levels = [int(x) for x in sys.argv[1:]] or [5, 6, 7]
    out = []
    print("=" * 74)
    print("THE ZERO-DIVISOR PARITY LAW")
    print("=" * 74)
    for lv in levels:
        dim, H, rows = parity_census(lv)
        out.append(report(dim, rows))
    print()
    print("=" * 74)
    for o in out:
        tag = 'fitted on this level' if o['dim'] in (32, 64) else 'GENUINE TEST'
        print(f"  dim {o['dim']:>4}   holds={o['holds']}   ({tag})")
    json.dump(out, open(f'/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/'
                        f'2026-08-15_zd_asymptote/parity_{"_".join(map(str,levels))}.json', 'w'),
              indent=2)
