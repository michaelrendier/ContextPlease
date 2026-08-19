"""TEST 4b — proper 1:1 lexical matching + partial correlation."""
import pickle, numpy as np
from collections import Counter, defaultdict
from itertools import combinations

d = pickle.load(open('/home/rendier/Projects/ThePlace/VAPMIP/monad_sedenion_addresses.pkl','rb'))
book = d['book']
names, vecs = [], []
for nm, ent in book.items():
    v = ent.get('sedenion') if isinstance(ent, dict) else ent
    if v is None or len(v) != 16: continue
    names.append(nm); vecs.append(np.asarray(v, float))
V = np.array(vecs); V[:,0] = 0.0
V /= np.clip(np.linalg.norm(V,axis=1,keepdims=True),1e-12,None)
N = len(names)
def tri(s):
    s=f"  {s}  "; return Counter(s[i:i+3] for i in range(len(s)-2))
TRI=[tri(n) for n in names]; MOD=['.'.join(n.split('.')[:2]) for n in names]
def tsim(a,b):
    return sum((a&b).values())/np.sqrt(sum(a.values())*sum(b.values()))

groups=defaultdict(list)
for i,m in enumerate(MOD): groups[m].append(i)
groups={g:ix for g,ix in groups.items() if len(ix)>=4}

rng=np.random.default_rng(3)
same_pairs=[]
for g,ix in groups.items():
    ps=list(combinations(ix,2))
    if len(ps)>400: ps=[ps[k] for k in rng.choice(len(ps),400,replace=False)]
    same_pairs+=ps
print(f"{len(same_pairs):,} same-module pairs")

# pool of cross-module pairs, indexed by lexical similarity
P=300_000
I=rng.integers(0,N,P); J=rng.integers(0,N,P)
m=np.array([MOD[i]!=MOD[j] and i!=j for i,j in zip(I,J)])
I,J=I[m],J[m]
lexD=np.array([tsim(TRI[i],TRI[j]) for i,j in zip(I,J)])
addrD=(V[I]*V[J]).sum(1)
order=np.argsort(lexD); lexD,addrD=lexD[order],addrD[order]
print(f"{len(I):,} cross-module pairs in the matching pool")
print(f"lexical sim range: same-module pool vs cross pool\n")

lexS=np.array([tsim(TRI[i],TRI[j]) for i,j in same_pairs])
addrS=np.array([float(V[i]@V[j]) for i,j in same_pairs])

# 1:1 nearest-neighbour match on lexical similarity, with a tolerance
TOL=0.02
mi=np.searchsorted(lexD,lexS)
mi=np.clip(mi,0,len(lexD)-1)
ok=np.abs(lexD[mi]-lexS)<=TOL
print(f"=== 1:1 MATCHED on lexical similarity (tol {TOL}) ===")
print(f"  matched {ok.sum():,} of {len(lexS):,} same-module pairs ({100*ok.mean():.1f}%)")
if ok.sum()>50:
    a,b=addrS[ok].mean(),addrD[mi[ok]].mean()
    la,lb=lexS[ok].mean(),lexD[mi[ok]].mean()
    diff=addrS[ok]-addrD[mi[ok]]
    se=diff.std()/np.sqrt(len(diff))
    print(f"  mean lexical sim : same {la:.4f}  vs matched cross {lb:.4f}  (matched OK)")
    print(f"  mean address cos : same {a:.4f}  vs matched cross {b:.4f}")
    print(f"  GAP = {a-b:+.4f}  +/- {se:.4f} (SE)   t = {(a-b)/se:+.1f}")
    print(f"  {'SURVIVES lexical matching' if (a-b)/se>3 else 'DOES NOT survive'}")

print("\n=== partial correlation: same-module effect controlling for lexical sim ===")
allL=np.concatenate([lexS,lexD]); allA=np.concatenate([addrS,addrD])
allS=np.concatenate([np.ones(len(lexS)),np.zeros(len(lexD))])
X=np.column_stack([np.ones(len(allL)),allL])
bA=np.linalg.lstsq(X,allA,rcond=None)[0]; rA=allA-X@bA
bS=np.linalg.lstsq(X,allS,rcond=None)[0]; rS=allS-X@bS
print(f"  corr(lexical, address)                 = {np.corrcoef(allL,allA)[0,1]:+.4f}")
print(f"  corr(same-module, address)             = {np.corrcoef(allS,allA)[0,1]:+.4f}")
print(f"  PARTIAL corr(same-module, address | lex)= {np.corrcoef(rS,rA)[0,1]:+.4f}")
