"""Shared functions for this probe's scripts 04+, pulled out of 01/03
so they're imported once, not copy-pasted."""
from __future__ import annotations
from collections import deque
from typing import Dict, Tuple

_GASKET_SEED = (-1, 2, 2, 3)


def smith_fold(s: complex) -> complex:
    return (s - 1) / (s + 1)


def _descartes_fourth(k1: int, k2: int, k3: int, k4: int) -> int:
    return 2 * (k1 + k2 + k3) - k4


def gasket_addresses(cap: int = 400, seed=_GASKET_SEED) -> Dict[int, Tuple[int, int]]:
    addr: Dict[int, Tuple[int, int]] = {}
    start = tuple(sorted(seed))
    dq = deque([(start, 0, -1)])
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
