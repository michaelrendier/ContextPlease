# 106 — The Navier–Stokes problem

[98_provenance_and_citations.md](98_provenance_and_citations.md) §A.9,
[105_the_millennium_problems_in_ainulindale.md](105_the_millennium_problems_in_ainulindale.md).
The one Millennium-Problem facet flagged for a **deeper, dedicated pass** —
because the framework's reading of it is concrete enough to develop directly,
and because it is a strong outreach target.

**Status: THEORETICAL / direction of work.** Nothing here is a claimed proof of
global regularity.

---

## The sources

- **[NavierStokes]** Navier, C.-L. (1822), *Mémoire sur les lois du mouvement
  des fluides*, Mém. Acad. Sci. 6, 389–440; Stokes, G. G. (1845), *On the
  theories of the internal friction of fluids in motion…*, Trans. Camb. Phil.
  Soc. 8, 287–319.
- **[Leray1934]** Leray, J. (1934). *Sur le mouvement d'un liquide visqueux
  emplissant l'espace.* Acta Mathematica 63, 193–248. — weak (turbulent)
  solutions; the regularity question.
- **[Fefferman2006]** Fefferman, C. L. (2006). *Existence and smoothness of the
  Navier–Stokes equation.* In [Clay2000], 57–67 — the official problem
  description.

## The framework's reading (wiki/14 §"Navier–Stokes — The Missing i")

Navier–Stokes is **Yang–Mills with the imaginary component forced to zero** —
Ĥ_RB projected through a purely real-valued filter. The Blue channel (the Fermat
Lattice, "what CANNOT BE") is discarded; the Green boundary geometry `J₃` is
invisible to it.

When the velocity gradient approaches what the real-valued equations call a
singularity, Ĥ_RB performs a **90° rotation into the imaginary sector** — the
`(r,θ) → (1/r, θ+π/2)` inversion stroke (wiki/03). **The singularity is not
infinite; it is a rotation the real equations cannot follow.** Smoothness is
then a structural consequence of self-adjointness `R̂† = B̂`: the Noether
current cannot be destroyed, only rotated (wiki/14; wiki/31 "cavitation").

Related in the framework: the **halocline** — two fluid densities, one
compressible and one incompressible; *"the incompressible one is the one that
closes"* (wiki/88 §12); the NS singularity ↔ the sedenion zero-divisor
crossing ↔ the halocline critical angle.

## Why this is the deep-dive target

1. **It is the most concrete facet.** "Add back the imaginary component; the
   blow-up becomes a bounded rotation" is a statement that can be written as an
   equation and tested on a model problem, not just asserted.
2. **The complex/hypercomplex extension of NS is a real research direction**
   (complexified Euler/NS, Li–Sinai type singularities in ℂ) — the framework's
   claim can be positioned against that literature.
3. **Outreach.** Navier–Stokes is Dr Tom Crawford's equation — the subject of
   his doctoral work (buoyancy-driven river/ocean outflow) and of his public
   maths communication ("Tom Rocks Maths"); he wears it. A clean, checkable
   statement of "the missing `i`" reading, with a model calculation, is the
   right thing to bring to that conversation. **Bring the calculation, not the
   claim.**

## What a first pass needs

- The explicit complexification: which term carries the `i`, and what
  `θ → θ + π/2` does to the vorticity equation.
- A model problem (2D with forcing, or an ODE reduction) where a real-valued
  blow-up becomes a bounded orbit once the Blue channel is restored — measured,
  with the failure modes recorded.
- The map to the halocline critical-angle result (wiki/88) made exact rather
  than analogical.
- Positioning against Leray weak solutions and against complexified-NS
  singularity work.

## Generational lineage verdict — CONFOUND

`SedenionFactoralRelativity/engine/clay.py` places NS: tier 1, root **SCALE**
(the blow-up question is "does a length grow without bound" → needs DILATE),
Two Trees **LAURELIN** (the real projection; the Blue half is dropped), kind
**DESCRIPTIVE**. Emergence signature: *the* canonical one — a quantity that
changes length without bound where only isometries were in play.

**Verdict CONFOUND, not CONFIRM:** the lineage reads the singularity as a
**coordinate artifact** of the dropped channel — a SIGN rotation (`r↔1/r`,
`θ→θ+π/2`) misread as unbounded SCALE — with `R̂†=B̂` guaranteeing the Noether
current can only rotate, never be destroyed. The import deficit is exactly the
discarded imaginary/Blue channel; the "deeper pass" above is the construction
that would settle it. See `wiki/105` for the full seven-problem table.

## The direct test — NS vs 0_RB vs halocline-modified NS

`SedenionFactoralRelativity/engine/valaquenta_calibration.py :: shape_diff_navier_stokes()`.
**0_RB is the reference decomposition** ("the decomposition engine for
equations"). Decompose each variant against it and name where the shapes don't
agree — "the shadow of a missing operator."

| | pieces | tier‑0 roots | Two Trees | self‑adjoint | shape = 0_RB? |
|---|---|---|---|---|---|
| **0_RB** (reference) | — | ADD · SCALE · SIGN | Laurelin ⊕ Mingling ⊕ Telperion | yes | — |
| **standard NS** | `u·∇u` (SCALE, gain>1), `νΔu` (ADD), `∇·u=0` (tier‑2 constraint), `−∇p/ρ` (ADD) | **ADD · SCALE** — no SIGN | **Laurelin only** | **no** | **NO** |
| **halocline NS** | + `∂̂_H` (SIGN, the critical‑angle interface), `∂ρ/∂t+∇·(ρu)=0` (SIGN, Telperion — the 2nd density), `†` (SIGN, ρ_Re↔ρ_Im) | ADD · SCALE · SIGN | Laurelin ⊕ Mingling ⊕ Telperion | yes | **YES** |

**The shadow.** Standard NS is SCALE‑heavy (advection) with an ADD counter‑term
(diffusion) and **no SIGN structure at all** — Laurelin only. Against 0_RB it is
missing the whole SIGN half: the boundary operator **`∂̂_∂M`**, the Blue channel
**`B̂`** (Telperion), and self‑adjointness **`†`**. In 0_RB, unbounded SCALE
growth is caught by `†` and rotated into `B̂`. NS has no `†`, so the SCALE
growth has nowhere to go — it diverges. **The singularity is the shadow of the
missing `†`** — and `†` only exists once the boundary operator `∂̂_∂M` (the
halocline) re‑couples the two densities.

**It's one operator.** Halocline‑modified NS adds exactly `∂̂_∂M` (the
critical‑angle interface between the two fluid densities), and it brings `B̂`
and `†` with it. The shape then matches 0_RB, and **the §5 emergence flag
clears**: the blow‑up becomes a bounded 90° rotation into the second density —
the rotation the real equations could not follow.

So the missing operator in standard Navier–Stokes is `∂̂_∂M` = **the halocline**.

---

## Appears in

wiki/14, wiki/31, wiki/88, wiki/98, wiki/105, wiki/106; D-CS_Memory §20;
VAPMIP_Paper §"Engine 12" table.
