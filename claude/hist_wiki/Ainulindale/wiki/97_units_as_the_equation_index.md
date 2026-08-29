# 97 — Units as the Equation Index

**Written 2026-08-25.** Continues the same-day thread from
[[95_the_scale]] and [[96_the_riemann_fermat_horizon]]. Engine:
`SedenionFactoralRelativity/engine/lineage.py` PW16, independently ported
to `ValaQuenta/modules/units/` and (the original, pre-existing design)
`PtolemyDesktop/Archimedes/UnitVector.py`.

Cody, opening the thread: *"information lives in the units, and units can
'spectrally show' direct generational lineage...mitochondrial lineage if
you will...the 'units' are directly 'how the geometries hold the
permutation.'"* And the claim that gives this page its name: *"it's the
smallest part but carries the most multidimensional context...and should
be considered 'word possibilities' if describing mathematical ideas...the
units will identify exactly what equations matter...they are the equation
index."*

---

## The formal spec, stated plainly

A unit is a point in a 7-axis lattice — the SI base dimensions: mass
(`kg`), length (`m`), time (`s`), current (`A`), temperature (`K`), amount
(`mol`), luminous intensity (`cd`). Every physical quantity's unit is an
integer (or rational, for roots) exponent vector over these 7 axes.
Multiplying two quantities **adds** their exponent vectors; dividing
**subtracts**; a component landing on exactly zero **is** cancellation —
not a special case, a direct consequence of vector arithmetic. This is not
a new theorem; it is standard dimensional analysis, the same discipline
behind the Buckingham Pi theorem (Buckingham, 1914) and every unit-check a
physics student is taught to run before trusting an answer. What this
project adds is not the physics — it's wiring that standard practice into
this project's own generational-lineage engine as an explicit, addressable,
third — now fourth — domain for the same decomposition discipline already
run on numbers (prime/composite) and processes (operator DAGs).

## Mitochondrial lineage — the metaphor, made exact

Mitochondrial DNA is inherited along one unbroken line and read off to
trace ancestry precisely, generation by generation. A named compound
unit's exponent vector works the same way: Tesla isn't declared, it's
*traced* —

```
T = Wb / m²  =  (V·s) / m²  =  (W/A)·s / m²  =  (J/s / A)·s / m²  =  ...
  =  kg¹ · m⁰ · s⁻² · A⁻¹
```

— six generations back to the leaves, and the trace **recombines exactly**
to Tesla's own declared vector (`PW16`, checked in code, not asserted).
That's the "spectral" reading too: like a mass spectrometer's line pattern
uniquely identifying a compound, an exponent vector's non-zero pattern
uniquely identifies which physical setting a bare number belongs to.

## Word possibilities — the exact parallel to `wordnet_boxkite`

This is not a loose analogy; it's the same move, run on a different
domain. `context_vector` (`VAPMIP/wordnet_boxkite.py`, Phase 31) takes a
word and returns a vector that narrows it to its candidate *senses*
(synsets) — the semantic "word possibilities" a bare token could mean.
`EQUATION_INDEX` (`ValaQuenta/modules/units/maths.py`) takes a dimension
signature and returns the candidate *equations* that produce it — real,
standard physical laws, checked against real derivations, not invented:

```
[kg·m²·s⁻²]  (Joule)  ->  kinetic energy E=½mv², gravitational PE E=mgh,
                          work W=F·d, spring PE E=½kx², heat Q=mcΔT
[kg·m·s⁻²]   (Newton) ->  F=ma, F=mg, Hooke's law F=kx, F=mv²/r
[kg·s⁻²·A⁻¹] (Tesla)  ->  B=Φ/A, Lorentz force F=qvB
```

A bare number is ambiguous the way a bare word is. The unit — like the
context vector — is what narrows the possibility space down to what the
number could actually *mean*.

## Units are a geometry — the same finding, a fourth time

`docs/wiki/Tuning-the-Engine/33_folded_in_context_and_the_geometry_that_does_no_work.md`
(VAPMIP) established that `∅_RB`, `σ_RB`, and the `J_red`/`J_blue` collapse
are all instances of one fact: **a geometry carries no numeric content and
does no work itself.** A unit fits the same description exactly — the
exponent vector `(1,2,-2,0,0,0,0)` computes nothing on its own, but it is
precisely what decides whether `7.2 J + 3.1 kg` is a legal sentence
(**no**) or `7.2 J / 3.1 s` is (**yes**, and the result is power, `(1,2,-3,0,0,0,0)`,
found automatically, not looked up). The equation index makes this
concrete: the geometry doesn't do the physics, it tells you which physics
is even *possible*.

## Caught, not hidden: the bug this page's own engine found in itself

The first version of the lineage-tracer stored a composite's ancestry as
bare parent names (`('Wb', 'm')` for Tesla) and always **added** the
parents' vectors. Running it failed all six named units immediately —
Tesla is `Wb/m²`, a divide by a square, not an add of `Wb` and `m`. Fixed
by carrying signed `(parent, power)` pairs per lineage step. Kept in the
record per this project's standing rule: a caught fault is information,
not an embarrassment to edit away.

## Three independent implementations, per this project's own convention

- `PtolemyDesktop/Archimedes/UnitVector.py` — the original design (string-
  list based, "beginnings," pre-dates this page).
- `SedenionFactoralRelativity/engine/lineage.py` `PW16` — the exponent-
  vector port, self-tested against the generational-lineage engine's own
  `_record`/`Status` machinery. 44/44 relations hold.
- `ValaQuenta/modules/units/` — the `EquationModule` port, plus
  `EQUATION_INDEX`, the new content this page names.

Independent ports, not shared imports — the per-repo self-containment
convention this project already uses for `factoral_spiral`, `cross_ratio`,
and every other cross-cutting result.

## Related

[[95_the_scale]] (SCALE, the sibling tier-0 irreducible this page's unit
vectors compose under); `VAPMIP/docs/wiki/Tuning-the-Engine/33_*.md` (the
"geometry does no work" finding this page extends to a fourth domain);
`SedenionFactoralRelativity/wiki/Units-and-the-Equation-Index.md` and
`ValaQuenta/wiki/units.md` (the sibling pages, same day).
