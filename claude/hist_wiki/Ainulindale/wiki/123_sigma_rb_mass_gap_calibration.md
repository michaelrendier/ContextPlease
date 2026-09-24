# 123 — σ_RB Mass Gap Calibration: Three Sigmas, and What Doesn't Conflate

**Measured 2026-09-23.** Cross-tests `ValaQuenta/bao_mass_gap.py` against
`ContextPlease/claude/scratchpad/2026-08-31_oblique-gear/oblique_gear_test.py`
for the first time. Continues [[50_bao_mass_gap_engine]], [[14_redblue_hamiltonian]],
[[25_sedenion_manual]]. Every number below is computed and checked against
the actual code, not asserted.

---

## The problem this page exists to prevent

"σ" names three different objects in this codebase. Each is correct in its
own file. The risk is carrying a result computed in one of them into a
sentence about another.

| Name | Where | What it is |
|---|---|---|
| **σ_ζ** | `ValaQuenta/modules/h_rb_hat/maths.py`, `sigma` parameter | Re(s), the Dirichlet/Euler coupling exponent. A single float. Facets: 0, ½, 1, 2, real-only — [[14_redblue_hamiltonian]]'s table. **No string/M-theory facet at this level.** |
| **σ-strata** | [[25_sedenion_manual]] §IX, `σ₀..σ₄` | Ordinal *nested-inclusion* levels of the sedenion — how many of the 16 components are switched on — not a continuous coupling exponent. `σ₄` = all 16 active = "String / ground state." |
| **σ_RB** | `oblique_gear_test.py` | `σ_RB[k] = ψ[k]·conj(ψ[k⊕4])`, `ψ∈ℂ¹⁶`. `tilt=Re` (8-vector, driven), `axis=Im` (8-vector, conserved anchor). `σ_self = ½ + Σtilt/(red+blue)` is a **separate, derived** scalar built *from* σ_RB, not σ_RB itself. |

Where "mass gap → string theory" already lives in this framework: it's
§VII of [[25_sedenion_manual]], at the σ-strata level, not the other two.
`GAP = e₁₅ component → ZD boundary → 7 imaginary octonion units → G₂
holonomy → 11D = 4 observable + 7 compact → M-theory, one vacuum.` That's
the *same chain, same 11=4+7, same G₂=Aut(𝕆)* as
`bao_mass_gap/maths.py`'s `mtheory_compactification()`. It is a
**compactification-scale argument** — Δ sets a geometric scale — not a
σ-facet assignment. Keep this distinction; it's the whole point of the
page.

---

## The calibration test

Forward propagation, not derivation: push Δ = 0.000707357533 (`bao_mass_gap.py`'s
Yang–Mills/BAO residue, computed independently from `Ω_ζΣ − D*·ln10`) into
σ_RB's real part as the mean tilt across all 8 struts, and read what the
operator's own established relations say about it. Δ is not derived here —
it's typed in, and what's tested is whether the machinery accepts it, and
what it does once accepted.

`Re(σ_RB) = tilt = Δ` on all 8 struts, exactly, by construction. Not a
finding — that's the input.

**σ_self is provably strut-blind**, once each pair's energy is held fixed
at a constant `E` (exact algebra: `red=4E+Σtilt`, `blue=4E−Σtilt`, so
`red+blue=8E` regardless of how tilt is distributed across the 7 struts):

```
σ_self = ½ + mean(tilt)/E = ½ + Δ/E
```

Verified to 12 digits against the running code, struts swept up to 16×Δ's
own scale — `σ_self` unchanged at every point. At `E=1`: `σ_self =
0.500707357179`, landing deep in the **σ_ζ = ½ (Quantum Mechanics /
Riemann)** facet, nowhere near string theory. This is the correct,
consistent result: the string/M-theory route belongs to the σ-strata /
compactification mechanism above, and doesn't emerge from feeding Δ into
σ_RB's tilt. If an M-theory-flavored read of "mass gap → σ_RB" shows up
elsewhere, it's very likely using the established compactification route,
not this one — they should not be merged into a single claim.

## A real correction, filed against T7

`oblique_gear_test.py`'s own T7 docstring claims drift tracks the 7 tilt
struts only — "the axis holds," mean doesn't matter. Measured otherwise:
same struts, three means, 200-step `gain=0.05` gear-train run:

```
mean=Δ    drift=3.6640
mean=0    drift=3.9194
mean=−Δ   drift=3.9303
```

The mean visibly moves the drift. Asymmetric in `±Δ`, and outside an
8-sample same-scale control's spread (`0.006`–`0.04`). **OPEN** — not yet
distinguished from ordinary chaotic sensitivity of a 200-step nonlinear
iterated rotation versus a genuinely Δ-specific effect. Needs many more
trials, or a proper local-sensitivity/Lyapunov measurement, before either
verdict is earned.

## The rectifier law — a leak, chased to its exact closed form

An earlier, energy-unnormalized embedding (`ψ[k]=ψ[k⊕4]=√|tilt_k|`,
signed) let strut information leak into `σ_self`. Flagged as an anomaly
per the standing chase-every-anomaly discipline rather than dismissed as
noise, and it resolved to an exact, derivable law:

```
σ_self = ½ + 4Δ / Σ_k |Δ + λ·u_k|
```

(`u` a fixed unit strut direction, `λ` the strut scale.) Verified exact to
12 digits against the code at 13 values of `λ` from `10⁻⁶` to `10⁵`. Two
sharply divided regimes:

- **Below the first sign-flip threshold:** `σ_self = 1.0` exactly, flat —
  the struts are completely invisible (no cancellation in `Σ|t_k|` while
  every `Δ+λu_k` still shares Δ's sign).
- **Above threshold:** log-log regression on the decay gives slope
  `−0.9985` — an exact **inverse-first-power** law, `dev ∝ λ⁻¹`, matching
  the closed form's own large-`λ` asymptote exactly. Tested against, and
  ruled out: inverse-square.

## Status

**OPEN / THEORETICAL.** This is an ad hoc cross-test between two existing
scripts (`bao_mass_gap.py`, `oblique_gear_test.py`) — neither is wired
into ValaQuenta's `EquationModule`/engine formulary, so nothing here earns
`:CALCULATED` (that suffix requires the machinery to reproduce a result
from its own construction, not accept an injected input unchanged).

**Solid:** the strut-blindness of `σ_self` (exact algebra, verified
numerically); the rectifier's inverse-first-power law (exact derivation +
verified fit).

**Open:** whether T7's mean-sensitivity is Δ-specific or generic chaotic
noise; whether σ_RB has any principled, non-injected route to *producing*
Δ rather than merely accepting it without contradiction.
