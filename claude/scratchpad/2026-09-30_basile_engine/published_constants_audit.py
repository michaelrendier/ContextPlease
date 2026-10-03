"""Audit of the constants in Basile's published files (libraryofbabel.info-algo: PRNG = babelia.cpp, imagesearch.cpp).
Read-only against Ainulindale/references/babel/. Uses gmpy2 for the big integers."""
import re, sys, time, math, random
import gmpy2
from gmpy2 import mpz
sys.set_int_max_str_digits(0)
D = "/home/rendier/Projects/ThePlace/Ainulindale/references/babel/"
def consts(path):
    out = {}
    for line in open(D + path):
        m = re.match(r'\s*static const boost::multiprecision::mpz_int (\w+)\("(\d+)"\);', line)
        if m: out[m.group(1)] = mpz(m.group(2))
    return out
t0 = time.time(); P = consts("PRNG"); I = consts("imagesearch.cpp"); print("parsed in %.1fs" % (time.time() - t0))
m, a, c, mk1, mk2, dv = (P[k] for k in ("m", "a", "c", "maskone", "masktwo", "divver")); ainv = I["ainverse"]
bl = lambda x: int(gmpy2.bit_length(x))
print("bit lengths: m %d | a %d | c %d | ainverse %d | maskone %d | masktwo %d | divver %d" % tuple(map(bl, (m, a, c, ainv, mk1, mk2, dv))))
print("image bits: 640*416 px * 12 = %d ; per quarter 33280*12 = %d ; shifts used: 399361 per quarter (8 quarters = %d bits)" % (640*416*12, 33280*12, 8*399361))
print("a < m: %s | c < m: %s | ainverse < m: %s | a/m ~ 2^%d | c/m ~ 2^%d" % (a < m, c < m, ainv < m, bl(a) - bl(m), bl(c) - bl(m)))
print("a * ainverse mod m == 1:", (a * ainv) % m == 1)
print("gcd(a, m) =", gmpy2.gcd(a, m) if bl(gmpy2.gcd(a, m)) < 64 else "large", "| gcd(c, m) =", gmpy2.gcd(c, m) if bl(gmpy2.gcd(c, m)) < 64 else "large")
print("m parity:", "odd" if m % 2 else "even", "| m mod 4 =", int(m % 4), "| a mod 4 =", int(a % 4), "| c mod 2 =", int(c % 2))
for name, x in (("maskone", mk1), ("masktwo", mk2), ("divver", dv)):
    pc = int(gmpy2.popcount(x)); print("%-8s popcount %d of %d bits; power of two: %s; 2^k-1: %s" % (name, pc, bl(x), pc == 1, pc == bl(x)))
print("divver bits - 399360 =", bl(dv) - 399360, "| divver - 2^399360 sign:", "greater" if dv > (mpz(1) << 399360) else "not greater")
# small prime factors of m and the Hull-Dobell condition a-1 divisible by every prime factor of m
small = [p for p in range(2, 200000) if gmpy2.is_prime(p)]
fac = [p for p in small if m % p == 0]
print("prime factors of m below 200000:", fac[:20], "| count", len(fac))
print("for those, (a-1) divisible:", [(p, (a - 1) % p == 0) for p in fac[:20]])
print("is m prime (probable):", bool(gmpy2.is_prime(m, 5)) if bl(m) < 4_000_000 else "skipped")
