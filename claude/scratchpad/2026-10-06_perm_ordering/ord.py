import sys, math, random, re, collections
from fractions import Fraction
sys.path.insert(0,'/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-10-02_ptolemy_json_poc')
import hyperindex as H, ptolemy_poc as P
R='/home/rendier/Projects/ThePlace/FourthAgePapers/HyperindexingSystem/'
def bits_exact(t, perm): return H.address(t, perm).bit_length()
def pen(t, perm, K=40):
    """analytic: log2(A+1) - n*log2(N), from leading K digits only"""
    N=len(perm); idx={c:i for i,c in enumerate(perm)}
    f=Fraction(1,N-1)+sum(Fraction(idx[c],N**(i+1)) for i,c in enumerate(t[:K]))
    return math.log2(f)
def orders(S, freq, starts):
    S=list(S); o={}
    o['code-point']=sorted(S)
    o['freq desc']=sorted(S,key=lambda c:(-freq[c],c))
    o['freq asc']=sorted(S,key=lambda c:(freq[c],c))
    txt=lambda c:c.isalnum() or c==' '
    o['text first']=sorted(S,key=lambda c:(not txt(c),-freq[c],c))
    o['punct first']=sorted(S,key=lambda c:(txt(c),-freq[c],c))
    o['chunk-start freq']=sorted(S,key=lambda c:(-starts[c],-freq[c],c))
    rs=[]
    for s in range(20):
        r=S[:]; random.Random(s).shuffle(r); rs.append(r)
    return o, rs
def run(name, text, chunks):
    S=sorted(set(text)); N=len(S)
    freq=collections.Counter(text); starts=collections.Counter(c[0] for c in chunks)
    o,rs=orders(S,freq,starts)
    H0=-sum(v/len(text)*math.log2(v/len(text)) for v in freq.values())
    print(f'\n== {name}: {len(text)} chars, N={N}, log2N={math.log2(N):.2f} b/char, entropy={H0:.2f} b/char, {len(chunks)} chunks')
    print(f'   {"ordering":18s} {"whole-doc bits":>15s}  {"mean pen/chunk":>15s}')
    sample=text[:60000]
    for k,p in o.items():
        wb=bits_exact(sample,p); an=len(sample)*math.log2(N)+pen(sample,p)
        pm=sum(pen(c,p) for c in chunks)/len(chunks)
        print(f'   {k:18s} {wb-len(sample)*math.log2(N):+15.2f}  {pm:+15.2f}   (analytic check {an-len(sample)*math.log2(N):+.2f})')
    ps=[sum(pen(c,p) for c in chunks)/len(chunks) for p in rs]
    print(f'   {"random x20":18s} {"":>15s}  {sum(ps)/20:+15.2f}   (min {min(ps):+.2f}, max {max(ps):+.2f})')
# Dante, stanza chunks
d=P.dante(R+'corpus/pg1001.txt'); run('Dante (stanzas)', d, P.stanza(d))
# Jupiter html, 1000-char chunks
j=open(R+'reengineer/Jupiter.html',encoding='utf-8').read(); run('Jupiter.html (1000-char chunks)', j, [j[i:i+1000] for i in range(0,len(j),1000)])
# json rows: entries built from Dante lines
rows=[P.entry(H.address(l,H.load_perm('/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-10-02_ptolemy_json_poc/perm/ascii.perm')),len(l),'20261006','ascii') for l in d.splitlines(keepends=True)[:600]]
run('JSON entries (600 rows)', ''.join(rows), rows)
