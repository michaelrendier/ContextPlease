"""TEST 1 — THE BRACKETING TEST.
Does a 'reverse pathway' survive non-associativity, or is it an artifact of
the bracketing the implementation silently chose?

Left-division: given a and c = a*b, recover b as a^-1 * c.
In an ALTERNATIVE algebra (octonions) this is exact. In sedenions it need not be.
"""
import numpy as np, sys
sys.path.insert(0, '/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/2026-08-08_sedenion_igpu_benchmark')
from sedbench2 import cd_mul_slow, cd_conj

def mul(x, y): return cd_mul_slow(np.asarray(x,float), np.asarray(y,float))
def inv(x):
    x = np.asarray(x,float); n2 = float(x@x)
    return cd_conj(x)/n2

rng = np.random.default_rng(7)
print("=== TEST 1: does left-division recover the input? ===")
print("   relative error  ||a^-1*(a*b) - b|| / ||b||\n")
for dim, name in ((4,'quaternion (associative)'), (8,'octonion (alternative)'),
                  (16,'SEDENION'), (32,'T32')):
    errs, asso = [], []
    for _ in range(400):
        a = rng.normal(size=dim); b = rng.normal(size=dim)
        c = mul(a, b)
        b2 = mul(inv(a), c)
        errs.append(np.linalg.norm(b2-b)/np.linalg.norm(b))
        d = rng.normal(size=dim)
        asso.append(np.linalg.norm(mul(mul(a,b),d) - mul(a,mul(b,d))) /
                    (np.linalg.norm(a)*np.linalg.norm(b)*np.linalg.norm(d)))
    print(f"  {name:26s} median {np.median(errs):.3e}   max {np.max(errs):.3e}"
          f"   | associator {np.median(asso):.3e}")

print("\n=== bracketing dependence: does the ANSWER depend on where you put parens? ===")
for dim, name in ((8,'octonion'), (16,'SEDENION')):
    diffs = []
    for _ in range(400):
        a,b,c = (rng.normal(size=dim) for _ in range(3))
        L = mul(mul(a,b),c); R = mul(a,mul(b,c))
        diffs.append(np.linalg.norm(L-R)/max(np.linalg.norm(L),1e-30))
    print(f"  {name:10s} median relative disagreement between the two bracketings: "
          f"{np.median(diffs):.4f}  ({100*np.median(diffs):.1f}%)")
