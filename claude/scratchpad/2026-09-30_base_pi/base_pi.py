"""Base-π (β-expansion, β = π) of the integers and the primes; radix economy; the log-base view of d* = Ω/ln b.
Greedy (Rényi) expansion: digits in {0,1,2,3}. mpmath, 80 digits."""
import mpmath as mp, math, sympy
from collections import Counter
mp.mp.dps = 80
PI = mp.pi
def expand(n, frac=24):
    n = mp.mpf(n); k = 0
    while PI ** (k + 1) <= n: k += 1
    digs = []; x = n
    for e in range(k, -frac - 1, -1):
        w = PI ** e; d = int(mp.floor(x / w)); d = min(d, 3); digs.append(d); x -= d * w
    return k, digs, x                        # k = highest exponent; digs from PI^k down to PI^-frac; x = remainder
def fmt(k, digs):
    s = "".join(map(str, digs)); return s[:k + 1] + "." + s[k + 1:]
print("== integers and primes in base π (greedy expansion, digits 0..3) ==")
for n in list(range(1, 13)) + [17, 19, 23, 29, 31]:
    k, digs, r = expand(n); back = sum(d * PI ** (k - i) for i, d in enumerate(digs)) + r
    assert abs(back - n) < mp.mpf(10) ** -60
    tag = "prime" if sympy.isprime(n) else "     "
    print("%3d %s  %s   (remainder < π^-24: %s)" % (n, tag, fmt(k, digs), r < PI ** -24))
print("\n== do integers >= 4 terminate? (a terminating expansion is a polynomial in π; π is transcendental) ==")
for n in (4, 5, 7, 100):
    k, digs, r = expand(n, frac=60); print(n, "nonzero digits in the last 20 of 60 fractional places:", sum(1 for d in digs[-20:] if d))
print("\n== digit statistics of the first 24 fractional digits: primes vs all integers in [4, 400] ==")
def fracfreq(nums):
    c = Counter()
    for n in nums:
        k, digs, _ = expand(n); c.update(digs[k + 1:])
    t = sum(c.values()); return [round(c[d] / t, 4) for d in range(4)]
ints = list(range(4, 401)); primes = [p for p in ints if sympy.isprime(p)]
print("all integers (%d):" % len(ints), fracfreq(ints)); print("primes       (%d):" % len(primes), fracfreq(primes))
print("\n== how many admissible n-digit words? (cylinders of the β-transformation) ==")
states = {mp.mpf(1): 1}; prev = 1
for n in range(1, 41):
    new = {}
    for r, cnt in states.items():
        top = r * PI; m = int(mp.floor(top))
        full = m if top != m else m                     # digits 0..m-1 give a full image
        if full: new[mp.mpf(1)] = new.get(mp.mpf(1), 0) + cnt * full
        if top != m: key = mp.nstr(top - m, 40); new[mp.mpf(key)] = new.get(mp.mpf(key), 0) + cnt
    states = new; tot = sum(states.values())
    if n in (1, 2, 3, 5, 10, 20, 30, 40): print("n=%2d words=%s ratio=%.6f" % (n, tot, tot / prev)); 
    prev = tot
print("π =", float(PI), "| 4^n would be all 2-bit strings; log2(π) =", round(math.log2(math.pi), 4), "bits/digit; log2(3) =", round(math.log2(3), 4))
print("\n== the log-base view: d*_b = Ω / ln b ==")
Om = float(mp.lambertw(1).real)
for name, b in (("2", 2), ("e", math.e), ("3", 3), ("π", math.pi), ("10", 10)):
    print("b = %-2s  d*_b = %.5f   ln10/ln b = %.5f" % (name, Om / math.log(b), math.log(10) / math.log(b)))
b_half = math.exp(2 * Om)
print("base with d*_b = 1/2 exactly: b = e^(2Ω) = %.5f ; π = %.5f ; relative difference %.3f%%" % (b_half, math.pi, 100 * abs(b_half - math.pi) / math.pi))
print("Ω =", Om)
