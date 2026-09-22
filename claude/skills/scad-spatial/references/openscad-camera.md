# OpenSCAD camera & edge reference

## Special variables (the camera, from inside the model)

| var | meaning | notes |
|---|---|---|
| `$vpr` | viewport rotation `[rx,ry,rz]` deg | rotates the *scene*; camera stays on the view axis. Euler X→Y→Z. |
| `$vpt` | viewport translation `[x,y,z]` | the camera **target** (look-at point) |
| `$vpd` | viewport distance | eye‑to‑target; the zoom |
| `$vpf` | viewport field of view (deg) | **read‑only in 2021.01**; writable in later builds |
| `$t` | animation time, `0 … 1` | set by `--animate N` (frame k → `$t = k/N`) or the GUI Animate FPS/Steps |
| `$fn` | facets per full circle | overrides `$fa`/`$fs` when > 0 |
| `$fa` | min angle per facet (deg, default 12) | curve smoothness by angle |
| `$fs` | min facet size (mm, default 2) | curve smoothness by length; effective count = `max(360/$fa, circ/$fs)` |
| `$preview` | true in F5 preview, false in F6 render | gate cheap vs. exact geometry |
| `$vpr`/`$vpt`/`$vpd` are also **readable** — a model can react to the camera. |

Set them on the CLI with `-D`: `openscad -D '$vpr=[55,0,25]' -D '$fn=64' …`.

## CLI camera

```
openscad -o out.png model.scad \
  --camera=TX,TY,TZ,RX,RY,RZ,DIST        # target + euler + distance   (7 numbers)
  --camera=EX,EY,EZ,CX,CY,CZ             # eye + centre                (6 numbers)
  --projection=p|o                       # perspective | orthographic
  --viewall --autocenter                 # fit + centre the model (ignores --camera translation)
  --imgsize=W,H
  --colorscheme=Cornfield|Tomorrow|Nature|"Tomorrow Night"|Sunset|Starnight|Metallic|BeforeDawn
  --render                               # full CGAL render (F6) instead of preview
  --animate N -o frame.png               # writes frame00000.png … frameNNNNN.png over $t
```

`--viewall` overrides the translation part of `--camera`; use it when you just
want "show me the whole thing from this angle".

## Canonical `$vpr` poses (target = model centre; pick `$vpd`/`DIST` to fit)

```
front   [ 90, 0,   0]      back    [ 90, 0, 180]
top     [  0, 0,   0]      bottom  [180, 0,   0]
right   [ 90, 0,  90]      left    [ 90, 0, -90]
iso     [ 55, 0,  25]      dimetric[ 60, 0,  45]      trimetric [65, 0, 35]
```

`--viewall` + one of these + `--projection=o` = an engineering drawing view.
`--projection=p` + `iso` + a `$t` orbit = the shape read for space, not measurement.

`assets/camera.py :: CANON` mirrors this table so the Python `assert_model_framed`
uses the same poses the render script does.

## Edges, silhouettes, sections

| want | do |
|---|---|
| the **outline** of a solid from the current camera | `projection(cut=false) <solid>` — flattens the shadow onto z=0 (rotate the solid into the view first, or read `$vpr` and pre‑rotate) |
| a **cross‑section** at z=0 | `projection(cut=true) <solid>` |
| a section at arbitrary z=`h` | `projection(cut=true) translate([0,0,-h]) <solid>` |
| the **wireframe / 1‑skeleton** | draw each edge as `hull(){translate(a) sphere(r); translate(b) sphere(r);}` (round) or a `cylinder` aligned a→b |
| a **convex outline** of a point set | `hull()` of small spheres at the points |
| **fillet / shell / offset** an edge set | `minkowski(){ <solid>; sphere(r); }` (round) — expensive; keep `$fn` low |
| apply a **projected n‑D rotation** | build the 4×4 in code, `multmatrix(M) <solid>` |

`$fn` on `hull`/`minkowski` sphere primitives controls how round the edges look;
8–16 while composing, 32–64 for a final still.

## 2021.01 caveats

- `$vpf` is read‑only — you cannot animate the fov from the model; set fov via
  `--camera` isn't supported either (fov is fixed ~22.5° in perspective). Dolly
  with `DIST` instead.
- No `assert()` with a message in some builds — use `echo()` + a visible marker.
- `text()` needs a font available; `linear_extrude(eps) text(...)` for 3D labels.
- Animation writes PNGs only; stitch with `ffmpeg -framerate 24 -i frame%05d.png
  -pix_fmt yuv420p out.mp4`.
