# 79 — THE BOUNDARY-CROSSING ALARM: π(x) AS ONE INSTANCE

**Author:** Cody Michael Allison
**Date:** 2026-07-12
**Status:** FIRST CAPTURE — session-derived engine, `ValaQuenta/prime_gate.py`
**Predecessor:** [wiki/74 — Lagrangians Are Catastrophe Theory](74_lagrangians_are_catastrophe_theory.md), [wiki/65 — Primes as Repellors](65_primes_repellors_drift_meaning.md), [wiki/44 — Halting Problem Dissolved in UNS](44_halting_problem_uns.md), [wiki/17 — Alpha Omega d*](17_alpha_omega_d_star.md)
**Cross-ref:** ValaQuenta/prime_gate.py (`BoundaryAlarm`, `PrimeGateEngine`), ValaQuenta/wiki/prime_gate.md, ValaQuenta/notebooks/prime_gate/01_gate_alarm_vs_gap.ipynb, PtolemyHolcus monad.py (P1 hash)

---

## 0. What This Engine Is For

The engine is the alarm — a reusable crossing detector — not a test of any dataset. `BoundaryAlarm(boundary_fn)` fires once per crossing, blind to everything except that the crossing happened. π(x) is `BoundaryAlarm(is_prime)` run over the integers. The Holcus "FIRING" signal (wiki/44 — a computation reaching σ=½, "does it stop HERE, at this depth") is the identical primitive run over a σ-trajectory instead. Both are demonstrated in the code, side by side, so the primitive reads as general rather than prime-specific.

Everything below the alarm itself — the gap channel, the two spirals, the Euler-spiral aside — came up while building it. None of it is the point. A wrong answer found along the way (the Euler-spiral falsification, §5) stays on record rather than getting deleted: it may be useful again later, and deleting it would just mean re-deriving it from scratch next time it's needed.

## 1. The Split

A session working the BulletCluster L_(I|O)/polarization composite drifted into a live derivation, starting from a screenshot of a Kuen surface and ending at this engine. The load-bearing move: separating two channels that were being silently conflated.

**π(x) — the Gate Alarm.** Counts primes crossed. A monotone staircase: steps up by exactly 1 at each prime, flat everywhere else. Every alarm event is identical regardless of the gap that preceded it — gap-blind by construction, not approximation.

**g_n = p_(n+1) − p_n — the Gap Channel.** The interval between alarms. Carries all the irregularity π(x) cannot see. A size-14 gap and a size-2 gap register as the same single step in π(x).

```
gate_alarm(200) = 46          -- 46 primes <= 200, no gap information present
alarm_events[:5] = [(2,1),(3,2),(5,3),(7,4),(11,5)]   -- (prime, pi(prime))
```

## 2. The P1 Hash Connection

The gate alarm is not a new idea — it is the same ordinal-index addressing already running in `monad.py`'s P1 Prime Hash: `word → prime p → π(p) ordinal index → γ_index`. The address of a word was never the prime's value. It was always the **count** — how many primes had been crossed to reach it. This session made that convention explicit and gave it a name: the gate.

Two spirals built on the T-map (`T(x) = x·e^{i d* ln x}`, d*=0.24600) make the distinction concrete:

```
ordinal_spiral: T(n)   = n   * e^{i d* ln n}     -- address = COUNT (the gate)
value_spiral:   T(p_n) = p_n * e^{i d* ln p_n}   -- address = MAGNITUDE
```

These are not rescaled copies of one another. Radius grows as n vs. n·ln(n) (Prime Number Theorem) respectively. Using the ordinal form is a deliberate choice to discard gap information — the same blindness π(x) has by construction.

## 3. The Gap Confirms PNT Directly

```
gap_scaling_fit: slope=0.9615, intercept=0.4264   (5132 gaps, primes to 50000)
PNT prediction: slope ~ 1.0  (average gap near p ~ ln(p))
```

Linear regression of g_n against ln(p_n) reproduces the Prime Number Theorem's average-gap law numerically, not by assertion.

## 4. The Telescoping Trap

A first attempt at a "prime curvature spiral" summed gap_n directly as a heading increment: `theta_n = scale * cumsum(gap_n)`. This telescopes trivially — since gap_n is itself a first difference of p_n, any cumulative sum of it collapses back to `p_n − p_0`. The construction silently degenerated into a rescaled value_spiral, not an independent curvature signal. Caught and corrected within the same session: the honest curvature signal is `kappa_n = ln(p_n)` — smooth, not a first difference of anything in the sequence, no telescoping.

## 5. The Euler-Spiral Falsification

The corrected curve — heading built from `kappa_n = ln(p_n)` — was tested against the true Euler spiral (clothoid, Fresnel integral, κ(s)=s). Result: **falsified, on record.**

```
is_true_euler_spiral():
  is_clothoid: False
  reason: ln(p_n) is monotonic and always positive; a clothoid requires
          curvature to cross zero and reverse sign to produce two
          asymptotic eyes (Fresnel integral).
  kappa range: [0.693, 10.820], sign changes: 0
  actual topology: single-point inward spiral (involute-like)
```

A true clothoid needs κ(s) = s: linear in arc length, passing through zero, negative for s<0 — exactly why the Fresnel-integral curve has **two** symmetric asymptotic eyes (visualized in the notebook against the corrected prime curve). Prime curvature ln(p_n) never reverses sign for any n ≥ 1: it can only ever tighten into **one** inward spiral around a single center. Not a clothoid, and the engine does not pretend otherwise. This is Cody's own methodology in force — a rescale or reframing that would make the data *look* like the target shape is exactly the move that must not be made silently (cf. wiki/65's warning that the sedenion spiral is NOT the Fano cardioid — the boundary lives between them, not because it was forced to coincide).

## 6. Why the Alarm Is Useful As An Alarm

Precisely because π(x) is gap-blind, it is cheap and unambiguous as a trigger: fire once per prime, no need to know or compute spacing to decide whether to fire. The gap channel stays available as a separate query for anything that needs to reason about *when the next crossing is likely* rather than merely *that one occurred*. Keeping the two channels apart — rather than collapsing them, as the first curvature attempt did — is the actual engineering content of this result.

---

## 7. Formal Targets

- [ ] Determine whether `curvature_spiral`'s single-point convergence radius has closed form in terms of d* and the prime-counting asymptotic N(T).
- [ ] Test whether a genuine two-eye clothoid can be constructed from a *signed* prime-derived signal (e.g. Möbius μ(n) or a Red/Blue difference current à la H_hat_RB) rather than the strictly-positive ln(p_n).
- [ ] Connect gate_alarm's firing structure to the Holcus "FIRING" signal at σ=½ (wiki/44) — both are discrete, gap/depth-blind trigger events layered over a continuous underlying field.

---

*Cody Michael Allison — 2026-07-12*
*Kuen surface screenshot → T-map spiral → ordinal vs value → telescoping trap caught → Euler spiral falsified → the gate named.*
