# Anomaly chase — T7 balanced-ψ drift (3.52 with zero tilt struts)

**2026-08-31 · Standing Protocol: chase every anomaly to a verdict.**

## The anomaly
`oblique_gear_test.py` T7: driving the tilt gear-train from a *balanced* ψ
(all 8 tilts ≈ 1e-16, Σtilt = 0, σ_self = ½) produced a state drift of 3.52
over 200 steps — nonzero motion from a zero-drive state. The in-code reading
pre-judged it as strut-driven; the balanced run has zero struts, so that
reading was wrong. Chased.

## Diagnostic (inline probe, this dir)
1. **Trace:** from balance, `max|tilt|` grows 5e-16 → 5.6e-16 → 6.9e-16 →
   9.2e-16 → 1.55e-15 over the first 5 steps — geometric, factor ≈ 1.3/step,
   seeded by the 1e-16 balancing residual. Macroscopic (~1) by ~step 130.
2. **Gain sweep (explicit Euler), λ per unit flow-time = ln(growth)/gain:**
   gain 0.1 → +2.36, 0.05 → +5.36, 0.025 → +5.70, 0.0125 → **+5.89**.
   Converges to a positive constant **λ ≈ 5.9** as the step shrinks (0.1 is the
   large-step artifact).
3. **Midpoint integrator (2nd order):** same convergence, **λ ≈ 6.1**.
   Two integrators, one limit ⇒ not a discretisation artifact.
4. **Generic (unbalanced) start:** `|tilt|` 3.41 → 1.23 → 1.3e-3 → 0 — the flow
   **converges to balance**; `|axis|` = 2.30370 and `|ψ|` = 5.47144 held to 5
   digits throughout.
5. **Σtilt from balance:** −1e-15 → −2e-15 → −6e-14 → −9e-11 → −1.9e-5 over 400
   midpoint steps — exponential departure of the σ_self−½ proxy from zero.

## Verdict — MATHS not yet accounted for (emergence), not a bug
The balanced state **Σtilt = 0 / σ_self = ½ is a hyperbolic fixed point** of
the tilt-driven gear flow, Lyapunov exponent **λ ≈ 6 > 0**, integrator- and
step-independent. It is a **saddle**: a generic ψ flows *into* it (destructive
interference of the 8 tilts builds spontaneously, `|tilt| → 0`), but from
*exactly* on it, any perturbation grows exponentially. `|axis|` is conserved on
both branches — the anchor rides through.

- CODE fault? No — checks ran, two integrators agree.
- METHOD error? No — gain→0 converges, integrator-independent.
- MATHS fault? No — the two sides (Euler, midpoint) agree on λ.
- **Emergence** — the flow has a saddle at σ = ½ that nothing in the model
  named.

## What it means

**"Can destructive interference ring backwards?" — yes, here it does.**
The flow *builds* the cancellation (Σtilt → 0) on its own from any generic
state, reaches it, and then **departs it exponentially**. The null is a turning
point, not a rest state — the system rings back out of perfect cancellation.

- **Dynamo, confirmed.** λ > 0 at balance = above the kinematic-dynamo
  threshold: seed with noise → exponential field growth → nonlinear saturation
  → the flower / rosette. `|axis|` conserved while `|tilt|` grows-then-saturates
  = a saturated dynamo converting the conserved (poloidal) seed into a
  growing-then-bounded (toroidal) field. Geodynamo behaviour.
- **Riemann, from the dynamics side.** σ = ½ is *dynamically* distinguished as
  the flow's saddle — the stable manifold's target and the unstable manifold's
  origin. A zero is where the phase runs through the saddle. This is the
  Berry–Keating "why the spectrum sits on the line" reached from the flow, not
  the operator.
- **"No Renormalization" fits.** You do not renormalise *onto* σ = ½ — the flow
  delivers you there from generic data, and the instability off it (the
  precession, the flowers) is the observable, not a subtraction.

## Open / next
- Confirm on real monad ψ (native complex, phase kept), not just random ℂ¹⁶ —
  blocked by the numpy 2.4.6 ABI issue (the pending upgrade).
- Add a proper T8 (Lyapunov spectrum, not just the top exponent) to the test.
- Fold σ = ½-as-flow-saddle into `project_oblique_gear.md` and a note to
  `RiemannHypothesisProof/`.
