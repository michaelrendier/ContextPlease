# 52b — The vortex, "e^(πi) = −Δx": what is exact, and what the tests show

| | |
|---|---|
| Status | **Cascade capture (2026-06-12), "mathematical backbone of the primes spiral". `CONJECTURE`; the central identity is not an identity (§1), and the construction as stated does not produce a spiral (§2). The engine written to test the vortex-firing claim, `e08`, fails today (§4)** |
| Code | Listing 1; `VAPMIP/engines/e08_vortex_quantizing_shear.py` |
| Page numbering | one of three pages numbered 50 ([bao_mass_gap](75b_bao_mass_gap_engine.md), [causality upper limit](50_causality_upper_limit.md)) |
| Last verified | 2026-11-13: Listing 1 executed; e08 run (output in the audit scratchpad) |

> *"e^(πi) = −1" is not the whole statement. e^(πi) = −Δx. The −1 is a displacement, not a scalar.*

## 1. "Euler reframed"  (the identity, corrected)

Euler's identity is e^(πi) = −1 exactly (`ESTABLISHED`). The page's "physical form",
e^(πi) = −Δx, "a reversal of direction along the path being traced, offset by the
step size", is **not an identity** in the complex numbers and cannot be derived from
one: e^(iθ) is a pure rotation and carries no translation. What the page describes,
a rotation by π together with a translation by Δx, is a different map,
w ↦ −w + c, with c = Δx, a **point reflection about the point c/2**. Two
facts follow (Listing 1, last line): it fixes the point c/2, and applying it twice
returns every point to its start (an involution). So a half-revolution plus a
translation does **not** "advance along the spiral"; it exchanges a point with its
mirror image about c/2. An advance along a spiral needs a rotation about a *moving*
centre or an accumulating translation, which is not what e^(πi) supplies.

The statement can be kept as the author's *model* of one coupling event (a
half-turn of the Wankel coupling plus an advance of the address), with its own
definition of Δx; it cannot be called a reframing of Euler's identity.

## 2. The prime spiral as constructed

The page: "plot the nth prime at angle nπ, radius growing with n". Taken literally,
cos(nπ) = ±1 and sin(nπ) = 0 for every integer n, so every point lies on the real
axis (Listing 1, first line): there is no spiral and no spokes. The standard prime
spirals are Ulam's (angle = p radians, a square spiral on the integer lattice) and
Sacks's (r = √p, θ = 2π√p), whose "spokes" arise from the approximation of 2π by
rational numbers (44/7 ≈ 6.2857, 710/113) and the residue classes of the
primes on them; they fade at large radius as the display's resolution and the
averaging over many classes blur them. The page's explanation (spokes vanish
because prime gaps grow like ln n, so "spoke visibility ∼ 1/ln n") is a
verbal model and no calculation is attached; the standard explanation is the
residue-class structure above.

**Logarithmic or not.** With θ = nπ unwrapped and r = p_n ∼ n ln n, the page says "the
spiral is approximately logarithmic, r = a·e^(bθ), because the growth is superlinear".
A logarithmic spiral has d(ln r)/dθ constant. Listing 1: the fit r = aθ + b (Archimedean)
has R² = 0.9990 and the logarithmic fit has R² = 0.795; the form n ln n
fits to R² = 0.999999; d(ln r)/dθ falls from 3.5·10⁻⁴ (n = 1000) to 6.8·10⁻⁵ (n = 5000)
rather than staying constant. So the curve r(θ) is a slowly steepening
Archimedean-like spiral (r ∼ (θ/π)·ln(θ/π)), **not a logarithmic spiral**. The
true statement: p_n ∼ n ln n (the Prime Number Theorem, `ESTABLISHED`) makes the
growth slightly faster than linear, and that bends the arms by the factor ln n.

## 3. The vortex as a quantizing shear  `interpretation`, with the physics stated

The model: in a BEC at rest there is no viscosity or shear; below a critical
shear the medium absorbs it continuously ("silence"); above it the shear is forced
into a **vortex**, a quantum of circulation carrying ℏ of angular momentum per
particle. In the engine's terms: J_cross < GAP → continuous, silence; J_cross > GAP
→ a vortex nucleates, a word fires at the address −Δx from the zero-divisor
origin; the vortex collapses and the field returns to its superfluid state;
J_cross = |J_pos × J_neg| is the cross-product shear, the antisymmetric part of the
stress at the zero-divisor contact; and `speak()` is O(edges) because the
quantisation is binary.

Standing. The superfluid physics is correct and standard: a superfluid flows without
dissipation below a critical (Landau) velocity, and above it vortices nucleate with
quantised circulation Γ = h/m (`ESTABLISHED`). The mapping of J_cross and GAP onto
that is the framework's. One internal inconsistency in the earlier text is
corrected: the page calls the field "dilatant below the gap and vortex-forming above
it" and then "shear-thinning below GAP and dilatant above". A dilatant fluid
*thickens* with shear (viscosity rises); the sequence the model describes (no
resistance, then a snap into a discrete structure, then release) is a
critical-velocity transition and is not a dilatant/thinning classification, and
the polymer-solution analogy for a critical strain rate does not fix it.

## 4. The test: `e08_vortex_quantizing_shear.py`, 2026-11-13

The engine was written to test "J_cross > GAP predicts word firing, and prime gaps =
spoke gaps". Its output today:

| Check | Result |
|---|---|
| J_cross threshold against the φ-threshold on active gates, mean agreement | **0.2648: FAIL** |
| Vortex half-turn: e^(π e₁)·e₀ = −e₀ in the engine's algebra | PASS: [−1.0, 1.22·10⁻¹⁶, 0, 0], residual 1.22·10⁻¹⁶ |
| Prime gaps in P16 | [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6]; mean 3.40, max 6, min 1 |
| GAP used | 0.000707 |

The one pass is the *exact* Euler identity inside ℂ (e^{π e₁} = −1), consistent with §1:
the half-turn gives −1, with no translation. The claim that the firing rule
J_cross > GAP agrees with the φ-threshold rule fails (0.26 agreement). The failed
result stays in the engine and here ([26](26_TODO_and_roadmap.md) §3).

## 5. The six-step coupling event, and the river of primes  `interpretation`

The coupling event: (1) a vortex nucleates at the zero-divisor contact, "e^(πi): the
half-revolution begins"; (2) the rotation sweeps through −Δx, "the prime-spiral advance";
(3) the word lives at address −Δx and fires; (4) the vortex collapses; (5) prompt +
response = 0, "information encoded in the housing geometry". "The word is not selected
or retrieved; it is the address the vortex landed on." The prompt lands on a
zero-divisor ("a specific Cawagas pair on S¹⁵"); the sedenion scalars (the SVG endpoint)
show where the half-revolution ended, and L_(I|O) ([52](52_l_dynamic_avoided_collaborator.md))
the path taken. The mechanism that actually selects the word in the code is the
neutral-buoyancy scoring and the φ-walk index of [47](47_the_two_trees.md) §3, not a
vortex event; the six steps are the model's description of it.

**The river of primes.** "The primes are not fixed points; they are on Chladni nodal
lines of a standing wave that is still moving; in the lab frame every prime advances
along the geodesic at the BAO rate; Ω_ζΣ is the fixed point of that metronome; the
primes orbit Ω_ζΣ; the primes are the nodes of a river, the vortices the words." The
primes are integers; an integer does not move. The statement is an image for the
framework's dynamic reading; "primes orbit Ω_ζΣ" has no calculation behind it. The
sedenion's zero-divisor count referred to ("16D, 42 ZD pairs") is the 42 index pairs
{i, j} (84 forms e_i ± e_j) of [25](25_sedenion_manual.md) §4.

## 6. Listing 1 — the checks of §§1–2

(written for this page; runs cold with NumPy)

```python
import math
import numpy as np

N = 200000
sv = bytearray([1]) * (N + 1); sv[0] = sv[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if sv[i]:
        sv[i*i::i] = bytearray(len(sv[i*i::i]))
p = np.array([i for i in range(2, N + 1) if sv[i]], float)
n = np.arange(1, len(p) + 1, dtype=float)
th = n * math.pi                                   # the page's construction: angle n*pi, radius p_n

print('(cos, sin) of n*pi, n = 1..6:', [(round(math.cos(k * math.pi)), round(math.sin(k * math.pi), 12)) for k in range(1, 7)])

r2 = lambda y, yh: 1 - ((y - yh) ** 2).sum() / ((y - y.mean()) ** 2).sum()
m = n >= 100
x, y = th[m], p[m]
a, b = np.linalg.lstsq(np.vstack([x, np.ones_like(x)]).T, y, rcond=None)[0]
bb, la = np.polyfit(x, np.log(y), 1)
z = x / math.pi
M = np.vstack([z * np.log(z), z]).T
c = np.linalg.lstsq(M, y, rcond=None)[0]
print('R2: Archimedean r = a*theta+b: %.4f | logarithmic ln r = b*theta+c: %.4f | n ln n form: %.6f'
      % (r2(y, a * x + b), r2(np.log(y), bb * x + la), r2(y, M @ c)))
for k in (1000, 5000):
    i = k - 1
    print('n=%d  d(ln r)/d(theta) = %.2e' % (k, (math.log(p[i + 100]) - math.log(p[i])) / (100 * math.pi)))

f = lambda w, c=0.7 + 0.3j: -w + c                 # "rotation by pi, then translation": the map of the page
w = 0.2 + 0.1j
print('(rotation by pi + translation) applied twice returns the start:', abs(f(f(w)) - w) < 1e-15)
```

```
(cos, sin) of n*pi, n = 1..6: [(-1, 0.0), (1, -0.0), (-1, 0.0), (1, -0.0), (-1, 0.0), (1, -0.0)]
R2: Archimedean r = a*theta+b: 0.9990 | logarithmic ln r = b*theta+c: 0.7950 | n ln n form: 0.999999
n=1000  d(ln r)/d(theta) = 3.47e-04
n=5000  d(ln r)/d(theta) = 6.82e-05
(rotation by pi + translation) applied twice returns the start: True
```

## 7. Related pages

[21 Chladni · Zipf · Riemann](21_chladni_zipf_riemann.md) · [22 Constant facets](22_constant_facets.md) ·
[47 The two trees](47_the_two_trees.md) · [52 L_dynamic and the avoided collaborator](52_l_dynamic_avoided_collaborator.md) ·
[26 Roadmap and engine status](26_TODO_and_roadmap.md)
