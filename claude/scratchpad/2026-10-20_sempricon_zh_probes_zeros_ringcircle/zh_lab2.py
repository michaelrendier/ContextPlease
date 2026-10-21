import sys, json, re, random, collections, numpy as np
exec(open('/tmp/claude-1000/-home-rendier-Projects-ThePlace/454aab1b-b2b4-4cfd-990e-e1d3a910b0fa/scratchpad/zh_lab1.py').read().split("MECH={")[0])
exec("def circ(a,b): d=abs(a-b); return min(d,N-d)")
# shuowen radical order
sw=json.load(open('/home/rendier/Projects/ThePlace/VAPMIP/SemPriCon/corpora/zh/classical/shuowen.json',encoding='utf-8'))
sec=[]; 
for e in sw:
    r=e['radical']
    if not sec or sec[-1]!=r: sec.append(r)
print('shuowen sections',len(sec))
# head char of section = first char with that radical label; map to kangxi radical via unihan
first={}
for e in sw:
    first.setdefault(e['radical'],e['char'])
kx_first={}
simp2trad={}
for c in chars:
    s=C[c].get('simp')
    for t in re.findall(r"U\+([0-9A-F]+)",s or ''): simp2trad[chr(int(t,16))]=c
for i,r in enumerate(sec):
    h=first[r]; h=h if h in C else simp2trad.get(h,h)
    if h in C:
        kx_first.setdefault(C[h]['rad'],i)
print('kangxi radicals reached by shuowen sections',len(kx_first),'of 214')
def rank_order(radkey, intra):
    return sorted(chars,key=lambda c:(radkey(C[c]['rad']),)+intra(c))
rk_kx=lambda r:r
rk_sw=lambda r:(kx_first.get(r,10**6),r)
ph={}
IDC=set('⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻')
def key(c):
    ids=C[c].get('ids')
    if not ids or ids==c: return ord(c)
    L=[l for l in ids if l not in IDC and l!='？']
    sem=[l for l in L if l in C and C[l]['rad']==C[c]['rad']]
    other=[l for l in L if l not in sem[:1]]
    return ord(other[0]) if other else ord(c)
intras={'res,cp':lambda c:(C[c]['res'],ord(c)),'tot,cp':lambda c:(C[c]['tot'],ord(c)),'moe desc,res':lambda c:(-C[c]['moe'],C[c]['res'],ord(c)),'key,res':lambda c:(key(c),C[c]['res'],ord(c)),'res,key':lambda c:(C[c]['res'],key(c),ord(c))}
def pos_of(order): return {c:(i*N)//M for i,c in enumerate(order)}
pairs=[(a,b) for a,b in two if a in C and b in C and a!=b]
random.seed(3); sh=[b for a,b in pairs]; random.shuffle(sh); rnd=[(a,b2) for (a,b),b2 in zip(pairs,sh) if a!=b2]
STOP=set('a an the of to or and in on for with by be is as at it from that this one any used also'.split())
G={c:({w for w in re.findall(r"[a-z]+",C[c]['defn'].lower()) if w not in STOP and len(w)>2} if C[c].get('defn') else None) for c in chars}
gc=[c for c in chars if G[c]]; random.seed(5); gp=[tuple(random.sample(gc,2)) for _ in range(300000)]
var=list({tuple(sorted((c,chr(int(t,16))))) for c in chars for k in ('sem','trad','simp') if C[c].get(k) for t in re.findall(r"U\+([0-9A-F]+)",C[c][k]) if chr(int(t,16)) in C and chr(int(t,16))!=c})
rv=[tuple(random.sample(chars,2)) for _ in range(len(var))]
def run(name,order):
    P=pos_of(order)
    out=[]
    for eps in (0.002,0.02):
        cm=np.mean([circ(P[a],P[b])<eps*N for a,b in pairs]); rr=np.mean([circ(P[a],P[b])<eps*N for a,b in rnd])
        near=[bool(G[a]&G[b]) for a,b in gp if circ(P[a],P[b])<eps*N]; far=[bool(G[a]&G[b]) for a,b in gp if circ(P[a],P[b])>=eps*N]
        out.append('eps %.3f: compounds %.4f/%.4f (x%.2f) gloss %.4f/%.4f (x%.2f)'%(eps,cm,rr,cm/rr,np.mean(near),np.mean(far),np.mean(near)/np.mean(far)))
    print('%-28s'%name,' | '.join(out))
for rn,rk in (('kangxi',rk_kx),('shuowen',rk_sw)):
    for inn,ig in intras.items():
        run(rn+' / '+inn,rank_order(rk,ig))
