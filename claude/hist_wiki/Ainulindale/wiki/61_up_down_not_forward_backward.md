# 61 — The Boundary Is Oriented: Up/Down, Not Forward/Backward

| | |
|---|---|
| Scope | the 2026-06-13 correction of the Noether-current framing from "forward/backward" to "up/down in the Cayley–Dickson tower"; the forced-σ meeting point; what the correction fixes and what it leaves open |
| Corrects | [05](05_noether_engine.md), [06](06_noether_information_engine.md), the ValaQuenta `noether` page ("forward/backward current") |
| Code | `ValaQuenta/modules/noether` (`forced_sigma`) |
| Confidence | F(σ) = B(σ) ⇔ σ = ½: ESTABLISHED (algebra) · up/down as the orientation of the currents: `INTERPRETATION` (consistent with the octonion-halves reading of [14](14_redblue_hamiltonian.md) §3) · "σ = ½ is the shadow of the world above": `THEORETICAL` |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. The correction

The earlier framing: J_forward = "what the word is" (Riemann current, attractor),
J_backward = "what the word cannot be" (Fermat current, repulsor). The corrected
framing: the two currents run **up** and **down the tower**:

```
J_ascending   away from the zero-divisors, toward the next Cayley–Dickson level above
J_descending  toward the zero-divisors, toward collapse
```

This is the same orientation as the octonion halves of
[14](14_redblue_hamiltonian.md) §3: the lower half e₀–e₇ and the upper half e₈–e₁₅
of the sedenion are "below" and "above" along the ⊕8 seam. The framework's
statement that the sedenion is the boundary the two halves compose is the algebraic
content behind the word "oriented".

The sign and naming conventions of the currents differ between pages and must be
read with care:

| Source | J_red | J_blue |
|---|---|---|
| this page (forced σ) | descending, from above; B(σ) = e^(−(1−σ)E) | ascending, from the zero-divisors; F(σ) = e^(−σE) |
| [14](14_redblue_hamiltonian.md), [133](133_canonical_maths.md) | the lower octonion e₀–e₇, "forward" | the upper octonion e₈–e₁₅, "reverse signal" |
| [64](64_l_dynamic.md) | e^(−(1−σ)E), "flows from O toward |" | e^(−σE), "flows from I toward |" |

The identification of the page-61 pair with the octonion halves is not made in the
source pages and is not derived in this wiki; the assignment of which half is
"above" is the author's, and the table records the mismatch (red is "forward /
lower" in one place and "descending from above" in another). Unifying it is an
open decision of [133](133_canonical_maths.md) §7.

## 2. The forced-σ meeting point  `ESTABLISHED`

```
from the zero-divisor side:  F(σ) = e^(−σE)         (decreasing in σ)
from the level above:        B(σ) = e^(−(1−σ)E)     (increasing in σ)
```

F = B ⇔ σ = 1 − σ ⇔ σ = ½, for every E ≠ 0 (at E = 0 both are 1 for all σ). The
meeting point does not depend on the level of the tower; it depends only on the
symmetry σ ↔ 1 − σ of the pair. So the algebra proves one thing: the two
exponential profiles cross at σ = ½, for any E. The tower-level reading in
the next section is on top of that and not derived from it.

**Listing 1 — the crossing, and what is and is not extremal there** (written for this page; needs numpy; runs cold)

```python
import numpy as np
for E in (0.5, 1.0, 5.0):
    s = np.linspace(0, 1, 100001)
    F, B = np.exp(-s * E), np.exp(-(1 - s) * E)
    print('E=%.1f  F=B at sigma=%.5f ; product F*B: min %.12f max %.12f (e^-E = %.12f) ; '
          'max of min(F,B) at sigma=%.5f value %.6f (e^-E/2 = %.6f)'
          % (E, s[np.argmin(abs(F - B))], (F * B).min(), (F * B).max(), np.exp(-E),
             s[np.argmax(np.minimum(F, B))], np.minimum(F, B).max(), np.exp(-E / 2)))
```

```
E=0.5  F=B at sigma=0.50000 ; product F*B: min 0.606530659713 max 0.606530659713 (e^-E = 0.606530659713) ; max of min(F,B) at sigma=0.50000 value 0.778801 (e^-E/2 = 0.778801)
E=1.0  F=B at sigma=0.50000 ; product F*B: min 0.367879441171 max 0.367879441171 (e^-E = 0.367879441171) ; max of min(F,B) at sigma=0.50000 value 0.606531 (e^-E/2 = 0.606531)
E=5.0  F=B at sigma=0.50000 ; product F*B: min 0.006737946999 max 0.006737946999 (e^-E = 0.006737946999) ; max of min(F,B) at sigma=0.50000 value 0.082085 (e^-E/2 = 0.082085)
```

Two facts the listing fixes, both used by later pages:

- the profiles cross at σ = ½ and min(F, B) peaks there (value e^(−E/2));
- the **product** F·B equals e^(−E) at every σ. It is not peaked at ½. Statements
  that "the coupling is maximal at σ = ½" are true of min(F, B) and false of the
  product; the consequence for the path integral is in [64](64_l_dynamic.md) §2.

## 3. The shadow reading  `THEORETICAL`

The page's picture: σ = ½ is "the shadow cast by the world above onto the world
below"; each doubling projects its boundary onto the algebra beneath, at the same
relative position. In this reading the word is held between an ascending current
that pulls it up toward the shadow and a descending current that would collapse it
into the zero-divisors, and σ = ½ is the one stable position.

What is established underneath: the crossing point of §2, the orientation of the
two octonion halves, and the zero-divisor structure of 𝕊 ([25](25_sedenion_manual.md)).
What is the author's reading: that the crossing is a shadow of the next algebra, and
that "a wrong claim cannot cross the shadow". The latter is an architectural
statement about the sedenion SVG, where activated words lie inside the dashed σ = ½
circle, and is a property of the drawing as built.

## 4. What changes for the other engines

| Engine | The correction |
|---|---|
| [03 Inversion](03_inversion_engine.md) | (I|O) is a vertical operation (a level and the level above); one (I|O) cycle is one doubling's worth of ascent and return |
| Sedenion SVG | the path through the 16 spokes ascends monotonically from the zero-divisor centre, ending at e₁₅ |
| Cavitation cascade | the black-hole horizon is read as the σ = ½ shadow for mass; as with all horizon statements here, it is a coordinate feature, not a point where physics changes ([53](53_t256_cryptographic_transparency.md) is unrelated; see the horizon corrections on [32](32_superconducting_medium.md)) |
| Heart | not carried over; see [60](60_heart_j2_involution.md) |

The standing phrase for all engines: *ascending current* (toward the shadow of
the level above) and *descending current* (toward the zero-divisor ground), in place
of "forward" and "backward".

## 5. Related pages

[05 Noether](05_noether_engine.md) · [06 Noether information](06_noether_information_engine.md) ·
[14 the RedBlue Hamiltonian](14_redblue_hamiltonian.md) · [64 L_(I|O)](64_l_dynamic.md) · [133 canonical maths](133_canonical_maths.md)
