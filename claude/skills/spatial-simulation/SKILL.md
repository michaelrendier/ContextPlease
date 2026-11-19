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
  meant to be looked at; anything in Minkowski spacetime (light cones, worldlines,
  boosts, the path of action, Wick rotation); any of the other spaces (De Sitter, Hilbert,
  Fano plane, sedenion space with bracketing and firing order, Mandelbrot-Julia, gauge space =
  orthogonal Smith charts / Apollonian gasket, equation space, the Higgs field space) and anything
  whose axes are not lines but hypercomplex fields; rendering the bundle of paths of a
  Lagrangian on the hat. Built 2026-11-17 from the Witch's Hat simulator; Minkowski recognition
  added the same day; spaces and the v2.0 rendering rules added 2026-11-19.
version: 1.2.0
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
`references/scad_openscad-camera.md`, code `assets/camera.py`, `assets/minkowski.py`, `assets/hyperview.scad`,
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

## 6. Minkowski space (the action lives here)

The Lagrangian, the action and the Standard-Model fields are Lorentzian: the viewport is **pseudo-Euclidean**. Signature (−, +, +): s² = −(c dt)² + dx² + dy². Use `assets/minkowski.py`.

| Euclidean viewport (§1) | Minkowski viewport |
|---|---|
| distance, preserved by rotations | interval s², preserved by **boosts** (hyperbolic rotations, rapidity η = atanh(v/c)) |
| frustum (a cone around the view axis) | the observer's **past light cone**: what is seen is on or inside it (`past_cone_viewport`) |
| pose = eye position + orientation | pose = an event + a unit timelike 4-velocity; changing the frame is a boost |
| "same distance" = a circle | "same interval" = a hyperbola; null (s² = 0) = the 45° lines |
| a model point is in frame or not | an event pair is **timelike / null / spacelike**, and that class is frame-independent (`classify`) |
| straight line = shortest | a free worldline **maximises** proper time τ; τ ≤ t always (`worldline`) |
| slice at constant z | **simultaneity slice**: tilts with the frame, t = t₀ + vx/c² (`simultaneity_slice`) |

Rules for a Minkowski render:
1. Plot **ct** (same units as x) so the light cone is exactly 45°; scale them differently and the cone lies.
2. The null cone of an event is the **hat** of `Ainulindale/wiki/29`: tip = the event, surface = the null geodesics, brim = where a constant-time slice cuts it (`light_cone`).
3. Never draw a Euclidean circle where an invariant hyperbola belongs; never draw a worldline outside the cone (`worldline` raises if v ≥ c).
4. Simultaneity is not absolute: two events on one horizontal line in one frame are not in another. If a figure shows "at the same time", name the frame.
5. 3D with time: (x, y, ct) with ct vertical; a boost shears/tilts the slices, it does not rotate the picture.
6. **Wick rotation** t → −iτ turns signature (−, +, +) into (+, +, +): a Lorentzian path in V becomes a Euclidean path in **−V**. For the Mexican hat the brim (the minimum of V) is the crest of −V and the hilltop is its bottom: a particle released at rest inside the brim rolls to the hilltop in finite Euclidean time with speed √(2·depth) (the bounce / instanton path from the brim to the point). `euclidean_path` computes it; the Lorentzian paths of the Witch's Hat engine are the other half of the same picture. Render them as two layers, labelled Lorentzian and Euclidean, never mixed.

Acceptance test, `assert_minkowski_sound()`: the interval is invariant under boosts (v = 0.1, 0.6, 0.95); a light ray stays null after a boost; the causal class is frame-independent; proper time never exceeds coordinate time; the ring of a past light cone is visible from its apex; slices tilt with velocity. All six hold (2026-11-17).

Layers for QFT-faithful renders: (1) the semiclassical paths (stationary phase of the path integral): Lorentzian paths in V on the Minkowski diagram; (2) the Euclidean paths in −V (instantons/bounces); (3) for a true field theory, the field configurations on a lattice in Euclidean time, with the weight e^{−S_E}. Say which layer a picture is.

## 7. Other spaces, and axes that are fields (2026-11-19)

A space is described by eight things: points · axes · motions · invariant · views · acceptance test · repo engine · status. The central rule: **an axis is (algebra, field, view), not a line**. A coordinate may be a complex number, a quaternion, an octonion or sedenion, a function over another space, or a pencil of circles; declare which real components are shown and how the rest enter (colour, slice, small-multiple, time). Each costs viewer budget: ℂ two real axes, ℍ four, 𝕆 eight, 𝕊 sixteen (§2). Pair with `observer-position`.

| space | axes | motions | status |
|---|---|---|---|
| Minkowski (§6) | ℝ | boosts | ESTABLISHED, asset |
| De Sitter | ℝ embedding, or (t, r) patch | SO(1,n), dilation | ESTABLISHED, recipe |
| Hilbert | ℂ amplitudes; functions in L² | unitary U(n), projection | ESTABLISHED, recipe |
| Fano plane | none (7 points, 7 lines) | PSL(2,7), order 168 (measured) | ESTABLISHED |
| Sedenion (+ bracketing, firing order) | 16 algebra units; bracketing is state | multiplication order | ESTABLISHED + engines `emerger`, `bracketing_firing_order`; 84 zero divisors measured |
| Mandelbrot–Julia | two ℂ planes (c and z) | iterate, travel in c, zoom | ESTABLISHED, recipe |
| Gauge space (orthogonal Smith charts, Apollonian gasket) | two orthogonal pencils of circles | Möbius group, z → 1/z, scale | RECORD + AUTHOR |
| Equation space (σ = 0 permutation space of 0_RB) | operator slots, hypercomplex | re-bracket, re-order | STUB |
| Higgs field space (the hat) | ℝ⁴ ≅ ℂ², O(4); brim = S³ | classical paths, time-dependent hat | ESTABLISHED, engine |

Full entries, measured facts and the repo engines: `references/spaces.md`. Rendering rules settled in use (show the maths exactly; one natural vertical scale; report the tip number; cutaway views; size budget; versioned names kept with the paper): `references/spaces.md` §10.

## Extending

This skill is meant to grow rendering and simulation capabilities. Add new recipes to §3/§4 with
the Blender version they were verified on, and keep worked instances under the owning repo.
