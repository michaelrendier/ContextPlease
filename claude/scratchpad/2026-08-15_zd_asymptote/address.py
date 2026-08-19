#!/usr/bin/env python3
"""
A COMPLETE ADDRESS FOR EVERY ZERO DIVISOR IN THE CAYLEY-DICKSON TOWER.

Cody, 2026-08-15: "we need an addressing system...im running down every street
i'm finding..."

The lineage recursion already IS the address; it was never made constructive:

    total(2d) = 2*total(d)  +  2(d-1)(d-2)
                \________/     \__________/
                 recurse to      address HERE
                 a parent

So an address is a PATH DOWN THE TOWER -- which line at each generation, until
you reach the generation where the coupling was actually formed:

    address := L <address>          in the lower copy of the parent
             | U <address>          in the upper copy of the parent
             | X(strut, i, sign)    formed HERE, crossing the boundary

Read it like a file path. `U.L.X(3,5,+)` means: go to the upper half, then its
lower half, and there you are a crossing diagonal in chart 3, leg 5, sign +.

WHY IT IS COMPLETE. At a level of dimension D with H = D/2, a crossing diagonal
is (e_i +/- e_(j+H)) with i, j in 1..H-1 and i != j. Its chart is
strut = i XOR j, and given the strut, j = i XOR strut. So (strut, i, sign)
determines it exactly, and there are (H-1)(H-2)*2 of them -- the lineage
recursion's second term, to the unit.
"""
import sys, math
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.box_kite.maths import cd_multiplication_table


def encode(i, j, sign, dim):
    """(i, j, sign) at dimension `dim`  ->  address string. i < j."""
    parts = []
    while True:
        H = dim // 2
        if j < H:                       # both legs in the lower copy
            parts.append('L'); dim = H
        elif i >= H:                    # both legs in the upper copy
            parts.append('U'); i -= H; j -= H; dim = H
        else:                           # crosses the boundary HERE
            b = j - H
            parts.append(f"X({i ^ b},{i},{'+' if sign > 0 else '-'})")
            return '.'.join(parts)


def decode(addr, dim):
    """address string at dimension `dim`  ->  (i, j, sign)."""
    toks = addr.split('.')
    offs, dims = [], []
    for t in toks[:-1]:
        H = dim // 2
        offs.append(0 if t == 'L' else H)
        dims.append(dim); dim = H
    strut, i, sg = toks[-1][2:-1].split(',')
    strut, i = int(strut), int(i)
    j = (i ^ strut) + dim // 2
    sign = 1 if sg == '+' else -1
    for off in reversed(offs):
        i += off; j += off
    return i, j, sign


def all_zd(level):
    """Every zero-divisor diagonal at this level, by the cycle walk."""
    tab, dim = cd_multiplication_table(level)
    perm = [[0]*dim for _ in range(dim)]; sign = [[0]*dim for _ in range(dim)]
    for a in range(dim):
        for b in range(dim):
            s, k = tab[(a, b)]; perm[a][b], sign[a][b] = k, s
    inv = [[0]*dim for _ in range(dim)]
    for a in range(dim):
        for b in range(dim): inv[a][perm[a][b]] = b
    out = []
    for i in range(dim):
        for j in range(i+1, dim):
            for s in (1, -1):
                seen = bytearray(dim); n = 0
                for st in range(dim):
                    if seen[st]: continue
                    L = 0; sg = 1; b = st
                    while not seen[b]:
                        seen[b] = 1; a = inv[i][perm[j][b]]
                        sg *= sign[i][a] * sign[j][b]; b = a; L += 1
                    if ((-1)**L if s > 0 else 1) == sg: n += 1
                if n: out.append((i, j, s))
    return dim, out


if __name__ == '__main__':
    print("=" * 74)
    print("ROUND-TRIP TEST — every zero divisor, every level")
    print("=" * 74)
    print(f"  {'dim':>5} {'ZD diagonals':>13} {'addresses':>10} {'unique':>8} "
          f"{'round-trip':>11}")
    for lv in (4, 5, 6):
        dim, zds = all_zd(lv)
        addrs = [encode(i, j, s, dim) for i, j, s in zds]
        back = [decode(a, dim) for a in addrs]
        print(f"  {dim:>5} {len(zds):>13} {len(addrs):>10} "
              f"{len(set(addrs)) == len(addrs)!s:>8} {back == zds!s:>11}")

    print("\n" + "=" * 74)
    print("WHAT AN ADDRESS LOOKS LIKE")
    print("=" * 74)
    dim, zds = all_zd(5)
    seen = {}
    for i, j, s in zds:
        a = encode(i, j, s, dim)
        seen.setdefault(a.count('.'), []).append((a, i, j, s))
    for depth in sorted(seen):
        a, i, j, s = seen[depth][0]
        n = len(seen[depth])
        print(f"  depth {depth}: {a:<22} = (e{i} {'+' if s>0 else '-'} e{j})/sqrt2"
              f"   [{n} diagonals at this depth]")
    print(f"""
  Depth is GENERATION. Depth 0 means the coupling was formed at this level --
  it crosses the boundary here. Depth 1 means it was inherited from the parent
  and crosses one level down. The address says WHEN a zero divisor was born
  and WHICH LINE it descended through.

  Counts by depth reproduce the lineage recursion exactly:
      2(d-1)(d-2) born here, and 2x the parent's whole census inherited.
""")
    print("=" * 74)
    print("THE ADDRESS IS THE ORIENTATION FRAME, MADE UNIQUE")
    print("=" * 74)
    print("""  Earlier the frame (nullity, location, strut) carved dim 32 into 24 cells
  holding 588 objects -- 24.5 per cell, a coarse address. The path form
  closes it:

      X(strut, i, sign)  is unique WITHIN a level
      L / U prefix       says which inherited line
      depth              says which generation

  and (H-1)(H-2)*2 crossing addresses per level is exactly the recursion's
  second term. Nothing is unaddressed and nothing is addressed twice.
""")
