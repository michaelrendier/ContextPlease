"""T7: the permutation content of a string address.
 (a) OrbitCache promises 'cheap integer offset' inside an orbit -- true for a transposition; check the identity.
 (b) exact multiset-permutation rank (orbit = anagram class): address = (count vector, rank in orbit); bits vs naive vs manifold."""
import math, random, importlib.util
from collections import Counter
R='/home/rendier/Projects/ThePlace/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/'
s=importlib.util.spec_from_file_location('ds',R+'hyperwebster.py'); ds=importlib.util.module_from_spec(s); s.loader.exec_module(ds)
hw=ds.HyperWebster(); N=hw.N; idx=hw._char_index
# (a) transposition offset
rnd=random.Random(7); t=''.join(rnd.choice(hw.characters) for _ in range(500))
i,j=17,333; L=len(t)
u=list(t); u[i],u[j]=u[j],u[i]; u=''.join(u)
di,dj=idx[t[i]]+1, idx[t[j]]+1
off=(dj-di)*(N**(L-1-i)) + (di-dj)*(N**(L-1-j))
print("transposition offset identity holds:", hw.point_to_text(u)==hw.point_to_text(t)+off)
# (b) exact multiset permutation rank
def rank(text):
    c=Counter(text); syms=sorted(c,key=lambda ch:idx[ch]); m=len(text)
    P=math.factorial(m)
    for k in c.values(): P//=math.factorial(k)
    r=0
    for ch in text:
        below=sum(c[x] for x in syms if idx[x]<idx[ch])
        r+=P*below//m
        P=P*c[ch]//m; c[ch]-=1; m-=1
    return r
def unrank(r,counts,L):
    c=dict(counts); syms=sorted(c,key=lambda ch:idx[ch]); m=L
    P=math.factorial(m)
    for k in c.values(): P//=math.factorial(k)
    out=[]
    for _ in range(L):
        for x in syms:
            if c[x]==0: continue
            w=P*c[x]//m
            if r<w: out.append(x); P=w; c[x]-=1; m-=1; break
            r-=w
    return ''.join(out)
txt=open('/home/rendier/Projects/ThePlace/Ainulindale/README.md',encoding='utf-8',errors='ignore').read()
txt=''.join(ch for ch in txt if ch in idx)
print(f"{'L':>5} {'naive':>7} {'multinomial':>12} {'+counts(97-vector)':>19} {'total':>7} {'ratio':>6} roundtrip")
for L in (140,1000,4000):
    t=txt[:L]; c=Counter(t); r=rank(t); back=unrank(r,c,L)
    M=math.factorial(L)//math.prod(math.factorial(k) for k in c.values()); mult=M.bit_length()-1+math.log2(M/(1<<(M.bit_length()-1)))
    cnt=math.log2(math.comb(L+N-1,N-1)); tot=mult+cnt; nv=L*math.log2(N)
    print(f"{L:>5} {nv:>7.0f} {mult:>12.0f} {cnt:>19.0f} {tot:>7.0f} {tot/nv:>6.3f} {back==t}")
