# 84 — The Box-Kite Debugger: the Geometry, Made Watchable

| | |
|---|---|
| Scope | the finite object behind the sedenion zero-divisors (PSL(2,7), order 168) against Moreno's continuous G₂; the 42 Assessors and seven box-kites; their octahedral shape and chart-level dispersion relation; ∅_RB and e₀ as outside the geometry; the associator as curvature; the finding that the charts do not touch by adjacency, and do by skeleton; the monad address census |
| Origin | 2026-08-05, built by Claude Opus 5, directed by the author: "how do we 'debug' the geometries / how do we watch the geometries interact" |
| Predecessors | [83](83_the_archimedes_screw.md), [82](82_l_io_photon_path.md), [80](80_aphasia_zd_reframe_memory.md) |
| Code | `ValaQuenta/modules/box_kite/` (`maths.py`: `verify_counts`, `box_kites`, `chart_spectrum`, `glued_graph`, `glued_spectrum`, `associator_census`, `e0_is_outside`, `skeleton_counts`); `ValaQuenta/wiki/box_kite.md`; notebook `15_box_kite.ipynb`; `ValaQuenta/zero_lattice.py` |
| Literature | E. Moreno, *The zero divisors of the Cayley–Dickson algebras over the real numbers* (preprint 1997; *Bol. Soc. Mat. Mexicana* 1998); R. de Marrais, *The 42 Assessors and the Box-Kites They Fly On* (2000) |
| Confidence | the counts, the octahedra, the spectrum and the census: ESTABLISHED (re-run 2026-11-13) · PSL(2,7) acting as the transition map between charts: `CONJECTURE` · the global dispersion relation: OPEN |
| Last verified | 2026-11-13: Listing 1 executed with the installed engine; its output is quoted below. The monad address census of §7c needs `VAPMIP/monad_sedenion_addresses.pkl` and was not re-run |

## 1. Where the object is, and is not  `INTERPRETATION` over a literature fact

Moreno showed that the norm-one zero-divisors of the sedenions are homeomorphic to the
exceptional Lie group G₂ (his preprint is 1997; the journal version 1998; this wiki previously
carried both dates). de Marrais's paper is a response: Moreno's result is a "blow-up", and "the
blow-ups in the history of number theory have all entailed the loss of something"; his aim is to expose
structure the A-D-E taxonomy "keeps hidden". The page's comparison:

```
G₂         continuous, dim 14, Aut(𝕆)        Moreno's blow-up: the shadow
PSL(2,7)   finite, order 168, Aut(Fano)      the exact object
```

the finite group preserving the Fano labelling has order 1344 = 8 · 168 and PSL(2,7) is its quotient (enumerated 2026-11-27, `ValaQuenta` `labelled_automorphisms`; it acts transitively on the 168 unit zero-divisor points, stabiliser of order 8; ledger X-68); G₂ forgets *which line is which*. The
framework's constant ZD_COMPOSITE = 168 is |PSL(2,7)|, and its diagrams were Fano-based throughout. That PSL(2,7) is
"the exact object" (and G₂ the forgetful one) is the page's reading of de Marrais; the group orders and the
subgroup relation are standard.

## 2. Everything derives  `ESTABLISHED`

The module builds the Cayley–Dickson table from the reals and computes:

```
ASSESSOR   a plane span(e_a, e_{b+8}), a, b ∈ 1..7, whose diagonals e_a ± e_{b+8} zero-divide; a = b never works
42         = 49 − 7 aligned planes
84         = 42 × 2 diagonals
168        = 42 × 4 signed unit points = |PSL(2,7)|
336        ordered annihilating pairs = 84 × 4 (each diagonal annihilates exactly 4 others)
STRUT      s = a XOR b ∈ 1..7 indexes the box-kite;   7 × 6 = 42: seven box-kites of six Assessors
```

Agreement with de Marrais and with ValaQuenta's constants is a check, not an input. These agree with the
independent count of [71](71_zd_statement_machine.md) (84 zero-divisors, 42 index pairs, 168 unordered
zero-product pairs, 336 ordered). Cross-check: de Marrais's Box-Kite I, (3,10), (2,11), (5,12), (4,13), (7,14), (6,15),
is this module's strut 1 (the engine lists it as the assessor labels (2,3), (3,2), (4,5), (5,4), (6,7), (7,6), where the
second label b stands for e_{b+8}: (e₂,e₁₁), (e₃,e₁₀), (e₄,e₁₃), (e₅,e₁₂), (e₆,e₁₅), (e₇,e₁₄)).

**Listing 1 — the counts, the charts, the gluing and e₀** (needs the installed ValaQuenta package; runs cold)

```python
import importlib
bk = importlib.import_module('ValaQuenta.modules.box_kite.maths')
vc = bk.verify_counts(); print({k: vc[k] for k in ('assessors', 'diagonals', 'unit_points', 'psl27_order', 'ordered_zd_pairs', 'kills_per_diagonal')})
kites = bk.box_kites(); print('strut 1 assessors:', sorted(kites[1]), '; assessors per strut:', {s: len(v) for s, v in kites.items()})
g = bk.glued_graph(); print({k: g[k] for k in ('n_vertices', 'n_edges', 'cross_strut_edges', 'within_strut_edges')})
print('associator census:', bk.associator_census())
print('chart spectrum (Laplacian), strut 1:', [round(x, 6) for x in bk.chart_spectrum(1)], '; zero modes in the glued spectrum:', sum(abs(x) < 1e-9 for x in bk.glued_spectrum()))
print('e0 outside:', bk.e0_is_outside())
```

```
{'assessors': 42, 'diagonals': 84, 'unit_points': 168, 'psl27_order': 168, 'ordered_zd_pairs': 336, 'kills_per_diagonal': 4}
strut 1 assessors: [(2, 3), (3, 2), (4, 5), (5, 4), (6, 7), (7, 6)] ; assessors per strut: {1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6}
{'n_vertices': 42, 'n_edges': 84, 'cross_strut_edges': 0, 'within_strut_edges': 84}
associator census: {'total': 4096, 'nonzero': 1848, 'zero': 2248}
chart spectrum (Laplacian), strut 1: [0.0, 4.0, 4.0, 4.0, 6.0, 6.0] ; zero modes in the glued spectrum: 7
e0 outside: {'e0_is_a_pg32_point': False, 'e0_in_any_assessor': False, 'e0_associator_always_vanishes': True, 'e0_is_outside_the_geometry': True}
```

## 3. The shape is an octahedron  `ESTABLISHED`

For every strut the six Assessors form a 4-regular graph on six vertices with exactly three non-edges, and the
non-edges are the reversal pairs (a, b) ↔ (b, a): that is K₂,₂,₂, the octahedron, verified from actual vanishing
products for all seven charts. So the geometries are **seven octahedra**, partitioning sedenion space, 42 vertices in
all. This supports the author's method ("an ultra hypercomplex laplacian topographic mercator style projection …
basically just local flatness") as an atlas of charts, and the atlas has exactly seven charts; de Marrais wrote it
down in 2000.

## 4. The dispersion relation at chart level  `ESTABLISHED`

```
adjacency   4, 0, 0, 0, −2, −2         (the octahedron's adjacency spectrum)
Laplacian   0, 4, 4, 4, 6, 6           ω²(k) on one box-kite   (Listing 1)
```

One zero mode, a threefold mode at 4, a twofold mode at 6.

## 5. ∅_RB is not the geometry  `ESTABLISHED`

The author's question, whether 0_RB, "the geometries' boundary generator", is not itself the geometries, is
answered by computation (`e0_is_outside`, Listing 1): e₀ is not a point of PG(3,2) (the skeleton is the fifteen pure
imaginaries); e₀ lies in no Assessor; e₀ is a vertex of no box-kite; and [e₀, ·, ·] = 0 always, the identity being
central. It generates the boundary and does not live on it, as d generates ∂ without being a manifold or a
Hamiltonian generates a flow without being the phase space. The zero mode of each chart is e₀'s signature:
the mode that exists everywhere and propagates nowhere. (Notation scope: Ĥ_RB in the mathematics, ∅_RB/0_RB in the Monad and
VAPMIP spaces, [127](127_names_of_the_null_operator.md).)

## 6. The curvature is the associator  `ESTABLISHED`

[a, b, c] = (ab)c − a(bc) is the curvature and [a, b] = ab − ba the torsion. Of the 4096 basis triples 1848 curve
(Listing 1: nonzero 1848, zero 2248). `associator_field(s)` paints the defect on a box-kite's vertices and edges: where it is large the
geometry is bending; this is the debug view.

## 7. The finding: the charts do not touch by adjacency

Assembling all 42 Assessors into one graph gives 84 edges and **zero cross-strut edges** (Listing 1): the seven
box-kites are mutually disconnected under zero-divisor adjacency, the glued Laplacian has seven zero modes, and 84
is both ZD_PAIRS and the atlas edge count (42 vertices of degree 4). A disturbance cannot propagate between charts along
ZD adjacency, so either the medium is seven separate ponds with no global dispersion relation, or the connection is the
**PSL(2,7) action permuting the struts**: the transition maps are group elements and not edges. The second is
where the page points ("adjacency was always the wrong place to expect the gluing"), and it is a `CONJECTURE`.

### 7b. Do the charts touch? Yes, in the skeleton  (v0.2)

The author's expectation: "they are all from the fixed point anyway". Two structures on one object:

| structure | relation | result |
|---|---|---|
| adjacency | zero-divisor products | 7 components, 7 zero modes |
| skeleton | shared basis indices | every usable index lies in 6 of 7 charts |

For strut s an Assessor is (a, (a XOR s) + 8), valid when a ≠ s, so index a lies in every chart except s = a (membership 6 of 7 for each index 1…7, by that rule); every pair of charts shares 5 lower and 5 upper skeleton indices, 10 points in all. Exactly two basis
elements lie in no Assessor: **e₀** (the identity, ∅_RB, the fixed point) and **e₈** (the Cayley–Dickson doubling
generator). Each chart has one zero mode, the constant function: seven copies of one object. Identifying them connects
the atlas, and that identification happens at e₀ and nowhere else. This is the precise sense in which ∅_RB points to
fixed-point space, where the boundary generator and the geometry's own mode are the same vector. Functions:
`index_chart_membership`, `skeleton_overlap`, `fixed_point_gluing`.

### 7c. The chart of addresses

`chart_of(v)` places a monad hyperindex (`VAPMIP/monad_sedenion_addresses.pkl`, `book[name]["sedenion"]`) in the atlas:
norm, peak dimension, fixed-point weight, e₀/e₈/lower/upper energy split, per-chart energy, nearest Assessor,
diagonals, local curvature, `is_zero_divisor`, outside share. `address_census` runs it over a corpus, descriptive
only. Recorded census over the monad book (3,288 entries; **not re-run in this pass**): all 42 Assessors occupied; mean
fixed-point weight 0.6435 (min 0.0583, max 1.0000); mean outside share e₀ + e₈ 0.6537; peak_dim = 0 for 2,751 of 3,288
(84 %); dominant chart strut 2 at 30.1 % down to strut 7 at 2.2 %; mean local curvature 8.37. So about two thirds of the average
address's energy lies outside the zero-divisor geometry. This localises Phase 23's finding (the monad projections
carry about 85 % common mode with 2–3 % content) to e₀ + e₈: the part of an address outside the geometry is the part
carrying no discriminating signal. Descriptive; not a result about translation.

## 8. Honest boundaries

- The 84 edges are within-strut only. `glued_graph()` / `glued_spectrum()` are an instrument reading, not a derivation of the global medium.
- PSL(2,7) as the transition map is a conjecture, named as the next step.
- `is_assessor()` costs O(4·49) products per call, fine at the fixed 16-dimensional scale; no claim is made for T₃₂ and above.

## Summary

The object is PSL(2,7), order 168 (G₂ is Moreno's continuous blow-up that forgets the labelling). The geometry is seven
octahedral charts on 42 Assessors, every count derived from the table and agreeing with de Marrais and with the framework's
constants. Each chart's Laplacian spectrum is {0, 4, 4, 4, 6, 6}, with the zero mode as e₀'s signature; the associator is
the curvature. The charts do not touch by adjacency and do touch in the skeleton, at e₀. The gluing is a group-action
problem, and that is the open item.

## Related pages

[71 the zero-divisor statement machine](71_zd_statement_machine.md) · [83 the Archimedes screw](83_the_archimedes_screw.md) ·
[57 the boundary ascending](57_boundary_ascending.md) · [19 the Cayley–Dickson tower](19_cayley_dickson_tower.md) · [25 the sedenion manual](25_sedenion_manual.md)

---

**Interactive pages (2026-11-27).** `ValaQuenta/gallery/box_kite/`: one octahedron, the 42 assessors as seven octahedra, the Fano plane and PG(3,2), the associator map, the group 1344 = 8 × 168 (non-split extension, computed). See `ValaQuenta/wiki/box_kite.md` and ledger X-69.
