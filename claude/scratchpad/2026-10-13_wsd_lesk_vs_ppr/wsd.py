"""Lesk vs most-frequent-sense vs personalised PageRank over the WordNet graph (typed edges, undirected). Scratch, offline."""
import numpy as np, scipy.sparse as sp, time
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
t0=time.time()
syn=list(wn.all_synsets()); ix={s:i for i,s in enumerate(syn)}; n=len(syn)
RELS=['hypernyms','instance_hypernyms','hyponyms','instance_hyponyms','member_holonyms','substance_holonyms','part_holonyms','member_meronyms','substance_meronyms','part_meronyms','attributes','entailments','causes','also_sees','verb_groups','similar_tos','topic_domains','region_domains','usage_domains']
r=[];c=[]
for s in syn:
    for m in RELS:
        for t in getattr(s,m)():
            r+= [ix[s],ix[t]]; c+= [ix[t],ix[s]]
A=sp.csr_matrix((np.ones(len(r)),(r,c)),shape=(n,n)); A.data[:]=1
d=np.asarray(A.sum(1)).ravel(); d[d==0]=1
P=sp.diags(1/d)@A            # row-stochastic
print("graph: %d synsets, %d directed edges, built in %.1fs"%(n,A.nnz,time.time()-t0))
def ppr(seed_idx,alpha=0.85,it=30):
    v=np.zeros(n); v[seed_idx]=1/len(seed_idx); x=v.copy()
    for _ in range(it): x=alpha*(P.T@x)+(1-alpha)*v
    return x
def wsd_ppr(words,target,pos='n'):
    seeds=[ix[s] for w in words if w!=target for s in wn.synsets(w)]
    if not seeds: return None
    x=ppr(seeds); cands=wn.synsets(target,pos)
    return max(cands,key=lambda s:x[ix[s]])
cases=[("neutron generation in different reactor types","reactor"),("neutron generation in different reactor types","generation"),
("the first reactor was built after neutrons were discovered","reactor"),("he sat on the bank of the river and fished","bank"),
("she deposited money at the bank","bank"),("the plant needs water and sunlight to grow","plant"),("the plant produces electricity from nuclear fission","plant")]
for sent,w in cases:
    toks=sent.split(); t=time.time()
    pp=wsd_ppr(toks,w); dt=(time.time()-t)*1000
    L=lesk(toks,w,'n'); print(f"{w:10s} PPR={pp.name() if pp else None:30s} lesk={L.name() if L else None:26s} ({dt:.0f} ms) | {sent}")
