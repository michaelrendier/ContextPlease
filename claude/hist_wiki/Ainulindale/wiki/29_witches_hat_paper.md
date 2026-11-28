# 29 — The Witches Hat: the null-cone pair and the inside-out hat

| | |
|---|---|
| Status | **A physical–geometric proposal (`THEORETICAL`)** with one exact lemma (§3) and one test that fails (§4). The earlier header ("D-P: first draft, animation complete") described a paper plan; see [26](26_TODO_and_roadmap.md) §1 |
| Code | `ArdaQuenta/modes/witches_hat.py` (591 lines: the null-cone pair, conformal inversion, galaxy emergence, the L_dynamic action cone; matplotlib animation) |
| Missing | the animation file `Ainulindale/animations/witches_hat.gif` named by the earlier page does not exist (no `animations/` directory in the repository); regenerate with `python3 modes/witches_hat.py output.gif` |
| Lineage | this page begins the Witches Hat / galactic particle-resonation-cavity line, the line in which the Schumann cavity resonance became relevant to the sonification work (`UniversalSynth/TODO.md`; [08](08_sonification_engine.md)) |
| Last verified | 2026-11-13: the exact statements re-derived; Listing 1 executed; the code file read for its stated model |

## 1. The null cone is the hat  `ESTABLISHED` (geometry)

At any spacetime event the null cone is ds² = 0, i.e. dr² + r²dΩ² = c²dt².
In the (r, t) plane it is r = |ct|, a 45° cone; with time projected out, the
future cone has the shape of a witch's hat: the **tip** is the event, the
**surface** is the null geodesics from it, and the **brim** is the circle of
radius r = ct where a constant-time surface cuts the cone.

*Correction.* The earlier page said that at a Schwarzschild horizon "the brim
of the null cone is the photon sphere". It is not: the horizon is at
r = 2GM/c² and the photon sphere at r = 3GM/c². The brim of the hat is a
construction of the picture, and where it is placed on a black hole is a choice
(§2).

## 2. The Hawking pair as two hats sharing a brim  `interpretation`

Hawking (1974) showed that quantum fields in a black-hole spacetime radiate. The
heuristic picture of virtual pairs, one negative-energy member falling in and one
escaping, is standard but heuristic. The proposal here is geometric: the pair is
two null cones sharing a brim, the **positive-mass hat** escaping (J_pos, Red,
Hawking radiation) and the **negative-mass hat** infalling (J_neg, Blue), and
the shared brim is the horizon, read as the framework's zero-divisor boundary
(two real, non-zero things whose product is nothing). The "fractal fur" of the
horizon is read as Hawking soft hair (Hawking, Perry, Strominger, 2016: soft
photons and gravitons on the horizon carrying information). That the horizon has
fractal structure at every scale is not part of the soft-hair result; it is
the framework's reading.

*Handedness.* The assignment infalling = J_neg = Blue (and escaping =
Red) follows the "normal chirality" convention of the UniversalSynth README. The
J_red/J_blue record takes J_red as the lower octonion. The two are to be
reconciled by a test, not by relabelling: see `UniversalSynth/README.md`
("Open: handedness") and [14](14_redblue_hamiltonian.md) §3.

## 3. Upside-down versus inside-out  (the exact lemma)

- **Upside-down** is rotation by 180°: same topology, the cone pointing the other way. The infalling hat is the positive hat so rotated.
- **Inside-out** is the conformal inversion of 3-space about the brim sphere, r ↦ R²/r (centre at the tip, R = R_H), direction unchanged.

**Lemma (`ESTABLISHED`).** The inversion is an involution; it fixes the brim sphere
r = R pointwise; it sends the tip (r → 0) to infinity; it exchanges the
exterior r > R and the interior r < R; it preserves angles. Its Jacobian is
(R/r)⁶ in three dimensions. So the brim is the unique fixed set, "the thing that does
not move", which the framework identifies with σ = ½. The identification is the
framework's; the fixed-point statement is exact.

The "Lagrangian unwrapping" of the earlier page, r(t) = (1−t)·r + t·R²/r,
fixes r = R for every t ∈ [0, 1] (check: (1−t)R + tR = R). It is a *chosen*
interpolation, not the solution of a variational problem; "the universe follows
it because it is energetically cheapest" has no action behind it. Also corrected:
the inversion is **not** "the unique angle-preserving map" (in three dimensions
all conformal maps are Möbius transformations, of which inversion is one).

## 4. Does inversion give the dark-matter halo? A test that fails

The earlier page said that the cone fabric, inverted to the interior, "produces the
1/r² density profile of dark-matter halos directly", and that no dark-matter
particle is needed. The profile that gives flat rotation curves is indeed
ρ ∝ r⁻² (the singular isothermal sphere: M(<r) ∝ r, so v² = GM/r is constant).
Whether the inversion produces it can be computed.

**Listing 1 — radial density after inversion** (written for this page; runs cold
with NumPy; seed fixed)

```python
import numpy as np
rng = np.random.default_rng(0)
R, n = 1.0, 2_000_000
bins = np.linspace(0.25, 1.0, 16)
mid = (bins[1:] + bins[:-1]) / 2

# 3-D: uniform density in the exterior shell R..4R, then r -> R^2/r
r = (R**3 + rng.random(n) * ((4*R)**3 - R**3)) ** (1/3)
h, _ = np.histogram(R*R / r, bins)
d = h / (4*np.pi * mid**2 * np.diff(bins))
print('uniform 3-D  slope', round(np.polyfit(np.log(mid), np.log(d), 1)[0], 2))

# cone SURFACE: uniform in area (pdf ~ r), r from R to 4R
r2 = np.sqrt(R**2 + rng.random(n) * ((4*R)**2 - R**2))
h2, _ = np.histogram(R*R / r2, bins)
print('uniform cone surface, surface density slope',
      round(np.polyfit(np.log(mid), np.log(h2 / (mid * np.diff(bins))), 1)[0], 2))
print('same, spread as spherical-shell volume density',
      round(np.polyfit(np.log(mid), np.log(h2 / (4*np.pi*mid**2*np.diff(bins))), 1)[0], 2))
```

```
uniform 3-D  slope -6.02
uniform cone surface, surface density slope -4.01
same, spread as spherical-shell volume density -5.01
```

Result (analytic: a uniform density maps to ρ' ∝ r'⁻⁶ because the Jacobian is
(R/r)⁶): the exterior's uniform density, inverted, is **ρ ∝ r⁻⁶**, not r⁻²;
the cone surface gives −4 (surface) or −5 (as a volume). Since ρ'(r') = ρ(r)·(r/R)⁶ with r = R²/r', an r'⁻² halo would need
the *source* density before inversion to fall as r⁻⁴ (3-D), which is not "uniform on the
cone fabric". **The claim "the 1/r² halo emerges directly from conformal
inversion" is not supported.** This failed result is recorded and not
removed; whatever density the cone fabric has before inversion is an input.

The remaining table, with statuses:

| Null cone | Galaxy (the framework's reading) | Status |
|---|---|---|
| tip, r → 0 | the central black hole (M87*, Sgr A*) | `interpretation`; the EHT images are of horizon-scale emission, not a "tip of an inverted cone" |
| brim, r = R_H | the disk edge, at the BAO-scale radius | the fixed-point property is exact (§3); the BAO-scale identification is not derived |
| fabric, r > R_H | the dark-matter halo | **fails** the 1/r² test (above) |
| helical seams | spiral arms (log spirals, "AGM of the cone") | not derived; no run on this page |
| half-angle of the cone | inclination / Tully–Fisher ratio | not derived |

## 5. Navier–Stokes, BAO, and standard candles

- **The cosmic fluid.** The universe has no free surface, so the free-boundary part of Navier–Stokes is absent; the fluid equation ∂(ρu)/∂t + ∇·(ρu⊗u) = −∇p + μ∇²u + f and ∂_μJ^μ = 0 are stated. The regularity problem is unaffected by this ([106](106_the_navier_stokes_problem.md)).
- **BAO.** The acoustic waves in the early photon–baryon plasma travel at c_s ≈ c/√3 = 0.5774c (reduced by baryon loading) until recombination. Ω_ζΣ = 0.5671 is within 1.8% of c/√3 (ratio 0.9823); the two are different numbers, and the closeness is noted, not used.
- **Standard candles and d\*.** Type Ia supernovae and d_L = (1+z)·r(z) show the transition from deceleration to acceleration at z ≈ 0.6–0.7 (flat ΛCDM with Ω_m = 0.31: z_t = (2Ω_Λ/Ω_m)^{1/3} − 1 = 0.645). The earlier page identified a boundary at z ∼ 0.7 with d*_spec = 0.24600. No derivation links the two numbers, and d*_spec is the measured value, not one of the four faces ([17](17_alpha_omega_d_star.md)). `OPEN`.
- **The Gnarl claim.** "The Gnarl iteration independently converges to Ω_ζΣ" is refuted ([27](27_third_age_CS_paper.md) §3).

## 6. The engine

`witches_hat.py` implements the model its docstring states: the null-cone
pair, the inversion r ↦ R_H²/r with the brim as the fixed point, galaxy
emergence, and the L_dynamic action cone (Lichtenberg attractors "from brim
to point", J_red descending from the point and J_blue ascending from the
brim, with the bubble forming at σ = ½). The operator mapping the earlier page printed
(null → e₁ negate, cone → e₁₁ dereference, horizon → e₂ bind, galaxy → e₁₄
interrupt, Hawking → e₁₂ compose, inversion → e₅ abstract) was **not found** as
code in that file; it stands as a proposed mapping onto the 16 operators of
[15](15_the_monad.md) §2. The animation's frame plan (0–60 pair, 60–100
separation, 100–180 inversion, 180–250 galaxy, 250–300 final) is the script's
design; the frame count is not re-run here.

## 7. Implications claimed, and their standing

| Claim | Standing |
|---|---|
| flat rotation curves without dark matter particles | not supported by the inversion (§4); an isothermal halo is the standard route and is a density input |
| a central black hole in every galaxy as the hat's tip | `interpretation`; supermassive black holes are common in massive galaxies; "every" is stronger than the observations |
| dark energy as the accumulated escaping hat | `CONJECTURE` |
| early massive galaxies (JWST) formed "instantaneously" by inversion | `CONJECTURE`; JWST's early galaxies are an active field of observation and modelling; no calculation here |
| Navier–Stokes regularity | not addressed by this page |

## 8. References

Hawking (1974), *Nature* 248, 30–31. Hawking, Perry & Strominger (2016), *Soft hair on black holes*, PRL 116, 231301.
Penrose (1965), PRL 14, 57. Event Horizon Telescope Collaboration (2019, 2022). Eisenstein et al. (2005), ApJ 633, 560.
DESI Collaboration (2024), BAO measurements from DESI Year 1. Townsend (Gnarl/Popcorn, Ultra Fractal formulary). Wiles (1995), *Annals of Math.* 141.
(Journal and volume details recalled; to be checked against [98](98_provenance_and_citations.md) before use.)

## 9. Related pages

[26 Roadmap and engine status](26_TODO_and_roadmap.md) · [28 Roko's Basilisk](28_rokos_basilisk.md) ·
[30 Lambda paper](30_lambda_paper.md) · [64 L_dynamic](64_l_dynamic.md) · [72 The cosmic telescope](72_the_cosmic_telescope.md)
