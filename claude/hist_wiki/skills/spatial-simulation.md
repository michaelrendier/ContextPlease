# spatial-simulation

**Skill:** `~/.claude/skills/spatial-simulation/` · mirror `ContextPlease/claude/skills/spatial-simulation/`
**Created:** 2026-11-17 · **Requested by:** Cody Michael Allison (Michael Rendier): "fold both the 2D and 3D spatial awareness skills into a single skill meant for simulations and Blender renderings ... it will get additional rendering and simulation capabilities later; its purpose is spatial awareness in rendering; one toolset is Blender."

## What it is
One viewport model for three frames (a 2D scroll pane, an OpenSCAD camera, a Blender camera), the human perception budget for showing n-dimensional maths, a headless Blender 4.x Python recipe set (verified on 4.0.2: Cycles CPU, no OpenImageDenoiser in this build), and the simulate → export → render pipeline (maths outside Blender, plain JSON in, no maths in the renderer except the height function).

## Folded in
`nes-viewport` (2D pane, NES archetypes) and `scad-spatial` (3D camera, edges and angles, x,y,z,t). Both originals are kept untouched; their descriptions point here. Their assets and references are copied into the new skill (`nes_*` and `scad_*` prefixes).

## Worked instance
`FourthAgePapers/WitchesHat/simulator/` (branch `witches-hat`): `hat_sim.py` (Standard-Model Higgs hat, Schrödinger ring states, Maxwell + hat vortex, classical paths and abbreviated action), `export_paths.py`, `render_hat.py`.

## Facts recorded from use
- `import bpy` only works inside Blender; run `blender -b -P script.py -- args`.
- The Blender here has no OpenImageDenoiser: `use_denoising = False`, else the run aborts.
- Top-down camera at elevation 90° is a TRACK_TO singularity; use 89.5°.
- Never `pkill -f` / `pgrep -f` a pattern that appears in the shell command that runs it (it kills the shell, exit 144).

## Update 2026-11-17: Minkowski recognition (author: 'the action lives in Minkowski space')
Added `assets/minkowski.py` and SKILL.md §6: signature (−,+,+), boosts, light cones (the null cone is the Witch's Hat), worldlines and proper time, simultaneity slices, the observer's past-cone viewport, Wick rotation to Euclidean paths in −V (brim to hilltop in finite Euclidean time, speed √(2·depth)), and `assert_minkowski_sound()` (six checks, all pass). Three layers for QFT-faithful renders: semiclassical Lorentzian paths, Euclidean instanton paths, lattice field configurations; every picture says which.

## Update 2026-11-19: spaces, axes that are fields, and the v2.0 rendering rules (v1.2.0)
Requested by Cody: add De Sitter, Hilbert, Fano plane, sedenion space with the bracketing and firing-order engines, Mandelbrot–Julia, gauge space, equation space; "they all have different movements, different axes ... the axes are not lines, they are hyper-complex fields." New: `references/spaces.md` (each space: points, axes, motions, invariant, views, acceptance test, repo engine, status) and SKILL.md §7. Central rule: an axis is (algebra, field, view), and each algebra dimension costs viewer budget (ℂ 2, ℍ 4, 𝕆 8, 𝕊 16).
- **Gauge space**, as Cody defined it: the Scale engine's orthogonal Smith charts, Γ_SCALE = tanh(½ ln s) ⟂ Γ_ADD = tanh(½ a), the Apollonian gasket as the same Möbius-group object ("the complete shape of scale", "a type of gauge theory space"). Record: `add_scale_sign` `.to_smith()`, `three_ring_scale`, SFR wiki PW8–PW9, citable-work index (Sullivan's dictionary). The word "gauge" is not in `scale/maths.py`: the gauge reading is the author's.
- **Equation space**, as Cody defined it: the permutation space of all equations possible from 0_RB; explored in Ainulindale wiki 19 (σ = 0, the infinite permutation space), the Emerger's `scale_partitions`, the Generational Lineage chrono/zeta orderings. Status STUB: nothing implements it; the next rigorous test after the Fourth Age papers.
- Measured with the repo's own code: Fano plane 168 collineations; sedenion 84 zero divisors over 42 index pairs (none in the octonions); Smith-chart circle pencils orthogonal and parabolic (all through Γ = 1); Mandelbrot landmarks; de Sitter interval invariant.
- **Minkowski in the Standard-Model engine:** not there (η appears only in two comparison helpers). The engine's Lorentzian action is the homogeneous mode of the Minkowski action; Euclidean = Wick rotation, motion in −V. Recorded so it is not assumed again.
- **Rendering rules (§10 of the reference), from WitchesHat Lagrangians v2.0:** show what the maths says, never draw to resemble a picture; integrate the whole family and select by outcome; one natural vertical scale (energy in V₀, action in V₀τ₀, τ₀ = R/√(2V₀)); report the tip number; cutaway views; polyline chunks (files ≤ 5 MB); versioned names kept with the paper (`FourthAgePapers/WitchesHat/papers/figures/lagrangians/vX.Y/`).

