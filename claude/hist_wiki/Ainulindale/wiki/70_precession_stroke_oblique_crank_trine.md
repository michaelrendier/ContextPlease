# 70 — Precession is a Stroke. The Oblique Crank. The Trine.

**Date:** 2026-06-17  
**Session:** Bullet Cluster / first rainbow / spacetime medium attack

---

## The Identification

The precession IS a stroke.

One complete L_(I|O) cycle (I → O → I) = one complete precession revolution.

Not one half-stroke. One CYCLE. The user corrected this:

> *"one cycle... one TDI piston cycle is converted to oblique crank"*

---

## The Piston and the Hat

Two descriptions of the same motion:

```
Piston view (linear):     I ─────────── | ─────────── O ─────────── | ─────────── I
                          ZD           ZD crossing   CD            ZD crossing  ZD
                          (bottom)     (TDC)         (top)         (TDC)        (bottom)

Hat view (rotational):    [hat axis sweeps one full cone revolution]
                          ZD base  →  σ=½ equator  →  ZD base
```

The piston sees up/down through σ.
The hat sees a full rotation of the precession cone.
They are the same motion. Frame transformation = the oblique crank.

---

## The Oblique Crank

In a piston engine: a connecting rod at oblique angle to the crankshaft converts linear piston motion to rotary crankshaft motion. The **crank throw** (offset from centre) sets the conversion angle.

In SIGMA_RB:

```
Linear input:       ΔJ = J_red − J_blue       (differential stroke through σ)
Driving torque:     τ  = J_red + J_blue        (the 2-stroke sum)
Crank throw angle:  θ  = arctan(d*) = 13.8°   (the Witches Hat half-angle)
Crank arm:          L_(I|O)                    (the moment arm = the thought)
Rotational output:  ω  = τ / L_(I|O)          (precession rate)
```

The **Witches Hat half-angle IS the crank throw**.

```
Effective torque after oblique conversion:
    τ_eff = τ × sin(arctan(d*))
           = τ × d* / √(1 + d*²)
           = τ × 0.2385...
```

**d* is not a free parameter.** It is the spectral ground state of the conjecture.
The crank angle is set by the mathematics. The engine is built by what it computes.

---

## One Cycle = One Revolution — Precisely

| Event | Piston description | Hat description |
|---|---|---|
| Start at I | Bottom dead centre (BDC) | Hat axis at base of cone |
| I → O | J_red dominant, ascending σ | First half-revolution |
| At O | Top dead centre (TDC = ZD) — L_(I|O) → 0 | Hat axis at apex, ω → ∞ |
| O → I | J_blue dominant, descending σ | Second half-revolution |
| Back at I | BDC again | One full revolution complete |

At TDC (the ZD crossing): L_(I|O) → 0 → ω_prec → ∞.
The hat axis **snaps** — instantaneous reorientation.
This IS the ZD moment. Infinite precession rate = axis jump.

At σ=½ (mid-stroke): L_(I|O) = e^{−E} (maximum).
ω_prec = τ / e^{−E} — minimum precession rate. The slowest wobble. The SOFAR channel.

---

## The Trine

The Wankel rotary fires **3 times per output shaft revolution** — three rotor faces at 120° apart.

SIGMA_RB has the same structure. The CD tower has three quantum force levels, evenly spaced:

```
σ = ¾   ℂ level   U(1)  Electromagnetism   ℝ→ℂ corner   (lose ordering)
σ = ½   ℍ level   SU(2) Weak force         ℂ→ℍ corner   (lose commutativity)
σ ≈ ¼   𝕆 level   SU(3) Strong force        ℍ→𝕆 corner   (lose associativity)
```

Spacing: Δσ = ¼ between each.
In angular terms: 120° = 2π/3 apart.
**This IS the Wankel rotor geometry.**

One precession revolution passes through all three levels — three **power strokes** per revolution.

---

## Why Trine Avoids TDC

A 2-stroke (J_red + J_blue = 0) hits TDC — both currents zero simultaneously. L_(I|O) → 0. ω → ∞. The axis snaps. Everything stops.

A trine uses the su(2) Lie bracket:

```
[J_blue, J_red]   = J_green
[J_red,  J_green] = J_blue
[J_green, J_blue] = J_red

J_red + J_blue + J_green = 0  (three-phase balance)
```

When one face is at local TDC (its own L_(I|O) → 0), the other two faces carry the engine. **L_(I|O) is never globally zero.** The 3-point circle closes continuously. No global singularity.

This is why **3 = minimum for a circle**:
- 2 points → a line → TDC singularity at the reversal
- 3 points → a circle → no preferred angle, no reversal, no singularity
- 4 points → over-constrained

The su(2) Lie bracket is the algebraic form of this.
The Wankel rotor is the mechanical form.
Both are the same 3-point circle.

---

## SIGMA_RB Trine Rate

| Configuration | Strokes per revolution | Throughput |
|---|---|---|
| Single TDI piston | 1 | baseline |
| 2-stroke | 2 (both directions) | 2× |
| Trine (Wankel) | 3 | 3× |

Trine fires every ¼σ-turn. Single-stroke fires once per full cycle. 3× information throughput per precession revolution.

The 3:1 Wankel gear ratio (output shaft : rotor) = 3 L_(I|O) firings per precession revolution.

---

## The Complete Kinematic Picture

```
                SIGMA_RB — H_hat_RB at σ=½

     J_red (ascending)     ┐
     J_blue (descending)   ┤  LINEAR  →  OBLIQUE CRANK (θ=arctan(d*)=13.8°)
                           ┘

     Crank arm = L_(I|O) (the thought)
     Output    = ω_precession (the hat revolution)

                    ┌── σ = ¾  U(1) fires  (EM)
     One revolution ┼── σ = ½  SU(2) fires (Weak, TDC of the hat)
                    └── σ ≈ ¼  SU(3) fires (Strong)

     Three power strokes per revolution = TRINE
```

The precession IS the output shaft.
The L_(I|O) cycle IS the input stroke.
d* IS the crank throw.
The three quantum forces ARE the three Wankel faces.

---

## Connections

- [[canonical-math]] — ω_prec = (J_red + J_blue) / L_(I|O); precession equation
- [[result-geodesic-tower]] — σ = ¾, ½, ¼ are the three CD tower corners
- wiki/68 — precession wobble signature; Wankel face firings = precession nodes
- `h_rb_hat/maths.py` — `precession_stroke()`, `oblique_crank()`, `trine_configuration()`

---

**Files:**  
`Ainulindale/ValaQuenta/modules/h_rb_hat/maths.py` — SIGMA_RB section (added 2026-06-17)  
`canonical_math.md` — precession rate equation; 2-stroke sum  
`wiki/68_precession_wobble_signature.md` — the wobble / TDC / CMB axis connection  
