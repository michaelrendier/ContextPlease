"""Second step of the chase: H1b (all starts were ODD, so every stream began with '1'; the 'large random n' used n|1, also odd) and H2 (streams that reach 1 end in a nearly forced tail).
Controls are matched on exactly the features being tested."""
import random, statistics as st
exec(open('lyndon_chase.py').read().split("rng = random.Random")[0].split('sys.path.insert')[0])   # imports only
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
def omega(bits): return duval_count(''.join(map(str, bits)))
rng = random.Random(14102026 + 1)
def stream_k(n, k):
    s = []; m = n
    for _ in range(k): s.append(m & 1); m = T(m)
    return s
def stream_to_one(n):
    s = []; m = n
    while m != 1: s.append(m & 1); m = T(m)
    return s
def rb(N, first=None, last=None):
    b = [rng.randint(0, 1) for _ in range(N)]
    if first is not None: b[0] = first
    if last: b[-len(last):] = list(last)
    return b
def stats(xs): return f'{st.mean(xs):.2f} (sd {st.pstdev(xs):.2f})'
print('A. Does forcing the FIRST bit to 1 raise the Lyndon-factor count of random bits?   (N=115, 20000 draws each)')
A0 = [omega(rb(115)) for _ in range(20000)]; A1 = [omega(rb(115, first=1)) for _ in range(20000)]; A2 = [omega(rb(115, first=0)) for _ in range(20000)]
print(f'   first bit free {stats(A0)} | first bit 1 {stats(A1)} | first bit 0 {stats(A2)}')
print('\nB. H3 / R2 test, matched: first k=115 parities of a LARGE random n (400 bits) vs random bits with the SAME first bit   (3000 draws)')
for parity in (1, 0):
    big = [omega(stream_k((rng.getrandbits(400) & ~1) | parity, 115)) for _ in range(3000)]
    ctl = [omega(rb(115, first=parity)) for _ in range(3000)]
    print(f'   n parity {parity}: large random n {stats(big)} | random bits, first bit {parity}: {stats(ctl)}')
print('\nC. H2 test: small odd starts, stream to 1, z-scores against three controls (300 starts, 400 control draws each)')
sample = rng.sample(range(3, 200001, 2), 300)
rows = {'unmatched': [], 'first bit matched': [], 'first bit + last 6 bits (001000) matched': []}
for n in sample:
    s = stream_to_one(n); N = len(s); w = omega(s)
    tail = tuple(s[-6:])
    for name, mk in (('unmatched', lambda: rb(N)), ('first bit matched', lambda: rb(N, first=1)), ('first bit + last 6 bits (001000) matched', lambda: rb(N, first=1, last=tail))):
        c = [omega(mk()) for _ in range(400)]
        rows[name].append((w - st.mean(c)) / (st.pstdev(c) or 1.0))
for name, zs in rows.items():
    print(f'   {name:44s} mean z {st.mean(zs):+.2f} (sd {st.pstdev(zs):.2f}), fraction z>0 {sum(z>0 for z in zs)/len(zs):.2f}')
print('\nD. same, small EVEN starts (first bit 0), first bit + tail matched (200 starts)')
sample_e = rng.sample(range(4, 200001, 2), 200); zs = []
for n in sample_e:
    s = stream_to_one(n); N = len(s); tail = tuple(s[-6:])
    c = [omega(rb(N, first=0, last=tail)) for _ in range(400)]
    zs.append((omega(s) - st.mean(c)) / (st.pstdev(c) or 1.0))
print(f'   even starts, matched: mean z {st.mean(zs):+.2f} (sd {st.pstdev(zs):.2f}), fraction z>0 {sum(z>0 for z in zs)/len(zs):.2f}')
