# SPDX-License-Identifier: GPL-3.0-only
"""
Twin-prime wheels: cut the primes into circles at the twin pairs.

A twin pair (p, p+2) has one number between its members, c = p + 1: the CENTRE.  Take two consecutive
centres c_i < c_{i+1}.  The wheel between them has circumference L = c_{i+1} − c_i and its zero point at c_i.
Every integer n with c_i ≤ n < c_{i+1} sits on the wheel at angle 2π(n − c_i)/L.  The end of one wheel
is the beginning of the next.

Runs cold with NumPy only:  python3 twin_wheels.py [N]      (default N = 10**7)
Prints every number it reports; nothing is fitted.
"""
import sys
import numpy as np

C2 = 0.6601618158468696            # Hardy–Littlewood twin prime constant, Π_{p≥3} p(p−2)/(p−1)²  (input, for comparison only)
B2 = 1.902160583104                # Brun's constant (input, for comparison only)


def sieve(n):
    """Boolean array is_prime[0..n]."""
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


def centres(is_prime):
    """Centres c = p+1 of every twin pair (p, p+2), in order."""
    p = np.nonzero(is_prime[:-2] & is_prime[2:])[0]
    return p + 1


def wheels(c):
    """Circumferences L_i = c_{i+1} − c_i of the wheels cut at the centres."""
    return np.diff(c)


def interior_primes(is_prime, c):
    """For each wheel, the number of primes strictly inside it, not counting the twin members that flank its ends."""
    cum = np.concatenate([[0], np.cumsum(is_prime)])         # cum[k] = number of primes < k
    inside = cum[c[1:] - 1] - cum[c[:-1] + 2]                # primes in [c_i + 2, c_{i+1} − 2]
    return inside


def singular_series(H, P=10 ** 6):
    """Hardy–Littlewood singular series of the tuple (n + h for h in H): Π_p (1 − ν_p/p)/(1 − 1/p)^k, ν_p = number of residues the tuple covers mod p."""
    s = sieve(P); prod = 1.0
    for p in np.nonzero(s)[0]:
        prod *= (1 - len({h % p for h in H}) / p) / (1 - 1 / p) ** len(H)
    return prod


def report(N):
    ip = sieve(N); c = centres(ip); L = wheels(c); ins = interior_primes(ip, c)
    out = {}
    out["N"] = N; out["twin pairs"] = len(c)
    out["first centres"] = c[:8].tolist()
    c6 = c[1:]                                                # (3,5) has centre 4; all later centres should be ≡ 0 (mod 6)
    out["centres ≡ 0 mod 6 (excluding (3,5))"] = f"{int(np.sum(c6 % 6 == 0))}/{len(c6)}"
    out["wheels L ≡ 0 mod 6 (excluding the first)"] = f"{int(np.sum(L[1:] % 6 == 0))}/{len(L[1:])}"
    m = L[1:] // 6                                             # wheel size in units of the circumference-6 circle
    out["mean L"] = float(L[1:].mean()); out["mean m = L/6"] = float(m.mean())
    out["local Hardy–Littlewood spacing at N, (ln N)²/(2C₂)"] = float(np.log(N) ** 2 / (2 * C2))
    out["smallest wheel"] = int(L.min()); out["largest wheel"] = int(L.max()); out["largest wheel at centre"] = int(c[np.argmax(L)])
    out["wheels with L = 6 (centres one 6-step apart)"] = int(np.sum(L == 6))
    out["wheels with no interior prime"] = int(np.sum(ins == 0))
    out["mean interior primes per wheel"] = float(ins.mean()); out["max interior primes"] = int(ins.max())
    # shape of the wheel-size distribution against a geometric law with the same mean (a Poisson cutting of the 6-steps)
    q = 1.0 / m.mean(); ks = np.arange(1, int(m.max()) + 1)
    pmf = q * (1 - q) ** (ks - 1); obs = np.bincount(m, minlength=len(ks) + 1)[1:] / len(m)
    out["max |observed − geometric| over m"] = float(np.max(np.abs(obs - pmf)))
    out["observed P(m=1), geometric P(m=1)"] = (float(obs[0]), float(pmf[0]))
    for mod in (30, 210):                                      # where the centres sit on the primorial circle
        cnt = np.bincount(c[c > 6] % mod, minlength=mod); nz = cnt[cnt > 0]
        out[f"centres > 6 mod {mod}: occupied residues / allowed"] = (len(nz), int(np.sum(np.array([(np.gcd(r - 1, mod) == 1 and np.gcd(r + 1, mod) == 1) for r in range(mod)]))))
        out[f"centres > 6 mod {mod}: min, max count over occupied"] = (int(nz.min()), int(nz.max()))
    out["wheel sizes by L mod 30 (0, 6, 12, 18, 24)"] = [int(np.sum(L[1:] % 30 == r)) for r in (0, 6, 12, 18, 24)]
    out["same, if consecutive centres drew their residue mod 30 independently from {0, 12, 18}"] = [1 / 3, 1 / 9, 2 / 9, 2 / 9, 1 / 9]
    out["observed shares"] = [round(float(np.mean(L[1:] % 30 == r)), 4) for r in (0, 6, 12, 18, 24)]
    out["share of wheels with m = 5 and m = 7 (L = 30, 42) vs m = 4 and m = 6"] = [float(np.mean(m == k)) for k in (5, 7, 4, 6)]
    # why the m = 1 wheel is rarer than a random cutting would make it: two adjacent centres c, c+6 are the quadruplet (c−1, c+1, c+5, c+7)
    S2, S4 = singular_series((0, 2)), singular_series((0, 2, 6, 8))
    out["singular series S(0,2), S(0,2,6,8)"] = (S2, S4)
    out["predicted P(m=1)/geometric = S(0,2,6,8)/(6·S(0,2)²)"] = S4 / (6 * S2 ** 2)
    out["observed P(m=1)/geometric"] = float(obs[0] / pmf[0])
    # Brun's sum and its tail
    s = float(np.sum(1.0 / c[1:] * 0 + 1.0 / (c[1:] - 1) + 1.0 / (c[1:] + 1)) + 1 / 3 + 1 / 5)
    out["Brun partial sum"] = s; out["B₂ − partial sum"] = B2 - s; out["4C₂/ln N"] = float(4 * C2 / np.log(N))
    # twin count against Hardy–Littlewood 2C₂ Σ 1/ln²x
    x = np.arange(2, N); hl = float(2 * C2 * np.sum(1.0 / np.log(x) ** 2))
    out["Hardy–Littlewood count"] = hl; out["observed / HL"] = len(c) / hl
    out["N / HL count (HL mean spacing over [0, N])"] = N / hl; out["N / observed pairs"] = N / len(c)
    return out, c, L, ins


def selfcheck(N=10 ** 6):
    """Cheap assertions that fail loudly if the program stops doing what this file says."""
    r, c, L, ins = report(N)
    assert c[0] == 4 and c[1] == 6 and np.all(c[1:] % 6 == 0) and np.all(L[1:] % 6 == 0)
    assert abs(r["B₂ − partial sum"] - r["4C₂/ln N"]) < 1e-3 and abs(r["observed / HL"] - 1) < 0.02
    return True


if __name__ == "__main__":
    N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10 ** 7
    r, c, L, ins = report(N)
    for k, v in r.items():
        print(f"{k}: {v}")
