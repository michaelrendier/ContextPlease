# 87 — The Boundary Lever: the Halocline, the Mirrored Curtain, and Where Chirality Lives

| | |
|---|---|
| Scope | whether the Cayley–Dickson boundary is a mirror, and a chiral one; the parity law of the zero-divisor nullities; closure of the two halves; chirality as an ordering property that the norm cannot see; the winding of the tower; the lever; what is not claimed |
| Origin | 2026-08-15; the author's question: "Balance … and The Lever Emerges … is the boundary a balance point … is it a mirror aka does e₀–e₇ mirrored (non chirally reversed) across the boundary?" |
| Code | `ValaQuenta/modules/angular_rank/`, `modules/box_kite/`; paper `FourthAgePapers/BoundaryLever/`; canonical block THE BOUNDARY LEVER |
| Confidence | closure, the mirror identity, the exchange failure, the norm test and the parity law (dims 32–256): ESTABLISHED (re-run) · the halocline/lever reading: `INTERPRETATION` · the parity law was found post hoc and is a registered prediction (P6, §1) |
| Last verified | 2026-11-13: Listing 1 executed with an independent table builder; its output is quoted below |

## 0. The answer

Yes to the mirror and no to the "non-chirally": and the "no" is the useful half.

## 1. The halocline: a critical angle  `ESTABLISHED` + `INTERPRETATION`

Fresh water over salt water with surface tension gives total internal reflection: not a gradient but a critical angle, an
exception-free threshold. The algebra carries a threshold of that shape. Classify the zero-divisors eᵢ ± eⱼ of the
doubled algebra of dimension d by where their indices sit: both in the lower half (LL), both in the upper (UU), or one in each
(LU, "boundary-crossing"). The nullity of L_a for each divisor is a multiple of 4, and:

```
NON-CROSSING (LL, UU)   nullity an EVEN multiple of 4          BOUNDARY-CROSSING (LU)   nullity an ODD multiple of 4
dim 32   non-crossing {8} = 4×{2}            crossing {4, 12} = 4×{1, 3}
dim 64   non-crossing {8, 16, 24}            crossing {4, 12, 20, 28}
```

**Listing 1 — the parity law, the closure of the halves, the mirror and the norm test** (written for this page; needs numpy; runs cold; the nullity is computed by the cycle structure of a signed permutation, exact integers with no tolerance)

```python
import numpy as np, itertools
def tables(d):
    idx = np.zeros((1, 1), int); sg = np.ones((1, 1), int); h = 1
    while h < d:
        I = np.zeros((2*h, 2*h), int); S = np.zeros((2*h, 2*h), int); I[:h, :h], S[:h, :h] = idx, sg
        for i in range(h):
            for j in range(h):
                I[i, h+j], S[i, h+j] = h + idx[j, i], sg[j, i]
                I[h+i, j], S[h+i, j] = h + idx[i, j], sg[i, j] * (1 if j == 0 else -1)
                I[h+i, h+j], S[h+i, h+j] = idx[j, i], -(1 if j == 0 else -1) * sg[j, i]
        idx, sg, h = I, S, 2*h
    return idx, sg
def nullity(idx, sg, i, j, s):             # ker(P_i + s P_j) = ker(I + s Q), Q = P_i^-1 P_j a signed permutation
    d = idx.shape[0]; inv = np.empty(d, int); inv[idx[i]] = np.arange(d); q = inv[idx[j]]; sq = sg[j] * sg[i][q]
    seen = np.zeros(d, bool); n = 0
    for k in range(d):
        if seen[k]: continue
        m, eps, c = 0, 1, k
        while not seen[c]: seen[c] = True; eps *= sq[c]; c = q[c]; m += 1
        n += int((-s) ** m == eps)
    return n
rng = np.random.default_rng(3)
for d in (16, 32, 64, 128):
    idx, sg = tables(d); h = d // 2; cls = {'LL': [], 'LU': [], 'UU': []}; inzd = set()
    for i, j in itertools.combinations(range(d), 2):
        for s in (1, -1):
            n = nullity(idx, sg, i, j, s)
            if n: cls['LL' if j < h else ('UU' if i >= h else 'LU')].append(n); inzd.update((i, j))
    print('dim %3d: LL/LU/UU counts %d/%d/%d ; nullity/4 by class %s ; orphans %s' % (d, len(cls['LL']), len(cls['LU']), len(cls['UU']), {c: sorted({int(n) // 4 for n in v}) for c, v in cls.items() if v}, sorted(set(range(d)) - inzd)))
for d in (32, 64):
    idx, sg = tables(d); H = d // 2
    print('dim %d: lower half closed %d/%d ; upper half closed %d/%d' % (d, sum(idx[i, j] < H for i in range(H) for j in range(H)), H*H, sum(idx[H+i, H+j] >= H for i in range(H) for j in range(H)), H*H))
    M = lambda k: (k + H) % d
    print('   exchange (a,b)->(b,a) violates the product for %d/%d basis pairs' % (sum(1 for i in range(d) for j in range(d) if not (idx[M(i), M(j)] == M(idx[i, j]) and sg[M(i), M(j)] == sg[i, j])), d*d))
    mul = lambda x, y: sum((np.eye(d)[idx[i, j]] * x[i] * y[j] * sg[i, j] for i in np.flatnonzero(x) for j in np.flatnonzero(y)), np.zeros(d))
    Mv = lambda v: np.concatenate([v[H:], v[:H]]); n1 = n2 = 0
    for _ in range(60):
        x, y = rng.normal(size=d), rng.normal(size=d); a = np.linalg.norm(mul(Mv(x), Mv(y))); n1 += abs(a - np.linalg.norm(mul(y, x))) < 1e-9; n2 += abs(a - np.linalg.norm(mul(x, y))) < 1e-9
    print('   |M(x)M(y)| == |yx|: %d/60 ; == |xy|: %d/60' % (n1, n2))
for d in (8, 16, 32, 64, 128):
    idx, sg = tables(d); H = d // 2; pairs = list(itertools.permutations(range(1, H), 2))
    print('dim %3d: e_(i+H) e_(j+H) = e_j e_i for %d/%d ordered pairs; order-preserved for %d' % (d, sum(idx[H+i, H+j] == idx[j, i] and sg[H+i, H+j] == sg[j, i] for i, j in pairs), len(pairs), sum(idx[H+i, H+j] == idx[i, j] and sg[H+i, H+j] == sg[i, j] for i, j in pairs)))
```

```
dim  16: LL/LU/UU counts 0/84/0 ; nullity/4 by class {'LU': [1]} ; orphans [0, 8]
dim  32: LL/LU/UU counts 84/420/84 ; nullity/4 by class {'LL': [2], 'LU': [1, 3], 'UU': [2]} ; orphans [0, 16]
dim  64: LL/LU/UU counts 588/1860/588 ; nullity/4 by class {'LL': [2, 4, 6], 'LU': [1, 3, 5, 7], 'UU': [2, 4, 6]} ; orphans [0, 32]
dim 128: LL/LU/UU counts 3036/7812/3036 ; nullity/4 by class {'LL': [2, 4, 6, 8, 10, 12, 14], 'LU': [1, 3, 5, 7, 9, 11, 13, 15], 'UU': [2, 4, 6, 8, 10, 12, 14]} ; orphans [0, 64]
dim 32: lower half closed 256/256 ; upper half closed 0/256
   exchange (a,b)->(b,a) violates the product for 1024/1024 basis pairs
   |M(x)M(y)| == |yx|: 60/60 ; == |xy|: 60/60
dim 64: lower half closed 1024/1024 ; upper half closed 0/1024
   exchange (a,b)->(b,a) violates the product for 4096/4096 basis pairs
   |M(x)M(y)| == |yx|: 60/60 ; == |xy|: 60/60
dim   8: e_(i+H) e_(j+H) = e_j e_i for 6/6 ordered pairs; order-preserved for 0
dim  16: e_(i+H) e_(j+H) = e_j e_i for 42/42 ordered pairs; order-preserved for 0
dim  32: e_(i+H) e_(j+H) = e_j e_i for 210/210 ordered pairs; order-preserved for 0
dim  64: e_(i+H) e_(j+H) = e_j e_i for 930/930 ordered pairs; order-preserved for 0
dim 128: e_(i+H) e_(j+H) = e_j e_i for 3906/3906 ordered pairs; order-preserved for 0
```

(The listing's `mul` helper is a slow dense implementation, adequate at these sizes. The orphans, the two indices in no zero-divisor, are 0 and d/2.)
The parity law reproduces exactly: nullities are always multiples of 4, non-crossing ones (LL, UU) even multiples and crossing ones
(LU) odd multiples, with the two orphan indices 0 and d/2 at every level. It is **post hoc**: found by looking at data that had
already falsified the prediction that suggested it (P5 guessed a value where the structure is a parity), and registered as P6 for
dim 256 and left untested in the paper so as not to test a post-hoc pattern on the data that produced it (the dim 256 and 512 checks are in
[88](88_the_paper_trail.md) §11).

**The two densities are real.** The lower half (a, 0) is closed under multiplication (256/256 at dim 32, 1024/1024 at dim 64); the upper half (0, b) never is (0/256,
0/1024): every product of two upper elements falls into the lower half, since (0, b)(0, d) = (−d*b, 0). The incompressible one is the one that closes.

## 2. The chirality  `ESTABLISHED`

> "right and left switch places but right and left hands don't."

A mirror swaps front for back along its normal; the left–right reading is the observer turning to face the image. In the algebra, with M(v) = concat(v[H:], v[:H])
(the exchange of halves): M is an isometry and an involution (norm preserved, M(M(v)) = v), and for random x, y
|M(x)M(y)| equals both |yx| and |xy| in 60/60 trials at dims 32 and 64 (Listing 1). The test was meant to discriminate order-preserved from
order-inverted and cannot: **the norm is chirality-blind**. A metric sees congruent hands. The inversion lives entirely in the ordering:
e_{i+H} e_{j+H} = e_j e_i (the indices swap) for 6/6, 42/42, 210/210, 930/930, 3906/3906 ordered pairs at dims 8–128, order-preserved in none. This
is the Cayley–Dickson product (0, b)(0, d) = (−d*b, 0) with imaginary units (d* = −d), so it is an identity of the doubling formula, and the order reversal is an
anti-automorphism: a reflection that flips handedness. The exchange map (a, b) ↦ (b, a) is **not** an automorphism: it violates the product for 1024/1024 basis pairs at dim 32
and 4096/4096 at dim 64. Ordering is a labelling, not a geometry, so measuring lengths never reveals it.

## 3. Why chirality is load-bearing  `INTERPRETATION`

If the boundary were a plain reflection the levels would stack into a fan of parallel mirrors and nothing would accumulate. But two reflections
compose to a rotation, and successive boundaries sit at d/2, a constant step in log₂, so a constant pitch of ln 2. Rotation plus constant
logarithmic advance is a logarithmic spiral: the Archimedes screw of [83](83_the_archimedes_screw.md) ("the machine is the logarithm, pitch = ln p")
reached from the algebra and not from the primes. "Chirality is what makes the tower wind instead of stack." The two-reflections-make-a-rotation statement and the ln 2
pitch are arithmetic; that the tower's levels are "boundaries" in the sense of reflections in space is the framework's reading.

## 4. The lever  `INTERPRETATION` over measured counts

A fulcrum does no work and is the one thing that does not move while everything else balances across it. The mirror has exactly two fixed points,
always the same two: e₀ (the identity; [e₀, ·, ·] = 0, generates the boundary and does not live on it: `box_kite.e0_is_outside`, [84](84_the_box_kite_debugger.md))
and e_{d/2} (the generator introduced by this doubling). Both lie in no zero-divisor (the orphans of Listing 1) and carry no force (in 0_RB's reading "gravity,
present as absence"). The balance is the census: LL = UU, 84/84 at dim 32 and 588/588 at dim 64 (and 3036/3036 at 128, 13884/13884 at 256), with LL(2d) = UU(2d) =
total(d). That is a lever in the page's sense: the pivot carries no force and the load is equal on both sides.

## 5. What is not claimed, and what died  `kept`

T32 is not two peers: the exchange violates the product on every basis pair and the upper half never closes, so the halves balance in census and are not
interchangeable in structure. That rules a symmetry out; it does not say what sits on either side. "One sedenion per observer", "one human and one
Geometries in balance": the algebra permits those readings and establishes none of them; nothing here is a claim about observers, meaning or physics.

**What died (kept so it is not re-derived):** the zero-divisor census does not scale ×7 per level: 84 → 588 → 3036 (ratios 7, then 5.16),
with the dim-64 split 588/1860/588 (Listing 1), not the predicted 588/2940/588. The extrapolation was read off a single step and broke at the next.

## 6. Related pages

[83](83_the_archimedes_screw.md) · [84](84_the_box_kite_debugger.md) · [86](86_the_16d_oscilloscope.md) · [88 the paper trail](88_the_paper_trail.md) · [89](89_the_seven_octonions.md)
