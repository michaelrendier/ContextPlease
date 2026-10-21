import sys, collections, csv, re
sys.path.insert(0,'/home/rendier/Projects/ThePlace/VAPMIP/SemPriCon/tools')
import ptol_bin
M=(1<<64)-1; PHI=0x9E3779B97F4A7C15; N=25000
def addr(w):
    v=0
    for c in w: v=(v*95+(ord(c)-31))&M
    if v>0: v-=1
    s=(v*PHI)&M
    return (s*N)>>64, v
d=ptol_bin.load('clean/archive/v1.0/test_english_v1.0.bin')
V=d['vocab']; byslot={i:w for i,w,E,*_ in V}
print('vocab',len(V),'slots labelled',len(byslot))
bad=[w for i,w,*_ in V if addr(w)[0]!=i]; print('label address mismatches',len(bad),bad[:5])
beta=d['beta']
# distinct tokens in corpus
cnt=collections.Counter()
for l in open('corpora/text/en_v1.txt',encoding='utf-8'):
    for t in re.findall(r"[a-z']+",l.lower()): cnt[t]+=1
print('distinct tokens in corpus',len(cnt),'total',sum(cnt.values()))
sl=collections.defaultdict(list)
for t,c in cnt.items():
    if len(t)>=2: sl[addr(t)[0]].append((c,t))
print('slots reached',len(sl),'tokens>=2',sum(len(x) for x in sl.values()))
occ=collections.Counter(len(x) for x in sl.values()); print('slot occupancy hist',sorted(occ.items())[:15])
import pickle; pickle.dump((cnt,dict(sl)),open('/tmp/claude-1000/-home-rendier-Projects-ThePlace/454aab1b-b2b4-4cfd-990e-e1d3a910b0fa/scratchpad/en1.pkl','wb'))
for w in ['valence','hydrogen','tree','water','knowledge','cognition','act','deed']:
    s,v=addr(w); print(w,s,'label:',byslot.get(s),'count',cnt.get(w),'sharing',sorted(sl.get(s,[]),reverse=True)[:6])
for w in ['valence','hydrogen']:
    s=addr(w)[0]
    print(w,'neighbours', [(k,byslot.get(k)) for k in range(s-6,s+7)])
print(addr('valence')[1]-addr('hydrogen')[1])
