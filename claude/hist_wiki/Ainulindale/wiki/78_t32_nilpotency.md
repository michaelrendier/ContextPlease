# 78 — T32 NILPOTENCY: ONE SHARED MECHANISM, TWO REPOS

**Author:** Claude Sonnet 5 (derivation), prompted and directed by Cody Michael Allison
**Date:** 2026-07-11
**Status:** Primitives ESTABLISHED (verified byte-for-byte against source). Both current uses of them are explicitly NOT validated — one already failed a control, one hasn't been tested that way yet.
**Predecessor:** [wiki/77 — Hypergon Constructibility](77_hypergon_constructibility.md)
**Cross-ref:** `ValaQuenta/modules/t32_nilpotency/`, `ValaQuenta/modules/hypergon_constructibility/` (now imports from here instead of duplicating), `FourthAgePapers/FermatMonster/engine/fermat_monster_engine.py` (`t32_nilpotency_check()`, new cross-repo import)

---

> *"Separate but importable engine into the n-shape engine."*
> — Cody Michael Allison, 2026-07-11

---

## 1. Why Separate

The factoring engine built the session before this one (`hypergon_constructibility`) needed the Hyperwebster address + T32/GF(2) machinery, and building it exposed two real bugs — a placeholder function claimed, without checking, to match the real source, and a hand-transcribed character table that was simply wrong. Both were caught, but only by numbers not matching, not by careful reading. Splitting this into its own module — `t32_nilpotency` — and having every consumer import from the one place removes the entire failure mode: there's now one implementation to get right, not several copies that can quietly diverge.

## 2. Wired Into the N-Shape Engine

`fermat_monster_engine.py` (FourthAgePapers/FermatMonster) gained a new function, `t32_nilpotency_check()`, that imports `t32_nilpotency` across repos (via `sys.path`, falling back to `None` rather than failing silently if unavailable) and tests its own `MOONSHINE_PRIMES` list for nilpotency, cross-referenced against which of them fill the Niemeier gap {e1, e11, e15}.

## 3. Raw Result

```
overall_nilpotent_pct                  = 80.0%
gap_filling_primes_nilpotent_pct (n=5) = 100.0%
non_gap_primes_nilpotent_pct (n=10)    = 70.0%
```

All five gap-filling primes (11, 17, 31, 47, 59) are nilpotent. Worth naming honestly: at a 70% baseline, 5/5 by pure chance happens roughly 1 time in 6 — a real number, not yet strong evidence. This has not been run through the magnitude-matched control that already caught the *other* use of this same mechanism (factoring, in `hypergon_constructibility`) failing. Until it has, this correlation should be held with the same open hand.

## 4. The Standing Lesson, Restated

This is the second engine this session where the actual value turned out to be as much about catching what doesn't hold up as what does — the factoring conjecture failed a control it had never been given; two real transcription bugs were caught building the tooling to test it. Neither is a setback to the record. Both are exactly what "let the maths speak" is for.
