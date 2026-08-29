# Collatz as the 2-adic Shift

Session origin: 2026-08-21. Cody, out of a run of pathway-mathematics reading:

> *"multiple inputs to one small ordered loop… Collatz Conjecture… I see a
> recursive decomposition on a modular function… what actually is it"*

The observation is correct, the object has a name, and this page says what it is.

**Status:** analysis result. **No claim, no prediction.** Every result carries a
provenance label. See `FourthAgePapers/CollatzShift/README.md` for the scorecard
and `engine/e_collatz_shift.py` for the measurements.

---

## 1. The map, and the address

The **shortcut map**, one halving folded into the odd branch so every step does
work:

```
T(n) = n/2         n even
T(n) = (3n+1)/2    n odd
```

Record the even/odd decision at each step and you get the **parity word** — a
sequence of bits. That word is not a summary of the orbit. It is a **coordinate**:
the 2-adic address of `n`, and the orbit is what you get by reading the address
from the left.

Measured, exhaustively to `k = 16` (65536 of 65536, no sampling):

> `Q_k : Z/2^k → Z/2^k`, `n ↦ its first k parities`, is a **bijection**, and
> `Q(T(n)) = shift(Q(n))`.

**The Collatz map is the one-sided binary shift.** Not analogous to it —
conjugate to it, by a measure-preserving homeomorphism. This is Bernstein (1994)
and Bernstein–Lagarias (1996); the engine re-measures it rather than citing it.

---

## 2. The recursive decomposition on a modular function — named

`T^k` restricted to a residue class mod `2^k` is an **affine map**:

```
n ≡ j (mod 2^k)   ⟹   T^k(n) = (3^d · n + c) / 2^k
```

with `d` = the number of odd steps, and `d` depending **only on the class**, never
on `n`. There are `2^k` such pieces; refining `k → k+1` splits every branch in
two.

That is the whole structure Cody was seeing. The "modular function" is the
indexing of the pieces by `Z/2^k`; the "recursive decomposition" is the
refinement. It is an iterated function system whose address space is the parity
word.

Verified for every class at every `k ≤ 8` — 510 classes, slope `3^d/2^k` in all of
them.

---

## 3. The tessellation — why the chaos is apparent

The intuition Cody arrived at from Hilbert, Koch and dragon curves — *"they seem
chaotic but are just tessellated"* — is exactly right here, and it is measurable.

Count, over the `2^k` classes mod `2^k`, how many odd steps each one takes:

```
k=8   {0:1, 1:8, 2:28, 3:56, 4:70, 5:56, 6:28, 7:8, 8:1}
```

**That is `C(8,d)`.** Exact binomial at every `k` up to 12, with no error term.
The branch structure of the Collatz tree is **Pascal's triangle** — the most
ordered combinatorial object there is — read through a metric that scrambles it.

A dragon curve is a paperfolding sequence read off binary digits; a Hilbert curve
is a base-4 address; the Collatz orbit is a base-2 address. Same category of
object: **a p-adic address rendered in the archimedean metric, which is what makes
it look like chaos.**

And the second half of Cody's intuition — *"chaos in multiple dimensions becomes
order, which we see in the normal curve"* — follows from the first half as a
theorem rather than as an observation. `log n` along an orbit is a sum of `k` iid
log-steps whose count is `Binomial(k, ½)`, so its limit is Gaussian by **de
Moivre–Laplace**. Measured at `k = 20`: `sup|binomial CDF − normal CDF| =
0.00139`, exact binomial, no sampling. The normal curve here is not an empirical
finding about Collatz. It is R4 in the limit.

---

## 4. The cycles, and the "near miss"

Every **periodic** parity word of length `k` with `d` ones determines exactly one
**rational** cycle, and its denominator is always `2^k − 3^d`:

| word | k | d | `2^k − 3^d` | x |
|---|---|---|---|---|
| `10` | 2 | 1 | **1** | **1** |
| `11` | 2 | 2 | −5 | −1 |
| `100` | 3 | 1 | 5 | 1/5 |
| `11000` | 5 | 2 | 23 | 5/23 |
| `1101000` | 7 | 3 | 101 | 23/101 |

A cycle is an **integer** cycle only when `2^k − 3^d` divides the numerator, and
`2^k − 3^d = 1` happens at `(k,d) = (2,1)` and nowhere else (Levi ben Gerson /
Catalan, cited not proved). **That single fact is why `1 → 2 → 1` is the
exceptional loop.** Every other parity word gives a perfectly good cycle that
simply does not land in `Z`.

Enumerating **primitive** necklaces to `k = 16`: exactly one positive-integer
cycle, `{1,2}`.

The candidate shapes are the continued-fraction convergents of
`log₂3 = 1.58496250`:

```
k/d = 2/1, 3/2, 5/3, 8/5, 13/8, 19/12, 84/53 → 1.58490566
2^19 − 3^12 = −7153      2^84 − 3^53 = −40432553845953101497907
```

### On the word "near miss"

This ladder is a **linear form in logarithms**: how close `k·log2` can come to
`d·log3` without equalling it. That is the same **family** as the Fermat
near-miss work (`FourthAgePapers/FermatMonster`,
`VAPMIP/engines/e14_fermat_near_miss.py`) — in both cases the question is how
closely towers of small primes can approach one another without touching.

It is **not the same problem**, and it is **not the Riemann Hypothesis**. What RH
and this share is only the underlying arena: a lattice generated by logarithms of
small primes, and how well it approximates a target. Recorded as a family
resemblance so that it does not get promoted to an identity later.

---

## 5. The direction result — up the tower vs down it

Cody, same session:

> *"going up the tower (reals to sedenion) is not information propagation; going
> down the tower (sedenion to real numbers) is information propagation"*

In this system that is measurable, and it comes out clean.

**Down** — the forward map. `T` is well defined as `Z/2^k → Z/2^(k-1)`, and every
fibre has **exactly 2** elements, at every level, with no exceptional fibre. So
each forward step destroys **exactly one bit**: `log 2` nats. The destroyed bit
never returns — provenance is discarded, exactly as `intention_monad.py` discards
it on collection.

**Up** — the backward tree. `n` always has the predecessor `2n`, and has an *odd*
predecessor iff `n ≡ 2 (mod 3)`, a density-`1/3` set. Mean out-degree measured
over `n < 10⁶`: **`4/3`**, not `2`.

```
forward  destroys   log 2      = 0.693147 nats/step
backward restores   log(4/3)   = 0.287682 nats/step
shortfall                      = 0.405465
log(3/2)                       = 0.405465     ← exact
```

**The shortfall between the two directions is `log(3/2)` exactly — the odd
branch's own gain.** Going up enumerates possibilities and propagates nothing;
going down propagates, and what propagates is the address. The gap is the
arithmetic the 2-adic metric cannot see, priced per step.

> ⚠ **Correction kept on the record.** The odd-predecessor condition is usually
> written *"`n ≡ 2 (mod 3)` **and** `(2n−1)/3` is odd"*. The second half is
> **vacuous** — `2n−1` is odd and `3` is odd, so the quotient is odd whenever it
> is an integer at all. The first run of the engine predicted `7/6` from that
> phantom condition and returned MATHS-FAULT. The engine now *measures* the
> vacuity instead of assuming it, the density is exactly `1/3`, and the shortfall
> comes out exact. The fault improved the result.

---

## 6. Why `σ = ½` is not a metaphor here

The shift is Bernoulli(½,½) under Haar measure, and the conjugacy of §1
**preserves** that measure. So half the steps are `×½` and half are `×3/2`, and
the per-step geometric mean is `√3/2 = 0.866 < 1`.

```
predicted   ½·log(3/2) + ½·log(½) = log(√3/2) = −0.143841
measured    −0.139102   over 2,157,078 steps, odd starts < 60,000
```

The residual `+0.0047` is **termination bias** — the sample stops at `1`, which
truncates the low tail. Stated, not corrected for, not hidden.

The critical parity fraction where the drift vanishes is `log2/log3 = 0.630930`.
The system contracts *because* the two branches are balanced, and `½` sits below
the critical value with margin. Same shape as the reading of `∅_RB` in
`.clauderc_canonical_maths`: self-adjointness is downstream of `J_red = J_blue`,
not assumed alongside it. Here the contraction is downstream of the balance.

---

## 7. The lineage verdict

Decomposed against the `generational-lineage` operation domain:

```
operation                  tier  descends from             status
n mod 2  (branch select)   t0    SIGN                      PRIMITIVE — one bit, nothing between
n / 2                      t1    SCALE → DILATE, gain ½    derived — changes length
3n                         t1    SCALE → DILATE, gain 3    derived — changes length
+ 1                        t0    ADD                       PRIMITIVE — identity 0
T = the Collatz map        t3    ADD ∘ SCALE ∘ SIGN        DERIVED — no new generator
```

**No new generator required.** `T` is the smallest non-trivial composition using
all three tier-0 irreducibles at once — and that is exactly why it is hard. ADD
and SCALE have **different identities** (`0` and `1`), and the `+1` is the only
thing coupling the two axes. Drop it: `n → 3n/2^v` is a pure SCALE tower,
strictly `×3` forever, with no conjecture in it.

No section-5 emergence signature fires. The one that came closest — *a fixed set
of the wrong dimension* — resolves: the fixed points of `T` in `Z` are `{0, −1}`,
the two constant parity words, and on `N` the attractor can only be a **loop**,
because every positive integer's word must alternate. Cody's *"one small
**ordered** loop"* is forced, not incidental.

---

## 8. Where the framework speaks — and one place it does not

- **`intention_monad.py`** — set the GC root to `{1}`. The Collatz conjecture is
  then the collector's completeness claim: **run it on `N` and it collects
  nothing**; the kernel is empty. And the descent is monotone in exactly the
  designed sense — one parity bit consumed per step, never restored.
- **`sieve_clock.py`** — the mod-3 leaves are the ORPHAN regime, with one
  difference the instrument does not currently model: a sieve orphan at `N` is
  adopted at `2N` (bounded by universe size); a Collatz orphan is **never**
  adopted (bounded algebraically). **Two kinds of orphan.**
- **`L_(I|O)`** — forward is deterministic and free; backward is a branching tree
  gated by a `mod 3` test. Forward throws away one bit per step, backward must
  guess it. **The parity word is the private key** — the same shape as *speaking
  English is easy, the inverse is factoring the modulus*.
- **`0_RB = e₀`** — the attractor is the identity. "Every trajectory falls into
  the identity" is the conjecture in this project's vocabulary.

### ⚠ The Two Trees do NOT split even/odd

Telperion = prime, Laurelin = composite. Even/odd is divisibility by 2, not
primality: `2` is prime and even, `9` is composite and odd. **The tempting
mapping is wrong** and is written down here as wrong so it does not get made
later.

The defensible Two Trees reading of Collatz is at the **tower** level, not the
integer level: the 2-tower (contracting, `×½`) against the 3-tower (expanding,
`×3/2`), with the Mingling at `log₂3 = 1.58496` — which is precisely where every
candidate cycle must live (§4).

---

## 9. What is open

- **The whole conjecture.** Nothing here bears on it, in either direction.
- **Two kinds of orphan.** Temporary (adopted at `2N`) vs permanent (algebraic).
  Not modelled anywhere in the framework.
- **Is `log(3/2)` per step the right price?** It is exact for this map. Whether
  the same construction on `(pn+1)/q` yields `log(p/q)` is untested.

---

## Files

```
FourthAgePapers/CollatzShift/
  README.md                      the scorecard
  engine/e_collatz_shift.py      10 relations, stdlib only, ~4s
  00_vision.ipynb                the question, and what is not claimed
  01_measurements.ipynb          the relations, plus R1/R4/R6 by hand
  02_lineage.ipynb               the decomposition and the emergence check
  03_results.ipynb               the scorecard and the three faults
  wiki/Collatz-as-the-2-adic-Shift.md   this page
```

Working notes: `ContextPlease/claude/scratchpad/2026-08-21_collatz_shift_conjugacy/`.
