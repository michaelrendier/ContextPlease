import sys, random, collections, numpy as np
sys.path.insert(0,'/home/rendier/Projects/ThePlace/VAPMIP/SemPriCon/tools')
from zh_structure import load
S=load(); C=S['chars']; two=S['two']
chars=list(C)
# orders
rs=sorted(chars,key=lambda c:(C[c]['rad'],C[c]['res'],ord(c)))
x_rs={c:i/len(rs) for i,c in enumerate(rs)}
x_cp={c:i/len(chars) for i,c in enumerate(sorted(chars,key=ord))}
phi=(1+5**.5)/2
x_hash={c:((i+0)/phi)%1 for i,c in enumerate(sorted(chars,key=ord))}   # v2-like (rank, golden)
x_gold_rs={c:(i/phi)%1 for i,c in enumerate(rs)}                          # golden in radical-stroke order
def circ(a,b): d=abs(a-b); return min(d,1-d)
pairs=[(a,b) for a,b in two if a in C and b in C and a!=b]
print('compound pairs usable',len(pairs))
random.seed(3)
moechars=[c for c in chars if C[c]['moe']>0]
sh=[b for a,b in pairs]; random.shuffle(sh); rnd=[(a,b2) for (a,b),b2 in zip(pairs,sh) if a!=b2]
share=lambda P:np.mean([C[a]['rad']==C[b]['rad'] for a,b in P])
print('share radical: compounds %.4f random %.4f'%(share(pairs),share(rnd)))
for name,x in [('codepoint rank',x_cp),('v2-like golden(rank)',x_hash),('golden over rad-stroke order',x_gold_rs),('rad-stroke contiguous',x_rs)]:
    dc=np.array([circ(x[a],x[b]) for a,b in pairs]); dr=np.array([circ(x[a],x[b]) for a,b in rnd])
    print('%-30s median|Δ| compounds %.4f random %.4f ; within 2%% of circle: %.4f vs %.4f'%(name,np.median(dc),np.median(dr),np.mean(dc<.02),np.mean(dr<.02)))
