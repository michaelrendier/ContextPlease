"""The law in plain view, and whether the final answer has an address in the orbit-of-orbits (exact; stdlib only)."""
import sys, io, contextlib, random, statistics as st
from math import gcd
sys.path.insert(0, '/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/2026-09-26_addition_matrix_sudoku')
import factor_search as fs
def phi10(k): return 4 * 10 ** (k - 1)
def v(N, p):
    c = 0
    while N % p == 0: N //= p; c += 1
    return c
def brute(N, k):
    M = 10 ** k; return sum(1 for a in range(M) for b in range(M) if (a * b - N) % M == 0)
print("1. live states after column c  vs  #{(p,q) mod 10^(c+1): pq = N mod 10^(c+1)}  vs  (v2(N)+1)(v5(N)+1) phi(10^(c+1))")
for N, n in ((3233, 2), (14351, 3), (420, 2), (850, 2), (5100, 2), (1022117, 4)):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): res = fs.factor_search(N, n, verbose=False)
    hist = res[-1] if isinstance(res, tuple) and isinstance(res[-1], list) else None
    # recompute survivor counts directly from the search function's own history if exposed, else re-run a copy
    import re
    out = io.StringIO()
    with contextlib.redirect_stdout(out): fs.factor_search(N, n, verbose=True)
    surv = [int(m) for m in re.findall(r'(\d+) survive', out.getvalue())]
    row = []
    for c in range(min(n, 3)):
        k = c + 1; b = brute(N, k) if k <= 3 else None
        cf = (v(N, 2) + 1) * (v(N, 5) + 1) * phi10(k) if v(N, 2) < k and v(N, 5) < k else None
        row.append((c, surv[c], b, cf))
    print(f"   N={N} (v2={v(N,2)}, v5={v(N,5)}), n={n}: (column, search survivors, brute count mod 10^(c+1), closed form when v<c+1)", row)
print("\n2. the answer's address: every solution p' mod 10^n gives q' = N/p' mod 10^n and an overflow K = (p'q' - N)/10^n; the true factorisation is exactly K = 0")
rng = random.Random(3)
def primes(lo, hi): return [x for x in range(lo, hi) if all(x % d for d in range(2, int(x ** .5) + 1))]
P3 = primes(101, 999)
rows = []
for _ in range(60):
    p, q = rng.sample(P3, 2); N = p * q; n = 3; M = 10 ** n
    Ks = []
    for pp in range(1, M):
        if gcd(pp, 10) != 1: continue
        qq = (N * pow(pp, -1, M)) % M
        Ks.append((pp * qq - N) // M)
    nz = sorted(abs(k) for k in Ks if k != 0)
    rows.append((len(Ks), Ks.count(0), nz[0], statistics_med := st.median(nz)))
print(f"   60 semiprimes p*q (3-digit primes): unit solutions per N = {set(r[0] for r in rows)}, solutions with K=0 (the true pair and its swap) = {set(r[1] for r in rows)}")
print(f"   smallest nonzero |K| among the other solutions: min {min(r[2] for r in rows)}, median {st.median(r[2] for r in rows)}, max {max(r[2] for r in rows)}; median |K| overall {st.median(r[3] for r in rows):.0f} (of a possible ~{10**n})")
