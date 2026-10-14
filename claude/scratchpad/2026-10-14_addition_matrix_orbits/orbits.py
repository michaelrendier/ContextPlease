"""Addition-matrix columns as rotors: ring-theory and orbit checks (exact; stdlib only).
Question (Cody 2026-10-14): can each diagonal of the addition matrix be an orbit of orbits, like Enigma rotors? is it ring theory? what are the dynamics?"""
from math import gcd
from collections import Counter
def cycle_type(f, N):
    """Lengths of the cycles of the functional graph x -> f(x) on range(N) (a permutation's cycle type; for a non-bijective map, the cycles the rho-shaped orbits end in).
    FAULT KEPT: the first version walked until any repeat, which is only the cycle type for permutations, and reported 117 'CRT failures' that were all non-unit multipliers."""
    state = [0] * N; pos = [0] * N; ct = Counter()
    for s in range(N):
        if state[s]: continue
        path, x = [], s
        while state[x] == 0:
            state[x] = 1; pos[x] = len(path); path.append(x); x = f(x)
        if state[x] == 1: ct[len(path) - pos[x]] += 1
        for y in path: state[y] = 2
    return ct
def crt_combine(c1, c2):
    out = Counter()
    for l1, k1 in c1.items():
        for l2, k2 in c2.items():
            g = gcd(l1, l2); out[l1 * l2 // g] += k1 * k2 * g
    return out
print("1. x -> a x + b on Z/10^m: cycle type vs the CRT product of the types on Z/2^m and Z/5^m  (two rotor stacks of different gearing)")
bad = n = 0
for m in (1, 2, 3, 4):
    N, N2, N5 = 10 ** m, 2 ** m, 5 ** m
    for a in (1, 3, 7, 9, 11, 13, 17, 19, 21, 2, 5, 6, 10, 20):
        for b in (0, 1, 2, 3, 5, 7):
            t10 = cycle_type(lambda x: (a * x + b) % N, N)
            t2 = cycle_type(lambda x: (a * x + b) % N2, N2); t5 = cycle_type(lambda x: (a * x + b) % N5, N5)
            n += 1; bad += (t10 != crt_combine(t2, t5))
print(f"   {n} affine maps checked (m<=4; units and non-units of the ring, 'cycle type' = the cycles the orbits end in), CRT prediction wrong for {bad}")
for m in (1, 2, 3, 4):
    N = 10 ** m; print(f"   odometer x->x+1 on Z/10^{m}: {dict(cycle_type(lambda x: (x + 1) % N, N))}   | x->3x+1: {dict(sorted(cycle_type(lambda x: (3*x+1) % N, N).items()))}")
print("\n2. renormalisation: first-return map of the odometer on Z/10^m to the sub-lattice {x = 0 mod 10} is the odometer on Z/10^(m-1) (x -> x/10)")
ok = True
for m in (2, 3, 4):
    N = 10 ** m
    def ret(x):
        y = (x + 1) % N
        while y % 10: y = (y + 1) % N
        return y
    ok &= all(ret(x) // 10 == (x // 10 + 1) % (N // 10) for x in range(0, N, 10))
print("   conjugate to the odometer one scale down for m = 2,3,4:", ok)
print("\n3. the digit at global column c of num1*(num2+t) as a function of t: its minimal period (a rotor of period 10^(c+1)/gcd(num1,10^(c+1)))")
def min_period(seq, cap):
    for p in range(1, cap + 1):
        if all(seq[i] == seq[i + p] for i in range(len(seq) - p)): return p
    return None
rows = []
for num1 in (1, 2, 3, 5, 7, 10, 13, 1234567890):
    per = []
    for c in range(4):
        P = 10 ** (c + 1); seq = [(num1 * (987654 + t) // 10 ** c) % 10 for t in range(2 * P + 5)]
        per.append((min_period(seq, P), P // gcd(num1, P)))
    rows.append((num1, per)); print(f"   num1={num1:>10}: columns c=0..3  measured period / predicted:", ' '.join(f"{a}/{b}" for a, b in per))
print("   all equal:", all(a == b for _, per in rows for a, b in per))
print("\n4. tree automorphisms (the 'rotor' structure): a bijection of Z/b^n that induces a bijection mod b^k for every k<n; x->ax+b' with a coprime to the base qualifies")
def solenoidal(f, base, n):
    for k in range(1, n):
        M = base ** k; img = {}
        for x in range(base ** n):
            y = f(x) % M
            if img.setdefault(x % M, y) != y: return False
    return True
print("   odometer, x->3x+1, x->5x+7 on Z/2^n (n<=8) are solenoidal:", all(solenoidal(f, 2, n) for n in range(2, 9) for f in (lambda x: x + 1, lambda x: 3*x + 1, lambda x: 5*x + 7)))
print("   every cycle length of those maps on Z/2^n is a power of two:", all(all(l & (l - 1) == 0 for l in cycle_type(lambda x, a=a, b=b: (a*x + b) % 2**n, 2**n)) for n in range(1, 11) for a in (1, 3, 5, 7, 9, 11) for b in (0, 1, 2, 3)))
print("   x->2x+1 on Z/5^n (a=2 is a unit mod 5): cycle lengths for n=1..4:", [sorted(cycle_type(lambda x, n=n: (2*x + 1) % 5**n, 5**n)) for n in range(1, 5)], "(factors of 4 and 5 appear: not a 5-group)")
