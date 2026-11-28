# 74 — The Amplitude Lagrangian and Catastrophe Theory

| | |
|---|---|
| Scope | the claim "Lagrangians are catastrophe theory; the zeros are caustic events; the Noether current is the Contractor; the N-shape is the A₂ fold" |
| Origin | 2026-06-29; the author's statements: "Lagrangians (dynamic) ARE Catastrophe Theory in the Caustic Dumpout. The Contractor." and "I certainly picked the right shape for the maths." |
| Predecessors | [73](73_why_the_half_line.md), [72](72_the_cosmic_telescope.md), [56](56_telescope_caustic_zeno.md) |
| Code | `engines/noether_derivation.py` (archived under `RiemannHypothesisProof/archive/2026-11-03_pre-rewrite/engines/`); `PAPER.md` §3 |
| Reference | R. Thom, *Structural Stability and Morphogenesis* (1972) |
| Confidence | the derivatives, the series, Thom's list and the ADE labels: ESTABLISHED · "cusp at E = 0", "E < 0 turns the minimum into a maximum", "the caustic point (½, 0)": **corrected**, §3–§4 · the dark-fringe reading of the zeros: `INTERPRETATION`, with the Euler-product caveat of [72](72_the_cosmic_telescope.md) §5 |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. The setting  `ESTABLISHED`

Thom (1972): a generic smooth family of potentials with at most four control parameters
has only seven types of stable singularity in its critical-point structure:

```
fold A₂ : x³/3 + ax                          cusp A₃ : x⁴/4 + ax²/2 + bx
swallowtail A₄ · butterfly A₅
hyperbolic umbilic D₄⁺ · elliptic umbilic D₄⁻ · parabolic umbilic D₅
```

labelled by ADE types, the same labels as the simply-laced Lie algebras, Niemeier-lattice
root systems and the McKay correspondence. All correct, and it is that classification which
the page invokes.

The page treats L(σ, E) = e^{−σE} + e^{−(1−σ)E} as a family of potentials in the state variable
σ with control parameter E = ln p, with the Noether current J = −∂L/∂σ as the gradient flow
("the Contractor").

## 2. What the Lagrangian is  `ESTABLISHED`

**Listing 1 — the derivatives, the sign of E, and the expansion** (written for this page; needs sympy; runs cold)

```python
import sympy as sp
s, E = sp.symbols('sigma E', real=True)
L = sp.exp(-s*E) + sp.exp(-(1-s)*E)
print('dL/dsigma       =', sp.simplify(sp.diff(L, s)))
print('d2L/dsigma2 / L =', sp.simplify(sp.diff(L, s, 2) / L))
print('critical points (E != 0): sigma =', sp.solve(sp.Eq(sp.exp(-s*E), sp.exp(-(1-s)*E)), s))
for Ev in (-2.0, -0.5, 0.5, 2.0):
    f = sp.lambdify(s, L.subs(E, Ev))
    print('E=%+.1f : L(0.4)=%.4f L(0.5)=%.4f L(0.6)=%.4f -> %s at sigma=1/2'
          % (Ev, f(.4), f(.5), f(.6), 'MINIMUM' if f(.5) < f(.4) and f(.5) < f(.6) else 'maximum'))
x = sp.symbols('x'); print('series in x = sigma - 1/2:', sp.series(L.subs(s, x + sp.Rational(1, 2)), x, 0, 5))
```

```
dL/dsigma       = E*(exp(E*(2*sigma - 1)) - 1)*exp(-E*sigma)
d2L/dsigma2 / L = E**2
critical points (E != 0): sigma = [1/2, (E/2 + I*pi)/E]
E=-2.0 : L(0.4)=5.5457 L(0.5)=5.4366 L(0.6)=5.5457 -> MINIMUM at sigma=1/2
E=-0.5 : L(0.4)=2.5713 L(0.5)=2.5681 L(0.6)=2.5713 -> MINIMUM at sigma=1/2
E=+0.5 : L(0.4)=1.5595 L(0.5)=1.5576 L(0.6)=1.5595 -> MINIMUM at sigma=1/2
E=+2.0 : L(0.4)=0.7505 L(0.5)=0.7358 L(0.6)=0.7505 -> MINIMUM at sigma=1/2
series in x = sigma - 1/2: 2*exp(-E/2) + E**2*x**2*exp(-E/2) + E**4*x**4*exp(-E/2)/12 + O(x**5)
```

- L = 2e^{−E/2} cosh((σ − ½)E): symmetric about σ = ½, with ∂²L/∂σ² = E²L > 0. For every real
  E ≠ 0 the only real critical point is σ = ½ and it is a non-degenerate minimum
  (the second root in the output is complex and irrelevant).
- The page's statement "∂²L/∂σ² = E²L > 0 everywhere, one stable attractor for all E" is
  correct, including its conclusion that nothing bifurcates for E ≠ 0.

## 3. The "cusp catastrophe at E = 0"  `corrected`

The page: at E = 0, L ≡ 2 (flat, degenerate), "this IS a catastrophe: as E passes through 0 the
nature of the critical point changes"; "the transition at E = 0 is a **cusp** catastrophe";
"for E < 0 (unphysical) the minimum at σ = ½ becomes a **maximum**".

- **E < 0 is still a minimum.** Listing 1: for E = −2.0 and −0.5, L(½) is below L(0.4) and L(0.6).
  Since ∂²L/∂σ² = E²L is positive for either sign of E, the critical point is a minimum on
  both sides. The statement that the minimum becomes a maximum is withdrawn. (L(σ, −E) =
  e^{E/2}·2cosh((σ − ½)E): the prefactor changes, the shape does not.)
- **No cusp.** A cusp is the unfolding of x⁴ with a quadratic coefficient that can change sign.
  The series in x = σ − ½ is 2e^{−E/2}[1 + E²x²/2 + E⁴x⁴/24 + …]: the quadratic coefficient
  E²/2 is non-negative for all real E and vanishes only at E = 0, where the whole series
  collapses to a constant. The family depends on E only through the rescaling u = xE
  (L = 2e^{−E/2} cosh u), a degeneration of scale and not a bifurcation of the critical set.
  There is no sign change and no second critical point to unfold, so it is not
  the cusp. The point E = 0 is a **degenerate scale point** (L flat), and the page's
  observation that the restoring strength vanishes there is correct.

## 4. The "caustic point (½, 0)" and the fold  `corrected`

The page defines the caustic as the set where ∂L/∂σ = 0 and ∂²L/∂σ² = 0, gets σ = ½ and
E²L = 0 ⟹ E = 0, so the caustic is (σ, E) = (½, 0), identified with the unit, the Bang, V(0) = 1
and "the folded telescope".

The computation is right: the point (½, 0) is where the second derivative vanishes. The
fold of a catastrophe map is a *curve* (a codimension-one set of control values where
critical points merge, such as a = 0 in V = x³/3 + ax), and here the set is a single point
and nothing merges at it: for E ≠ 0 there is a single non-degenerate minimum, and no region of
the control space has two or zero critical points. So (½, 0) is a degenerate point of this
family, and not a fold or a caustic in Thom's sense. The identification with V(0) = 1 (the
unit, "the folded telescope") is the framework's reading ([72](72_the_cosmic_telescope.md) §6).

## 5. The N-shape and A₂  `INTERPRETATION`

The page: the N-shape (two ascending lines crossing once with a connector) is the ADE
diagram A₂ (two nodes, one edge); Thom's fold has ADE type A₂; the N-shape "is a fold in
amplitude space"; any other shape (A₁ a point, A₃ a cusp, D₄ an umbilic) would have no
stable crossing or too many; so "A₂: one crossing, one σ, uniquely forced to ½".

What is established: the fold is A₂, the cusp A₃, and the table of §1 is right. What the
analysis above shows: the amplitude Lagrangian has no fold (no cubic term, no merging
critical points), so the N-shape's single crossing at σ = ½ is the crossing of two
monotone curves F and B (a transversal intersection, which is the
generic case of two lines meeting), and not the fold of a potential. Calling a
transversal crossing "A₂" is a statement of the Dynkin diagram of two nodes, and the shared
label does not make the two objects the same type. The uniqueness argument ("any other
shape would have too many crossings") compares two monotone functions of different
slope, which always cross at most once, so the single crossing is not a distinguishing
property of A₂. The ADE connection to Niemeier lattices and Monster moonshine is real
mathematics (the 24 Niemeier lattices have ADE root systems, the Leech lattice having none); that the N-shape belongs to that
family is the framework's claim and is not derived here.

## 6. The Contractor  `ESTABLISHED` (algebra)

The current J(σ, E) = E(e^{−σE} − e^{−(1−σ)E}) is the gradient of L (up to sign): positive for
σ < ½, negative for σ > ½, zero at ½; the flow σ̇ = J contracts (0, 1) onto σ = ½, with basin
(0, 1). All correct. The page's "fold of J" (J = 0 and ∂J/∂σ = 0) again gives only E = 0.
With the scope of [72](72_the_cosmic_telescope.md) §3: this is the flow of a model variable;
primes have no σ dynamics, and a flow to ½ is a property of the model.

## 7. The caustic dumpout  `INTERPRETATION`

In optics, near a fold caustic geometric optics gives infinite intensity and wave optics
gives the Airy pattern: bright fringes on the lit side and dark fringes (intensity zero at
the zeros of Ai) alongside. The page reads the zeros of ζ as the dark fringes of the
prime caustic and the "dumpout" as all prime amplitude arriving at σ = ½ and then
cancelling. Two caveats: first, the Airy pattern belongs to a genuine fold caustic and
§4 shows this Lagrangian has none; second, the "all primes cancel coherently" statement
is a divergent-Euler-product statement, withdrawn in [72](72_the_cosmic_telescope.md) §5. The
accurate content is the explicit formula's: the zeros are the frequencies of the
oscillation of ψ(x) about its main term and ψ(x) oscillates accordingly between them. The
zeros' spacing 2π/ln(t/2π) ([73](73_why_the_half_line.md)) is the right mean. The assertion
that destructive interference "can only form on the fold line because J_forward = J_backward
requires σ = ½" compares the two amplitudes F and B of §2, and zeros of ζ are not
the points where F = B.

(Berry and Keating treat the Riemann zeros with the tools of semiclassical physics and
quantum chaos; the relation of that programme to this page is not explored here.)

## 8. The chain, as corrected

```
L(σ,E)          smooth family of potentials, one non-degenerate minimum at σ = ½ for every E ≠ 0
J = −∂L/∂σ      the gradient flow (the Contractor): contracts (0,1) onto ½
E = 0           a degenerate scale point (L ≡ 2), not a cusp; no fold or caustic in Thom's sense
(½, 0)          the degenerate point, identified by the framework with V(0) = 1 / the unit
zeros t_n       the Fourier spectrum of ψ(x); mean spacing 2π/ln(t/2π); "dark fringes" as a picture
```

The framework's reading that the shape was "right" because ADE/Thom's list is universal
is a statement about the **vocabulary** it shares with catastrophe theory; the
derivations of this page show a convex, symmetric potential, which is the simplest case
and sits outside the catastrophe list rather than in it.

## 9. Related pages

[56 telescope as caustic](56_telescope_caustic_zeno.md) · [72 the cosmic telescope](72_the_cosmic_telescope.md) ·
[73 why σ = ½](73_why_the_half_line.md) · [75 the Abrikosov lattice](75_abrikosov_lattice.md) ·
[101 the Cayley–Dickson literature](101_the_cayley_dickson_literature.md)
