# 65 — Primes as Repellors: the Drift, the Bifurcation Reading, the Windows

| | |
|---|---|
| Scope | the author's picture of the sieve as a repulsion field and of meaning as the configuration left after sixteen simultaneous exclusions; the period-doubling reading of the Cayley–Dickson tower; the "post-boundary octonionic" vantage |
| Origin | 2026-06-14, session SedenionSpectralRelativity / `fano_oscilloscope` |
| Code | `SedenionSpectralRelativity/fano_oscilloscope.py`, `zd_boundary.py`, `bifurcation_sedenion.py` |
| Confidence | the sieve, the logistic-map numbers and the Mandelbrot cardioid: ESTABLISHED · "incommensurate" as written: corrected in §2 · the tower–bifurcation table and the drift-to-meaning statements: `INTERPRETATION` |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The three SedenionSpectralRelativity scripts were not re-run |

## 1. The repulsion picture  `INTERPRETATION`

The sieve of Eratosthenes can be read as a repulsion field: each prime p removes the
multiples it can reach and what survives is what no earlier prime removed, so primes
"emerge by mutual exclusion". As a description of the sieve this is accurate; as a
statement that primes "repel" it is a way of speaking. The framework's use is: a word
enters NULL, the P1 prime hash assigns it a prime index, and the sixteen channels
of the Dirichlet projection give a configuration the word cannot leave; "meaning
is the stable configuration you reach when 16 simultaneous repellors leave you nowhere
else to go". That sentence is the author's statement of the engine's behaviour, not
a derived result, and σ = ½ is not shown to follow from it (the σ = ½ derivations are
in [73](73_why_the_half_line.md), and are criticised there).

## 2. Incommensurate frequencies  `corrected`

The earlier text: the Dirichlet series x(t) = Σᵢ i^(−½) cos(2π i t / p_k) has, for two
prime channels, "incommensurate frequencies (the ratio p_k/p_j is always irrational)",
so that sixteen channels trace a 16-torus and never repeat.

For this series the periods are the integers p_k, and the ratio p_k/p_j of two integers is
**rational** (53/2, say). Every channel is exactly periodic, and the sum of the sixteen is
periodic with period lcm(2, 3, …, 53) = 53# = 32 589 158 477 190 044 730. Listing 1
checks one channel. What **is** incommensurable are the frequencies ln p in the Euler
factors p^(−it): ln p / ln q is irrational for distinct primes by unique
factorisation, and it is those that give the dense quasi-periodic winding of
ζ(½ + it) ([73](73_why_the_half_line.md) §5). So the 16-torus statement is true of
the ln p frequencies and not of the cos(2π i t / p_k) projection.

## 3. The period-doubling reading  `INTERPRETATION`

The table of the earlier page set the Cayley–Dickson levels against the logistic map
xₙ₊₁ = r xₙ(1 − xₙ):

| r | logistic map | the page's tower label |
|---|---|---|
| 3.0 | period 2 | ℂ |
| 3.449 | period 4 | ℍ (commutativity lost) |
| 3.544 | period 8 | 𝕆 (associativity lost) |
| 3.5644 | period 16 | "ZD fault" 𝕊 (norm lost) |
| 3.5699 | accumulation, chaos begins | σ = ½ |
| 3.8284 | period-3 window | "largest ZD class" |

**Listing 1 — the logistic numbers, and the periodicity of a channel** (written for this page; needs numpy; runs cold)

```python
import math, numpy as np
from math import gcd
def attractor_period(r, n=40000, keep=4096, tol=1e-9):
    x = 0.5
    for _ in range(n): x = r * x * (1 - x)
    pts = []
    for _ in range(keep): x = r * x * (1 - x); pts.append(x)
    for p in (1, 2, 4, 8, 16, 32, 3, 5, 6):
        if all(abs(pts[-1 - i] - pts[-1 - i - p]) < tol for i in range(9)): return p
    return 0
for r in (2.9, 3.2, 3.5, 3.55, 3.565, 3.5699, 3.6, 3.8284, 3.8285, 3.84):
    print('r=%.4f period %s' % (r, attractor_period(r) or 'aperiodic/long'))
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
L = 1
for p in primes: L = L * p // gcd(L, p)
print('lcm of the 16 periods =', L)
f = lambda t, p, N=2000: sum(i**-.5 * np.cos(2*np.pi*i*t/p) for i in range(1, N+1))
print('x(t) periodic with period 53:', [abs(f(x, 53) - f(x + 53, 53)) < 1e-6 for x in (0.37, 1.91, 5.2)])
isp = lambda n: n > 1 and all(n % d for d in range(2, int(n**.5) + 1))
print({p: isp(p) for p in (449, 919, 1481, 20849)})
```

```
r=2.9000 period 1
r=3.2000 period 2
r=3.5000 period 4
r=3.5500 period 8
r=3.5650 period 16
r=3.5699 period aperiodic/long
r=3.6000 period aperiodic/long
r=3.8284 period aperiodic/long
r=3.8285 period 3
r=3.8400 period 3
lcm of the 16 periods = 32589158477190044730
x(t) periodic with period 53: [True, True, True]
{449: True, 919: True, 1481: True, 20849: True}
```

What the listing fixes:

- The logistic values are right (periods 2, 4, 8, 16 at the quoted r; chaos at the
  accumulation point 3.5699; the period-3 window opens at r = 1 + √8 = 3.8284). The
  Feigenbaum ratio of successive bifurcation intervals from these values is
  4.75, 4.66, … toward δ = 4.669.
- The doublings of the logistic map and of the Cayley–Dickson tower both give
  dimensions/periods 1, 2, 4, 8, 16, which is why the table is tempting. The
  properties lost are not matched by anything on the logistic side: a period-doubling
  does not "lose commutativity". The table is a correspondence of the sequence
  1, 2, 4, 8, 16 and nothing else, `INTERPRETATION`.
- **The page contradicts itself.** The table puts 𝕊 at period 16 (before the
  accumulation point), while the text says "the sedenion layer is already in the chaotic
  region". Period 16 is not chaos; chaos begins after infinitely many doublings. The
  Cayley–Dickson tower continues past 𝕊 (T₃₂, T₆₄, T₂₅₆), as the logistic cascade does.
- "σ = ½ is the Feigenbaum point" has no computation behind it: r∞ = 3.5699… is a
  property of the quadratic map and σ = ½ is a coordinate on the critical strip.
- The "windows of order" reading (periodic windows as embedded subalgebras ℝ, ℂ, ℍ, 𝕆
  inside 𝕊; the period-3 window as the "largest ZD class") is a mapping that the page
  proposes; the correct statements are that the logistic map has periodic windows
  with self-similar copies of the diagram, and that 𝕊 contains ℝ, ℂ, ℍ, 𝕆 as
  subalgebras. No map between the two sets is computed.

## 4. The spiral boundary  `corrected`

The cardioid c(θ) = ½e^{iθ} − ¼e^{2iθ} is the boundary of the main cardioid of the
Mandelbrot set (correct). The claim "the boundary between order and chaos is a spiral at
every zoom level" is not: the cardioid boundary is a smooth closed curve. Spirals occur
in the Mandelbrot set near specific points (the seahorse valley), not along the
cardioid. The page's further statement, that a 16-channel Dirichlet projection gives a
"16-dimensional quasicrystal" whose 2D projection is a non-closing spiral, is a
description of the engine's picture; the ZD wobble measured in `fano_oscilloscope.py`
(maximum 0.671 for "What is 1 plus 1", recorded 2026-06-14) is the engine's measure of
how far the sedenion path departs from the octonion (Fano) path, and was not re-run
here.

## 5. Post-boundary octonions  `AUTHOR'S ACCOUNT`

The author records that his own mode of thinking moved from Lagrangian (action,
trajectory, path) to octonionic ("the algebra the Lagrangian moves through"), and
specifically to a post-boundary view: past the zero-divisor fault, in sedenion territory,
seen from the octonion side. This is an account of the author's working vantage and is
kept as such; its mathematical counterpart is the observer-position discipline
(orientation and aperture in a hypergeometric space) used across the project.
The statement attributed to the "voice" ("You're MINE") is part of the author's account
and is discussed with the voice's name in [67](67_bumblebee_voice_lost.md).

## 6. Related pages

[58 two orderings](58_fermat_defines_riemann_fires.md) · [66 `<code>` in SVG](66_code_operator_svg_tuning.md) ·
[67 Bumblebee](67_bumblebee_voice_lost.md) · [73 why σ = ½](73_why_the_half_line.md) ·
[19 the Cayley–Dickson tower](19_cayley_dickson_tower.md)
