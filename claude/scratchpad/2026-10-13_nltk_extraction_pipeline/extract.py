"""NLTK-only extraction + disambiguation of a prompt. Offline: tokenizer (no data), perceptron tagger trained on UD-EWT (tagger_train.py),
RegexpParser chunker, WordNet morphy/synsets, extended-Lesk (Banerjee-Pedersen style, own 15 lines, gloss of sense + glosses of its related synsets)."""
import pickle, re, time, collections
from nltk.tokenize import NLTKWordTokenizer
from nltk.tag import PerceptronTagger
from nltk.chunk import RegexpParser
from nltk.corpus import wordnet as wn
w,td,cl=pickle.load(open('perceptron_ewt.pkl','rb'))
pt=PerceptronTagger(load=False); pt.model.weights=w; pt.tagdict=td; pt.classes=cl; pt.model.classes=cl
TOK=NLTKWordTokenizer()
CHUNK=RegexpParser(r"""
 NP: {<DET|PRON>?<NUM>?<ADJ|NOUN|PROPN>*<NOUN|PROPN>}
 PP: {<ADP><NP>}
""")
UPOS2WN={'NOUN':'n','PROPN':'n','VERB':'v','ADJ':'a','ADV':'r','AUX':'v'}
STOP=set("a an the of in on at to for and or is are was were be been it its this that these those with by from as which who what how why when where".split())
def words(text): return [t for t in re.findall(r"[a-z]+",text.lower()) if t not in STOP and len(t)>2]
def bag(s,related=True):
    b=collections.Counter(words(s.definition()))
    for ex in s.examples()[:2]: b.update(words(ex))
    if related:
        for m in ('hypernyms','hyponyms','part_meronyms','part_holonyms','member_holonyms','substance_meronyms','entailments','causes','also_sees','similar_tos','attributes'):
            for t in getattr(s,m)(): b.update(words(t.definition()))
    return b
def ext_lesk(target,pos,context_lemmas):
    ctx=collections.Counter()
    for l,p in context_lemmas:
        if l==target: continue
        for s in wn.synsets(l,p)[:4]: ctx.update(bag(s,related=False))   # glosses of the context words' senses
    best=None;score={}
    for s in wn.synsets(target,pos):
        b=bag(s); sc=sum(min(b[k],ctx[k]) for k in b if k in ctx); score[s.name()]=sc
    return max(score,key=score.get) if score and max(score.values())>0 else None, score
def run(prompt):
    t0=time.time()
    toks=TOK.tokenize(prompt); tagged=pt.tag(toks)
    # Zork-style repair: a token tagged ADJ/other that WordNet only knows as a noun, sitting directly before a NOUN, is a noun modifier
    fixed=[]
    for i,(wd,tg) in enumerate(tagged):
        if tg=='ADJ' and not wn.synsets(wd,'a') and wn.synsets(wd,'n') and i+1<len(tagged) and tagged[i+1][1] in('NOUN','PROPN'): tg='NOUN'
        fixed.append((wd,tg))
    tree=CHUNK.parse(fixed)
    ctx=[(wn.morphy(wd.lower(),UPOS2WN.get(tg,'n')) or wd.lower(),UPOS2WN[tg]) for wd,tg in fixed if tg in UPOS2WN]
    out=[]
    for sub in tree:
        if hasattr(sub,'label') and sub.label()=='NP': nps=[sub]
        elif hasattr(sub,'label') and sub.label()=='PP': nps=[x for x in sub if hasattr(x,'label')]
        else: continue
        for np_ in nps:
            lv=list(np_.leaves()); sens=[]
            for wd,tg in lv:
                if tg in('NOUN','PROPN'):
                    hl=wn.morphy(wd.lower(),'n') or wd.lower(); sense,_=ext_lesk(hl,'n',ctx)
                    sens.append((hl,sense))
            head=sens[-1][0] if sens else None
            out.append((sub.label(),' '.join(x[0] for x in lv),'head='+str(head),sens))
    verbs=[(wd,wn.morphy(wd.lower(),'v')) for wd,tg in fixed if tg=='VERB']
    return fixed,out,verbs,(time.time()-t0)*1000
if __name__=='__main__':
    for p in ["neutron generation in different reactor types","The first reactor was built after neutrons were discovered","She deposited money at the bank","The plant produces electricity from nuclear fission"]:
        fixed,out,verbs,ms=run(p); print("\n>>",p,"(%.0f ms)"%ms); print("  tags:",fixed)
        for o in out: print("  ",o)
        print("   verbs:",verbs)
