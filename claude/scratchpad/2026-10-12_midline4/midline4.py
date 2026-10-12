"""Midline 4-digit code, sign dropped for digits. Code = T S DD (decimal): type, sign, step (2 digits)."""
import math, string, itertools
U, L, D = string.ascii_uppercase, string.ascii_lowercase, string.digits
P = [chr(c) for c in range(0x21, 0x7F) if not chr(c).isalnum()]          # 32, ASCII order
assert len(P) == 32
def code(ch):
    if ch.isupper() or ch.islower():
        t = 0 if ch.isupper() else 1
        pos = (U if t == 0 else L).index(ch); d = pos - 12
        return (t, 0 if d <= 0 else 1, abs(d))                          # step 0 -> sign 0 (canonical)
    if ch.isdigit(): return (2, 0, int(ch))
    i = P.index(ch); return (3, i // 16, i % 16)
def char(t, s, st):
    if t in (0, 1):
        a = U if t == 0 else L
        return a[12 - st] if s == 0 else a[12 + st]
    if t == 2: return str(st)
    return P[s * 16 + st]
def valid(t, s, st):
    if t in (0, 1): return (s == 0 and 0 <= st <= 12) or (s == 1 and 1 <= st <= 13)
    if t == 2: return s == 0 and 0 <= st <= 9
    return t == 3 and s in (0, 1) and 0 <= st <= 15
ALL = [(t, s, st) for t in range(4) for s in range(2) for st in range(16) if valid(t, s, st)]
LIST = [''.join(map(str, (t, s))) + f'{st:02d}' for t, s, st in ALL]     # the 4-digit strings, sorted
CH = [char(*c) for c in ALL]
if __name__ == '__main__':
    assert len(set(LIST)) == len(LIST) == 94 and len(set(CH)) == 94
    for c in CH: assert char(*code(c)) == c and valid(*code(c))           # round trip, every char
    assert sorted(CH) == sorted(chr(x) for x in range(0x21, 0x7F))        # exactly the 94 graphic ASCII
    # also: nothing outside the valid set decodes
    bad = [(t,s,st) for t in range(4) for s in range(2) for st in range(100) if valid(t,s,st) != ((t,s,st) in set(ALL))]
    assert not bad
    # Horner over list indices (base 94): all 94^2 pairs + a long text round trip
    IDX = {c: i for i, c in enumerate(CH)}
    def enc(t):
        a = 0
        for c in t: a = a * 94 + IDX[c]
        return a
    def dec(a, n):
        o = []
        for _ in range(n): a, r = divmod(a, 94); o.append(CH[r])
        return ''.join(reversed(o))
    for a, b in itertools.product(CH, repeat=2): assert dec(enc(a + b), 2) == a + b
    txt = ''.join(open('/home/rendier/Projects/ThePlace/FourthAgePapers/HyperindexingSystem/corpus/pg1001.txt', encoding='utf-8').read().split())
    txt = ''.join(c for c in txt if c in IDX)
    assert dec(enc(txt), len(txt)) == txt
    print(f'ALL TESTS HOLD: {len(LIST)} codes, 94^2 pairs round-trip, {len(txt)}-char Dante (whitespace removed) round-trip')
    print(f'bits/char: 4 decimal digits {math.log2(10000):.2f} | K=128 packing 7.00 | list index base 94 {math.log2(94):.2f} | base-97 {math.log2(97):.2f}')
    print('min/max code:', LIST[0], LIST[-1])
    for t, name in enumerate(['Uppercase', 'Lowercase', 'Digit', 'Punctuation']):
        for s in (0, 1):
            row = [(f'{t}{s}{st:02d}', char(t, s, st)) for (tt, ss, st) in ALL if tt == t and ss == s]
            if row: print(f'{name:11s} sign {s}: ' + ' '.join(f'{c}={ch}' for c, ch in row))
    print('\nindex -> code -> char:')
    for i in range(0, 94, 10): print('  ' + '  '.join(f'{j:2d}:{LIST[j]}={CH[j]}' for j in range(i, min(i + 10, 94))))
