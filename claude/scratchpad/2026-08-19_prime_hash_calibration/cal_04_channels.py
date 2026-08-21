#!/usr/bin/env python3
"""cal_04_channels.py — does ANY context channel map carry contextual signal?

5c showed two candidates carrying none:
    hash     coherence 0.1545 shuffled / 0.1540 real   -> no signal
    descent  coherence 0.9961 shuffled / 0.9956 real   -> saturated

Both used LETTERS to compute a CONTEXT channel, which prime_hash.py's own
docstring names as the failure ("addressing by spelling is provenance
addressing"). So the question is whether a channel map built from what a word
LICENSES — its distributional company — separates real context from shuffled.

CONTROL IS RUN FIRST AND ON THE IDENTICAL PIPELINE.
"""
import sys, math, time, random, collections
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP')
import lineage_hash as LH

R = []
def out(s=''):
    R.append(s); print(s)

CP = LH.CONTEXT_PRIMES
WIN = 16

txt = open('/media/rendier/Datasets/ThePlace/DataSets/Language_Corpus/'
           'crawford_thesis_clean.txt', encoding='utf-8', errors='ignore').read()
toks = [t for t in (''.join(ch if ch.isalpha() else ' ' for ch in txt.lower())).split()
        if t.isascii() and len(t) > 1]
types = sorted(set(toks))
out(f'corpus {len(toks)} tokens / {len(types)} types')

# ── one pass: co-occurrence inside the sedenion window ────────────────
t0 = time.perf_counter()
uni = collections.Counter(toks)
co = collections.defaultdict(collections.Counter)
for i in range(0, len(toks) - WIN, WIN):
    w = toks[i:i + WIN]
    s = set(w)
    for a in s:
        for b in s:
            if a != b:
                co[a][b] += 1
build = time.perf_counter() - t0
out(f'co-occurrence table built in {build:.2f} s   '
    f'({sum(len(v) for v in co.values())} nonzero cells)')

N = sum(uni.values())
K = 8                                  # channels per word

def ppmi_channels(w):
    """The K associates with highest PPMI. THIS is what the word licenses."""
    c = co.get(w)
    if not c:
        return ()
    tot = sum(c.values())
    sc = []
    for b, n in c.items():
        p = (n / tot) / (uni[b] / N)
        if p > 1:
            sc.append((math.log2(p), b))
    sc.sort(reverse=True)
    return tuple(b for _, b in sc[:K])

t0 = time.perf_counter()
CHAN_IDX = {t: i for i, t in enumerate(types)}
CHANNELS = {t: ppmi_channels(t) for t in types}
CODE = {}
for t in types:
    v = 1
    for b in CHANNELS[t]:
        v *= CP[CHAN_IDX[b]]
    CODE[t] = v
prep = time.perf_counter() - t0
out(f'channel codes for {len(types)} types in {prep:.2f} s '
    f'(mean {1e6*prep/len(types):.1f} us/type, computed ONCE)')
out(f'mean channels per type   '
    f'{sum(len(v) for v in CHANNELS.values())/len(types):.2f}')
out()

windows = [toks[i:i + WIN] for i in range(0, len(toks) - WIN, WIN)]
SAMPLE = windows[:1200]
out(f'sampling {len(SAMPLE)} windows = {len(SAMPLE)*WIN} word-fills per condition')
out()

def descent_channels(w, ctx):
    """gcd(code(word), code(context)) -> the shared licence. THE DESCENT."""
    cw = CODE.get(w, 1)
    cx = 1
    seen = set()
    for t in ctx:
        for b in CHANNELS.get(t, ()):
            if b not in seen:
                seen.add(b)
                cx *= CP[CHAN_IDX[b]]
    g = math.gcd(cw, cx)
    if g == 1:
        return frozenset()
    return frozenset(b for b in CHANNELS.get(w, ()) if g % CP[CHAN_IDX[b]] == 0)

def run(shuffle, seed=11):
    rng = random.Random(seed)
    hist = collections.defaultdict(list)
    empty = 0
    t = 0.0
    for win in SAMPLE:
        for i, w in enumerate(win):
            ctx = win[:i] + win[i+1:]
            if shuffle:
                ctx = rng.sample(toks, len(ctx))
            t0 = time.perf_counter()
            k = descent_channels(w, ctx)
            t += time.perf_counter() - t0
            hist[w].append(k)
            if not k:
                empty += 1
    return hist, t, empty

def coherence(hist):
    vals = []
    for w, ks in hist.items():
        if len(ks) < 4:
            continue
        c = collections.Counter(ks)
        vals.append(c.most_common(1)[0][1] / len(ks))
    return (sum(vals)/len(vals) if vals else float('nan')), len(vals)

def meansize(hist):
    a = [len(k) for ks in hist.values() for k in ks]
    return sum(a)/len(a)

out('=' * 74)
out('PPMI CHANNEL DESCENT — control first')
out('=' * 74)
res = {}
for label, shuf in (('CONTROL (shuffled context)', True), ('REAL    (true context)', False)):
    hist, t, empty = run(shuf)
    c, n = coherence(hist)
    us = 1e6 * t / (len(SAMPLE) * WIN)
    res[label] = c
    out(f'{label}')
    out(f'   coherence        {c:.4f}   over {n} repeated words')
    out(f'   mean |shared|    {meansize(hist):.3f} channels')
    out(f'   empty descents   {empty}/{len(SAMPLE)*WIN}  '
        f'({100*empty/(len(SAMPLE)*WIN):.1f}%)')
    out(f'   cost             {us:.1f} us/word   {us*WIN/1000:.3f} ms/window')
    out()

a, b = res['REAL    (true context)'], res['CONTROL (shuffled context)']
out(f'REAL - CONTROL   {a - b:+.4f}      ratio {a/b:.4f}')
out()
out('for comparison, the two candidates from cal_03:')
out('   hash      0.1540 real / 0.1545 shuffled   diff -0.0005')
out('   descent   0.9956 real / 0.9961 shuffled   diff -0.0005')

with open('/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/'
          '2026-08-19_prime_hash_calibration/cal_04_channels.out', 'w') as f:
    f.write('\n'.join(R) + '\n')
