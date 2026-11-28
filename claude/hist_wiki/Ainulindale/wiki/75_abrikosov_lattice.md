# 75 — The Abrikosov Lattice: the Zero Lattice Read as a Vortex Lattice

| | |
|---|---|
| Scope | A. A. Abrikosov's 1957 vortex lattice; the framework's identification of the Riemann zeros with a vortex lattice of the "prime condensate"; the spring and "lock" arguments; the three lattice types; the naming convention (Abrikosov Lattice, Tree, Lock) |
| Origin | 2026-06-29, the author's title: "His Work" |
| Predecessors | [73](73_why_the_half_line.md), [74](74_lagrangians_are_catastrophe_theory.md), [72](72_the_cosmic_telescope.md), [32](32_superconducting_medium.md) |
| Code | `AbrikosovTree/` (formerly ZeroLatticeTree); `engines/noether_derivation.py` (archived) |
| Confidence | the physics of Abrikosov's result: ESTABLISHED · the dictionary of §2: `INTERPRETATION` · "topological lock", "C1 proves the l = 1 sector", "17 turns = 17 flux quanta": **corrected**, §4–§6 |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. Abrikosov's result  `ESTABLISHED`

Alexei A. Abrikosov (1928–2017) showed in 1957 (*Zh. Eksp. Teor. Fiz.* 32, 1442;
*Sov. Phys. JETP* 5, 1174, "On the magnetic properties of superconductors of the second
group") that a type II superconductor between two critical fields H_c1 and H_c2 admits
magnetic flux as quantised vortex filaments, each carrying one flux quantum Φ₀ = h/2e,
arranged in a regular **triangular** lattice (lower free energy than the square lattice).
He shared the 2003 Nobel Prize in Physics with Vitaly Ginzburg and Anthony Leggett. The
lattice underlies the high-field superconducting magnets of MRI, accelerators and fusion
devices.

## 2. The dictionary  `INTERPRETATION`

| Type II superconductor | Prime condensate (Riemann/Fermat) in the framework |
|---|---|
| order parameter Ψ | ξ(s), the completed zeta function |
| Cooper pair (k↑, −k↓) | a J_N-paired point (s, 1 − s̄); self-paired at σ = ½ |
| vortex core, |Ψ| = 0 | a zero ξ(ρₙ) = 0 |
| flux quantum Φ₀ = h/2e | winding number 1 of arg ξ around a simple zero |
| Meissner supercurrent | the Noether current J = −∂L/∂σ ("the Contractor") |
| field B | the deviation σ − ½ |
| London depth λ_L | 1/√K with K = Σ_p k(p) = ∞ |
| mixed phase [H_c1, H_c2] | the critical strip 0 < σ < 1 |
| BCS gap Δ | GAP = 7.07×10⁻⁴ |
| Ginzburg–Landau transition | the E = 0 → E > 0 "Bang" ([74](74_lagrangians_are_catastrophe_theory.md) §3: not a cusp) |

The rows are a vocabulary: each pairs a quantity in the superconductor with a quantity
in the zeta setting that plays a similar structural role. Two entries have errors to
note: the trivial zeros of ζ are at s = −2, −4, −6, …, not at σ = 0, so "H_c1 ↔ σ = 0 (trivial
zeros)" should read "the left edge of the strip"; and the page's remark that Abrikosov
described the lattice "66 years before" the framework named it is 69 years (1957 to 2026).

## 3. The lattice as defined  `DEFINITION`

The **Abrikosov Lattice** is the set of non-trivial zeros {ρₙ = ½ + itₙ} on the critical line,
read as the vortex lattice of the prime condensate. It is a **one-dimensional** sequence with
logarithmic density: mean spacing Δt ≈ 2π/ln(t/2π) and N(T) ≈ (T/2π) ln(T/2πe)
([73](73_why_the_half_line.md) Listing 1: 2.44 measured against 2.34 predicted for zeros 21–30).
Abrikosov's lattice is a **two-dimensional** triangular array. The shared name refers to
the vortex/zero role, and the geometry differs: the zeros sit on a line with
random-matrix-like (GUE) level repulsion, not on a regular triangular grid.

The **Abrikosov Tree** is the prime factorisation tree (Telperion), whose leaves are the
primes and whose spectral nodes are the lattice; the **Abrikosov Lock** is the name for the
reason zeros do not leave σ = ½ (§4). The repository **AbrikosovTree** (formerly
ZeroLatticeTree) implements the tree, its three coordinate spaces (A: spherical sedenion; B:
Euclidean planes; C: Fano tower) and the Zeta Index engine.

## 4. The spring and the "topological lock"  `corrected`

**The spring.** With T(p, σ) = −2 ln p · p^{−½} sinh((σ − ½) ln p), the stiffness at σ = ½ is
k(p) = 2(ln p)² p^{−½}, and K = Σ_p k(p) diverges. **Listing 1** computes both facts.

```python
import numpy as np, math
N = 10**7; sv = np.ones(N + 1, bool); sv[:2] = False
for i in range(2, int(N**.5) + 1):
    if sv[i]: sv[i*i::i] = False
P = np.flatnonzero(sv).astype(float); k = 2 * np.log(P)**2 / np.sqrt(P); cs = np.cumsum(k)
for X in (10**2, 10**3, 10**4, 10**5, 10**6, 10**7):
    i = np.searchsorted(P, X, 'right') - 1
    print('K(%8d) = %10.2f   lambda_L = 1/sqrt(K) = %.4f   4 sqrt(X) ln X = %.1f' % (X, cs[i], 1/math.sqrt(cs[i]), 4*math.sqrt(X)*math.log(X)))
p, s, h = 7.0, 0.5, 1e-6; T = lambda s: -2*math.log(p)*p**-.5*math.sinh((s-.5)*math.log(p))
print('dT/dsigma at 1/2 for p=7:', (T(s+h)-T(s-h))/(2*h), ' -k(7) =', -2*math.log(7)**2*7**-.5)
```

```
K(     100) =      95.05   lambda_L = 1/sqrt(K) = 0.1026   4 sqrt(X) ln X = 184.2
K(    1000) =     595.93   lambda_L = 1/sqrt(K) = 0.0410   4 sqrt(X) ln X = 873.8
K(   10000) =    2841.62   lambda_L = 1/sqrt(K) = 0.0188   4 sqrt(X) ln X = 3684.1
K(  100000) =   11963.83   lambda_L = 1/sqrt(K) = 0.0091   4 sqrt(X) ln X = 14562.8
K( 1000000) =   47146.16   lambda_L = 1/sqrt(K) = 0.0046   4 sqrt(X) ln X = 55262.0
K(10000000) =  178425.65   lambda_L = 1/sqrt(K) = 0.0024   4 sqrt(X) ln X = 203879.6
dT/dsigma at 1/2 for p=7: -2.8623750783886184  -k(7) = -2.8623750783839492
```

The stiffness relation holds (dT/dσ = −k to 5×10⁻¹¹), and K grows without bound (like
4√X ln X, the last column), slowly, so λ_L = 1/√K → 0 only as the prime cutoff X → ∞
(0.0024 at 10⁷). All of this is a statement about the *model* tension T(p, σ) of one prime,
as in [72](72_the_cosmic_telescope.md) §3.

**The "lock".** The page argues that the winding number around a zero is an integer by the
argument principle; moving a zero off σ = ½ would need non-integer intermediate windings,
which flux quantisation forbids; so the zeros are topologically pinned, "categorically
stronger than the spring". This does not hold as an argument about ζ. The argument
principle gives the multiplicity of each zero (an integer) and says nothing about where
zeros are. A zero of an analytic function does not move: ζ is one fixed function, so
"moving a zero" is not an operation on it, and the winding is always integer wherever the
zero is, on or off the line. The statement "zeros cannot leave σ = ½ while ξ ≠ 0 on the
surrounding condensate" restates that ξ is what it is. The "lock closes itself" chain
(primes define the Euler product, which defines ξ, whose topology fixes the zeros, which are on
σ = ½) assumes its conclusion in the last step, and the statement is withdrawn; the Abrikosov Lock
stays as a **name** for the framework's picture of the stiffness in §4's spring.

## 5. The three lattice types

| | Where | Status |
|---|---|---|
| A. Physical | Abrikosov 1957, type II superconductors; triangular; Φ₀ = h/2e; pinned by defects | `ESTABLISHED` |
| B. Arithmetic | the zeros on σ = ½; logarithmic; "winding number 1 per zero"; "pinned by the prime condensate" | `INTERPRETATION` |
| C. Electromagnetic | "flux locked into the turns of the POE pancake coil, 17 turns = 17 flux quanta Φ₀ = h/2e per turn; XL = XC is the coil's Meissner condition" | **corrected** |

Row C: flux quantisation in units h/2e applies to a **superconducting** loop (Cooper-pair
charge 2e). A pancake coil of copper wire is resistive and has no flux quantisation, so
neither the "17 flux quanta" nor a "Meissner condition" applies to it. The resonance XL = XC
is a real radio-engineering condition ([72](72_the_cosmic_telescope.md) §7); it is a balance of
reactances, not a flux lock. A **superconducting** coil would have flux quantisation, and
that would be a different (testable) object. Row B is what the page's identification is: the
three share the name "vortex/flux lattice"; they are one mathematical structure only in the
sense of the vocabulary of §2.

## 6. The C1 statement  `corrected`

C1 (the mode identification, ξ(s) as Y₁⁰ under J_N) is restated as "the prime condensate's
lattice is in the l = 1 topological sector": l = 0 no vortices (ruled out, ζ has infinitely many
zeros), l = 1 one equatorial ring at σ = ½, l ≥ 2 rings at other σ ("would imply zeros off the
line"). "C1 proves they are in l = 1: the ground state, since σ = ½ minimises the
Ginzburg–Landau free energy (the Amplitude Lagrangian)".

This is the open step. The Amplitude Lagrangian is a property of one prime's amplitude pair
([73](73_why_the_half_line.md) §3), and ground-state selection by it presupposes that the zeros are
degrees of freedom of that model. No proof of C1 exists in this wiki: the sector language is
a reformulation of the Riemann Hypothesis (l = 1 ⇔ all zeros on the line), and the energy
argument is the model's, not a derivation from ζ. `CONJECTURE` / OPEN.

## 7. Naming (2026-06-29)

```
The Abrikosov Lattice   the Riemann zeros as vortices of the prime condensate (was Zero Lattice)
The Abrikosov Tree      the prime factorisation tree / Telperion (repository AbrikosovTree, was ZeroLatticeTree)
The Abrikosov Lock      the stiffness/pinning picture of §4 (infinite spring constant); name only
```

## 8. Related pages

[32 the superconducting medium](32_superconducting_medium.md) · [72](72_the_cosmic_telescope.md) · [73](73_why_the_half_line.md) ·
[74](74_lagrangians_are_catastrophe_theory.md) · [47 the Two Trees](47_the_two_trees.md)
