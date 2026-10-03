"""Is an octonion PRODUCT chain usable as the top 'composite'?  Octonions over Z/2^32 (Cayley-Dickson), components = 8 x uint32.
 composite_n = composite_{n-1} (x) label_n   (label_n = SHA-256 of ingest n split into 8 uint32).
Tests: composition (norm multiplicative), order dependence, collapse when factors have even norm, forgeability (inverse exists for odd-norm), uniqueness."""
import hashlib, random
M = 1 << 32
def conj(x): return [x[0]] + [(-v) % M for v in x[1:]]
def add(x, y): return [(a + b) % M for a, b in zip(x, y)]
def sub(x, y): return [(a - b) % M for a, b in zip(x, y)]
def mul(x, y):
    n = len(x)
    if n == 1: return [(x[0] * y[0]) % M]
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    left = sub(mul(a, c), mul(conj(d), b)); right = add(mul(d, a), mul(b, conj(c)))
    return left + right
def norm(x): return sum(v * v for v in x) % M
rnd = random.Random(1)
rx = lambda: [rnd.getrandbits(32) for _ in range(8)]
print("norm multiplicative mod 2^32 on 2000 random pairs:", all(norm(mul(x, y)) == norm(x) * norm(y) % M for x, y in ((rx(), rx()) for _ in range(2000))))
x, y, z = rx(), rx(), rx()
print("non-commutative:", mul(x, y) != mul(y, x), "| non-associative:", mul(mul(x, y), z) != mul(x, mul(y, z)))
def label(i: int, salt=b""): h = hashlib.sha256(salt + i.to_bytes(4, "big")).digest(); return [int.from_bytes(h[k:k + 4], "big") for k in range(0, 32, 4)]
def chain(labels, force_odd):
    c = [1] + [0] * 7
    for L in labels:
        if force_odd and norm(L) % 2 == 0: L = [L[0] ^ 1] + L[1:]       # make the norm odd: a unit
        c = mul(c, L)
    return c
print("fraction of random labels with ODD norm (units):", sum(norm(rx()) % 2 for _ in range(20000)) / 20000)
for force in (False, True):
    zeros = 0; trail = []
    c = [1] + [0] * 7
    for i in range(200):
        L = label(i)
        if force and norm(L) % 2 == 0: L = [L[0] ^ 1] + L[1:]
        c = mul(c, L); trail.append(norm(c))
    even_steps = sum(1 for v in trail if v % 2 == 0)
    print("chain of 200 labels, force_odd=%-5s: composite norm is even at %3d of 200 steps | composite all-zero: %s | lowest set bit of the final norm: %s" %
          (force, even_steps, all(v == 0 for v in c), (norm(c) & -norm(c)).bit_length() - 1 if norm(c) else "norm = 0"))
# order dependence and sensitivity (force_odd chain)
labels = [label(i) for i in range(34)]
base = chain(labels, True); swapped = labels[:]; swapped[10], swapped[11] = swapped[11], swapped[10]
print("swap two adjacent ingests changes the composite:", chain(swapped, True) != base)
flip = [l[:] for l in labels]; flip[20][3] ^= 1; ch = chain(flip, True)
print("one bit changed in one ingest changes %d of 8 components; bits differing in the 256-bit composite: %d" % (sum(a != b for a, b in zip(ch, base)), sum(bin(a ^ b).count("1") for a, b in zip(ch, base))))
# forgeability: with odd-norm factors the last factor is recoverable from (previous composite, new composite): inverse = conj / norm
prev = chain(labels[:-1], True); top = chain(labels, True); L = labels[-1]; L = [L[0] ^ 1] + L[1:] if norm(L) % 2 == 0 else L
inv_norm = pow(norm(prev), -1, M); prev_inv = [(v * inv_norm) % M for v in conj(prev)]
print("last ingest label recoverable from (previous composite, top):", mul(prev_inv, top) == L)
# uniqueness: 20000 random 5-ingest histories (force_odd): any duplicate composites?
seen = set(); dup = 0
for t in range(20000):
    h = tuple(chain([label(rnd.getrandbits(32), salt=b"x") for _ in range(5)], True)); dup += h in seen; seen.add(h)
print("20000 random 5-ingest histories: duplicate composites:", dup)
