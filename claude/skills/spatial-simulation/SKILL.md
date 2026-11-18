---
name: spatial-simulation
description: >
  Spatial awareness for rendering and simulation, one skill: the viewport model
  (2D pane = NES scroll window, 3D camera = OpenSCAD/Blender frustum), the human
  perception budget for showing n-dimensional maths, a Blender 4.x headless Python
  (bpy) recipe set, and the simulate -> export -> render pipeline for mapping
  established maths directly into pictures, animations and checks. Folds in
  nes-viewport and scad-spatial (both kept, now superseded by this skill).
  Load when: building or debugging a scrolling pane/scrollbar; designing a 3D
  model, OpenSCAD camera pose or Blender scene; choosing how to show a 4th+
  dimension; turning a calculation (potential, path family, field, lattice) into
  a render or turntable; scripting Blender from Python (`blender -b -P`); proving
  that a render frames the whole model; writing a simulator whose output is
  meant to be looked at. Built 2026-11-17 from the Witch's Hat simulator.
version: 1.0.0
---

# Spatial simulation: viewport, camera, Blender, and the maths behind them

One idea: a **viewport** is a fixed frame onto a scene larger than itself. The same
discipline (clamp, canonical poses, prove the whole scene passes through the frame)
governs a scrollbar, a CAD camera, and a Blender render. Simulations feed it: compute
first (numbers, tested), export plain data, render last (no maths in the renderer).

## 1. One model, three frames

| | 2D pane | 3D camera (OpenSCAD) | Blender camera |
|---|---|---|---|
| content | `cw×ch` map | scene bounding box | all objects in the scene |
| frame | `vw×vh` viewport | frustum (fov, near, far, aspect) | `camera.data` lens/sensor + render resolution |
| pose | offset `(ox,oy)`, clamped `0 ≤ o ≤ max(0, c−v)` | eye, target, up (`$vpr`, `$vpt`, `$vpd`) | `location` + `TRACK_TO` constraint on an empty |
| derived indicator | scrollbar thumb (never stored) | NDC `[-1,1]³` test after the w-divide | the pixel bounding box of the objects |
| canonical moves | home/end/page | front/top/iso poses | the same poses + one orbit |
| acceptance test | `assert_viewport_sound` (clamp, flush, thumb, sweep) | `assert_model_framed` (`assets/camera.py`) | render, then check the object bbox is inside the image and fills a sane fraction |

2D details (offset/clamp math, three layers, D-pad navigation, NES archetypes as test corpus,
Android and curses recipes, failure table): `references/nes_viewport-model.md`,
`nes_scroll-archetypes.md`, `nes_android-scrollbars.md`, code `assets/viewport.py`,
`viewport_demo.py`, `nes_scan.py`. Core rules: scrollbar geometry is derived from the offset,
never stored; clamp after every move; `max_oy = max(0, ch − vh)`; thumb
`len = clamp(round(T·vh/ch), MIN, T)`, `pos = round((T−len)·oy/max_oy)`; prove with
CLAMP / FLUSH / THUMB / SWEEP.

3D details (CSG, transforms, `$fn`, CLI camera, canonical `$vpr` poses, `projection`):
`references/scad_openscad-camera.md`, code `assets/camera.py`, `assets/hyperview.scad`,
`assets/render.sh`.

## 2. What a human can perceive (the budget)

Two 2D retinal images → about 2.5D. No native 4th spatial axis; a 4D object is a series of 3D
shadows or a stack of slices. Pick 3 axes for the frustum (the ones judged metrically); send
the rest through rotate / slice / project / encode / small-multiples under the budget:
**1** animated parameter; **2–3** colour/size/opacity channels; **~7±2** categories;
**≤ 5×5** small-multiples; **≤ ~4** depth layers without a scale cue. Always add a scale
reference (gnomon, box, known object). Orthographic to measure, perspective to see occlusion,
never both in one figure. Recipes and worked examples: `references/scad_nd-to-3d.md`.

## 3. Blender from Python (headless, Blender 4.x)

Run: `blender -b -P script.py -- ARGS` (everything after `--` is `sys.argv[sys.argv.index("--")+1:]`).
`import bpy` works only inside Blender's own Python (system python3 has no `bpy`); Blender ships
numpy, not scipy: **do the maths outside, export JSON/npz, read it in the script.**
Working example: `assets/blender_render_example.py` (the Witch's Hat scene).

Recipe set (all verified on Blender 4.0.2 in this environment):

| job | pattern |
|---|---|
| clean scene | `bpy.ops.wm.read_factory_settings(use_empty=True)` |
| mesh from a grid | `bmesh.new()`, `bm.verts.new`, `bm.faces.new`, `bm.to_mesh(me)`; `p.use_smooth = True` |
| mesh from arrays | `me.from_pydata(verts, [], faces); me.update()` |
| a path as a tube | `bpy.data.curves.new(n,"CURVE")`, `dimensions="3D"`, `bevel_depth=r`, `splines.new("POLY")`, `points.add(k-1)`, `points[i].co=(x,y,z,1)` |
| glow | Principled BSDF: set `Emission Color` and `Emission Strength` (4.x names; not "Emission") |
| translucency | `Alpha` input + `material.blend_method="BLEND"` |
| camera aim | empty at the target + `TRACK_TO` constraint, `track_axis="TRACK_NEGATIVE_Z"`, `up_axis="UP_Y"` |
| orbit | camera at `(d·cos el·cos az, d·cos el·sin az, d·sin el)`; step `az`; `render(write_still=True)` per frame |
| top view | elevation 89.5°, not 90° (a TRACK_TO singularity otherwise) |
| turntable video | frames to PNG, then `ffmpeg -framerate 24 -i turn_%03d.png -pix_fmt yuv420p out.mp4` |

Environment facts: this build has **no OpenImageDenoiser** (`use_denoising=False` or the run aborts);
use Cycles CPU (EEVEE needs a display); 48 samples at 1280×800 is a fair stills setting; long renders
go to the background. A scene of ~150 bevelled curves plus a 90×160 surface renders in about a minute.

## 4. The simulate → export → render pipeline

1. **Simulate** in plain numpy/scipy; print the numbers; every layer says whether it is
   ESTABLISHED (textbook/measured), THEORETICAL (the author's reading) or `:CALCULATED`.
2. **Test** against a closed form or a conservation law before any picture (the picture is not evidence).
3. **Export** only what the renderer draws (JSON/npz): geometry, per-point scalars, labels.
4. **Render** with no maths in the script except the height function; units of the object's own scale
   (e.g. brim radius = 1) so the figure holds for any size or depth.
5. **Frame check**: canonical poses + one orbit; the object fills the frame, nothing clipped, scale cue present.
6. **Label layers** in the figure caption and the README exactly as in step 1.

Worked instance: `FourthAgePapers/WitchesHat/simulator/` (`hat_sim.py` numbers; `export_paths.py`;
`render_hat.py`): the Standard-Model Higgs hat, Schrödinger ring states, Maxwell + hat (Nielsen–Olesen
vortex), classical paths and their abbreviated action, the author's cone.

## 5. Choice as camera steering

Picking the next element of a sequence can be treated as steering a path through a manifold:
score a candidate by curvature/jerk of the path, conserved invariants and silhouette continuity,
with frequency as the tie-breaker (details in the superseded scad-spatial note; `references/scad_nd-to-3d.md`).

## Extending

This skill is meant to grow rendering and simulation capabilities. Add new recipes to §3/§4 with
the Blender version they were verified on, and keep worked instances under the owning repo.
