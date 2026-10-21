import sys, itertools; sys.path.insert(0,'/home/rendier/Projects/ThePlace/SedenionSpectralRelativity')
from fractions import Fraction as F
from firing_plan import *
def circ(k):
    v=[F(0)]*16; v[0]=F(3,5); v[k]=F(4,5); return tuple(v)
from collections import Counter
cnt=Counter()
for t in itertools.combinations(range(1,16),3):
    L=[Leaf(f"e{k}",vec=circ(k)) for k in t]
    vals={value(p) for p in permuted_shapes(L)}
    cnt[len(vals)]+=1
print("triples by distinct results (permuted shapes, all orders):",dict(cnt))
# separable permutations reachable by written-order binary plans
for n in (3,4,5):
    L=[Leaf(str(i)) for i in range(n)]
    seqs={tuple(fire_sequence(p)) for p in binary_plans(L)}
    print(n,"leaves: written-order binary plans", count_plans(n,'binary'), "reach", len(seqs),"of",math.factorial(n),"orders; n-ary count",count_plans(n,'nary'))
