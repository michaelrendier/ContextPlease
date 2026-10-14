"""Bernstein-Lagarias (1996) conjecture on fixed points of the conjugacy map, re-measured on the truncations Q_k.
Q_k(n) = parity vector of the first k steps of the shortcut map. A fixed point at level k reduces to a fixed point at level k-1 (solenoidal),
so the fixed points form a tree; the nodes with descendants at the deepest level are the finite-precision shadows of genuine fixed points in Z_2."""
import time
def T(n): return n >> 1 if n % 2 == 0 else (3 * n + 1) >> 1
def Qk(n, k):
    v, m = 0, n
    for i in range(k):
        v |= (m & 1) << i; m = T(m)
    return v
K = 200; t = time.time()
levels = {}
frontier = [0, 1]                       # candidate residues mod 2^1
for k in range(1, K + 1):
    fp = [x for x in frontier if Qk(x, k) == x]
    levels[k] = fp
    frontier = fp + [x + (1 << k) for x in fp]          # only fixed points can have fixed-point extensions
print(f'levels computed to k={K} in {time.time()-t:.1f}s (extending only surviving fixed points: exact, because a fixed point mod 2^(k+1) reduces to one mod 2^k)')
# survivors: nodes at level k that have a descendant at level K
alive = set(levels[K])
for k in range(K, 0, -1):
    alive = {x % (1 << (k - 1)) for x in alive} if k > 1 else alive
print('fixed points at each level k (all, odd, even):')
for k in [1,2,3,4,5,6,8,10,12,16,20,24,32,40,48,64,80,100,128,160,200]:
    fp = levels[k]; print(f'  k={k:3d}  all {len(fp):4d}  odd {sum(x & 1 for x in fp):4d}  even {sum(1-(x&1) for x in fp):4d}')
fK = levels[K]
inv3 = pow(3, -1, 1 << K)
print('1/3 mod 2^K =', inv3, ' is a level-K fixed point:', inv3 in fK, '; -1 mod 2^K =', (1 << K) - 1, ' is a level-K fixed point:', ((1 << K) - 1) in fK)
odd = [x for x in fK if x & 1]; print('odd fixed points at level K:', len(odd), ' sample:', sorted(odd)[:12])
print('odd fixed points at level K that are -1 or 1/3 (mod 2^K):', sorted(x for x in odd if x in ((1<<K)-1, inv3)))
print('all fixed points at level K:', len(fK), ' even ones:', len(fK)-len(odd), ' the even ones that are 0 mod 2^K:', fK.count(0))
