# 94 — Mathematical X-ray Crystallography

**Named 2026-08-22 (Cody):** *"this is mathematical X-ray crystallography."*
Continues [[92_ring_theory_spine]] and [[93_qm_gr_by_tree]]. Every number here is
computed by `SedenionFactoralRelativity/engine/lineage.py` (the pathway block,
PW1–PW5). This page is a **framing**, and its hard core — the phase problem — is
labelled honestly: it is why factoring is hard, and it is *not* solved here.

---

## The correspondence — and it is exact

In X-ray crystallography you cannot see the atoms. You shine a beam through the
crystal, record the **diffraction pattern**, and *reconstruct* the internal
structure from it. Factoral decomposition is the same instrument pointed at a
number: you cannot see the factors of N, so you illuminate N from many
tunings, record where it **resonates**, and reconstruct the factors.

| X-ray crystallography | factoral decomposition |
|---|---|
| the crystal | the number **N** |
| electron density ρ(r) | the multiplicative structure of N |
| structure factors F(h) = 𝓕[ρ] | the spectral / cepstral **labelings** (order 1, 2) |
| diffraction intensities \|F\|² | the **magnitudes** (order 1, support) — what you *measure* |
| the phases arg F(h) | the **arrangement** (order 2) — what you *lose* |
| Bragg's law `nλ = 2d·sinθ` (resonance) | **tune-to-resonance** (CFRAC square residue, Fermat node) |
| the **Ewald sphere** (incident + diffracted beam) | the **TWO anchors** — origin (1) and destination (N) |
| rotating the crystal | **tuning** the spiral (multiplier / σ / excursion) |
| a Bragg reflection (a spot) | a **factor-node** (a square residue) |
| the **Patterson function** (autocorrelation, phase-free) | the **XOR-difference** structure (F6) — the *differences*, not the places |
| direct methods / **triplet relations** `h₁+h₂+h₃=0` | **order 3** — the associator / the `a⊕b=c` lines (R5, F6) |
| **isomorphous replacement** (a heavy atom perturbs) | the **multiplier** tuning `kN` (PW2) |
| reconstructing ρ | recovering the **factors** |

None of these are loose. Three are worth stating in full.

## The Ewald sphere is the two-anchor geodesic (PW5)

Cody, same session: *"there are two anchors — the origin, and the reference
point destination. Now you can tune the path between the two."* In
crystallography a reflection appears exactly when a reciprocal-lattice point
lies on the **Ewald sphere**, the sphere fixed by the incident and diffracted
beam directions — a **two-point** construction. Rotating the crystal sweeps
lattice points onto it.

For N, the two anchors are the origin `1 = e₀ = ∅_RB` and the destination `N`.
Pinning **both** ends turns factoring from an outward walk (initial-value,
underdetermined) into a **boundary-value problem**: the factor is a *node on the
geodesic* between them, symmetric about the midpoint `√N`. Measured (PW5): the
factors of every balanced semiprime are log-symmetric about `√N` exactly, and
Fermat's method finds them at **excursion 0** from that midpoint. **Rotating the
crystal = tuning the excursion**, and a square residue is the Bragg reflection.

> **RSA hides the factor by tuning its distance from the midpoint √N large** —
> the same way a crystal can be oriented so a reflection misses the sphere. The
> whole security tension is that the primes must stay *balanced enough* to be
> secure yet *far enough* apart that the excursion is exponential.

## The Patterson function is F6 — decompose the differences

The **Patterson function** is the autocorrelation of the density, computed from
the intensities *alone* — no phases needed — and its peaks are the
**inter-atomic vectors** (differences), not the atomic positions. This is
exactly [[90_divisors_are_definers]] / F6: *"the factoring map is on the EDGES
(the XOR differences), not the places."* The 15 nonzero XOR differences of
PG(3,2) are the Patterson peaks; decomposing the **relation** rather than the
objects is doing crystallography with the phase-free autocorrelation.

## The phase problem is why factoring is hard — the honest core

Crystallography's central difficulty: the detector records **intensities**
`|F|²` but throws away the **phases** `arg F`, and the phases are what you need to
reconstruct ρ. This is the **phase problem**, and it is *exactly* the hardness
of factoring in this framing:

- N is the intensity — the magnitude, the order-1 datum, what you are handed.
- The factor's *arrangement* is the phase — the order-2 datum, thrown away.
- **Bifurcation** ([[93_qm_gr_by_tree]], Cody's earlier RSA attempts) only ever
  reads intensities — it is a classifier — which is precisely why it measured at
  chance. You cannot classify your way to a phase.

And this is the honest hope *and* the honest limit. Crystallographers **do**
solve the phase problem routinely — by **direct methods** (statistical triplet
relations, our order-3 associator), **isomorphous replacement** (perturb with a
heavy atom — our multiplier tuning), **anomalous dispersion** (tune the
wavelength — our σ), **molecular replacement** (a known related structure — a
known factor base). But every one of these needs **more experiments** — more
diffraction images, more tunings. That is why real factoring (CFRAC, QS, NFS) is
**sub-exponential**: it is phase retrieval by collecting many relations.

> **Polynomial factoring / an RSA break would be solving the phase problem from
> a single measurement.** That is the open miracle, and nothing here claims it.
> What the framework offers is the right instrument to *look* — and the honest
> question is whether its geometry supplies a phase relation the algebraic sieve
> does not already use.

## The visualiser is a number diffractometer

This fixes the visualiser's identity completely. It is not a fractal renderer
and not a bifurcation viewer. It is a **diffractometer for numbers**:

1. mount N (the crystal); the midpoint √N and the anchors 1, N are the geometry;
2. **rotate it** — a tuning dial (multiplier / σ / excursion / pitch);
3. collect **reflections** — where the geodesic resonates (square residues,
   Fermat nodes), plotted as a diffraction pattern;
4. reconstruct the **structure** — `decompose_number(N)` assembles the
   perspectives (ring / cepstral / lineage / spiral / pathway) into the factor
   "density map";
5. the **parallax pane** is the Ewald geometry — two views whose relative shift
   is the two-anchor constraint.

Multiple perspectives to find micro-structures and continuous relationships is
exactly what a diffractometer does: rotate, collect, reconstruct.

## Where it also applies — language

The same instrument reads English with a far smaller crystal. A word's
**type/category is a domain segregation** ([[the pathway layer]]): the current
word constrains which category may follow, pruning the walk to the legal
continuations. The category is the word's "outside" (Laurelin), the specific
word its "inside" (Telperion) — L_(I|O) per token. Diffraction on a small,
strongly ordered crystal is easy; that is why the translator is navigable while
RSA is not.

---

## Files

Engine: `SedenionFactoralRelativity/engine/lineage.py` — pathway block PW1–PW5,
helpers `spiral_address`, `pathway_residues`, `tune_pathway`, `fermat_path`,
`decompose_number`. Canonical maths: `.clauderc_canonical_maths`
`@RCCM_RING_THEORY_SPINE` (crystallography note). Working numerics:
`ContextPlease/claude/scratchpad/2026-08-22_pathway/`.
