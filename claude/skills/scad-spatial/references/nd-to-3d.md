# n dimensions → 3 → the eye

A person gets **two 2D retinal images** and reconstructs ~**2.5D** (depth from
disparity, motion parallax, occlusion, shading, perspective, familiar size).
There is **no native 4th spatial axis**. Everything below is a way to spend the
three spatial slots you have and route the rest through weaker channels.

## The four moves for a 4th axis `w`

### rotate — `w` becomes motion
4D rotation in the `x–w` plane: `x' = x cos θ − w sin θ`, `w' = x sin θ + w cos θ`.
Then project 4D→3D (perspective from a `w`‑axis eye at distance `d`:
`k = d/(d−w')`, scale `(x',y,z)` by `k`; or orthographic: drop `w'`). Animate θ.
**Reads:** "this is *one* connected object" — the tesseract's inner cube everting
through the outer, the 5‑cell's cells trading places, the Hopf fibration's
linked circles. **Budget:** one animated parameter — you are already at the human
limit; do not also animate a colour.
`assets/hyperview.scad MODE="rotate"`.

### slice — show the 3D cross‑section at `w = w₀`, scrub `w₀`
`intersection()` the projected object with a thin slab, step the slab.
**Reads:** the *interior* metrically — "what is actually present at this level".
**Cost:** you lose the whole shape; only meaningful with a scrub control or a
small‑multiples strip of levels. `assets/hyperview.scad MODE="slice"`.

### project — Schlegel / stereographic
Push one cell of a 4‑polytope to infinity (Schlegel) or stereographically map
S³→ℝ³. **Reads:** adjacency and topology — every cell visible at once, all edges.
**Cost:** heavy occlusion, distances are not metric. `MODE="project"`.

### encode — `w` is a scalar field over `xyz`
Colour, opacity, glyph size, or an **iso‑surface value**. **Reads:** a field, not
a shape: `|f(z)|` domain colouring, a σ‑face value over the critical strip,
temperature over a volume. **Budget:** 2–3 channels total; colour is ordinal at
best, never metric — always give a legend.

## Perceptual budgets (state these; cut a design that exceeds them)

| channel | reliable capacity |
|---|---|
| smoothly animated parameters tracked at once | **~1** (2 only if slow + looped + independent) |
| simultaneous colour / size / opacity channels | **2–3** before interference |
| discrete glyph / colour categories held | **7 ± 2** |
| small‑multiples grid | **≤ 5 × 5** |
| depth layers read without a scale cue | **~4** |

Always include a **scale reference**: labelled `xyz` gnomon, bounding box, or a
familiar‑size object. Prefer **orthographic** when the viewer must compare
lengths/angles; **perspective** only for spatial immersion.

## Worked examples

**Tesseract / 5‑cell** — `rotate` for "one object", `project` for cell adjacency,
`slice` to feel the interior. Never all three in one figure; three linked panels.

**Complex function `w = f(z)`** — domain is 2D (`Re z, Im z`), codomain is 2D.
Put domain on `x,y`; `|w|` on `z` (a landscape); `arg w` on **hue** (domain
colouring). One animated parameter free for a family `f_a`. This is 4 real dims
in 3 spatial + 1 colour + optional time.

**σ‑face field over the critical strip** — `x = Re s ∈ [0,1]`, `y = Im s` (tall),
`z` or hue = the J‑ratio / σ‑face class. Iso‑surface at `σ = ½` is a *sheet*; its
intersection with `Re s = ½` is the critical line. Animate a parameter of the
generating operator; a still at frame 0 must already show the ½‑sheet.

**Prime‑exponent lattice as an EKG / waterfall** — the multiplicative structure
of ℕ is the free commutative monoid on the primes: `n ↦ (e₂, e₃, e₅, …)`
(finitely supported), a bijection by unique factorisation. The **ordinal** axis
(successor, `n → n+1`) is a *single 1‑D path threading transverse to that
∞‑D lattice*, visiting every lattice point once in an order that respects
neither the lattice metric nor divisibility — so "ordinal ⟂ prime‑lattice" is a
fair intuition, and the prime axes are mutually independent (each prime a free
coordinate: `e₂` tells you nothing about `e₃`).

Visualise it exactly like a multi‑lead EKG / a wiggle plot:

```
x  = n            (time sweep, left → right)
lane p (stacked): 2, 3, 5, 7, 11, …        one horizontal channel per prime
mark height / intensity in lane p at column n  =  eₚ(n)

n prime      → one unit spike in exactly one lane, all others silent
n = pᵏ       → a tall spike (height k) in one lane
n highly composite → many lanes fire together: a "chord"
```

Prime `p`'s lane pulses with period `p` and spikes higher at `p², p³, …`. It is
a genuine spectrogram of factorisation with primes as the (non‑uniform,
labelled) frequency bins — use the **wiggle / stacked‑trace** form, not a
heat‑map, because the bins are discrete and named. Read structure off it the way
an SDR waterfall reveals a carrier: coherent vertical alignment across lanes =
shared factors; a lone spike = a prime.

**"Next element" as camera steering** (see `SKILL.md` §6) — the candidate set is
a cloud of next control points for a path on the manifold; score by
curvature/jerk of the resulting path + an invariant held (σ near ½, Noether
balance) + spectral‑track continuity, and let raw frequency only break ties.
Inspect the candidates as a waterfall of their spectra and pick the column that
continues the dominant tracks without a jump.
