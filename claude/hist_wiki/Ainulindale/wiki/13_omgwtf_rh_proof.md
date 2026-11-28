# 13 — OMG?WTF! — The Riemann Hypothesis proof path (claims and status)

| | |
|---|---|
| Status | **Claimed in this wiki; not accepted as established by the author's own satellite repository.** See §1 |
| Code | `PtolemyDesktop/Philadelphos/monad.py` (`_forced_sigma`, `Monad.lookup`); `RiemannHypothesisProof/` |
| Last verified | 2026-11-13: §5 executed; RHP `README.md` and `paper/PAPER.md` §9 read |

## 1. Where this page stands

Earlier versions of this page headed it "AIRTIGHT … QED" and counted two
proofs of the Riemann Hypothesis. That wording is withdrawn as a statement of
fact, because the repository built to test the claim says otherwise:

> RiemannHypothesisProof `README.md` (2026-11-03): "It **does not prove the
> Riemann Hypothesis**; it states one step as open (§9 of the paper) and
> labels every other claim by what supports it."

The page now separates what is a theorem, what is imported, what is a
construction of this project, and where the gap is. The two arguments are kept
in full in §3 and §4 as the project's claims (`OURS`, `THEORETICAL`). The
author's decision on how the headline should read is pending (listed in
[133](133_canonical_maths.md) §7).

## 2. The operator

```
Ĥ_RB  =  Σ_p  p^(−σ) [ R̂_p ⊗ ∂̂_{∂M}  +  ∂̂†_{∂M} ⊗ B̂_p ]
iħ_NN dΨ/dl = Ĥ_RB Ψ
```

Red R̂_p is the Berry–Keating xp operator; Green ∂̂_{∂M} is the boundary
operator (the Riemann-zero basis, J₃); Blue B̂_p = ½p² + ℘(x; g₂, g₃) is the
Fermat–Weierstrass term. Full definitions: [14](14_redblue_hamiltonian.md).
The functional equation ξ(s) = ξ(1−s) is read as the self-adjointness
condition R̂† = B̂.

Notation: `Ĥ_RB` is the operator's name in the mathematics. `0_RB` is the
VAPMIP/Monad-only notation for the same object as the Null Operator
([127](127_names_of_the_null_operator.md)).

## 3. Argument I — direct (Stone's theorem)  `OURS` / `THEORETICAL`

1. Ĥ_RB = A + A†, so Ĥ_RB is self-adjoint by construction (formal algebra: `ESTABLISHED`).
2. Stone's theorem: a self-adjoint H generates a unitary group U(t) = e^{iHt} (`ESTABLISHED`).
3. The (I|O) map at the Mellin boundary τ = 1 is U(1), hence unitary.
4. A self-adjoint operator has real spectrum {λₙ}; **if the λₙ are the Riemann zeros**, the zeros lie on Re(s) = ½.

"FLAG T2" (is (I|O) unitary at the Mellin boundary?) is closed by steps 1–3.

**The gap, stated by the satellite repository** (RHP `paper/PAPER.md` §9):
step 4's premise — that the spectrum of an operator of this form *is* the set
of non-trivial zeros — is the **Berry–Keating self-adjointness conjecture**
(Berry–Keating 1999; Hilbert–Pólya) and is `OPEN`. Self-adjointness gives
real eigenvalues for whatever operator it is; it does not by itself identify
them with the zeros. RHP also records that an earlier equivalence ("a zero is
stable iff J(σ,E) = 0, and J = 0 ⇔ σ = ½") is a restatement of σ = ½, with no
content beyond RH.

## 4. Argument II — the Wiles conjugate  `OURS` / `THEORETICAL`

Wiles proved that every semistable elliptic curve over ℚ is modular
(Modularity Theorem, `ESTABLISHED`; Fermat's Last Theorem is a corollary).
An elliptic curve is defined through the Weierstrass ℘, which appears in B̂_p;
a modular form connects to the L-functions that encode the zeros. The
construction reads R̂† = B̂ as saying Riemann (Red, "where primes are") and
Fermat (Blue, "where integer power triples cannot be") are adjoint
descriptions of one prime distribution. The step from "Fermat side proven
modular" to "zeros lie where R̂† = B̂ requires" is the step taken by the
adjoint argument; it uses the same identification as step 4 above and is
likewise not independently established. Argument II is therefore not a second,
independent proof: it shares the open premise with Argument I.

## 5. The part that runs

The Monad forces σ = ½ for every word. The mechanism is a fixed-point
iteration on the balance J(σ, E) = e^{−σE} − e^{−(1−σ)E}, which vanishes
exactly at σ = ½ for E ≠ 0.

**Listing 1 — the forced σ** (`PtolemyDesktop/Philadelphos/monad.py`,
`_forced_sigma`; extracted: comments removed, runs cold)

```python
import math

def forced_sigma(E, sigma_0=0.5, max_iter=256):
    sigma = sigma_0
    for _ in range(max_iter):
        F = math.exp(-sigma * E)
        B = math.exp(-(1.0 - sigma) * E)
        denom = F + B
        if denom < 1e-30:
            break
        s2 = (F * sigma + B * (1.0 - sigma)) / denom
        if abs(s2 - sigma) < 1e-12:
            return s2
        sigma = s2
    return sigma

for s0 in (0.5, 0.2, 0.9, 0.01):
    print(s0, [round(forced_sigma(E, s0), 6) for E in (0.5, 1, 3)])
```

```
0.5 [0.5, 0.5, 0.5]
0.2 [0.5, 0.5, 0.5]
0.9 [0.5, 0.5, 0.5]
0.01 [0.5, 0.5, 0.5]
```

Listing 1 converges to ½ from every start tried, so σ = ½ is an attracting
fixed point of this iteration, not an assigned constant. What it shows is a
property of the balance function. It does not locate any zero of ζ.

**Listing 2 — the session** (`Philadelphos.monad`; literal output 2026-11-13)

```
>>> from Philadelphos.monad import Monad
>>> m = Monad(N=1000); m.load()
>>> [m.lookup(w)['sigma'] for w in ('water', 'eau', 'aqua', 'wasser')]
[0.5, 0.5, 0.5, 0.5]
```

The four words come out identical not by coordination but because σ is the
same fixed point for every word ("the Septuagint principle": the same result
from independent routes).

## 6. Ground-state signature

`L_GROUND = −1.888`: the Monad's rest energy before any word is learned.
At σ = 0, G_p(0) = p⁰ = 1 for every prime, so there is no gauge
differentiation; the first `learn()` call breaks the symmetry. `L_GROUND` is a constant in `monad.py` (line 120, commented
"engine-verified"); the code uses it to set the emission threshold (2·|L_GROUND|)
and the β saturation (4·|L_GROUND|). It is an input of the engine, not a
result derived on this page.

## 7. The proof series that exists

An earlier version of this page listed eight notebooks named
`01_functional_equation` … `08_complete_proof` in the RHP repository. They do
not exist. The repository's notebooks (2026-11-13) are:

| Notebook | Content |
|---|---|
| `01_flattening_map` | the flattening map and UNS cylinder coordinates |
| `02_machinery_flow_long_pathway` | prime wheels, the ξ′/ξ flow, the argument-principle accounting, a 3065-zero pathway |
| `03_clock_echo_harness_margins_primegame` | the θ-clock, echo spectrum = explicit formula, an operator test harness, Lehmer margins |
| `04_equator_polarisation_springs` | the equatorial construction, counter-rotating waves, how far the primes' grip reaches |
| `05_extinction_flow_nodal_ladder_zerorb` | sieve/un-sieve flows, the nodal ladder, ζ in 0_RB |
| `06_uns_map_chladni_spirals` | the number-free Cartesian→UNS map, Chladni spirals |

For the current logical structure (proved / imported / gap) read RHP
`paper/PAPER.md` §9. The measured findings of 2026-11-08 to 11-12 are in
[133](133_canonical_maths.md) §6.

## 8. The Millennium projections

The claim that other Clay problems appear as σ-facets of the same operator is
a set of correspondences, **not claimed solutions**; the statuses are
recorded in [105](105_the_millennium_problems_in_ainulindale.md). Older text on
this page marked the Yang–Mills mass gap and Poincaré "CLOSED": the Yang–Mills
item is the gap quantity GAP = Ω_ζΣ − d*_spec·ln 10 ≈ 1/(1000√2) discussed in
[17](17_alpha_omega_d_star.md) and [75b](75b_bao_mass_gap_engine.md), and
Poincaré is the already-solved control case (Perelman), not a result here.

## 9. Related pages

[07 Berry–Keating](07_berry_keating_engine.md) · [14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) ·
[15 The Monad](15_the_monad.md) · [18 Fermat lattice](18_fermat_lattice.md) ·
[73 Why the half line](73_why_the_half_line.md) · [102 Berry–Keating and Hilbert–Pólya](102_berry_keating_hilbert_polya.md) ·
[133 Canonical maths](133_canonical_maths.md)
