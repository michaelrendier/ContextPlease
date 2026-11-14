---
name: scad-spatial
description: >
  3D spatial-awareness methodology: the camera as the viewport onto a scene
  larger than the frustum, the OpenSCAD language of edges / transforms / camera
  angles in x,y,z,t, and a disciplined method for designing visualisations of
  higher-dimensional maths within the hard limits of human 4D-spacetime
  perception (one 2D retinal image ×2 → ~2.5D reconstruction; no native 4th
  spatial axis). Load when: designing or critiquing a 3D / CAD / OpenSCAD model
  or a camera pose; choosing how to show a 4th spatial dimension (rotate / slice
  / project / encode); deciding which axes of an n-D dataset get the frustum and
  which get colour / time / small-multiples; reasoning about occlusion and what
  a viewer can actually see; framing "which next element" as steering a camera
  through a manifold rather than reading a frequency table.
---

# 3D SCAD spatial awareness — the camera is the viewport

The 3D camera is the exact analogue of the 2D pane in `nes-viewport`: a fixed
frame onto content larger than it. Same discipline — clamp, canonical poses,
prove the whole thing passes through the frame — plus the language of edges and
angles, and the projection from n dimensions down to what a human eye can build.

## 1. The camera = the viewport

| 2D pane (`nes-viewport`) | 3D camera |
|---|---|
| content `cw×ch` | scene bounding box `[min..max]³` |
| viewport `vw×vh` | view frustum (near/far, fov, aspect) |
| offset `(ox,oy)` clamped | pose: eye **e**, target **t**, up **u** — clamped to keep the model in frame |
| map→screen translate | model → view → clip → NDC → screen (`multmatrix` chain) |
| scrollbar (derived) | the framing indicator: is every model vertex inside NDC `[-1,1]³` after `w`-divide? derived, never stored |
| `move_to_top / bottom` | orbit/dolly to **canonical poses** (front, top, iso…) and re-check framing |

`assets/camera.py` ships `look_at`, `perspective`, `project`, `in_frustum`,
`CANON` (the pose table), and **`assert_model_framed(points, aspect)`** — the 3D
`assert_viewport_sound`: for every canonical pose, every model point must land
inside the NDC box and the model must fill a sane fraction of it (not a speck,
not clipped).

## 2. The language of edges & angles (OpenSCAD)

**Solids & edges:** `cube sphere cylinder polyhedron` · CSG `union() difference()
intersection()` · `hull()` (convex wrap — the edge set of the outline) ·
`minkowski()` (fillet/offset) · `linear_extrude`/`rotate_extrude` (2D profile →
3D edges) · `projection(cut=false)` = the **silhouette / shadow** onto z=0,
`projection(cut=true)` = the **cross-section** at z=0.

**Transforms (the angle language):** `translate([x,y,z])` · `rotate([rx,ry,rz])`
(Euler, applied X then Y then Z) or `rotate(a, [ux,uy,uz])` (axis-angle) ·
`scale` · `mirror` · `multmatrix(M)` — a full 4×4, which is how you apply a
projected n-D rotation (build M in code, hand it to `multmatrix`).

**Facet resolution = how many edges approximate a curve:** `$fn` (fixed count),
or `$fa` (max angle/facet, deg) + `$fs` (max facet size). Low `$fn` while
composing, raise for the final render.

**Camera from the model** (special vars, live in the GUI, settable on the CLI):
`$vpr=[rx,ry,rz]` viewport rotation · `$vpt=[x,y,z]` camera target · `$vpd`
distance (zoom) · `$vpf` fov (2021.01: read‑only) · `$t` animation time 0→1.

**Camera from the CLI:**
```
openscad -o out.png model.scad \
  --camera=tx,ty,tz,rx,ry,rz,dist   # target + euler + distance   (or ex,ey,ez,cx,cy,cz)
  --projection=o|p  --imgsize=1600,1200  --colorscheme=Tomorrow
openscad -o frame.png model.scad --animate 120   # writes frame00000.png … over $t
```

Canonical `$vpr` poses (target the model centre, pick `$vpd` for fit):
`front [90,0,0]` · `back [90,0,180]` · `top [0,0,0]` · `bottom [180,0,0]` ·
`right [90,0,90]` · `left [90,0,-90]` · `iso [55,0,25]` · `dimetric [60,0,45]`.
Details: `references/openscad-camera.md`.

## 3. x, y, z, t — and everything past z

`t` is free: `$t` (or `--animate`) sweeps it. A **4th spatial** axis has no
camera. Route it through one of these — never more than a couple at once:

| method | what it is | best for | cost to the viewer |
|---|---|---|---|
| **rotate** | spin in an x–w (or y–w, z–w) plane; the 3D shadow deforms | showing that structure is *one* connected 4D object (tesseract, 5‑cell, Hopf) | 1 animated parameter — near the human limit already |
| **slice** | show the 3D cross‑section at `w = w₀`; scrub `w₀` | metric reading of the interior; "what is actually at this level" | 1 animated/UI parameter + you lose the whole shape |
| **project** | Schlegel diagram (one cell pushed to infinity) / stereographic | topology & adjacency of a polytope, all cells at once | heavy occlusion; edges only |
| **encode** | colour / opacity / glyph size / iso‑surface value = `w` | a scalar field over xyz (σ‑face over the critical strip, `|f(z)|` domain‑colour) | 2–3 channels max; colour is not metric |
| **small‑multiples** | a grid of 3D views, one per `w` value | comparison across a few discrete `w` | ≤ ~5×5 before it is a wall |
| **parallax / stereo** | spend real binocular depth on the *3rd* axis so xyz are all "spatial" and the 4th is free for motion | any case where z must be judged, not guessed | needs a stereo display or an orbiting camera for motion parallax |

## 4. What a human can actually perceive (why this skill exists)

A person receives **two 2D retinal images** and the brain reconstructs roughly
**2.5D**: depth from binocular disparity, motion parallax, occlusion, shading,
linear perspective, and familiar size. There is **no native perception of a 4th
spatial dimension** — a 4D object is only ever apprehended as a *time‑series of
3D shadows* or a *stack of 3D slices*. So every "4D visualisation" reduces to:
pick 3 axes for the frustum, spend stereo + parallax on those 3, send axes 4…n
through {time, slice, colour, glyph, small‑multiples} under a budget:

- **~1** smoothly‑animated parameter can be tracked (2 only if very slow / looped).
- **2–3** simultaneous colour/size/opacity channels before they interfere.
- **~7 ± 2** discrete glyph/colour categories held at once.
- **≤ 5×5** small‑multiples grid.
- **≤ ~4** distinct depth layers read reliably without a scale cue.

A design that exceeds these is over budget — say so and cut, or split into views.
Always include a **scale reference**: a gnomon (labelled xyz axes), a bounding
box, or a familiar‑size object. Without it, perspective makes size unreadable.

## 5. The design method (checklist)

1. **True dimensionality & type** of each axis: continuous / ordinal / cyclic /
   categorical. Cyclic axes want rotation or a torus embedding, not a line.
2. **Pick the 3 frustum axes** — the ones the viewer must make *metric* judgments
   on (distance, angle, monotonicity). Everything else is a channel.
3. **Assign the rest** by the §4 budget. If it doesn't fit, small‑multiples or a
   linked‑views dashboard, not more channels.
4. **Projection:** orthographic to measure / compare lengths; perspective for
   spatial immersion and occlusion cues. Not both in one figure.
5. **Poses:** the canonical set + exactly one orbit (so motion parallax resolves
   depth). Land each canonical pose and run `assert_model_framed`.
6. **`$fn`:** lowest that makes curvature read; bump for the final render only.
7. **Scale cue** present. **Silhouette** (`projection`) checked — the salient
   structure must be non‑self‑occluded from ≥ 1 canonical view.
8. **Animation:** one parameter, looped, slow enough to track; a still frame at
   `$t=0` must already communicate the gist.

## 6. "Better than statistical prevalence" — choice as camera steering

Picking the next few words (or the next few options in any sequence) is usually
`argmax` over an empirical frequency table. Reframe it as **steering a trajectory
through the semantic manifold**, the same way you steer a camera:

- the phrase so far is a **path** in the embedding; each candidate word is a
  **next control point**.
- score a candidate not by how *common* it is but by how it keeps the path:
  - **low curvature / jerk** — the path's second/third derivative stays small
    (a smooth continuation, a well‑formed melodic line — the visual analogue is a
    camera move with no snap);
  - **invariant conserved** — the project's own constants: σ‑face stays near ½
    (on the critical line), the Noether `J₊/J₋` balance holds, BAO proximity
    doesn't degrade;
  - **silhouette continuity** — the candidate's spectral signature (its
    decomposition over the semantic basis — see `references/nd-to-3d.md` on the
    prime‑exponent analogy) continues the phrase's spectrogram without a
    discontinuity in the dominant tracks.
- frequency then breaks ties, it doesn't lead. This yields choices that *belong
  on the path* rather than choices that are merely popular — and it's directly
  inspectable as a waterfall / wiggle plot of the candidate spectra (see the
  discussion note that accompanied this skill).

## Files

- `assets/camera.py` — pure‑Python camera / frustum / `assert_model_framed`.
- `assets/hyperview.scad` — parametric tesseract & 5‑cell; `MODE = rotate | slice
  | project | shadow`; a labelled gnomon; `$t` drives the x–w rotation.
- `assets/render.sh` — batch‑render the canonical views + a `$t` animation.
- `references/openscad-camera.md` — `$vp*`, the CLI camera, canonical poses,
  `projection`/`cut`, `$fn/$fa/$fs`, 2021.01 caveats.
- `references/nd-to-3d.md` — projection / slice / animate / encode recipes,
  the perceptual budgets, worked examples (tesseract, domain colouring, a σ‑field
  over the critical strip, the prime‑exponent lattice as an EKG/waterfall).
