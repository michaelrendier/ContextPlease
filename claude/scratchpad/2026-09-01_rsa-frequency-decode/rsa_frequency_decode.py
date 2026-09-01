#!/usr/bin/env python3
"""
rsa_frequency_decode.py  --  test Cody's proposal (2026-09-01)

  "ping the factors of an RSA modulus from the Ceiling down to 0 ... have both
   of those numbers be a frequency decode through the prime wavelength and prime
   spiral crystallography ... the ordinal are the locations ... the Zeta index
   is the anchor and the tension is the 'weight of the primes'. test this"

Machinery under test:
  prime wavelength      f(p) = F0 * ln(p)             (log-frequency: products -> sums)
  prime spiral (Sacks)  p -> (r = sqrt(p), phi = 2*pi*sqrt(p) mod 2*pi)
  ordinal = location    k = pi(p)                     (the index of p)
  zeta index = anchor   theta_RS(gamma * ln p) mod 2*pi   (Riemann-Siegel theta)
  tension = weight      w(p) = ln(p)/sqrt(p)          (zeta_weight; peaks at p = 7)

Four tests. Each ends with an explicit CODE / MATHS / METHOD verdict
(per the generational-lineage rule: three kinds of wrong).
"""
import math, time
import numpy as np

# ----------------------------------------------------------------- primes ------
def sieve(n):
    b = np.ones(n + 1, bool); b[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if b[i]:
            b[i * i::i] = False
    return np.flatnonzero(b).astype(np.int64)

P = sieve(3_000_000)
PI_OF = {int(p): i for i, p in enumerate(P, start=1)}   # prime -> ordinal (pi(2)=1)

def is_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1; s = 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

# --------------------------------------------------------------- mappings ------
F0 = 100.0                                  # Hz per nat
def f_of(p):  return F0 * math.log(p)

def theta_rs(t):
    """asymptotic Riemann-Siegel theta, float"""
    if t <= 0:
        return 0.0
    return (0.5 * t * math.log(t / (2 * math.pi)) - 0.5 * t - math.pi / 8
            + 1.0 / (48 * t) + 7.0 / (5760 * t ** 3))

GAMMA = 14.134725                            # height of the first Riemann zero
def anchor(p):  return theta_rs(GAMMA * math.log(p)) % (2 * math.pi)
def tension(p): return math.log(p) / math.sqrt(p)
def sacks_phi(p): return (2 * math.pi * math.sqrt(p)) % (2 * math.pi)

def p_of_f(f):
    """nearest prime whose f() matches a measured frequency -- the 'decode'"""
    target = math.exp(f / F0)
    idx = int(np.searchsorted(P, target))
    cands = [int(P[max(0, idx - 1)]), int(P[min(len(P) - 1, idx)])]
    return min(cands, key=lambda q: abs(f_of(q) - f))


# ================================================================ TEST 1 ======
def test1_two_tone_decode():
    print("=" * 72)
    print("TEST 1   small-semiprime two-tone frequency decode  (does it work at all)")
    print("=" * 72)
    SR, DUR = 48_000, 0.5
    t = np.arange(int(SR * DUR)) / SR
    res_hz = 1.0 / DUR
    win = np.hanning(len(t))
    freqs = np.fft.rfftfreq(len(t), 1 / SR)
    rng = np.random.default_rng(0)
    pool = [int(x) for x in P[:400]]                     # primes up to ~2740

    buckets = {}
    for _ in range(600):
        p, q = int(rng.choice(pool)), int(rng.choice(pool))
        if p == q:
            continue
        sig = (tension(p) * np.sin(2 * np.pi * f_of(p) * t)
               + tension(q) * np.sin(2 * np.pi * f_of(q) * t))
        spec = np.abs(np.fft.rfft(sig * win))
        order = np.argsort(spec)[::-1]
        picks = []
        for i in order:
            if all(abs(freqs[i] - freqs[j]) > 3 for j in picks):
                picks.append(int(i))
            if len(picks) == 2:
                break
        got = sorted(p_of_f(freqs[i]) for i in picks)
        b = 1 << int(max(p, q)).bit_length()
        d = buckets.setdefault(b, [0, 0])
        d[1] += 1
        d[0] += (got == sorted([p, q]))

    print(f"  FFT resolution = {res_hz:.1f} Hz     f(p) spacing near p: 100/p Hz per unit p")
    print(f"  {'max prime <':>14} | {'exact recovery':>16}")
    for b in sorted(buckets):
        ok, tot = buckets[b]
        print(f"  {b:>14} | {ok:>5}/{tot:<5} = {ok / tot:5.0%}")
    print()
    print("  VERDICT")
    print("    CODE   : ran, deterministic")
    print("    MATHS  : forward render exact; log map additive (Test 2)")
    print("    METHOD : decode succeeds only while f(p), f(q) are separated by more")
    print("             than the FFT bin. That needs TWO already-distinct tones --")
    print("             the DTMF row+col. A semiprime hands you ONE sum tone.")


# ================================================================ TEST 2 ======
def test2_identities():
    print("=" * 72)
    print("TEST 2   which quantity linearises the product  N = p*q")
    print("=" * 72)
    rng = np.random.default_rng(1)
    pool = [int(x) for x in P[100:8000]]
    d_logf, d_sacks, d_anchor = [], [], []
    for _ in range(4000):
        p, q = int(rng.choice(pool)), int(rng.choice(pool))
        N = p * q
        d_logf.append(f_of(N) - (f_of(p) + f_of(q)))
        d_sacks.append((sacks_phi(N) - (sacks_phi(p) + sacks_phi(q))) % (2 * math.pi))
        d_anchor.append((anchor(N) - (anchor(p) + anchor(q))) % (2 * math.pi))
    d_logf = np.abs(np.array(d_logf))
    d_sacks = np.array(d_sacks)
    d_anchor = np.array(d_anchor)
    uni = math.pi / math.sqrt(3)                          # std of U(0,2pi)
    print(f"  log-frequency   |f(N) - (f(p)+f(q))|   max = {d_logf.max():.2e}"
          "      -> ADDITIVE (exact)")
    print(f"  Sacks angle     residual mod 2pi       std = {d_sacks.std():.3f} rad"
          f"   (U(0,2pi) std = {uni:.3f})  -> NOT additive")
    print(f"  zeta anchor     residual mod 2pi       std = {d_anchor.std():.3f} rad"
          f"   (U(0,2pi) std = {uni:.3f})  -> NOT additive")
    print()
    print("  VERDICT")
    print("    MATHS  : ln is the ONLY tested map with f(N) = f(p) + f(q).")
    print("             2*pi*sqrt(.) and theta_RS(.) are non-linear in the factors:")
    print("             they RE-CLOCK the schedule (cf. un-sieve) but add NO")
    print("             independent linear constraint on {p, q}.")
    print("    METHOD : one linear equation, two unknowns. No second filter tone.")


# ================================================================ TEST 3 ======
def test3_ceiling_probe():
    print("=" * 72)
    print("TEST 3   'ping from the Ceiling down to 0'  --  swept resonance probe")
    print("=" * 72)
    rng = np.random.default_rng(2)
    print(f"  {'bits':>4} | {'gap p-q':>18} | {'steps ceiling->hit':>20} | recovered")
    for bits in (24, 32, 40, 48):
        half = bits // 2
        # (a) random balanced primes  -- real-RSA-like gap ~ sqrt(N)
        p = next_prime(int(rng.integers(2 ** (half - 1), 2 ** half)))
        q = next_prime(int(rng.integers(2 ** (half - 1), 2 ** half)))
        p, q = max(p, q), min(p, q)
        N = p * q
        r = math.isqrt(N); steps = 0
        while r > 1 and N % r:
            r -= 1; steps += 1
        print(f"  {bits:>4} | {p - q:>18,} | {steps:>20,} | {r == q and (N // r) == p}")
        # (b) deliberately CLOSE primes -- the 'same bit length' RSA flaw, extreme
        base = next_prime(int(rng.integers(2 ** (half - 1), 2 ** half)))
        p2 = next_prime(base); q2 = next_prime(p2)
        N2 = p2 * q2
        r = math.isqrt(N2); steps = 0
        while r > 1 and N2 % r:
            r -= 1; steps += 1
        print(f"  {bits:>4} | {q2 - p2:>18,} | {steps:>20,} | {'(close primes)':>9}")
    print()
    print("  VERDICT")
    print("    CODE   : ran; recovers p, q exactly for small N")
    print("    MATHS  : resonance R(r) = [ r | N ].  Exact peaks at r in {p, q}.")
    print("    METHOD : the downward sweep from sqrt(N) IS Fermat's method.")
    print("             steps ~ (sqrt(N) - q) ~ |p - q| / (2 sqrt(N)) * sqrt(N).")
    print("             CLOSE primes  -> a few steps  (this is why RSA forbids it).")
    print("             BALANCED random primes -> ~sqrt(N) steps -> a HUNT.")
    print("             'Ceiling down to 0' does not change O(pi(sqrt N)).")


# ================================================================ TEST 4 ======
def test4_recipe():
    print("=" * 72)
    print("TEST 4   Cody's recipe:  ordinal = location, zeta = anchor, tension = weight")
    print("=" * 72)
    rng = np.random.default_rng(3)
    pool = [int(x) for x in P[1000:40000]]
    X, y_sum, y_lo = [], [], []
    for _ in range(4000):
        p, q = int(rng.choice(pool)), int(rng.choice(pool))
        N = p * q
        # features a decoder actually holds -- functions of N ALONE:
        X.append([
            N / math.log(N),                 # ordinal 'location' proxy pi(N)
            anchor(N),                        # zeta anchor of N
            math.log(N),                      # = ln p + ln q   (the sum tone)
            sacks_phi(N),                     # spiral angle of N
            tension(N),                       # 'weight' of N
        ])
        lo, hi = min(p, q), max(p, q)
        y_sum.append(math.log(p) + math.log(q))
        y_lo.append(math.log(lo))
    X = np.array(X); y_sum = np.array(y_sum); y_lo = np.array(y_lo)
    Xa = np.hstack([X, np.ones((len(X), 1))])

    def r2(y):
        c, *_ = np.linalg.lstsq(Xa, y, rcond=None)
        pred = Xa @ c
        return 1 - np.sum((y - pred) ** 2) / np.sum((y - y.mean()) ** 2)

    print(f"  best linear decode from N-only features:")
    print(f"    ln p + ln q   (the SUM  / one tone) : R^2 = {r2(y_sum):.4f}")
    print(f"    ln(min factor)(the SPLIT / 2nd tone): R^2 = {r2(y_lo):.4f}")
    print()
    print("  VERDICT")
    print("    CODE   : ran, deterministic (lstsq)")
    print("    MATHS  : sum  ln p + ln q = ln N        -> R^2 = 1   (a filter)")
    print("             split into the two addends     -> R^2 ~ 0   (a hunt)")
    print("    METHOD : ordinal(N) is a function of N (no factor info); the zeta")
    print("             anchor is non-linear; tension is an amplitude, not a")
    print("             coordinate. The recipe delivers the SUM tone and no second")
    print("             independent tone. RSA sets p ~ q, so the sum tone's two")
    print("             halves are ~equal -> maximally degenerate. That degeneracy")
    print("             IS the 'same bit length' rule.")


def main():
    t0 = time.time()
    test1_two_tone_decode(); print()
    test2_identities();       print()
    test3_ceiling_probe();    print()
    test4_recipe();           print()
    print("=" * 72)
    print("SYNTHESIS")
    print("=" * 72)
    print("""\
  The prime wavelength with f(p) = F0*ln(p) makes a semiprime an EXACT one-tone
  sum:  f(N) = f(p) + f(q).  That single tone is a clean filter (R^2 = 1).

  A filter decode of {p, q} needs a SECOND, independent linear constraint --
  the DTMF column to that row.  The two candidates from the machinery:
      * prime spiral angle   2*pi*sqrt(N)
      * zeta / RS-theta index
  are both non-linear in the factors.  Tested: they re-clock the schedule but
  carry no independent linear constraint.  So the decode stays one equation in
  two unknowns -- a hunt, O(pi(sqrt N)).

  RSA's two documented weak spots fall straight out:
      'far enough apart'  -> one tone near DC (q small) -> trial division reads it
      'same bit length'   -> the two half-tones coincide -> nothing to separate
  RSA lives exactly in the band where the one tone we DO get is maximally
  degenerate.  The machinery explains WHY factoring is hard here; it does not
  make it easy.

  Where it IS a filter: small and structured N (Test 1 low band), where the
  factor tones are already resolvable -- the same 8 tones the phone company
  could afford.\
""")
    print(f"\n  ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
