"""Train an NLTK POS tagger OFFLINE from the UD English-EWT treebank already on disk (no downloads), measure accuracy/size/speed."""
import time, pickle, os, sys
import nltk
from nltk.tag import PerceptronTagger, UnigramTagger, BigramTagger, DefaultTagger
D='/home/rendier/Projects/ThePlace/VAPMIP/datasets/UD_English-EWT/'
def read(f):
    out=[];cur=[]
    for line in open(D+f,encoding='utf8'):
        line=line.rstrip('\n')
        if not line:
            if cur: out.append(cur); cur=[]
        elif not line.startswith('#'):
            p=line.split('\t')
            if '-' in p[0] or '.' in p[0]: continue
            cur.append((p[1],p[3]))
    return out
tr,te=read('en_ewt-ud-train.conllu'),read('en_ewt-ud-test.conllu')
print("train sents",len(tr),"test sents",len(te))
def acc(tg):
    g=sum(len(s) for s in te); ok=0
    for s in te:
        pr=tg.tag([w for w,_ in s]); ok+=sum(1 for (a,b),(_,c) in zip(s,pr) if b==c)
    return ok/g
t=time.time(); uni=UnigramTagger(tr,backoff=DefaultTagger('NOUN')); big=BigramTagger(tr,backoff=uni)
print("uni+bigram backoff acc %.4f  train %.1fs"%(acc(big),time.time()-t))
t=time.time(); pt=PerceptronTagger(load=False); pt.train(tr,nr_iter=5)
print("perceptron acc %.4f train %.1fs"%(acc(pt),time.time()-t))
pt.save_to_json if hasattr(pt,'save_to_json') else None
pickle.dump((pt.model.weights,pt.tagdict,pt.classes),open('perceptron_ewt.pkl','wb'))
print("perceptron pickle bytes",os.path.getsize('perceptron_ewt.pkl'))
s=[w for w,_ in te[5]]; t=time.time()
for _ in range(200): pt.tag(s)
print("perceptron tag %.2f ms / %d-token sentence"%((time.time()-t)/200*1000,len(s)))
print(pt.tag("neutron generation in different reactor types".split()))
