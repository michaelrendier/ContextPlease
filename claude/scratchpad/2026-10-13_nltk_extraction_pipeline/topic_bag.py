"""Cody's idea: learn the topic from a search/AI overview (ingested text), then disambiguate the prompt against that topic bag."""
import collections, re, time
from extract import *
txt=open('neutron_generation_overview.txt').read()
t0=time.time(); bag_topic=collections.Counter()
for sent in re.split(r'(?<=[.:])\s+',txt):
    toks=TOK.tokenize(sent); tg=pt.tag(toks)
    for wd,t in tg:
        if t in UPOS2WN:
            l=wn.morphy(wd.lower(),UPOS2WN[t]) or wd.lower()
            if l not in STOP and len(l)>2: bag_topic[l]+=1
print("topic bag: %d lemmas, %.0f ms; top:"%(len(bag_topic),(time.time()-t0)*1000),bag_topic.most_common(12))
def topic_sense(target,pos,topic):
    sc={}
    for s in wn.synsets(target,pos):
        b=bag(s); sc[s.name()]=sum(min(b[k],topic[k]) for k in b if k in topic)
    return sc
for tgt in ['reactor','generation','type','neutron']:
    sc=topic_sense(tgt,'n',bag_topic); best=max(sc,key=sc.get)
    print(f"{tgt:10s} -> {best:26s} {wn.synset(best).definition()[:55]} | scores top3 {sorted(sc.items(),key=lambda x:-x[1])[:3]}")
