exec(open('struts.py').read().split('print("== one strut')[0])
sup=lambda k:{k[0],k[1]+8}
tot=ov=match=0; sym_from_overlap=collections.Counter()
for k1,k2 in itertools.combinations(keys,2):
    if k1[0]^k1[1]==k2[0]^k2[1]: continue
    tot+=1; o=len(sup(k1)&sup(k2)); fr=stats(Y[k1],Y[k2])[3]
    sym_from_overlap[(o,round(fr,3))]+=1
print("cross-kite pairs:",tot,"; (shared indices, |{x,y}|) -> count:",dict(sym_from_overlap))
