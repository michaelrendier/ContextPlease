import sys, re, collections, pickle
sys.path.insert(0,'/home/rendier/Projects/ThePlace/VAPMIP/SemPriCon/tools')
import ptol_bin
M=(1<<64)-1; PHI=0x9E3779B97F4A7C15; N=25000; DS=0.24600; OM=0.56714
def addr(w):
    v=0
    for c in w: v=(v*95+(ord(c)-31))&M
    if v>0: v-=1
    s=(v*PHI)&M
    return (s*N)>>64, DS+(s>>11)/9007199254740992.0*(OM-DS)
HEX=set('0123456789abcdefABCDEF')
def reject_reason(t):
    n=len(t)
    if n>24: return 'longer than 24'
    if t.endswith("'"): pass
    if n>=3 and t[0]=='0' and t[1] in 'xX': return 'hex'
    if n>=6 and all(c in HEX for c in t): return 'hex-string gate (a-f letters only, 6+)'
    vc=sum(c in 'aeiouy' for c in t if c!="'"); letters=sum(c!="'" for c in t)
    if letters>0:
        if vc==0: return 'no vowel'
        if n>=6 and vc*100//n<15: return 'low vowel ratio'
    if t[-1]=="'": return 'trailing apostrophe'
    return None
txt=open('corpora/text/en_v1.txt',encoding='utf-8').read()
order=collections.OrderedDict(); cnt=collections.Counter(); rej=collections.Counter(); rejn=collections.Counter(); lead=collections.Counter(); short=0
for m in re.finditer(r"[A-Za-z']+",txt):
    t=m.group(0).lower()
    if len(t)<2: short+=1; continue
    if t[0]=="'": lead[t]+=1; continue
    r=reject_reason(t)
    if r: rej[t]+=1; rejn[r]+=1; continue
    cnt[t]+=1
    if t not in order: order[t]=len(order)
print('accepted tokens',sum(cnt.values()),'distinct',len(cnt),'rejected',sum(rej.values()),dict(rejn),'leading-apostrophe',sum(lead.values()),'under2',short)
d=ptol_bin.load('clean/archive/v1.0/test_english_v1.0.bin')
print('bin word_count',d['word_count'],'vocab',d['vocab_size'])
slots=collections.defaultdict(list)
for t in order: slots[addr(t)[0]].append(t)   # insertion order = first appearance
vocab={i:(w,E) for i,w,E,*_ in d['vocab']}
print('slots from port',len(slots),'slots in bin',len(vocab),'same set',set(slots)==set(vocab))
bad=0
for s,ws in slots.items():
    top=max(ws,key=lambda w:addr(w)[1])
    if vocab.get(s,(None,))[0]!=top: bad+=1
print('label != highest-E member in',bad,'slots')
pickle.dump(dict(slots=dict(slots),cnt=cnt,order=order,rej=rej,rejn=rejn,lead=lead,short=short),open('/tmp/claude-1000/-home-rendier-Projects-ThePlace/454aab1b-b2b4-4cfd-990e-e1d3a910b0fa/scratchpad/en1_dict.pkl','wb'))
