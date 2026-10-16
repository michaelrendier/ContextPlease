"""P2b — chase the 'above chance' result of P2. Hypothesis: every hit is an exact pi-lattice identity (constants 1/2,1,2,pi,2pi,1/pi,sqrt2 are all in {2^a pi^b}).
Test: (1) classify each hit as exact algebra; (2) rerun the search with ONLY the non-lattice UNS constants (phi,e,ln10,Omega,d*,d*_spec,GAP);
(3) chance baseline matched to that set; (4) allow the four quantities to be taken in any role (radius/diameter/circ/area of the SAME constant)."""
import math, itertools, random
import mpmath as mp
mp.mp.dps = 25
LN10 = float(mp.log(10)); OM = float(mp.lambertw(1).real); PHI = (1+5**.5)/2
UNS = {"phi": PHI, "e": math.e, "ln10": LN10, "Omega": OM, "d*": OM/LN10, "d*_spec": 0.246, "GAP": 1/(1000*2**.5)}
def quad(c):  # as radius
    return {"r": c, "d": 2*c, "C": 2*math.pi*c, "A": math.pi*c*c}
cells = [(f"{k}({n})", v, n) for n, c in UNS.items() for k, v in quad(c).items()]
def hits(cells, tol=1e-3):
    out = []
    for (a, va, na), (b, vb, nb) in itertools.combinations(cells, 2):
        if na == nb: continue
        if abs(va-vb)/max(va, vb) < tol: out.append((a, b, va, vb))
    return out
h = hits(cells); print("non-lattice UNS constants only:", len(cells), "cells ->", len(h), "cross hits"); [print("  ", x) for x in h]
# also against the small integers and 1/2 (so 'd*=1/4 ceiling' style coincidences show)
base_cells = cells + [(f"{k}({n})", v, n) for n, c in {"1/2": .5, "1": 1., "2": 2., "4": 4., "1/4": .25}.items() for k, v in quad(c).items()]
h2 = [x for x in hits(base_cells) if not (x[0].split('(')[1][:-1] in UNS and x[1].split('(')[1][:-1] in UNS)]
print("UNS cell vs small-rational circle cells:", len(h2)); [print("  ", x) for x in h2]
random.seed(7); lo, hi = math.log(0.0007), math.log(2.8)
def rand_hits():
    cs = [math.exp(random.uniform(lo, hi)) for _ in UNS]
    cc = [(f"{k}({i})", v, i) for i, c in enumerate(cs) for k, v in quad(c).items()]
    cc += [(f"{k}(q{n})", v, f"q{n}") for n, c in {"1/2": .5, "1": 1., "2": 2., "4": 4., "1/4": .25}.items() for k, v in quad(c).items()]
    return len(hits(cc))
base = [rand_hits() for _ in range(600)]
print(f"chance (same count, same range, same small-rational cells): mean {sum(base)/len(base):.2f}, 95th pct {sorted(base)[int(.95*len(base))]}, max {max(base)}; observed total {len(h)+len(h2)}")
