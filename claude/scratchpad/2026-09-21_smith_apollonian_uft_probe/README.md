# 2026-09-21 — Smith chart ⊥ Apollonian gasket: can it derive 0_RB?

Cody's question: does the continuous (Smith)/discrete (Apollonian) split
in `GenerationalLineage/engine/toolsets/scale.py` — already flagged in
that file's own docstring as untested ("matter/energy is the tilt
between the two axes — not computed at this layer. A later pass chases
whether it is more than that.") — reproduce or derive `∅_RB`'s structure?

**Answer: not shown, and the one existing test that looked like it might
(`sedenion_locus_orthogonality()`, METHOD verdict) was answering a
different, weaker question than the one actually asked.** Five scripts,
run live, in order:

1. **`01_complex_smith_chart.py`** — `scale.py`'s `charts()` only ever
   takes real `s`, confining `Gamma(s)=(s-1)/(s+1)` to a 1-D slice of the
   disk. Run on the PROPER coordinate (complex `s=sigma+i.t`, the actual
   zeta argument): `|Gamma(s)|=|Gamma(1-s)|` holds **exactly, and only,**
   at `sigma=1/2` — confirmed by direct sweep, not spot-check. Traced to
   the algebra: forced by `Gamma`'s own fixed points at `{+1,-1}`, nothing
   about zeta enters. A second, independent `sigma=1/2`, not the same
   mechanism as zeta's functional equation, landing on the same number.
2. **`02_apollonian_own_half.py`** — does the gasket have its own,
   independent `1/2`? Three candidates tested: (a) the seed's curvature-2
   circles have radius 1/2 — real but **definitional**, an artifact of
   the chosen seed `(-1,2,2,3)`, not emergent (Ideal Principle: a
   different valid seed gives a different radius, no 1/2 in it). (b) the
   Hausdorff-dimension formula `lambda_0=delta(2-delta)`'s own reflection
   symmetry centres at **delta=1, not 1/2** — genuine, checked, negative.
   (c) Ford circles/Farey mediants do have a native 1/2, but that's an
   *unbounded strip packing*, a different object from `scale.py`'s
   *bounded* seeded gasket — doesn't transfer. **No independent Apollonian
   1/2 found.**
3. **`03_gasket_generation_address.py`** — built the genuine 2-D discrete
   address `scale.py` never had: `(generation, move_index)`, a real word
   in the Descartes-move generators, replacing the old 1-D "nearest
   curvature by magnitude."
4. **`04_orthogonality_at_the_half.py`** — the direct test. Feeding
   `|Gamma(s)|` into the new discrete address does show symmetry about
   `sigma=1/2` — but it's **inherited**, not independent (the discrete
   side was driven by Smith's own already-symmetric output). Checked the
   discrete side entirely on its own terms (no `Gamma` involved at all):
   no reflection structure exists on `(generation, move_index)` — moves
   aren't paired by any involution, generation only increases. **The two
   `1/2`s do not independently coincide** — there is one `1/2` here
   (Smith's, separately echoed by zeta's own, `half_is_the_equator.py`,
   re-verified this pass), not two meeting in the middle.
5. **`05_curvature_vs_potential.py`** — the Mexican-hat framing, checked
   piece by piece. Smith's `Gamma` is a Möbius map: Schwarzian derivative
   **exactly zero** everywhere (confirmed numerically to float precision)
   — it carries no curvature in the classical/gauge (`F_munu`) sense;
   `local_scale_factor=|dGamma/ds|` is a conformal/metric scale factor,
   one derivative short of true curvature. The gasket's curvature ladder
   is a discrete spectrum (mass-like), not a continuous potential well;
   the complex-Descartes theorem's `+-` gives an genuine but **discrete
   Z_2** choice of centre at fixed curvature (top gap/bottom gap), not a
   continuous U(1) Mexican-hat vacuum circle. The analogy is directionally
   sound (curvature↔quantized/radial, some discrete choice↔symmetry
   breaking) but the continuous-U(1)-Higgs version specifically doesn't
   structurally fit without more work.

## What this does and doesn't settle

**Does not close the door on the underlying hypothesis** — it closes the
*specific* claims tested (a shared `1/2`; literal gauge curvature; a
continuous Mexican hat). **What's still genuinely open and untried:**
`scale.py`'s own named-but-unbuilt quantity, the **tilt** between the two
charts at a fixed `s` — not their shared fixed point, their *difference*
— checked against whether that difference has `∅_RB`'s actual shape
(`R_p ⊗ ∂_∂M + h.c.`, self-adjoint by construction, forced to `sigma=1/2`
by a Noether-style balance `|J_red|=|J_blue|`, not by either chart's own
fixed points). Not attempted this pass.

## Files

- `01_complex_smith_chart.py`, `02_apollonian_own_half.py`,
  `03_gasket_generation_address.py`, `gasket_addresses_lib.py` (shared
  functions for 04), `04_orthogonality_at_the_half.py`,
  `05_curvature_vs_potential.py` — run in order, each self-contained,
  real output above and in-terminal.

## Related

`GenerationalLineage/engine/toolsets/scale.py`,
`GenerationalLineage/wiki/The-Two-Charts-and-Jurisdiction.md`,
`ContextPlease/claude/scratchpad/2026-08-13_apex_path/half_is_the_equator.py`
(re-verified this pass, all four of its own T1-T4 checks still hold),
`.claude/.clauderc_canonical_maths` (`0_RB` definition, gauge-curvature
section).
