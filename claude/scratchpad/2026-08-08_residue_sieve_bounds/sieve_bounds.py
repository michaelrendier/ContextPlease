from math import log, exp, gcd
from sympy import primerange

print("=== 1. LAST-DIGIT CONSTRAINT: does knowing N mod m restrict p? ===")
for m in (10, 100, 1000):
    units = [a for a in range(m) if gcd(a, m) == 1]
    # for a fixed N residue, which p residues are possible?
    worst = 0
    for Nr in units:
        ok = [p for p in units if (Nr * pow(p, -1, m)) % m in units]
        worst = max(worst, len(ok))
    print(f"  m={m:5d}: phi(m)={len(units):4d} unit residues | p residues NOT excluded: {worst:4d}"
          f"  -> reduction factor {len(units)/worst:.3f}x")
print("  REASON: q = N*p^-1 mod m is DETERMINED by p. The pair is constrained; p alone is not.\n")

print("=== 2. WHAT DOES HELP: wheel / small-prime sieving, density = prod(1-1/p) ===")
for B in (10, 100, 10**3, 10**4, 10**6):
    d = 1.0
    for p in primerange(2, B+1): d *= (1 - 1/p)
    print(f"  sieve all primes <= {B:>8}: density {d:.5f}  -> speedup {1/d:6.2f}x")
print("  Mertens: density ~ e^-gamma / ln B  -> the WHOLE family is bounded by ~1/ln B.\n")

print("=== 3. THE ACTUAL GAP, RSA-2048 ===")
lnN = 2048*log(2)
gnfs = exp(1.923 * lnN**(1/3) * log(lnN)**(2/3))
trial = 2**1023 / (1024*log(2))            # primes up to sqrt(N)
print(f"  primes to try, naive          : 10^{log(trial,10):.1f}")
print(f"  GNFS operations               : 10^{log(gnfs,10):.1f}")
print(f"  GNFS already buys             : 10^{log(trial/gnfs,10):.0f}  orders of magnitude")
print(f"  best possible residue sieve   : 10^{log(1/0.027,10):.1f}  orders of magnitude (~37x)\n")

print("=== 4. GO COMPARISON ===")
go_legal, go_tree = 2.08e170, 1e360
print(f"  Go legal positions            : 10^{log(go_legal,10):.0f}")
print(f"  Go game-tree complexity       : 10^{log(go_tree,10):.0f}")
print(f"  1024-bit primes               : 10^{log(trial,10):.0f}")
print(f"  ratio to Go legal positions   : 10^{log(trial/go_legal,10):.0f}  ({log(trial,10)/log(go_legal,10):.1f}x the orders of magnitude)")
