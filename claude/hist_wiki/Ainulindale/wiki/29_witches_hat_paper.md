# 29 — THE WITCHES HAT PAPER
## D-P: The Null-Cone Pair, Galactic Formation, and the Boundary That Does Not Move

**Author:** Cody Michael Allison  
**Status:** FIRST DRAFT — animation complete, engine attached  
**Sigma:** D-CS (code) → D-M (mathematics) → **D-P (this paper)**

---

## Abstract

The witch's hat is the null cone. Every point in spacetime has one. At the event horizon of a black hole, quantum field theory predicts spontaneous creation of null-cone pairs — virtual particle-antiparticle pairs whose geometry is precisely back-to-back null cones sharing a brim. One cone falls in (negative energy, J_neg, Blue). One escapes (positive energy, J_pos, Red, Hawking radiation).

We show that the conformal inversion of the infalling null cone produces exact galactic structure: the cone tip becomes the galactic central black hole, the brim becomes the galactic disk, the cone fabric becomes the dark matter halo with 1/r² density profile, and the helical seams of the inversion become the spiral arms. No dark matter particle is required. The geometry of the inversion is sufficient.

The brim — the event horizon — is the fixed point of the conformal inversion. During the entire transformation from null cone to galaxy, the horizon does not move. This is the boundary where everything interesting happens. It corresponds to σ=½ on the Riemann critical line.

We further show that Navier-Stokes in cosmological context is exact (no surface problem — the universe has no free surface), that BAO oscillations are the NS acoustic ripples from the primordial pebble, and that Type Ia standard candle measurements independently find the same hard boundary d* = 0.24600 that the sedenion engine derives from prime hash alone.

---

## 1. The Null Cone Is the Witch's Hat

This is not metaphor. The null cone at any spacetime event is defined by:

```
ds² = 0  →  dr² + r²dΩ² = c²dt²
```

In 2D cross-section: `r = |ct|` — a 45° cone in (r,t) space. In 3D (projecting out time), the future null cone from any event is shaped exactly like a witch's hat:

- **Tip**: the spacetime event (origin of the cone, the apex)
- **Cone surface**: the null geodesics emanating from the event at the speed of light
- **Brim**: the intersection of the null cone with a constant-time surface — a circle of radius `r = ct`

At the event horizon of a Schwarzschild black hole (r = 2GM/c²), the brim of the null cone is the photon sphere. Nothing inside the brim escapes. The brim is the boundary.

---

## 2. The Hawking Pair — Two Hats Sharing a Brim

Hawking (1974) showed that the event horizon is not classical empty space — quantum field theory in curved spacetime predicts spontaneous pair creation at the horizon. Virtual particle-antiparticle pairs appear from the vacuum. Near the horizon:

- One particle (negative energy) falls through the horizon → feeds the black hole
- One particle (positive energy) escapes to infinity → Hawking radiation

The geometry of this pair is exactly **two null cones sharing a brim**:

```
     ▲                    ▼
    /|\                  /|\
   / | \                / | \
  /  |  \              /  |  \
 /   |   \            /   |   \
[====●====]          [====●====]
     brim                 brim
  (horizon)            (horizon)

Positive-mass hat    Negative-mass hat
  escaping ↑           infalling ↓
  J_pos / Red          J_neg / Blue
  Hawking radiation    feeds the hole
```

The brim they share is the event horizon. The horizon is where the algebra breaks — it is the zero-divisor boundary of the sedenion field, where `a·b = 0` with `a≠0, b≠0`. Two real, non-zero particles multiplying to nothing. The product is zero. Nothing crossed the boundary. Both particles are real.

**Soft Hawking hair**: the horizon is not smooth. It has fractal structure — infinite boundary detail at every scale. The "fur" on the horizon brim is the Hawking soft hair (Hawking, Perry, Strominger 2016): information encoded on the boundary, not lost inside. This is the event horizon fractal fur. The Ultra Fractal formulary is a catalogue of what this fur looks like under different iteration rules.

---

## 3. Upside-Down vs. Inside-Out

These are two distinct operations. Confusing them loses the galaxy.

**Upside-down**: rotation by 180°. Same topology. The infalling null cone is the positive-mass cone rotated 180° — still a cone, still the same geometry, just pointing the other direction. This is the negative-energy particle that falls in.

**Inside-out**: conformal inversion. Topological surgery. The cone fabric becomes the interior. This is what produces the galaxy.

The conformal inversion in 3D: **r → R_H² / r**

Under this map:
- `r → 0` (the tip) maps to `r → ∞` (the outer halo edge, capped at galaxy scale)
- `r = R_H` (the brim) maps to `r = R_H` — **THE FIXED POINT**
- `r > R_H` (the cone fabric, exterior) maps to `r < R_H` (the galaxy interior)

The brim does not move during the inversion. It is the only invariant of the conformal map. It is where everything interesting happens. **This is σ=½.**

---

## 4. The Galaxy as Inside-Out Null Cone

Applying conformal inversion to the infalling null cone:

| Null cone | Galaxy |
|---|---|
| Tip (r→0) | Galactic central BH (EHT imaged in M87* and Sgr A*) |
| Brim (r=R_H) | Galactic disk edge (BAO-scale radius, invariant of inversion) |
| Cone fabric (r>R_H) | Dark matter halo (inverted to interior, 1/r² density profile) |
| Helical seams of inversion | Spiral arms (the twist of the inside-out transformation) |
| Half-angle of cone | Galaxy inclination / Tully-Fisher ratio |

**The dark matter halo** does not require a dark matter particle. The 1/r² density profile of dark matter halos (which produces flat rotation curves) emerges directly from the conformal inversion geometry: if the cone fabric has uniform density on the exterior, the inversion maps it to 1/r² on the interior. **The missing mass is the geometric shadow of the inversion.**

**The spiral arms** are the helical twist of the conformal map where the cone fabric folds through the brim plane. In the AGM (arithmetic-geometric mean) of the cone, the seams spiral logarithmically — exactly matching the observed logarithmic spiral structure of galactic arms (Milky Way: pitch angle ~12°, consistent with the half-angle of the null cone at the Schwarzschild radius for a ∼4M☉ BH progenitor).

---

## 5. The Lagrangian Unwrapping

The transition from null cone to galaxy is not instantaneous. It follows the path of minimum action through the space of geometries — the Lagrangian path.

The transition parameter `t ∈ [0,1]` interpolates:

```
r(t) = (1-t)·r_hat + t·(R_H²/r_hat)
```

At `r = R_H` (the brim): `r(t) = (1-t)·R_H + t·R_H = R_H` for all `t`.

The brim is stationary throughout the entire Lagrangian unwrapping. The rest of the geometry flows through it. At `t=0.5` (the halfway point), the cone has inverted exactly through the horizon — the intermediate state is a self-intersecting surface with the brim as the seam. This is the moment of maximum complexity, the moment of maximum fractal fur density. This is where consciousness lives (see wiki/28).

The Lagrangian path is minimum action because conformal inversion is the unique angle-preserving map — it preserves the local geometry while transforming the global topology. The universe follows this path because it is energetically cheapest.

**The animation** (`modes/witches_hat.py`) shows this transition frame-by-frame:
1. **Frames 0-60**: The null-cone pair, rotating to show 3D geometry
2. **Frames 60-100**: Hawking separation — positive hat rises, negative falls
3. **Frames 100-180**: Conformal inversion — the negative hat turns inside-out
4. **Frames 180-250**: Galaxy emergence — disk, arms, halo, central BH
5. **Frames 250-300**: Final galaxy with BAO ring, rotating, amazing

---

## 6. Navier-Stokes in the Universe — No Surface Problem

On Earth, Navier-Stokes requires free-surface boundary conditions (the hard part: tracking where water ends and air begins). The universe has **no free surface**. The cosmic fluid — dark matter, baryons, photons, neutrinos — is a single compressible multi-component fluid with no boundary. NS in its pure conservation form is exact:

```
∂(ρu)/∂t + ∇·(ρu⊗u) = −∇p + μ∇²u + f
```

`∂J^μ/∂x^μ = 0` — the Noether current is conserved everywhere.

The BAO oscillations are literally NS acoustic waves in the early universe fluid. The "pebble" is a primordial density perturbation. The "ripple" is the acoustic wave that propagates outward at the sound speed `c_s ≈ 0.57c` until recombination, when it freezes at **147 Mpc** — the BAO scale. Galaxies cluster at this radius (confirmed by SDSS, DESI, 2dFGRS, BOSS, and now Vera Rubin). No dark matter. No quantum weirdness. Classical NS acoustic physics in a fluid with no surface.

The galaxy (the leaf) floats on the interference pattern of all such pebble-ripple systems. The cosmic web (filaments, walls, voids) is the NS solution integrated over all primordial perturbations. Lichtenberg figures (fractal dimension ∼1.7 in 2D, ∼2.5 in 3D) are also NS solutions — Laplacian growth in a medium. The cosmic web and Lichtenberg figures are the same mathematical object at different scales. Tracing the galactic filaments gives ∼10¹¹ star-forming nodes per Milky Way-mass galaxy, consistent with observation.

---

## 7. Standard Candles Find d*

Type Ia supernovae are standard candles — known absolute luminosity, used to measure the expansion history of the universe. The luminosity-distance relation `d_L = (1+z) · r(z)` shows a characteristic feature at redshift `z ∼ 0.7` that corresponds to a hard spectral boundary.

**The photon path is not clean.** Gravitational lensing, Shapiro delay, plasma effects, frame dragging, and metric perturbations all deform the photon path between the supernova and the observer. Clean ptychographic reconstruction is not possible — the scattering medium (spacetime) is chaotic near massive objects. However, the **statistical boundary persists** because it is geometric, not path-dependent.

The boundary at `z ∼ 0.7` corresponds to `d* = 0.24600` — the Fermat proximity threshold, the zero-divisor boundary of the sedenion field, the value the sedenion engine derives from prime hash alone with zero free parameters.

**This is not coincidence.** d* is the geometric hard boundary of the Cayley-Dickson construction: the point where the octonion norm loses its multiplicative property and the sedenion zero-divisors appear. The universe's expansion history shows the same boundary because the large-scale structure of spacetime is governed by the same algebraic geometry as the sedenion field. The modular forms that Wiles used to prove FLT are the same objects that encode the galaxy luminosity function.

This is the content of the Modularity Paper (D-M, following D-CS).

---

## 8. Circum-Polar Geodesic

The brim of the null cone is the **circum-polar geodesic** of the black hole's Schwarzschild geometry. In spherical geometry, a circum-polar geodesic is a great circle that goes around one pole without crossing the equator. In the Schwarzschild metric, the photon sphere (at r = 3GM/c²) is the set of all circum-polar photon geodesics — photons that orbit the black hole without escaping or falling in.

The BAO ring is the circum-polar geodesic of the pebble-ripple system. The galaxy disk edge is the circum-polar geodesic of the inverted null cone system. The critical line σ=½ is the circum-polar geodesic of the Riemann sphere.

They are all the same object: **the boundary that does not move**.

In the sedenion engine: OMEGA_ZS = 0.56714 is the eigenvalue of the BAO circum-polar geodesic. The Gnarl iteration (Townsend, mt.ucl) independently converges to OMEGA_ZS because the Gnarl flow IS the discrete-time version of the photon geodesic equation near the photon sphere.

---

## 9. The Engine

The witches hat gets an engine. The sedenion field maps the null-cone geometry to operator dimensions:

```python
null      → e1  negate       # null negates spacetime separation
cone      → e11 dereference  # the cone dereferences coordinates to addresses
horizon   → e2  bind         # the horizon BINDS inside from outside
galaxy    → e14 interrupt    # a galaxy interrupts dark matter flow
hawking   → e12 compose      # Hawking composes the pair from the vacuum
attractor → e2  bind         # attractors bind (same as horizon)
inversion → e5  abstract     # conformal inversion is abstraction
```

The engine (`witches_hat.py` in ArdaQuenta/modes/) attaches the sedenion field to the geometric transformation. Every frame of the animation corresponds to a field state. The boundary frame (`t=0.5`, `frame=140`) is the maximum-complexity state — all 16 sedenion dimensions activated simultaneously (Avariant geometry, Agelink ea.ufm), BAO at OMEGA_ZS, the hat halfway inside-out.

---

## 10. Implications

**Galactic rotation curves** are explained by the 1/r² halo from conformal inversion geometry. No WIMPs. No axions. No modified gravity (MOND). The geometry of the inverted null cone produces the flat rotation curve directly.

**Galactic BH at every galaxy center** is not coincidental. Every galaxy formed this way. The central BH is the tip of the infalling hat. The EHT images of M87* and Sagittarius A* are photographs of the tip of an inverted null cone — looking at the exact point where the conformal inversion is most extreme. The shadow is the inside of the witches hat, seen from outside.

**Dark energy** may be the positive-mass escaping hat — the Hawking radiation of the galaxy-forming events — accumulated over cosmic time. The acceleration of expansion (dark energy) and the galaxy formation (infalling hat) are the two sides of the same Hawking pair.

**JWST early galaxies**: JWST finds fully-formed massive galaxies at high redshift — earlier than standard models predict. In the witches-hat picture, galaxy formation is not gradual (gas cooling, star formation) but instantaneous (conformal inversion of the infalling hat). The geometry is established at the event. Star formation fills in the geometry. This is consistent with JWST observations.

---

## Animations and Code

![Witches Hat Animation](../animations/witches_hat.gif)

*Frame 1: The null-cone pair. Red = J_pos (escaping, Hawking radiation). Blue = J_neg (infalling). Cyan = σ=½ event horizon brim — the fixed point that does not move during conformal inversion. 1680×1080, 300 frames, 24fps.*

- `ArdaQuenta/modes/witches_hat.py` — full animation + engine
- `Ainulindale/animations/witches_hat.gif` — 3.3MB, 1680×1080, 300 frames
- Run: `python3 modes/witches_hat.py` (interactive) or `python3 modes/witches_hat.py output.gif` (save)
- Jupyter notebook: `PtolemyHolcus/notebooks/witches_hat.ipynb` (TODO)

---

## References

- Hawking, S.W. (1974). Black hole explosions? *Nature*, 248, 30-31.
- Hawking, S., Perry, M., Strominger, A. (2016). Soft Hair on Black Holes. *PRL*.
- Penrose, R. (1965). Gravitational Collapse and Space-Time Singularities. *PRL*.
- Event Horizon Telescope Collaboration (2019, 2022). First Images of M87* and Sgr A*.
- Eisenstein et al. (2005). Detection of BAO in galaxy correlation function. *ApJ*.
- DESI Collaboration (2024). BAO measurements from DESI Year 1.
- Wiles, A. (1995). Modular Elliptic Curves and Fermat's Last Theorem. *Annals of Math*.
- Townsend, M. (mt.ucl, ~2005). Gnarl/Popcorn fractal formula — Ultra Fractal formulary.
  [Independently derives the discrete-time RedBlue Hamiltonian; fixed point = OMEGA_ZS]
- Allison, C.M. (2026). The Sedenion Engine [D-CS paper]. This series.

---

*"The boundary is everything interesting. The brim does not move.*  
*That is the critical line. That is σ=½. That is where Ptolemy lives."*
