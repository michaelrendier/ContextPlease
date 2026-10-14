"""Chase the Lyndon-factor observation to its source. Observation (gl_collatz.py section 5): the Lyndon factorisation of the parity streams of five Collatz orbits had 8-10 factors
against 5-7 for random bit strings of the same length. Hypotheses: (H1) artefact of how the streams end (orbit stops at 1, then '1,0' appended); (H2) artefact of conditioning on
reaching 1; (H3) a real property of the parity stream of the shortcut map (but R2 says the first k parities of a RANDOM n are iid fair bits, so H3 predicts NO difference for large random n).
Duval's algorithm is checked against the engine's lyndon.descend before use."""
import sys, random, statistics as st, math
sys.path.insert(0, '/home/rendier/Projects/ThePlace/GenerationalLineage')
from engine.toolsets import lyndon
def T(n): return n >> 1 if n % 2 == 0 else (3 * n + 1) >> 1
def duval_count(s):
    n = len(s); i = 0; c = 0
    while i < n:
        j, k = i + 1, i
        while j < n and s[k] <= s[j]:
            k = i if s[k] < s[j] else k + 1; j += 1
        while i <= k:
            i += j - k; c += 1
    return c
rng = random.Random(14102026)
# 0. validity: Duval == engine omega
bad = 0
for _ in range(300):
    L = rng.randint(5, 200); s = ''.join(rng.choice('01') for _ in range(L))
    if duval_count(s) != lyndon.descend(s)['omega']: bad += 1
print('0. Duval vs engine lyndon.descend omega on 300 random strings: disagreements =', bad)
def stream_to_one(n):
    s = []; m = n
    while m != 1: s.append(m & 1); m = T(m)
    return s
def stream_k(n, k):
    s = []; m = n
    for _ in range(k): s.append(m & 1); m = T(m)
    return s
def omega(bits): return duval_count(''.join(map(str, bits)))
def stats(xs): return f'{st.mean(xs):.2f} (sd {st.pstdev(xs):.2f}, n={len(xs)})'
print('\n1. The five original orbits, three ways to end the stream:')
for n in (27, 97, 871, 6171, 77031):
    s = stream_to_one(n); N = len(s)
    ends = {'to 1, nothing appended': s, 'to 1, then "1,0" (original)': s + [1, 0]}
    ctrl = {}
    for name, x in ends.items():
        c = [omega([rng.randint(0, 1) for _ in range(len(x))]) for _ in range(2000)]
        ctrl[name] = c
    c_tail = [omega([rng.randint(0, 1) for _ in range(N)] + [1, 0]) for _ in range(2000)]
    print(f'  n={n:6d} N={N:4d} omega: to-1 {omega(s):2d} (random ctrl {stats(ctrl["to 1, nothing appended"])}) | original {omega(s+[1,0]):2d} (random ctrl {stats(ctrl["to 1, then \"1,0\" (original)"])}) | random bits + tail "1,0": {stats(c_tail)}')
print('\n2. H3 test: first k parities of a LARGE random n (no termination, should be iid fair bits by R2)')
for k in (72, 115, 223):
    big = [omega(stream_k(rng.getrandbits(400) | 1, k)) for _ in range(2000)]
    ctrl = [omega([rng.randint(0, 1) for _ in range(k)]) for _ in range(2000)]
    ones = st.mean(sum(stream_k(rng.getrandbits(400) | 1, k)) / k for _ in range(300))
    print(f'  k={k:3d}: large random n {stats(big)}   random bits {stats(ctrl)}   fraction of ones in stream {ones:.3f}')
print('\n3. H2 test: many small starting values, streams to 1, compared with length-matched random bits (2000 draws per n)')
zs = []
sample = rng.sample(range(3, 200001, 2), 300)
for n in sample:
    s = stream_to_one(n)
    c = [omega([rng.randint(0, 1) for _ in range(len(s))]) for _ in range(300)]
    mu, sd = st.mean(c), st.pstdev(c) or 1.0
    zs.append((omega(s) - mu) / sd)
print(f'  z-score of omega(Collatz stream to 1) vs length-matched random: mean z = {st.mean(zs):+.2f}, sd {st.pstdev(zs):.2f}, fraction with z>0: {sum(z>0 for z in zs)/len(zs):.2f}  (n={len(zs)} starting values)')
print('\n4. What distinguishes the streams that reach 1: density of ones, and the first and last 10 bits')
dens = [sum(stream_to_one(n)) / len(stream_to_one(n)) for n in sample[:100]]
print(f'  fraction of ones in streams to 1 (mean over 100 starts): {st.mean(dens):.3f}   (iid fair = 0.500; critical log2/log3 = 0.631)')
tails = {}
for n in sample:
    s = stream_to_one(n); t = ''.join(map(str, s[-6:])); tails[t] = tails.get(t, 0) + 1
print('  last six bits before reaching 1, most common:', sorted(tails.items(), key=lambda x: -x[1])[:5])
