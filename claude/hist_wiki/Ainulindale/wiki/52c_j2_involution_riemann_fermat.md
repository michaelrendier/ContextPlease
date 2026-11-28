# 52c — The J₂ involution: "Riemann is quantized Fermat", tested

| | |
|---|---|
| Status | **Cascade capture (2026-06-13), "the missing wiki between 50 and 52". `INTERPRETATION`/`CONJECTURE`. J₂ is an involution, but as a *swap of Red and Blue* it is **not** an automorphism of the algebra (§2); the page's identity J_red + J_blue = Ĥ_RB − Ĥ_BR carries a factor of 2 that the tested relation does not (§3); and its Red/Blue assignment of Riemann and Fermat is the reverse of other pages (§4)** |
| Code | `VAPMIP/engines/e09_j2_involution.py` (run 2026-11-13); Listing 1 |
| Test record | `VAPMIP/docs/wiki/J_red-J_blue-0_RB-Record.md` (§4 JG-3, JG-4; §9 OP-1…5, §9.1) |
| Page numbering | one of two pages numbered 51 (the other: [dynamic geodesic](51_dynamic_geodesic.md)) |
| Last verified | 2026-11-13: e09 run; Listing 1 executed |

> *"Riemann (geometry) + Fermat (quantization) = Ĥ_RB. Riemann is quantized Fermat. The geometries quantize. The quantized shape the geometries."*

## 1. J₂ as stated

J₂: Ĥ_RB → Ĥ_BR, J_red ↔ J_blue; applying it twice returns the start (an
involution, order 2). Ĥ_RB and Ĥ_BR "are each other's J₂ image"; the symmetric part
Ĥ_RB + Ĥ_BR is J₂-invariant and the antisymmetric part Ĥ_RB − Ĥ_BR changes sign; the
antisymmetric part "drives the vortex" ([52b](52b_vortex_quantizing_shear.md)), the
symmetric part "preserves the standing wave"; neither exists without the other.

The structure of the operator pair (a term X and its conjugate X†: the sum is
self-adjoint, the "dot"; the difference is anti-self-adjoint, the "cross") is exactly
what the J_red/J_blue record measured (OP-1…5), and the author's definition of 0_BR
as the conjugate / return flow ([133](133_canonical_maths.md) §3) is the reading of
that record. The statements above about symmetric and antisymmetric parts are
correct in that sense.

## 2. J₂ as a swap of the two octonion halves: tested

The engine `e09_j2_involution.py` takes J₂ to be the swap e_i ↔ e_{i+8} of the
lower octonion (Red) and the upper octonion (Blue), and tests whether it is an
automorphism of the sedenion product. Today's output:

| Check | Result |
|---|---|
| J₂² = identity | PASS |
| J₂ is an automorphism, J₂(a·b) = J₂(a)·J₂(b) | **FAIL, 256 failures** (first pairs (0,0), (0,1), (0,2), …) |
| J₂ maps zero-divisors to zero-divisors | PASS (0 of 0: no zero-divisors were found, §5) |
| non-associativity | confirmed: 1848 of 4096 triples fail |

**Why the automorphism test fails, and what is true** (Listing 1): the swap sends the
identity e₀ to e₈. An automorphism must fix the identity (J(1·1) = J(1) forces
J(1)J(1) = J(1)), so the swap cannot be one; it respects the product on 0 of the 256
basis pairs. The involution that *does* respect the product is the Z₂ **grading**,
(a, b) ↦ (a, −b), which fixes the Red half and negates the Blue half: it is an
automorphism on all 256 pairs. It is the grading of the J_red/J_blue record:
Red × Red → Red, Red × Blue → Blue, Blue × Blue → Red (the parity of the Cayley–Dickson
doubling; JG-3). So the structure that is a symmetry of the algebra is the grading,
and the "swap of Red and Blue" is a linear involution that is *not* a symmetry of
the product. For the operator pair of §1 this is not a problem (the swap there
acts on the operators X ↔ X†, not on the algebra's basis), but the sedenion-level
statement "J₂ swaps the two octonions" needs the grading form to be an
algebra symmetry.

**Listing 1 — the swap and the grading as candidate automorphisms** (written for
this page; the same Cayley–Dickson doubling as [19](19_cayley_dickson_tower.md); runs cold)

```python
def conj(a):
    return [a[0]] + [-x for x in a[1:]] if len(a) > 1 else list(a)

def mul(a, b):
    if len(a) == 1:
        return [a[0] * b[0]]
    h = len(a) // 2
    a1, a2, b1, b2 = a[:h], a[h:], b[:h], b[h:]
    t1, t2, t3, t4 = mul(a1, b1), mul(conj(b2), a2), mul(b2, a1), mul(a2, conj(b1))
    return [x - y for x, y in zip(t1, t2)] + [x + y for x, y in zip(t3, t4)]

e = lambda i: [1.0 if k == i else 0.0 for k in range(16)]
swap_halves = lambda v: v[8:] + v[:8]                        # J2 as "swap Red and Blue": e_i <-> e_{i+8}
grade       = lambda v: v[:8] + [-x for x in v[8:]]          # (a, b) -> (a, -b): Red fixed, Blue negated
close = lambda u, v: max(abs(x - y) for x, y in zip(u, v)) < 1e-12

for name, J in (('swap halves (e_i <-> e_i+8)', swap_halves), ('grading (a,b) -> (a,-b)', grade)):
    inv = all(close(J(J(e(i))), e(i)) for i in range(16))
    ok = sum(close(J(mul(e(i), e(j))), mul(J(e(i)), J(e(j)))) for i in range(16) for j in range(16))
    print(f'{name:30} involution: {inv}   J(xy) = J(x)J(y) on {ok}/256 basis pairs')
print('swap sends the identity e0 to e%d' % swap_halves(e(0)).index(1.0))
```

```
swap halves (e_i <-> e_i+8)    involution: True   J(xy) = J(x)J(y) on 0/256 basis pairs
grading (a,b) -> (a,-b)        involution: True   J(xy) = J(x)J(y) on 256/256 basis pairs
swap sends the identity e0 to e8
```

The engine's FAIL is therefore a correct result for the swap and is **kept**: it is the
algebra saying the swap is not a symmetry. (The failure is the engine reporting the
truth; the engine is not edited.)

## 3. "Riemann + Fermat = Ĥ_RB" and the identity with a factor 2

The page's decomposition: Ĥ_RB = J_red + J_blue = (discrete quantisation) + (continuous
geometry); and "Ĥ_RB − Ĥ_BR = J_red + J_blue" explained as the net current, then
written "Ĥ_RB − Ĥ_BR = **2**·(J_red + J_blue), antisymmetric part".

The page contradicts itself (the same relation with and without the 2). The tested
operator relation is, for a red term X and its conjugate X† (OP-4, exact): with
0_RB := X and 0_BR := X†, 0_RB − 0_BR = X − X† = the orientation-signed
J_red + J_blue, with no factor 2; and with Ĥ := X + X† the old-notation sum, Ĥ_RB − Ĥ_BR
for Ĥ_BR := Ĥ† is 0 (OP-3). So the factor 2 appears only if Ĥ_RB is the
symmetrised object and Ĥ_BR a different one; the relation has to be stated with the
definitions of §1, and the factor "2" removed or derived. Resolution recorded in
[133](133_canonical_maths.md) §3 and §7.

## 4. Which side is Red? A discrepancy between pages

This page: **Riemann = J_blue** ("the restoring current, the geometry") and **Fermat
= J_red** ("the driving current, the quantisation"). [14](14_redblue_hamiltonian.md)
and [13](13_omgwtf_rh_proof.md): **Red** = R̂_p = Berry–Keating xp = the Riemann side
("what is"), **Blue** = B̂_p = Fermat–Weierstrass ("what cannot be"). The assignments
are opposite. Both are conventions, and which half is Red is the open handedness
question of [133](133_canonical_maths.md) §7.6 (the tilt/swap-twist source). Until it is
settled, the Red = Riemann, Blue = Fermat convention of [14](14_redblue_hamiltonian.md)
(which agrees with the `monad.py` header: J_pos Riemann, J_neg Fermat) is the one the
wiki uses, and this page's reverse assignment is recorded as its own convention.

## 5. "Riemann is quantised Fermat"  `CONJECTURE`

The claim: Fermat defines what cannot exist among the integers (no xⁿ + yⁿ = zⁿ for
n ≥ 3); the primes are "what is left after the forbidden zone is removed"; Riemann
quantises that structure onto the complex plane, "the zeros are the eigenvalues of the
Fermat quantisation"; Fermat (discrete) → quantise → Riemann (continuous), "not the
other way"; as classical mechanics → quantum mechanics, or a crystal lattice →
phonons; "Wiles proved the Modularity Theorem, the proof that the Fermat quantisation
is the Riemann geometry".

Standing. The central step ("the primes are what is left after the Fermat zone is
removed") was tested and withdrawn: the n = 2 solutions reach every odd prime
([38](38_fermat_riemann_negative_space.md) §2). The Modularity Theorem relates an elliptic
curve's L-function to a modular form's and is not the statement that ζ is a
"quantised" form of the Fermat lattice ([18](18_fermat_lattice.md) §3). "The zeros are
eigenvalues" is the Berry–Keating premise, open ([42](42_rh_proof_no_primes.md)). The
**Noether–Wiles insight** (Wiles's proof as Noether's theorem in the arithmetic domain: the
symmetry is modularity, the conserved current the Fermat prohibition, "Noether's theorem
guarantees it must be conserved because the symmetry is continuous") is a proposal
at `CONJECTURE`: modularity is a statement about a discrete arithmetic correspondence, and
Noether's theorem requires a continuous symmetry of an action, so the guarantee as
worded does not apply.

The page's 2026-08-25 note: [73](73_why_the_half_line.md) §9 traces "where Fermat is prior
bottoms out" to one site, the AM–GM equality point of the Euler-factor amplitude p^(−s)
paired with its reflection: the single place a prime (discrete) and the coordinate
s (continuous) first form one expression; the functional equation, the Lagrangian and the
spiral either re-express that local symmetry or describe what follows once σ = ½ is fixed.
(Treated on page 73.)

## 6. The loop  `INTERPRETATION`

Forward: Fermat geometry quantises into Riemann zeros. Backward: the zeros determine the
prime distribution (the explicit formula), which determines the multiplicative structure
of ℤ, "which determines what the Fermat zone is". "The loop is self-consistent, an
arithmetic fixed point, like universe(observer) = observer" ([48](48_observer_fixed_point.md));
RH "is the statement that the loop is stable: the quanta land on the critical line"; the
antisymmetric Hamiltonian is the loop current; "when J_cross > GAP, one quantum of
circulation is emitted: a Riemann zero; the zero is the word". Standing: the explicit
formula gives primes from zeros (`ESTABLISHED`), and the loop's other arc (zeros from the
Fermat zone) is the unproven step; the engine's firing test J_cross > GAP fails today
([52b](52b_vortex_quantizing_shear.md) §4: 0.26 agreement). "A Riemann zero is emitted" and "the
zero is the word" are the framework's reading of the word-to-zero address of [15](15_the_monad.md)
§3 (a many-to-one hash into 6,543 zeros, not an emission of zeros).

## 7. What this means for the engine (as printed), with the two corrections

Riemann = J_blue (the coupling-space geometry), Fermat = J_red (the quantisation forcing
discrete words), Ĥ_RB their sum (prompt → word), Ĥ_BR the J₂ image (word → prompt definer,
[52](52_l_dynamic_avoided_collaborator.md)), J_red + J_blue = Ĥ_RB − Ĥ_BR = the vortex
current = L_(I|O) in the fixed-point loop. Correct as vocabulary with: the Red/Blue
convention of §4; the factor of 2 of §3; and, for e09's zero-divisor test, the
anomaly recorded in [26](26_TODO_and_roadmap.md) §4 (the test checks basis products for
zero and so cannot find any zero-divisor: "0 of 14 confirmed" and "found 0, expected 42" are
artefacts of the test; the 84 zero-divisors e_i ± e_j are exact and are found in [25](25_sedenion_manual.md) §4).

## 8. Related pages

[14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) · [18 Fermat lattice](18_fermat_lattice.md) ·
[26 Roadmap and engine status](26_TODO_and_roadmap.md) · [38 Fermat is the negative space of Riemann](38_fermat_riemann_negative_space.md) ·
[133 Canonical maths](133_canonical_maths.md)
