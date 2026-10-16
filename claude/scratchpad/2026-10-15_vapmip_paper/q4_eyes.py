"""Q4 — one fixed question, five eyes (R sigma=1, C 3/4, H 1/2, O 1/4, S 0): sigma_self and Gamma per eye, and the full sigma sweep;
chase the non-monotone sweep seen for the longest prompt (METHOD? length aliasing?)."""
import math, random, subprocess, os
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
def sself(s,sig):
    x=[]
    for k in range(16):
        f=2*math.pi/P[k]; blue=4<=k<=7 or 12<=k<=15
        x.append(sum(c*i**(-sig)*(math.sin(f*i) if blue else math.cos(f*i)) for i,c in enumerate(s,1)))
    n=sum(a*a for a in x); return sum(x[k]**2 for k in range(16) if not (4<=k<=7 or 12<=k<=15))/n
PR=["finger pointer","what is a tree","neutron generation in different reactor types","good morning","can you play the piano?","the first reactor was built after neutrons were discovered"]
print("EYES (sigma 1, .75, .5, .25, 0): sigma_self / Gamma=2s-1")
for p in PR:
    row=[(sig,sself(p.encode(),sig)) for sig in (1.0,.75,.5,.25,0.0)]
    print(f"{p[:44]:44s} len={len(p):2d} "+"  ".join(f"{s:.4f}/{2*v-1:+.3f}" for s,v in row))
# check against the C: ptol -eye X -r
env=dict(os.environ,HOME=os.path.expandvars("$CLAUDE_JOB_DIR/tmp/home")); ok=True
for eye,sig in zip("RCHOS",(1.0,.75,.5,.25,0.0)):
    o=subprocess.run(["./ptol","-eye",eye,"-r","what is a tree"],capture_output=True,text=True,cwd="/home/rendier/Projects/ThePlace/VAPMIP/PtolC",env=env)
    line=[l for l in o.stderr.splitlines()+o.stdout.splitlines() if "σ_self" in l][0]
    c=float(line.split("σ_self:")[1].split()[0]); py=sself(b"what is a tree",sig); ok&=abs(c-py)<1e-9
    print(f"  C eye {eye}: sigma_self {c:.10f}  Python {py:.10f}")
print("C == Python for all five eyes:", ok)
# monotonicity vs length
random.seed(3)
import os as _o
words=[w.strip() for w in open("/usr/share/dict/words")] if _o.path.exists("/usr/share/dict/words") else None
if not words:
    from nltk.corpus import brown; words=[w for w in brown.words()[:200000] if w.isalpha()]
grid=[i/20 for i in range(21)]
buckets={}
for _ in range(3000):
    s=" ".join(random.choice(words) for _ in range(random.randint(1,12))); L=len(s)
    c=[sself(s.encode(),g) for g in grid]; mono=all(b>=a-1e-12 for a,b in zip(c,c[1:]))
    key=(L//10)*10; t=buckets.setdefault(key,[0,0]); t[0]+=mono; t[1]+=1
print("\nsigma_self(sigma) monotone-increasing on [0,1]? by prompt length (chars):")
for k in sorted(buckets): print(f"  {k:3d}-{k+9:3d}: {buckets[k][0]:4d}/{buckets[k][1]:4d} = {buckets[k][0]/buckets[k][1]:.1%}")
