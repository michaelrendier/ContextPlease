"""
The three-way addition-matrix sudoku, as an actual digit-DP constraint-
propagation search recovering p, q (both unknown) from N = p*q.

State at column c: (p_digits_so_far, q_digits_so_far, carry_in). At each
column, every candidate NEW digit pair (p_c, q_c) is tried; a candidate
survives only if the full convolution sum at that column (using ALL
already-fixed digits plus the new pair) matches N's actual digit there,
mod 10, with the correct carry propagating forward.

This is real pruning (verified below, not asserted) -- NOT a claim of
polynomial-time factoring. Worst-case branching is still real; this is
the honest, checked structure of what the pruning actually buys you.
"""
from __future__ import annotations
from typing import List, Tuple


def digits_lsb(n: int, width: int) -> List[int]:
    out = []
    for _ in range(width):
        out.append(n % 10)
        n //= 10
    return out


def factor_search(N: int, n_digits: int, verbose: bool = True):
    n_cols = 2 * n_digits
    target = digits_lsb(N, n_cols)

    # states: (p_digits list, q_digits list, carry)
    states: List[Tuple[List[int], List[int], int]] = [([], [], 0)]
    history = []

    for c in range(n_cols):
        new_states = []
        for p_digits, q_digits, carry in states:
            if c < n_digits:
                candidates = range(10)
            else:
                candidates = (0,)  # no more real digits beyond n_digits -- must be 0
            for new_p in candidates:
                for new_q in candidates:
                    trial_p = p_digits + [new_p] if c < n_digits else p_digits
                    trial_q = q_digits + [new_q] if c < n_digits else q_digits
                    s = carry
                    for i in range(len(trial_p)):
                        j = c - i
                        if 0 <= j < len(trial_q):
                            s += trial_p[i] * trial_q[j]
                    if s % 10 == target[c]:
                        new_states.append((trial_p, trial_q, s // 10))
        history.append((c, len(states), len(new_states)))
        if verbose:
            print(f"  column {c:2}: {len(states):5} live states -> "
                  f"{len(new_states):5} survive (target digit={target[c]})")
        states = new_states

    # final filter: carry must be exactly 0 (no leftover overflow)
    final = [(p, q) for p, q, carry in states if carry == 0]
    return final, history


def digits_to_int(digits: List[int]) -> int:
    return sum(d * (10 ** i) for i, d in enumerate(digits))


if __name__ == "__main__":
    N = 61 * 53  # = 3233
    print(f"Factoring N={N} via 2-way digit-DP search (n_digits=2 per factor)\n")
    final, history = factor_search(N, n_digits=2)

    print(f"\n{len(final)} surviving (p,q) digit-sequences with carry=0:")
    seen = set()
    for p_digits, q_digits in final:
        p, q = digits_to_int(p_digits), digits_to_int(q_digits)
        if p * q == N and p > 1 and q > 1:
            key = tuple(sorted((p, q)))
            if key not in seen:
                seen.add(key)
                print(f"  p={p}, q={q}  (p*q={p*q}, verified={p*q==N})")

    print("\nBranching factor per column (live states before -> after this column's filter):")
    for c, before, after in history:
        ratio = after / before if before else 0
        print(f"  col {c}: {before:5} -> {after:5}  (survival ratio {ratio:.3f}, "
              f"vs 100 blind candidates per state)")
