exec(open('struts.py').read().split('print("== one strut')[0])
sq=[nz(m(Y[k],Y[k])+np.dot(Y[k],Y[k])*np.eye(16)[0]) for k in keys]; print("x*x = -|x|^2 e0 for all 84 diagonals: max residual %.1e"%max(sq))
# same-kite pairs: anticommute whenever nonzero?
bad=0;nzc=0
for k1,k2 in itertools.combinations(keys,2):
    if k1[0]^k1[1]==k2[0]^k2[1]:
        r=stats(Y[k1],Y[k2]); 
        if r[0]>1e-9: nzc+=1; bad+= r[3]>1e-9
print("same-kite pairs with nonzero product:",nzc," of which NOT exactly anticommuting:",bad)
# cross-kite friction by kite pair
tab=collections.defaultdict(list)
for k1,k2 in itertools.combinations(keys,2):
    s1,s2=k1[0]^k1[1],k2[0]^k2[1]
    if s1!=s2: tab[tuple(sorted((s1,s2)))].append(stats(Y[k1],Y[k2])[3])
v=np.array([np.mean(x) for x in tab.values()]); print("cross-kite mean anticommutator |{x,y}| per kite pair: min %.3f mean %.3f max %.3f; distinct values:"%(v.min(),v.mean(),v.max()),sorted(set(np.round(v,3))))
allv=np.concatenate([np.array(x) for x in tab.values()]); print("per-pair anticommutator values (rounded) and counts:",dict(collections.Counter(np.round(allv,3)).most_common(8)))
# is the friction tied to whether the two struts' lines/kites share structure?  s1^s2 vs friction
byx=collections.defaultdict(list)
for (s1,s2),x in tab.items(): byx[s1^s2].append(np.mean(x))
print("mean friction by (s1 xor s2):",{k:round(float(np.mean(x)),3) for k,x in sorted(byx.items())})
