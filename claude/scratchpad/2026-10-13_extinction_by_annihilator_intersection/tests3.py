exec(open('tests2.py').read().split('# T1')[0])
rel=collections.Counter(); ex=[]
for i,j in itertools.combinations(range(84),2):
    if ker([i,j]).shape[1]==4:
        (a,b,s),(c,d,t)=keys[i],keys[j]
        rel[("same_plane" if (a,b)==(c,d) else "reversed" if (a,b)==(d,c) else "same_a" if a==c else "same_b" if b==d else "other", "samesign" if s==t else "oppsign", "samestrut" if a^b==c^d else "diffstrut")]+=1
        if len(ex)<3: ex.append((keys[i],keys[j]))
print("dim-4 pairs:",dict(rel)); print(ex)
# invariance on pairs that DO have a common kernel
Ds=derivations()
def flow(t): return expm(sum(ti*D for ti,D in zip(t,Ds)))
rng=np.random.default_rng(3); g=flow(rng.normal(size=14)*0.7)
bad=0;n=0
for i,j in itertools.combinations(range(84),2):
    d0=ker([i,j]).shape[1]
    if d0>0:
        M=np.vstack([Rm(g@Y[i]),Rm(g@Y[j])]); d1=16-int((np.linalg.svd(M,compute_uv=False)>1e-9).sum()); n+=1; bad+=(d0!=d1)
print("random G2 flow: common-kernel dim preserved on",n-bad,"/",n,"pairs that had a nonzero kernel")
