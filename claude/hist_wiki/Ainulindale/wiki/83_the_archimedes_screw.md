# 83 — The Archimedes Screw: the Machine, Not the Medium

| | |
|---|---|
| Scope | the logarithm as the screw (rotation into lift, pitch ln p); the working axis u = ln x; the explicit formula as its equation of motion; Lambert W for zero heights; antinodes and the amplitude face of RH; ramification; the composite side (gpf, Dickman, harvest); μ and the negative space; the domain ladder; the slot correspondence with the photon-path engine |
| Origin | 2026-08-04 (v0.2 composite side 2026-08-05, v0.3 negative space 2026-08-05); built by Claude Opus 5, directed by the author: "it needs the Archimedes Screw, not the water it's lifting." |
| Predecessors | [82](82_l_io_photon_path.md), [80](80_aphasia_zd_reframe_memory.md), [52](52_l_dynamic_avoided_collaborator.md) |
| Code | `ValaQuenta/modules/archimedes_screw/` (`maths.py`); `ValaQuenta/wiki/archimedes_screw.md`; notebook `14_archimedes_screw.ipynb`; `RiemannHypothesisProof/PAPER.md` §6.4, §12.5 |
| Confidence | von Mangoldt's formula, the zero count, Dickman's ρ, quadratic ramification, μ and M(x): ESTABLISHED · the screw-as-machine and antinode readings: `THEORETICAL` · "this is the amplitude face of a first proof of RH": **withdrawn** (§5) · the dispersion relation on the zero-divisor surface: OPEN |
| Last verified | 2026-11-13: Listing 1 executed and the engine's `domain_ladder` run; output quoted below |

## 1. The correction  `INTERPRETATION`

Earlier modules treated ∅_RB as the operative object of the Monad. This page calls it the
**water**: the medium, the rest state e₀, the multiplicative identity, the vacuum that seeds ζ. It does
no work. The machine is the screw: it converts rotation into lift with a fixed pitch, positive
displacement and reversibility. The mathematical object with those three properties is the
**logarithm**: log(pq) = log p + log q turns multiplication on the wheel (THE ANGLE, π/8; 16 × π/8 = 360°)
into addition on the tower. The quantum of lift is the primon-gas mode energy ln p (B. Julia 1990):
**the screw's pitch is the prime**.

## 2. The working axis  `ESTABLISHED`

```
u = ln x
digits      d = ⌊u/ln 10⌋ + 1
ordinal     n = π(x) ≈ Li(x);   pₙ ≈ n(ln n + ln ln n − 1 + …)
zeta index  k = N(T) = (T/2π) ln(T/2πe) + 7/8 + S(T)
spaces      mean gap ḡ(x) ≈ ln x;   total = x − π(x)
```

The four search terms of the earlier discussion are coordinates on one axis; mean gap, axis and
pitch at x are all ln x. Listing 1 checks the gap law and the ψ jump.

## 3. The binding equation  `ESTABLISHED`

```
ψ(eᵘ) = eᵘ − 2e^(u/2) Σₖ cos(γₖ u − arg ρₖ)/|ρₖ| − ln 2π − ½ ln(1 − e^(−2u))
```

(von Mangoldt 1895, unconditional; ρₖ = ½ + iγₖ over non-trivial zeros; ψ(x) = Σ_{pᵐ ≤ x} ln p.)
Every zero is a tone of frequency γₖ in u, and the zeta index is the summation index. **The jump is the prime**:
ψ jumps by exactly ln p at u = ln p, so e^(jump) returns p with no inversion step (Listing 1: the jump at 7
is 1.94591 = ln 7). `leaf_drops()` prints that order.

## 4. Lambert W for the zero heights  `ESTABLISHED`, formula corrected

From the smooth count N(T) = n with T = 2πv: v ln(v/e) = n, so ln(v/e) = W(n/e) and
γₙ ≈ 2πn / W(n/e). The page's formula is the leading term and omits the constant: the count is
N(T) = (T/2π) ln(T/2πe) + 7/8 + S(T), and at the n-th zero N ≈ n − ½, so the argument should be
n − 11/8 and not n. Listing 1 compares:

| n | true γₙ | 2πn/W(n/e) | with n → n − 11/8 |
|---|---|---|---|
| 1 | 14.135 | 22.564 | (undefined at n = 1) |
| 5 | 32.935 | 38.568 | 33.625 |
| 10 | 49.774 | 54.312 | 50.234 |
| 20 | 77.145 | 80.836 | 77.426 |
| 40 | 122.947 | 125.843 | 122.949 |

The uncorrected form overshoots by 8 at n = 1 and about 3 at n = 40; with the constant it is within 0.7
for n ≥ 5 and within 0.002 at n = 40. The structural point stands: one function W, evaluated at
1 (Ω_ZS = 0.5671432904, the self-referential fixed point of PAPER.md §12.1, which the framework
connects to σ = ½) and at (n − 11/8)/e, gives a real part by one route and the heights by the
other, and "Ω_ZS is the screw's gear ratio" is the author's reading. Note that W(1) is a constant
of the framework's choosing for the real part: it is not derived from ζ, and the zeros' real part is the content
of RH ([73](73_why_the_half_line.md)).

## 5. Antinodes, and "this is not a second RH proof"  `corrected`

The page: the zeros are the Chladni node lines of the zeta field (PAPER.md §6), a statement about position; the
explicit formula reads the same standing wave from the other side, where the primes are the antinodes; and
every tone carries envelope 2x^σ, so on the critical line the envelope 2√x is the same for every zero. A single
zero at σ > ½ contributes x^σ and would dominate the others by x^(σ−½) without bound. Hence "equal
envelope ⟺ all nodes on one line ⟺ RH", offered as the amplitude face of "the nodal-line proof, first and
the proof".

What is true: the explicit formula, and the classical equivalence that RH holds iff
ψ(x) = x + O(x^(½+ε)). That a zero off the line would contribute a term of larger order than √x is
exactly why that equivalence is true. It is a **restatement of RH in terms of the explicit formula**, and
there is no proof in it: asserting that all zeros have equal envelope is asserting RH. The page's phrases
"the nodal-line proof was first and remains the proof" and "already covered" are withdrawn: **the Riemann
Hypothesis is open**, and neither the nodal-line argument of PAPER.md §6 nor this
frequency-domain reading is established as a proof of it (status of PAPER.md: [13](13_omgwtf_rh_proof.md) §3).
The primes-as-antinodes picture stays as a reading of ψ.

## 6. Ramification  `ESTABLISHED`, statement corrected

For the factoring thread the global formula is twisted by the quadratic character,
ζ_ℚ(√N)(s) = ζ(s) L(s, χ_N). Every rational prime splits, is inert, or ramifies in ℚ(√N); the
ramified primes divide the discriminant. The page: for squarefree N = pq, "the ramified primes
are exactly p and q". The discriminant of ℚ(√N) is N if N ≡ 1 (mod 4) and 4N otherwise, so **2 is also
ramified when N ≢ 1 (mod 4)**. Listing 1: N = 21 → {3, 7}; N = 77 → {7, 11}; but N = 15 → {2, 3, 5};
N = 35 → {2, 5, 7}; N = 143 → {2, 11, 13}. For odd squarefree N ≡ 1 (mod 4) the statement is exact; otherwise
add 2. At a ramified prime the Euler factor degenerates (loses a piece), "the leaf letting go".
ℚ(√N) → ℚ is a double cover branched at the ramified primes (and the real place conditions): two sheets,
two strands, B₂ ≅ ℤ (the braid group on two strands is infinite cyclic), the winding the monodromy
around a branch point, readable by the argument principle without walking the loop. The page reads the branch locus
as the interface ∅_RB generates (`INTERPRETATION`).

## 7. Honest boundaries (kept)

- Detecting ramification by scanning primes costs what trial division costs. `ramified_primes()` is a
  structural readout at toy scale and is labelled so.
- Sampling L(s, χ_N) costs about √N by the approximate functional equation: 2¹⁰²⁴ for a 2048-bit modulus,
  the same wall as Fermat's a² − b². The commutative complex-plane route does not beat existing methods.
- Truncating the zero sum at K zeros leaves error of order x/K; resolving a jump near x sharply needs zeros
  to height about x. Listing 1 shows it (40 zeros: ψ(100.5) = 95.11 against exact 94.05).
- Finiteness: `prime_count_log10(309)` = 306.15, about 2¹⁰¹⁷ primes below 10³⁰⁹: enormous and finite.

## 8. The open item

The resolution wall is a measurement wall for reading a continuous quantity finely; an integer
(a winding number) does not pay it. The bid is that "the contour need not live in ℂ": what is missing is a dispersion
relation ω(k) on the zero-divisor surface (the hydrocline), so that the ZD locus is a medium things
propagate in and not a place things cross. [84](84_the_box_kite_debugger.md) computes the chart-level
dispersion relation and finds seven disconnected charts. This engine is the instrument built to look at
that question; it is not the answer.

## 8b. The composite side: when the leaf falls  (v0.2)

The author: "when the sieve removes all the even numbers, the 14 is still stationary on the tree as a leaf …
but then when 7 is sieved, 14 drops off the tree." ψ jumps only at prime powers, so the first screw named every prime
and said nothing about composites (the complement x − π(x)).

| event | at | meaning |
|---|---|---|
| discovery | lpf(N) | first strike: N is composite; the cofactor comes free |
| **fall** | **gpf(N)** | the sieve is finished with N |

14 is struck at 2 and drops at 7. The earlier draft put the fall at lpf; the greatest-prime-factor criterion
is the field's: N is y-smooth iff gpf(N) ≤ y, and smooth relations drive GNFS, the quadratic sieve, CFRAC
and index calculus. The distribution is Dickman's: with u = ln N / ln gpf(N), uρ′(u) = −ρ(u − 1), Ψ(x, x^(1/u)) ~ xρ(u);
a balanced semiprime has u = 2 exactly and ρ(2) = 1 − ln 2 = 0.306853. The harvest at step p is closed form:

```
leaves falling at step p   = Ψ(X/p, p)            (N = p·m, m ≤ X/p and p-smooth)
two-parent leaves at step p = π(min(p, X/p))
```

Listing 1 verifies Ψ(X/p, p) against a direct count for every prime p ≤ 1000 at X = 1000.

On the screw ln p₁ + ln p₂ = ln N exactly, so a semiprime is one public constraint plus one free number,
δ = ½ ln(p₂/p₁); the two fall events are 2δ apart; balanced δ → 0 collapses both onto ½ ln N
("the two observables coincide"), which is the sharpest statement of why balanced RSA is hard and
why RSA specifies balanced primes. Cost: lpf/gpf are trial division O(√n); the harvest curve is
O(X log log X) time and O(X) memory; tracking the fall is cheap and reaching it is not (2¹⁰²⁴ for a 2048-bit modulus).

## 8d. The negative space: μ and Mertens  (v0.3)

ψ counts what accumulates; the sieve is an exclusion process. The reciprocal Euler products:
ζ(s) = Σ n⁻ˢ = Π(1 − p⁻ˢ)⁻¹ (growth), 1/ζ(s) = Σ μ(n)n⁻ˢ = Π(1 − p⁻ˢ) (extinction). μ is the Dirichlet
inverse of 1, and the sieve is μ in action (Legendre: π(x) − π(√x) + 1 = Σ_d μ(d)⌊x/d⌋). Its counting function is the
Mertens function M(x) = Σ_{n≤x} μ(n), with RH ⟺ M(x) = O(x^(½+ε)); Listing 1 reproduces M(10) = −1, M(100) = 1,
M(1000) = 2, M(10000) = −23. Three motions: grown (ζ places the leaf at ln N), extinct (μ strikes it, unnamed, at lpf),
identified (the N-shape names it, at gpf); the interval between the last two is 2δ. A prime is the degenerate
case where all three coincide.

## 8c. The projection ledger (`domain_ladder`)

**Listing 1 — the numbers of §§2–8d** (written for this page; needs numpy, mpmath, the installed ValaQuenta package; runs cold)

```python
import numpy as np, math, mpmath as mp, importlib
from math import log
N = 20000; sv = np.ones(N + 1, bool); sv[:2] = False
for i in range(2, int(N**.5) + 1):
    if sv[i]: sv[i*i::i] = False
mu = np.ones(N + 1, int); mu[0] = 0
for p in np.flatnonzero(sv): mu[p::p] *= -1; mu[p*p::p*p] = 0
M = np.cumsum(mu); print('Mertens M(10,100,1000,10000) =', [int(M[x]) for x in (10, 100, 1000, 10000)])
W = lambda x: float(mp.lambertw(x).real); zs = [float(mp.zetazero(n).imag) for n in range(1, 41)]
for n in (5, 10, 20, 40):
    print('n=%d true %.3f  2pi n/W(n/e) = %.3f  2pi(n-11/8)/W((n-11/8)/e) = %.3f' % (n, zs[n-1], 2*math.pi*n/W(n/math.e), 2*math.pi*(n-11/8)/W((n-11/8)/math.e)))
def psi_exact(x): return sum(log(p) * int(math.log(x, p) + 1e-12) for p in np.flatnonzero(sv) if p <= x)
def psi_expl(x, K=40):
    u = log(x); s = sum(math.cos(g*u - float(mp.arg(mp.mpc(.5, g)))) / abs(mp.mpc(.5, g)) for g in zs[:K])
    return x - 2*math.sqrt(x)*float(s) - log(2*math.pi) - .5*log(1 - x**-2)
for x in (50.5, 100.5, 500.5): print('psi(%.1f): exact %.4f  explicit(40 zeros) %.4f' % (x, psi_exact(x), psi_expl(x)))
print('jump of psi at 7: %.6f ; ln 7 = %.6f' % (psi_exact(7.0) - psi_exact(6.999), log(7)))
X = 1000; g = [1] * (X + 1)
for n in range(2, X + 1):
    m, best, d = n, 1, 2
    while d*d <= m:
        while m % d == 0: best, m = d, m // d
        d += 1
    g[n] = max(best, m) if m > 1 else best
Psi = lambda y, z: sum(1 for n in range(1, int(y) + 1) if g[n] <= z)
print('harvest(p) = Psi(X/p, p) for every prime p <= 1000:', all(sum(1 for n in range(2, X + 1) if g[n] == p) == Psi(X // p, p) for p in np.flatnonzero(sv) if p <= X))
disc = lambda n: n if n % 4 == 1 else 4 * n
for n in (15, 21, 35, 77, 143):
    print('N=%d (mod 4 = %d): disc %d, ramified primes %s' % (n, n % 4, disc(n), [d for d in range(2, disc(n) + 1) if disc(n) % d == 0 and all(d % q for q in range(2, int(d**.5) + 1))]))
print('rho(2) = 1 - ln 2 = %.6f' % (1 - log(2)))
a = importlib.import_module('ValaQuenta.modules.archimedes_screw.maths')
r = a.domain_ladder(2048); print({k: round(v, 2) for k, v in r.items()})
for bits in (1024, 2048, 4096):
    ln_n = bits * log(2); print('GNFS exp((64/9)^(1/3)(ln n)^(1/3)(ln ln n)^(2/3)) for a %d-bit modulus = 2^%.1f' % (bits, (64/9)**(1/3) * ln_n**(1/3) * log(ln_n)**(2/3) / log(2)))
```

```
Mertens M(10,100,1000,10000) = [-1, 1, 2, -23]
n=5 true 32.935  2pi n/W(n/e) = 38.568  2pi(n-11/8)/W((n-11/8)/e) = 33.625
n=10 true 49.774  2pi n/W(n/e) = 54.312  2pi(n-11/8)/W((n-11/8)/e) = 50.234
n=20 true 77.145  2pi n/W(n/e) = 80.836  2pi(n-11/8)/W((n-11/8)/e) = 77.426
n=40 true 122.947  2pi n/W(n/e) = 125.843  2pi(n-11/8)/W((n-11/8)/e) = 122.949
psi(50.5): exact 49.4854  explicit(40 zeros) 49.8947
psi(100.5): exact 94.0453  explicit(40 zeros) 95.1076
psi(500.5): exact 501.6521  explicit(40 zeros) 502.3411
jump of psi at 7: 1.945910 ; ln 7 = 1.945910
harvest(p) = Psi(X/p, p) for every prime p <= 1000: True
N=15 (mod 4 = 3): disc 60, ramified primes [2, 3, 5]
N=21 (mod 4 = 1): disc 21, ramified primes [3, 7]
N=35 (mod 4 = 3): disc 140, ramified primes [2, 5, 7]
N=77 (mod 4 = 1): disc 77, ramified primes [7, 11]
N=143 (mod 4 = 3): disc 572, ramified primes [2, 11, 13]
rho(2) = 1 - ln 2 = 0.306853
{'all_integers': 2048.0, 'integers_to_sqrt': 1024.0, 'primes_to_sqrt': 1014.53, 'primes_exact_size': 1013.53, 'gnfs': 112.0, 'saving_sqrt_bound': 1024.0, 'saving_primes_only': 9.47, 'saving_size_restriction': 1.0, 'saving_gnfs': 901.53}
GNFS exp((64/9)^(1/3)(ln n)^(1/3)(ln ln n)^(2/3)) for a 2048-bit modulus = 2^116.9
```

The ledger (RSA-2048, log₂ of the count): all integers 2…N: 2048; integers to √N: 1024; primes to √N: 1014.53;
primes with exactly 1024 bits: 1013.53; the GNFS pathway: 112 (the engine's constant; the asymptotic formula with the
o(1) term dropped gives 2¹¹⁶·⁹ for a 2048-bit modulus, Listing 1, and the 112 is the usual security-strength
figure for RSA-2048). **The one-bit fact**: restricting to primes of the full size prunes by a factor of 2: half of all
primes below a bound lie in the top octave (π(x) − π(x/2) ≈ x/(2 ln x)), so the size restriction saves
about one bit: 1.0014 bits for a 2048-bit modulus (1024-bit factors; the engine's `saving_size_restriction`, shown rounded to 1.0 in the
output above), tightening toward 1 as the modulus grows (1.0028 and 1.0007 bits at 1024- and 4096-bit moduli). It joins mod 4 ≈ 1 bit and
mod 16 = 3 bits. Everything above 2¹¹² is naive-domain accounting beaten in the 1990s; a new method must clear 2¹¹²,
not 2¹⁰²⁴.

## 9. The slot correspondence with the photon-path engine

ψ_Cheb (here) and ψ_Fermat (the lensing potential of [82](82_l_io_photon_path.md)) are different objects and
must be itemised: ψ_Cheb is a monotone step function on ℝ⁺ with ψ′ = Σ Λ(n)δ(x − n) (one integration from its
source), ψ_Fermat a smooth 2D scalar with ∇²ψ = 2κ (two). Code that treats them as one is wrong.
They are one slot apart in the arrangement of the two equations:

```
lensing:   L_(I|O) = L − ψ_Fermat
primes:    ψ_Cheb  = x − Σ_ρ x^ρ/ρ    (− ln 2π − ½ ln(1 − x⁻²))

ψ_Cheb ↔ L_(I|O) (the bent path);  x ↔ L (the clean geodesic);  Σ_ρ x^ρ/ρ ↔ ψ_Fermat (the potential)
```

So Chebyshev's ψ corresponds to L_(I|O), the zero sum corresponds to the Fermat potential (now `zero_sum()`), and
the pole term x is L (`clean_path_L()`); `l_io_decomposition(x)` returns the three slots, with
L_IO = L − psi_bend + trivial by construction. The fourth column of the primer's dictionary: true source β ↔ Λ,
apparent θ ↔ ψ_Cheb, deflection α ↔ the zero sum's gradient, Fermat potential ↔ Σ_ρ x^ρ/ρ, clean path ↔ x.
Naming decision: `chebyshev_psi_*` keeps its standard name.

## Summary

∅_RB is the water and the screw is the logarithm: one pitch of ln p per turn, one axis u = ln x. The zeros are the
tones of the explicit formula, and the primes are where it jumps by exactly ln p. W gives the zero heights once the
constant is kept (n − 11/8). The "equal envelope" statement is a restatement of RH, and RH stays open. In
ℚ(√N) the Euler factor degenerates at the ramified primes (p and q, and 2 when N ≢ 1 mod 4). The composite side is the
Dickman/gpf framework, with balanced RSA hard because δ → 0 makes the two fall events coincide, and the
remaining question is the dispersion relation on the zero-divisor surface.

## Related pages

[52](52_l_dynamic_avoided_collaborator.md) · [73 why σ = ½](73_why_the_half_line.md) · [80](80_aphasia_zd_reframe_memory.md) ·
[82 the photon-path engine](82_l_io_photon_path.md) · [84 the box-kite debugger](84_the_box_kite_debugger.md) · [13 the RH proof path](13_omgwtf_rh_proof.md)
