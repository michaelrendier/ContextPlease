import os, sys, time, shutil, re
sys.path.insert(0, '.')
import ptolemy_poc as P
assert not re.search(r'hashlib|sha\d|md5', open('hyperindex.py').read() + open('ptolemy_poc.py').read(), re.I)
TXT = P.dante('../../../../FourthAgePapers/HyperindexingSystem/corpus/pg1001.txt')
TS = '2026-10-02T00:00:00Z'
print('corpus: %d chars, %d symbols (normalised Longfellow Inferno)' % (len(TXT), len(set(TXT))))
print('%-10s %6s %9s %9s %9s %9s %7s %7s' % ('chunking','rows','ROWS B','TABLES B','ptolemy B','x corpus','ingest s','recon s'))
for name, f in P.CHUNKERS.items():
    d = 'out/' + name; shutil.rmtree(d, ignore_errors=True); os.makedirs(d); top = d + '/ptolemy.json'
    t0 = time.time(); r, tb = P.ingest(top, TXT, f, TS); t1 = time.time()
    docs = P.reconstruct(top); t2 = time.time()
    assert docs == [TXT], name                       # zero loss
    sz = os.path.getsize(top)
    print('%-10s %6d %9d %9d %9d %9.2f %7.1f %7.1f' % (name, len(f(TXT)), r, tb, sz, sz / len(TXT), t1 - t0, t2 - t1))
# repeated ingest into ONE ptolemy.json, twice with the fixed clock -> byte-identical; history check
runs = []
for k in (1, 2):
    d = 'out/chain%d' % k; shutil.rmtree(d, ignore_errors=True); os.makedirs(d); top = d + '/ptolemy.json'
    tops = []
    for name in ('whole', 'canto', 'stanza', 'fixed1000'):
        P.ingest(top, TXT, P.CHUNKERS[name], TS); tops.append(open(top).read())
    runs.append(open(top).read())
assert runs[0] == runs[1]
print('chain of 4 ingests: file bytes identical across two runs; ptolemy.json = %d B; all 4 tops distinct: %s'
      % (len(runs[0]), len(set(tops)) == 4))
docs = P.reconstruct('out/chain2/ptolemy.json')
assert docs == [TXT] * 4
print('reconstructed 4 documents from ptolemy.json alone: all equal to corpus')
# past top from the final one: TABLES prefix property
final = P.load_tables('out/chain2/ptolemy.json'); ents = P.parse(final)
import hyperindex as H
pre = ''.join(P.entry(*e[:2], e[2], e[3]) for e in ents[:2])
a = H.address(pre, P.perm('json'))
print('prefix (first 2 of 4 TABLES entries) re-addressed: %d digits, equals a recorded past TOP: %s'
      % (len(str(a)), str(a) in [P.parse(t)[0][0].__str__() for t in tops]))
