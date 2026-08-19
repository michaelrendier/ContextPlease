#!/usr/bin/env python3
"""
THE PARENTS OF AN RSA MODULUS — the same lineage question, asked of Z/N.

For N = p*q the parents are p and q, and CRT is the genealogy:

    Z/N  ~=  Z/p  x  Z/q          (exact, elementary)

This asks the questions we just asked of the Cayley-Dickson tower:
  - what is the census (units vs zero divisors)?
  - what is the recursion / inheritance rule?
  - what is the zero-divisor DENSITY, and how does it scale?
and states plainly where the analogy holds and where it breaks.
"""
import math
from sympy import isprime, totient, nextprime

def census(p, q):
    N = p * q
    units = (p - 1) * (q - 1)                 # phi(N)
    zd_p  = q - 1                             # nonzero multiples of p:  p,2p,...,(q-1)p
    zd_q  = p - 1                             # nonzero multiples of q
    return {'N': N, 'units': units, 'zd_p': zd_p, 'zd_q': zd_q,
            'zero': 1, 'total': units + zd_p + zd_q + 1,
            'exact': units + zd_p + zd_q + 1 == N,
            'zd_density': (zd_p + zd_q) / N}

print("=" * 76)
print("THE CENSUS OF Z/N  —  the exact partition")
print("=" * 76)
print("  every element is: a unit, a nonzero zero divisor, or 0")
print(f"  N = phi(N) + (q-1) + (p-1) + 1 = (p-1)(q-1) + (q-1) + (p-1) + 1\n")
print(f"{'p':>7} {'q':>7} {'N':>11} {'units phi(N)':>13} {'ZDs':>8} {'exact':>7} {'ZD density':>12}")
for p, q in [(3,5),(7,11),(13,17),(101,103),(1009,1013),(65537,65539),(1000003,1000033)]:
    if not (isprime(p) and isprime(q)): continue
    c = census(p, q)
    print(f"{p:>7} {q:>7} {c['N']:>11} {c['units']:>13} {c['zd_p']+c['zd_q']:>8} "
          f"{str(c['exact']):>7} {c['zd_density']:>12.3e}")

print()
print("=" * 76)
print("THE INHERITANCE RULE  —  and how it compares to the CD tower")
print("=" * 76)
print("""
  CD tower   total(2d) = 2*total(d) + 2(d-1)(d-2)      <- two copies of the
                          \\_______/   \\____________/       parent + the new
                          inherited     intermarriage       couplings between

  Z/N        N         = (p-1)(q-1)  + (p-1) + (q-1) + 1
                          \\________/    \\____________/
                           the units     each parent's own kernel
                           (intermarriage)  (inherited, disjoint)

  SAME SHAPE: a product term for what the two parents make TOGETHER, plus a
  linear term for what each contributes ALONE. In both, the product term is
  the one that dominates.
""")

print("=" * 76)
print("WHERE THE ANALOGY BREAKS — and it breaks in the direction that matters")
print("=" * 76)
print(f"\n{'object':>26} {'ZD density':>14} {'as size grows':>22}")
print(f"{'-'*64}")
for d in (16, 64, 256, 512):
    frac = 1 - (d*(3*math.log2(d) - 2.5) + 4)/(d*(d-1))
    print(f"{'Cayley-Dickson dim '+str(d):>26} {frac:>14.6f} {'-> 1  (takes over)':>22}")
for p, q in [(101,103),(65537,65539),(1000003,1000033)]:
    c = census(p, q)
    print(f"{'Z/N, N='+str(c['N']):>26} {c['zd_density']:>14.3e} {'-> 0  (vanishes)':>22}")
print("""
  OPPOSITE ASYMPTOTICS. In the CD tower zero divisors take over: density -> 1.
  In Z/N they vanish: density ~ 1/p + 1/q -> 0. A random element of Z/N is
  almost surely a UNIT; a random basis-pair diagonal high in the CD tower is
  almost surely a ZERO DIVISOR.
""")

print("=" * 76)
print("THE HARD PART, STATED EXACTLY")
print("=" * 76)
print("""
  In Z/N, exhibiting ONE non-trivial zero divisor IS factoring:

      x a zero divisor  =>  gcd(x, N) is a non-trivial factor
""")
p, q = 1000003, 1000033
N = p * q
for x in (3*p, 7*q, 12345*p):
    g = math.gcd(x % N, N)
    print(f"    x = {x % N:<14}  gcd(x, N) = {g:<9}  -> parent found: {g in (p,q)}")
print(f"""
  So the ZD structure of Z/N and its factorisation are THE SAME OBJECT.
  The CD tower's zero divisors are cheap to enumerate because the
  multiplication table is KNOWN and finite. Z/N's are expensive for exactly
  the reason RSA exists: you cannot write the table down without the parents.

  ENUMERABILITY IS THE WHOLE DIFFERENCE. Structural similarity between the
  two censuses does not transfer any of it.
""")

print("=" * 76)
print("delta = (1/2) ln(q/p)  —  the repo's own negative result (Phase 24)")
print("=" * 76)
print(f"\n{'p':>10} {'q':>10} {'q/p':>10} {'delta':>12}   note")
for p, q in [(3,1000003),(101,65537),(65537,65539),(1000003,1000033)]:
    d = 0.5*math.log(q/p)
    note = 'BALANCED — delta collapses' if abs(d) < 1e-3 else 'unbalanced'
    print(f"{p:>10} {q:>10} {q/p:>10.4f} {d:>12.6f}   {note}")
print("""
  A semiprime's 'hidden content' delta = (1/2)ln(q/p) goes to ZERO exactly
  when p ~ q -- which is precisely how RSA moduli are chosen. The quantity
  is largest for the cases already easy, and vanishes for the case that
  matters. That is a documented NEGATIVE result and it stands.
""")
