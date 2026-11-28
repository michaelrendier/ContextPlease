# 81 — SHA-1 Real Collision Geometry: the Schedule Differential, Verified

| | |
|---|---|
| Scope | the T32/GF(2) reading of the real SHAttered collision (Stevens et al., CWI/Google, 2017): the expanded message-schedule differential, where it vanishes |
| Origin | 2026-07-17, the author with Claude |
| Predecessors | [78](78_t32_nilpotency.md), [21](21_chladni_zipf_riemann.md), [79](79_prime_gate_alarm.md) |
| Code | `TuringStack/wiki/SHA1-Real-Collision-Geometry-2026-07-17.md`, `TuringStack/paper.tex` §3, `TuringStack/sha1_chladni_figure.py`, `TuringStack/hypercomplex_laplacian.py`; data `TuringStack/shattered_data/shattered-{1,2}.pdf` |
| Confidence | the measurements: ESTABLISHED (reproduced from the files 2026-11-13) · the geometric reading: `INTERPRETATION` · scope: a characterisation of an already-broken hash; no new attack |
| Last verified | 2026-11-13: both PDFs hashed and the schedule differential recomputed; output quoted below |

## 0. What changed

`TuringStack/paper.tex` carried a Proposition that the real SHAttered message differential lies in
the T32/GF(2) XOR-linear null space, never checked against the real files. It was checked
against the files from the original disclosure (`shattered.io`), verified against the known
public hash, with a from-scratch SHA-1 implementation.

## 1. The wrong instrument first  `kept`

The first test, do adjacent words of the raw 16-word block differential multiply to exactly zero in
T32/GF(2), was negative on both real near-collision blocks, as it had been on an earlier toy-data
control. The reason: exact zero-divisor pairs are a sparse locus in T32 and a full-weight differential
essentially never lands on it by that test, collision or not. Recorded under the policy that failed
predictions stay in the record.

## 2. The right instrument: the expanded message schedule  `MEASURED`

The paper's claim concerns L, the XOR-linear component of the full round structure (the
80-word schedule recurrence plus the Parity rounds), not a raw word-pair check. Expanding both
real near-collision blocks to their 80-word schedules with SHA-1's linear recurrence
Wₜ = ROL₁(Wₜ₋₃ ⊕ Wₜ₋₈ ⊕ Wₜ₋₁₄ ⊕ Wₜ₋₁₆) and taking the word-wise differential:

**Listing 1 — the SHAttered schedule differential** (written for this page; python3 standard library; runs cold from the repository root)

```python
import struct, hashlib
a = open('TuringStack/shattered_data/shattered-1.pdf', 'rb').read()
b = open('TuringStack/shattered_data/shattered-2.pdf', 'rb').read()
print('sha1 equal:', hashlib.sha1(a).hexdigest() == hashlib.sha1(b).hexdigest(), hashlib.sha1(a).hexdigest(),
      '| sha256 equal:', hashlib.sha256(a).digest() == hashlib.sha256(b).digest(), '| sizes', len(a), len(b))
diff_blocks = [i for i in range(len(a) // 64) if a[64*i:64*i+64] != b[64*i:64*i+64]]
print('differing 64-byte blocks:', diff_blocks)
rol = lambda x, n: ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF
def sched(blk):
    w = list(struct.unpack('>16I', blk))
    for t in range(16, 80): w.append(rol(w[t-3] ^ w[t-8] ^ w[t-14] ^ w[t-16], 1))
    return w
for i in diff_blocks:
    d = [x ^ y for x, y in zip(sched(a[64*i:64*i+64]), sched(b[64*i:64*i+64]))]
    print('block', i, ': exact-zero schedule words:', sum(1 for x in d if x == 0), 'of 80; indices', [t for t, x in enumerate(d) if x == 0])
    print('   Hamming weights, rounds 60-79:', [bin(x).count('1') for x in d[60:80]])
```

```
sha1 equal: True 38762cf7f55934b34d179ae6a4c80cadccbb7f0a | sha256 equal: False | sizes 422435 422435
differing 64-byte blocks: [3, 4]
block 3 : exact-zero schedule words: 11 of 80; indices [30, 31, 35, 55, 58, 61, 62, 63, 64, 65, 66]
   Hamming weights, rounds 60-79: [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 3, 2]
block 4 : exact-zero schedule words: 11 of 80; indices [30, 31, 35, 55, 58, 61, 62, 63, 64, 65, 66]
   Hamming weights, rounds 60-79: [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 3, 2]
```

It reproduces the earlier record exactly: 11 of 80 expanded schedule words are exactly zero (indices
30, 31, 35, 55, 58, 61–66), with six exact zeros in a row starting at round 61 as the algorithm
re-enters its linear round window. The two differing blocks (3 and 4, the two near-collision
blocks) give the *same* differential (by the attack's construction, per the cryptanalysis literature; not re-derived here). The two
files agree under SHA-1 (38762cf7…) and differ under SHA-256.

Since the XOR-difference over GF(2) is T32 addition, "the differential is zero" and "these words are
algebraically identical" are one statement. The framework's reading is that the collapse is read off
a fact already in the algebra, in the way `is_nilpotent()` does not create nilpotency
([78](78_t32_nilpotency.md)). The author's phrasing: "we didn't have to XOR it … it's encoded into
the geometry … now I understand XOR."

## 3. What the measurement is, and is not

Where the differential vanishes is determined by the differential path the attackers constructed
(the disturbance vector of the SHAttered attack), so the exact zeros are a designed property of the
collision, documented in the SHA-1 cryptanalysis literature. The framework's addition is the
reading of those zeros as a locus in the T32/GF(2) algebra. That reading is `INTERPRETATION`; the
exact-zero positions are measured facts, reproducible from the two public files.

## 4. Honest scope

No preimage, no forgery, no new attack on SHA-1. This is a retrospective geometric
characterisation of an already-broken hash, verified against the real published collision
instead of asserted. The scope `paper.tex` has held stands unchanged.

## 5. Related pages

[78 T32 nilpotency](78_t32_nilpotency.md) · [21 Chladni, Zipf, Riemann](21_chladni_zipf_riemann.md) ·
[79 the boundary-crossing alarm](79_prime_gate_alarm.md) · [135 findings ledger](135_engine_findings_ledger.md)
