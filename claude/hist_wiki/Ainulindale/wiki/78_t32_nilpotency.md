# 78 — T32 Nilpotency: One Shared Mechanism, Two Repositories

| | |
|---|---|
| Scope | the separate `t32_nilpotency` module (Hyperwebster address → T32/GF(2) element → nilpotency test); its wiring into the N-shape engine; the raw result and its chance baseline |
| Origin | 2026-07-11, derived by Claude Sonnet 5, directed by the author: "Separate but importable engine into the n-shape engine." |
| Predecessor | [77](77_hypergon_constructibility.md) |
| Code | `ValaQuenta/modules/t32_nilpotency/` (`hw_address`, `hw_to_t32`, `t32_mul`, `is_zero_divisor_pair`, `is_nilpotent`, `prime_nilpotency_report`, and from 0.110/0.120 `radical_census`, `trace_laplacian`, `nilpotency_window`, `matched_prime_control`); `FourthAgePapers/FermatMonster/engine/fermat_monster_engine.py` (`t32_nilpotency_check()`); `hypergon_constructibility` now imports from here |
| Confidence | the primitives, the square law and the detector: ESTABLISHED · the two uses: not validated: one failed its control ([77](77_hypergon_constructibility.md)); this one now has one (§6) and does not stand out against primes of its size |
| Last verified | 2026-11-26: §§3, 5, 6 re-run (`modules/t32_nilpotency` 0.120, 14 tests); the interactive pages are in `ValaQuenta/gallery/t32_nilpotency/` |

## 1. Why separate

The factoring engine of [77](77_hypergon_constructibility.md) needed the Hyperwebster address and the T32/GF(2) machinery and
exposed two bugs (a placeholder claimed to match the source; a hand-transcribed character table
that was wrong). Both were caught only by numbers failing to match. Splitting the machinery into
one module that every consumer imports removes the failure mode of several copies that can
diverge.

## 2. Wired into the N-shape engine

`fermat_monster_engine.py` gained `t32_nilpotency_check()`, which imports `t32_nilpotency` across
repositories (via `sys.path`, falling back to `None` and not failing silently) and tests its own
`MOONSHINE_PRIMES` list for nilpotency, cross-referenced against the primes that fill the Niemeier
gap {e₁, e₁₁, e₁₅}.

## 3. The raw result, re-run  `MEASURED`

**Listing 1 — nilpotency of the 15 Moonshine primes, split by the Niemeier-gap set** (needs the installed ValaQuenta package; runs from any directory)

```python
import importlib
t3 = importlib.import_module('ValaQuenta.modules.t32_nilpotency.maths')
MOON = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]; gap = [11, 17, 31, 47, 59]
nil = {p: t3.is_nilpotent(t3.hw_to_t32(p)) for p in MOON}
print('nilpotent:', [p for p in MOON if nil[p]], ' (%d of 15 = %.0f%%)' % (sum(nil.values()), 100 * sum(nil.values()) / 15))
print('gap-filling primes all nilpotent:', all(nil[p] for p in gap), ' non-gap:', sum(nil[p] for p in MOON if p not in gap), '/ 10')
print('chance of 5/5 at a 70%% baseline: %.3f = 1 in %.1f' % (0.7**5, 1 / 0.7**5))
```

```
nilpotent: [3, 5, 11, 13, 17, 23, 29, 31, 41, 47, 59, 71]  (12 of 15 = 80%)
gap-filling primes all nilpotent: True  non-gap: 7 / 10
chance of 5/5 at a 70% baseline: 0.168 = 1 in 5.9
```

This reproduces the record: overall 80 %, gap-filling 100 % (n = 5), non-gap 70 % (n = 10). At a 70 %
baseline, 5 of 5 nilpotent happens by chance about 1 time in 6, so the correlation is not strong
evidence. It has **not** been run through the magnitude-matched control that caught the factoring use
failing ([77](77_hypergon_constructibility.md) Listing 1), and until it has, it is held as an observation.
(The non-nilpotent Moonshine primes in the run are 2, 7 and 19.)

## 4. The standing lesson

For the second time in a session the value lay as much in what failed a control (the factoring
conjecture) and in the bugs caught building the tooling as in what held. Both belong in the
record: failed results stay in documentation and code.

## 5. Related pages

[77 hypergon constructibility](77_hypergon_constructibility.md) · [81 SHA-1 collision geometry](81_sha1_real_collision_geometry.md) ·
[135 findings ledger](135_engine_findings_ledger.md)

## 5. The square law and the detector (added 2026-11-26)

`MEASURED`, `modules/t32_nilpotency` 0.110, tests `tests/test_t32_nilpotency.py`:

- **Square law.** In T32/GF(2) every x has x² ∈ {0, e₀}. Each element is nilpotent (x² = 0, the radical) or an involutory unit (x² = e₀). At dim 8, exhaustively: 128 nilpotent (counting 0), 128 involutory, 0 other.
- **One detector.** Δ(w) = w·𝟏 (𝟏 = all ones) vanishes exactly when w² = 0: exhaustive at dim 2, 4, 8; no mismatch in 20,000 random words at dim 32.
- **Corrected lemma** (2026-08-22, supersedes the UDEO white-paper proof): 𝟏 is not a global annihilator (e₀·𝟏 = 𝟏 ≠ 0); only the iff holds. The older statement stays in the record as withdrawn.
- The 11 of 16 (sedenion basis primes) and 12 of 15 (Moonshine primes) nilpotent counts are counts, not a signal; the controls of §3 and [77](77_hypergon_constructibility.md) still apply.

## 6. The control the page lacked (added 2026-11-26)

`MEASURED`, `modules/t32_nilpotency` 0.120 (`nilpotency_window`, `matched_prime_control`; tests `tests/test_t32_nilpotency.py`).

§3 compared the five gap primes with a "70 % baseline", the observed rate of the ten other Moonshine primes. That is not a chance rate. The square law (§5) gives one: a random word is nilpotent half the time (0.4961 in 20,000 random 32-bit words), and the Hyperwebster words of the integers are nilpotent half the time too:

| range | primes | composites | composites ending 1, 3, 7, 9 |
|---|---|---|---|
| 10 – 99 | 17 / 21 = 0.81 | 29 / 69 = 0.42 | 4 / 15 = 0.27 |
| 100 – 999 | 70 / 143 = 0.49 | 377 / 757 = 0.50 | 107 / 217 = 0.49 |
| 1,000 – 9,999 | 523 / 1,061 = 0.49 | 3,974 / 7,939 = 0.50 | 1,285 / 2,539 = 0.51 |
| 10,000 – 99,999 | 4,232 / 8,363 = 0.51 | 40,752 / 81,637 = 0.50 | 13,750 / 27,637 = 0.50 |

All of the excess seen in the 16 sedenion basis primes (11 of 16) and the 15 Moonshine primes (12 of 15) is the two-digit window; from three digits up primes and composites are indistinguishable. The prime-matched control draws the same number of random primes up to the same maximum: P(5 of 5) = 0.127 for the gap set (primes up to 59; 1 in 8, against 1 in 5.9 at the old 70 % and 1 in 32 at the random-word 50 %), and P(≥ 12 of 15) = 0.36 for the Moonshine set in its pool of 20 primes. The 16 sedenion basis primes are every prime up to 53, so their own control is vacuous. **Reading:** the gap-prime result is unremarkable against primes of its own size, so this use has now met a control and does not stand out; it stays an observation, and the factoring verdict of [77](77_hypergon_constructibility.md) is untouched. The "+26 pp nilpotent bias of primes" in VAPMIP Tuning-the-Engine 19 (a 50 % baseline, 2026-06-30) is the same small-range effect; Tuning-the-Engine is not edited, and [135](135_engine_findings_ledger.md) X-60 is its correction. Why the two-digit window differs (a 90-number table whose pattern depends on the two decimal digits through the base-97 address) is not explained here.

## 7. The closed form behind the square law (added 2026-11-26)

`MEASURED`, `modules/t32_nilpotency` 0.130 (`weight_parity`; tests `tests/test_t32_nilpotency.py`). Chasing the two-digit anomaly of §6 to its source:

- **w·w = (popcount(w) mod 2)·e₀.** The square of a word is the parity of its number of 1 bits: every word at d ≤ 16, 20,000 random words at d = 32. Nilpotent means an *even* number of 1 bits; involutory means *odd*. (§5 said the class of a word had no known rule; that is withdrawn.)
- Δ(w) = w·𝟏 = parity(w)·𝟏; **parity(a·b) = parity(a)·parity(b)** for every pair at d ≤ 8: the weight parity is a ring homomorphism T32 → GF(2), and the radical is its kernel, the even-weight words: closed under XOR, dimension d − 1, an ideal.
- The nilpotency indicator of the Hyperwebster word of n is the **Thue–Morse sequence** of the address. That is why primes and composites are both ½ from three digits up. (Post-Hoc: Mauduit and Rivat, Ann. of Math. 171 (2010), find the binary digit sum of primes equidistributed; the address here is not the prime, so this is a parallel, not a proof.)
- The two-digit excess (17 of 21 primes, 29 of 69 composites) is one 90-number table: one-sided hypergeometric P = 0.0016 for primes among the 90, chosen after looking (the 16 sedenion basis and 15 Moonshine primes are small), so a look-elsewhere number; it is gone at three digits (70 of 143). **Open:** why three digits wash it out. The author's reading, that three digits carry the three-part structure (inclination, declination, distance; Add:Scale:Sign), is consistent with the data and untested.
