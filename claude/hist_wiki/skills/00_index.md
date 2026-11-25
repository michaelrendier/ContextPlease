# skills — one wiki page per skill

**Created 2026-10-17 (Cody).** Standing rule: every custom skill gets a page here **at creation**, and a page is
written or refreshed **for each skill loaded in a session**. Pages are the narrative view; the skill itself
(`../../skills/<name>/SKILL.md`) is the operating manual. Only `walk-the-hallway` exists so far; the other custom
skills (addition-matrix, cs-paper-code-conventions, generational-lineage, imagemagick, nes-viewport,
nltk-zork-wordnet, observer-position, scad-spatial, unit-management) get theirs as they are next loaded.

| skill | page | one line |
|---|---|---|
| walk-the-hallway | [walk-the-hallway.md](walk-the-hallway.md) | breadth-first surface mapper for any public-facing collection and protocol (mount family, S3, FTP, HTTP, APIs, TAP, container files); records its own sitemap to power the real crawl; resumable chunk cycles; generalised AppArmor/robots wall. Built: local-image mount backend |
| cs-paper-code-conventions | [cs-paper-code-conventions.md](cs-paper-code-conventions.md) | how a CS paper shows code (conventions A–G), the assistant note, introductions, and (v0.5.0) the CS engineering white paper measured on the thesearecool corpus |
| spatial-simulation | [spatial-simulation.md](spatial-simulation.md) | one viewport model for 2D pane, OpenSCAD camera and Blender camera; Blender 4.x bpy recipes; simulate → export → render (supersedes nes-viewport and scad-spatial, which are kept); v1.2.0 (2026-11-19) adds the spaces (De Sitter, Hilbert, Fano, sedenion + bracketing/firing order, Mandelbrot–Julia, gauge = orthogonal Smith charts / Apollonian gasket, equation space), axes that are hypercomplex fields, and the v2.0 rendering rules |
| zork-mapping | [zork-mapping.md](zork-mapping.md) | the graph-paper lattice method for Infocom/ZIL games: read ZIL rooms and exits, 3x3 per room, SVG and ASCII/Unicode maps, level colours, viewer rules |
| midi | [midi.md](midi.md) | MIDI as sheet music and generative material: SMF read/write, NES corpus survey, asinh/log/gamma envelope stretch, wavetable render (UniversalSynth), Yamaha P-105 helpers; corpus caveat: the live Midi directory is zero-filled |
| lean | [lean.md](lean.md) | Lean 4 + Mathlib: read, write, build and audit proofs (statement, axioms, escape hatches, clean rebuild); KERNEL-CHECKED label; not installed yet |
| scalar-context-reading | [scalar-context-reading.md](scalar-context-reading.md) | reads a text by the ScalarContextPropagation mechanism (synset -> 19 relations -> prime -> gamma_radial), lifted to sentence sums, fields, recurrence and WordNet-anchor emotions; measured on GoEmotions and on the long frustrated prompt, with limits |
| html-spatial-awareness | [html-spatial-awareness.md](html-spatial-awareness.md) | pages with a space in them: panels as viewports, y-up buffers, yaw/pitch/distance cameras, path parameter for colour and growth; raw WebGL vs three.js vs Canvas 2D vs SVG vs CSS 3-D vs React; Cody's gallery conventions; the JavaScript sub-gallery naming rule (webgl_/threejs_/canvas2d_/svg_/css3d_/react_); headless Firefox verification; surveyed from the 1,160-project HTML_CSS_JS collection |
