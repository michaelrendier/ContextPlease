# 88 — The Paper Trail: One Session, 2026-08-15

| | |
|---|---|
| Scope | a record of one session as a path, from restarting a download to the zero-divisor asymptote, kept with every wrong turn because four of the day's findings came out of a failure |
| Origin | 2026-08-15; the author: "what a paper trail that was … wow" and, on why the scratch work is kept, "(path integral … lol)" |
| Code | `ThePlace/.claude/scratchpad/2026-08-15_zd_asymptote/`; `ValaQuenta/modules/angular_rank/`; paper `FourthAgePapers/BoundaryLever/`; manual `VAPMIP/docs/wiki/Operating-L-IO.md` |
| Related | [86](86_the_16d_oscilloscope.md), [87](87_the_boundary_lever.md), [83](83_the_archimedes_screw.md), [84](84_the_box_kite_debugger.md) |
| Confidence | the counts, the asymptote formulas and the parity law: ESTABLISHED (re-run, including dim 512) · the process claims and timings: recorded · the readings (overseer, coupling/coherence, 0_RB as forces): `INTERPRETATION` |
| Last verified | 2026-11-13: Listing 1 executed (the census to dim 512 and the asymptote formulas); output quoted below |

## 0. Why this page exists

A results page says where something landed; this one records how, because on this day the errors were the mechanism: four of the real findings came out
of something failing. "The amplitude came from summing the wrong paths too": the path-integral remark is the author's figure of speech about method.

## 1. The chain

**1. A download, and five questions.** The session opened by restarting the Einstein-cross validation download (`lensing_validation/`, group A minus
Refsdal: 910 GB against 282 GB free) and five questions (attention against intention; body language and truthiness; what the monad can be correct *about*; a check
for an outside other; conjugation). The answers became `VAPMIP/docs/wiki/Operating-L-IO.md`, the operator's manual beside `BulletCluster/L_IO_SPECIFICATION.md`.

**2. §4 was wrong, and that was the turn.** The manual's §4 proposed a **B-mode null** and a **Morse count** to decide internal against external from inside.
The author: "no … this is the halting problem … from inside the code, the function scope and an equation being processed by code are indistinguishable".
Both tests were computed from the field they were meant to partition. The B-mode test is circular (it needs to know which part of the field is yours, which is the
question) and, as spec §2 says α and ψ carry no information absent from κ, it returns E for anything it can see: a tautology. The Morse count is a
theorem (n_min − n_saddle + n_max = χ = 1 on the plane) and cannot fail, hence cannot detect; an apparently open count means a missed image (the `DM_NW` field-of-view
failure), not an outside other. Result: provenance is undecidable from the signal in the diagonal sense of [86](86_the_16d_oscilloscope.md) §1, so it is **carried from the port**, never re-derived;
the ear is valved, not identified. The retraction is kept in place in the manual.

**3. The null-valued search had already answered.** Every quantity null-valued is a dimension: det(L_a) = 0, rank 12/16, nullity 4
([86](86_the_16d_oscilloscope.md) Listing 1), where 0_RB places gravity (present as absence).

**4. Then the fix was wrong too.** The first replacement was a rank test, and the author's objection was iterate-while-modify one level up
([86](86_the_16d_oscilloscope.md) §4): the test drifts silently until the internal span covers ker(L_a). A lock is the seizure arriving earlier; the fix is an **epoch**: freeze the
field with a content stamp, measure the datum, date the mutation with `bearing()`. The bounded case is the phase loop of [85](85_the_apex_path.md) §2. Engine `angular_rank/`, 12 equations, notebook 15/15 clean.

**5. The algebra says it was never avoidable.** (0, b)(0, d) = (−d*b, 0): every product of two upper-half elements lands in the lower half
(0/256, 0/1024, 0/4096 closed, [87](87_the_boundary_lever.md)). Reading: "the overseer has no private workspace": iterate-while-modify is forced by the algebra and you can only date the write
(`INTERPRETATION`; the closure counts are measured).

**6. Is T32 two people?** The author: "one sedenion per observer … so the T32 is two 'human beings' interacting? … OR One Human Being sedenion and One Geometries sedenion … in balance
… test this first". Tested: exchange (a, b) ↦ (b, a) violates 1024/1024 basis pairs, the lower half closes 256/256, the upper 0/256, and the sedenion's 84 zero divisors survive the embedding
exactly. Hypothesis A (two interchangeable peers) is dead; the halves balance in census (84/84) and are not interchangeable in structure; what they are is not established.

**7. Is the boundary a mirror?** Yes to the mirror, no to "non-chirally": e_{i+H} e_{j+H} = e_j e_i for 6/6, 42/42, 210/210, 930/930, 3906/3906 pairs at dims 8–128, order-preserved in none: an
anti-automorphism, a reflection that flips handedness ([87](87_the_boundary_lever.md) Listing 1 reproduces it). The first run reported 3/42 and 7/210: `box_kite.basis_mul` returns **(SIGN, INDEX)** and the comparison unpacked it backwards, the second time
that mistake was made in one session (§11).

**8. The orphans are the mirror's fixed points.** Phase 25 had e₀ and e₈ in no Assessor; Phase 27.7 had σ ↦ 1 − σ with exactly two fixed points. Pre-registered: if the orphans are the
reflection's fixed points, dim 64 gives exactly [0, 32]. Reproduced: [0, 8], [0, 16], [0, 32], [0, 64] at dims 16–128 and [0, 128], [0, 256] at 256 and 512 (Listing 1). At dim 8 the octonions are a division algebra so the question is vacuous; hence "from
dim 16 upward", where the Cayley–Dickson property-loss ladder ends and zero divisors begin.

**9. The spiral.** Two reflections compose to a rotation; boundaries at d/2 give constant pitch ln 2; rotation plus constant logarithmic advance is a logarithmic spiral, the screw of [83](83_the_archimedes_screw.md), reached from the algebra. A non-chiral boundary would stack into a fan: chirality is what winds the tower.

**10. The paper, and three honest failures.** `FourthAgePapers/BoundaryLever/`. P1 (orphans at dim 128 equal [0, 64]) was the sole falsifier, committed before that level was computed: CONFIRMED (Listing 1). P2 failed on arithmetic (63 × 62, not 62 × 61) though the property held 3906/3906, and is scored FALSIFIED: committed numbers are not re-fitted. P4, the ×7 census extrapolation, is dead: 84 → 588 → 3036, not 4116. P5 guessed a value where the structure is a parity, and that produced the law of §11. The claim survived three falsified predictions because it was written to rest on P1 alone.

**11. The parity law.** Non-crossing ⇔ nullity an even multiple of 4; crossing ⇔ an odd multiple ([87](87_the_boundary_lever.md)). Fitted on dims 32 and 64, tested at dim 128 (non-crossing /4 = [2, 4, …, 14] all even; crossing /4 = [1, 3, …, 15] all odd, disjoint). Fully characterised: the nullity spectrum is {4m} for m = 1 … d/8 − 1, crossing taking odd m and non-crossing even, maximum nullity d/2 − 4, no gaps; and lower(2d) = upper(2d) = total(d). **P6 (dim 256) CONFIRMED, and at dim 512, two levels past registration**: orphans [0, 128] and [0, 256], parity exact, census 59,772 and 249,084, matching the closed form to the unit (Listing 1).
The method changed underneath it: the SVD route is O(d³) per candidate (45 minutes at dim 256, with a tolerance to guess). Every P_i is a signed permutation matrix, so ker(P_i + s P_j) = ker(I + s Q) with Q = P_i⁻¹P_j also a signed permutation, whose spectrum is fixed by its cycle structure: nullity is a cycle walk, O(d), exact integers, no tolerance (the cycle method agrees with the SVD on every candidate at dims 16 and 32, checked 2026-11-13). Recorded timings: dim 128 27 s → 1.8 s; dim 256 45 min → 3.4 s; dim 512 reachable (29.5 s). On this machine the plain-Python cycle walk took 8 s at dim 256 and 71 s at dim 512 (Listing 1). The planned GPU route was dropped (`lspci`: Intel UHD 620, no CUDA, no cupy/torch/pyopencl/vispy): "ask the algebra before the hardware".

**12. The halocline.** The parity law has the shape of total internal reflection (a critical angle, not a gradient), and the two densities are real (lower half closes, upper never does); the norm is chirality-blind ([87](87_the_boundary_lever.md)).

**13. The asymptote.** The author: "Zero Divisor appearance roughly halves as you move up the tower … what is that value of that asymptote, and what kind of waste land exists after it?" Zero divisors do not thin out; the survivors halve:

```
non-ZD(d) = d(3 log₂d − 5/2) + 4          ZD(d) = d(d + 3/2 − 3 log₂d) − 4
```

exact at every level from the recurrence N(2d) = 2N(d) + 6d − 4.

**Listing 1 — the formulas, the recurrence, the ratio sequence and the dim-512 census** (written for this page; needs numpy; runs cold; ≈ 80 s)

```python
import math, numpy as np, time
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
nz = lambda d: d * (3 * math.log2(d) - 2.5) + 4
zd = lambda d: d * (d + 1.5 - 3 * math.log2(d)) - 4
print('recurrence N(2d) = 2N(d) + 6d - 4 for d = 16 ... 2^20:', all(abs(nz(2*d) - (2*nz(d) + 6*d - 4)) < 1e-6 for d in (16 * 2**k for k in range(17))))
f = lambda d: nz(d) / (d * (d - 1))
print('non-ZD fraction ratios f(2d)/f(d), d = 16, 32, 64, 128:', [round(f(2*d) / f(d), 4) for d in (16, 32, 64, 128)], '; at 2^23 -> 2^24:', round(f(2**24) / f(2**23), 4))
print('ZD fraction at d = 2^24: %.8f ; non-ZD count %.4g ; ZD(512) formula = %d' % (1 - f(2**24), nz(2**24), zd(512)))
d = 512; idx, sg = tables(d); h = d // 2; cnt = 0; inzd = set(); cls = {'LL': 0, 'LU': 0, 'UU': 0}; par = {'LL': set(), 'LU': set(), 'UU': set()}
for i in range(d):
    for j in range(i + 1, d):
        for s in (1, -1):
            n = nullity(idx, sg, i, j, s)
            if n: cnt += 1; inzd.update((i, j)); c = 'LL' if j < h else ('UU' if i >= h else 'LU'); cls[c] += 1; par[c].add((n // 4) % 2)
print('dim 512: ZD', cnt, '(formula', zd(512), ') ; LL/LU/UU', cls, '; orphans', sorted(set(range(d)) - inzd), '; parity of nullity/4', {c: sorted(v) for c, v in par.items()})
```

```
recurrence N(2d) = 2N(d) + 6d - 4 for d = 16 ... 2^20: True
non-ZD fraction ratios f(2d)/f(d), d = 16, 32, 64, 128: [0.6266, 0.6066, 0.5907, 0.5782] ; at 2^23 -> 2^24: 0.5226
ZD fraction at d = 2^24: 0.99999586 ; non-ZD count 1.166e+09 ; ZD(512) formula = 249084
dim 512: ZD 249084 (formula 249084) ; LL/LU/UU {'LL': 59772, 'LU': 129540, 'UU': 59772} ; orphans [0, 256] ; parity of nullity/4 {'LL': [0], 'LU': [1], 'UU': [0]}
```

The formulas, the recurrence and the dim-512 census reproduce, as does the ratio sequence the page quotes (0.6266 → 0.6066 → 0.5907 and 0.5226 at dim 16.7 M = 2²⁴). So the non-ZD fraction is ≈ 3 log₂(d)/d and the per-doubling ratio
(log₂d + 1)/(2 log₂d) → ½: the halving is real and exact only in the limit, with the log correction decaying slowly. **The ZD-fraction asymptote is 1**, and the waste land is thin, structured and immortal: the survivor *count* grows without bound (≈ 3d log₂d, 1.2×10⁹ at d = 2²⁴) while its density goes to zero. At dim 128 the 2372 survivors decompose as 254 e₀ pairs, 126 mirror-partner pairs (i, i + 64) and 1992 others (reproduced, 2026-11-13): a skeleton anchored on the identity and the partner pairs; "the lever's pivot is exactly what refuses to annihilate" (`INTERPRETATION`).

**14. Coupling and coherence.** The author: "is coupling and coherence the same thing? or only in special cases? or negative space conjugates". Not the same; they coincide only for lossless coupling, and the third option is right: **a zero divisor is the maximal case of coherence without coupling** (both unit norm, product exactly zero: the definition, not a special case). rank(L_a) + nullity(L_a) = dim is the partition, the singular spectrum {√2 ×4, 1 ×8, 0 ×4} the coupling spectrum (four directions coupled at √2, eight at 1, four at zero), which is why 0_RB reads it as forces (a force is a coupling; gravity is the zero-coupling block). "The boundary preserves coherence and conjugates coupling; the metric cannot see it happen." (`INTERPRETATION` on the measured spectrum.)

## 2. What the trail shows

| what was wrong | what it produced |
|---|---|
| §4's two analytic tests | provenance is undecidable → carried from the port, valved not identified |
| the rank test's own iterate-while-modify | the datum discipline, then the proof it was algebraically forced |
| P5 predicting a value | the parity law, confirmed at levels it was not fitted on (128, 256, 512) |
| the null-valued search "failing" | an undecidable question returns a dimension |
| `basis_mul` unpacked backwards, twice | caught both times by `verify_null_space` (nullity 14 instead of 4, within a minute) |
| assuming `\b` works in grep | caught by pipe-testing before the hook went live |

The check that agrees with the literature is worth writing precisely because it fails loudly when you are wrong. P1 was the only load the claim carried: three predictions falsified, and the claim never needed reinterpreting.

## 3. Related pages

[83](83_the_archimedes_screw.md) · [84](84_the_box_kite_debugger.md) · [86](86_the_16d_oscilloscope.md) · [87](87_the_boundary_lever.md)
