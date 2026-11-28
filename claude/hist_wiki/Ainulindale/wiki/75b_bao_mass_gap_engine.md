# 75b — The mass-gap engine Δ (`bao_mass_gap`)

| | |
|---|---|
| Module | `bao_mass_gap` — `ValaQuenta/modules/bao_mass_gap/` · class `BaoMassGapModule` · v0.131 · confidence floor ESTABLISHED (as registered) |
| API page | `ValaQuenta/wiki/bao_mass_gap.md` · notebook `ValaQuenta/notebooks/core/19_bao_mass_gap.ipynb` |
| Registry | 7 equations: `summary`, `gap_value`, `spectral_residue`, `gap_identity`, `bao_consistency`, `mtheory_compactification`, `validate` |
| Last verified | 2026-11-13: every equation run through `registry.run('bao_mass_gap.<name>', {})`; Listing 1 executed |
| Page numbering | three pages carry the number 50 (this one, [50 causality upper limit](50_causality_upper_limit.md), [50 vortex quantizing shear](52b_vortex_quantizing_shear.md)); renumbering is part of the index repass |

## 1. What it computes

```
Δ = Ω_ζΣ − d*·ln 10 = 0.5671432904097838 − 0.246·2.302585092994046 = 0.000707357533248576
```

The two constants are the "ceiling" Ω_ζΣ = W(1) (the thermal-information bound)
and the "floor" d*·ln 10 = 0.5664359329. **Which d\* this is matters** ([17](17_alpha_omega_d_star.md) §3.2):
the engine carries **d*_spec = 0.24600**, the *measured* spectral value, not the
Boundary face 0.24631. With the Boundary/Flow value Ω_ζΣ/ln 10 the gap is zero by
construction; the engine's positive Δ exists because the measured d*_spec is
smaller. "Ω_ζΣ and d* taken from opposite ends of the Ĥ_RB operator, one value,
zero free parameters" therefore needs the qualification that d*_spec is an input
carried to five decimals.

`gap_value` returns the derivation chain as an ordered list ("take Ω_ζΣ …; take
D* = 0.246 …; convert; subtract; the residue is positive; the gap exists").
"The gap exists because the residue is positive": a difference of two constants
being positive is arithmetic; calling it a mass gap is the framework's reading
([123](123_sigma_rb_mass_gap_calibration.md)).

## 2. "The residue" and the explicit formula

The page's argument: Δ is a *residue*, what is left after the explicit formula
decomposes the prime distribution,

ψ(x) = x − Σ_ρ x^ρ/ρ − ln 2π − ½ ln(1 − x⁻²)  (von Mangoldt; `ESTABLISHED`),

with the x term read as the de Sitter ground state, the sum as one acoustic standing
wave per zero, and the band between the floor and the ceiling "absorbed by no
standing wave". The engine's `spectral_residue` evaluates the explicit formula
(Σ_ρ x^ρ/ρ = 0.13108455 over 20 zeros at x = 10, ψ(10) = 7.83201418) and moves to
the coordinate x_BAO = exp(1/Ω_ζΣ) = 5.83120014. Standing:

- the explicit formula is an exact identity about ψ(x), and the engine reproduces it numerically;
- Δ is **not a term of that formula**: it is the difference of two constants, and "independent of the number of zeros summed (residue spread exactly 0.0)" is true because it never involves the zeros. The engine's check "the BAO residue reproduces Δ exactly" is a tautology;
- the identification of Δ with "what the standing waves leave" is the framework's reading, with no derivation from ψ(x).

## 3. How exact is "Δ = 1/(1000√2)"?

The page's headline and `gap_identity`: Δ = 1/(1000√2) = 0.000707106781.

- Δ = 0.000707357533 and 1/(1000√2) = 0.000707106781: they differ by 2.508·10⁻⁷ (0.0354%); **they agree to three significant figures, not exactly** (the engine's own check is `identity_3sf: True`; the page's "Δ = 0.0007073575 = 1/(1000√2)" is an approximate equality).
- The d* that would make it exact is 0.2460001089, which differs from the carried 0.24600 by 1.089·10⁻⁷, "inside the last carried digit" (the engine's wording).
- **That last-digit allowance is what limits the claim.** d* is carried to five decimals, so d*_spec = 0.24600 ± 5·10⁻⁶ and the uncertainty of Δ is ± 5·10⁻⁶·ln 10 = ±1.15·10⁻⁵, which is **±1.6% of Δ** itself. Any value of Δ in that window is consistent with the carried d*.

**Listing 1 — how special is the match inside that window?** (written for
this page; runs cold)

```python
import math
Om = 0.5671432904097838; L = math.log(10)
D = Om - 0.246 * L; w = 5e-6 * L                 # the window set by d*'s last digit
forms = {}
for k in range(1, 6):
    for m in range(1, 41):
        forms[f'1/(10^{k}*sqrt({m}))'] = 1 / (10**k * math.sqrt(m))
        forms[f'1/(10^{k}*{m})'] = 1 / (10**k * m)
hits = [(n, v) for n, v in forms.items() if abs(v - D) <= w]
print('window +/-', round(w, 8), 'around Delta =', round(D, 9), '(relative +/-%.3f%%)' % (100 * w / D))
print('forms tested:', len(forms), ' inside window:', len(hits))
for n, v in hits:
    print('  ', n, round(v, 9))
```

```
window +/- 1.151e-05 around Delta = 0.000707358 (relative +/-1.628%)
forms tested: 400  inside window: 2
   1/(10^2*14) 0.000714286
   1/(10^3*sqrt(2)) 0.000707107
```

Of 400 simple closed forms 2 lie inside the window: 1/(1000√2) and 1/1400. Over
the several decades these forms span, about one hit is expected by chance. So the
match is **consistent with the carried precision and has weak discriminating
power**; it would become significant only if d*_spec were measured to ~7 digits,
or if the 10³ were derived. The page already says the 1/√2 is accounted for (the
first Cayley–Dickson doubling; 1/√2 = sin 45°, the Red/Blue symmetry point) and the
10³ is not derived. Write it 1/(1000√2) or 1/√(2·10⁶), **not** 1/√2000 = 0.02236
(31.6× too large); that guidance stands.

## 4. Precision of d*  (table kept, with the status of each value)

| Value | Source | Gap |
|---|---|---|
| d*_spec = 0.24600 | measured, carried; ACTIVE in this engine | 0.000707 |
| d*_taut = Ω_ζΣ/ln 10 = 0.246307201… | the Flow face; zero gap by construction, not a result | 0 |
| d*_exact = 0.2460001089 | the d* at which Δ = 1/(1000√2) exactly | — |

The residual 2.508·10⁻⁷ measures the precision of d*, not the identity.

## 5. Compactification  `CONJECTURE`

"11 = 4 observable + 7 compact; the compact 7 carry G₂ holonomy, G₂ = Aut(𝕆); the
seven directions are e₁…e₇, algebraic and never spatial; the compactification
scale is Δ; Δ is computed so it is not a modulus; no moduli, no landscape: 10⁵⁰⁰ → 1."
The engine checks the dimension arithmetic exactly (`Fraction`: 11 − 4 = 7;
`count_consistent: True`). That a computed 7·10⁻⁴ sets the compactification scale of
M-theory, and that the landscape reduces to one vacuum, are not derived anywhere
in the repository ([25](25_sedenion_manual.md) §6: "no derivation of the
11-dimensional structure from the number 0.000707 is given").

## 6. Acoustic scale  (a unit mismatch)

Planck 2018: r_s = 147.09 ± 0.26 Mpc, fractional precision 0.26/147.09 = 0.177%.
The engine reports Δ/σ_BAO = 0.000707/0.001768 = 0.4002 and concludes "Δ is a resolvable
feature of the acoustic spectrum". **The comparison does not carry that meaning:**
Δ is a dimensionless gap between two information-unit constants, while 0.177% is
the fractional error of a length; no map from Δ to a fractional shift of the sound
horizon is given, so the ratio 0.4 has no physical interpretation, and a
0.4-error-bar quantity would in any case not be "resolvable" (that would need a
ratio above 1). The check `bao_resolvable: True` rests on the engine's own
threshold (> 0.1), chosen without justification. Recorded, not repaired.

## 7. The seven checks of `validate`

`gap_positive`, `gap_in_range`, `identity_3sf`, `identity_in_d_star_precision`,
`residue_equals_gap`, `bao_resolvable`, `dimension_count_exact`: all True (7/7),
reproduced today. By §§2–6, three of the seven are structural truths
(`gap_positive`, `dimension_count_exact`, and the numerical form of
`identity_3sf`), three are tautologies or consistency-with-precision
(`residue_equals_gap`, `identity_in_d_star_precision`, `gap_in_range`), and one rests on an
unjustified threshold (`bao_resolvable`). "7/7" therefore certifies that the code
runs consistently, not that the physical claims hold.

## 8. Entry points  (corrected)

```bash
python3 -m ValaQuenta --info      # bao_mass_gap registers first
python3 -m ValaQuenta --curses    # derivation console, top module
```

(The earlier page printed `python3 -m ainulindale_engine …`, the pre-ValaQuenta
package name.)

## 9. Related pages

[07 Berry–Keating](07_berry_keating_engine.md) · [17 A_fermat · Ω_ζΣ · d*](17_alpha_omega_d_star.md) ·
[123 σ_RB and the mass gap](123_sigma_rb_mass_gap_calibration.md) · [30 Lambda paper](30_lambda_paper.md) ·
`FourthAgePapers/addenda/addendum_VIII_BAO_mass_gap.md`
