---
name: unit-management
description: Identify which physical equations are relevant to a prompt by decomposing the physical quantities/units it mentions into SI base-dimension exponent vectors, then looking up which standard equations produce that dimension signature. Use when a prompt mentions physical quantities with units (energy, force, pressure, voltage, concentration, etc.), asks "what equation applies here", needs a unit-consistency check, needs unit conversion, or needs to narrow down which mathematical/physical relationship is being described from the units alone.
version: 0.1.0
---

# Unit Management — Units as the Equation Index

A unit is not decoration on a number. It is a coordinate that narrows what
the number could mean — the exact same move `context_vector` makes for a
word (narrowing it to candidate WordNet senses), run on a different domain.
Built from `SedenionFactoralRelativity/engine/lineage.py` `PW16` and
`ValaQuenta/modules/units/`, 2026-08-25.

## 0. The method, in one line

**Decompose every unit mentioned in the prompt into its 7-axis SI exponent
vector, combine those vectors the way the prompt combines the quantities
(multiply/divide), then look up the resulting signature in the equation
index.** The signature narrows a large space of possible relationships to
a short, checkable list — it does not, by itself, tell you which one is
meant. Report the candidates; do not silently pick one.

## 1. The 7 leaves (irreducible — nothing decomposes further)

```
kg  m  s  A  K  mol  cd     (mass, length, time, current, temperature, amount, luminous intensity)
```

Every unit is an exponent vector `(kg, m, s, A, K, mol, cd)` over these 7
axes. Multiplying quantities **adds** the vectors; dividing **subtracts**;
a component landing on exactly zero **is** cancellation, not a special
case.

## 2. The named-compound lineage table (composites, not leaves)

| unit | symbol | exponents `(kg,m,s,A,K,mol,cd)` | built from |
|---|---|---|---|
| Newton | N | `(1,1,-2,0,0,0,0)` | `kg¹·m¹·s⁻²` |
| Joule | J | `(1,2,-2,0,0,0,0)` | `N¹·m¹` |
| Watt | W | `(1,2,-3,0,0,0,0)` | `J¹·s⁻¹` |
| Pascal | Pa | `(1,-1,-2,0,0,0,0)` | `N¹·m⁻²` |
| Coulomb | C | `(0,0,1,1,0,0,0)` | `A¹·s¹` |
| Volt | V | `(1,2,-3,-1,0,0,0)` | `W¹·A⁻¹` |
| Ohm | Ω | `(1,2,-3,-2,0,0,0)` | `V¹·A⁻¹` |
| Farad | F | `(-1,-2,4,2,0,0,0)` | `C¹·V⁻¹` |
| Weber | Wb | `(1,2,-2,-1,0,0,0)` | `V¹·s¹` |
| Tesla | T | `(1,0,-2,-1,0,0,0)` | `Wb¹·m⁻²` |
| Henry | H | `(1,2,-2,-2,0,0,0)` | `Wb¹·A⁻¹` |

Verified: each row's build column, walked all the way back, recombines
exactly to that row's own exponent vector — checked in code
(`unit_lineage_decompose`), not asserted. The first draft of this table
stored bare parent names and always *added* them, which failed every row
built by division (Tesla is `Wb/m²`, not `Wb·m`) — the lesson: a lineage
step needs a signed power, not just a parent's name.

## 3. The equation index (the actual point of this skill)

Given a resolved dimension signature, these are real, standard physical
relationships known to produce it — a starting table, not exhaustive:

```
(1,2,-2,0,0,0,0)  Joule    -> E=½mv² (kinetic), E=mgh (grav. PE), W=F·d,
                              E=½kx² (spring PE), Q=mcΔT (heat)
(1,1,-2,0,0,0,0)  Newton   -> F=ma, F=mg, F=kx (Hooke), F=mv²/r (centripetal)
(1,2,-3,0,0,0,0)  Watt     -> P=W/t, P=Fv, P=IV
(1,-1,-2,0,0,0,0) Pascal   -> P=F/A, PV=nRT (ideal gas)
(0,0,1,1,0,0,0)   Coulomb  -> Q=It
(1,2,-3,-1,0,0,0) Volt     -> V=IR (Ohm's law), V=W/Q
(1,2,-3,-2,0,0,0) Ohm      -> R=V/I
(-1,-2,4,2,0,0,0) Farad    -> C=Q/V
(1,2,-2,-1,0,0,0) Weber    -> Φ=BA, EMF=-dΦ/dt (Faraday)
(1,0,-2,-1,0,0,0) Tesla    -> B=Φ/A, F=qvB (Lorentz)
(1,2,-2,-2,0,0,0) Henry    -> L=Φ/I, EMF=-L·dI/dt
(0,-3,0,0,0,1,0)  mol/m³   -> c=n/V (molar concentration)
(0,1,-1,0,0,0,0)  m/s      -> v=d/t
(0,0,-1,0,0,0,0)  1/s      -> f=1/T (frequency)
```

If the mentioned quantities' combined signature isn't in this table, say
so plainly and report the raw exponent vector — do not force a match.

## 4. Worked procedure

1. Identify every physical quantity in the prompt and its stated or
   implied unit.
2. Convert each unit to its `(kg,m,s,A,K,mol,cd)` vector — leaves directly,
   named compounds via §2's table (or `unit_lineage_decompose` if it's not
   listed here).
3. Combine the vectors exactly the way the prompt combines the quantities
   (multiply = add vectors, divide = subtract).
4. Look up the resulting vector in §3. Report the candidate equations, or
   report "no known match, raw signature is X" honestly if there isn't one.
5. If the prompt gives no units at all, this skill does not apply —
   dimensional analysis needs at least one real unit to anchor to.

## 5. The real code, when a worked example isn't enough

```python
from SedenionFactoralRelativity.engine import (
    SI_BASE, unit_vector, unit_mul, unit_div, unit_lineage_decompose,
)
# or the independent ValaQuenta port:
from ValaQuenta.modules.units import (
    SI_BASE, unit_vector, unit_mul, unit_div, LINEAGE_TABLE,
    equation_index_lookup,
)
```

Both are independent ports of the same identity (this project's per-repo
self-containment convention) — either is authoritative; they agree by
construction (both self-tested, `SedenionFactoralRelativity`: 44/44
relations hold).

## 6. What this skill is NOT

- Not a claim that a dimension signature uniquely determines an equation —
  many different physical laws share the same units (Joule is both kinetic
  and potential energy; the signature narrows, it does not decide).
- Not a general unit-conversion calculator — it identifies *which
  equations apply*, given units; converting a value between compatible
  units is a separate, much simpler scalar-factor operation not covered
  here.
- Not exhaustive — `EQUATION_INDEX`/§3 covers common mechanical and
  electromagnetic quantities. A signature with no listed match is real
  information (a rare or unnamed combination), not a failure of the skill.

## Related

`Ainulindale/wiki/97_units_as_the_equation_index.md`,
`ValaQuenta/wiki/units.md`,
`SedenionFactoralRelativity/wiki/Units-and-the-Equation-Index.md` — the
full writeups, including the caught-bug story and the "geometry does no
work" framing this skill's method depends on: a unit computes nothing on
its own, it only decides what's dimensionally legal.
