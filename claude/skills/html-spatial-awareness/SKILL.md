---
name: html-spatial-awareness
description: >
  How to build HTML pages that have a SPACE in them: gallery pages, 3-D and 2-D visualizations, canvas/WebGL/SVG/CSS-3D panels, mouse-driven cameras, data that grows on screen.
  Built 2026-11-24 from a survey of the whole xml12333/HTML_CSS_JS collection (1,160 front-end projects, cloned at ThePlace/Build/HTML_CSS_JS), from Cody's own gallery page
  (RiemannHypothesisProof/image_gallery), and from the browser comparison page made that day (RiemannHypothesisProof/visualizations/javascript/webgl_aizawa_vs_zeta_uns.html).
  Load before writing or changing any gallery, sub-gallery, JavaScript visualization, viewer or animation page; before choosing WebGL vs Canvas 2D vs SVG vs CSS 3-D vs three.js vs React;
  and before verifying a page in a headless browser. Records what was MEASURED, including the failures.
---

# HTML spatial awareness

**STANDING RULES (Cody, 2026-11-24):** (1) Load and apply this skill every time an HTML gallery or visualization page is made or edited. (2) **ALL GALLERIES GET COMMITTED AND PUSHED when they are finished being edited** (name the files; GITHUB_TOKEN via http.extraheader; never rewrite history). (3) Every page mentions the GitHub source it draws on and cites the literature (links + references in the page footer).

## 1. The space a page has (decide these first)
- **Panels are viewports.** Each panel is a rectangle of CSS pixels with its own backing store: canvas width/height = clientSize x devicePixelRatio, re-set on resize (`resize()` before every frame), `aspect = width/height`.
- **Pick the up axis once.** Python/maths code is z-up; WebGL pages here are y-up. The shipped buffer layout (from the Aizawa page and rhp.strange_path) is positions `[x, z, y]` so z is drawn up. Say it in a comment.
- **Camera = yaw, pitch, distance** about a centre point. mvp = perspective(fov 0.8 rad) * translate(0,0,-dist) * rotX(pitch) * rotY(yaw) * translate(-centre). Pitch 0 = equatorial view; pitch pi/2 = looking down the up axis (the view from the pole). Provide those two buttons, reset (double-click), wheel zoom (`{passive:false}`), pointer drag with `touch-action:none`, and a "link cameras" toggle when two panels compare.
- **One parameter along a path.** Geometry is (positions Float32Array(3n), param Float32Array(n)); param = i/n colours the path (rainbow) and also drives growth animation: draw the first `count` vertices.

## 2. Which technology (from the survey of 1,160 projects; counts are index.html + js/script.js)
requestAnimationFrame 201 · SVG 186 · GSAP 89 · Canvas 2D 88 · GLSL shaders 74 · Float32Array buffers 68 · raw WebGL 45 · three.js 43 (OrbitControls 28, bloom 10) · p5 16 · React 13 · CSS 3-D 8 · Web Audio 7 · Matter 6 · D3 3 · Vue 2.
- **Raw WebGL** for 10^5 points and up, or when the page must run with no libraries (one program, `gl.POINTS` or `LINE_STRIP`, additive blend, no depth test).
- **three.js** up to ~5x10^4 vertices or when you want bloom / OrbitControls; vendor it locally (importmap to a local file) with its MIT licence. Never a CDN: these pages run offline.
- **Canvas 2D** for small plots (spectra, 2-D paths); **SVG** for diagrams and labelled figures; **CSS 3-D** (`preserve-3d`, `perspective`) for cards and cubes; **CSS radial gradients** for backgrounds.
- **React / JSX.** Cody's note: "Gemini uses React Native". React Native targets iOS/Android, not browser pages; browser output from Gemini is normally React (JSX). Not tested here: if a React page arrives, use a local React build, one `useRef` per canvas, and cancel `requestAnimationFrame` in the effect cleanup. Mark such a page `react_*`.
- **Gradient mesh** (collection entry 1074): nine `radial-gradient(at X% Y%, var(--cN) 0, transparent 50%)` layers on a 3x3 grid of control points, summed: a smooth field interpolated from control values (a radial-basis mixture; the vector version is a Coons/bicubic patch). Use it for backgrounds and for colouring a surface from a few control values.

## 3. Rules learned by failing (each one was measured)
1. **Additive glow saturates.** 400,000 points at alpha 0.3 is a white disc. Scale alpha with the point count (alpha ~ K / count, clamp 0.05..0.5) and draw every 3rd point for dense paths (order and growth are kept).
2. **A sampling lattice draws fake structure.** Sampling a rotating curve at equal phase steps puts every point on a few fixed angles: 32 rigid spokes appeared that were not in the curve. Jitter the phase grid (golden-ratio offset), or draw lines.
3. **file:// pages cannot `fetch()` local files in Firefox.** Bake data into a `<script src="x_data.js">` as base64 Float32Array text (`window.X = {...}`); it works offline and from a local server.
4. **Headless Firefox does not capture WebGL canvases.** The screenshot shows black while `gl.readPixels` reports lit pixels. Verify with (a) `preserveDrawingBuffer:true`, (b) a lit-pixel count written into the DOM, (c) a `?snap=1` option that replaces each canvas by an `<img src=canvas.toDataURL()>` so a screenshot shows it.
5. **Make errors visible in the DOM** (shader log, `gl.getError()`, WebGL version) - a black canvas gives no other clue.
6. `gl_PointCoord` is undefined for lines: round-point discard needs a uniform that is 0 when drawing lines.
7. Data wider than the panel: set `aspect-ratio` on the canvas wrapper, not fixed pixel sizes; two columns above 800 px, one below; 16 px gutters.
8. Do not run someone else's JavaScript to "see what it does": read it. (The harness blocked executing a downloaded page; the equations were verified by reading and by an independent Python port.)

## 4. Cody's gallery conventions (image_gallery/Riemann_Fermat_Atlas_Gallery.html, gallery_config.json)
- Config-driven: `name`, `slug`, `port`, `tagline`, `catalog`, `exclude`, and `groups` = {name, regex `match`, `blurb`}; every item carries its description and provenance.
- Light/dark with colour tokens on `:root` (`--bg --fg --mut --card --line --acc`) and a `prefers-color-scheme` block; deep links `#g=<group>&img=<id>`; a lightbox with prev/next; a contact header/footer (email, Facebook, ORCID) on every page.
- Served by `serve_gallery.sh`: `python3 -m http.server <port> --bind 127.0.0.1` from the repo root, then `xdg-open` (Firefox shows the favicon only for http pages).
- A picture shows a space or a machinery; it is not evidence. Say so in the tagline.

## 5. The JavaScript sub-gallery (decided 2026-11-24)
`RiemannHypothesisProof/visualizations/javascript/` with `index.html` listing the pages. **File names say the kind of code inside:** `webgl_*.html` (raw WebGL), `threejs_*.html`, `canvas2d_*.html`, `svg_*.html`, `css3d_*.html`, `react_*.html`; data files `<name>_data.js`; serve with `visualizations/serve_visualizations.sh [port=8770] [page]`. URL options on a page (`?chart=&view=&zeros=&ticks=&snap=1`) so a view can be linked and screenshotted. Each page states in a comment what code, what data and what engine it came from.

## 6. Verify a page (recipe)
```
mkdir -p /tmp/claude-1000/shot/prof
firefox --headless --no-remote --profile /tmp/claude-1000/shot/prof --screenshot out.png --window-size=1300,900 "file:///.../page.html?snap=1"
```
Read the PNG; check the DOM-written GL status line; look at the equatorial AND the pole view; look with few points and with all of them.

## 7. Where to look in the collection (ThePlace/Build/HTML_CSS_JS; local clone, no licence shown, read-only reference)
1137 Holographic Aizawa Attractor (three.js + bloom, RK4 buffers) · 1030 Electric Attractor (1,525-line Lorenz page) · 923 Decomposed Torus · 1074 Gradient Mesh · 1156 Navier-Stokes · 500 3D Globe · 503 3D CSS · 814 Portal Effect · 527 Whale Animation · 893 Stars (CSS Houdini) · 1007 Glass Clock (Pixi). Author of the collection: "Nikolay T." (github.com/xml12333, 30 public repos, learning projects from TraversyMedia, FlorinPop, EasyTutorials, TylerPotts, Bedimcode, Kevin Powell, Codepen). A learner's collection, not an authority; the originals are the sources.
