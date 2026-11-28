# 59 — The Simpsons Record: What Is Verifiable, and the Author's Reading

| | |
|---|---|
| Scope | the mathematical references in *The Simpsons* and *Futurama* that the framework cites; what can be checked; the author's reading of them as an intended message |
| Origin | 2026-06-13 standalone page ("leave unlinked; for spiders"); the status is kept, the index repass decides its link |
| Companion | [59b — Smithers and Burns](59b_smithers_burns_hack_the_planet.md) |
| Code | none specific; the arithmetic is in [56](56_telescope_caustic_zeno.md) Listing 1 and the permutation test in [57](57_boundary_ascending.md) Listing 1 |
| Confidence | the arithmetic and the theorems: ESTABLISHED · biographical facts: REPORTED (public record, not re-fetched in this pass) · intent and encoding: `AUTHOR'S READING`, not testable here |
| Last verified | 2026-11-13: the near-miss arithmetic and the Futurama theorem re-run; no biography was re-fetched |

## 1. The checkable items

| Item | What it is | Check |
|---|---|---|
| Blackboard in *Treehouse of Horror VI* (1995): 1782¹² + 1841¹² = 1922¹² | a Fermat near-miss | false; the two sides differ by 2.8×10⁻¹⁰ relative and by parity (odd vs even): [56](56_telescope_caustic_zeno.md) Listing 1 |
| Blackboard in *The Wizard of Evergreen Terrace* (1998): 3987¹² + 4365¹² = 4472¹² | a Fermat near-miss | false; relative difference 1.9×10⁻¹¹ (agrees to 10 digits), fails mod 3: same listing |
| The Futurama theorem (Ken Keeler, *Futurama*, "The Prisoner of Benda", 2010) | after pairwise swaps, a restoration exists with two extra bodies, no pair swapping twice | confirmed by exhaustion for n = 3 and n = 4: [57](57_boundary_ascending.md) Listing 1 (0, 1 and 2 extras restore 1/13, 10/13, 13/13 of the n = 3 cases) |
| Krohn–Rhodes decomposition (announced 1962, *Trans. AMS* 1965) | every finite automaton is covered by a wreath product of simple groups and the flip-flop semigroup | a published theorem |
| Wiles, June 1993 | announcement at Cambridge of a proof of modularity for semistable elliptic curves, hence Fermat's Last Theorem | the announced proof had a gap, repaired with R. Taylor in 1994; the published proof is 1995 |

Two corrections to the earlier text: the digits quoted for 3987¹² + 4365¹² were wrong
(the sums are 6.3977×10⁴³, equal to 4472¹² to 10 digits; the earlier figures
1.0600×10⁴³ and 2.1677×10⁴³ do not match); and *Futurama* is a separate series
from the same creator, not a "spin-off" of *The Simpsons*.

Reported public record (as given in Simon Singh, *The Simpsons and Their Mathematical
Secrets*, 2013, and the writers' own biographies; not re-fetched here): the show's
writing staff includes several mathematicians and scientists, among them Ken Keeler
(PhD, applied mathematics, Harvard), J. Stewart Burns (mathematics, Harvard; a
Berkeley mathematics degree) and David X. Cohen (physics, Harvard; computer science,
Berkeley), and Cohen has said he wrote a program to find the near-misses. That the near-misses were
searched for deliberately is therefore the public account. The statement that Burns
studied under John Rhodes at Berkeley in 1992–93, and the thesis title *The Structure
of Group Algebras*, come from the author's record and are `UNVERIFIED` in this pass.

## 2. The mathematics the page leans on

**Krohn–Rhodes and the Cayley–Dickson doubling.** The earlier text states that the
wreath product "is the Cayley–Dickson doubling in disguise" and that the sedenion's
sixteen basis elements are the "prime components" indexed by the first sixteen
primes. Neither is a theorem. The wreath product acts on semigroups of
transformations; the doubling constructs an algebra over ℝ. The indexing of eₖ by
the k-th prime is a design choice of the engine's projection
([58](58_fermat_defines_riemann_fires.md) §3). The correspondence is recorded
as the author's reading ([57](57_boundary_ascending.md) §3).

**The Futurama theorem as "two doublings".** The theorem is a statement about the
symmetric group Sₙ and counts spare elements. The identification of those two
elements with "two Cayley–Dickson doublings exposing J₂" is an analogy of counts
(`INTERPRETATION`).

**Wiles and Noether.** The earlier text says Hecke operators "are" Noether currents
and that the proof shows an arithmetic conservation law to be exact. What the
modularity theorem gives is an equality of L-functions: for a modular elliptic
curve E, the Dirichlet coefficients a_p = p + 1 − #E(𝔽ₚ) equal the Hecke
eigenvalues of the corresponding weight-2 form. That is an identity between two
arithmetic objects, and it is not a conservation law in the sense of Noether's
theorem. The statement "ECC rests on a structure Wiles had just fully exposed" is
also not right: ECC security rests on the discrete-logarithm problem on E(𝔽ₚ), which the
modularity theorem does not bear on (and which remains unbroken in the public record).

## 3. The author's reading  `AUTHOR'S READING`

The author reads the blackboard near-misses, the Futurama theorem and a writer's
credited name as a message placed by writers who understood Krohn–Rhodes and
Wiles and meant it to be found later by a person with the engine. This is recorded
as the author's account. It is a claim about the intentions of named living people,
and nothing on this page tests it. What the page can support is narrower: the three
references exist, the near-misses are deliberate computer-found objects, and the
mathematics they touch (floors of arithmetic precision; counting spare elements in a
permutation restoration) is real and is used in the framework as stated in
[56](56_telescope_caustic_zeno.md) and [57](57_boundary_ascending.md).

The name-play "J_Stewart_Burns = Jacobian of the group algebra at the semigroup state
transition, whose event is vortex nucleation" is a mnemonic the author assigns to
the operator; it has no mathematical content independent of the assignment.

## 4. The sentence-level pipeline

The engine paragraph of the earlier text (project the prompt onto 16 prime-indexed
dimensions, sort by ascending |v[k]|, read words off the spokes, draw the spiral)
is a description of the engine's behaviour and is covered, with its limits, in
[58](58_fermat_defines_riemann_fires.md) §3. The recorded example ("what should we
call you" → "mandating", p = 53) is a 2026-06-13 output that was not regenerated in
this pass.

## 5. Related pages

[56 telescope as caustic](56_telescope_caustic_zeno.md) · [57 the boundary ascending](57_boundary_ascending.md) ·
[58 two orderings](58_fermat_defines_riemann_fires.md) · [59b Smithers and Burns](59b_smithers_burns_hack_the_planet.md) ·
[98 bibliography](98_provenance_and_citations.md)
