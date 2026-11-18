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
