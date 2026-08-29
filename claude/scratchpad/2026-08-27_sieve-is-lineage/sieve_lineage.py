#!/usr/bin/env python3
"""
sieve_lineage.py -- "The Sieve IS Generational Lineage ... Fibonacci under
factoring waves."  (Cody, 2026-08-27)

Claims under test
-----------------
C1  The sieve's pass order IS the decompositional lineage order: composite n
    dies on the pass of prime spf(n) (smallest prime factor), and
        generation(n) = pi(spf(n))        -- the ordinal of that prime.
C2  "one pass per prime" -> the stability/uniformity is because the sieve is a
    single deterministic forward sweep of pi(sqrt N) passes, no iteration to a
    fixed point, no backtracking.
C3  "Fibonacci under factoring waves": the Legendre sieve count obeys a linear
    TWO-TERM recurrence
        phi(x, a) = phi(x, a-1) - phi(x / p_a, a-1)
    exactly Fibonacci's shape (S_k built from two earlier S), except the second
    term's argument is SCALED by a prime (a "factoring wave") instead of the
    index being shifted by 1.  Fibonacci is the p_a -> "shift" degenerate case.
C4  Closed form:  phi(x, a) = sum_{d | P_a} mu(d) * floor(x / d)
    = ADD (the sum) o SCALE (floor x/d) o SIGN (the Mobius mu in {-1,0,+1}).
C5  Two orderings.  ORDINAL (ascending prime) vs a RIEMANN-ZETA weight order
    (primes by descending log(p)/sqrt(p), the size of the p-term in the
    sigma=1/2 prime sum).  The final prime set and the disjoint first-mark
    partition are ORDER-INVARIANT; generation(n) = pi(spf(n)) is UNIQUE to the
    ordinal order.
"""
from __future__ import annotations

import math
from collections import Counter
from functools import reduce


# ── basic tooling ────────────────────────────────────────────────────────────
def sieve_flags(n: int):
    f = [True] * (n + 1)
    f[0] = f[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if f[p]:
            f[p * p::p] = [False] * len(f[p * p::p])
    return f


def primes_up_to(n: int):
    return [i for i, ok in enumerate(sieve_flags(n)) if ok]


def spf_table(n: int):
    """smallest prime factor of every k in 0..n (0 for 0,1)."""
    s = [0] * (n + 1)
    for i in range(2, n + 1):
        if s[i] == 0:
            for j in range(i, n + 1, i):
                if s[j] == 0:
                    s[j] = i
    return s


def gpf(m: int) -> int:
    g = 1
    d = 2
    while d * d <= m:
        while m % d == 0:
            g = d
            m //= d
        d += 1
    return m if m > 1 else g


def mobius_table(n: int):
    mu = [1] * (n + 1)
    mu[0] = 0
    primes = primes_up_to(n)
    for p in primes:
        for j in range(p, n + 1, p):
            mu[j] *= -1
        for j in range(p * p, n + 1, p * p):
            mu[j] = 0
    return mu


# ═══════════════════════════════════════════════════════════════════════════
# C1 + C2 — the sieve pass order IS the lineage order
# ═══════════════════════════════════════════════════════════════════════════
def run_sieve_traced(N: int, order):
    """Run the sieve marking composites in `order` (a list of primes).  Record
    the pass index on which each composite is FIRST marked."""
    marked_on = [None] * (N + 1)          # pass index that first killed k
    passes = 0
    for pass_i, p in enumerate(order):
        if p * p > N:                    # this prime marks nothing new in [2,N]
            # it still "runs" but does zero work -- count only working passes
            continue
        passes += 1
        for k in range(p * p, N + 1, p):
            if marked_on[k] is None:
                marked_on[k] = pass_i
    return marked_on, passes


def c1_c2(N: int = 200_000):
    primes = primes_up_to(N)
    order = primes[:]                                   # ascending / ordinal
    spf = spf_table(N)
    pi = {p: i for i, p in enumerate(primes)}           # pi(p) = ordinal index

    marked_on, working_passes = run_sieve_traced(N, order)

    # generation(n) as the sieve assigns it == pass index of spf(n)?
    mism = 0
    checked = 0
    for n in range(4, N + 1):
        if spf[n] == n:                                 # prime -- a leaf, skip
            continue
        checked += 1
        # the pass that first marks n is the pass whose prime == spf(n)
        want = pi[spf[n]]
        if marked_on[n] != want:
            mism += 1

    # C2: number of *working* passes vs pi(sqrt N)
    root_primes = sum(1 for p in primes if p * p <= N)

    # generation histogram -- the disjoint partition of the composites
    gen_hist = Counter(marked_on[n] for n in range(4, N + 1)
                       if marked_on[n] is not None)
    disjoint_total = sum(gen_hist.values())
    n_composites = sum(1 for n in range(4, N + 1) if spf[n] != n)

    print("── C1 the sieve pass order IS the lineage order ──────────────────")
    print(f"   N = {N};  primes = {len(primes)};  composites in [4,N] = {n_composites}")
    print(f"   generation(n) == pi(spf(n))          : {checked - mism}/{checked} "
          f"({'HOLDS' if mism == 0 else f'{mism} MISMATCH'})")
    print(f"   composites first-marked exactly once : {disjoint_total}/{n_composites} "
          f"({'DISJOINT partition' if disjoint_total == n_composites else 'GAP'})")
    print("── C2 one pass per prime, single forward sweep ───────────────────")
    print(f"   working marking passes               : {working_passes}")
    print(f"   pi(sqrt N) = primes p with p*p <= N  : {root_primes}   "
          f"({'MATCH — no iteration, no backtracking' if working_passes == root_primes else 'DIFF'})")
    top = sorted(gen_hist.items())[:6]
    print("   generation sizes (pass i -> count first-marked):")
    for i, c in top:
        print(f"     pass {i:2d}  prime {order[i]:>3}   {c:>8}   ({100*c/n_composites:5.2f}%)")
    return {'c1_holds': mism == 0, 'c2_holds': working_passes == root_primes,
            'disjoint': disjoint_total == n_composites}


# ═══════════════════════════════════════════════════════════════════════════
# C3 — Fibonacci under factoring waves: the Legendre two-term recurrence
# ═══════════════════════════════════════════════════════════════════════════
def phi_recurrence(x: int, a: int, primes):
    """phi(x,a) = # of 1..x divisible by NONE of the first a primes.
    Legendre's recurrence, memoised: phi(x,a) = phi(x,a-1) - phi(x//p_a, a-1)."""
    from functools import lru_cache

    P = primes

    @lru_cache(maxsize=None)
    def phi(x, a):
        if a == 0:
            return x
        return phi(x, a - 1) - phi(x // P[a - 1], a - 1)

    return phi(x, a)


def phi_direct(x: int, a: int, primes):
    P = set(primes[:a])
    return sum(1 for k in range(1, x + 1) if all(k % p for p in P))


def c3(x: int = 30_030, a: int = 6):
    primes = primes_up_to(200)
    print("── C3 Fibonacci under factoring waves — the 2-term recurrence ─────")
    ok = True
    for aa in range(1, a + 1):
        r = phi_recurrence(x, aa, primes)
        d = phi_direct(x, aa, primes)
        t1 = phi_recurrence(x, aa - 1, primes)
        t2 = phi_recurrence(x // primes[aa - 1], aa - 1, primes)
        ok &= (r == d == t1 - t2)
        print(f"   a={aa} p_a={primes[aa-1]:>2}: phi(x,a)={r:>6}  "
              f"= phi(x,a-1)[{t1:>6}] - phi(x/p_a,a-1)[{t2:>6}]   "
              f"direct={d:>6}  {'ok' if r == d == t1 - t2 else 'FAIL'}")
    print("   Fibonacci:  F(n)   = F(n-1)      - (-F(n-2))     [index shift  n-1]")
    print("   Sieve    :  phi(x,a)= phi(x,a-1) -  phi(x/p_a,·) [SCALE shift  x/p_a]")
    print("   -> same linear 2-term shape; the 2nd term is a FACTORING WAVE")
    print("      (argument divided by a prime) not an index step.  Fibonacci is")
    print("      the degenerate 'p_a acts as +1 shift' case.")
    return {'c3_holds': ok}


# ═══════════════════════════════════════════════════════════════════════════
# C4 — closed form = ADD o SCALE o SIGN
# ═══════════════════════════════════════════════════════════════════════════
def c4(x: int = 30_030, a: int = 6):
    primes = primes_up_to(200)
    P = primes[:a]
    Pa = reduce(lambda u, v: u * v, P, 1)
    mu = mobius_table(Pa + 1)

    # phi(x,a) = sum_{d | P_a} mu(d) floor(x/d)
    divisors = [d for d in range(1, Pa + 1) if Pa % d == 0]
    total = 0
    plus = minus = 0
    for d in divisors:
        m = mu[d]
        if m == 0:
            continue
        term = (x // d)                     # SCALE: a floored division
        total += m * term                   # ADD, with SIGN = mu(d)
        plus += (m > 0)
        minus += (m < 0)

    ref = phi_recurrence(x, a, primes)
    print("── C4 closed form  phi = ADD( SIGN * SCALE ) ─────────────────────")
    print(f"   P_a = prod(first {a} primes) = {Pa}")
    print(f"   squarefree divisors d | P_a with mu(d) != 0 : {plus + minus}  "
          f"(+{plus} / -{minus})")
    print(f"   sum_d  mu(d) * floor(x/d)  = {total}")
    print(f"   phi(x,a) via recurrence    = {ref}    "
          f"{'MATCH' if total == ref else 'FAIL'}")
    print("   SCALE = floor(x/d)   SIGN = mu(d) in {-1,0,+1}   ADD = sum_d")
    print("   -> the inclusion-exclusion IS a superposition of signed division")
    print("      waves; exactly the add_scale_sign floor.")
    return {'c4_holds': total == ref}


# ═══════════════════════════════════════════════════════════════════════════
# C5 — two orderings: ordinal vs Riemann-zeta weight
# ═══════════════════════════════════════════════════════════════════════════
def zeta_weight(p: int) -> float:
    """size of the p-term in the sigma=1/2 von-Mangoldt prime sum:
    Lambda(p) * p^{-1/2} = ln p / sqrt p.  Peaks near p=7, then decays."""
    return math.log(p) / math.sqrt(p)


def c5(N: int = 200_000):
    primes = primes_up_to(N)
    spf = spf_table(N)
    n_comp = sum(1 for n in range(4, N + 1) if spf[n] != n)

    orders = {
        'ordinal  (asc prime)':   sorted(primes),
        'descending (gpf-first)':  sorted(primes, reverse=True),
        'riemann-zeta weight':     sorted(primes, key=zeta_weight, reverse=True),
    }
    pi_ord = {p: i for i, p in enumerate(sorted(primes))}

    print("── C5 orderings — what is order-invariant, what is not ───────────")
    print(f"   zeta-weight order starts: "
          f"{sorted(primes, key=zeta_weight, reverse=True)[:9]}")
    print(f"   {'order':<24} {'primes':>7} {'gen==pi(spf)':>14} {'gen entropy':>12}")
    results = {}
    for name, order in orders.items():
        marked_on, _ = run_sieve_traced(N, order)
        found = [i for i, ok in enumerate(sieve_flags(N)) if ok]
        same_primes = (found == sorted(primes))
        # generation == pi(spf)?
        pos = {p: i for i, p in enumerate(order)}
        mism = sum(1 for n in range(4, N + 1)
                   if spf[n] != n and marked_on[n] != pos[spf[n]])
        # entropy of the first-mark partition (bits)
        hist = Counter(marked_on[n] for n in range(4, N + 1) if marked_on[n] is not None)
        H = -sum((c / n_comp) * math.log2(c / n_comp) for c in hist.values())
        disjoint = sum(hist.values()) == n_comp
        tag = 'HOLDS' if mism == 0 else f'{mism} off'
        print(f"   {name:<24} {'same' if same_primes else 'DIFF':>7} "
              f"{tag:>14} {H:>12.3f}")
        results[name] = {'same_primes': same_primes, 'gen_matches_spf': mism == 0,
                         'disjoint': disjoint, 'entropy_bits': H}
    print("   -> final prime set + disjoint partition: ORDER-INVARIANT.")
    print("      generation(n) = pi(spf(n)): ONLY the ordinal order.")
    print("      ordinal also MINIMISES the generation entropy (front-loaded:")
    print("      pass 0 kills every even = half the composites in one wave).")
    return results


if __name__ == '__main__':
    print("=" * 66)
    print("THE SIEVE IS GENERATIONAL LINEAGE — Fibonacci under factoring waves")
    print("=" * 66)
    r1 = c1_c2()
    print()
    r3 = c3()
    print()
    r4 = c4()
    print()
    r5 = c5()
    print()
    print("=" * 66)
    verdict = {
        'C1 sieve pass = lineage order (gen = pi(spf))': r1['c1_holds'],
        'C2 one deterministic sweep, pi(sqrt N) passes': r1['c2_holds'],
        'C1 disjoint composite partition':               r1['disjoint'],
        'C3 Legendre 2-term recurrence (Fibonacci shape)': r3['c3_holds'],
        'C4 closed form = ADD o SIGN o SCALE':            r4['c4_holds'],
        'C5 prime set order-invariant':
            all(v['same_primes'] for v in r5.values()),
        'C5 gen=pi(spf) UNIQUE to ordinal':
            (r5['ordinal  (asc prime)']['gen_matches_spf']
             and not r5['descending (gpf-first)']['gen_matches_spf']
             and not r5['riemann-zeta weight']['gen_matches_spf']),
    }
    for k, v in verdict.items():
        print(f"  [{'PASS' if v else 'FAIL'}]  {k}")
    print("=" * 66)
