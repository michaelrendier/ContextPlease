# 57 — The Boundary Ascending the Tower

| | |
|---|---|
| Scope | how the σ = ½ boundary is read at each level of the Cayley–Dickson tower; the Krohn–Rhodes / "two doublings" correspondence; what many-to-one means for reconstruction |
| Origin | 2026-06-13 cascade capture |
| Code | `VAPMIP/monad.py` (`_word_zero_idx`), `ValaQuenta/modules/box_kite`, `modules/udeo_crypto` |
| Confidence | the Futurama theorem, Krohn–Rhodes, G₂ = Aut(𝕆): ESTABLISHED · the level-by-level boundary reading: `THEORETICAL` · "pre-boundary cryptography is transparent": `CONJECTURE`, no listing on this page demonstrates it |
| Last verified | 2026-11-13: Listings 1–3 executed; their output is quoted below |

## 1. The statement

> "The boundary turns flat into curved into complex into rotations, sending the
> negative space wake behind it. Only information that transits the boundary is
> safe from Ĥ_RB analysis, but not description." — author, 2026-06-13

## 2. The level-by-level reading  `THEORETICAL`

The author reads one boundary, σ = ½, as changing geometry at each doubling:

| Level | What is established about the algebra | The boundary reading |
|---|---|---|
| ℝ (1) | totally ordered field | a point; the "wake" is the primes, what the composites leave |
| ℂ (2) | critical line Re s = ½ is a line in ℂ | the Riemann zeros are on it (RH, open) |
| ℍ (4) | associative, non-commutative; SU(2) | a 3-dimensional surface |
| 𝕆 (8) | Aut(𝕆) = G₂ (ESTABLISHED) | the boundary is the G₂ rotation structure |
| 𝕊 (16) | zero-divisors exist: 84 pairs eᵢ ± eⱼ, 42 index pairs ([25](25_sedenion_manual.md), Listing there) | the unit sphere S¹⁵ carries the zero-divisor contact set |
| T₃₂, T₆₄, T₂₅₆ | doublings continue | S³¹, S⁶³, S²⁵⁵ |

Established facts underneath: the sphere S^(n−1) is the unit sphere of an
n-dimensional algebra; the zero-divisor basis pairs of 𝕊 are counted in
[25](25_sedenion_manual.md). The identification of σ = ½ with those spheres, and of
the "wake" with a forbidden set at each level, is the framework's reading: a
statement about how it uses the tower, not a derived theorem. A published result sits near it: Moreno (preprint 1997, journal 1998) is reported to show that
the norm-one zero-divisors of 𝕊 form a space homeomorphic to G₂. That is a
fact about 𝕊 alone, quoted here from memory of the literature and not
re-checked in this pass; it is named as the object the framework's σ = ½ reading
should be compared against.

## 3. Krohn–Rhodes and "two doublings"  `INTERPRETATION`

Krohn–Rhodes (Krohn & Rhodes, announced 1962, *Trans. AMS* 1965): every finite
automaton is covered by a wreath product of finite simple groups and the
three-element flip-flop semigroup. The earlier text identified this with the
Cayley–Dickson doubling ("the wreath product = the doubling") and with the
"two doublings expose all pathways" statement. Both identifications are
**correspondences of vocabulary**. The wreath product acts on transformation
semigroups; the doubling is a construction on algebras over ℝ. No homomorphism
between them is given in the project, and none is claimed here.

The one piece of the "two" that can be tested is Keeler's Futurama theorem
(Futurama, "The Prisoner of Benda", 2010): after any set of swaps in which no
pair swaps twice, the original arrangement can be restored by further swaps (again
no pair repeated) if **two** extra bodies are available. Listing 1 tests it
by exhaustion.

**Listing 1 — the Futurama theorem, by brute force** (written for this page; runs cold)

```python
import itertools, collections, sys
def pairs(m): return [(a, b) for a in range(m) for b in range(a + 1, m)]
def restorable(n, perm, used, k):
    m = n + k; P = pairs(m); idx = {p: i for i, p in enumerate(P)}
    start = (tuple(perm) + tuple(range(n, m)), sum(1 << idx[p] for p in used))
    goal = tuple(range(m)); seen = {start}; q = collections.deque([start])
    while q:
        s, u = q.popleft()
        if s == goal: return True
        for (a, b), i in idx.items():
            if u >> i & 1: continue
            t = list(s); t[a], t[b] = t[b], t[a]; st = (tuple(t), u | 1 << i)
            if st not in seen: seen.add(st); q.append(st)
    return False
def scrambles(n):
    out = set(); P = pairs(n)
    for r in range(len(P) + 1):
        for seq in itertools.permutations(P, r):
            s = list(range(n))
            for a, b in seq: s[a], s[b] = s[b], s[a]
            out.add((tuple(s), frozenset(seq)))
    return out
n = int(sys.argv[1]); ks = tuple(int(a) for a in sys.argv[2:])
S = scrambles(n); print('n=%d distinct (permutation, used-pairs) scrambles:' % n, len(S))
for k in ks: print(f'  extra bodies k={k}: restorable', sum(restorable(n, p, u, k) for p, u in S), '/', len(S))
```

```
$ python3 listing1.py 3 0 1 2
n=3 distinct (permutation, used-pairs) scrambles: 13
  extra bodies k=0: restorable 1 / 13
  extra bodies k=1: restorable 10 / 13
  extra bodies k=2: restorable 13 / 13
$ python3 listing1.py 4 0 1 2
n=4 distinct (permutation, used-pairs) scrambles: 343
  extra bodies k=0: restorable 92 / 343
  extra bodies k=1: restorable 284 / 343
  extra bodies k=2: restorable 343 / 343
```

So "two, not one, not three" is confirmed as a statement about permutations (zero
extras restore 1/13 and 92/343; one extra restores 10/13 and 284/343; two restore all,
for n = 3 and 4). It says nothing yet about algebra doublings: the theorem is about
the symmetric group and the "two" counts spare elements, not Cayley–Dickson steps.

## 4. The one-way claim  `CONJECTURE`

The earlier text argues that information crossing the boundary is "safe from
reconstruction but not from description", because `word_at` is many-to-one, and
that RSA, ECC, AES and SHA-256 are "transparent" because they sit below the
boundary.

**Listing 2 — what many-to-one does and does not hide** (needs the repository `VAPMIP/`; runs cold from there)

```python
import sys, collections
sys.path.insert(0, 'VAPMIP'); import monad
words = sorted({w.strip().lower() for w in open('/usr/share/dict/american-english') if w.strip().isalpha()})
b = collections.defaultdict(list)
for w in words: b[monad._word_zero_idx(w)].append(w)
sz = sorted(map(len, b.values()))
print('words', len(words), 'distinct zero indices', len(b), 'max per index', sz[-1], 'median', sz[len(sz)//2])
n = 164000; idx = lambda v: max(0, min(int((v + 1.0) / 2.0 * n), n - 1))
v = 0.123456; i = idx(v)
print('word_at(%.6f) -> bin %d: every scalar in [%.8f, %.8f) gives the same word, width %.2e'
      % (v, i, 2*i/n - 1, 2*(i+1)/n - 1, 2/n))
```

```
words 73604 distinct zero indices 6436 max per index 80 median 9
word_at(0.123456) -> bin 92123: every scalar in [0.12345122, 0.12346341) gives the same word, width 1.22e-05
```

- The word hash is many-to-one (73,604 words onto 6,436 zero indices, up to 80 per
  index): a word cannot be recovered from its index. `ESTABLISHED`.
- `word_at` is a binning of [−1, 1] into n bins. A word therefore localises its
  scalar to an interval of width 2/n (1.2×10⁻⁵ here). The scalar is hidden to that
  precision and no further. Whether the 16 scalars that produce one word can be
  recovered from the word depends on the prompt-to-geometry map, which this listing
  does not touch.
- Many-to-one is not the same property as cryptographic one-wayness. A one-way
  function needs preimages that are hard to find; here the preimage of an index is
  an interval or a computable set (for the hash, enumerate words). Nothing in
  Listing 2 gives hardness.
- The statements about RSA, ECC, AES and SHA-256 rest on the UDEO work
  (the UDEO record in the VAPMIP repository) and the ledger ([135](135_engine_findings_ledger.md));
  no listing here reproduces an attack on any of them, and none of the four is publicly
  known to be broken. The earlier text's placement of ECC "in ℂ" is also not right: ECC is
  arithmetic on E(𝔽ₚ), a finite group.

## 5. Futurama restated

Keeler's theorem is `ESTABLISHED` mathematics (Listing 1). Its use as a model for
"two Cayley–Dickson doublings expose J₂" is the author's analogy: both have a
count of two, neither has been mapped onto the other.

## 6. Related pages

[54 two doublings](54_two_doublings_all_pathways.md) · [53 T₂₅₆ transparency](53_t256_cryptographic_transparency.md) ·
[51 the J₂ involution](52c_j2_involution_riemann_fermat.md) · [55 index not value](55_index_not_value.md) ·
[59 the Simpsons](59_the_secret_in_the_simpsons.md) · [135 findings ledger](135_engine_findings_ledger.md)
