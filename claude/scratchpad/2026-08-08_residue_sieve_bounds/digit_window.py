from math import gcd
from sympy import isprime

print("=== A. Can a modulus end in 26? ===")
print("  N = p*q with p,q odd primes  =>  N is ODD.  26 is even.")
print("  N mod 10 must be in {1,3,7,9}.  '26' cannot occur at all.\n")

print("=== B. The core question: do N's last digits FACTOR into p's and q's? ===")
print("  The operation is (p mod 100)*(q mod 100) = N mod 100  -- multiplication that WRAPS.")
print("  Integer factorization of the residue is NOT preserved.\n")
print("  COUNTEREXAMPLE, checkable by hand.  Target: N ends in 21 = 3 x 7.")
p, q = 211, 311
print(f"    {p} x {q} = {p*q}   both prime: {isprime(p)}, {isprime(q)}")
print(f"    N ends in {(p*q)%100:02d}.  p ends in {p%100}, q ends in {q%100}.")
print("    Neither factor ends in 3 or 7. 11 x 11 = 121 -> wraps to 21.\n")

print("=== C. For a target ending, which p endings are possible? ===")
units = [a for a in range(100) if gcd(a,100)==1]
for target in (1, 21, 49):
    ok = sorted({a for a in units if any((a*b)%100==target for b in units)})
    print(f"  N ends {target:02d}: {len(ok)}/{len(units)} p-endings possible -> {ok[:8]} ...")
print("  ALL 40 occur, every time. Given p's ending, q's is forced; p is never restricted.\n")

print("=== D. The decrementing/incrementing digit window: build p from the bottom ===")
print("  Write p = p_k + a*10^k, q = q_k + b*10^k, knowing p_k,q_k = p,q mod 10^k.")
print("  Matching one more digit of N gives ONE congruence:")
print("      a*q_k + b*p_k = (N - p_k*q_k)/10^k   (mod 10)")
print("  ONE equation, TWO unknowns (a and b).  For each of 10 choices of a, b is determined.")
print("  => branching factor 10 per decimal digit, 2 per bit.  NOTHING is pruned.")
n_digits = 309
print(f"  p has ~{n_digits} digits -> 10^{n_digits} leaves = the brute-force count, unchanged.\n")

print("=== E. Where this DOES become a real attack: Coppersmith 1996 ===")
for bits in (1024, 2048, 4096):
    pbits = bits//2
    print(f"  RSA-{bits}: p is {pbits} bits (~{int(pbits*0.301)} digits); "
          f"need {pbits//2} bits (~{int(pbits*0.301/2)} digits) of p to factor in poly time")
print("  You need HALF of p's digits. Two digits is not a partial win -- it is below threshold.")
