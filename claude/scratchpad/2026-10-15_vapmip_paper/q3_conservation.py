"""Q3 — test ptol.c's header claim 'J_red x J_blue = d* = 0.24600 is conserved at ALL sigma' using the C's own definitions
(project(), L2-normalised v, s_rb[k] = v[k]*v[partner(k)]) re-implemented and cross-checked against `ptol -r` (q2)."""
import math, subprocess, os
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
def proj(s,k,sig):
    f=2*math.pi/P[k]; blue=4<=k<=7 or 12<=k<=15
    return sum(c*i**(-sig)*(math.sin(f*i) if blue else math.cos(f*i)) for i,c in enumerate(s,1))
def partner(k): return k+4 if k<4 else k-4 if k<8 else k+4 if k<12 else k-4
PR=["finger pointer","what is a tree","neutron generation in different reactor types","good morning","can you play the piano?","the first reactor was built after neutrons were discovered"]
print(f"{'prompt':28s} sigma | sum_k s_rb | sum|s_rb| | Pred*Pblue | sqrt(PrPb) | sigma_self")
for p in PR[:3]:
    for sig in (0.0,0.25,0.5,0.75,1.0):
        x=[proj(p.encode(),k,sig) for k in range(16)]; n=math.sqrt(sum(a*a for a in x)); v=[a/n for a in x]
        s=[v[k]*v[partner(k)] for k in range(16)]
        pr=sum(v[k]**2 for k in range(16) if not (4<=k<=7 or 12<=k<=15)); pb=1-pr
        print(f"{p[:28]:28s} {sig:4.2f} | {sum(s):+.6f} | {sum(abs(a) for a in s):.6f} | {pr*pb:.6f} | {math.sqrt(pr*pb):.6f} | {pr:.6f}")
print("\nd* = 0.24600 (header) ; 0.24631 (Omega/ln10). Is any column constant across sigma and prompts? -> see spread below")
import statistics
vals={"sum_s":[], "abs_s":[], "PrPb":[], "sqrtPrPb":[]}
import itertools
for p in PR:
    for sig in (0.0,0.25,0.5,0.75,1.0):
        x=[proj(p.encode(),k,sig) for k in range(16)]; n=math.sqrt(sum(a*a for a in x)); v=[a/n for a in x]
        s=[v[k]*v[partner(k)] for k in range(16)]; pr=sum(v[k]**2 for k in range(16) if not (4<=k<=7 or 12<=k<=15))
        vals["sum_s"].append(sum(s)); vals["abs_s"].append(sum(abs(a) for a in s)); vals["PrPb"].append(pr*(1-pr)); vals["sqrtPrPb"].append(math.sqrt(pr*(1-pr)))
for k,a in vals.items(): print(f"{k:9s} min {min(a):+.5f} max {max(a):+.5f} mean {statistics.mean(a):+.5f}")
