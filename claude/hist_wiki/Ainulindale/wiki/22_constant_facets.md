# 22 — The Constant Facets: π · φ · i · e

| | |
|---|---|
| Scope | four constants read as σ-facets of the RedBlue operator; π from the flat boundary; what the identities do and do not show |
| Code | `ValaQuenta/modules/berry_keating`, `modules/h_rb_hat`; Listing 1 below is self-contained |
| Confidence | the identities are ESTABLISHED mathematics; the claim that the constants are *outputs* of the operator is `THEORETICAL` and is not demonstrated (§6) |
| Last verified | 2026-11-13: every identity in §§1–5 recomputed by Listing 1 |

Earlier versions headed this page "Status: DERIVED" and said that Euler's
identity is a theorem of the RedBlue engine and that no definition of any
constant was used. Both statements are withdrawn (§6). The identities
themselves are correct and are kept, each with the verdict of the check.

## 1. Facet table

The weight of prime p at coupling σ is p^(−σ) ([14](14_redblue_hamiltonian.md)).
Setting σ to a constant gives:

| σ | Identity | Check | Reading by the framework |
|---|---|---|---|
| φ = 1.6180… | φ² = φ + 1, so φ(φ − 1) = 1 and p^(−φ) = p^(−1)·p^(−1/φ) for every p | holds exactly, termwise | the Fibonacci recursion; the recursion eigenvalue of the Cayley–Dickson iteration; "golden facet" |
| i | \|p^(−i)\| = 1 for every prime | holds | every prime contributes with unit magnitude: the "democratic facet", pure phase |
| e = 2.718… | p^(−e) = e^(−e·ln p) | an identity for *every* σ, not specific to e | "thermal facet": a Boltzmann weight |
| π = 3.14159… | (2/π)·π = 2; π(π − 1) = 6ζ(2) − π | holds, and is a rewriting: 6ζ(2) = π² | "circular facet": the U(1) normalisation closes |

Notes on each, so the readings are not mistaken for derivations:

- **φ.** The termwise factorisation is exact. The operator-level statement
  H^RB(φ) = H^RB(1)·H^RB(1/φ), as earlier text had it, is **false** as written:
  a sum of products is not a product of sums. For the first six primes,
  Σ p^(−φ) = 0.648 while (Σ p^(−1))·(Σ p^(−1/φ)) = 3.04. What is true is that
  each weight splits, which is the Fibonacci recursion at the level of exponents.
  Also withdrawn: "s(s−1) = 1 is the unique σ where ξ(s) = ξ(1−s)". The
  functional equation holds for every s; s(s−1) = 1 only picks out
  s = φ and s = 1 − φ, where the symmetric prefactor of ξ equals 1.
- **i.** i is the element with i² = −1 that the first Cayley–Dickson doubling
  introduces ([19](19_cayley_dickson_tower.md)). Unit modulus of p^(−it) is why
  the explicit formula ψ(x) = x − Σ_ρ x^ρ/ρ − … is a sum of pure phases; the zeros
  appear in it as the frequencies.
- **e.** e enters through the Berry–Keating flow ẋ = x, x(t) = x₀eᵗ
  ([20](20_three_phase_architecture.md) §2): the equation already contains the
  exponential; it is not produced from nothing. Any σ gives a "Boltzmann"
  form p^(−σ) = e^(−σ ln p), so nothing is special at σ = e. At s = e the
  von Mangoldt identity −ζ′(s)/ζ(s) = Σ Λ(n) n^(−s) holds as it does for every s > 1.
- **π.** π enters the operator as the prefactor 2/π of L_NN ([04](04_lagrangian_engine.md)),
  as an input. The "closure" (2/π)·π = 2 is arithmetic. π(π − 1) = 6ζ(2) − π is
  π² − π = π(π − 1) after Basel's 6ζ(2) = π².

## 2. π from a flat boundary  (result 2026-06-08)

The remainder of this page's constructive content: π reached from two
perpendicular axes, with no angle assumed.

1. Draw the X and Y axes (perpendicularity is a relation, not a measurement).
2. Mark equal unit distances: the unit square (0,0), (1,0), (1,1), (0,1).
3. The circumscribed square has side 2, tangent to the circle at the axes.
4. The inscribed square has corners on the circle, side √2, rotated 45° to the axes. The 45° is an output of the construction.
5. The circle is x² + y² = 1 (Pythagorean distance).

The eight points (four inner corners, four outer tangents) are the 8th roots of
unity. Archimedes started from a hexagon, so 60° was assumed; this construction
starts from a square. Doubling the point count gives a recursive tower whose
terms lie in ℚ(√2) (nested square roots):

| Points | Half-perimeter n·sin(π/n) | Closed form |
|---|---|---|
| 4 | 2√2 = 2.828 (lower bound; 4 is the upper) | square alone |
| 8 | 3.0615 | 4√(2 − √2) |
| 16 | 3.1214 | 8√(2 − √(2 + √2)) |
| 2^(k+2) | → π | limit of nested radicals (a Viète-type product) |

Every term is algebraic; π is transcendental (Lindemann, 1882), so the tower
never terminates, and the gap at any finite step is the geometric face of that
transcendence. The limit operation, not a Euclidean construction, reaches π.
`ESTABLISHED` (this is the classical polygon method, entered from squares).

**Flat boundary and σ = ½.** Cartesian coordinates hold exactly only where
curvature is identically zero. The framework reads σ = ½ as that locus in the
Riemann picture (the axis of the symmetry s ↦ 1 − s). This is the exact change
of variable of [21](21_chladni_zipf_riemann.md) §1, and as there it locates a
geometry and not the zeros.

**Fermat.** x² + y² = z² has integer solutions; xⁿ + yⁿ = zⁿ has none for
n > 2. The framework reads n = 2 as the flat boundary where the circle, and so π,
exists. Wiles's proof passing through modular forms ([18](18_fermat_lattice.md))
is read as "visiting σ = ½". That sentence is an interpretation; the proof
does not mention σ.

## 3. π from the primes

```
Σ 1/n² = π²/6 = Π_p 1/(1 − p⁻²)          (Euler 1734; Basel)
```

No factor of the Euler product contains π, and no single prime does; the
infinite product over all primes equals π²/6. π is the aggregate of the whole
prime distribution, not a local property. `ESTABLISHED`; Listing 1 checks it to
the truncation error (primes below 10⁵ give 1.6449327472 against π²/6 =
1.6449340668).

## 4. The three ground states

| Radius | Result | Note |
|---|---|---|
| r = 1 | area = π; circumference = 2 × area (true only at r = 1) | the canonical ground state; x² = π is "squaring the circle" in its plainest form |
| r = π/2 | circumference = π² = area of the circumscribed square | the unique radius where the linear measure equals the quadratic one |
| r = π | area = π³ | |

All three are exact. The framework calls them "fixed points of the flat
boundary's own geometry".

## 5. Verification

**Listing 1 — the identities of this page** (written for this page; runs cold)

```python
import math
phi = (1 + 5 ** 0.5) / 2
primes = [2, 3, 5, 7, 11, 13]
S = lambda s: sum(p ** -s for p in primes)

print('phi(phi-1)         =', phi * (phi - 1))
print('weights factor     =', all(abs(p**-phi - p**-1 * p**-(1/phi)) < 1e-15 for p in primes))
print('sum p^-phi         =', round(S(phi), 3), '  but S(1)*S(1/phi) =', round(S(1) * S(1/phi), 3))
print('|p^-i|             =', [round(abs(p ** -1j), 12) for p in primes])
print('pi(pi-1), pi^2-pi =', math.pi * (math.pi - 1), math.pi ** 2 - math.pi)
N = 100000
sv = bytearray([1]) * (N + 1); sv[0] = sv[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if sv[i]:
        sv[i*i::i] = bytearray(len(sv[i*i::i]))
ep = 1.0
for p in range(2, N + 1):
    if sv[p]:
        ep *= 1 / (1 - p ** -2)
print('Euler product      =', ep, ' pi^2/6 =', math.pi ** 2 / 6)
for n in (8, 16, 32):
    print(n, 'points', n * math.sin(math.pi / n))
```

```
phi(phi-1)         = 1.0000000000000002
weights factor     = True
sum p^-phi         = 0.648   but S(1)*S(1/phi) = 3.039
|p^-i|             = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
pi(pi-1), pi^2-pi = 6.728011747499565 6.728011747499565
Euler product      = 1.6449327472027284  pi^2/6 = 1.6449340668482264
8 points 3.0614674589207183
16 points 3.121445152258052
32 points 3.1365484905459393
```

## 6. What is not shown

The page's thesis, "the constants are outputs, not inputs, and Euler's
identity is a theorem of the engine", needs the constants to be produced
without being supplied. In the engine they are supplied: π in the 2/π prefactor
and in the gauge period, i in the complex plane the explicit formula lives in,
e in the exponential flow, φ in the tower's recursion. The derivations above
rewrite those inputs; they do not remove them. Euler's identity e^(iπ) + 1 = 0
is a theorem of complex analysis (`ESTABLISHED`), and its appearance in the
framework's vocabulary is a consistency, not a derivation from the primes.
"The universe counts; counting forces the constants" is the framework's motto
for the programme, and it stays a programme (`THEORETICAL`).

## 7. Related pages

[04 Lagrangian](04_lagrangian_engine.md) · [14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) ·
[17 A_fermat · Ω_ζΣ · d*](17_alpha_omega_d_star.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md) ·
[126 The circle catalogue](126_the_circle_catalogue.md)
