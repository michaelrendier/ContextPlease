import sys, collections, csv, pickle, random, math
sys.path.insert(0,'/home/rendier/Projects/ThePlace/VAPMIP/SemPriCon/tools')
import ptol_bin, numpy as np
S='/tmp/claude-1000/-home-rendier-Projects-ThePlace/454aab1b-b2b4-4cfd-990e-e1d3a910b0fa/scratchpad/'
cnt,sl=pickle.load(open(S+'en1.pkl','rb'))
d=ptol_bin.load('clean/archive/v1.0/test_english_v1.0.bin')
label={i:w for i,w,*_ in d['vocab']}; Ev={i:E for i,w,E,*_ in d['vocab']}
dom={s:max(x)[1] for s,x in sl.items()}
tot=sum(c for s,x in sl.items() for c,t in x)
lab_ok=sum(1 for s in dom if label.get(s)==dom[s]); print('slots where label == most frequent token:',lab_ok,'of',len(dom))
mass_ok=sum(c for s,x in sl.items() for c,t in x if label.get(s)==t); print('corpus token mass whose word is the label: %.3f'%(mass_ok/tot))
mass_dom=sum(max(x)[0] for x in sl.values()); print('mass held by dominant token per slot %.3f'%(mass_dom/tot))
edges=d['edges']; print(len(edges), edges['w'][:5], 'w quantiles',np.quantile(edges['w'],[0,.5,.9,.99,1]))
adj=collections.defaultdict(dict)
for i,j,w in edges: adj[int(i)][int(j)]=w; 
def addr(w):
    v=0
    for c in w: v=(v*95+(ord(c)-31))&((1<<64)-1)
    if v>0:v-=1
    return (((v*0x9E3779B97F4A7C15)&((1<<64)-1))*25000)>>64
def nb(w,k=15):
    s=addr(w); items=sorted(adj[s].items(),key=lambda x:-x[1])[:k]
    return [(dom.get(j,label.get(j)),round(x,2)) for j,x in items]
for w in ['valence','hydrogen','cognition','knowledge','tree','water']:
    print(w,addr(w),'E=%.4f'%Ev.get(addr(w),0)); print('  ',nb(w))
a=set(j for j in adj[addr('valence')]); b=set(j for j in adj[addr('hydrogen')]); print('shared edge targets valence/hydrogen',len(a&b),len(a),len(b),[dom.get(j) for j in list(a&b)[:30]])
