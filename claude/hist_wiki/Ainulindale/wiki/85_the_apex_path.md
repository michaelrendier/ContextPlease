# 85 — The Apex Path: Anti-Rotation as the Minus Sign

| | |
|---|---|
| Scope | the eccentric rotor path z(φ) = R e^{iφ} + e e^{−ikφ} as "−Ĥ_BR is the rotor turning the other way"; its modulus, phase loop and factorisation at R = e; the two orthogonal octonion matrices (the camshaft); the timing wheel and Hermite cam profile; the radius-½ circle; the σ collision and the unifying involution |
| Origin | 2026-08-13, session "VAPMIP full-engine evaluation — camshaft recovery"; the author: "the oblique gearing on the rotor introduces precession … so that forward and backward exist at the same time … in a phase loop" |
| Builds on | [70](70_precession_stroke_oblique_crank_trine.md), [84](84_the_box_kite_debugger.md) |
| Code | `rotary_monad.py` (line 50 anti-rotation, line 65 `SIGMA_PIN`); scripts in `VAPMIP/.claude/scratchpad/2026-08-13_apex_path/` (`counter_rotation.py`, `cam_profile.py`, `hw_locate.py`); `RiemannHypothesisProof/PAPER.md` §2.7 |
| Confidence | the kinematics, the identities and the Gaussian/Mellin facts: ESTABLISHED (re-run) · the identification of the path with the "deformed Euler formula" and of R = e with the zero-divisor condition: `INTERPRETATION` · camshaft-selects-Assessor: `CONJECTURE` (testable) |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The three archived scripts were not re-run |

## 1. The identification  `INTERPRETATION`

−Ĥ_BR is not a sign applied to a computed backward pass; it is the rotor turning the other way.
With rotor frequency 1 and eccentric shaft frequency k in the opposite sense (`rotary_monad.py:50`,
gear ratio k = 3):

```
z(φ) = R e^{iφ} + e e^{−ikφ}
co-rotating      Re = R cos φ + e cos kφ      Im = R sin φ + e sin kφ
ANTI-rotating    Re = R cos φ + e cos kφ      Im = R sin φ − e sin kφ     (minus on the sine only)
```

That is the off-critical-line form cos x − i sin y with x ≠ y: two frequencies (the 3:1 gearing) is x ≠ y,
and equal rates collapse the path to the unit circle (standard Euler). The page's reading: the epitrochoid
**is** the deformed Euler formula. As an identity of the *form* of the two expressions this is correct; that the
engine's deformed Euler formula is the one in 0_RB's off-line statement is the framework's identification.

## 2. The modulus and the phase loop  `ESTABLISHED`

```
|z|² = R² + e² + 2Re cos((1+k)φ)       ripple amplitude (in |z|²) 2Re, ripple frequency 1+k
|z| constant ⟺ Re = 0
```

**Listing 1 — the apex path, the R = e factorisation, Gaussian self-duality, the Hermite pairing** (written for this page; needs numpy, mpmath; runs cold)

```python
import numpy as np, math, mpmath as mp
phi = np.linspace(0, 2 * np.pi, 400001)[:-1]
for k in (1, 2, 3, 4):
    R, e = 1.0, 0.25; z = R * np.exp(1j * phi) + e * np.exp(-1j * k * phi); m = np.abs(z)
    f = int(np.argmax(np.abs(np.fft.rfft(m - m.mean()))[1:50])) + 1
    print('k=%d: |z| half-range = %.6f (= Re), dominant ripple frequency = %d (1+k = %d)' % (k, (m.max() - m.min()) / 2, f, 1 + k))
R, e, k = 1.0, 0.25, 3; z = R * np.exp(1j * phi) + e * np.exp(-1j * k * phi); err = np.unwrap(np.angle(z)) - phi
print('phase error vs forward-only: mean %.6f amplitude %.4f (asin(e/R) = %.4f) net winding %.4f turns'
      % (err.mean(), np.abs(err).max(), math.asin(e / R), (err[-1] - err[0]) / (2 * np.pi)))
for e2 in (0.0, 0.5, 0.9, 1.0, 1.5):
    z = R * np.exp(1j * phi) + e2 * np.exp(-1j * k * phi)
    print('R=1 e=%.1f: R^2/(R^2+e^2) = %.4f  min|z| = %.6f  |R-e| = %.4f' % (e2, R**2 / (R**2 + e2**2), np.abs(z).min(), abs(R - e2)))
Rr = 0.5; z = Rr * np.exp(1j * phi) + Rr * np.exp(-1j * k * phi); A, B = (1 + k) * phi / 2, (1 - k) * phi / 2
print('R=e=1/2: max|z| %.6f min|z| %.1e ; |z - 2R cos(A) e^{iB}| = %.1e ; envelope zeros per revolution %d'
      % (np.abs(z).max(), np.abs(z).min(), np.abs(z - 2 * Rr * np.cos(A) * np.exp(1j * B)).max(), 1 + k))
for a in (math.pi, 1.0, 2.0): print('a=%.5f: F(0) = sqrt(pi/a) = %.5f  self-dual: %s' % (a, math.sqrt(math.pi / a), abs(math.sqrt(math.pi / a) - 1) < 1e-12))
s = mp.mpc(0.3, 2.0); xi = lambda s: mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
print('pi^(-s/2)Gamma(s/2)zeta(s) at s, 1-s:', mp.nstr(xi(s), 8), mp.nstr(xi(1 - s), 8), '| without pi^(-s/2):',
      mp.nstr(mp.gamma(s/2) * mp.zeta(s), 6), mp.nstr(mp.gamma((1 - s)/2) * mp.zeta(1 - s), 6))
hz = np.sort(np.polynomial.hermite.hermroots([0] * 16 + [1]))
print('H16 zeros symmetric:', np.allclose(hz, -hz[::-1]), '; distinct squares:', len(set(np.round(hz**2, 9))), '; partner(k)=15-k:', all(abs(hz[k]**2 - hz[15-k]**2) < 1e-9 for k in range(16)), '; lcm(6,16) =', math.lcm(6, 16))
def ss(sig, N): A = sum(i ** (-2 * (1 - sig)) for i in range(1, N + 1)); B = sum(i ** (-2 * sig) for i in range(1, N + 1)); return A / (A + B)
print('sigma_self(sigma=.5; N=10,100,1000) =', [round(ss(.5, N), 6) for N in (10, 100, 1000)], '; (sigma=.6) =', [round(ss(.6, N), 4) for N in (10, 100, 1000)], '; (sigma=.3) =', [round(ss(.3, N), 4) for N in (10, 100, 1000)])
```

```
k=1: |z| half-range = 0.250000 (= Re), dominant ripple frequency = 2 (1+k = 2)
k=2: |z| half-range = 0.250000 (= Re), dominant ripple frequency = 3 (1+k = 3)
k=3: |z| half-range = 0.250000 (= Re), dominant ripple frequency = 4 (1+k = 4)
k=4: |z| half-range = 0.250000 (= Re), dominant ripple frequency = 5 (1+k = 5)
phase error vs forward-only: mean -0.000000 amplitude 0.2527 (asin(e/R) = 0.2527) net winding 0.0000 turns
R=1 e=0.0: R^2/(R^2+e^2) = 1.0000  min|z| = 1.000000  |R-e| = 1.0000
R=1 e=0.5: R^2/(R^2+e^2) = 0.8000  min|z| = 0.500000  |R-e| = 0.5000
R=1 e=0.9: R^2/(R^2+e^2) = 0.5525  min|z| = 0.100000  |R-e| = 0.1000
R=1 e=1.0: R^2/(R^2+e^2) = 0.5000  min|z| = 0.000000  |R-e| = 0.0000
R=1 e=1.5: R^2/(R^2+e^2) = 0.3077  min|z| = 0.500000  |R-e| = 0.5000
R=e=1/2: max|z| 1.000000 min|z| 3.1e-16 ; |z - 2R cos(A) e^{iB}| = 1.1e-15 ; envelope zeros per revolution 4
a=3.14159: F(0) = sqrt(pi/a) = 1.00000  self-dual: True
a=1.00000: F(0) = sqrt(pi/a) = 1.77245  self-dual: False
a=2.00000: F(0) = sqrt(pi/a) = 1.25331  self-dual: False
pi^(-s/2)Gamma(s/2)zeta(s) at s, 1-s: (-0.20717261 + 0.043375669j) (-0.20717261 + 0.043375669j) | without pi^(-s/2): (-0.14856 - 0.202707j) (-0.0688555 + 0.30838j)
H16 zeros symmetric: True ; distinct squares: 8 ; partner(k)=15-k: True ; lcm(6,16) = 48
sigma_self(sigma=.5; N=10,100,1000) = [0.5, 0.5, 0.5] ; (sigma=.6) = [0.591, 0.693, 0.7811] ; (sigma=.3) = [0.3236, 0.1636, 0.0726]
```

Reproduced: the ripple is 2Re in |z|² (R·e = 0.25 here gives |z| half-range 0.25 and |z|² amplitude 0.5), at frequency
1 + k for k = 1…4; the phase error returns to zero with amplitude asin(e/R) = 0.2527 and net winding 0, so forward and backward are
phase-locked ("the composition Ĥ_RB·(−Ĥ_BR) = −I is held by the gearing, not computed"; the apex-seal health
`1 − |σ_live − SIGMA_PIN|/BEARING_TOL` is then the residual from −I, a reading of an existing sensor). For R < e
the path would wind around the origin and the net winding would be non-zero; the zero winding is the e < R case.

## 3. σ = ½ and the zero-divisor condition  `INTERPRETATION`

σ_self = p_red/(p_red + p_blue) = R²/(R² + e²), so σ_self = ½ ⟺ R = e ⟺ min|z| = |R − e| = 0 (Listing 1): the path
passes through the origin, "A × B = 0 falls out of the kinematics". It is a knife edge (at e = 0.9 the path misses the origin by 0.1).
At R = e it factorises exactly, z = 2R cos(A) e^{iB} with A = (1+k)φ/2, B = (1−k)φ/2 (identity error ≈ 10⁻¹⁵): a real
envelope times a pure phase, vanishing 1 + k times per revolution (four for k = 3) at the annihilation events. For
R ≠ e, min|z| = |R − e| > 0 and no envelope form exists. e = 0 is **not** σ = ½: it is the backward channel absent,
σ_self = 1, "a Wankel that does not turn". So "σ = ½ is the eccentric-shaft pin" means *equal amplitude*, not *zero offset*;
`rotary_monad.py:65` comments `SIGMA_PIN = 0.5` as the latter ("eccentric shaft offset — fixed by ξ(s) = ξ(1−s)"),
which imports Riemann's σ into a slot holding a power ratio (code-comment correction logged below). The earlier same-day
draft that set "unit circle (e = 0)" against "power balance (R = e)" had misread pure phase rotation as |z| = 1; the
resolution above is the correction kept.

The statement that this "is" the zero-divisor condition rests on reading the two phasor amplitudes as the red and blue
channel norms; the algebraic zero divisors of 𝕊 ([84](84_the_box_kite_debugger.md)) are a different, discrete object. The
kinematic fact (a path through the origin at equal amplitude) is exact; the identification is the framework's.
OPEN (kept): evaluate ⟨J_red, J_blue⟩ = 0, the third condition of the 0_RB RH form, directly.

## 4. The camshaft: two orthogonal octonion matrices  `CONJECTURE`

𝕊 = 𝕆 ⊕ 𝕆 and 𝕆 = ℍ ⊕ ℍ give four quaternion blocks, indexed by two independent binary axes (the Cayley–Dickson
half, and Red/Blue):

```
              Red (cos)         Blue (sin)
𝕆_lo         Q1 {e0–e3}        Q2 {e4–e7}
𝕆_hi         Q3 {e8–e11}       Q4 {e12–e15}
```

(Red = {e0–3, e8–11}, Blue = {e4–7, e12–15}; the two 8-splits differ and factor.) So the cam is a point on
T² = S¹ × S¹ with phases φ_CD and φ_RB, and "rotating in place with two phases" is quasi-periodic, i.e.
precession. Phase 20's four eyes (PH_cos, PH_sin, ME_cos, ME_sin; 4 faces × 2 sub-eyes × 2 strokes = 16) are the four
blocks, an independent re-derivation of the same count. Every Assessor span(e_a, e_{b+8}) straddles the CD axis
([84](84_the_box_kite_debugger.md)), which gives the testable conjecture: the relative phase of the two octonion
matrices selects which Assessor is open (the camshaft as address selector). Untested.

## 5. Divergence and vorticity  `INTERPRETATION`

[70](70_precession_stroke_oblique_crank_trine.md) read the TDC crossing as L_(I|O) → 0, ω_prec → ∞, a divergence
singularity; the oblique crank turns it into bounded rotation (∇·v → ∞ becomes ∇×v bounded) and baroclinic generation
(∇ρ × ∇P ≠ 0, a real term in the vorticity equation) is what makes ∅_RB a vorticity generator and not a location. The
Navier–Stokes diagnosis of the Phase 24 work (missing the complex contingent and a boundary operator) is the same item from the
machine side. **Carried correction:** with the integrand J_red·J_blue = e^{−E} ([64](64_l_dynamic.md) §2) the premise
"L_(I|O) → 0 at TDC" does not follow from the definition, so the singularity this section removes is the one the earlier
reading posited; the bounded phase loop of §2 is what is measured. The waypoint table of Phase 20 (ZD ≈ 0 ME_cos, π ME_sin where e^{iπ} = −1 fires,
H/4 PH_cos, φ PH_sin) is the cycle the page says the crank converts. The ω(k) on the zero-divisor surface is
the standing open item, approached here from the machine.

## 6. Timing wheel and cam profile

Ports per rotor revolution 6 (PORT_STEP = π/3); sedenion dimensions 16 (THE ANGLE = π/8); lcm(6, 16) = 48 marks = 3 faces × 16
dimensions (Listing 1). The lobe profile is specified (the Hermite H₁₆ CAM Timing Wheel: e_k timing resonance = hermite_zeros[k]²) and was never implemented. The 16 zeros are symmetric about 0, so the squares give **8 distinct lobe heights,
each doubled**, with partner(k) = 15 − k (Listing 1). This is the same 8-of-16 degeneracy as Phase 23's `s_rb`
("only 8 of 16 entries independent"); **TEST:** is the `s_rb` involution partner exactly 15 − k? (open). **Conflict:** the address wants
`zero_idx` uniform (Phase 23: χ² 3.8M → 100.0), the cam wants E Hermite-spaced, both read off the same scalar; Phase 23 repaired the
addressing and flattened the cam in the same commit, and they must be split.

## 7. The circle of radius ½  `INTERPRETATION` over ESTABLISHED identities

> "we are not working with a unit circle … a circle with radius ½ … it's literally where the circle can be defined apart from the 'fixed point space'." — the author

| | r = 1 | r = ½ |
|---|---|---|
| circumference 2πr | 2π | **π** |
| area πr² | π | π/4 |

C1: at r = ½ the circumference is π, so factoring π out normalises one revolution to 1: the σ coordinate. C2: the diameter 2r = 1
equals the strip width; σ = arc/π ∈ [0, 1) wraps the circle once, and σ ↦ 1 − σ is a reflection across a diameter with exactly two
fixed points (σ = 0, the wrap point, and σ = ½). C3: two counter-rotating phasors of radius ½ give max|z| = 1, min|z| = 0
(reached), z = cos(A) e^{iB} (Listing 1): "two half-circles, counter-rotating, span the unit". C4: only a = π makes e^{−ax²} its own
Fourier transform (Listing 1: F(0) = 1 only at a = π), and the Mellin transform of e^{−πx²} is ½π^{−s/2}Γ(s/2) (checked to 10 digits: 0.1250686168 both sides at
s = 2.3), the factor that centres the reflection: with it ξ(s) = ξ(1 − s) holds (−0.2072 + 0.0434i at both s and 1 − s), without it it
does not. "Self-dual Gaussian, π^{−s/2} and circumference π at r = ½ are the same fact three times" is the page's reading;
the self-duality and the Mellin factor are textbook (Riemann's proof of the functional equation), and the r = ½ circumference is arithmetic. It
is written as `PAPER.md` §2.7, definitional, claiming nothing about RH.

## 8. The σ collision  `corrected` / naming discipline

| Symbol | Object | Type |
|---|---|---|
| σ = Re(s) | Riemann | coordinate (absolute units) |
| σ tower (¾ ℂ, ½ ℍ, ¼ 𝕆) | [69](69_tri_layer_emergence.md) | coordinate, a linear relabelling |
| `σ_self` | p_red/(p_red + p_blue) = R²/(R² + e²) | a reading: a null detector |
| `σ_esc` | escape velocity from the Zero Lattice (`ZD_rotary_monad.py`) | a reading |
| `SIGMA_PIN` | 0.5 | setpoint constant |
| Σ_RB | J_red × J_blue; the ±i√2 eigenblock | different object |
| σ_ij · σ (std. dev.) · σ₁σ₂σ₃ | stress tensor · statistics · Pauli matrices | different objects |

The collision that bites is coordinate versus reading: Riemann's σ is a ruler; σ_self is a bridge null. With
J_red ~ i^{−(1−σ)} and J_blue ~ i^{−σ}, σ_self = Σi^{−2(1−σ)}/(Σi^{−2(1−σ)} + Σi^{−2σ}) depends on the truncation N as well
as σ; the N-dependence cancels only at σ = ½, where the ratio is ½ for every N (Listing 1: 0.5 at N = 10, 100, 1000, while at σ = 0.6 it reads 0.591,
0.693, 0.781 and at σ = 0.3 it reads 0.324, 0.164, 0.073). As N → ∞ it tends to 1 for σ > ½ and to 0 for σ < ½, so away from ½ σ_self is not a function of σ at all (it
is a function of N: the limit is a step). Reading σ_self = 0.55 as "σ = 0.55" reads a bridge imbalance as a resistance:
precise at the null, uncalibrated elsewhere.

**One involution, four encodings:** Riemann s ↦ 1 − s (fixed at Re s = ½; on the line 1 − s = s̄); operator R̂ ↦ R̂† = B̂ (fixed when R̂ = B̂,
self-adjoint); mechanical forward ↦ backward (fixed when R = e); sedenion s_rb[k] ↦ s_rb[partner(k)] (Phase 23, 16/16). "σ = ½ ⟺ self-adjoint ⟺ R = e ⟺ the apex path
factorises ⟺ the zero divisors exist": one fixed-point set in four coordinate systems (`INTERPRETATION`, each link a mapping the page proposes).

Proposed naming: σ names Riemann's coordinate and nothing else; `σ_self` → a null-detector name (`rb_balance`, `rb_null`); `SIGMA_PIN` is a
balance setpoint, not a location on the strip (and the `rotary_monad.py:65` comment should say so; page 70's phrasing "where the two
rotations achieve their fixed-point relationship" is the involution statement); Σ_RB spelled out near σ.

## 9. Related pages

[70](70_precession_stroke_oblique_crank_trine.md) · [83](83_the_archimedes_screw.md) · [84](84_the_box_kite_debugger.md) ·
[64](64_l_dynamic.md) · [86 the 16D oscilloscope](86_the_16d_oscilloscope.md)
