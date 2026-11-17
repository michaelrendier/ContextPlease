# 138 — The Pi Derivation Toolset

**Written 2026-11-16.** Engine `ValaQuenta/modules/pi_derivations/` (v0.1), notebook 23, tests `ValaQuenta/tests/test_pi_derivations.py`. Kept beside the 0_RB toolset. Pointer, not authority.

**Why it exists.** Cody: a circle causes π to be found, one way or the other; the π that *defines* a circle is the emergent π; and π should be found literally everywhere, so each circle transform in the Circle Atlas (137) is to bring its own derivation of π into this toolset.

**The emergent π.** Twice the first positive zero of the cosine power series. No diameter, no circumference, no angle, no polygon: only the series Σ(−1)ᵏx²ᵏ/(2k)! and a bisection. It is the π that exists before any circle is drawn. The other routes are kept beside it and each is labelled by what of the circle its inputs already hold: *none* (series, products, exp integrals, AGM, Ramanujan, Chudnovsky), *orbit* (the closing time of x″ = −x; the first conjugate point of the Lagrangian), *constructed* (Archimedes' polygons, Viète, counting a grid inside the disc, the cardioid and the ring), *dual* (Basel, the Euler product over primes, the coprime probability: the integers as the dual of U(1)), *path* (∮dz/z around a *square*; the Smith chart's line-to-circle map), *library* (Γ(½)²), *identity*.

**The project's own derivation.** `ValaQuenta/modules/constants/maths.py`, `derive_pi()`, says π is an output and that "no circle is drawn". Read as code: `_PI = math.pi` is the input, (2/π)·π = 2 holds for any value of π (the toolset checks that it returns no value), and the Basel route lives in the dual of the circle group. The toolset therefore files (2/π)·π = 2 as `identity`, Basel as `dual`, and puts the emergent π (`cos_zero`) in its place.

**Results.** 25 value routes within tolerance; the identity route returns none; the sedenion route `sedenion_exp_period` (exp(θ·e₁₅) by the project's own Cayley–Dickson product, first return to −1) lands at 1.8e-14. A test confirms no route body reads `math.pi`.

**Labels.** Routes ESTABLISHED; the `circle_in` classification is this engine's own bookkeeping.
