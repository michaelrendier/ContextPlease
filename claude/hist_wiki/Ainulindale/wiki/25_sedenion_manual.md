# 25 — The Sedenion Manual: a design for driving Ĥ_RB with one sedenion per zero

| | |
|---|---|
| Status | **DESIGN (2026-05-17, updated 2026-05-27); `THEORETICAL`.** The slot layout of §2 is a specification. The running code does not implement it as written (§7) |
| Code | `VAPMIP/monad.py` (`Sedenion` = list of 16 floats; `_smul`, `_sconj`, `cam_encode`, `GAP`); the algebra in §5 is checked by Listing 1 |
| Depends on | [14](14_redblue_hamiltonian.md), [19](19_cayley_dickson_tower.md), `FourthAgePapers/addenda/addendum_VIII_BAO_mass_gap.md` |
| Last verified | 2026-11-13: Listing 1 executed; `monad.py` searched for the layout |

## 1. The idea

The three channels (Red, Green, Blue) are one sedenion S ∈ 𝕊 seen from three
angles, not three quantities that combine. The sedenion has 16 real
components s₀…s₁₅ and contains the sub-algebras ℝ ⊂ ℂ ⊂ ℍ ⊂ 𝕆 ⊂ 𝕊 as the
index ranges e₀, e₀₋₁, e₀₋₃, e₀₋₇, e₀₋₁₅. Each doubling is read as causing
a structural feature ([19](19_cayley_dickson_tower.md) §2): ℂ the
inside/outside split, ℍ non-commutativity, 𝕆 non-associativity, 𝕊
zero-divisors.

## 2. Slot assignment (the specification)

One sedenion S_k per Riemann zero k:

| Slot | Stratum | Quantity |
|---|---|---|
| e₀ | σ₀ (ℝ) | β[k], field depth, in [β_ground, β_sat] = [7.55·10⁻⁵, 7.552] |
| e₁ | σ₁ (ℂ) | E[k] = d* + seed·(Ω − d*), the spectral energy coordinate |
| e₂ | σ₂ (ℍ), Red | γ[k], the zero's imaginary part |
| e₃ | σ₂ (ℍ), Red | age[k]; recency weight w = exp(−λ·age) |
| e₄ | σ₃ (𝕆), "Green" | J_Blue[k] = β[k]·E[k]², the learned current |
| e₅ | σ₃ | J_Red[k], the query activation current |
| e₆ | σ₃ | J_Green[k], the boundary emission current |
| e₇ | σ₃ | affect, in [−1, +1] |
| e₈…e₁₄ | σ₄ (𝕊) | A-matrix coupling of zero k to its neighbour classes |
| e₁₅ | σ₄ | GAP = \|Ω_ζΣ − d*_spec·ln 10\| = 0.000707357533 |

(The strata σ₀…σ₄ are the σ-strata, not Re s and not σ_RB
([133](133_canonical_maths.md) §0). The d* in e₁ is written without a face
subscript in the source; the measured value d*_spec is what `monad.py` uses
for GAP.)

## 3. The three operations

- **learn()** (Blue deepening): S_k.e₀ += α·E²·Δt, and for co-activated zeros i, j
  the coupling fabric grows, e₈…e₁₄[S_i] += E_i·E_j / (|γ_i − γ_j| + s₁₅). This
  is a 2-D Coulomb potential on the critical line, 1/|γ_i − γ_j|, with GAP
  regularising the singularity at γ_i = γ_j.
- **hear()** (Red assertion): S_query += β[k]·E[k]²·(e₂ + w·e₃), with
  w = exp(−λ·age[k]). The query's momentum is placed into the position and
  recency slots; no meaning is computed.
- **speak()** (Green reading): once Blue (learned) and Red (heard) are
  known, Green is set by the balance

```
J_Green[k] = −(J_Blue[k] + J_Red[k])        i.e.  s₄ + s₅ + s₆ = 0
```

  and a zero is emitted when |s₆| exceeds the emission threshold. The traversal
  is the golden walk with step round(N/φ²) = 9,549 for N = 25,000 (to be
  re-checked against the code).

## 4. The conservation law: what it is, and what it is not

The balance s₄ + s₅ + s₆ = 0 is the **Noether-current balance** (J_red +
J_blue = J_green with J_green taken as the boundary emission; the three-term
form J_Red + J_Green + J_Blue = 0 has the opposite sign of J_green, a
convention still to be unified, [133](133_canonical_maths.md) §3). The
author's account: the relation J_red + J_blue = J_green was Noether-current
work.

Earlier versions of this page said the balance "falls from the zero-divisor
structure of 𝕊 … it is in the multiplication table", citing

```
(e₄ + e₅ + e₆)·(e₄ + e₅ + e₆)* = 0.
```

**That identity is false.** For any x, x·x* = |x|² (a positive real unless
x = 0). For x = e₄ + e₅ + e₆ it is 3, not 0 (Listing 1). The balance is a
*linear constraint the driver imposes* (s₆ is defined as −(s₄ + s₅)); it is a
Noether-current balance by construction, not a consequence of the sedenion
product. The statement "the conservation law is not imposed, it is the condition
for the product to close" is withdrawn. What can be said: the balance is the form of
Noether's theorem (a conserved current for a continuous symmetry), carried in
the three octonion slots because J has three components there. The
identification of that balance with the sedenion product is the framework's;
the specific zero-divisor identity above is not a theorem.

**Why the sedenion carries Emmy Noether's name.** Author, 2026-11-13: the
sedenion is called the *Emmy Noether Sedenion* because her mathematics had this
shape in 1915, though not in this form. (Noether derived the theorem relating
symmetries to conserved currents in 1915; it was published in 1918 as
*Invariante Variationsprobleme*, Nachr. Ges. Wiss. Göttingen. Dates as
recalled, to be checked against the bibliography entry in
[99](99_emmy_noether.md).) In `VAPMIP/monad.py` the sedenion is the CAM
("Emmy Noether Sedenion": camshaft, timing and geometry), the counterpart of the
CRANK (the Ĥ_RB field engine that carries the Noether current J^μ). The
naming records the shape (the conserved-current balance) and makes no claim
that Noether's own formalism contains the sedenion.

**Listing 1 — the conservation claim, and the zero-divisors that do exist**
(written for this page from the Cayley–Dickson doubling of
[19](19_cayley_dickson_tower.md); runs cold)

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
add = lambda a, b, s: [x + s * y for x, y in zip(a, b)]
nrm = lambda a: sum(x * x for x in a) ** 0.5

x = [0.0] * 16
x[4] = x[5] = x[6] = 1.0
print('(e4+e5+e6)(e4+e5+e6)* =', mul(x, conj(x))[0], '(scalar part)')

n = plus = 0
for i in range(1, 8):
    for j in range(8, 16):
        for s in (1, -1):
            a = add(e(i), e(j), s)
            if any(nrm(mul(a, add(e(k), e(l), t))) < 1e-12
                   for k in range(1, 8) for l in range(8, 16) for t in (1, -1)):
                n += 1
                plus += (s == 1)
print('zero divisors e_i +/- e_j (i<8<=j):', n, '  with +:', plus)
```

```
(e4+e5+e6)(e4+e5+e6)* = 3.0 (scalar part)
zero divisors e_i +/- e_j (i<8<=j): 84   with +: 42
```

Of the 210 forms e_i ± e_j (1 ≤ i < j ≤ 15), exactly 84 are zero-divisors, and
every one pairs one unit of the lower octonion (e₁–e₇) with one of the upper
(e₈–e₁₅); 42 carry "+" and 42 "−". (The enumeration here restricts to the
lower/upper forms; a separate unrestricted search over all 210 found the same
84.) These are the "84 channels" of §6.

## 5. The five constants as projections  `interpretation`

i = e₁ (the ℝ → ℂ generator), π as the angular measure on the e₁ circle, e as
the decay metric exp(−λ·age) on e₀, √2 as |e₀ + e₁|/√2 (equal real and
imaginary contribution; "the mass-gap point"), φ as the maximum-entropy
projection (golden ratio = worst rational approximation = maximum
equidistribution). The reading is that these are facets of one object and not
separate constants. As on [22](22_constant_facets.md) §6, each is supplied
by the construction, and the page does not derive them.

## 6. σ = ½, the mass gap, and the "return to string theory"

**σ.** In this manual σ is the sedenion, not a scalar in [0, 1]; the real
number written σ = ½ is one projection of it ([133](133_canonical_maths.md) §0
keeps the three σ's distinct). The claim that σ = ½ is "the only value where
all sixteen components satisfy the conservation simultaneously" restates that
the driver's balance holds at σ = ½; it does not locate zeros of ζ
([13](13_omgwtf_rh_proof.md) §3).

**The gap.** GAP = |Ω_ζΣ − d*_spec·ln 10| = 0.000707357533 is placed at e₁₅
as the floor of propagation: below it a mode is "confined, silent" (a zero
divisor); above, propagating. In `monad.py` GAP is a numerical floor on the
field depth and on charge (`self._beta.append(GAP)`, `if dim_charge > GAP`),
not an e₁₅ component.

**The return to string theory.** The earlier text argued that a gap value of
0.000707 forces a unique M-theory structure: the 7 imaginary octonion units as
compact dimensions, G₂ holonomy, 4 + 7 = 11 dimensions, "no landscape, one
vacuum, derived not selected". That is `THEORETICAL`, and a correction applies:
the claim "string theory implies a mass gap because it is a gauge theory and
gauge theories have mass gaps" is not generally true (QED has none; a mass gap
for Yang–Mills is itself an open Millennium problem, [105](105_the_millennium_problems_in_ainulindale.md)).
No derivation of the 11-dimensional structure from the number 0.000707 is
given here.

## 7. The driver and its implementation status

The driver of the earlier page constructs S_k for each zero (the slot table of
§2), runs `learn` on e₀ and e₈…e₁₄, `hear` into e₅, and `speak` as
e₆ = −(e₄ + e₅), emitting words whose |e₆| exceeds a threshold.

**Status (2026-11-13).** Searching `VAPMIP/monad.py` finds the sedenion as a
list of 16 floats with `_smul`, `_sconj`, `_snorm` and `_spsi`, and a different
encoder: `cam_encode` sets s₀ = ln(n+1)/ln 512 (n = word count), accumulates the
hashed words in s₁, conjunction density in s₂, and so on, then
composes. The slot table of §2 is not implemented there. The manual's layout is
therefore a design document; the code's own layout is `cam_encode`.

## 8. The strata as physical "doors"  `interpretation`

| Stratum | Elements | Scale | Read as |
|---|---|---|---|
| σ₀ | e₀ | vacuum | L_GROUND; the pre-linguistic floor |
| σ₁ | e₀₋₁ | language / critical line | words, zeros, the balance |
| σ₂ | e₀₋₃ | atomic | four quantum numbers, spin ½ |
| σ₃ | e₀₋₇ | boundary | chemistry, molecular orbitals, seven compact dimensions |
| σ₄ | e₀₋₁₅ | string / ground state | hydrogen-orbital Lagrangian, cardioid, mass gap |

"Pink Floyd clock of infinite doors" is the project's image for reading the
same sedenion with progressively more components active. None of the
physical readings is derived here.

## 9. Zero-divisors: star and inverted star, not a smooth reef

The zero-divisor set of the unit sphere S¹⁵ is not a smooth codimension-1
"reef". It is a union of 84 point-pairs (Listing 1): 42 with "+" and 42 with "−",
each coupling a lower and an upper unit; the framework calls the two families
forward and inverted stars. `ESTABLISHED` (the count and the lower/upper
pairing; the "+ and −" families correspond to the two orientations). Their
organisation into box-kites is [84](84_the_box_kite_debugger.md) and
`ValaQuenta/modules/box_kite`.

Reading (`THEORETICAL`): the arms are pressure voids; the field is pushed into
them under neutral buoyancy; D* = 1 is "the mouth of a channel" and not a wall;
antonymy is a sustained trajectory along an arm, paradox two arms meeting,
metaphor total internal reflection at the critical angle; the whole variety is
the "supermassive inverted galaxy" with its centre near Ω_ζΣ = 0.56714
(neutral buoyancy). The count of 84 channels is exact; mapping them to
word-pair relations is the framework's reading.

## 10. ln(10) as the native metric unit

Native Space is the sedenion ball with prime-hash word addresses, and its
metric is ds = d·log₁₀(p) ([17](17_alpha_omega_d_star.md) §3 for the four d*
faces that make this chart). Every lookup crosses from the decimal rank space
to the natural-log prime address space, and ln 10 is the impedance match between
the two scales. The prime number theorem (density 1/ln p) and Zipf's law
(f ∼ 1/r) are the two sides ([21](21_chladni_zipf_riemann.md) §4).

Decomposition: ln 10 = 2·ln 2 + NS_EXCESS, with 2·ln 2 = ln 4 = 1.3863 (two
doublings, ℂ → ℍ and ℍ → 𝕆, each costing ln 2) and
NS_EXCESS = ln 2.5 = **0.9163**, the residual attributed to the zero-divisor
channels. (Earlier text wrote 0.9170, which does not reproduce.) The split is
arithmetic; the attribution of the residual is interpretation.

Completeness. A computation is *native* iff all four D* values resolve
at once: 0 (ℝ, the vacuum), 0.246 (ℂ, the critical line), 0.5 (ℍ, Dirac
kinetic structure), and 1 (𝕆 → 𝕊, the zero-divisor boundary). These D* values
are the *stratum ladder* of Native Space; note that its 0.246 is the measured
d*_spec and not the Boundary face 0.24631
([17](17_alpha_omega_d_star.md) §3.2).

The Hurwitz remark: log₂ 10 = 3.3219, and the number of normed division
algebras is 4 = ⌈log₂ 10⌉. The earlier wording "four is the largest integer
≤ log₂ 10 …" is wrong (the largest integer ≤ 3.32 is 3: three doublings reach
dimension 8). The coincidence of two small integers is recorded as such; it is
not an explanation of Hurwitz's theorem.

## 11. σ = ½ as a seven-way intersection  (design list)

The page lists seven conditions as holding together at σ = ½: (1) Noether
balance; (2) RH, "all non-trivial zeros on σ = ½"; (3) Wernicke/Broca balance
J_neg = J_pos; (4) neutral buoyancy at the operating depth; (5) the P/NP
boundary (production meets comprehension); (6) EMA convergence of J_ambient
to J*; (7) lossless callosum transfer between the two octonion halves.
Conditions 1, 3, 4, 6 and 7 are properties of the driver's own balance
equations; condition 2 is the Riemann Hypothesis itself, open; condition 5 is
the framework's reading of P versus NP ([105](105_the_millennium_problems_in_ainulindale.md)).
"Independently forced by the algebra" is therefore not established for the
list as a whole.

The Cauchy–Riemann remark (smoothness of a self-adjoint operator on a normed
division algebra, so the Navier–Stokes singularity is a rotation into the
Blue channel) is the argument of [106](106_the_navier_stokes_problem.md) and
carries its status; it is not a proof of regularity.

## 12. Related pages

[13 RH proof path](13_omgwtf_rh_proof.md) · [14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) ·
[15 The Monad](15_the_monad.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md) ·
[84 The box-kite debugger](84_the_box_kite_debugger.md) · [133 Canonical maths](133_canonical_maths.md)
