import sys, collections, csv, pickle, random, math
sys.path.insert(0,'/home/rendier/Projects/ThePlace/VAPMIP/SemPriCon/tools')
import ptol_bin, numpy as np
S='/tmp/claude-1000/-home-rendier-Projects-ThePlace/454aab1b-b2b4-4cfd-990e-e1d3a910b0fa/scratchpad/'
cnt,sl=pickle.load(open(S+'en1.pkl','rb'))
d=ptol_bin.load('clean/archive/v1.0/test_english_v1.0.bin')
dom={s:max(x)[1] for s,x in sl.items()}
def addr(w):
    v=0
    for c in w: v=(v*95+(ord(c)-31))&((1<<64)-1)
    if v>0:v-=1
    return (((v*0x9E3779B97F4A7C15)&((1<<64)-1))*25000)>>64
adj=collections.defaultdict(dict)
for i,j,w in d['edges']: adj[int(i)][int(j)]=w
rows=list(csv.DictReader(open('calibration/calibration_v1_en_zh.tsv',encoding='utf-8'),delimiter='\t'))
by=collections.defaultdict(dict)
for r in rows: by[r['pair']][r['half']]=r['en_us']
pairs=[(v['S'],v['L']) for v in by.values() if 'S' in v and 'L' in v]
print('pairs',len(pairs))
ds=[abs(addr(a)-addr(b))/25000 for a,b in pairs]
print('|dslot|/N quartiles',np.quantile(ds,[.25,.5,.75]).round(4),'(triangle: 0.134 0.293 0.5)')
print('within 1%: ',sum(x<.01 for x in ds),' expected ~',round(len(ds)*0.0199,1))
# edge-neighbourhood overlap: top-50 strongest edge targets by weight (exclude hubs)
deg=collections.Counter()
for s,m in adj.items():
    for j in m: deg[j]+=1
def top(s,k=60):
    m=adj.get(s,{}); return set(j for j,_ in sorted(m.items(),key=lambda x:-x[1]/ (deg[x[0]]**.5))[:k])
def jac(a,b):
    A,B=top(addr(a)),top(addr(b)); return len(A&B)/max(1,len(A|B))
J=[jac(a,b) for a,b in pairs]
random.seed(1); words=[w for p in pairs for w in p]
R=[jac(random.choice(words),random.choice(words)) for _ in range(5000)]
print('edge-neighbourhood Jaccard, same-synset pairs: mean %.4f median %.4f ; random pairs: mean %.4f median %.4f'%(np.mean(J),np.median(J),np.mean(R),np.median(R)))
print('pairs with Jaccard > 95th pct of random:',sum(j>np.quantile(R,.95) for j in J),'of',len(J),'(chance 5%%=%.0f)'%(len(J)*.05))
best=sorted(zip(J,pairs),reverse=True)[:12]; print([(round(j,2),a,b) for j,(a,b) in best])
# nearest-in-slot among frequent words
top3000=[t for t,c in cnt.most_common(3000) if len(t)>=2]
srt=sorted((addr(t),t) for t in top3000)
close=[(srt[i+1][0]-srt[i][0],srt[i][1],srt[i+1][1]) for i in range(len(srt)-1)]
close.sort(); print('closest-in-slot pairs among the 3000 most frequent words:',[(g,a,b) for g,a,b in close[:25]])
random.seed(7)
print('random +-3 slot neighbourhoods (most-frequent token per slot):')
for s in random.sample(sorted(dom),8): print(s,[dom.get(k) for k in range(s-3,s+4)])
