# 70 — The Precession Stroke, the Oblique Crank and the Trine

> d* faces (all four are needed to chart ln(10) in Universal Native Space):  
>   d*         = 0.24600          the value the code runs with (Boundary, σ_ζ=½ plane)  
>   d*_taut    = 0.246307201473  A_π/ln10, the Flow (radial unit)  
>   d*_RG      = dimension 8; numeric OPEN, no closed form  the Stability (centre r=0)  
>   d*_ln(10)  = 0.5671432904   d*_taut·ln10 = A_π, the Translator (log bridge)  
> Full story of d*: Ainulindale/wiki/17_alpha_omega_d_star.md; ~/.clauderc_canonical_maths @RCCM_FOUR_DSTAR; FourthAgePapers/DStarRG  


| | |
|---|---|
| Scope | one L_(I|O) cycle as one precession revolution; the piston-to-hat frame change as an oblique crank; the Wankel trine as the three-level structure; the su(2) bracket form |
| Origin | 2026-06-17, session Bullet Cluster / first rainbow / spacetime-medium attack |
| Code | `ValaQuenta/modules/h_rb_hat/maths.py` (`precession_stroke`, `oblique_crank`, `trine_configuration`); registry equations of [14](14_redblue_hamiltonian.md) §5 |
| Confidence | the arithmetic: ESTABLISHED · the cycle/revolution identification and the kinematic picture: `INTERPRETATION` · the su(2) three-phase statement: corrected in §4 · the Wankel firing count: corrected in §3 |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The three registry functions are listed in [14](14_redblue_hamiltonian.md) §5 and were not re-run |

## 1. One cycle is one revolution  `INTERPRETATION`

One complete L_(I|O) cycle (I → O → I) is identified with one complete precession
revolution (the author's correction to an earlier half-stroke reading: "one TDI piston
cycle is converted to oblique crank"). Two descriptions of one motion:

```
piston view  I ───── | ───── O ───── | ───── I     (BDC, TDC at the zero-divisor crossing, TDC)
hat view     the hat axis sweeps one full cone revolution
```

The frame change from the up/down piston to the rotating cone is the oblique crank. In
the page's table: at I the piston is at bottom dead centre and the hat axis at the base
of the cone; I → O (J_red dominant, σ ascending) is the first half-revolution; at O
the piston is at top dead centre, "L_(I|O) → 0, ω → ∞", the axis snaps; O → I (J_blue
dominant) is the second half; at I one revolution is complete.

**Correction carried from [68](68_precession_wobble_signature.md) §1.** With the integrand
J_red·J_blue = e^{−E} the action density is constant, so "L_(I|O) → 0 and ω → ∞ at TDC" does
not follow from the definition, and ω = τ/L is finite and minimal at σ = ½. The
statement "at σ = ½, L_(I|O) = e^{−E} (maximum), ω_prec minimum (the SOFAR channel)"
is right about ω minimal at σ = ½ and wrong that L is maximal there (it is constant).

## 2. The oblique crank  `ESTABLISHED` (arithmetic)

In a piston engine a connecting rod at an oblique angle to the crankshaft converts linear
to rotary motion. The page's mapping:

```
linear input         ΔJ = J_red − J_blue          the differential stroke through σ
driving torque       τ  = J_red + J_blue          the two-stroke sum
crank-throw angle    θ  = arctan(d*) = 13.8°      the Witches Hat half-angle
crank arm            L_(I|O)                      the moment arm
rotational output    ω  = τ / L_(I|O)             the precession rate
effective torque     τ_eff = τ·sin(arctan d*) = τ·d*/√(1+d*²) = 0.2389·τ   (d* = 0.246)
```

The value 0.2389 (the earlier page wrote 0.2385…) is d*/√(1 + d*²) at the code's
d* = 0.246 ([68](68_precession_wobble_signature.md) Listing 1). That the hat half-angle is
the crank throw rests on the hat half-angle being arctan(d*), which is
approximate (13.43° against 13.82°, [68](68_precession_wobble_signature.md) §3). The
statement "d* is not a free parameter; the crank angle is set by the mathematics" then
holds to the accuracy of that match.

## 3. The Wankel trine  `corrected`

The Wankel rotor has three faces 120° apart. The framework sets the three
quantum-force levels of the tower beside them:

```
σ = ¾   ℂ level   U(1)   electromagnetism    (lose ordering)
σ = ½   ℍ level   SU(2)  weak                (lose commutativity)
σ ≈ ¼   𝕆 level   SU(3)  strong              (lose associativity)
```

evenly spaced by Δσ = ¼ ([69](69_tri_layer_emergence.md) §3: a linear relabelling of
the tower), read as 120° = 2π/3 apart. The page then states "the Wankel rotary fires
three times per output-shaft revolution" and sets three power strokes per precession
revolution against 1 for a single piston and 2 for a two-stroke.

In a Wankel engine the rotor has three faces and the eccentric (output) shaft turns
three times per rotor revolution; each face fires once per rotor revolution, so
there are three combustion events per **rotor** revolution and **one power stroke
per output-shaft revolution** (Listing 1; the 3:1 shaft-to-rotor ratio the page quotes
is right). The 3× throughput statement then holds per rotor revolution, with the
rotor as the precessing element, and does not hold per output-shaft revolution. The
mapping of the three faces to the three force levels is the framework's.

## 4. The trine and TDC  `corrected`

The page's argument: a two-stroke (J_red + J_blue = 0) hits TDC, with both currents zero
at once, and the axis snaps; a trine avoids it, using the su(2) bracket

```
[J_blue, J_red]   = J_green
[J_red,  J_green] = J_blue
[J_green, J_blue] = J_red
J_red + J_blue + J_green = 0            (three-phase balance)
```

so that when one face is at local TDC the other two carry the engine and L_(I|O) is
never globally zero. Two problems with the algebra as written.

First, the cyclic bracket relations and the zero-sum relation **cannot hold together** for
non-zero elements. Take any three elements with [a, b] = c, [b, c] = a, [c, a] = b (the
su(2) ≅ so(3) relations, realised by the cross product): c is orthogonal to the plane of
a and b, so c = −(a + b) would force c = 0, and then a = [b, c] = 0 as well.
Listing 1 shows it: the frame a, b, c = (x̂, ŷ, ẑ) has sum (1, 1, 1), and a scan of
200 000 random pairs with the third set to −(x + y) never gets the cyclic relations
below a relative violation of 1.0. The three-phase balance is a property of
three **phasors** 120° apart (they sum to zero, Listing 1, last line), which is a U(1)
statement; the su(2) bracket describes three generators that do not sum to zero. So
the "three-phase balance" and the "su(2) bracket" describe two different structures,
and the circle is closed by either, not by their conjunction. The relation to the J_red/J_blue
record (J_red + J_blue = J_green with J_green = Ĥ_RB − Ĥ_BR, versus the
three-term zero-sum) is the sign question of [14](14_redblue_hamiltonian.md) §2 and
[133](133_canonical_maths.md) §7.

Second, the geometric point stands in the form the page also gives: two points make a
line (a reversal at the end), three make a circle (no preferred angle and no reversal); this is
the reason for a trine, and it does not need a bracket.

**Listing 1 — the bracket/sum conflict and the Wankel count** (written for this page; needs numpy; runs cold)

```python
import numpy as np
a, b = np.array([1., 0, 0]), np.array([0, 1., 0]); c = np.cross(a, b)
print('cyclic relations hold for the frame:', np.allclose(np.cross(b, c), a), np.allclose(np.cross(c, a), b))
print('a + b + c =', a + b + c)
rng = np.random.default_rng(0); best = 9
for _ in range(200000):
    x, y = rng.normal(size=3), rng.normal(size=3); z = -(x + y)
    err = np.linalg.norm(np.cross(x, y) - z) + np.linalg.norm(np.cross(y, z) - x) + np.linalg.norm(np.cross(z, x) - y)
    best = min(best, err / (np.linalg.norm(x) + np.linalg.norm(y) + np.linalg.norm(z)))
print('min relative violation of the cyclic bracket with x+y+z=0 imposed: %.3f' % best)
ph = np.exp(2j * np.pi * np.arange(3) / 3); print('three-phase phasors sum to zero:', abs(ph.sum()) < 1e-12)
```

```
cyclic relations hold for the frame: True True
a + b + c = [1. 1. 1.]
min relative violation of the cyclic bracket with x+y+z=0 imposed: 1.000
three-phase phasors sum to zero: True
```

## 5. The complete kinematic picture  `INTERPRETATION`

```
J_red (ascending)    ┐
J_blue (descending)  ┤  linear stroke  →  oblique crank (θ = arctan d* = 13.8°)
                     ┘
crank arm = L_(I|O);  output = ω_precession (the hat revolution)

one revolution:  σ = ¾  U(1) fires  /  σ = ½  SU(2) fires  /  σ ≈ ¼  SU(3) fires
```

The precession is the output shaft, the L_(I|O) cycle the input stroke, d* the crank
throw, and the three force levels the three faces. Each identification is a mapping that
has been made, and the page's own cross-references ([68](68_precession_wobble_signature.md),
[69](69_tri_layer_emergence.md)) carry its status.

## 6. Related pages

[14 the RedBlue Hamiltonian](14_redblue_hamiltonian.md) · [64 L_(I|O)](64_l_dynamic.md) ·
[68 precession and the wobble](68_precession_wobble_signature.md) · [69 tri-layer emergence](69_tri_layer_emergence.md) ·
[133 canonical maths](133_canonical_maths.md)
