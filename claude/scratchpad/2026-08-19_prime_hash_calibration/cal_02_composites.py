#!/usr/bin/env python3
"""cal_02_composites.py — generational COMPOSITES with parentage.

The composite is NOT the spell code. spell() is Horner base-27 (positional,
order-carrying). The composite is the PRODUCT of the letter primes
(multiplicative, order-free, factors back to its parents).

    comp(w) = prod over letters c of LETTER_PRIME[c]

It is deliberately NOT prime. Its whole content is that it factors.

Tests, in order:
  4a  parentage recovery      — factor comp(w), get the letter multiset back
  4b  gcd == shared letters   — the LCA in letter space, one division
  4c  generation profile      — exponent vector over the 4 Fermat bands
  4d  profile vs strut        — how much the OR throws away
  4e  the no-kite class       — words that never reach the division generation
"""
import sys, math, collections, random
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP')
import lineage_hash as LH

R = []
def out(s=''):
    R.append(s); print(s)

LP = LH.LETTER_PRIME
PL = LH.PRIME_LETTER

def comp(word):
    """The generational composite. Order-free, factors back to parents."""
    v = 1
    for c in LH.split_tiers(word)[0]:
        v *= LP[c]
    return v

def parents(n):
    """Factor the composite back to its letter multiset. THE PARENTAGE."""
    out_ = collections.Counter()
    for c in LH.FREQ_ORDER:
        p = LP[c]
        while n % p == 0:
            n //= p
            out_[c] += 1
    return out_, n          # n == 1 means fully accounted for

def profile(word):
    """Exponent vector over the 4 Fermat generations. A multiset, not a set."""
    v = [0, 0, 0, 0]
    for c in LH.split_tiers(word)[0]:
        v[LH.generation(LP[c])] += 1
    return tuple(v)

words = []
with open('/usr/share/dict/words', encoding='utf-8', errors='ignore') as f:
    for line in f:
        w = line.strip()
        if w and w.isalpha() and w.isascii():
            words.append(w.lower())
words = sorted(set(words))

out('=' * 74)
out('PASS 4a — PARENTAGE RECOVERY   (CALIBRATION)')
out('=' * 74)
out(f'corpus  {len(words)} words')
ok = bad = 0
maxbits = 0
for w in words:
    c = comp(w)
    par, rem = parents(c)
    truth = collections.Counter(LH.split_tiers(w)[0])
    maxbits = max(maxbits, c.bit_length())
    if rem == 1 and par == truth:
        ok += 1
    else:
        bad += 1
out(f'composite factors back to exact letter multiset   {ok}/{len(words)}')
out(f'failures                                          {bad}')
out(f'largest composite                                 {maxbits} bits')
out(f'is the composite prime?  (it must not be)         '
    f'{sum(1 for w in random.Random(0).sample(words, 500) if LH._is_prime(comp(w)))}/500 prime')
out()

out('=' * 74)
out('PASS 4b — gcd IS THE SHARED-LETTER LCA   (CALIBRATION)')
out('=' * 74)
rng = random.Random(1)
pairs = [(rng.choice(words), rng.choice(words)) for _ in range(20000)]
agree = 0
for a, b in pairs:
    g = math.gcd(comp(a), comp(b))
    got, rem = parents(g)
    ca, cb = collections.Counter(LH.split_tiers(a)[0]), collections.Counter(LH.split_tiers(b)[0])
    want = collections.Counter({k: min(ca[k], cb[k]) for k in set(ca) & set(cb)})
    want = collections.Counter({k: v for k, v in want.items() if v})
    if rem == 1 and got == want:
        agree += 1
out(f'gcd(comp a, comp b) == componentwise-min letter multiset   {agree}/{len(pairs)}')
out('  (one division; no tree walk, no search)')
out()

out('=' * 74)
out('PASS 4c/4d — GENERATION PROFILE vs THE STRUT   (RESULT)')
out('=' * 74)
prof = collections.Counter()
strut = collections.Counter()
joint = collections.Counter()
for w in words:
    p = profile(w)
    s = LH.Word(w).strut
    prof[p] += 1; strut[s] += 1; joint[(p, s)] += 1

def H(counter):
    t = sum(counter.values())
    return -sum((n/t) * math.log2(n/t) for n in counter.values() if n)

out(f'distinct generation profiles (multiset)   {len(prof)}')
out(f'distinct struts (set / OR)                {len(strut)}')
out(f'H(profile)   {H(prof):7.4f} bits')
out(f'H(strut)     {H(strut):7.4f} bits')
out(f'H(profile) - H(strut)  =  {H(prof) - H(strut):.4f} bits DISCARDED by the OR')
out(f'ratio kept by the strut                   {H(strut)/H(prof):.4f}')
out()
out('top 12 generation profiles  (ranking, factors, GROUPING, division)')
for p, n in prof.most_common(12):
    out(f'  {p}   {n:6d}  {100*n/len(words):5.2f}%')
out()

out('=' * 74)
out('PASS 4e — THE NO-KITE CLASS   (RESULT)')
out('=' * 74)
pre = [w for w in words if LH.Word(w).box_kite is None]
out(f'words with no box kite   {len(pre)}  ({100*len(pre)/len(words):.2f}%)')
alpha = sorted({c for w in pre for c in LH.split_tiers(w)[0]})
out(f'alphabet they are built from   {"".join(alpha)}')
out(f'that alphabet == the 7 letters below the division band?  '
    f'{alpha == sorted(c for c in LH.FREQ_ORDER if LH.generation(LP[c]) < 3)}')
out(f'those 7 letters, frequency-ordered   '
    f'{"".join(c for c in LH.FREQ_ORDER if LH.generation(LP[c]) < 3)}')
out()
out(f'longest no-kite words  {sorted(pre, key=len, reverse=True)[:8]}')
out(f'sample                 {pre[::len(pre)//12][:12]}')

with open('/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/'
          '2026-08-19_prime_hash_calibration/cal_02_composites.out', 'w') as f:
    f.write('\n'.join(R) + '\n')
