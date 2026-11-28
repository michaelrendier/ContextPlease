# 97 — Units as the Equation Index

| | |
|---|---|
| Scope | a unit as a point in the 7-axis SI exponent lattice; the lineage of a named unit (Tesla) traced and recombined; `EQUATION_INDEX` as the unit-signature analogue of the WordNet context vector; units as a geometry that does no work |
| Written | 2026-08-25, continuing [95](95_the_scale.md) and [96](96_the_riemann_fermat_horizon.md) |
| Code | `GenerationalLineage/engine/lineage.py` PW16 (the engine named SedenionFactoralRelativity when the page was written); the independent port `ValaQuenta/modules/units/` (`SI_BASE`, `LINEAGE_TABLE`, `EQUATION_INDEX`, `unit_mul/div/pow`, `unit_lineage_decompose`, `verify_lineage_table`, `equation_index_lookup`); the original design `PtolemyDesktop/Archimedes/UnitVector.py`; sibling pages `GenerationalLineage/wiki/Units-and-the-Equation-Index.md`, `ValaQuenta/wiki/units.md` |
| The author | "information lives in the units, and units can 'spectrally show' direct generational lineage … mitochondrial lineage if you will … the 'units' are directly 'how the geometries hold the permutation'", and, naming the page: "it's the smallest part but carries the most multidimensional context … the units will identify exactly what equations matter … they are the equation index." |
| Confidence | dimensional analysis and the table entries: ESTABLISHED (re-run) · "units are the equation index" as a design statement: `INTERPRETATION` · the "geometry does no work" parallel: `INTERPRETATION` |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. The formal spec  `ESTABLISHED`

A unit is a point in a 7-axis lattice, the SI base dimensions mass (kg), length (m), time (s), current (A), temperature (K), amount (mol), luminous intensity (cd): every physical quantity's unit is an integer (or rational, for roots) exponent vector over them. Multiplying quantities adds the vectors, dividing subtracts, and a component landing on exactly zero is cancellation: a consequence of
vector arithmetic. This is standard dimensional analysis (the discipline behind Buckingham's Pi theorem, 1914, and every unit check a student runs); what the project adds is wiring it into the generational-lineage engine as an explicit, addressable domain for the same decomposition run on numbers (prime/composite) and processes (operator DAGs): the lineage engine's third domain, now its fourth with the Scale.

## 2. Mitochondrial lineage, made exact

A named compound unit's exponent vector is traced, not declared:

```
T = Wb/m² = (V·s)/m² = (W/A)·s/m² = ((J/s)/A)·s/m² = …  =  kg¹ m⁰ s⁻² A⁻¹
```

and the trace recombines exactly to the declared vector (PW16). Like a mass spectrometer's line pattern identifying a compound, the non-zero pattern of an exponent vector identifies the physical setting a bare number belongs to.

## 3. Word possibilities: the parallel to `wordnet_boxkite`  `INTERPRETATION` over a table

`context_vector` (`VAPMIP/wordnet_boxkite.py`, Phase 31) narrows a word to its candidate senses; `EQUATION_INDEX` narrows a dimension signature to its candidate equations, real standard laws checked against derivations. A bare number is ambiguous as a bare word is; the unit narrows what it could mean.

**Listing 1 — the lineage table, the Tesla trace, a unit quotient, and the index** (written for this page; needs the installed ValaQuenta package; runs cold)

```python
import importlib
u = importlib.import_module('ValaQuenta.modules.units.maths')
print('SI base axes:', u.SI_BASE)
vt = u.verify_lineage_table(); print('verify_lineage_table: holds =', vt['holds'], '; named units checked:', len(vt['results']))
t = u.unit_lineage_decompose(u.unit_vector([1, 0, -2, -1, 0, 0, 0], 'T'), u.LINEAGE_TABLE)
print('Tesla: declared', t['declared_exponents'], 'traced', t['traced_exponents'], 'match', t['matches']); print('lineage path:', t['lineage_path'])
J = u.unit_vector([1, 2, -2, 0, 0, 0, 0], 'J'); s = u.unit_vector([0, 0, 1, 0, 0, 0, 0], 's')
print('J / s ->', u.unit_div(J, s)['exponents'], '(power)')
for sig in ((1, 2, -2, 0, 0, 0, 0), (1, 1, -2, 0, 0, 0, 0), (1, 0, -2, -1, 0, 0, 0)): print(sig, '->', u.equation_index_lookup(sig))
print('equation index size:', len(u.EQUATION_INDEX), 'signatures')
```

```
SI base axes: ('kg', 'm', 's', 'A', 'K', 'mol', 'cd')
verify_lineage_table: holds = True ; named units checked: 11
Tesla: declared (1, 0, -2, -1, 0, 0, 0) traced (1, 0, -2, -1, 0, 0, 0) match True
lineage path: ['T', 'Wb', 'V', 'W', 'J', 'N', 'kg', 'm', 's', 'm', 's', 'A', 's', 'm']
J / s -> (1, 2, -3, 0, 0, 0, 0) (power)
(1, 2, -2, 0, 0, 0, 0) -> ['kinetic energy: E = (1/2)*m*v^2', 'gravitational PE: E = m*g*h', 'work: W = F*d', 'spring PE: E = (1/2)*k*x^2', 'heat: Q = m*c*dT']
(1, 1, -2, 0, 0, 0, 0) -> ["Newton's 2nd law: F = m*a", 'weight: F = m*g', "Hooke's law: F = k*x", 'centripetal force: F = m*v^2/r']
(1, 0, -2, -1, 0, 0, 0) -> ['magnetic flux density: B = Phi/A', 'Lorentz force: F = q*v*B']
equation index size: 16 signatures
```

The table of the earlier page reproduces: Joule [kg·m²·s⁻²] → kinetic energy ½mv², gravitational PE mgh, work F·d, spring PE ½kx², heat mcΔT; Newton [kg·m·s⁻²] → F = ma, F = mg, Hooke's law, mv²/r; Tesla [kg·s⁻²·A⁻¹] → B = Φ/A and the Lorentz force F = qvB; J/s lands on (1, 2, −3, 0, 0, 0, 0), power, "found automatically, not looked up". The engine's Tesla path lists 14 entries ending in the leaves (the earlier page counts six generations of depth; the path is the same trace written out in order). The index has 16 signatures: a small curated table, not an enumeration of physics, so "the unit identifies exactly what equations matter" holds for the entries it contains and says that a signature is *consistent with* those equations, not that no other equation shares it.

## 4. Units are a geometry that does no work  `INTERPRETATION`

`VAPMIP/docs/wiki/Tuning-the-Engine/33_folded_in_context_and_the_geometry_that_does_no_work.md` established that ∅_RB, σ_RB and the J_red/J_blue collapse are instances of one fact: a geometry carries no numeric content and does no work itself. A unit fits: the vector (1, 2, −2, 0, 0, 0, 0) computes nothing but decides whether `7.2 J + 3.1 kg` is a legal sentence (no) or `7.2 J / 3.1 s` is (yes; the result is power). The equation index makes it concrete: the geometry does not do the
physics; it tells you which physics is possible (the dimensional-consistency constraint, the necessary condition behind Buckingham's theorem).

## 5. Caught, not hidden: the bug the engine found in itself

The first lineage-tracer stored a composite's ancestry as bare parent names (`('Wb', 'm')` for Tesla) and always **added** the parents' vectors; it failed all six named units immediately (Tesla is Wb/m², a division by a square). Fixed by carrying signed `(parent, power)` pairs per step. Kept in the record: a caught fault is information.

## 6. Three independent implementations

- `PtolemyDesktop/Archimedes/UnitVector.py`: the original design (string-list based, "beginnings", predating this page);
- `GenerationalLineage/engine/lineage.py` PW16: the exponent-vector port, self-tested against the engine's own `_record`/`Status` machinery (the engine now reports 44/44 relations hold, [92](92_ring_theory_spine.md));
- `ValaQuenta/modules/units/`: the `EquationModule` port plus `EQUATION_INDEX`, the new content this page names (Listing 1).

Independent ports, not shared imports: the per-repository self-containment convention used for `factoral_spiral`, `cross_ratio` and the other cross-cutting results.

## 7. Related pages

[95 the Scale](95_the_scale.md) · [92 the ring-theory spine](92_ring_theory_spine.md) · `VAPMIP/docs/wiki/Tuning-the-Engine/33_*.md` · [96](96_the_riemann_fermat_horizon.md)
