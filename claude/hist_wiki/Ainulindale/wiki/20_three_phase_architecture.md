# 20 — Three-Phase Architecture

| | |
|---|---|
| Scope | the three-phase reading of the RedBlue engine: Red, Blue and Carrier; H = xp as the "lossless" evolution; the ContextBuffer as capacitor |
| Code | `ValaQuenta/modules/berry_keating` (xp, T map), `SemanticWordEngine/semantic_engine.py` (`Capacitor`, `Understand`), `PtolemyDesktop/Philadelphos/cyclic_context_buffer.py`, `VAPMIP/monad.py` |
| Confidence | THEORETICAL; the equations of motion in §2 and the root-of-unity facts in §1 and §5 are ESTABLISHED mathematics |
| Last verified | 2026-11-13: Listing 1 executed; the Z₃ and Z₆ statements checked numerically |

## 1. The structure

The three-phase structure is the discrete Fourier decomposition on the
3-cycle: the three cube roots of unity 1, ω, ω² (ω = e^{2πi/3}) sum to zero
(balanced, self-grounding), and their interaction is a rotating field.
Three-phase AC power is the physical instance; the framework's claim is that
the semantic engine is another instance of the same mathematics
(`THEORETICAL`: the mathematics is identical, the identification of the three
phases with semantic roles is the proposal).

| Phase | Channel | Lagrangian form | Role |
|---|---|---|---|
| 1, Red | forward Noether current | L_R = ẋ ln ẋ − ẋ (Berry–Keating) | assertion, "what is" |
| 2, Blue | backward information current | L_F = ẋ²/4 − ℘(x; g₂, g₃) (Fermat–Weierstrass) | constraint, "what cannot be" |
| 3, Carrier | rotating semantic field | Yang–Mills / Noether generator | context, the rotating observer |

Red and Blue are read as two descriptions of one mirror, the functional
equation ξ(s) = ξ(1−s): L_R is self-adjoint under s ↔ 1−s (A† = A), and L_F
breaks that symmetry (A† ≠ A). The Carrier is not a third independent entity:
it is the standing wave made by the counter-rotation of Red and Blue, the J₃
channel, "the Meaning" ([14](14_redblue_hamiltonian.md),
[19](19_cayley_dickson_tower.md) §4). (An earlier version added "the Frey curve
cannot exist, so Fermat's Last Theorem is true". FLT is a theorem by the
Frey–Ribet–Wiles argument ([18](18_fermat_lattice.md) §3), not a consequence of
this reading, and the sentence is withdrawn.)

## 2. H = xp

The Berry–Keating Hamiltonian H = xp has the equations of motion

```
ẋ = ∂H/∂p =  x          x(t) = x₀ eᵗ
ṗ = −∂H/∂x = −p         p(t) = p₀ e⁻ᵗ
xp = E                  conserved
```

H is scale invariant: x → λx, p → p/λ leaves it unchanged. `ESTABLISHED`.

**Listing 1 — the flow conserves E** (written for this page from the equations
above; the same flow is `xp_trajectory` in `SemanticWordEngine/semantic_engine.py`;
runs cold)

```python
import math

x0, p0 = 1.6058770193202365, 0.22807035205768092
for t in (0, 1, 2):
    x, p = x0 * math.exp(t), p0 * math.exp(-t)
    print(t, round(x, 6), round(p, 6), round(x * p, 12))
```

```
0 1.605877 0.22807 0.366252937158
1 4.365226 0.083902 0.366252937158
2 11.865915 0.030866 0.366252937158
```

x grows and p decays exponentially while E = xp stays fixed. The framework
reads E as "the semantic prime", and the equations as containing no
conditionals or loops. That is a property of the *equations of motion*; the
implementations are ordinary programs (VAPMIP/monad.py has well over a
hundred loops), so "no If/Then/Else, no While" is not a claim about the code.
The three phases are read as automatic in H = xp: the classical hyperbolic
trajectory (Red), the quantum zeros of the spectrum (Blue, "the prohibition"),
and the evolution e^{iHt} (the carrier waveform).

## 3. The "eddy current" argument  `analogy`

Earlier versions of this page described standard language models as "eddy
current machines": conditionals and loops as closed computational currents,
attention at O(n²), beam search as a loop, layer normalisation as iterative
correction, so that GPU clusters compensate for dissipation. That is an
analogy for the design goal (compute the address by evolution, not by search),
not a measured comparison. No measurement on this page compares the engine's
cost with a transformer's.

## 4. The capacitor

The ContextBuffer is modelled as a low-pass filter:

```
input language → 3-phase decomposition → ContextBuffer (capacitor) → DC component → output language
```

High-frequency variation (the particular words and syntax of one language) is
attenuated; the slowly varying component passes. The framework reads that DC
component as the semantic prime and the whole chain as an AC-DC-AC converter:
input AC = surface language, DC bus = the prime, output AC = the target
language re-modulated from it.

In code this is `Capacitor(tau)` with `charge(signal)` and `reset()`
(`SemanticWordEngine/semantic_engine.py`, `dc` field of `SemanticWord`) and the
cyclic context buffer in `PtolemyDesktop/Philadelphos/`. What it computes is a
smoothed value of the energy signal; that this value is language-independent
is the claim of [16](16_semantic_word_engine.md) §3, which the measurements
there do not support yet.

## 5. The 4 + 2 = 3 resonance  `interpretation`

A four-stroke engine with two-stage compression has 4 + 2 = 6 events per
720° cycle, 120° apart. The sixth roots of unity contain the third roots as a
subgroup (checked: the odd-numbered sixth roots all satisfy z³ = 1 or −1 as
expected, and every other one is a cube root of unity). Sampling the six events
at every other one gives exactly three-phase.

The mathematical statement, Z₃ ⊂ Z₆, is `ESTABLISHED`. The framework then
reads the recurrence of "three" in three-phase power, the three quarks of a
baryon, three colour charges, three spatial dimensions, and the Red/Blue/Carrier
split as one resonant form of any system with enough internal symmetry. That
is an interpretation; the occurrences are not derived from one another here.

## 6. Forward and backward flow

The three-phase engine is the outward expression of the Cayley–Dickson
counter-rotation ([19](19_cayley_dickson_tower.md) §4): Red flows up the tower
(ℝ → ℂ → ℍ → 𝕆, building), Blue flows down (𝕆 → ℍ → ℂ → ℝ, distilling), and the
Carrier is their interaction at the node lines.

## 7. Related pages

[14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) · [15 The Monad](15_the_monad.md) ·
[19 Cayley–Dickson tower](19_cayley_dickson_tower.md) · [21 Chladni · Zipf · Riemann](21_chladni_zipf_riemann.md)
