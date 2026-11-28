# 63 — L_(I|O) as the Third Term: the Action Cone

| | |
|---|---|
| Scope | the 2026-06-13 observation that the Witches Hat showed J_red and J_blue and omitted the path between them; the "action cone"; standing-wave "cavitation"; what the geometry claims about galaxy arms |
| Predecessors | [52](52_l_dynamic_avoided_collaborator.md) (L_(I|O) first named), [62](62_hands_on_paper_minds_eye_caustic.md), [29](29_witches_hat_paper.md) |
| Code | `ArdaQuenta/modes/witches_hat.py` (the Witches Hat renderer) |
| Confidence | the definition's algebra: see [64](64_l_dynamic.md) §2 · the action cone and Lichtenberg picture: `CONJECTURE` · the singing/cavitation and galaxy-arm statements: corrected in §3 and §4 |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The renderer was not re-run |

## 1. The three parts

```
J_red     descending current, from above
J_blue    ascending current, from below
─────────────────────────────────────────────
L_(I|O)   the path actually traveled between them: the boundary in motion
```

The sedenion scalars give the endpoint, the Hamiltonian gives the energy, and
L_(I|O) is meant to give the path. This page's observation is about the picture: the
Witches Hat renderer drew the dome (J_pos), the bowl (J_neg), the brim (σ = ½) and
the galaxy emergence by conformal inversion, and drew no path. The 2026-06-13 request
is for an **action cone** in `witches_hat.py`: paths from the brim to the point, 16
primary branches at the sedenion spoke angles, sub-branches at the zero-divisor
intersections, J_red descending and J_blue ascending, meeting at σ = ½.
Whether `witches_hat.py` now draws it is a code-state question for the audit of
`ArdaQuenta`; this page records the specification.

The conventions for J_red and J_blue used here are those of
[61](61_up_down_not_forward_backward.md) §1 (the sign and direction conventions
differ between pages and are tabulated there).

## 2. The counts the picture uses

The "42 branch points" are the 42 zero-divisor index pairs of the sedenion
([25](25_sedenion_manual.md): 84 zero-divisors eᵢ ± eⱼ over 42 index pairs). "16
primary branches" is the sedenion dimension. Neither number is tied to a path
computation; they are counts taken from the algebra and drawn onto the cone.

## 3. "Singing is standing-wave cavitation"  `corrected`

The earlier text says the standing wave holds a shape that collapses and reforms, "the
vocal cord does not push air; it cavitates it", and that L_(I|O) is the "surface area
of the bubble". In physics, **cavitation** is the formation of vapour cavities in a
liquid where the local pressure falls below the vapour pressure. Phonation is
different: the vocal folds are set into self-sustained oscillation by the airflow
through them (the myoelastic–aerodynamic theory), modulating the air flow, which
radiates as sound. There is no cavitation in air in that process.

What survives as a statement of the framework is the geometric picture the
page draws from it: two opposite pressure-like currents meeting at a surface where a
discrete event occurs. The word "cavitation" there is a metaphor for a sharp
transition at σ = ½, as in [52b](52b_vortex_quantizing_shear.md) (where the transition is
the vortex nucleation at J_cross > GAP), and the vocal-fold physics is not
evidence for it.

## 4. Galaxy arms as the frozen action cone  `CONJECTURE`

The claim: galaxy spiral arms are the Lichtenberg paths of the action cone, frozen
into the disk by the conformal inversion through σ = ½. The earlier text added that
an animation with four evenly spaced linspace arms is "wrong" because real arms
are irregular and branching, with dominant arms set by the firing order.

What can be said from standard astronomy: spiral arms are well described by
logarithmic spirals with pitch angles of order 10°–30° and by density-wave theory;
real galaxies have branching and spurs. The framework's claim is a specific different
origin for that structure. It has not been tested against a galaxy's arm pattern:
no listing here fits an arm geometry, and the arm-spacing statements in the
earlier text are descriptions of the animation. As a status: `CONJECTURE`, untested.

## 5. Imperfection and the geodesic

"Perfection includes imperfection": the geodesic is the zero-information path and
L_(I|O) is the actual path, with L_(I|O) ⊃ geodesic. In ordinary mechanics the
geodesic is the extremum of the action among nearby paths; the real path of a system
with dissipation or noise is not extremal. The framework's statement is that the
information is in the deviation from the extremum. That is a design statement about
what the engine reads; how the deviation is measured is the subject of
[64](64_l_dynamic.md) §2, where the path-integral form is found to reduce to
e^(−E) times path length.

**Listing 1 — a branching path has no scale-stable length** (written for this page; runs cold)

```python
for n in (0, 4, 8, 16, 32):
    print('Koch refinement', n, ' length factor %.3e' % (4 / 3) ** n)
```

```
Koch refinement 0  length factor 1.000e+00
Koch refinement 4  length factor 3.160e+00
Koch refinement 8  length factor 9.989e+00
Koch refinement 16  length factor 9.977e+01
Koch refinement 32  length factor 9.955e+03
```

A Lichtenberg-type branching path is a fractal; its length grows without limit
as the resolution refines (Koch curve shown, length (4/3)ⁿ). Any quantity defined
as an integral along the path therefore needs a stated resolution, which is also
the engine's floor GAP ([56](56_telescope_caustic_zeno.md)).

## 6. Required updates recorded by the page

1. `witches_hat.py`: the action cone phase (16 primary branches, sub-branches at the zero-divisor intersections, red/blue/cyan colouring, arms as Lichtenberg paths) — open code item.
2. The overview page of the Standard Model of Monad Information Propagation ([01](01_overview.md)): add L_(I|O) as the third term next to J_red and J_blue.
3. The canonical maths: a formal L_(I|O) definition and its relation to J_red, J_blue ([133](133_canonical_maths.md) §3 and §7 hold the current state; the definition on [64](64_l_dynamic.md) is a conjecture).

## 7. Related pages

[29 Witches Hat](29_witches_hat_paper.md) · [52](52_l_dynamic_avoided_collaborator.md) · [62](62_hands_on_paper_minds_eye_caustic.md) ·
[64](64_l_dynamic.md) · [82 the L_(I|O) photon path](82_l_io_photon_path.md)
