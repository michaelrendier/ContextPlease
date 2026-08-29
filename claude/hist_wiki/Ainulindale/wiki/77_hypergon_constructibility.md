# 77 — HYPERGON CONSTRUCTIBILITY: ALL 16, AND THE FACTORIZATION TEST THAT DIDN'T SURVIVE

**Author:** Claude Sonnet 5 (derivation), prompted and directed by Cody Michael Allison
**Date:** 2026-07-11
**Status:** Part 1 ESTABLISHED (real classical mathematics, verified directly). Part 2 an honest, re-tested NEGATIVE result — not smoothed into a partial positive.
**Predecessor:** [wiki/76 — Sigma Expansion](76_sigma_expansion.md), [wiki/75 — The Abrikosov Lattice](75_abrikosov_lattice.md)
**Cross-ref:** `ValaQuenta/modules/hypergon_constructibility/`, `ValaQuenta/wiki/hypergon_constructibility.md`, `ValaQuenta/notebooks/core/16_hypergon_constructibility.ipynb`, `VAPMIP/docs/wiki/Tuning-the-Engine.md` Phase 19 & 22, `TuringStack/fermat_sedenion_test.py`

---

> *"Create the factorization engine purely...test all hyper *-gons to 16 for the sedenion. Get me a good description of the definition of all the primes."*
> — Cody Michael Allison, 2026-07-11

---

## 1. Resolving a Same-Session Confusion First

Earlier the same session, "the 13-gon" was checked against the wrong object — `fermat_monster_engine.py`'s Coxeter-number/Niemeier-lattice structure, where h=13 turned out to be perfectly achievable, not extinct. The real 13-gon lives in `Tuning-the-Engine.md` Phase 19: dimension e5 (channel v[5], tied to prime 13) in the Dirichlet projection, extinct because 13 is not a Fermat prime and has no Cayley-Dickson tower anchor. This page generalizes that single example to all 16 positions, computed directly.

## 2. Part 1 — All 16 Hyper-N-Gons (Raw Result)

**Gauss-Wantzel theorem (1796/1837, real classical mathematics, not a framework-specific claim):** a regular n-gon is constructible with straightedge and compass if and only if n = 2^k × (product of distinct Fermat primes). Only five Fermat primes are known to exist, ever — 3, 5, 17, 257, 65537 — and whether more exist is a genuine open problem in number theory.

Applied to all 16 sedenion basis primes {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53}:

```
CONSTRUCTIBLE (4/16): e0=2, e1=3, e2=5, e6=17
HOLES (12/16):        e3=7, e4=11, e5=13, e7=19, e8=23, e9=29, e10=31,
                       e11=37, e12=41, e13=43, e14=47, e15=53
```

Constructibility is the exception among primes, not the rule.

## 3. Part 2 — The Factorization Engine, Tested Honestly

Phase 22 corrected the factoring conjecture from Fermat-midpoint parameters (a,b) to the actual prime factors (p,q) directly — reporting q at +26 percentage points of T32/GF(2) nilpotency above baseline. That number reproduces here for close-magnitude pairs. It does not survive a control that wasn't run before:

```
close prime pairs (real factors, small):   p=69.1%  q=76.4%
far-apart prime pairs (real factors):      p=47.4%  q=45.4%
random prime pairs (not factors of any N): p=50.5%  q=56.7%
```

The random control beats the far-apart real factor pairs on q. If the mechanism tracked genuine factoring structure, that shouldn't happen. **Verdict: artifact**, most likely of how small numbers map through the Hyperwebster base-97 address encoding, not evidence the mechanism sees factoring relationships. Reported plainly, not softened — the framework's own stated policy is that failed predictions stay in the record.

## 4. Two Bugs Caught Mid-Build — Not Hidden

Building this engine required reusing `hw_to_t32`. A first attempt used a placeholder (`n & 0xFFFFFFFF`) with an unverified docstring claim that it "matched exactly." It didn't. The fix attempt then hand-transcribed the real 97-character Hyperwebster charset from memory — fabricating a 120-character alphabetical string instead of the real QWERTY-keyboard-row mapping. Both caught by raw-number mismatches against an earlier standalone verification in this same session, not by trusting the code on sight. Final version pulled the real string via `repr()`, verified byte-for-byte and numerically identical across 21 test values before anything downstream was trusted.

## 5. The Definition of All the Primes

Two real, verified definitions — not yet unified into one:

**Arithmetic:** no non-trivial factorization. This is why AbrikosovTree's tree has primes as leaves surviving all 9 CD-tower levels — no factorization, no possible zero-divisor pair, the norm never fails.

**Geometric:** Gauss-Wantzel constructibility (Part 1) — real, verified, and the exception rather than the rule among primes.

**What connects them to actual factoring of a composite N remains open.** Part 2 closes off the one candidate bridge that looked promising in the prior session's narrower test. That is a real result — a wrong path correctly identified as wrong — not a failure to find an answer.
