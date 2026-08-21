#!/usr/bin/env python3
"""cal_03_context.py — composites + context. The refining pass.

5a  the three prime ladders, and where they collide
5b  box_kite() as a reducer: does it return one label for two opposite states
5c  the sedenion-window refining pass, CONTROL FIRST (shuffled context)
5d  one string -> 7 strings: the pencil, computed not asserted
"""
import sys, math, time, random, collections
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP')
import lineage_hash as LH
import prime_hash as PH
import context_fill as CF

R = []
def out(s=''):
    R.append(s); print(s)

LP = LH.LETTER_PRIME

def comp(word):
    v = 1
    for c in LH.split_tiers(word)[0]:
        v *= LP[c]
    return v

def strut_of(n):
    """Generation bits of a composite, read off its prime factors."""
    bits = 0
    for c in LH.FREQ_ORDER:
        if n % LP[c] == 0:
            bits |= 1 << LH.generation(LP[c])
    return bits

# ══════════════════════════════════════════════════════════════════════
out('=' * 74)
out('PASS 5a — THREE PRIME LADDERS IN THE LIVE CODE   (CALIBRATION)')
out('=' * 74)
lad = {
    'lineage_hash  letters': set(LP.values()),
    'lineage_hash  context': set(LH.CONTEXT_PRIMES[:64]),
    'prime_hash    letters': set(PH.LETTER_PRIMES),
    'prime_hash    context': set(PH.CONTEXT_PRIMES[:64]),
    'context_fill  kites  ': set(CF.ContextFill.PRIMES),
}
for k, v in lad.items():
    out(f'{k}   n={len(v):3d}   min={min(v):4d}  max={max(v):4d}')
out()
out('pairwise integer overlap between ladders that must not share values')
checks = [
    ('lineage_hash  letters', 'prime_hash    context'),
    ('context_fill  kites  ', 'lineage_hash  letters'),
    ('context_fill  kites  ', 'prime_hash    letters'),
    ('lineage_hash  context', 'prime_hash    context'),
]
for a, b in checks:
    ov = sorted(lad[a] & lad[b])
    tag = ''.join(LH.PRIME_LETTER.get(p, '') for p in ov)
    out(f'  {a}  x  {b}   |overlap|={len(ov):2d}  {ov[:10]}'
        + (f'   = letters {tag!r}' if tag else ''))
out()

# ══════════════════════════════════════════════════════════════════════
out('=' * 74)
out('PASS 5b — IS box_kite() A VALID REDUCER?   (RESULT)')
out('=' * 74)
words = []
with open('/usr/share/dict/words', encoding='utf-8', errors='ignore') as f:
    for line in f:
        w = line.strip()
        if w and w.isalpha() and w.isascii():
            words.append(w.lower())
words = sorted(set(words))

below = [w for w in words if not (LH.Word(w).strut & 0b1000)]
allDiv = [w for w in words if LH.Word(w).strut == 0b1000]
out(f'box_kite() returns None for   {len(below) + len(allDiv)} words')
out(f'  class 1  BELOW division  (no gen-3 letter at all)   {len(below):5d}')
out(f'  class 2  PURE division   (gen-3 letters ONLY)       {len(allDiv):5d}')
out(f'  the two classes are disjoint                        '
    f'{len(set(below) & set(allDiv)) == 0}')
out(f'  class 1 alphabet   {"".join(sorted({c for w in below for c in LH.split_tiers(w)[0]}))}')
out(f'  class 2 alphabet   {"".join(sorted({c for w in allDiv for c in LH.split_tiers(w)[0]}))}')
out(f'  class 1 sample     {below[::max(1,len(below)//8)][:8]}')
out(f'  class 2 sample     {allDiv[::max(1,len(allDiv)//8)][:8]}')
out()

# ══════════════════════════════════════════════════════════════════════
out('=' * 74)
out('PASS 5c — THE REFINING PASS, 16-WORD SEDENION WINDOW')
out('   CONTROL RUN FIRST: identical pipeline on SHUFFLED context.')
out('=' * 74)

txt = open('/media/rendier/Datasets/ThePlace/DataSets/Language_Corpus/'
           'crawford_thesis_clean.txt', encoding='utf-8', errors='ignore').read()
toks = [t for t in (''.join(ch if ch.isalpha() else ' ' for ch in txt.lower())).split()
        if t.isascii() and len(t) > 1]
out(f'corpus  crawford_thesis_clean.txt   {len(toks)} tokens, '
    f'{len(set(toks))} types')

WIN = 16
windows = [toks[i:i + WIN] for i in range(0, len(toks) - WIN, WIN)]
out(f'sedenion windows (16 words, non-overlapping)   {len(windows)}')
out()

cf = CF.ContextFill()

def kite_hash(w, ctx):
    """current context_fill stub — base-131 rolling hash, bits 1..7"""
    return cf._kites_for(w, ctx)

def kite_letters(w, ctx):
    """lineage_hash: the word's own strut. Context ignored."""
    k = LH.Word(w).box_kite if LH.split_tiers(w)[0] else None
    return (k,) if k else ()

_cc = {}
def kite_descent(w, ctx):
    """PROPOSED: strut of gcd(comp(word), comp(context)). One division.
    Depends on word AND context, and is structural rather than scrambled."""
    cw = _cc.get(w)
    if cw is None:
        cw = _cc[w] = comp(w)
    cx = 1
    for t in ctx:
        ct = _cc.get(t)
        if ct is None:
            ct = _cc[t] = comp(t)
        cx *= ct
    g = math.gcd(cw, cx)
    s = strut_of(g) & 0b0111
    return tuple(k for k in range(1, 8) if s & (1 << (k - 1))) or ()

METHODS = [('hash    ', kite_hash), ('letters ', kite_letters), ('descent ', kite_descent)]

def run(windows, shuffle, seed=7):
    """Return per-method: {word: [kite tuples]}, and elapsed seconds."""
    rng = random.Random(seed)
    res = {name: collections.defaultdict(list) for name, _ in METHODS}
    t = {name: 0.0 for name, _ in METHODS}
    for win in windows:
        for i, w in enumerate(win):
            ctx = win[:i] + win[i+1:]
            if shuffle:
                ctx = rng.sample(toks, len(ctx))       # same size, wrong context
            for name, fn in METHODS:
                t0 = time.perf_counter()
                k = fn(w, ctx)
                t[name] += time.perf_counter() - t0
                res[name][w].append(k)
    return res, t

SAMPLE = windows[:1200]          # 19,200 word-fills per condition
out(f'sampling {len(SAMPLE)} windows = {len(SAMPLE)*WIN} word-fills per condition')
out()

def coherence(hist):
    """Mean over words of: mass of the modal kite-set / total readings.
    1.0 = every reading of this word lit the same channels."""
    vals = []
    for w, ks in hist.items():
        if len(ks) < 4:
            continue
        c = collections.Counter(ks)
        vals.append(c.most_common(1)[0][1] / len(ks))
    return (sum(vals) / len(vals) if vals else float('nan')), len(vals)

for label, shuf in (('CONTROL  (shuffled context)', True), ('REAL     (true context)', False)):
    res, t = run(SAMPLE, shuf)
    out(label)
    for name, _ in METHODS:
        c, n = coherence(res[name])
        us = 1e6 * t[name] / (len(SAMPLE) * WIN)
        out(f'   {name}  coherence={c:.4f}  over {n:5d} repeated words   '
            f'{us:8.1f} us/word   {us*WIN/1000:7.3f} ms/window')
    out()

out('=' * 74)
out('PASS 5d — ONE STRING -> 7 STRINGS   (CALIBRATION)')
out('=' * 74)
out('the pencil: the 7 ways to factor one XOR relation into two others')
for rel in (1, 6, 15):
    facs = [(a, a ^ rel) for a in range(1, 16) if a < (a ^ rel) and (a ^ rel) < 16]
    out(f'  relation {rel:2d} ({rel:04b})  -> {len(facs)} factor pairs  {facs}')
out()
counts = collections.Counter()
for rel in range(1, 16):
    facs = [(a, a ^ rel) for a in range(1, 16) if a < (a ^ rel) and (a ^ rel) < 16]
    counts[len(facs)] += 1
out(f'factor-pair count per relation, over all 15 relations   {dict(counts)}')
out(f'105 incidences / 15 relations = {105//15}')

with open('/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/'
          '2026-08-19_prime_hash_calibration/cal_03_context.out', 'w') as f:
    f.write('\n'.join(R) + '\n')
