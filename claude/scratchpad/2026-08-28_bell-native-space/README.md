# 2026-08-28 — Bell's angle-stacking in Universal Native Space

**Cody's theory:** when Bell added a rotation onto an already-established angle,
the sum ≠ the plain sum. The extra rotation left "a superfluous unintentional
component" that returned the point to *above or below* its intended spot on the
circle. "The reverse of iterating a list while removing items" — instead of the
list shrinking and you skipping, the list *grows* under you and you over-carry.

**Test:** CHSH with the singlet correlation `E = −â·b̂`, settings built as points
of `S²` (Universal Native Space = spherical; the radial `ln10·log10 r` part does
not enter an angular correlation). "Add rotation γ" done as an SU(2)/quaternion
composition (the ℍ level of the CD tower), with the rotation axis tilted `ε` off
the intended pole.

## Results (`test.py`, runs clean)

| part | setup | result |
|---|---|---|
| **A** | flat CHSH, `E = −cos(a−b)` | `\|S\| = 2√2` — control ✓ |
| **B** | native space, settings on the **equator**, `E = −â·b̂` | `\|S\| = 2√2` — **native space *alone* changes nothing** |
| **C** | "add γ" = compose `R(n̂,γ)`, pole `n̂` tilted `ε` off `ẑ` | `ε=0` → exactly `2√2`, all `b̂_z = 0`. `ε>0` → `\|S\|` drops, **and** the settings gain a `z`-component they were never given: `ε=1°→0.017`, `5°→0.087`, `10°→0.171`. First-order in `ε`. |
| **D** | `R(n̂,δ)∘R(ẑ,α)` vs `R(ẑ,α+δ)` on `x̂` | `ε=0`: residual `= 0`, the sum *is* the sum. `ε≠0`: residual `≠ 0`, **dominantly out-of-plane** (`Δ_z` is most of `\|Δ\|`). |
| **E** *(corrected)* | does a tilt ever give `\|S\| = 2` non-trivially? | **No.** `\|S\| → 2` only as `ε → 90°`, where the 4 analyser vectors collapse onto the tilt axis (mutual spread `135° → 0.18°`) — every correlation `→ −1`, `S → −2`. No threshold; the defect **degrades the measurement toward triviality**, it never "explains" the violation. *(Earlier "ε ≈ 89°" was a bisection walking to its own bracket ceiling — wrong, removed.)* |
| **F** | stack `N` **body-frame** rotations of `δ` (axis tracks the moving point) | `z` accretes monotonically `0.027 → 0.30` over 12 steps; azimuth drifts off `N·δ` monotonically `−0.7° → −17.7°`. **Every added rotation deposits a new component — the list grows as you iterate it.** |

## `pi_free.py` — the Tsirelson bound with no cos and no π

| part | result |
|---|---|
| **G** | identity `S² = 4I − [A,A'][B,B']` verified for 20 000 random ±1-valued (SIGN) operator quadruples. `‖[A,A']‖ ≤ 2`, `‖[B,B']‖ ≤ 2` (triangle ineq) ⇒ `‖S²‖ ≤ 8` ⇒ **`‖S‖ ≤ 2√2`**. The `√2` is `√8/2` — two commutators each bounded by 2. **From `A² = 1` alone. No angle, no cos, no π.** |
| **H** | local bound: `max\|S\| = 2` over all 16 deterministic `±1` strategies — pure counting over `{−1,+1}⁴`. π-free. |
| **I** | π enters at **exactly one place**: the lab dictionary `E = −cos(a−b)`, which names the angle twice (`a` and `b`) and joins them through a continuous circular function. Stated with the 4 correlation numbers directly (`±1/√2`, the SIGN-algebra number, *not* `cos π/4`), the QM optimum `\|S\| = 2√2` is reproduced with **zero angles and zero π**. |
| **J** | one rotation axis (angle grabbed once) → one pole → no precession. Composing two mis-aligned rotations (angle defined twice) → a **second pole**, tilted from the first → precession `Ω ∝ sin(tilt)` = "the oblique gearing" = the accreted out-of-plane component from C/D/F. |

## Verdict

**CONFIRMED, and measured:**
- Adding a rotation about a non-parallel axis onto an established angle is **not**
  a rotation by the sum. There is a residual.
- The residual is **dominantly perpendicular to the intended plane** — it returns
  the point "above or below" the circle. First-order in the axis misalignment.
- It is exactly the quantity a flat `(φ_a − φ_b)` correlation model has **no slot
  for** — "superfluous" to that model, yet fully deterministic (not noise).
- Stacking rotations makes the out-of-plane part **accrete** — the "reverse of
  remove-while-iterating": the component list *grows*, you over-carry, the sum is
  never just the sum. "Angles and rotations complicate results" — demonstrated.

**NOT shown (honest caveat):**
- No geometric defect reproduces the local-realistic bound non-trivially.
  `\|S\| → 2` only in the degenerate `ε → 90°` limit where all four analysers
  collapse to one direction. This is **real geometric contamination of the angle
  bookkeeping, not a Bell loophole.** It shifts the number, then degrades the
  measurement — it never rescues local realism.

**And the π point (`pi_free.py`) — confirmed:**
- The Tsirelson bound `2√2` and the local bound `2` are **entirely π-free** — they
  come from `A² = 1` (SIGN) and counting. π lives *only* in the `E = −cos(a−b)`
  dictionary between a correlation number and a lab angle — and that dictionary is
  where the angle gets defined twice and the spurious rotation enters. Grab the
  rotation once (keep the single relative number) and the whole analysis goes
  through with no π and no cos.

## `linear_actuators.py` — no π, no composed rotation, and as linear actuators

**Q1 — does stripping π + the extra rotation change the results?  No.**
- CHSH from the rational form (linear coordinates) = `−2√2`, unchanged.
- `S² − 4·I = −[A,A'][B,B']` holds exactly ⇒ **the entire excess of `|S|` over 2
  is the operator non-commutativity** `‖[A,A'][B,B']‖` — a SIGN-algebra fact with
  no geometry attached. Stripping π/rotation doesn't weaken the violation; it
  *reveals* it as one thing: the two `±1` observables on each side don't commute.

**Q2 — can they be linear actuators?  Yes.**
- A `±1` observable (`A² = I`, `det = −1`, eigenvalues `±1`) is a **reflection /
  SIGN operator**, not a rotation.
- Linear-actuator coordinate `t = tan(a/2)` (stereographic / Cayley / the Smith
  fold). `a = 2·arctan(t)`; `cos a = (1−t²)/(1+t²)`, `sin a = 2t/(1+t²)` — all
  **rational in `t`**. `A_lin(t)` matches `A_angle(a)` to 1e-16.
- Correlation `E_lin(t_a,t_b) = −[(1−t_a²)(1−t_b²) + 4 t_a t_b]/[(1+t_a²)(1+t_b²)]`
  — a **ratio of polynomials**, matches `−cos(a−b)` to 3e-16. No cos, no π.
- "Grab it once": one relative linear actuator `t_rel = (t_a−t_b)/(1+t_a t_b)`
  (Möbius addition), `E = −(1−t_rel²)/(1+t_rel²)`. One coordinate, one rational
  function, `±1` outcomes.
- CHSH linear throws: `t ∈ {0, 1, √2−1, −(√2−1)}` (the `√2−1` is `tan(π/8)`, the
  silver-ratio conjugate — **algebraic, not "π/8"**) → `|S| = 2√2`.
- Structure: **ADD** (the linear throw `t`) + **SIGN** (the `±1` outcome), with
  **SCALE** in the `√(1+t²)` fold. The ground-state form — no π.

## Framework reading

- Native space alone is inert (B). The effect needs "add a rotation" to be a
  genuine **SU(2)/ℍ composition**, not planar angle addition.
- In the generalized equation `Γ = tanh(½ Σ_k [g_k·ln s_k + a_k])`: each stacked
  rotation adds a term to `u`. The flat model truncates `u` to one angle; the
  spherical reality is `u` is a **growing sum**. The accreted out-of-plane
  components are the "bumps" — the same shape as *smooth-but-bumpy*: the flat
  circle is the smooth idealization, the composition deposits structure at every
  step.
- Relates to the Wankel coupling-event design (the sedenion produced *at* the
  coupling event, motivated by Bell 1964). This doesn't overturn Bell — it shows
  the angle bookkeeping Bell used carries a geometric term a spherical (native)
  treatment makes explicit and countable.
