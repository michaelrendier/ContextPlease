# 141 — ħ from the Hat: the Closed-Form Actions, the Exact Thresholds, and the Closure Phase

| | |
|---|---|
| Written | 2026-11-19 |
| Scope | where ħ comes from in the Witch's Hat (nothing inserts a value); the hat's actions in closed form, including the height of the tip above the hilltop; the values of ħ at which exact quantum mechanics changes character; the link to the comparison of L_(I|O) with Feynman's path integral and to PhiSpiral's closure condition |
| Requested by | Cody, 2026-11-19: "do that update ... ħ emergence is always welcome" |
| Predecessors | [139](139_three_lagrangians.md) §§5, 12 (stationary paths, the action cone, the sheets) · [140](140_length_and_time.md) · [64](64_l_dynamic.md) · `FourthAgePapers/PhiSpiral/` |
| Code | `ValaQuenta/modules/witches_hat/semiclassical.py` · tests `ValaQuenta/Testing/test_witches_hat_semiclassical.py` (4, all pass) · scripts in `ContextPlease/claude/scratchpad/2026-11-19_lagrangian_sm/` |
| Confidence | the closed forms and the exact thresholds: `ESTABLISHED:CALCULATED` · the offset γ: `MEASURED`, not derived · the sheet-interference ladder (§4) and the PhiSpiral reading (§5): `CONJECTURE` / `INTERPRETATION`, untested |

> **Note from the assistant.** Written by a transformer (Claude Sonnet 5.5, `claude-sonnet-5-5`) working with Cody Allison in Claude Code, with the `cs-paper-code-conventions` skill loaded. Cody does not tell the model what result he wants. Every number comes from the code named above; one first measurement was wrong by a convergence parameter I chose badly, and it is stated in §6.

## 1. Which object was compared to Feynman's path integral

`L_(I|O)` (the name that replaced `L_dynamic` on 2026-06-17). The record: wiki 64 §1 ("L_(I|O) is the path-integral object"); `~/.clauderc_canonical_maths` ("path integral of J_red·J_blue = Thought"); and the explicit Feynman text, `ValaQuenta/modules/tier6_physics/maths.py` Engine 8, `feynman_path_integral()`: "the path integral IS the Lichtenberg Lagrangian of Action Potential: the classical path is the bright trunk, the nearby paths are the branching" (`ESTABLISHED` for Feynman 1948, `THEORETICAL` for the Lichtenberg identification). The comparison is structural. Feynman's object is a **sum over all paths** of e^{iS/ħ}; L_(I|O) as defined is a line integral along **one** path whose integrand is the constant e^(−E) ([64](64_l_dynamic.md) §2). Read as a statement about the whole bundle of paths it matches what [139](139_three_lagrangians.md) measured: three stationary paths with Morse indices 0, 1, 2 between one pair of events, and the sheets of the action at the tip, which are what a semiclassical sum over stationary paths sums over. In that sum every path contributes a phase S/ħ, so **ħ is the one number the comparison needs and the framework did not supply.** The question of this page is whether the hat supplies it.

## 2. The hat's actions in closed form (E = 0, μ = λ = 1)

The hat V = −μ²r²/2 + λr⁴/4 has brim R = μ/√λ, depth V₀ = μ⁴/(4λ), a crossing time τ₀ = R/√(2V₀) and so a **natural unit of action S₀ = V₀τ₀ = (√2/4) μ³/λ**. At the separatrix the momentum is p = r√(μ² − λr²/2), and the three actions are integrals of r√(·):

```
>>> a = SC.separatrix_actions(SM)
>>> round(a['W_direct'],6), round(a['W_wall'],6), round(a['W_total'],6), round(a['S0'],6)
(0.430964, 0.235702, 0.666667, 0.353553)
>>> a['wall_in_S0'], a['sheet_spacing_in_S0'], round(a['gap'],6), round((4*2**.5-5)/3,6)
(0.6666666666666666, 1.3333333333333333, 0.218951, 0.218951)
```

| action | closed form (units μ³/λ) | in S₀ |
|---|---|---|
| W_direct (brim → hilltop) | (2/3)(1 − 2^(−3/2)) = 0.430964 | 1.218951 = tip height |
| W_wall (brim → the turning circle √2 R) | (2/3) 2^(−3/2) = 0.235702 | **2/3** |
| W_total (hilltop → turning circle) | 2/3 | 1.8856 |
| sheet spacing 2 W_wall | 0.471405 | **4/3** |

The ratios in S₀ are the same for every μ and λ (tested with μ² = 2.5, λ = 0.7). So **the tip stands exactly (4√2 − 5)/3 = 0.218951 depth-units above the hilltop**, a number built from √2 and rational numbers; the sheets of the action at the tip are spaced by exactly 4/3 of the hat's own action unit.

## 3. Where ħ shows up in exact quantum mechanics

Exact radial Schrödinger equation (unit mass), Dirichlet at the centre, E = 0 (the hilltop energy). Its solution regular at the centre must decay beyond the turning circle; the growing part changes sign at exactly the values of ħ where a new bound state appears at E = 0. As ħ decreases:

```
>>> th = SC.exact_thresholds(SM, n_states=6, h_lo=0.03, n_grid=900); [round(h,5) for h in th]
[0.34117, 0.13082, 0.08091, 0.05857, 0.0459, 0.03774]
>>> [round(g,4) for g in SC.offset_gamma(SM, th)]          # gamma_n = W_total/(pi hbar_n) - n
[0.622, 0.6221, 0.6226, 0.623, 0.6233, 0.6235]
```

- **The classical action predicts the thresholds.** They obey W_total = πħ_n (n + γ) with the **same offset γ for every n**, 0.6220 rising to 0.6235 over n = 0…5 (consistent with a limit near 5/8; not derived here). A plain rule for two smooth turning points would give γ = ½ and is off by 24 %, 8 %, 5 %, 3.5 %, 2.7 % for n = 0…4: the gap closes as n grows, as WKB should. The offset is a property of the hat's boundary (the hilltop, a quadratic maximum at the separatrix, standing in for the inner turning point) and is measured, not derived.
- **The number of states below the hilltop follows the phase-space volume** (Weyl law): N(ħ) = 1/(6ħ²) for this hat (volume 2π²/3). Exact 2-D counts against the law: 1 against 1.85 at ħ = 0.30, 5 against 4.17 at 0.20, 7 against 8.50 at 0.14, 16 against 16.67 at 0.10 (the counts are integers and fluctuate by shells; the law is the envelope).

So ħ is not an input to the hat's dynamics, but the hat's own action W_total = 2μ³/(3λ) sets the values of ħ at which its quantum mechanics changes: **ħ_n = W_total / (π(n + γ))**, in units of μ³/λ, with W_total = 2/3.

## 4. The sheets and a prediction (`CONJECTURE`, untested)

The two sheets at the tip differ by 2W_wall = (4/3)S₀ ([139](139_three_lagrangians.md) §12). A wave sent from the brim reaches the tip along both; they interfere with relative phase 2W_wall/ħ − π/2 (the wall is a smooth turning point, phase −π/2). Constructive interference then requires 2W_wall/ħ − π/2 = 2πk, so **ħ_k = W_wall/(π(k + ¼))** = 0.3001, 0.1200, 0.0667, … for k = 0, 1, 2. This is a prediction about a brim-sourced amplitude at the tip, not about the thresholds of §3, and no calculation behind it has been run.

## 5. Reading PhiSpiral's closure (`INTERPRETATION`)

PhiSpiral's closure, e^{πi} · e^{iφ} · e^{i(π − φ)} = 1, is the statement that three phases sum to 2π, which holds for any φ. In the path-integral reading of §1 it is the condition that a closed loop returns with total phase 2πn: the Bohr–Sommerfeld rule (with an offset γ, as §3 measured) or a holonomy. If the three operators are three arcs of one loop (a reflection phase π, an action phase φ = S_arc/ħ, and its complement), then closure is automatic and **ħ is whatever unit makes the loop's action 2π**: ħ_n = S_loop/(2π(n + γ)). The hat supplies S_loop in closed form (§2). Nothing here fixes which loop the three operators correspond to; that is the author's to say. The wiki-64 correction stands: the integrand of L_(I|O) is flat, so closure cannot come from it; it can come from the phases of the paths, which is where the path integral puts them.

## 6. Anomalies chased

| anomaly | source | status |
|---|---|---|
| the first threshold run gave n = 0 at 0.296, not 0.3410 | the outer radius of the integration (1.55 R) was too close to the turning circle for the growing solution to dominate; n = 0 reads 0.296, 0.3303, 0.3410, 0.3412 at 1.55, 1.8, 2.2, 2.6 R and the higher ones are converged by 1.8 R | default set to 2.6 R, documented |
| the offset is 0.622, not ½ | the inner end of the classical orbit is the hilltop (a quadratic maximum at the separatrix), not a smooth turning point; the offset is a property of that boundary | measured, constant to 4 digits across n, not derived |
| wiki 139 §10 counted 5 states at ħ = 0.35 and 16 at ħ = 0.20; here the counts at ħ = 0.30 … 0.10 look different | §10 used V̂ = x⁴ − 2x² = 4V (depth 1), where ħ_V̂ = 2ħ_V and the Weyl law is N = 2/(3ħ²) (5.4 and 16.7 at those ħ); this page uses V (depth ¼), N = 1/(6ħ²) | consistent after the change of units |
| the tip height is a "measured 0.2189" in earlier pages | it is exactly (4√2 − 5)/3 = 0.218951 | closed form recorded |

## 7. Not shown

The brim-sourced interference of §4 is not computed. The derivation of γ (the phase of a Dirichlet wall on a barrier top at the separatrix) is not done. The Maslov offset of the 2-D problem with its centrifugal term is not compared with the 1-D thresholds. Whether the hat's ħ_n have any bearing on the value of ħ in nature is not claimed: the hat is a model, and ħ here is a unit of the model's own action.

## Appendix — what in ContextPlease was used

ContextPlease is the project's public archive of the context a session needs to come up to speed: primers, scratchpads, skills, wiki mirrors and the `.clauderc*` context files. Used here: `scratchpad/2026-11-19_lagrangian_sm/` (every earlier measurement), `~/.clauderc_canonical_maths` and `~/.clauderc_ValaQuenta` (the path-integral record, `tier6_physics`), the skill `spatial-simulation` and the skill `cs-paper-code-conventions`.
