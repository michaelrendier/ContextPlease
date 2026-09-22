"""
03_gasket_generation_address.py

Replaces scale.py's 1-D "nearest curvature by magnitude" discrete reading
with the genuine 2-D combinatorial address a point in a Kleinian limit set
actually has: (generation depth, which of the four Descartes moves got you
there) -- a real word in the group's generators, not just a rank.

This is the "proper coordinates" for the discrete side the way complex
s=sigma+i.t is the proper coordinate for the continuous side (01).
"""
from __future__ import annotations
from collections import deque
from typing import Dict, Tuple

_GASKET_SEED = (-1, 2, 2, 3)


def _descartes_fourth(k1: int, k2: int, k3: int, k4: int) -> int:
    return 2 * (k1 + k2 + k3) - k4


def gasket_addresses(cap: int = 400, seed=_GASKET_SEED) -> Dict[int, Tuple[int, int]]:
    """curvature -> (generation, move_index) where move_index in 0..3 is
    WHICH of the quadruple's four members was replaced to produce it --
    the genuine branch label, not just 'how far out'. First occurrence
    wins (BFS), same discipline as scale.py's apollonian_curvatures()."""
    addr: Dict[int, Tuple[int, int]] = {}
    start = tuple(sorted(seed))
    dq = deque([(start, 0, -1)])   # (quad, generation, move_index_that_produced_it)
    seen = {start}
    for k in start:
        if k not in addr:
            addr[k] = (0, -1)
    while dq:
        quad, gen, _ = dq.popleft()
        a, b, c, d = quad
        moves = ((a, b, c, d), (a, b, d, c), (a, c, d, b), (b, c, d, a))
        for move_idx, (x, y, z, w) in enumerate(moves):
            nw = _descartes_fourth(x, y, z, w)
            if abs(nw) > cap:
                continue
            if nw not in addr or gen + 1 < addr[nw][0]:
                addr[nw] = (gen + 1, move_idx)
            nq = tuple(sorted((x, y, z, nw)))
            if nq not in seen:
                seen.add(nq)
                dq.append((nq, gen + 1, move_idx))
    return addr


if __name__ == "__main__":
    addr = gasket_addresses(60)
    print(f"{'curvature':>10}{'generation':>12}{'move_index':>12}")
    for k in sorted(addr):
        if k > 0:
            gen, mv = addr[k]
            print(f"{k:>10}{gen:>12}{mv:>12}")
    print(f"\n{len(addr)} curvatures addressed up to cap=60, each with a real")
    print("(generation, move_index) pair -- a genuine 2-coordinate discrete")
    print("address, not a 1-D rank by magnitude.")
