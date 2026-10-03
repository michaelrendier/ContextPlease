"""Freeze json.perm: the characters canonical entries can contain, ordered by frequency (ties: code point)."""
import collections, sys
sys.path.insert(0,'.')
import ptolemy_poc as P, hyperindex as H
TS = '2026-10-02T00:00:00Z'
vocab = set('{}":,\n0123456789-T' + 'Z' + 'HYPERINDEXDATALNGTMSIPz' + 'ascii' + 'json')
prov = sorted(vocab)
open('perm/_prov.perm','w').write(''.join('%02X\n' % ord(c) for c in prov))
P.PERMS['json'] = H.load_perm('perm/_prov.perm')
t = P.dante('../../../../FourthAgePapers/HyperindexingSystem/corpus/pg1001.txt')
cnt = collections.Counter()
for name in ('whole', 'canto', 'stanza'):
    rows = ''.join(P.entry(H.address(c, P.ASCII), len(c), TS, 'ascii') for c in P.CHUNKERS[name](t))
    tables = P.entry(H.address(rows, P.PERMS['json']), len(rows), TS, 'json')
    cnt.update(rows); cnt.update(tables)
assert set(cnt) <= vocab, set(cnt) - vocab
order = sorted(vocab, key=lambda c: (-cnt[c], ord(c)))
with open('perm/json.perm', 'w') as f:
    f.write('# json.perm: characters of the canonical ptolemy/TABLES/ROWS .json entries, most frequent first\n')
    f.write('# frequency measured on whole/canto/stanza ingests of Longfellow Inferno (normalised); ties by code point\n')
    f.write('# one code point per line, hex; position in this file = digit value\n')
    for c in order: f.write('%02X   # %-5s %d\n' % (ord(c), repr(c), cnt[c]))
print(len(order), ''.join(order).replace('\n', '\\n'))
