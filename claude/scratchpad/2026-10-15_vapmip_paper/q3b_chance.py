"""Q3b — is P_red*P_blue ~ 0.2460 at sigma in {0,1} for the neutron prompt a coincidence? Count how often 2000 random English-ish prompts land within 1e-4 of 0.2460 (and 0.24631)."""
import math, random, itertools
random.seed(7)
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
def pp(s,sig):
    x=[]
    for k in range(16):
        f=2*math.pi/P[k]; blue=4<=k<=7 or 12<=k<=15
        x.append(sum(c*i**(-sig)*(math.sin(f*i) if blue else math.cos(f*i)) for i,c in enumerate(s,1)))
    n=sum(a*a for a in x); pr=sum(x[k]**2 for k in range(16) if not (4<=k<=7 or 12<=k<=15))/n
    return pr*(1-pr)
words=[w.strip() for w in open("/usr/share/dict/words")] if __import__("os").path.exists("/usr/share/dict/words") else None
if not words:
    import nltk; from nltk.corpus import brown; words=[w for w in brown.words()[:200000] if w.isalpha()]
N=0; hit=0; hit31=0
for _ in range(2000):
    s=" ".join(random.choice(words) for _ in range(random.randint(2,6))).encode()
    for sig in (0.0,0.25,0.5,0.75,1.0):
        v=pp(s,sig); N+=1
        if abs(v-0.2460)<1e-4: hit+=1
        if abs(v-0.24631)<1e-4: hit31+=1
print(f"samples {N}; within 1e-4 of 0.2460: {hit} ({hit/N:.4%}); of 0.24631: {hit31} ({hit31/N:.4%})")
print("neutron prompt: P_r*P_b at sigma=0, 1 =", pp(b"neutron generation in different reactor types",0.0), pp(b"neutron generation in different reactor types",1.0))
print("expected hits for 30 samples at this rate:", 30*hit/N)
