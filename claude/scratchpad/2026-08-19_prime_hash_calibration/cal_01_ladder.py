#!/usr/bin/env python3
"""cal_01_ladder.py — CALIBRATION pass 1-3 of the box-kite prime hash.

CALIBRATION, not RESULT: this tests the pipeline (the ladder, the letter map,
the spell bijection) and the distribution the encoder actually produces. No
hypothesis is under test yet.

Nothing is interpreted in a print statement. Numbers out; judgement after.
"""
import sys, math, collections
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP')

import lineage_hash as LH
import prime_hash as PH

R = []
def out(s=''):
    R.append(s); print(s)

# ══════════════════════════════════════════════════════════════════════
out('=' * 74)
out('PASS 1 — THE FERMAT LADDER  (CALIBRATION)')
out('=' * 74)

F = LH.FERMAT
out(f'FERMAT               {F}')
out(f'prod                 {math.prod(F)}')
out(f'2^16 - 1             {2**16 - 1}')
out(f'prod == 2^16-1       {math.prod(F) == 2**16 - 1}')

subs = [s for n in range(1, 16) for s in [[F[i] for i in range(4) if n >> i & 1]]]
out(f'nonempty subsets     {len(subs)}')
with257 = [s for s in subs if 257 in s]
out(f'  containing 257     {len(with257)}')
out(f'  minus no-free-bit  {len(with257) - 1}')

# F_n = 2^(2^n)+1 check
out(f'F_n == 2^(2^n)+1     {[2**(2**n)+1 for n in range(4)] == F}')
out()

# ══════════════════════════════════════════════════════════════════════
out('=' * 74)
out('PASS 2 — THE LETTER MAP  (CALIBRATION)')
out('=' * 74)
out(f'LETTER_CAP  lineage_hash  {LH.LETTER_CAP}   pool={len(LH.LETTER_POOL)}   '
    f'CONTEXT_PRIMES[0]={LH.CONTEXT_PRIMES[0]}')
out(f'LETTER_CAP  prime_hash    {PH.LETTER_CAP}   pool={len(PH.LETTER_PRIMES)}   '
    f'CONTEXT_PRIMES[0]={PH.CONTEXT_PRIMES[0]}')
out()
out('letter  prime  gen   generation-name')
gen_hist = collections.Counter()
letters_used = []
for c in LH.FREQ_ORDER:
    p = LH.LETTER_PRIME[c]
    g = LH.generation(p)
    gen_hist[g] += 1
    letters_used.append(p)
    out(f'   {c}     {p:4d}   {g}    {LH.GENERATION[g] if g < 4 else "OUT-OF-BAND"}')
out()
out(f'max letter prime actually used   {max(letters_used)}')
out(f'prime_hash LETTER_CAP            {PH.LETTER_CAP}')
out(f'letters above prime_hash cap     '
    f'{[(c, LH.LETTER_PRIME[c]) for c in LH.FREQ_ORDER if LH.LETTER_PRIME[c] > PH.LETTER_CAP]}')
out()
out('generation histogram over the 26 letters')
for g in range(5):
    if gen_hist[g]:
        pct = 100 * gen_hist[g] / 26
        out(f'  gen {g} ({LH.GENERATION[g] if g<4 else "OOB":>9s})  {gen_hist[g]:3d}  {pct:5.1f}%')
out()

# ══════════════════════════════════════════════════════════════════════
out('=' * 74)
out('PASS 3 — SPELL BIJECTION + STRUT DISTRIBUTION OVER A REAL CORPUS')
out('=' * 74)

words = []
with open('/usr/share/dict/words', encoding='utf-8', errors='ignore') as f:
    for line in f:
        w = line.strip()
        if w and w.isalpha() and w.isascii():
            words.append(w.lower())
words = sorted(set(words))
out(f'corpus  /usr/share/dict/words   {len(words)} distinct [a-z]+ words')

spells = {}
coll = []
overflow = 0
struts = collections.Counter()
kites = collections.Counter()
lineages = collections.Counter()
for w in words:
    W = LH.Word(w)
    if len(W.letters) > 13:
        overflow += 1
    if W.spell in spells and spells[W.spell] != W.letters:
        coll.append((spells[W.spell], W.letters))
    spells[W.spell] = W.letters
    struts[W.strut] += 1
    kites[W.box_kite] += 1
    lineages[W.lineage] += 1

out(f'distinct spell codes             {len(spells)}')
out(f'spell collisions                 {len(coll)}')
out(f'words > 13 letters (uint64 OOB)  {overflow}')
rt = sum(1 for v, l in spells.items() if LH.Word.unspell(v) == l)
out(f'unspell round-trip               {rt}/{len(spells)}')
out()
out('STRUT distribution   (bit0=ranking bit1=factors bit2=GROUPING bit3=division)')
for s, n in sorted(struts.items()):
    out(f'  {s:04b}  {s:2d}   {n:7d}   {100*n/len(words):6.2f}%')
out()
out('BOX KITE distribution   (strut & 0b0111, division bit forced)')
for k, n in sorted(kites.items(), key=lambda x: (x[0] is None, x[0])):
    out(f'  {str(k):>4s}   {n:7d}   {100*n/len(words):6.2f}%')
out()

def entropy(counter, total):
    return -sum((n/total) * math.log2(n/total) for n in counter.values() if n)

out(f'H(strut)     {entropy(struts, len(words)):.4f} bits   (max {math.log2(len(struts)):.4f})')
out(f'H(box_kite)  {entropy(kites, len(words)):.4f} bits   (max {math.log2(len(kites)):.4f})')
out(f'H(lineage)   {entropy(lineages, len(words)):.4f} bits   '
    f'over {len(lineages)} distinct ordered lineages')
out()
out(f'words with NO box kite (never reach division gen)  {kites.get(None, 0)}')

with open('/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/'
          '2026-08-19_prime_hash_calibration/cal_01_ladder.out', 'w') as f:
    f.write('\n'.join(R) + '\n')
