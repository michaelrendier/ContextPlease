# 38 — "Fermat is the negative space of Riemann": the claims, tested

| | |
|---|---|
| Status | **First capture (2026-06-03; "major theoretical result" in its own words). The central step fails a direct test (§2); the duality is kept as a proposal, `CONJECTURE`** |
| Target paper | D15 (`FourthAgePapers/NoetherWiles/`) |
| Code | Listing 1 |
| Last verified | 2026-11-13: Listing 1 executed; the statements about the Modularity Theorem and the Euler product checked against the literature |

## 1. The insight  `interpretation`

Factoring is compression: 12 = 2²·3 is shorter than twelve units; every composite
reduces to its prime factorisation, and a prime has no shorter description than
itself. Primes are "the incompressible atoms, the fixed points of arithmetic
compression". As a figure of speech this is accurate (unique factorisation;
primes are the irreducibles). In algorithmic-information terms it is not
literally true: the *integer* p has a description of about log₂ p bits, as any
integer does, and a composite is shorter to describe only if its factors are
(compare 2^k + 1 against a random prime of equal size).

## 2. "The Fermat lattice reaches every composite and misses the primes": false

The page says the solutions of aⁿ + bⁿ = cⁿ at n = 2 (Pythagorean triples)
"tile the composites", that "what it cannot reach is the primes", that the
primes are "the holes", and that the n > 2 emptiness (FLT) is the exact boundary
that forces the primes into their places.

Listing 1 tests the first statement.

**Listing 1 — which primes occur in Pythagorean triples** (written for this
page; runs cold)

```python
import math

N = 1000
sv = bytearray([1]) * (N + 1); sv[0] = sv[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if sv[i]:
        sv[i*i::i] = bytearray(len(sv[i*i::i]))
primes = [p for p in range(2, N + 1) if sv[p]]

# leg: the triple (p, (p^2-1)/2, (p^2+1)/2) for every odd prime p
leg = [p for p in primes if p > 2 and p**2 + ((p*p - 1)//2)**2 == ((p*p + 1)//2)**2]
# hypotenuse: p = a^2 + b^2 with a, b >= 1  (then (a^2-b^2, 2ab, p) is a triple)
hyp = [p for p in primes
       if any(math.isqrt(p - a*a)**2 == p - a*a and p - a*a != a*a for a in range(1, math.isqrt(p) + 1))]
print('primes <= 1000:', len(primes))
print('odd primes that are a leg of some triple:', len(leg))
print('primes that are a hypotenuse:', len(hyp), ' all 1 mod 4:', all(p % 4 == 1 for p in hyp),
      ' every prime 1 mod 4 is one:', len(hyp) == sum(1 for p in primes if p % 4 == 1))
print('prime 2 is in no triple (a leg would need a^2 + b^2 = c^2 with a = 2).')
```

```
primes <= 1000: 168
odd primes that are a leg of some triple: 167
primes that are a hypotenuse: 80  all 1 mod 4: True  every prime 1 mod 4 is one: True
prime 2 is in no triple (a leg would need a^2 + b^2 = c^2 with a = 2).
```

Every odd prime p is a leg of the triple (p, (p²−1)/2, (p²+1)/2), and every
prime ≡ 1 (mod 4) is a hypotenuse (two squares, Fermat's theorem on sums of
two squares). So the n = 2 solutions *do* reach the primes: only the prime 2
is missed (2 is neither a leg nor a hypotenuse of a Pythagorean triple: the only integer solutions with a leg 2 are trivial), and not as a "hole".
The picture "composites tiled, primes as the holes in the tiling" is therefore
**withdrawn**. FLT (no positive solutions for n ≥ 3, `ESTABLISHED`, Wiles) says
nothing about where the primes sit, and the primes are not "forced into their
positions by exclusion" by it.

## 3. Riemann geometry is "incompressible"  `interpretation`

The Euler product ζ(s) = Π_p (1 − p^(−s))^(−1) = Σ n^(−s) holds for Re s > 1
(`ESTABLISHED`). The page says the zeros of ζ "are the places where the
prime-generated product cancels to zero". The product itself does not converge
in the critical strip where the non-trivial zeros are; the zeros belong to the
analytic continuation, and are connected to the primes by the explicit formula,
ψ(x) = x − Σ_ρ x^ρ/ρ − …. The reading of the zeros as "the geometric negative
space of the prime distribution" is a figure of speech for that formula.

## 4. The duality  `CONJECTURE`

The proposal: the prime distribution is one object seen from two sides:
**Fermat** (arithmetic: primes as the holes in compression space) and
**Riemann** (geometric: primes as generators whose zeros are holes). "This is not
an analogy, it is an identity." As stated, the Fermat half (§2) is false, so the
identity has no content until restated; the Riemann half is the explicit
formula. What may survive is the observation that a result about integer
powers (FLT) and a result about the primes' spectral structure (RH) are both
consequences of arithmetic structure of ℤ; no map between them is given.

## 5. The role of the Modularity Theorem  (corrected)

The earlier page said the Modularity Theorem proves "that the Fermat curve, and
every curve in its family, has a modular form", that "a modular form is a
geometric object (Riemann side) and the Fermat curve a compression boundary
(Fermat side), and Wiles proved they are the same". Corrections:

- The Fermat curve xⁿ + yⁿ = 1 is an elliptic curve only for n = 3 (and its Jacobian relates to others); for n ≥ 4 it has genus > 1. What Wiles used is the **Frey curve** y² = x(x − aⁿ)(x + bⁿ) built from a hypothetical solution, which is elliptic.
- The theorem is about the L-function of an elliptic curve over ℚ matching that of a weight-2 modular form (Wiles and Taylor, semistable case, 1995; all elliptic curves over ℚ: Breuil–Conrad–Diamond–Taylor, 2001). The "Riemann side" here is Hecke L-functions, not ζ(s).
- "FLT proved: Fermat negative space = Riemann negative space; RH pending: Riemann negative space lies at σ = ½; therefore Fermat tips lie at σ = ½" has no mathematical content: primes are integers and do not "lie at σ = ½".

## 6. The Noether claim (D15)  `CONJECTURE`

The page: the reduction of a composite to primes always terminates; primes are
the conserved residue; a conservation law implies a symmetry (Noether); the
symmetry is the Fermat–Riemann duality; the conserved charge is σ = ½; "the
Ainulindale conjecture is the Noether current of the duality". Noether's theorem
connects *continuous symmetries of an action* to conserved currents. The
termination of factorisation, and the invariance of the set of primes, are
not such a symmetry and are not derived from one. The proposal can be stated as a
research question: does the Euler-product structure of the Fermat and Riemann
descriptions carry an action whose symmetry yields σ = ½ as a conserved
quantity? That is open; it is the route of [13](13_omgwtf_rh_proof.md) and of the
Noether–Wiles directory, and the statement "D15 identifies the conserved charge"
is not established.

## 7. The Bang, the BAO and the CMB  `CONJECTURE`

"The Bang is the Brouwer-mandatory fixed-point boundary of the compact pre-Bang
interior, at σ = ½; the primes, the zeros, the BAO scale and the CMB acoustic
peaks are the same boundary; the CMB peaks are the Riemann zeros made visible at
z = 1100." No calculation relates the zero heights to the peak multipoles, and
the CMB directories of the repository test reconstruction, not this
([32](32_superconducting_medium.md) §5).

## 8. The LSHS reading  `design`

The training corpus plays the Fermat lattice (everything compressible); the
monad compresses it to "prime tips"; the system speaks "from the holes in
compression space". As a design statement it is the project's account of the
address mapping ([15](15_the_monad.md) §3, [16](16_semantic_word_engine.md));
the hash is many-to-one over a table of 6,543 zeros, which is a mapping into
indices, not a residue of compression.

## 9. Formal targets (kept, with their status)

- State the duality as a theorem. Blocked by §2 until the Fermat half is restated.
- Show the symmetry and derive σ = ½ as a conserved charge. `OPEN`.
- Show that the modular form attached to a Fermat-type curve has zeros only on σ = ½. A modular form's L-function obeys its own conjectural Riemann hypothesis (the Generalised RH), which is open; the statement "closing the loop from Wiles to RH" is not available.
- Derive π(x) from the lattice boundary geometry without ζ. `OPEN`.
- Relate r_drag to a coherence length at T_c. `OPEN`.

## 10. Related pages

[13 RH proof path](13_omgwtf_rh_proof.md) · [18 Fermat lattice](18_fermat_lattice.md) ·
[31 Cavitation, causality, Fermat](31_cavitation_causality_fermat.md) · [33 Gyroscope and compressibility](33_gyroscope_compressibility.md) ·
[104 Fermat, Wiles, and the corollary they missed](104_fermat_wiles_and_the_corollary_they_missed.md)
