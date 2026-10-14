"""The five-orbit table of gl_collatz.py section 5, redone with controls matched on the first bit and on the last six bits (the forced approach to 1)."""
import sys, random, statistics as st
sys.path.insert(0, '/home/rendier/Projects/ThePlace/GenerationalLineage')
from engine.toolsets import lyndon, berlekamp_massey, re_pair
def T(n): return n >> 1 if n % 2 == 0 else (3 * n + 1) >> 1
def stream_to_one(n):
    s = []; m = n
    while m != 1: s.append(m & 1); m = T(m)
    return s
def metrics(bits):
    sx = ''.join(map(str, bits))
    return (berlekamp_massey.descend(bits)['linear_complexity'], re_pair.descend(sx)['compression_ratio'], lyndon.descend(sx)['omega'])
rng = random.Random(77)
print(f'{"n":>6} {"N":>4} | Collatz (L, RePair ratio, Lyndon omega) | matched control mean (sd) | z for each')
for n in (27, 97, 871, 6171, 77031):
    s = stream_to_one(n); N = len(s); real = metrics(s); tail = s[-6:]
    ctl = []
    for _ in range(300):
        b = [rng.randint(0, 1) for _ in range(N)]; b[0] = s[0]; b[-6:] = tail; ctl.append(metrics(b))
    cols = list(zip(*ctl)); mu = [st.mean(c) for c in cols]; sd = [st.pstdev(c) or 1 for c in cols]
    z = [(r - m) / d for r, m, d in zip(real, mu, sd)]
    print(f'{n:6d} {N:4d} | L={real[0]:3d} R={real[1]:.3f} W={real[2]:2d} | L {mu[0]:.1f}({sd[0]:.1f}) R {mu[1]:.3f}({sd[1]:.3f}) W {mu[2]:.1f}({sd[2]:.1f}) | z = ({z[0]:+.1f}, {z[1]:+.1f}, {z[2]:+.1f})')
