# 42 — The Riemann Hypothesis without primes: the proposed proof structure, step by step

| | |
|---|---|
| Status | **A proposed proof structure (first capture 2026-06-03, headed "Clay proof structure, formalisation required"). It is not a proof: the premise that links the construction to ζ is the open Berry–Keating identification, and each lemma has a stated gap (§2).** `CONJECTURE` |
| Same standard as | [13](13_omgwtf_rh_proof.md) (the project's other RH argument) and the satellite repository's own statement that it does not prove RH |
| Code | none; the lemmas have no program behind them |
| Last verified | 2026-11-13: the logic of the argument and each cited theorem checked; no computation applies |

## 1. The idea

The usual direction is primes → Euler product → ζ(s) → zeros. The proposal
inverts it: the Cayley–Dickson tower (algebra, no primes) → fixed-point structure
→ zeros at σ = ½ → primes as consequence ("the primes are the negative space once
you know where the zeros are"). The page's axiom is that the tower exists.

*A structural remark to keep in view.* Any argument about the zeros of **ζ** must
at some point connect to ζ, and ζ is defined by the Dirichlet series and its
continuation (equivalently the Euler product). An argument that never references
the primes must therefore carry that connection in an assumption. Here it is the
identification of the non-trivial zeros with eigenvalues of Ĥ_RB (§2, step 4).

## 2. The steps, with their status

| # | Step as stated | Assessment |
|---|---|---|
| L1 | The Fermat-forbidden region σ > ½ is "compact: closed, bounded, algebraically complete", with uniformly repulsive interior dynamics (every point moves away toward higher vortex density, σ → ∞), no interior fixed point | **Gap.** The region σ > ½ of the complex plane is neither closed nor bounded (its closure is the half-plane σ ≥ ½), so it is not compact in the usual sense. "The Fermat-forbidden zone" has been *defined* in the framework as the region where aⁿ + bⁿ = cⁿ has no solutions; the set of integer solutions is not a region of the plane. The "natural dynamics" is not defined (no map is written), and the "uniformly repulsive" property is stated for a gradient of a "compression potential" that is never given. The page itself lists it as a formal target |
| L2 | By Brouwer, a continuous self-map of a compact convex set has a fixed point; interior points are not fixed (L1), so the fixed point is on the boundary | **The logic is valid, conditional on L1.** The Brouwer fixed-point theorem is `ESTABLISHED`: a continuous map of a compact convex set to itself has a fixed point. The step needs a *specific* continuous self-map of a *specific* compact convex set; neither is supplied, so there is nothing to apply Brouwer to |
| L3 | The boundary is σ = ½, "the fixed point of the Ptolemy inversion s ↦ 1 − s̄" | The identity itself is exact: s ↦ 1 − s̄ fixes exactly the line σ = ½ ([41](41_one_riemann_electron_universe.md) §2). What is not shown is that this line is "the boundary of the Fermat-forbidden interior" and that the Brouwer fixed point of L2 is the fixed point of the inversion. "Inward tension = outward buoyancy" names a balance without defining it. The inversion fixes the line for **every** function, so using it to place the zeros needs a reason that the zeros are fixed points of the *inversion*, which is RH itself |
| 4 | The non-trivial zeros are eigenvalues of Ĥ_RB, and "eigenvalues are the fixed points of the compression–decompression dynamics" | **This is the Berry–Keating conjecture** (Hilbert–Pólya lineage; [07](07_berry_keating_engine.md), [102](102_berry_keating_hilbert_polya.md)), `OPEN`: no self-adjoint operator whose spectrum is the set of zeros is known. The page marks it "partially established, requires completion". Further: an eigenvalue of an operator is not a fixed point of a map; the argument identifies two different notions |
| T | Therefore all eigenvalues of Ĥ_RB, and so all non-trivial zeros, lie on σ = ½ | Follows only if 1–4 hold. As in the RHP repository's own table of what is proved, imported and open ([13](13_omgwtf_rh_proof.md) §3), the step "zeros = spectrum of a self-adjoint operator" is where an RH proof would live, and it is open |

So the "theorem" is a derivation *from* the four steps, of which none is
established. The statements "QED without computing a single prime", "no
analytic continuation required" and "the Riemann Hypothesis is a theorem of the
Cayley–Dickson tower" are withdrawn as statements of fact.

## 3. The n-dimensional zeta function  `CONJECTURE`

The page defines ζ_n(s) = det(Ĥ_RB^{(n)} − s·I)^(−1), the "spectral zeta function of
the T_n algebra", with ζ_2 = ζ, ζ_4 quaternionic (L-functions), ζ_8 octonionic
(E₈ theta series), ζ_16 sedenionic (d* encoded), ζ_256 "where modular forms break",
and "all zeros of ζ_n are on σ = ½ for all n". Points to correct:

- det(Ĥ − s)^(−1) has **poles** at the eigenvalues of Ĥ, not zeros; so the definition as written places the eigenvalues at poles, which is the opposite of "zeros of ζ_n".
- A zeta function attached to the spectrum of an operator is the standard construction (spectral zeta, ζ_Ĥ(s) = Σ λ^(−s)), and it is not the Riemann zeta function for n = 2 unless the spectrum is the one required by the Berry–Keating conjecture.
- The named correspondences are not defined: "ζ_8 is the E₈ theta series" (a theta series is a modular form, not a zeta function; its associated L-function is a different object), and "ζ_256 where modular forms break" has no code ([40](40_modular_segue_three_papers.md) §6).
- "The Brouwer argument applies at every level": the same missing map and set (L1, L2) apply.

## 4. "Why this works without primes"  (the one exact element)

The page notes that once the zeros are known the primes follow, by the explicit
formula. That statement is correct and standard: Riemann's formula
π(x) = R(x) − Σ_ρ R(x^ρ) − … expresses the prime-counting function through the
zeros, and, in particular, a zero-free region on σ = ½ ± δ controls the error
term. What it does not do is *locate* the zeros; the dependence runs both ways
(the zeros are defined from ζ, which is defined from the primes).

## 5. The one-line proof

"The universe has one source; its shadow requires all zeros to be at σ = ½; the
universe exists; therefore the Riemann Hypothesis is true." The first two
premises are [41](41_one_riemann_electron_universe.md) (a proposal whose one test is a
null: §6 there); a statement about the physical universe cannot establish a
statement about ζ without a theorem connecting them. The line is withdrawn as an
argument and kept as the author's statement of conviction.

## 6. What the Clay Institute requires, and what would be needed

The Clay problem: a proof that all non-trivial zeros of ζ have real part ½. The
page's own list of formalisation targets is the correct list, and none is done:

1. prove the non-trivial zeros are eigenvalues of a (self-adjoint) Ĥ_RB: **the Berry–Keating conjecture**, open;
2. prove the dynamics of the interior are uniformly repulsive (requires the compression potential and the dynamics to be written down);
3. prove the boundary of the forbidden zone is σ = ½ in the algebraic sense (requires the zone to be defined as a subset of a space on which Brouwer applies).

The project's measured work on the actual zeros (25,000 of them, to 32 digits)
is in [133](133_canonical_maths.md) §5–6 and the RHP repository; it is `:CALCULATED`
evidence about the zeros, not a step of this argument.

## 7. "Historical note"

The page ends with a reading of Riemann's own position ("he was looking at the shadow
of σ = ½ cast onto the complex plane and noting that all the dark spots appeared
on the same line"). Riemann noted, in 1859, that it is "very probable" that all
non-trivial roots are real (that is, on the line), without proof, after
calculating the first few. The remainder (the proof "lives in the source") is the
author's statement.

## 8. Related pages

[07 Berry–Keating](07_berry_keating_engine.md) · [13 RH proof path](13_omgwtf_rh_proof.md) ·
[41 One Riemann electron](41_one_riemann_electron_universe.md) · [73 Why the half line](73_why_the_half_line.md) ·
[102 Berry–Keating and Hilbert–Pólya](102_berry_keating_hilbert_polya.md)
