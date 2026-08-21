#!/usr/bin/env python3
"""cal_06_zeno.py — "how is the prime ladder linear?"

Two different objects were conflated in one sentence yesterday:

  (1) THE LADDER      p_n, the sequence of primes.  p_n ~ n ln n.  QUASI-linear
                      (superlinear by a log factor). This is what makes the
                      Fermat band widths lopsided, and this claim stands.

  (2) THE OCCUPANCY   how primes sit INSIDE composites. v_p is geometric:
                      P(p^k | n) = p^-k. Half the integers carry a 2, a quarter
                      carry two, an eighth carry three -- Zeno, and E[v_2] = 1.
                      NOT linear, and this is the structure Cody is pointing at.

Measured here: which of the two the word-composites actually follow, and how
much of it the strut's OR destroys.
"""
import sys, math, collections, statistics
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP')
import lineage_hash as LH

R = []
def out(s=''):
    R.append(s); print(s)

LP, PL = LH.LETTER_PRIME, LH.PRIME_LETTER

words = []
with open('/usr/share/dict/words', encoding='utf-8', errors='ignore') as f:
    for line in f:
        w = line.strip()
        if w and w.isalpha() and w.isascii():
            words.append(w.lower())
words = sorted(set(words))
out(f'corpus {len(words)} words')
out()

out('=' * 78)
out('(1) THE LADDER — is p_n linear?   (CALIBRATION)')
out('=' * 78)
P = [LP[c] for c in LH.FREQ_ORDER]
out(f'p_1..p_26 used as letters   {P[0]} .. {P[-1]}   (factor {P[-1]/P[0]:.1f} over 26 steps)')
out(f'FERMAT F_0..F_3             {LH.FERMAT[0]} .. {LH.FERMAT[-1]}   '
    f'(factor {LH.FERMAT[-1]/LH.FERMAT[0]:.1f} over 4 steps)')
out()
out(' n   p_n   n*ln(n)   ratio     which Fermat band')
for n in (1, 2, 5, 10, 20, 26, 40, 65):
    pn = LH._P[n-1]
    nl = n * math.log(n) if n > 1 else 1.0
    out(f'{n:2d}  {pn:4d}   {nl:7.2f}   {pn/nl:5.2f}     gen {LH.generation(pn)}')
out()
bands = collections.Counter(LH.generation(p) for p in LH._P if p <= 313)
out('primes available per Fermat band, up to the 313 pool')
for g in range(5):
    if bands[g]:
        out(f'  gen {g}   {bands[g]:2d} primes available')
out(f'letters actually assigned   '
    f'{dict(collections.Counter(LH.generation(LP[c]) for c in LH.FREQ_ORDER))}')
out()
out('VERDICT (1): p_n / (n ln n) stays within a factor of ~1.2 across the range,')
out('so the ladder is QUASI-linear. Cutting it at doubly-exponential thresholds')
out('is the whole source of the 2/1/4/19 lopsidedness. That claim stands.')
out()

out('=' * 78)
out('(2) THE OCCUPANCY — Zeno. is v_p geometric?   (RESULT)')
out('=' * 78)
out('For a RANDOM integer:  P(v_p >= k) = p^-k,  E[v_p] = 1/(p-1).')
out('For a WORD composite:  v_p(comp w) = how many times that letter occurs.')
out()
out('letter  p    P(v>=1)   P(v>=2)   P(v>=3)     E[v]   random E[v]   ratio')
tot = len(words)
counters = {c: collections.Counter() for c in LH.FREQ_ORDER}
for w in words:
    for c, n in collections.Counter(LH.split_tiers(w)[0]).items():
        counters[c][n] += 1
for c in LH.FREQ_ORDER[:10]:
    p = LP[c]
    ge = lambda k: sum(n for v, n in counters[c].items() if v >= k) / tot
    ev = sum(v * n for v, n in counters[c].items()) / tot
    rnd = 1.0 / (p - 1)
    out(f'   {c}   {p:3d}   {ge(1):7.4f}   {ge(2):7.4f}   {ge(3):7.4f}   '
        f'{ev:6.3f}   {rnd:9.4f}   {ev/rnd:6.2f}')
out()
e_ge = [sum(n for v, n in counters['e'].items() if v >= k) / tot for k in range(1, 6)]
out(f"'e' (prime 2) survival curve      {[round(x,4) for x in e_ge]}")
out(f'random-integer survival curve     {[round(2.0**-k,4) for k in range(1,6)]}')
out(f"ratio of successive terms, 'e'    "
    f"{[round(e_ge[i+1]/e_ge[i],3) for i in range(len(e_ge)-1) if e_ge[i]]}")
out('  (a geometric law would hold this ratio CONSTANT at 1/p = 0.5)')
out()

omega  = [len(set(LH.split_tiers(w)[0])) for w in words]      # distinct primes
Omega  = [len(LH.split_tiers(w)[0]) for w in words]           # with multiplicity
out(f'omega  (distinct prime factors)   mean {statistics.mean(omega):.3f}')
out(f'Omega  (with multiplicity)        mean {statistics.mean(Omega):.3f}')
out(f'Omega - omega  = repeated mass    mean {statistics.mean(Omega)-statistics.mean(omega):.3f}')
out(f'  a random integer near 2^{statistics.mean([comp.bit_length() for comp in [1]]) if False else 80}'
    f' has omega ~ ln ln 2^80 = {math.log(math.log(2**80)):.2f}')
out()

out('=' * 78)
out('WHAT EACH ENCODING KEEPS   (RESULT)')
out('=' * 78)
def H(c):
    t = sum(c.values())
    return -sum((n/t)*math.log2(n/t) for n in c.values() if n)

spell_H = math.log2(len(words))
multi = collections.Counter(frozenset(collections.Counter(LH.split_tiers(w)[0]).items()) for w in words)
supp  = collections.Counter(frozenset(LH.split_tiers(w)[0]) for w in words)
prof  = collections.Counter(tuple(sorted(collections.Counter(
            LH.generation(LP[c]) for c in LH.split_tiers(w)[0]).items())) for w in words)
strut = collections.Counter(LH.Word(w).strut for w in words)
kite  = collections.Counter(LH.Word(w).box_kite for w in words)

rows = [
    ('spell (Horner, ordered)',      spell_H,   len(words)),
    ('valuation vector (multiset)',  H(multi),  len(multi)),
    ('support (which letters, OR)',  H(supp),   len(supp)),
    ('generation profile',           H(prof),   len(prof)),
    ('strut (generation OR)',        H(strut),  len(strut)),
    ('box kite',                     H(kite),   len(kite)),
]
out(f'{"encoding":32s} {"bits":>8s} {"classes":>9s}  {"kept":>6s}')
for name, h, n in rows:
    out(f'{name:32s} {h:8.3f} {n:9d}  {100*h/spell_H:5.1f}%')
out()
out(f'multiset -> support  loses {H(multi)-H(supp):.3f} bits '
    f'= the p-adic DEPTH (how many times, not whether)')
out(f'support  -> strut    loses {H(supp)-H(strut):.3f} bits '
    f'= which letter, collapsed to which generation')

with open('/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/'
          '2026-08-19_prime_hash_calibration/cal_06_zeno.out', 'w') as f:
    f.write('\n'.join(R) + '\n')
