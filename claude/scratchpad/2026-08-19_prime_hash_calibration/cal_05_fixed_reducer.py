#!/usr/bin/env python3
"""cal_05_fixed_reducer.py — cal_04 said the conditions separate; its coherence
statistic could not say so, because the EMPTY descent is a gate value and the
mode collapses onto it (shuffled: 33.6% empty, so the modal set IS the empty
set). argmax on gated data returns a confident wrong number.

Re-measured on statistics that are valid in the presence of a gate:
    - empties reported separately, never mixed into the average
    - agreement = mean pairwise Jaccard over a word's NON-EMPTY readings
    - a per-word paired test: same word, same reducer, real vs shuffled
"""
import sys, math, time, random, collections, statistics
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP')
import lineage_hash as LH

R = []
def out(s=''):
    R.append(s); print(s)

CP = LH.CONTEXT_PRIMES
WIN, K = 16, 8

txt = open('/media/rendier/Datasets/ThePlace/DataSets/Language_Corpus/'
           'crawford_thesis_clean.txt', encoding='utf-8', errors='ignore').read()
toks = [t for t in (''.join(ch if ch.isalpha() else ' ' for ch in txt.lower())).split()
        if t.isascii() and len(t) > 1]
types = sorted(set(toks))
uni = collections.Counter(toks)
co = collections.defaultdict(collections.Counter)
for i in range(0, len(toks) - WIN, WIN):
    s = set(toks[i:i + WIN])
    for a in s:
        for b in s:
            if a != b:
                co[a][b] += 1
N = sum(uni.values())
IDX = {t: i for i, t in enumerate(types)}

def ppmi_channels(w):
    c = co.get(w)
    if not c:
        return ()
    tot = sum(c.values())
    sc = [(math.log2((n/tot)/(uni[b]/N)), b) for b, n in c.items()
          if (n/tot)/(uni[b]/N) > 1]
    sc.sort(reverse=True)
    return tuple(b for _, b in sc[:K])

CHANNELS = {t: ppmi_channels(t) for t in types}
CODE = {}
for t in types:
    v = 1
    for b in CHANNELS[t]:
        v *= CP[IDX[b]]
    CODE[t] = v

def descent(w, ctx):
    cw = CODE.get(w, 1)
    cx, seen = 1, set()
    for t in ctx:
        for b in CHANNELS.get(t, ()):
            if b not in seen:
                seen.add(b); cx *= CP[IDX[b]]
    g = math.gcd(cw, cx)
    return frozenset(b for b in CHANNELS.get(w, ()) if g % CP[IDX[b]] == 0) if g > 1 else frozenset()

windows = [toks[i:i+WIN] for i in range(0, len(toks)-WIN, WIN)]
SAMPLE = windows[:1200]

def run(shuffle, seed=11):
    rng = random.Random(seed)
    hist = collections.defaultdict(list)
    for win in SAMPLE:
        for i, w in enumerate(win):
            ctx = rng.sample(toks, WIN-1) if shuffle else win[:i] + win[i+1:]
            hist[w].append(descent(w, ctx))
    return hist

def jaccard(a, b):
    u = a | b
    return len(a & b) / len(u) if u else 1.0

def agreement(readings):
    ne = [r for r in readings if r]
    if len(ne) < 2:
        return None
    tot = cnt = 0
    for i in range(len(ne)):
        for j in range(i+1, len(ne)):
            tot += jaccard(ne[i], ne[j]); cnt += 1
    return tot / cnt

out('=' * 74)
out('CORRECTED REDUCER — gate handled, paired per word')
out('=' * 74)
H = {}
for label, shuf in (('CONTROL (shuffled)', True), ('REAL    (true ctx)', False)):
    H[label] = run(shuf)
    all_r = [r for rs in H[label].values() for r in rs]
    ne = [r for r in all_r if r]
    out(f'{label}')
    out(f'   readings              {len(all_r)}')
    out(f'   EMPTY descents        {len(all_r)-len(ne)}  '
        f'({100*(len(all_r)-len(ne))/len(all_r):.1f}%)   [gate, reported separately]')
    out(f'   mean |shared| overall {statistics.mean(len(r) for r in all_r):.3f}')
    out(f'   mean |shared| non-mt  {statistics.mean(len(r) for r in ne):.3f}')
    ag = [a for rs in H[label].values() if (a := agreement(rs)) is not None]
    out(f'   agreement (Jaccard)   {statistics.mean(ag):.4f}   over {len(ag)} words')
    out()

out('=' * 74)
out('PAIRED PER-WORD TEST — same word, same reducer, real vs shuffled')
out('=' * 74)
c_h, r_h = H['CONTROL (shuffled)'], H['REAL    (true ctx)']
common = [w for w in r_h if len(r_h[w]) >= 4 and w in c_h]
d_share, d_empty, d_agree = [], [], []
for w in common:
    d_share.append(statistics.mean(len(r) for r in r_h[w])
                   - statistics.mean(len(r) for r in c_h[w]))
    d_empty.append(sum(1 for r in r_h[w] if not r)/len(r_h[w])
                   - sum(1 for r in c_h[w] if not r)/len(c_h[w]))
    ar, ac = agreement(r_h[w]), agreement(c_h[w])
    if ar is not None and ac is not None:
        d_agree.append(ar - ac)

def sign_test(d):
    pos = sum(1 for x in d if x > 0); neg = sum(1 for x in d if x < 0)
    n = pos + neg
    if n == 0:
        return pos, neg, float('nan')
    z = (pos - n/2) / math.sqrt(n/4)
    return pos, neg, z

for name, d in (('|shared| real-ctrl', d_share),
                ('empty%   real-ctrl', d_empty),
                ('agreement real-ctrl', d_agree)):
    pos, neg, z = sign_test(d)
    out(f'{name:22s}  mean {statistics.mean(d):+.4f}   '
        f'words better {pos:4d} / worse {neg:4d}   sign-test z = {z:+.2f}')
out()
out(f'words compared   {len(common)}')

with open('/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/'
          '2026-08-19_prime_hash_calibration/cal_05_fixed_reducer.out', 'w') as f:
    f.write('\n'.join(R) + '\n')
