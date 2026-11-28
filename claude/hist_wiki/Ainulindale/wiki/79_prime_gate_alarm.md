# 79 — The Boundary-Crossing Alarm: π(x) as One Instance

| | |
|---|---|
| Scope | a reusable crossing detector (`BoundaryAlarm`); π(x) as the alarm run over the integers; the gap channel as its separate companion; the telescoping trap; the falsified Euler-spiral reading |
| Origin | 2026-07-12, a live derivation that began from a screenshot of a Kuen surface |
| Predecessors | [74](74_lagrangians_are_catastrophe_theory.md), [65](65_primes_repellors_drift_meaning.md), [44](44_halting_problem_uns.md), [17](17_alpha_omega_d_star.md) |
| Code | `ValaQuenta/prime_gate.py` (`BoundaryAlarm`, `PrimeGateEngine`, `sigma_half_alarm`); `ValaQuenta/wiki/prime_gate.md`; notebook `prime_gate/01_gate_alarm_vs_gap.ipynb`; `VAPMIP/monad.py` (P1 hash) |
| Confidence | the counts and the regression: ESTABLISHED (re-run) · the falsification: ESTABLISHED and kept · the Holcus-FIRING parallel: `INTERPRETATION` |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 0. What the engine is for

The engine is the alarm: a reusable crossing detector, not a test of a dataset.
`BoundaryAlarm(boundary_fn)` fires once per crossing and is blind to everything else; π(x) is
`BoundaryAlarm(is_prime)` run over the integers; the Holcus "FIRING" signal ([44](44_halting_problem_uns.md): a computation reaching σ = ½,
"does it stop here, at this depth") is the same primitive run over a σ-trajectory
(`sigma_half_alarm`). The gap channel, the two spirals and the Euler-spiral aside came up while
building it. A wrong answer found on the way (the Euler-spiral falsification, §5) stays in the
record.

## 1. The split

Two channels that had been silently conflated:

- **π(x), the gate alarm**: a monotone staircase, +1 at each prime, flat elsewhere; every event is
  identical whatever gap preceded it, so it is gap-blind by construction.
- **g_n = p_{n+1} − p_n, the gap channel**: the interval between alarms, carrying all the
  irregularity π(x) cannot see (a gap of 14 and a gap of 2 are the same single step in π(x)).

## 2. The P1 hash connection

The gate is the ordinal-index addressing already in `monad.py`'s P1 prime hash:
word → prime p → π(p) → γ_index. The address was never the prime's value but the **count** of
primes crossed. Two spirals on the T-map T(x) = x·e^{i d* ln x} (d* = 0.24600, the code's value)
make the distinction concrete:

```
ordinal_spiral: T(n)   = n   · e^{i d* ln n}     address = COUNT (the gate)
value_spiral:   T(pₙ)  = pₙ  · e^{i d* ln pₙ}    address = MAGNITUDE
```

The radius grows as n and as n ln n respectively (Prime Number Theorem). Using the ordinal form
deliberately discards gap information, the same blindness π(x) has.

## 3. The gap and the PNT; the telescoping trap  `ESTABLISHED`

**Listing 1 — the counts, the gap regression and the trap** (written for this page; needs numpy; runs cold)

```python
import numpy as np
N = 50000
sv = np.ones(N + 1, bool); sv[:2] = False
for i in range(2, int(N**.5) + 1):
    if sv[i]: sv[i*i::i] = False
P = np.flatnonzero(sv)
print('pi(200) =', int((P <= 200).sum()), '; primes <= 50000:', len(P), '; gaps:', len(P) - 1)
g = np.diff(P).astype(float); lp = np.log(P[:-1].astype(float))
sl, ic = np.polyfit(lp, g, 1); print('gap_scaling_fit: slope=%.4f intercept=%.4f' % (sl, ic))
k = np.log(P.astype(float)); print('kappa = ln p_n range [%.3f, %.3f], sign changes %d' % (k.min(), k.max(), int((np.diff(np.sign(k)) != 0).sum())))
print('telescoping: cumsum(gap) == p_n - p_0:', bool(np.array_equal(np.cumsum(np.diff(P)), P[1:] - P[0])))
```

```
pi(200) = 46 ; primes <= 50000: 5133 ; gaps: 5132
gap_scaling_fit: slope=0.9615 intercept=0.4264
kappa = ln p_n range [0.693, 10.820], sign changes 0
telescoping: cumsum(gap) == p_n - p_0: True
```

All four numbers of the earlier record reproduce (46; slope 0.9615, intercept 0.4264 over
5,132 gaps; κ range [0.693, 10.820]; the telescoping identity). The regression of gₙ on ln pₙ
gives the PNT average-gap law (slope near 1) numerically.

**The telescoping trap.** A first "prime curvature spiral" summed gapₙ as a heading increment,
θₙ = scale·Σ gapₙ. Since gapₙ is a first difference of pₙ, the cumulative sum collapses to
pₙ − p₀ (confirmed in Listing 1), so the construction was only a rescaled value spiral, not an
independent curvature signal. The honest curvature signal is κₙ = ln pₙ: smooth, not a first
difference of anything in the sequence.

## 4. Why the alarm is useful as an alarm

Because π(x) is gap-blind, it is cheap and unambiguous as a trigger: fire once per prime without
computing spacing. The gap channel stays available as a separate query for reasoning about *when* the
next crossing is likely. Keeping the two channels apart is the engineering content of the result.

## 5. The Euler-spiral falsification  `ESTABLISHED`, kept

The corrected curve (heading from κₙ = ln pₙ) was tested against the true Euler spiral (clothoid,
Fresnel integral, κ(s) = s). Result: **falsified**.

```
is_true_euler_spiral():   (engine output as recorded; the κ range and sign count are reproduced by Listing 1)
  is_clothoid: False
  reason: ln(p_n) is monotonic and always positive; a clothoid requires curvature to cross zero
          and reverse sign to produce two asymptotic eyes (Fresnel integral).
  kappa range: [0.693, 10.820], sign changes: 0       (reproduced in Listing 1)
  actual topology: single-point inward spiral (involute-like)
```

A clothoid has κ linear in arc length, negative for s < 0, hence two symmetric asymptotic eyes.
Prime curvature ln pₙ never reverses sign for n ≥ 1 (Listing 1: 0 sign changes), so it can only tighten into one inward spiral about a single centre. Not a
clothoid, and the engine does not pretend otherwise. This is the same discipline as the warning in
[65](65_primes_repellors_drift_meaning.md) that the sedenion spiral is not the Fano cardioid.

## 6. Formal targets (open)

- [ ] closed form of `curvature_spiral`'s single-point convergence radius in terms of d* and N(T);
- [ ] whether a two-eye clothoid can be built from a *signed* prime-derived signal (the Möbius function μ(n), or a Red/Blue difference current as in Ĥ_RB) instead of the positive ln pₙ;
- [ ] connect the gate alarm's firing to the Holcus "FIRING" signal at σ = ½ ([44](44_halting_problem_uns.md)): both are discrete, depth-blind triggers over a continuous field.

## 7. Related pages

[44 the halting problem](44_halting_problem_uns.md) · [65 primes as repellors](65_primes_repellors_drift_meaning.md) ·
[74](74_lagrangians_are_catastrophe_theory.md) · [81 SHA-1 collision geometry](81_sha1_real_collision_geometry.md) · [83 the Archimedes screw](83_the_archimedes_screw.md)
