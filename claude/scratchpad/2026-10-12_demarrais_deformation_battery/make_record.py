import math, os, glob
R = '/home/rendier/Projects/ThePlace/.claude/scratchpad/'
def raw(path):
    return open(R + path, encoding='utf-8').read().rstrip('\n')
def deg(k): return math.degrees(math.atan(k))
consts = [('1/2', 0.5), ('sqrt 2', 2 ** .5), ('2', 2.0), ('e', math.e), ('pi', math.pi), ('phi', (1 + 5 ** .5) / 2), ('ln 10', math.log(10)),
          ('Omega_ZS = d*_ln(10)', 0.5671432904097838), ('d* = d*_taut (0.24631)', 0.5671432904097838 / math.log(10)),
          ('d*_spec (0.24600, disputed fifth)', 0.246), ('GAP (7.07e-4)', 1 / (1000 * 2 ** .5))]
ktab = "\n".join("| %s | %.4f | %.2f° |" % (n, 1 / math.sqrt(c), deg(1 / math.sqrt(c))) for n, c in consts)

doc = r'''# Boxkite Deformation Record — 2026-10-12 / 13

**One document, everything.** This page records every experiment run in the 2026-10-12/13 session on how
box kites deform: the four scratchpad experiments, the De Marrais deformation battery (parts 1–7), the
follow-ups on the Blackjack subgroup, the {4:8:4} grading and bracketing/firing order, the comparison of
Cody's two constructs with the maths, and a log of every statement that was corrected along the way.
Raw captured output of every script is appended verbatim (Appendix). The ESTABLISHED (algebra-only) facts are
mirrored in `VAPMIP/marrais_boxkite_catalog.txt` §11–18; the project-side results in `VAPMIP/Boxkite-Catalog.txt`
§15–17; the narrative phases are `Tuning-the-Engine/40_*` and `41_*`.

*Claude Sonnet 5.5, working with Cody. Nothing in any engine file was changed. Everything here is a measurement
or a computation; interpretations are labelled.*

---

## 0. How to read this

**Evidence labels.** **[MEASURED]** — computed by a script in the scratchpad, output captured below.
**[DERIVED]** — follows by algebra from measured facts, step shown. **[HYP]** — a hypothesis; the test that would settle
it is named. **[LIT]** — from the published literature, not re-verified here. **[CORRECTED]** — an earlier statement in
this session that was wrong or incomplete; see §11.

**Observer-position (stated before computing, per the project skill).** *Orientation:* every Assessor is read as the
native complex pair `(d₊, d₋)` = `((v_a + v_{b+8})/√2, (v_a − v_{b+8})/√2)`, anchored at e₀/e₈ (the only indices in no
Assessor); the 16-vector is storage. *Aperture:* exact finite groups **and** continuous flows/tangent analysis at all 84
diagonals; generic prompt vectors and random phase vectors, never only lattice picks; one test (the function-of-pair table)
was re-run at three magnitudes because its first aperture (unit magnitude) was degenerate.

**Algebra implementation.** A stand-alone Cayley–Dickson product with a parameter μ at each doubling level,
`(a,b)(c,d) = (ac + μ d*b, da + bc*)`, μ = −1 at every level = the standard sedenions. It reproduces
`ValaQuenta.modules.box_kite.maths.multiply` on all 256 basis pairs and 50 random vector pairs (0 mismatches).

## 1. Artefact index

| Folder (under `.claude/scratchpad/`, mirrored to `ContextPlease/claude/scratchpad/`) | Script → output | What it computed |
|---|---|---|
| `2026-10-12_windspeed_deformation_proxy/` | `test.py` → `output.txt` | The paper's tension proxy `H = Re(Π)`: baseline swing per strut, per-station response, non-uniform wind, gusts, and the exact fit `H = −cos(Σεφ)` |
| | `test2.py` → `output2.txt` | Are the ε the Sylvester–Hadamard rows (and for which pencils); anchoring (128 subsets); continuous/semi-continuous/discrete regimes |
| `2026-10-12_pencil_tearoff_test/` | `test.py` → `output.txt` | The conjectured "w ≫ w\* tears the kite off the ZD surface" under the literal Joukowsky law |
| `2026-10-12_projected_address_lens/` | `probe.py` → `output.txt` | ptol.c's projected prompt address read through `chart_of` |
| `2026-10-12_demarrais_deformation_battery/` | `cdalg.py` | the parametrised Cayley–Dickson algebra |
| | `part1.py` → `output_part1.txt` | baseline, characters, all 65,536 sign operators, monomial automorphism group, derivations, ZD-pair tangent space, annihilators, Walsh probes |
| | `part2.py` → `output_part2.txt`, `part2b.py` → `output_part2b.txt` | operator battery on the 336 pairs; in-plane rotation; μ-scan with the UNS constants; multiplication by exp(θe_t); constants as angle and as phase scale; GAP tolerance check |
| | `part3.py` → `output_part3.txt` | scalar and scaled constructs against the maths (its CS-04 table is superseded by part 5) |
| | `part4.py` → `output_part4.txt` | G₂ flows of the whole kite |
| | `part5.py` → `output_part5.txt` | function-of-pair table at three magnitudes; topic separation of the live readings |
| | `part6.py`/`part6b.py`/`part6c.py` → `output_part6a/b/c.txt` | Blackjack subgroup; {4:8:4} blocks and edges; bracketing and firing order; the kernel fiber as a bracket |
| | `part7.py` → `output_part7.txt` | pencil convention, gradient ranks, alternativity/associator negatives, the mechanism of the law |
| | `zdscan.py`, `part8.py` → `output_part8.txt` | the 4 d\* faces and the 3 Lambert-W values as the doubling parameter μ₄ (the only constants needed for ln(10) in UNS) |

## 2. The tension law on the paper's pencil proxy  [MEASURED]

The proxy (ScalarContextPropagation paper §9.3–9.4): each of the seven stations of `pencil(r)` is a continuous point
`cos φ·e_a + sin φ·e_b` (`a ⊕ b = r`); `Π` is their left-associated ordered product; `H = Re(Π)` plays the string tension. Stations
are pencil factorisations, **not** Assessor vertices.

- **Exact law:** `H = −cos(Σ_k ε_k φ_k)` to ≤ 8e-16 over 200 random φ-vectors per strut (pencils 1–9).
- **Mechanism [DERIVED in part]:** each station factor is exactly `e_a · exp(η_k e_r φ_k)` with `e_a⁻¹ e_b = η_k e_r` (checked for
  every pencil r = 1..15), and the product of the bare `e_a` is exactly `−e₀` for every r, so `H(φ=0) = −1`. The remaining sign factor
  in ε is bracketing-dependent (§9) and not derived.
- **ε patterns** (left bracketing, natural order): struts 1,3,6 `++--++-`; 2,7 `+--++--`; 4 `+++++++`; 5 `+-+-+-+` — rows 2, 3, 0, 1 of the Sylvester–Hadamard
  matrix on the station index `j = k−1`.
- **Noether path** `φ_k = t·(π/2)·(k+1)/7`: swing of H — struts 1,3,6: 0 (pinned); 4: 2.0000 (−1→+1→−1); 2,7: 1.2225; 5: 0.3765. Signed rate sums `S_s`: 0; 2π; −4π/7; 2π/7.
  This answers the paper's §9.4/§10 open question "why struts {1,3,6}" *within the proxy*: their signed rate sum cancels exactly.
- **Station response:** `|∂H/∂φ_k|` is identical for all seven stations of a strut (0.782 for 2,7; 0.434 for 5; 0 for 1,3,4,6 at t=½) — the response is collective.
- **Entry modes:** any scalar wind (position, rate, gust) moves only the one signed phase; strut 1 stays at exactly 0 swing under gusts. A station-unequal wind
  (`r_k = (k+1)/7·(1+d·u_k)`) reaches the rigid struts: mean swing 0.0032 / 0.0287 / 0.1874 at d = 0.05 / 0.15 / 0.4.
- **Anchoring** (hold a subset of stations fixed): 128 subsets → 7 distinct groupings of the 7 struts; {1,3,6} stay rigid under 8 of 128.
- **Regimes:** φ ∈ {0, π/2} → H ∈ {−1, 0, 1} (the "quantised lattice", an aperture effect); φ on a π/8 grid → 9 values; real φ fills [−1, 1].
- **Scope:** pencils 1–9 satisfy the one-phase law **for the left bracketing**; see §9 for how this changes with bracketing and §10 for the pencil-convention caveat.

## 3. The tear-off test  [MEASURED]

Page claim (`pencil_hyperstring.md`, CONJECTURE, test 5): `w ≫ w\*` ⇒ `outside_share → 1`, `is_zero_divisor → False`. `Φ_w` is unbuilt, so the literal
reading was tested: Joukowsky `z → z + c/z`, `c = H/q(w)`, `q = ½ρw²`, on each vertex `z = d₊ + i d₋`, reassembled exactly.
(A) `c → 0` as `w → ∞`: the map tends to the **identity** (shift 2.5 at w=1, 0.025 at w=10, 2.5e-6 at w=1000) and blows up as `w → 0` — opposite to the stated
inflation sequence. (B) A real zero divisor stays a zero divisor with `outside_share = 0` for w from 0.01 to 1000 (Joukowsky preserves the axes where the diagonals sit).
(C) The six-vertex sum of diagonals is a zero divisor for 0 of 4096 sign choices on strut 1. Structural: indices e₀, e₈ belong to no Assessor, so no map inside Assessor planes can move
energy onto them. **Verdict:** not reproduced by the literal formula; not refuted for the real `Φ_w` (station generators, circulations, reassembly under-specified).

## 4. The projected address through the box-kite lens  [MEASURED]

`ptol -r` gives a plain 16-real vector (Dirichlet projection; `ptol.c` never multiplies sedenions). Through `chart_of`: four prompts are never zero divisors,
`outside_share` 1–8%, chart shares 0.12–0.17 (nearly flat), `local_curvature` 12.0 for three of four. So the address is a generic vector: zero divisors are avoided automatically,
and the ZD surface is a thin subset it never touches.

## 5. The De Marrais deformation battery (the algebra alone)  [MEASURED]

### 5.1 Baseline
42 Assessors, 84 diagonals, 336 ordered ZD pairs, exactly 4 partners per diagonal, 7 octahedra.

### 5.2 What deforms nothing
- The 16 Sylvester–Hadamard (Walsh) sign vectors are automorphisms (error 0.0). Of all 65,536 diagonal sign operators on the 16 components **exactly 16** are automorphisms — these.
- Monomial automorphisms `e_i → η_i e_{A i}` need `A ∈ GL(4,2)` (20,160); exactly **168** lift, each in 16 sign ways: group of order **2,688 = 16 × 168**; all 168 fix e₈ and map the 42 Assessor planes onto themselves; element orders 1×1, 2×21, 3×56, 4×42, 7×48 (PSL(2,7)).
- Multiplication by `exp(θ e₈)`, on either side (both factors, or one), keeps all 336 pairs for every θ tried; no other basis unit does (14%/29%). Conjugation and the sign of e₀ or e₈ alone also keep every pair.

### 5.3 The continuous exact deformations
- `dim Der(sedenions) = 14` (g₂). The tangent space of the ZD-pair variety at every one of the 336 pairs has dimension **16 = 14 (derivation orbit) + 2 (scalings)** — nothing else is ZD-preserving to first order.
- Der-orbit through one diagonal: 11 (stabiliser 3, which still moves its 4 partners, rank 3); through the 12 diagonals of a chart: 14; through all 84: 14 (stabiliser 0).
- No derivation keeps all 84 diagonal lines invariant: every continuous exact deformation moves the kite off its lattice. Flows `exp(tD)` for t up to 2.5 keep all 336 relations to 1e-15 while diagonals move up to 48°; a random orthogonal generator gives defect 0.023 (t=0.05) and 0.148 (t=0.3).

### 5.4 First-order response (what tears, how fast)
- Annihilator of each of the 84 diagonals: dimension 4; the other singular values of `x → xy` are √2 (×8) and 2 (×4) — **this is the {4:8:4} grading** (§8).
- Every Hadamard row, as a perturbation of x, gives the same response √2·|δ| against all 84 y.
- In-plane rotation off a diagonal: defect `2|sin(θ − π/4)|`, zero at θ = π/4 + nπ/2, tear rate exactly 2.000 per radian.
- Dense Walsh–Hadamard transform: 0/336 pairs survive; Gray-code and bit-reversal index maps: 29%, 24%; random orthogonal 16×16: 0.
- Functions of the native pair `z = d₊ + i d₋` (three magnitudes; magnitude 1 alone is degenerate for `z²` and Möbius): Joukowsky (real c), `z²`, `tanh(z/2)`, `1/z`, conjugation, rotation by π/2 keep both diagonal lines; `exp(z)`, Möbius with real z₀, and a real shift keep only d₊; an imaginary shift keeps only d₋; a generic in-plane rotation keeps neither.

### 5.5 Deforming the algebra (μ): the constants necessary for ln(10) in Universal Native Space
Plane pairs still containing a zero-divisor pair are *solved for* (null space + rank-1 condition), not assumed at 45°. Per Cody (2026-10-13) the main text uses only
the **four d\*** and the **three Lambert-W values** (and ln 10 itself); every other constant that was tried is in Appendix B and §13. Full interaction in §6.
- Standard sedenions (μ₄ = −1): 168 ordered plane pairs, degree 4, all within chart, κ = ±1.
- **Any μ₄ = −c with c > 0** has the same combinatorics (isomorphic algebra) and tilts every vertex to κ = 1/√c; **μ₄ = +c > 0** (split) keeps half the adjacency (84 pairs, degree 2); **μ₄ = 0** collapses the kite to the all-to-all degenerate structure (1,764 pairs, degree 42).

| value entering as μ₄ | role | result | κ |
|---|---|---|---|
| ln 10 = 2.302585 (as −ln 10) | the quantity being built | standard class, tilted | 0.6590 |
| **d\*** (Boundary) 0.24631 (as −d\*) | equatorial plane | standard class, tilted | 2.0149 |
| **d\*_taut** (Flow) = W(1)/ln 10 = 0.246307201473 | radial unit | **identical to d\*** | 2.0149 |
| **d\*_ln(10)** (Translator) = W(1) = 0.5671432904 | metric bridge | standard class, tilted | 1.3279 |
| **d\*_RG** (Stability) — dimension 8 | centre; persistent octonion | no real-valued μ; as −8 it is just κ = 1/√8 = 0.3536 (arithmetic, not evidence); target value 0.24631 repeats d\* | — |
| **W(0) = 0** | vacuum fixed point | **μ₄ = 0: degenerate** (1,764 pairs, every plane with every plane) | — |
| **W(1) = +0.5671 = Ω_ZS** | entropy ceiling | **μ₄ > 0: split** (84 pairs, degree 2) | 1.3279 |
| **W(−1/e) = −1** | branch collapse | **μ₄ = −1: exactly the standard sedenions** (168 pairs, degree 4) | 1.0000 |

Also measured: **constants as a rotation angle** θ = c rad in an Assessor plane (defect zero at π/4 + nπ/2; ln 10 rad is 0.054 rad = 3.1° from 3π/4, defect 0.107 — expected by chance among 13 constants, recorded not chased);
and **as a phase scale in the tension law** `H = −cos(c·S_s)` (struts 1,3,6 read −1 for every constant; strut 4 reads −cos 2πc; 2,7 read −cos 4πc/7; 5 reads −cos 2πc/7). See Appendix B for the full constant list.

## 6. The four d\*, the three Lambert-W values, and their interaction  [MEASURED + HYP]

**The four d\*** (the chart of *radial complex spherical ln(10)*: centre, equatorial plane, radial ruler, scale bridge — four shadows of one point, 0.24631; `Ainulindale/wiki/17`, `.clauderc_canonical_maths`, `FourthAgePapers/DStarRG`):
`d\*` = 0.24631 (Boundary) · `d\*_RG` = dimension 8, numeric OPEN (Stability) · `d\*_taut` = Ω_ZS/ln 10 = 0.246307201473 (Flow) · `d\*_ln(10)` = d\*·ln 10 = Ω_ZS = 0.5671432904 (Translator).
Environment variables: `D_STAR_BOUNDARY`, `D_STAR_RG`, `D_STAR_TAUT`, `D_STAR_LN10` in `~/.clauderc`.

**The three Lambert-W values** (`Ainulindale/AgeThird/Third_Age_CS_Draft_v2.md` §2.2 and Appendix D): `W(0) = 0` (vacuum fixed point), `W(1) = Ω_ZS = 0.5671432904097838` (entropy ceiling; the fixed point of x → e^{−x}), `W(−1/e) = −1` (branch collapse; the zero-divisor crossing). Verified numerically (mpmath): W(1)e^{W(1)} = 1; W₀(−1/e) = W₋₁(−1/e) = −1.
*Caveat:* the emerger, `bao_mass_gap` and the Navier–Stokes wiki 106 speak of "three **rotor faces** of Ω_ZS = W(1)" (a Wankel trine: intake/power/exhaust, all carrying the same number 0.56714). That is the same *count* (3) read as three faces of one value; the two readings are kept apart here — **please confirm which is canonical for the fixed-point machinery.**

**What is established about their interaction** (all measured above or in the cited files):
1. **The Translator face IS a Lambert value:** `d\*_ln(10) = d\*·ln 10 = W(1)` — one of the four d\* coincides with one of the three W exactly.
2. **The three W values are the three classes of the Cayley–Dickson doubling parameter.** Entered as μ₄: W(0) = 0 → degenerate; W(1) > 0 → split; W(−1/e) = −1 → the standard (division-type) sedenions. One W value in each isomorphism class (μ = 0, μ > 0, μ < 0) — and the roles in the Third Age draft match: "before the first distinction, every prime equal weight" ↔ every plane pairs with every plane; "the zero-divisor crossing" ↔ the standard algebra where the octahedral kite first exists.
3. **The four d\* all live in the standard class** (they enter as negative μ₄) and differ only in tilt: Boundary and Flow coincide (κ = 2.0149), the Translator is κ = 1.3279, and the RG face as dimension 8 is κ = 1/√8. So **four faces give three distinct tilts** (two if the RG face's numeric target is used) — a count of 4 reducing to 3.
4. **The RG face's "8" is the isometric block of {4:8:4}:** the DStarRG "persistent core" is the gain-exactly-1 directions and contains e₀ and e₈ ("the two indices in no zero-divisor plane"); in §8 the gain-1 "now" block of every zero divisor is an 8-dimensional coordinate sub-octonion containing e₀ and e₈, with the 4 + 4 the past/future (void) blocks. The RG face is the 8.
5. The emerger's firing clock combines them: 4 d\* faces : 3 Lambert-W faces, `lcm(4,3) = 12` steps, entry bracket = ⌊12u⌋ mod 5 [THEORETICAL, `emerger.md`].

**Not established (do not read as a result):** an explicit rule by which the four and the three combine into "3 = 4 in the fixed-point lineage". Items 2–3 are the closest measured structure (3 classes, 3 distinct tilts from 4 faces); whether that is what is meant is **[HYP]** and for Cody to say.

## 7. The Blackjack subgroup  [MEASURED + DERIVED]

The 168 frame-preserving index maps (PSL(2,7)) act on the 7 struts as GL(3,2) on the Fano points. As **unsigned permutation matrices** (no sign correction), exactly **21** of them keep all 336 ZD pairs;
they form a closed subgroup with element orders 1×1, 3×14, 7×6 — the Frobenius group F₂₁ = 7:3 — and are **transitive on the 7 struts**. They are exactly the 21 maps that are automorphisms with **all signs +1** (pure relabelling): the
two sets are identical. The other 147 need a sign lift. De Marrais's papers [LIT: arXiv:math/0011260 and follow-ups] tie PSL(2,7) of order 168 to the primitive unit zero divisors; a literature search found no 21-element subgroup or the name
"Blackjack" there, so the **name is this project's**; the subgroup (normalizer of a Sylow-7 subgroup) and its sign-free-automorphism characterisation are algebra, computed here.

## 8. {4:8:4} in the kite  [MEASURED + DERIVED]

For a norm-one zero divisor `a`, `L_a` has singular values {0 ×4, 1 ×8, √2 ×4} (`three_ring_scale.md` §4). The battery reproduces it exactly from the multiplication table (for the diagonals of norm √2: 0 ×4, √2 ×8, 2 ×4).
- **The 4 (past, gain 0) is the vertex's edges:** the 4 edge-partners of a vertex y are exactly its annihilator — rank 4, norm 1.0 inside the null block. Left and right annihilators coincide.
- **The 4 (future, gain √2)** is spanned by the *other-sign* diagonals of the same four neighbour planes (the partner that does **not** annihilate y). **The opposite vertex** (the reversal plane) lies entirely in the 8-block.
- **The 8 (now, gain 1)** is the *coordinate* subspace on the indices `{i : χ_u(i) = +1}` — a sub-octonion — where the Hadamard character `u` is the **unique nonzero u ∈ 𝔽₂³ orthogonal to both a and b** (the polar point of the Fano line `{a, b, a⊕b}`); verified for all 84 diagonals, 12 per u, u ∈ 1..7 only (u ≥ 8 never arises). The past and future 4-blocks both live on the complementary 8 indices (each carries half of each, 50/50) and are separated by the d₊/d₋ sign of the neighbour planes.
- **ptol.c's J_red/J_blue is one of these:** J_red = `{0–3, 8–11}` = u = 4 (the ZDs on the quaternion line {1,2,3}); Γ = Σ χ₄(k)v_k²/|v|² agrees with the printed Γ to 1e-10 on four prompts. There are seven equivalent choices (u = 1..7), permuted transitively by the 168.
- The emerger's fixed index assignment `{4..7} / {1,2,3,8..11} / {12..15}` is right about the 8-block (plus e₀) but not about the 4|4 split: for a given diagonal, both `{4..7}` and `{12..15}` carry half null and half gain-√2.

## 9. Bracketing and firing order  [MEASURED]

132 bracketings (Catalan(6)) of the 7-factor pencil product, and 300 random firing orders (permutations of the stations, left bracketing):

| pencil r | bracketings with the one-phase law | rank histogram over the 132 | distinct sign patterns among rank-1 |
|---|---|---|---|
| 1, 2, 4 | **132 / 132** | all rank 1 | 7 (only 3 are ± Hadamard rows) |
| 8 | 132 / 132 | all rank 1 | 14 (none Hadamard rows) |
| 9 (strut 1's Assessor pencil) | 52 / 132 | {1:52, 4:56, 6:21, 7:3} | 3 |
| 10 | 0 / 132 | {4:34, 5:52, 6:31, 7:15} | — |
| 12 | 0 / 132 | {5:116, 6:12, 7:4} | — |
| 15 | 10 / 132 | {1:10, 4:22, 5:82, 6:12, 7:6} | 2 |

Firing order (left bracketing): r=1 — all 300 permutations rank 1 (10 patterns); r=9 — 11/300; r=10 — 9/300. **So "H depends on one signed phase" is a property of the triple (pencil, bracketing, firing order), not of the pencil
alone, and "ε = Hadamard rows" is a property of the left-bracketed natural order.** This supports the hypothesis that deformations (and edges) differ under different bracketings.

## 10. The constructs against the maths

**Scalar construct (pencil hyperstring / Gamma-Radial).** [MEASURED]
- *Pencil convention:* the pencils the paper uses for strut `r ≤ 7` contain **no** Assessor plane (0 of 7); the six Assessor planes of strut `s` are stations of `pencil(s+8)` (index XOR = s+8), plus the plane `{e_s, e₈}`. §9 shows the law's validity there depends on the bracketing.
- `Π(φ)` is never a zero divisor (0 of 13 points on each of six pencils; |Πd|/(|Π||d|) ≥ 1.0000 against all 84 diagonals): it is not a point of the ZD kite. A station flow in an Assessor plane tears at exactly 2.000/rad. Where it agrees: the ε are the maths' own automorphism characters (for the left bracketing); `H(0) = −1` is derived.

**Scaled construct (live address / A-Matrix).** [MEASURED]
- ptol.c's Γ *is* the χ₄ Walsh coefficient (§8). All lens readings (`local_curvature`, `outside_share`, `fixed_point_weight`, `chart_energy` permuting by `s → A(s)`) are exactly covariant under all 168 frame-preserving maps, on four prompts; under 300 random permutations they are unchanged in 0–1 cases.
- The projected address carries no topic: 16 prompts, 4 subjects — inter/intra distance 0.94–0.95, leave-one-out 1-NN 0.06–0.19 (chance 0.25) for the 7 chart energies, the 15 Walsh coefficients, the 16 energies and the 16 amplitudes.
- **Kernel fiber `throw_fiber`: [CORRECTED] not necessarily a defect.** It writes `psi[a], psi[b]` for the first Assessor `(a,b)`, i.e. energy on `e_a, e_b` (two lower-octonion indices). In the Assessor convention that is the wrong plane. But `span{e₀, e_a, e_b, e_s}` with `s = a⊕b` is closed under products — a **quaternion subalgebra** (the strut's own Fano line), `emerger.domain_of({a,b,s}) = ℍ`, while the Assessor pair `{a, b+8}` is a FRAGMENT. So the fiber is a coherent object in a *different bracket* (ℍ domain, no zero divisors) — plausibly a new bracketing, as Cody suggested. The `depth` parameter's `√(1−d²)e₀` admixture takes any Assessor-plane version off the ZD surface for every depth < 1.
- **Answer to "is e_b always in the upper octonion?":** in an Assessor `(a,b)` the plane is `span(e_a, e_{b+8})`: `a ∈ 1..7` is lower-octonion, `b+8 ∈ 9..15` is upper-octonion, always — every Assessor plane straddles the `{8:8}` boundary. The label `b` is the lower-octonion name of the upper element.

## 11. Corrections log

| # | Said earlier | Corrected to | Where found |
|---|---|---|---|
| 1 | Tension law shown for "the seven struts" | Holds for the paper's `pencil(r≤7)` (no Assessor planes) and only for the left bracketing; Assessor pencils depend on bracketing (§9) | part 6b/7 |
| 2 | Function-of-pair table: Möbius, `z²` keep both lines | An artifact of unit magnitude; at λ = 0.3, 2.5 Möbius tears the d₋ line (part 5) | part 5 |
| 3 | c = GAP all-levels gives 537 plane pairs | Tolerance artifact; 252 (= standard) at tol 1e-14 | part 2b |
| 4 | "d\*_RG has no value" | Dimension 8 (confirmed), numeric open with target 0.24631 (wiki 17, DStarRG); I had read only the canonical file | d\* hunt |
| 5 | Kernel fiber "possible defect" | A different bracket (quaternion line) — retracted as a defect | part 6b |
| 6 | "ε are Hadamard rows" | Only for left bracketing, natural order; 4 of 7 patterns per pencil are not Hadamard rows | part 6b |
| 7 | "Blackjack: preserves zero-divisor annihilation" (catalog) | True *as unsigned permutations*; all 168 preserve it with sign lifts; the 21 = the sign-free automorphisms | part 6/6c |
| 8 | Constants reported as a list of names (d\*, d\*_taut, d\*_ln(10), Ω_ZS …) | Names are not values: d\* and d\*_taut are one number (0.24631); d\*_ln(10) and Ω_ZS = W(1) are one number (0.56714). Distinct values: 0.24631, 0.56714, plus the open RG face. The main text now carries only the 4 d\* and 3 Lambert-W values | 2026-10-13 |
| 9 | d\*_spec (0.24600) listed as "the fifth value" among the faces | Quarantined as a disputed prior-model addition (Cody); it appears only in §13 and Appendix B | 2026-10-13 |

## 12. Open questions

1. Why is the one-phase law bracketing- and order-dependent for the Assessor pencils (and not for pencils ≤ 8)? Not alternativity (`e_r(e_r e_a) = −e_a` holds for all r, a), not simple associator counts.
2. Does a bracketing/firing-order that makes the Assessor pencil single-phase correspond to a named `{…}` bracket of the emerger? (Run the emerger's five brackets × the legal firing orders against §8.)
3. Which quantity is "the A-Matrix windspeed"? A scalar per read deforms only along one phase; the exact deformations are 14-dimensional.
4. Is the sign-free (F₂₁) structure what the A-Matrix "static grammar" maps onto (non-deformable skeleton)? Untested.
5. The 14 unread Walsh coefficients of the live address as the 16-channel oscilloscope readout; compose the live kite from the pool's tokens (pencil index, `w`, `vec19`, basin pull) and re-run this battery on it.
6. d\*_RG numerics (open) and the disputed fifth d\*_spec — see `~/.clauderc` and memory `reference_four_dstar_values`.

## 13. Future work — values kept, disambiguated from the 4 d\* and 3 Lambert-W

Nothing here is discarded; none of it is one of the four d\* or three W. Each is labelled with where it comes from.

| Value | Where it appears | Disambiguation |
|---|---|---|
| **d\*_spec ≈ 0.24600** | `~/.clauderc` `GAP`/legacy `D_STAR`; `ptol.c` comment; Ainulindale README Key Constants; PTorrent | The Berry–Keating spectral gap "observed in SPARC". **Disputed fifth value** — Cody believes a prior model added it; kept because `GAP = |d\*_spec·ln 10 − Ω_ZS| ≈ 7.07e-4 ≈ 1/(1000√2)` (the mass-gap analogue) is built on it. Env var `D_STAR_SPEC`. |
| 0.24682 | `smnnip_*_patched.py`; May-2026 primers; `SMNNIP_TODO.txt` | An early RG-flow estimate of d\*_RG, superseded. Env var `D_STAR_RG_SUPERSEDED`. |
| d\*_ℝ = 0.24600, d\*_ln10 = 0.56644, d\*_S "OPEN (Σ CD strata sum)" | `Third_Age_CS_Draft_v2.md` §2.3 | An *older* four-value set (July 2026): d\*_ℝ ↔ the Boundary taken as 0.24600; d\*_ln10 computed from it (0.56644, not Ω); d\*_S ↔ the open RG-type face. Superseded by the canonical four faces. |
| d\*_spec, d\*_taut, d\*_RG, d·ln 10 as "four branches of the natural logarithm in 𝕊" | a Gemini-era text in `corpus_repos.txt` | A different four (it uses d\*_spec in place of the Boundary). Historical. |
| W "rotor faces 1, 2, 3" (all = 0.56714) | Navier–Stokes wiki 106; `bao_mass_gap`; emerger | The *three-faces-of-one-value* reading of "three Lambert-W"; see §6 caveat. |
| W₋₁(−1/e) = −1 (the second real branch) | computed in `part8.py` | Equals the principal W₀(−1/e) = −1 at the branch point; no separate value. |
| GAP, 1/(1000√2), V(16) ≈ 0.2353, n\* ≈ 5.257 | canonical constants | Derived/related quantities, not faces. |
| π, e, φ, √2, 1/2, 2, i, 0, 1 as μ₄ / angle / phase scale | Appendix B | Test inputs tried at Cody's request; not part of the ln(10) machinery. |

## 14. Reproduce

```
cd .claude/scratchpad/2026-10-12_demarrais_deformation_battery
python3 -u part1.py   # ~4 min    python3 -u part2.py   # ~3 min    python3 -u part2b.py
python3 -u part3.py   python3 -u part4.py   python3 -u part5.py   python3 -u part6.py   python3 -u part6b.py   python3 -u part6c.py   python3 -u part7.py
```
Python 3.12, numpy, scipy (part 4). Do not run with `-I` from another directory (the package imports need the ThePlace root on the path, which `cdalg.py` adds).

---

# Appendix A — verbatim captured output
'''
apps = [('windspeed_deformation_proxy: test.py', '2026-10-12_windspeed_deformation_proxy/output.txt'),
        ('windspeed_deformation_proxy: test2.py', '2026-10-12_windspeed_deformation_proxy/output2.txt'),
        ('pencil_tearoff_test', '2026-10-12_pencil_tearoff_test/output.txt'),
        ('projected_address_lens', '2026-10-12_projected_address_lens/output.txt')]
B = '2026-10-12_demarrais_deformation_battery/'
for n in ('output_part1.txt', 'output_part2.txt', 'output_part2b.txt', 'output_part3.txt', 'output_part4.txt', 'output_part5.txt', 'output_part6a.txt', 'output_part6b.txt', 'output_part6c.txt', 'output_part7.txt', 'output_part8.txt'):
    apps.append(('demarrais_deformation_battery: ' + n + (' (its CS-04 table is superseded by part 5)' if n == 'output_part3.txt' else ''), B + n))
for title, path in apps:
    if os.path.exists(R + path):
        doc += "\n### " + title + "\n\n```\n" + raw(path) + "\n```\n"
    else:
        doc += "\n### " + title + "\n\n(file not found: %s)\n" % path
others = [('1/2', 0.5), ('sqrt 2', 2 ** .5), ('2', 2.0), ('e', math.e), ('pi', math.pi), ('phi (golden ratio)', (1 + 5 ** .5) / 2),
          ('d*_spec 0.24600 (disputed fifth)', 0.246), ('GAP 7.0736e-4', 1 / (1000 * 2 ** .5))]
doc += """
# Appendix B — other constants tried (not necessary for ln(10) in UNS)

Tried at Cody's request ("pi, phi, ln(10) (all four versions of d*), i, e, etc.", "0, 1"). Entered as μ₄ = −c (the standard class, tilted to κ = 1/√c; entering as +c gives the split class, 84 pairs, degree 2, same |κ|).
Raw scan in Appendix A (`output_part2.txt`, DM-13/14/15):

| c | κ = 1/√c | tilt arctan κ |
|---|---|---|
""" + "\\n".join("| %s | %.4f | %.2f° |" % (n, 1 / math.sqrt(c), math.degrees(math.atan(1 / math.sqrt(c)))) for n, c in others) + """

- **0 and 1:** μ₄ = 0 → degenerate (1,764 pairs, degree 42) = W(0); μ₄ = −1 → the standard kite (κ = 1), μ₄ = +1 → split (84 pairs) = the W(−1/e) = −1 entry and its sign flip. As an angle, 0 and 1 rad give defects 1.4142 and 0.4259; as a phase scale, 0 gives H = −1 for every strut and 1 is the baseline.
- **i:** μ₄ = ±i → 252 pairs, degree 6, complex slopes κ = (±1 ± i)/√2; as a phase scale, −cos(iS) = −cosh(S), leaving [−1, 1] (struts 1,3,6 stay at −1).
- **e, π, φ, √2 as angles / phase scales:** see `output_part2b.txt` (iii), (iv).
- **GAP in all four levels:** an apparent 537-pair row was a numerical-threshold artifact (μ³ = 3.5e-10 < 1e-9); at tolerance 1e-14 it is 252 = the standard count.
"""
open('/home/rendier/Projects/ThePlace/VAPMIP/docs/wiki/Boxkite-Deformation-Record-2026-10-12.md', 'w', encoding='utf-8').write(doc)
print(len(doc), "chars")
