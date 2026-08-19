#!/usr/bin/env python3
"""
THE PARITY LAW, computed from the ALGEBRA instead of by SVD.

The SVD route is O(d^3) per candidate and floating point. At dim 256 that is
~45 minutes and a tolerance you have to guess. This is O(d) per candidate and
EXACT INTEGER ARITHMETIC -- no tolerance at all.

THE REDUCTION
-------------
P_i = left multiplication by e_i. Because e_i . e_j = +/- e_k, every P_i is a
SIGNED PERMUTATION MATRIX -- one nonzero per row and column. So for
a = (e_i + s.e_j)/sqrt(2):

    L_a = (P_i + s P_j)/sqrt(2)
    ker(L_a) = ker(P_i + s P_j) = ker(P_i (I + s Q)),   Q = P_i^-1 P_j

P_i is invertible, so nullity(L_a) = multiplicity of eigenvalue (-s) in Q.
And Q is itself a signed permutation matrix, whose spectrum is fixed entirely
by its CYCLE STRUCTURE: a cycle of length L with sign product sigma carries
exactly the L-th roots of sigma.

    eigenvalue (-s) appears once per cycle with  (-s)^L == sigma

    s = +1  ->  count cycles with (-1)^L == sigma
    s = -1  ->  count cycles with sigma == +1

So the whole question is a cycle walk. No matrices are ever built.

Verified against the SVD census at dim 32, 64 and 128 before being trusted.
"""
import sys, time, json
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.box_kite.maths import cd_multiplication_table


def signed_perms(tab, dim):
    """P_i as (perm, sign): e_i . e_j = sign[i][j] * e_(perm[i][j])."""
    perm = [[0] * dim for _ in range(dim)]
    sign = [[0] * dim for _ in range(dim)]
    for i in range(dim):
        pi, si = perm[i], sign[i]
        for j in range(dim):
            s, k = tab[(i, j)]          # box_kite returns (SIGN, INDEX)
            pi[j], si[j] = k, s
    return perm, sign


def nullity(perm, sign, inv, i, j, s, dim):
    """Multiplicity of eigenvalue (-s) in Q = P_i^-1 P_j, by cycle walk."""
    pi, si, pj, sj, ii = perm[i], sign[i], perm[j], sign[j], inv[i]
    seen = bytearray(dim)
    n = 0
    for start in range(dim):
        if seen[start]:
            continue
        # walk the cycle of b -> ii[pj[b]], accumulating the sign product
        L, sigma, b = 0, 1, start
        while not seen[b]:
            seen[b] = 1
            a = ii[pj[b]]
            sigma *= si[a] * sj[b]
            b = a
            L += 1
        # eigenvalue (-s) present on this cycle iff (-s)^L == sigma
        if ((-1) ** L if s > 0 else 1) == sigma:
            n += 1
    return n


def census(level, verbose=True):
    t0 = time.time()
    tab, dim = cd_multiplication_table(level)
    H = dim // 2
    perm, sign = signed_perms(tab, dim)
    inv = [[0] * dim for _ in range(dim)]
    for i in range(dim):
        pi, ii = perm[i], inv[i]
        for j in range(dim):
            ii[pi[j]] = j

    rows = []
    for i in range(dim):
        for j in range(i + 1, dim):
            for s in (1, -1):
                n = nullity(perm, sign, inv, i, j, s, dim)
                if n:
                    loc = 'lower' if j < H else ('upper' if i >= H else 'cross')
                    rows.append((i, j, s, n, loc))
    if verbose:
        print(f"  dim {dim:>5}: {len(rows):>7} zero divisors   ({time.time()-t0:.1f}s)")
    return dim, rows


def report(dim, rows):
    nc = sorted({n for *_, n, l in rows if l in ('lower', 'upper')})
    cr = sorted({n for *_, n, l in rows if l == 'cross'})
    nc_ok = all(n % 4 == 0 and (n // 4) % 2 == 0 for n in nc)
    cr_ok = all(n % 4 == 0 and (n // 4) % 2 == 1 for n in cr)
    dis = set(nc).isdisjoint(cr)
    cnt = {l: sum(1 for *_, x in rows if x == l) for l in ('lower', 'cross', 'upper')}
    orph = sorted(set(range(dim)) - ({r[0] for r in rows} | {r[1] for r in rows}))
    holds = nc_ok and cr_ok and dis
    print(f"    census        {cnt}  total {len(rows)}")
    print(f"    orphans       {orph}")
    print(f"    non-crossing  /4 = {[n//4 for n in nc]}")
    print(f"    crossing      /4 = {[n//4 for n in cr]}")
    print(f"    max nullity   {max(nc+cr)}   (d/2 - 4 = {dim//2 - 4})")
    print(f"    PARITY LAW HOLDS   {holds}   (even/odd ok: {nc_ok}/{cr_ok}, disjoint: {dis})")
    return {'dim': dim, 'total': len(rows), 'counts': cnt, 'orphans': orph,
            'non_crossing': nc, 'crossing': cr, 'holds': bool(holds),
            'max_nullity': max(nc + cr)}


if __name__ == '__main__':
    levels = [int(x) for x in sys.argv[1:]] or [5, 6, 7, 8]
    out = []
    print("=" * 74)
    print("PARITY LAW — cycle-walk method (exact integers, no SVD, no tolerance)")
    print("=" * 74)
    for lv in levels:
        dim, rows = census(lv)
        out.append(report(dim, rows))
        print()
    print("=" * 74)
    for o in out:
        print(f"  dim {o['dim']:>5}   ZD {o['total']:>8}   orphans {o['orphans']}   "
              f"parity holds = {o['holds']}")
    json.dump(out, open('/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/'
                        '2026-08-15_zd_asymptote/parity_fast.json', 'w'), indent=2)
