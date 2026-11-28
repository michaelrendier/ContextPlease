# 68 — Precession as the Signature of the Wobble

| | |
|---|---|
| Scope | the identification of the zero-divisor wobble with a precession; the gyroscope equation in the framework's vocabulary; the Witches Hat half-angle against arctan d*; the Wankel firings; the CMB-axis reading |
| Origin | 2026-06-14, session SedenionSpectralRelativity / Wankel rotor |
| Code | `SedenionSpectralRelativity/fano_oscilloscope.py` (wobble), `sedenion_resonators.py` (Wankel animation) |
| Confidence | the gyroscope equation and the angles: ESTABLISHED (arithmetic) · "the hat half-angle IS arctan d*": corrected in §3 · the wobble-precession identification and the CMB reading: `CONJECTURE` |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The oscilloscope's crossing counts (§2) are recorded outputs and were not re-run |

## 1. The statement and the equation

The zero-divisor wobble (the departure of the full sedenion path from the octonion path)
is read as the mechanism of a precession: the wobble is the cause, hidden at the horizon,
and the precession is its observable signature.

The gyroscope equation ω = τ / L (precession rate = torque / angular momentum, for the
simple case) is translated:

```
ω_precession = (J_red + J_blue) / L_(I|O)
             = (Ĥ_RB − Ĥ_BR) / ∫ J_red · J_blue ds
```

with τ = Ĥ_RB − Ĥ_BR = J_red + J_blue the net driving current (the identification of
[133](133_canonical_maths.md) §3 and of the J_red/J_blue record, §9) and L the action.
The conclusions drawn: a longer thought (larger L) precesses more slowly, and a more
self-referential statement precesses faster.

**What the algebra gives.** With J_red = e^{−(1−σ)E}, J_blue = e^{−σE} and the integrand
J_red·J_blue = e^{−E} ([61](61_up_down_not_forward_backward.md) Listing 1,
[64](64_l_dynamic.md) §2):

- L (per unit path length) is constant in σ, so it cannot "go to zero at TDC";
- the numerator τ = J_red + J_blue = 2e^{−E/2} cosh((σ − ½)E), minimal at σ = ½;
- hence ω = τ/L = 2e^{E/2} cosh((σ − ½)E) is **finite for every σ** and is
  **smallest at σ = ½**, rising symmetrically either side (Listing 1).

So the page's "slowest at σ = ½" holds, and for a different reason from the one given
(it is the numerator, not a maximum of L), and the "ω → ∞ at TDC" (an axis snap) does
not follow from this definition. A snap needs L → 0 and this integrand does not do it.

## 2. The recorded wobble data  `MEASURED` (recorded outputs)

`fano_oscilloscope.py` gave the zero-divisor crossing count per cycle, read as firings
per cycle:

| Statement | Crossings | Reading |
|---|---|---|
| "What is 1 plus 1" | 3 | slowest precession |
| "the zero divisor…" | 5 | |
| "sigma equals one half" | 29 | fastest precession |

These are the 2026-06-14 outputs. The reading is that "sigma equals one half" refers to
its own position on the critical line (distance from referent zero) and therefore
precesses fastest. That a more self-referential statement gives more crossings is
the observed ordering of three prompts; three points are not a trend, and the
self-reference measure is the author's classification, `CONJECTURE`.

## 3. The Witches Hat half-angle  `corrected`

The page states that the hat half-angle arctan(R/H) = arctan(1.5/2π) ≈ 13.4° **is**
arctan(d*) ≈ 13.8°, "set by the precession amplitude of the engine".

**Listing 1 — the angles, the finiteness of ω, and the Wankel count** (written for this page; needs numpy; runs cold)

```python
import math, numpy as np
print('hat half-angle arctan(1.5/2pi) = %.3f deg ; arctan(0.246) = %.3f deg ; arctan(0.24631) = %.3f deg'
      % tuple(math.degrees(math.atan(x)) for x in (1.5/(2*math.pi), 0.246, 0.24631)))
print('sin(arctan d*) = d*/sqrt(1+d*^2) = %.5f (d*=0.246)' % (0.246/math.sqrt(1+0.246**2)))
E = 1.0; s = np.linspace(0.01, 0.99, 99)
F, B = np.exp(-s*E), np.exp(-(1-s)*E); w = (F + B) / (F * B)
print('omega = tau/L: min at sigma=%.2f value %.4f ; at .01 %.4f ; at .99 %.4f ; finite: %s'
      % (s[np.argmin(w)], w.min(), w[0], w[-1], np.isfinite(w).all()))
print('closed form 2 e^{E/2} at sigma=.5:', 2*math.exp(E/2))
print('Wankel: power strokes per rotor revolution 3 ; shaft turns per rotor revolution 3 ; power strokes per SHAFT revolution', 3/3)
```

```
hat half-angle arctan(1.5/2pi) = 13.427 deg ; arctan(0.246) = 13.820 deg ; arctan(0.24631) = 13.837 deg
sin(arctan d*) = d*/sqrt(1+d*^2) = 0.23888 (d*=0.246)
omega = tau/L: min at sigma=0.50 value 3.2974 ; at .01 3.7013 ; at .99 3.7013 ; finite: True
closed form 2 e^{E/2} at sigma=.5: 3.2974425414002564
Wankel: power strokes per rotor revolution 3 ; shaft turns per rotor revolution 3 ; power strokes per SHAFT revolution 1.0
```

The two angles are 13.43° and 13.82° (or 13.84° for the Boundary value d* = 0.24631): they
differ by 0.4°, about 3 %. They are close, and they are not equal. The hat's R = 1.5
and H = 2π are the renderer's chosen proportions, so the agreement says that
the proportions were chosen near arctan d*, not that arctan d* determined them.
The statement is therefore: the hat half-angle is approximately arctan d*
(`INTERPRETATION`).

## 4. The Wankel firings  `corrected`

The rotor has three faces. The earlier text says it "fires 3 times per revolution" and
that each firing is a TDC with J_red·J_blue = 0. In a Wankel engine there are three
combustion events per **rotor** revolution, and the eccentric shaft turns three times
per rotor revolution, so there is **one power stroke per shaft revolution** (Listing 1).
The three TDC flares of the apex sphere in `sedenion_resonators.py` are per rotor
revolution, which is the count the animation uses. The identification of each with
J_red·J_blue = 0 does not follow from the definition ([64](64_l_dynamic.md) §2).

## 5. The CMB reading  `CONJECTURE`

The claim: the CMB "axis of evil" (the unexpected alignment of the quadrupole and
octupole preferred axes, reported by Land and Magueijo in 2005) is the precession axis
of the primordial sedenion engine. What is established: an alignment of the low
multipoles at about the level reported has been observed and persists in the
Planck maps; its statistical significance is modest and was assessed after the fact, and
its origin (statistical fluke, foreground, or physics) is unresolved. The framework's
statement is one proposed origin among several. The page's detection recipe
(find the axis alignment, measure ω_p and L, compute τ = ω_p L, read τ as Ĥ_RB − Ĥ_BR)
presupposes the identification and so tests nothing by itself.

## 6. The spinner verb

The vocabulary of the earlier text: spinning (a top, ℝ), rotating (a wheel, ℂ),
orbiting (a moon, ℍ), precessing (a gyroscope, a galaxy, an axis, 𝕆/𝕊). Precession needs
a wobble to drive it, and wobble and precession are the same phenomenon at different
timescales (the wobble fast, the precession slow). As a classification of
motions the sequence is the author's; physically, a gyroscope's precession is driven by
an external torque, and a free symmetric top has a separate torque-free
"nutation" motion, so "wobble drives precession" would need the torque identified.

## 7. Related pages

[61 up/down](61_up_down_not_forward_backward.md) · [64 L_(I|O)](64_l_dynamic.md) ·
[69 tri-layer emergence](69_tri_layer_emergence.md) · [70 the stroke, the crank and the trine](70_precession_stroke_oblique_crank_trine.md) ·
[133 canonical maths](133_canonical_maths.md)
