# 94 — Mathematical X-ray Crystallography

| | |
|---|---|
| Scope | the correspondence between X-ray crystallography and factoral decomposition (the number as crystal, the factors as structure); the Ewald sphere as the two-anchor geodesic; the Patterson function as the XOR differences; the phase problem as the hardness of factoring; the visualiser as a "number diffractometer" |
| Named | 2026-08-22, by the author: "this is mathematical X-ray crystallography." |
| Continues | [92](92_ring_theory_spine.md), [93](93_qm_gr_by_tree.md) |
| Code | `GenerationalLineage/engine/lineage.py` (the pathway block PW1–PW9 as the engine now stands; named SedenionFactoralRelativity when the page was written): `spiral_address`, `pathway_residues`, `tune_pathway`, `fermat_path`, `decompose_number`; canonical `@RCCM_RING_THEORY_SPINE` |
| Confidence | the Fermat-method and phase-problem statements about factoring, as tested in Listing 1: ESTABLISHED · the whole dictionary: `INTERPRETATION` (a framing); its hard core, the phase problem, is not solved here |
| Last verified | 2026-11-13: Listing 1 executed; the lineage engine run (44/44 relations hold, [92](92_ring_theory_spine.md)). PW1–PW5 individually were not re-run |

## 1. The correspondence

In X-ray crystallography you cannot see the atoms: you shine a beam through the crystal, record the diffraction pattern and reconstruct the structure. Factoral decomposition is the same instrument pointed at a number: you cannot see the factors of N, so you illuminate N from many tunings, record where it resonates, and reconstruct the factors.

| X-ray crystallography | factoral decomposition |
|---|---|
| the crystal | the number N |
| electron density ρ(r) | the multiplicative structure of N |
| structure factors F(h) = 𝓕[ρ] | the spectral / cepstral labelings (orders 1, 2) |
| diffraction intensities |F|² | the magnitudes (order 1, support): what you measure |
| the phases arg F(h) | the arrangement (order 2): what you lose |
| Bragg's law nλ = 2d sin θ (resonance) | tune-to-resonance (CFRAC square residue, Fermat node) |
| the Ewald sphere (incident + diffracted beam) | the two anchors: origin (1) and destination (N) |
| rotating the crystal | tuning the spiral (multiplier / σ / excursion) |
| a Bragg reflection (a spot) | a factor node (a square residue) |
| the Patterson function (phase-free autocorrelation) | the XOR-difference structure (F6): the differences, not the places |
| direct methods / triplet relations h₁ + h₂ + h₃ = 0 | order 3: the associator / the a ⊕ b = c lines (R5, F6) |
| isomorphous replacement | the multiplier tuning kN (PW2) |
| reconstructing ρ | recovering the factors |

The mapping is the page's framing; the left column is textbook crystallography (Bragg 1913; Ewald; Patterson 1934; the direct methods of Hauptman and Karle, 1985 Nobel Prize in Chemistry), and the right column is the engine's vocabulary.

## 2. The Ewald sphere is the two-anchor geodesic  `INTERPRETATION` over a measured statement

The author: "there are two anchors — the origin, and the reference point destination. Now you can tune the path between the two." In crystallography a reflection appears when a reciprocal-lattice point lies on the Ewald sphere, a two-point construction. For N the anchors are 1 = e₀ = ∅_RB and N. Pinning both ends turns factoring from an outward walk (an initial-value problem, underdetermined) into a
boundary-value problem: a factor is a node on the geodesic between them, **log-symmetric about the midpoint √N** (ln p + ln q = ln N, which holds for every N = pq and not only balanced ones). Fermat's method finds the factors at the **excursion** a − √N, with a = (p + q)/2 the first square-completing value, and Listing 1 measures how that excursion depends on the gap.

**Listing 1 — Fermat's method: steps against the prime gap** (written for this page; needs sympy; runs cold)

```python
import math
from sympy import nextprime
def fermat(N, limit=10**7):
    a = math.isqrt(N); a += (a * a < N); s = 0
    while s < limit:
        b2 = a * a - N; b = math.isqrt(b2)
        if b * b == b2: return s, a - b, a + b
        a += 1; s += 1
for bits, gap in ((32, 2), (32, 2 * 10**6), (32, 32000000), (40, 5 * 10**6), (48, 48000000), (64, 0)):
    p = nextprime(2**(bits - 1)); q = nextprime(p + max(gap, 1)); N = p * q; pred = (q - p)**2 / (8 * math.isqrt(N))
    r = fermat(N) if pred < 10**6 else None
    print('%d-bit p, q-p = %9d : predicted excursion (q-p)^2/(8 sqrt N) = %9.3g ; Fermat steps from ceil(sqrt N) = %s ; factors recovered: %s'
          % (bits, q - p, pred, r[0] if r else 'not run', bool(r and {r[1], r[2]} == {p, q}) if r else 'n/a'))
```

```
32-bit p, q-p =        34 : predicted excursion (q-p)^2/(8 sqrt N) =  6.73e-08 ; Fermat steps from ceil(sqrt N) = 0 ; factors recovered: True
32-bit p, q-p =   2000004 : predicted excursion (q-p)^2/(8 sqrt N) =       233 ; Fermat steps from ceil(sqrt N) = 232 ; factors recovered: True
32-bit p, q-p =  32000070 : predicted excursion (q-p)^2/(8 sqrt N) =  5.92e+04 ; Fermat steps from ceil(sqrt N) = 59164 ; factors recovered: True
40-bit p, q-p =   5000026 : predicted excursion (q-p)^2/(8 sqrt N) =      5.68 ; Fermat steps from ceil(sqrt N) = 5 ; factors recovered: True
48-bit p, q-p =  48000040 : predicted excursion (q-p)^2/(8 sqrt N) =      2.05 ; Fermat steps from ceil(sqrt N) = 2 ; factors recovered: True
64-bit p, q-p =        70 : predicted excursion (q-p)^2/(8 sqrt N) =  6.64e-17 ; Fermat steps from ceil(sqrt N) = 0 ; factors recovered: True
```

(The first and last rows are near-twin cases; the exact gaps are `nextprime` outcomes.) The number of Fermat steps is the integer part of (q − p)²/(8√N), measured: 232 against 233, 59164 against 59,200, 5 against 5.68, 2 against 2.05. So "Fermat's method finds the factors of every balanced semiprime at excursion 0" holds only for *near-twin* primes, (q − p)² < 8√N, i.e. |q − p| ≲ 2.8 N^{1/4}; for primes of the same bit-length that are
merely "balanced" (|q − p| ~ √N or larger) the excursion is enormous, which is the reason standard RSA key-generation rules require |p − q| to be large (FIPS 186-4 uses |p − q| > 2^{n/2−100}, quoted from memory). The page's closing statement is the right one: "RSA hides the factor by tuning its distance from the midpoint √N large, the same way a crystal can be oriented so a reflection misses the sphere": primes must be balanced enough to be secure
yet far enough apart that the excursion is exponential. Rotating the crystal is tuning the excursion, and a square residue is the Bragg reflection (PW5, the page's identification).

## 3. The Patterson function is F6  `INTERPRETATION`

The Patterson function is the autocorrelation of the density computed from the intensities alone, and its peaks are the interatomic vectors (differences), not the positions. This is the framework's F6, "the factoring map is on the EDGES (the XOR differences), not the places": the 15 non-zero XOR differences of PG(3, 2) are the Patterson peaks (the lineage engine's relation
counts 120 pairs = 15 differences × 8 pairs and 35 lines a ⊕ b = c, each difference in 7 of them: 105/15, in its run). Decomposing the relation rather than the objects is crystallography with the phase-free autocorrelation.

## 4. The phase problem is why factoring is hard: the honest core

Crystallography's central difficulty: the detector records intensities |F|² and discards the phases arg F, which are what reconstruction needs. In this framing N is the intensity (the order-1 datum you are handed) and the factor's arrangement is the phase (order 2, thrown away). Bifurcation (the author's earlier RSA attempts) only ever reads intensities, a classifier, and so measured at chance
(recorded outcome, not re-run): "you cannot classify your way to a phase."

Crystallographers do solve the phase problem routinely: direct methods (statistical triplet relations, the order-3 associator), isomorphous replacement (a heavy-atom perturbation, the multiplier tuning), anomalous dispersion (tuning the wavelength, the σ), molecular replacement (a known related structure, a known factor base). Each needs more experiments, more diffraction images or tunings. That is why real factoring
(CFRAC, the quadratic sieve, the number field sieve) is sub-exponential: **phase retrieval by collecting many relations**. Listing 1 and [83](83_the_archimedes_screw.md) fix the corresponding costs (Fermat: gap-dependent; sieving: beyond 2¹¹² for RSA-2048).

> Polynomial factoring, an RSA break, would be solving the phase problem from a single measurement. That is the open miracle and nothing here claims it. The framework offers the right instrument to look, and the honest question is whether its geometry supplies a phase relation the algebraic sieve does not already use.

## 5. The visualiser is a number diffractometer

It is not a fractal renderer or a bifurcation viewer: (1) mount N (the crystal), with the midpoint √N and the anchors 1 and N as the geometry; (2) rotate it, a tuning dial (multiplier / σ / excursion / pitch); (3) collect reflections (where the geodesic resonates: square residues, Fermat nodes) as a diffraction pattern; (4) reconstruct the structure, with
`decompose_number(N)` assembling the ring / cepstral / lineage / spiral / pathway perspectives into the factor "density map"; (5) the parallax pane is the Ewald geometry (two views whose relative shift is the two-anchor constraint). Multiple perspectives to find micro-structures and continuous relationships is what a diffractometer does: rotate, collect, reconstruct.

## 6. Where it also applies: language

The same instrument reads English with a far smaller crystal. A word's type/category is a domain segregation (the pathway layer): the current word constrains which category may follow, pruning the walk to the legal continuations; the category is the word's outside (Laurelin), the specific word its inside (Telperion): L_(I|O) per token. Diffraction on a small, strongly ordered crystal is easy, which is why the translator is navigable
while RSA is not (`INTERPRETATION`).

## 7. Related pages

[92 the ring-theory spine](92_ring_theory_spine.md) · [93 QM and GR by tree](93_qm_gr_by_tree.md) · [83 the Archimedes screw](83_the_archimedes_screw.md) · [90 divisors are definers](90_divisors_are_definers.md)
