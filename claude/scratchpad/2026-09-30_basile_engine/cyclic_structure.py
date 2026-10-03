"""Is 'several locations, one image' cyclic? Two tests.
T1 (published constants): is the offset between sibling locations a FIXED translation (a coset of a subgroup of Z_m),
    and do offsets for different bits add?  (siblings = L + offset, offset independent of L?)
T2 (toy scrambler, Listing 2): cycle structure of scramble on [0, N): one N-cycle, or several? plus pure LCG and xorshift parts."""
import sys, random, math
from collections import Counter
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.basile import maths as M
pub = M.Published(); m = int(pub.m)
rnd = random.Random(5)
locs = [rnd.getrandbits(3194895) % m for _ in range(3)]
print("== T1: offset between a location and its sibling, for the same flipped bit, at three different locations ==")
for pos in (399360, 3194888, 3194890):
    offs = []
    for L in locs:
        p = pub.forward(L); L2 = pub.inverse(p ^ (1 << pos)); offs.append((L2 - L) % m)
    same = len(set(offs)) == 1
    print("bit %8d: offset identical across the 3 locations: %s | offsets as signed residues (bits): %s" % (pos, same, [ (o if o < m//2 else o - m).bit_length() for o in offs]))
print("\n== T1b: do offsets add?  offset(bit a ^ bit b) == offset(a) + offset(b) (mod m) at one location ==")
L = locs[0]; p = pub.forward(L)
off = lambda bits: (pub.inverse(p ^ sum(1 << b for b in bits)) - L) % m
a_, b_ = 399360, 3194890
print("additive:", off([a_, b_]) == (off([a_]) + off([b_])) % m)
print("\n== T2: cycle structure of the toy scrambler (Listing 2) on [0, N), N = 29^3 ==")
N = 29 ** 3; sc, un = M.power_of_two_scrambler(N)
def cycles(f, n):
    seen = [False] * n; out = []
    for i in range(n):
        if not seen[i]:
            j, k = i, 0
            while not seen[j]: seen[j] = True; j = f(j); k += 1
            out.append(k)
    return sorted(out, reverse=True)
c = cycles(sc, N); print("scrambler : cycles %d | longest %d | shortest %d | fixed points %d | lcm of cycle lengths has %d digits" % (len(c), c[0], c[-1], c.count(1), len(str(math.lcm(*c)))))
e = (N - 1).bit_length(); Mm = 1 << e
lcg = lambda x: (1664525 * x + 1013904223) % Mm
c2 = cycles(lcg, Mm); print("pure LCG mod 2^%d : cycles %d | longest %d  (Hull-Dobell: one full cycle of %d)" % (e, len(c2), c2[0], Mm))
def xs(x):
    x ^= x >> 7; x ^= (x << 5) & (Mm - 1); return x
c3 = cycles(xs, Mm); print("xorshift part alone (a permutation of [0,2^%d)): cycles %d | longest %d" % (e, len(c3), c3[0]))
print("scrambler cycle-length histogram (top 8):", Counter(c).most_common(8))

print("\n== T1c: additivity of the sibling offsets over ALL pairs and the full set of the 16 valid unread bits, at two locations ==")
import itertools
bits = [b for b in pub.unread_positions() if pub.sibling(locs[0], b)["forward_matches"]]
print("valid unread bits:", len(bits))
for L in locs[:2]:
    p = pub.forward(L)
    off = lambda S: (pub.inverse(p ^ sum(1 << b for b in S)) - L) % m
    single = {b: off([b]) for b in bits}
    pairs_ok = all(off([a, b]) == (single[a] + single[b]) % m for a, b in itertools.combinations(bits, 2))
    all_ok = off(bits) == sum(single.values()) % m
    print("location %s...: all 120 pairs additive: %s | all 16 flipped together == sum of the 16 offsets: %s" % (str(L)[:12], pairs_ok, all_ok))
    print("   the 16 single-flip offsets are distinct mod m:", len(set(single.values())) == 16)
