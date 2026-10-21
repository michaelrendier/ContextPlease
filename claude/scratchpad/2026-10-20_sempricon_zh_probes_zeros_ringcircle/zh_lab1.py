import sys, random, collections, re, math, numpy as np
sys.path.insert(0,'/home/rendier/Projects/ThePlace/VAPMIP/SemPriCon/tools')
from zh_structure import load
D=load(); C=D['chars']; two=D['two']; alpha=D['alpha']
N=25000; PHI=(1+5**.5)/2; M=len(alpha)
chars=[chr(c) for c in alpha]
order=sorted(chars,key=lambda c:(C[c]['rad'],C[c]['res'],ord(c)))
def S0():  # v2-like rank Horner → golden seed
    return {c:int(((i)/PHI%1)*N) for i,c in enumerate(chars)}
def S1():  # golden assignment in dictionary order
    return {c:(i*9549)%N for i,c in enumerate(order)}
def S3():  # population CDF
    return {c:(i*N)//M for i,c in enumerate(order)}
def S2():  # pure mixed radix: equal arc per radical, residual strokes spread across arc
    smax=collections.defaultdict(int)
    for c in chars: smax[C[c]['rad']]=max(smax[C[c]['rad']],C[c]['res'])
    return {c:min(N-1,int(N*((C[c]['rad']-1)+(C[c]['res']+0.5)/(smax[C[c]['rad']]+1))/214)) for c in chars}
def S5():  # radical-pure slots: slots per radical ∝ population (largest remainder), members spread by rank
    cnt=collections.Counter(C[c]['rad'] for c in chars)
    raw={r:N*cnt[r]/M for r in cnt}; w={r:max(1,int(raw[r])) for r in cnt}
    left=N-sum(w.values())
    for r in sorted(cnt,key=lambda r:-(raw[r]-int(raw[r])))[:max(0,left)]: w[r]+=1
    while sum(w.values())>N:
        r=max(w,key=lambda r:w[r]); w[r]-=1
    start={};s=0
    for r in sorted(cnt): start[r]=s; s+=w[r]
    pos={}; seen=collections.Counter()
    for c in order:
        r=C[c]['rad']; j=seen[r]; seen[r]+=1
        pos[c]=start[r]+min(w[r]-1,(j*w[r])//cnt[r])
    return pos
MECH={'S0 v2-like hash':S0,'S1 golden in dict order':S1,'S2 mixed radix (pure)':S2,'S3 population CDF':S3,'S5 radical-pure slots':S5}
def circ(a,b): d=abs(a-b); return min(d,N-d)
def gini(x):
    x=np.sort(np.asarray(x,float)); n=len(x); return (2*np.arange(1,n+1)-n-1).dot(x)/(n*x.sum())
pairs=[(a,b) for a,b in two if a in C and b in C and a!=b]
random.seed(3); sh=[b for a,b in pairs]; random.shuffle(sh); rnd=[(a,b2) for (a,b),b2 in zip(pairs,sh) if a!=b2]
STOP=set('a an the of to or and in on for with by be is as at it from that this one any used also'.split())
def gl(c):
    d=C[c].get('defn'); 
    return None if not d else {w for w in re.findall(r"[a-z]+",d.lower()) if w not in STOP and len(w)>2}
G={c:gl(c) for c in chars}; gc=[c for c in chars if G[c]]
random.seed(5); gp=[tuple(random.sample(gc,2)) for _ in range(300000)]
rel=lambda a,b: bool(G[a]&G[b])
var=[]
for c in chars:
    for k in ('sem','trad','simp'):
        v=C[c].get(k)
        if v:
            for t in re.findall(r"U\+([0-9A-F]+)",v):
                d=chr(int(t,16))
                if d in C and d!=c: var.append((c,d))
var=list({tuple(sorted(p)) for p in var})
print('probe sizes: compounds',len(pairs),'gloss pairs',len(gp),'variant pairs',len(var))
print('%-26s %8s %8s | %8s %8s %6s | %8s %8s | load max  empty  gini'%('mechanism','cmp<2%','rnd<2%','nearRel','farRel','x','var<2%','rnd<2%'))
rv=[tuple(random.sample(chars,2)) for _ in range(len(var))]
for name,f in MECH.items():
    P=f()
    cm=np.mean([circ(P[a],P[b])<0.02*N for a,b in pairs]); rr=np.mean([circ(P[a],P[b])<0.02*N for a,b in rnd])
    near=[rel(a,b) for a,b in gp if circ(P[a],P[b])<0.02*N]; far=[rel(a,b) for a,b in gp if circ(P[a],P[b])>=0.02*N]
    nr,fr=np.mean(near),np.mean(far)
    vv=np.mean([circ(P[a],P[b])<0.02*N for a,b in var]); vr=np.mean([circ(P[a],P[b])<0.02*N for a,b in rv])
    occ=collections.Counter(P.values()); L=[occ.get(s,0) for s in range(N)]
    print('%-26s %8.4f %8.4f | %8.4f %8.4f %6.2f | %8.4f %8.4f | %6d %6.3f %5.2f'%(name,cm,rr,nr,fr,nr/fr,vv,vr,max(L),sum(1 for x in L if x==0)/N,gini(L)))
