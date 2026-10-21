import sys, random, collections, re, unicodedata
sys.path.insert(0,'/home/rendier/Projects/ThePlace/VAPMIP/SemPriCon/tools')
from zh_structure import load
C=load()['chars']
IDC=set('⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻')
def leaves(ids): return [ch for ch in ids if ch not in IDC and ch not in '？']
def toneless(p): return unicodedata.normalize('NFD',p).encode('ascii','ignore').decode()
def keyof(c):
    r=C[c]; ids=r.get('ids')
    if not ids or ids==c: return c, 'self'
    L=leaves(ids)
    if len(L)<2: return c,'self'
    rad=r['rad']
    sem=[l for l in L if l in C and C[l]['rad']==rad] or [l for l in L if l in C and C[l].get('tot')==None]
    other=[l for l in L if l not in sem[:1]]
    return (other[0] if other else c), 'comp'
K={c:keyof(c) for c in C}
print('simple/self',sum(v[1]=='self' for v in K.values()),'composite',sum(v[1]=='comp' for v in K.values()))
# sound predictiveness: pairs sharing key -> share toneless pinyin?
by=collections.defaultdict(list)
for c,(k,t) in K.items():
    if t=='comp' and 'mand' in C[c]: by[k].append(c)
same=tot=0
for k,cs in by.items():
    for i in range(len(cs)):
        for j in range(i+1,len(cs)):
            tot+=1; same+= toneless(C[cs[i]]['mand'])==toneless(C[cs[j]]['mand'])
print('same-key pairs',tot,'share toneless pinyin %.3f'%(same/tot))
allc=[c for c in C if 'mand' in C[c] and K[c][1]=='comp']; random.seed(1)
hit=0;n=200000
for _ in range(n):
    a,b=random.sample(allc,2); hit+= toneless(C[a]['mand'])==toneless(C[b]['mand'])
print('random pairs share toneless pinyin %.4f'%(hit/n))
# mmh pictophonetic subset: does my key == mmh phonetic?
agree=cnt=0
for c,r in C.items():
    m=r.get('mmh')
    if m and m.get('etymology') and m['etymology'].get('type')=='pictophonetic' and K[c][1]=='comp':
        cnt+=1; agree+= K[c][0]==m['etymology'].get('phonetic')
print('pictophonetic chars with a key',cnt,'key == makemeahanzi phonetic: %.3f'%(agree/cnt))
