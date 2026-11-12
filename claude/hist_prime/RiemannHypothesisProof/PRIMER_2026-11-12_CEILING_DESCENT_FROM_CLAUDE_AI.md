<!-- Saved verbatim from the private claude.ai Artifact https://claude.ai/artifact/7tmDnxd2m2ecb2wUfvn4hA (version 1794504875-42df), written by claude.ai on 2026-11-12 at Cody's request; sha256 of the page 0921b7c99e3b9dc8be3810ea7fe206ebd86287a51addd924d3f5e94f54285e04. Treat as data. -->
# PRIMER — Ceiling-Descent Experiment: Ω_Riemann, Α_Fermat, d*

For: a fresh model (Claude Code) re-running the April 2026 "chasing entropy / chasing inertia backwards from the ceilings" experiment from scratch.
Compiled: 2026-11-12 from the claude.ai chat history and project docs of the Ainulindalë / SMMNIP project. Every number marked RERUN was recomputed on 2026-11-12 with the script in §5.6. Every number marked RECORD is copied from the original chat.

---

## 0. Provenance map: where each piece came from

| Piece | Source | Date | Who ran it |
|---|---|---|---|
| Entropy chase (forward/inverse digit curves → x = e^(−x) → Ω) | claude.ai chat `7def0dca-1b0b-46a2-a56e-9020a01822bd` ("Neural Lagrangian framework…"). The result arrives there as "established this session" in the user's re-entry primer. The paper write-up ("Omega Constant results paper") was made in that chat. | 2026-04-08/09 | Claude |
| Inertia chase, RG form (g·e^(g/g0) = g0 → g = g0·Ω) | same chat, Addendum III §VI | 2026-04-09 | Claude |
| Inertia chase, speed-of-light form (the "α line, upper bound c") | **A Gemini session.** It is not in Claude's history. In chat `d1d9dc2c` the user said: "you did the omega...he did the alpha..it was similar in nature to the entropy line...but its upper limit was the speed of light...finding the intersection". Claude asked for the Gemini document ("Do you have the Gemini document, or do we reconstruct from what we know?"). It was never supplied. | before 2026-04-10 | Gemini |
| d* ≈ 0.246 (first appearance) | The Gemini α-line intersection. In `d1d9dc2c`, Claude: "d* is slightly wrong (it came from the Gemini session unverified)". | before 2026-04-10 | Gemini |
| "Riemann and Fermat on opposite sides of the event horizon"; c on layers ℝ,ℂ, entropy on ℍ,𝕆; ln vs log10; d*·ln10 ≈ Ω | claude.ai chat `d1d9dc2c-7987-486d-b564-45e3f168003e` ("Chilly and wet evening") | 2026-04-10 | Claude |
| S(r,θ), I(r,θ) polar field, "rogue waves", d* ring, log-base slider | same chat, widget `entropy_inertia_polar_field` | 2026-04-10 | Claude |
| "Tangency, K = 0 at d*" | same chat, stated in the papers "The Alpha and The Omega of Flat Curvature" and "The Resonant Riemann and the Flowing Fermat". **Never computed in any record.** | 2026-04-10 | Claude (stated only) |
| 1-D forms S(d) = 1 − exp(−α ln(d+1)), I(d) = 1/(1+exp(−(ln(d+1) − τ/2))) with α = 1/137.036, τ = π/2 | chat `1eb2b366-1b42-4aa7-9d1f-dbac31e4278c` ("Chasing entropy and inertia in Berry-Keating"), written into RiemannHypothesisProof v3 §3.6. They are 1-D re-writes of the widget's base terms. | 2026-05-11 | Claude |
| Names Alpha_Fermat (Α_π) and Omega_Riemann (Ω_ζΣ); "ceiling descent" method statement | chat `9c28934d-acbb-405c-9924-c7fbcfc6c13f`; notation in `SMNNIP_TODO.txt` and `The_First_Age_Ainulindale_Conjecture.*` | 2026-04-14 → 2026-05-11 | user + Claude |
| ω_H = e^π "Hagedorn ceiling" | Notation set in the First Age documents / `SMNNIP_TODO.txt`. It does **not** appear in the April 9–10 runs. In the original entropy chase the entropy ceiling was T_Planck. | ~2026-04-13/14 | user + Claude |
| "Fermat prime generator" | **No record under this name or any equivalent** in chats or project docs. See §4. | — | — |

Searches run to build this map: conversation_search for "Alpha_fermat Lambert W fixed point", "chasing inertia speed of causality Hagedorn", "digit ceiling digit floor D_max D_min Planck temperature crossing", "Fermat prime generator", "Omega constant convergence entropy inertia speed of light inverse curve", "Gaussian curvature K=0 tangency entropy inertia polar", "Hagedorn e^pi information ceiling", "Gemini alpha line upper bound c…", "3.05e-16 D_max D_min python T_Planck lambertw", and others. project_search over all 58 project docs, including the Gemini_Deep_* reports.

---

## 1. The two ceilings

### 1.1 Speed of causality
- c = 299 792 458 m/s. Exact by SI definition.
- Role in the experiment: the upper bound on the "α line" (the inertia / propagation side; Gemini's curve). In the April 10 polar widget it is the parameter `cfrac` (fraction of c, default 1.00). It caps the entropy field: S ≤ cfrac. It is drawn as the dashed outer circle at r = 4.
- Layer assignment (`d1d9dc2c`, user instruction, adopted): c bounds layers ℝ, ℂ (L0, L1; propagation). Entropy bounds layers ℍ, 𝕆 (L2, L3; reasoning).

### 1.2 Entropy / information ceiling

There are two values on record. They belong to different stages.

(a) **Original run (April 9): Planck temperature.**
- T_Planck = √(ħ c⁵ / G) / k_B
- RECORD: 1.416784 × 10³² K
- RERUN: 1.4167841617232971231 × 10³² K, with ħ = 1.054571817 × 10⁻³⁴ J·s (exact), c (exact), G = 6.67430 × 10⁻¹¹ m³·kg⁻¹·s⁻² (CODATA 2018), k_B = 1.380649 × 10⁻²³ J/K (exact)

(b) **Later notation (from ~April 13): Hagedorn ceiling ω_H.**
- ω_H = e^π. Dimensionless (framework units, no SI unit attached anywhere in the record).
- RERUN: ω_H = 23.1406926327792690057290863679
- Stated role: "Hagedorn/thermal ceiling. Noether saturation limit. Fixed. Does not slide." It is chosen so that 2/ln(ω_H) = 2/π. RERUN: 2/ln(ω_H) = 0.63661977236758134307553505349.
- ω_H was **not** an input to the April 9 entropy chase or the April 10 polar field. If the rerun is meant to use ω_H as the entropy ceiling, that is a new run, not a reproduction.

---

## 2. The two chases

### 2.1 Entropy chase → Ω (Claude, April 9)

**Forward curve: "digit ceiling" (RECORD, verbatim definitions)**

    S_forward(T) / k_B = 2π · E · r / (ħ · c)        [Bekenstein bound]
    E = k_B · T
    D_max(T) = floor( log10( S_forward(T) / k_B ) )

- T: temperature, K
- E: energy, J
- r: radius of the bounding region, m. **No value is given in the record.**
- ħ: J·s; c: m/s; k_B: J/K
- S_forward/k_B: dimensionless (nats); D_max: count of decimal digits
- Recorded description: "strictly increasing in T with a hard ceiling at T_Planck", "grows sublogarithmically in T and saturates at T_Planck"

**Inverse curve: "digit floor" (RECORD, verbatim)**

    D_min(T) = ceil( log10( T / T_Planck ) )

- Dimensionless count of decimal digits "needed to specify T relative to the Planck temperature"

**Crossing equation (RECORD, verbatim chain)**

    D_max = D_min
    ⇒ log10(S/k_B) = log10(T/T_Planck)
    ⇒ S(T*)/k_B = T*/T_Planck
    "Substituting the Bekenstein entropy at T*":  T*/T_Planck = e^(−T*/T_Planck)
    x ≡ T*/T_Planck  ⇒  x = e^(−x)  ⇒  x = Ω = W(1)
    T* = Ω · T_Planck

**Numbers at each step**

| Quantity | RECORD | RERUN (2026-11-12) |
|---|---|---|
| Ω = W(1) | 0.5671432904097838729999686622… | 0.56714329040978387299996866221035555 |
| Ω − e^(−Ω) | — | 1.1479 × 10⁻⁴¹ (40-digit arithmetic) |
| x_{n+1} = e^(−x_n), x_0 = 0.5, tol 1e−12 | — | 0.5671432904103493 after 45 steps |
| T_Planck | 1.416784 × 10³² K | 1.4167841617232971231 × 10³² K |
| T* = Ω·T_Planck | 8.0349 × 10³¹ K (8.035e31) | 8.0351963128021810104 × 10³¹ K (8.03519539559935 × 10³¹ K using the recorded T_P) |
| "D_max(T*)" | 31.905… | log10(T*/K) = 31.904996491743447446 |
| "D_min(T*)" | 31.905… | ceil(log10(T*/T_P)), evaluated as written, = 0 |
| \|D_max − D_min\| | 3.05 × 10⁻¹⁶ | not reproducible: log10(Ω·T_P) and log10(e^(−Ω)·T_P) differ by 0.0 in IEEE double |
| log10(T*/T_Planck) | — | −0.2463072014734225780494036 |

RERUN findings on this chase. These are arithmetic, checked in §5.6:
1. The recorded 31.905 is log10 of T* in kelvin. It is not either digit function as defined. With the floor/ceil as written, D_min(T*) = 0.
2. With the Bekenstein form as given, S/k_B = 2π k_B T r/(ħ c) is linear in T. Setting it equal to T/T_Planck gives r = ħc/(2π k_B T_Planck) = l_P/(2π) = 2.57234976355338 × 10⁻³⁶ m, **for every T**. That fixes the radius. It does not produce an exponential. The step "T*/T_P = e^(−T*/T_P)" does not follow from the Bekenstein substitution. It is an added assumption (see §6).
3. **The crossing's base-10 coordinate is d*.** log10(T*/T_P) = log10(Ω) = −ln(1/Ω)/ln 10 = −Ω/ln 10, because ln(1/Ω) = Ω. So the decimal-digit position of the crossing below the Planck ceiling is

        |log10(T*/T_Planck)| = Ω / ln 10 = 0.2463072014734225780494036

   That is the d* ≈ 0.246 value, coming out of the entropy chase itself.
4. The "gap": (Ω/ln10 − 0.24600)·ln 10 = 0.000707357533248635. This is exactly the recorded gap 0.00070 (Gemini cites 0.00070685; the April 10 value is 0.00070). It equals the rounding of 0.2463072… to 0.246. Gemini_Deep_Thoughts.txt (project doc) reached the same identity: "0.246 … arises from the base-10 logarithm of the reciprocal of Ω."
5. The project rule "D* must never be defined as Ω/ln(10) — tautology" (memory; `SMNNIP_TODO.txt` patch note) is about hard-coding D_STAR = Ω/ln 10 in code. Finding 3 is different: it says the ceiling-descent run, done as recorded, produces |log10 x*| = Ω/ln 10. Keep D_STAR_SPEC = 0.24600 as the code constant. Record the RERUN value separately. Do not substitute one for the other.

### 2.2 Inertia chase → Ω (two distinct versions on record)

**Version A: RG fixed point (Claude, April 9, Addendum III §VI, RECORD verbatim)**

    g(l*) · e^( g(l*)/g0 ) = g0
    ⇒ g(l*) = g0 · W(1) = g0 · Ω

- g(l): neural coupling at layer depth l (dimensionless). g0: bare coupling at the input layer. l*: the "flat event horizon" layer, where five conditions are claimed to coincide: R_NN = 0, D_l J = 0, β(g) = 0, β = β0, dR_NN/dl ≠ 0.
- Forward curve: g(l) running down with l. Inverse curve: g0·e^(−g/g0). **Neither functional form g(l) nor a β-function producing this fixed-point equation is on record.** The equation is stated, not derived from a flow.
- RERUN: g0 = 1 → g* = 0.56714329040978384, residual 0. g0 = Α_π = 0.00729735256928 → g* = 0.0041386445474239052, residual −8.674 × 10⁻¹⁹.
- Algebra check: put u = g/g0. Then u·e^u = 1, so u = W(1) = Ω. That is correct.

**Version B: "chasing inertia backwards from the speed of causality" (Gemini, α line)**

- Described as: rises from the fine-structure floor Α_π = 1/137, bounded above by c, "similar in nature to the entropy line". Its intersection with Claude's Ω line was read off as d* ≈ 0.246.
- **The forward curve, inverse curve, crossing equation and step numbers are not in any Claude chat or project doc.** Claude (2026-04-10): "What we still need: the explicit functional forms of both curves so the intersection can be derived analytically rather than read off numerically." The user's Gemini history is the only place it can exist. Retrieve it from gemini.google.com activity around 2026-04-09/10 before rerunning, or treat Version B as unreconstructed.
- The closest Claude-side stand-in is the widget's inertia field I(r,θ) with the c-bound `cfrac` (§3). That is Claude's April 10 reconstruction. It is not Gemini's curve.

---

## 3. S(r), I(r): definitions, coordinates, tangency, K

### 3.1 Polar coordinates (widget `entropy_inertia_polar_field`, April 10)
- Canvas 680 × 420 px, centre (cx, cy) = (340, 210), maxR = min(cx, cy) − 20 = 190 px
- r = √((px−cx)² + (py−cy)²) / maxR · 4 → r ∈ [0, 4], dimensionless. The c-bound circle is at r = 4 (pixel radius maxR).
- θ = atan2(py−cy, px−cx) ∈ (−π, π]
- Stated reading: "theta is modular, r is linear, holds both orthogonally. Entropy is radial direction, inertia is angular direction, observer sits at origin."

### 3.2 Definitions (verbatim from the widget, transcribed to math)

    L(r) = log_b(r + 1)            b = e by default (slider "Log base", 1 → e, up to 10)

    S(r,θ) = clamp_[0, cfrac]( cfrac·(1 − e^(−α·L)) + 0.08·sin(6.28·L + θ)·e^(−0.3 r) )
    I(r,θ) = clamp_[0, 1]   ( 1/(1 + e^(−(L − 0.5·depth))) + 0.12·cos(6.28·L − θ + π/2)·e^(−0.2 r) )
    S = I = 0 for r < 0.001

- α: "Entropy coupling α". Slider 0.01–2, **default 0.137** (not 1/137)
- depth: "Inertia depth l". Slider 0.1–6.28, default 1.57 (≈ π/2 = τ)
- cfrac: "c-bound fraction". Slider 0.1–1, default 1.00
- All quantities are dimensionless. The constants 0.08, 6.28, 0.3, 0.12, 0.2, 0.35 are hand-chosen widget constants, not derived.
- Interference = (S + I)/2 + 0.35·S·I. Rogue amplitude = exp(−20 (S−I)²)·(S+I)/2. A "rogue event" is a pixel with amplitude > 0.3.

### 3.3 How d* was computed in the widget
- d* = the r of the pixel minimising |S − I| over 0.1 < r < 3, all θ. Shown as metric "d* intersection", with d*·ln10 beside it.
- The text label "d* ≈ 0.246" on the canvas is a hard-coded string. It is drawn regardless of the computed value.
- RERUN (1:1 Python port, 4001 θ × 6501 r grid near the minimum):

| Parameters | min \|S − I\| | at r | at θ |
|---|---|---|---|
| defaults (α 0.137, depth 1.57, cfrac 1, ln) | 0.1471267038 | 0.256300 | −0.029400 |
| defaults, log10 | 0.1645164178 | 0.626800 | −0.057100 |
| α = 1/137.035999084, depth = π/2, ln | 0.1750563787 | 0.234600 | −0.053300 |

- S and I **never meet** in this field (min |S−I| ≈ 0.147). The "d* ring" is the radius of closest approach, not an intersection or a tangency. Switching to log10 moves it to 0.6268, not to Ω = 0.5671.
- The base terms alone (no oscillation): S0(r) = 1 − e^(−α ln(r+1)), I0(r) = 1/(1+e^(−(ln(r+1) − depth/2))). They have **no crossing on (0, 50]**. min |S0 − I0| = 0.3132 for both parameter sets.

### 3.4 1-D forms in RH proof v3 §3.6 (May 11)
Recorded claim: "At α = 1/137 and τ = π/2, S(d*) = I(d*) = d* ≈ 0.24600."
RERUN: S(0.246) = 0.0016036809, I(0.246) = 0.3622851241. Neither equals 0.246, and they are not equal to each other. The claim does not hold for the formulas as written.

### 3.5 Tangency and K = 0
- On record: "Gaussian curvature K = 0 exactly at d*. The metric is flat at d* and saddle on either side." **No computation of K exists in any chat or doc.**
- RERUN: graph surface z = F(x,y), F = S − I, defaults. K = (F_xx F_yy − F_xy²)/(1 + F_x² + F_y²)², central differences with h = 1e−4, 64 angles per ring:

| r | mean K | min K | max K |
|---|---|---|---|
| 0.1 | −4.0316 | −44.751 | +25.037 |
| 0.2 | +0.21235 | −9.6558 | +13.717 |
| 0.246 | +0.81841 | −6.1628 | +13.738 |
| 0.3 | +0.59717 | −4.0391 | +10.310 |
| 0.5 | −0.47116 | −2.5827 | +0.95928 |
| 1.0 | +0.0045166 | −0.15921 | +0.17944 |

K changes sign around each ring and is not zero along r = 0.246. Choosing a different surface (z = S, z = I, or the metric built from them) is an open choice. The record does not say which surface was meant.

---

## 4. "Fermat prime generator" and A_fermat

- **No construction called a "Fermat prime generator" exists in the searchable record.** That covers all claude.ai chats in this project and all 58 project docs. No step on record produces A_fermat as an output.
- What A_fermat **is** on record: Α_π (Alpha_Fermat) = 1/137.035999084 (CODATA 2018). It is set by notation ("Fine structure constant. BK operator domain LOWER wall. E8/Wyler n-ball geometry. Fermat domain floor. Fixed."), first fixed in `SMNNIP_TODO.txt` / First Age docs (~April 14). The name "Alpha_Fermat" was given by the user on 2026-05-11. RERUN: Α_π = 0.007297352569283800997285105.
- Closest "generator" material on record. These are the only candidates; none is called a Fermat prime generator:
  1. n-ball volume formula V_n = π^(n/2)/Γ(n/2+1), called "the generator of α via Wyler" (`d1d9dc2c`, April 10). RERUN: V_1 = 2.0, V_2 = 3.14159265358979, V_3 = 4.18879020478639, V_4 = 4.93480220054468, V_5 = 5.26378901391432, V_6 = 5.16771278004997, V_7 = 4.7247659703314, V_8 = 4.05871212641677. Recorded V_8/V_peak = 0.769, "not α directly".
     Wyler's formula: α = (9/(8π⁴))·(π⁵/(2⁴·5!))^(1/4). RERUN: 0.007297348130031832129, so 1/α = 137.036082448164.
  2. "Fermat rigidity series / golden prime spiral" (Ainulindale_Conjecture_Revised): the n-th prime at angle θ_n = n·2π/φ² (mod 2π) with weight φ^(−n). Σ_{n≥0} φ^(−n) = φ² = 2.618033988749894848204587. Step 2π/φ² = 2.399963229728653322231556 rad.
  3. April 10 widget `fermatDensity(N, depth)`: counts near-miss triples |x^n + y^n − z^n| < tol, with tol shrinking with depth and α. Recorded result: "Fermat lattice density at depth π, α = 1/137: drops to ~10⁻⁴ of Riemann field."
- If "Fermat prime generator" names something from a Gemini session or a repo file (Ainulindale / ValaQuenta / RiemannHypothesisProof), check there. Ask the user for the file before inventing one.

---

## 5. Code, verbatim

### 5.1 Original entropy-chase code
Not recoverable. The April 9 chat carries only the results ("Match precision: 3.05e-16") inside the user's re-entry primer. The computing session is not in the searchable history.

### 5.2 April 10 polar field widget: script, verbatim (HTML/CSS chrome omitted, logic complete)

```javascript
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
const W = 680, H = 420;
let mode = 'interference';

function setMode(m) {
  mode = m;
  document.querySelectorAll('.tab').forEach(t => t.classList.toggle('active', t.textContent.toLowerCase().replace(' ','') === m));
  draw();
}

function logN(x, b) {
  if (x <= 0) return -Infinity;
  if (b === 1) return Math.log(x);
  return Math.log(x) / Math.log(b);
}

function getParams() {
  const alpha = parseFloat(document.getElementById('alpha').value);
  const depth = parseFloat(document.getElementById('depth').value);
  const cfrac = parseFloat(document.getElementById('cfrac').value);
  const rawb = parseFloat(document.getElementById('logb').value);
  const logbase = rawb < 1.05 ? Math.E : rawb;
  document.getElementById('alphaV').textContent = alpha.toFixed(3);
  document.getElementById('depthV').textContent = depth.toFixed(2);
  document.getElementById('cfracV').textContent = cfrac.toFixed(2);
  document.getElementById('logbV').textContent = rawb < 1.05 ? 'e' : rawb.toFixed(1);
  return { alpha, depth, cfrac, logbase };
}

// S(r,θ) — entropy: rises from 0, bounded above by cfrac (c-analog)
// Like Riemann zeta along the critical line — logarithmic + oscillatory
function entropy(r, theta, alpha, logbase, cfrac) {
  if (r < 0.001) return 0;
  const logr = logN(r + 1, logbase);
  const base = cfrac * (1 - Math.exp(-alpha * logr));
  const oscillation = 0.08 * Math.sin(6.28 * logr + theta) * Math.exp(-0.3 * r);
  return Math.max(0, Math.min(cfrac, base + oscillation));
}

// I(r,θ) — inertia: orthogonal conjugate, conjugate phase π/2
// Like Fermat lattice — discrete-ish, structured
function inertia(r, theta, depth, logbase) {
  if (r < 0.001) return 0;
  const logr = logN(r + 1, logbase);
  const base = 1 / (1 + Math.exp(-(logr - depth * 0.5)));
  const lattice = 0.12 * Math.cos(6.28 * logr - theta + Math.PI / 2) * Math.exp(-0.2 * r);
  return Math.max(0, Math.min(1, base + lattice));
}

function hsl(h, s, l, a = 1) {
  return `hsla(${h},${s}%,${l}%,${a})`;
}

function draw() {
  const { alpha, depth, cfrac, logbase } = getParams();
  const isDark = matchMedia('(prefers-color-scheme: dark)').matches;
  ctx.clearRect(0, 0, W, H);

  const cx = W / 2, cy = H / 2;
  const maxR = Math.min(cx, cy) - 20;

  // Draw pixel-by-pixel in polar coords
  const imgData = ctx.createImageData(W, H);
  const data = imgData.data;

  let maxInterference = 0, dstarX = -1, dstarY = -1, dstarDiff = 999, rogueCount = 0;

  for (let px = 0; px < W; px++) {
    for (let py = 0; py < H; py++) {
      const dx = px - cx, dy = py - cy;
      const r = Math.sqrt(dx * dx + dy * dy) / maxR * 4;
      const theta = Math.atan2(dy, dx);

      const S = entropy(r, theta, alpha, logbase, cfrac);
      const I = inertia(r, theta, depth, logbase);
      const interference = (S + I) / 2 + 0.35 * S * I;
      const diff = Math.abs(S - I);

      // track d*
      if (r > 0.1 && r < 3 && diff < dstarDiff) {
        dstarDiff = diff;
        dstarX = px; dstarY = py;
      }

      let rr = 0, gg = 0, bb = 0, aa = 0;

      if (mode === 'entropy') {
        const t = S;
        rr = Math.round(232 * t); gg = Math.round(89 * t); bb = Math.round(60 * t);
        aa = Math.round(200 * t + 20);
      } else if (mode === 'inertia') {
        const t = I;
        rr = Math.round(59 * t); gg = Math.round(139 * t); bb = Math.round(212 * t);
        aa = Math.round(200 * t + 20);
      } else if (mode === 'interference') {
        const t = interference;
        // blend entropy (warm) and inertia (cool) by their relative strength
        const wS = S / (S + I + 0.001);
        const wI = 1 - wS;
        rr = Math.round(232 * wS * t + 59 * wI * t);
        gg = Math.round(89 * wS * t + 139 * wI * t);
        bb = Math.round(60 * wS * t + 212 * wI * t);
        aa = Math.round(220 * t + 15);
      } else if (mode === 'rogue') {
        // constructive interference: show only when S ≈ I and both high
        const rogue = Math.exp(-20 * diff * diff) * (S + I) / 2;
        if (rogue > 0.3) rogueCount++;
        if (rogue > maxInterference) maxInterference = rogue;
        rr = Math.round(159 * rogue); gg = Math.round(127 * rogue); bb = Math.round(221 * rogue);
        aa = Math.round(255 * rogue);
      }

      const idx = (py * W + px) * 4;
      data[idx] = rr; data[idx+1] = gg; data[idx+2] = bb; data[idx+3] = aa;
    }
  }

  ctx.putImageData(imgData, 0, 0);

  // Draw polar grid
  ctx.save();
  ctx.strokeStyle = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.08)';
  ctx.lineWidth = 0.5;
  for (let ring = 1; ring <= 4; ring++) {
    ctx.beginPath();
    ctx.arc(cx, cy, ring * maxR / 4, 0, Math.PI * 2);
    ctx.stroke();
  }
  for (let a = 0; a < 8; a++) {
    const angle = a * Math.PI / 4;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(cx + maxR * Math.cos(angle), cy + maxR * Math.sin(angle));
    ctx.stroke();
  }
  ctx.restore();

  // c-bound circle
  ctx.save();
  ctx.beginPath();
  ctx.arc(cx, cy, maxR, 0, Math.PI * 2);
  ctx.strokeStyle = isDark ? 'rgba(232,89,60,0.6)' : 'rgba(200,60,30,0.5)';
  ctx.lineWidth = 1.5;
  ctx.setLineDash([4, 3]);
  ctx.stroke();
  ctx.setLineDash([]);
  ctx.restore();

  // d* marker
  if (dstarX > 0) {
    const rdstar = Math.sqrt((dstarX-cx)*(dstarX-cx) + (dstarY-cy)*(dstarY-cy));
    // draw d* ring
    ctx.save();
    ctx.beginPath();
    ctx.arc(cx, cy, rdstar, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(242, 166, 35, 0.8)';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([6, 4]);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.restore();

    const dstarR = rdstar / maxR * 4;
    document.getElementById('dstar').textContent = dstarR.toFixed(3);
    document.getElementById('omega').textContent = (dstarR * Math.log(10)).toFixed(4);
  }

  if (mode === 'rogue') {
    document.getElementById('rogueAmp').textContent = (maxInterference * 100).toFixed(1) + '%';
    document.getElementById('rogueCount').textContent = rogueCount.toLocaleString();
  } else {
    document.getElementById('rogueAmp').textContent = '—';
    document.getElementById('rogueCount').textContent = '—';
  }

  // Labels
  ctx.save();
  ctx.font = '11px sans-serif';
  ctx.fillStyle = isDark ? 'rgba(255,255,255,0.5)' : 'rgba(0,0,0,0.45)';
  ctx.textAlign = 'center';
  ctx.fillText('c bound', cx, cy - maxR - 6);
  ctx.fillText('r=1', cx + maxR/4 + 2, cy - 4);
  ctx.fillText('r=2', cx + maxR/2 + 2, cy - 4);
  ctx.fillText('r=3', cx + 3*maxR/4 + 2, cy - 4);
  ctx.fillStyle = 'rgba(242,166,35,0.9)';
  ctx.fillText('d* ≈ 0.246', cx + 4, cy - Math.sqrt((dstarX-cx)*(dstarX-cx) + (dstarY-cy)*(dstarY-cy)) - 6);
  ctx.restore();
}

draw();
```

Slider markup (verbatim): `alpha` min 0.01 max 2 step 0.01 value 0.137; `depth` min 0.1 max 6.28 step 0.01 value 1.57; `cfrac` min 0.1 max 1 step 0.01 value 1; `logb` min 1 max 10 step 0.1 value 1.

### 5.3 April 10 d*·ln10 check (verbatim computational lines; signature-hash lines elided)

```python
import hashlib, datetime, math
# [signature-hash prompt/response strings elided]
# verify the omega calculation
omega = 0.5671432904
d_star = 0.246
ln10 = math.log(10)
product = d_star * ln10
print(f'd* x ln(10) = {d_star} x {ln10:.6f} = {product:.6f}')
print(f'Omega constant = {omega}')
print(f'Difference = {abs(product - omega):.6f}')
```
Recorded output: d*·ln10 = 0.56644, Ω = 0.56714, difference = 0.00070.

### 5.4 April 10 n-ball check (verbatim computational lines; hash lines elided)

```python
import hashlib, datetime, math
# Compute n-ball volumes for reference
print('n-ball volumes V_n = pi^(n/2) / Gamma(n/2 + 1):')
for n in [1,2,3,4,5,6,7,8]:
    vol = math.pi**(n/2) / math.gamma(n/2 + 1)
    print(f'  n={n}: {vol:.6f}')

peak_n = 5.2569
peak_vol = math.pi**(peak_n/2) / math.gamma(peak_n/2 + 1)
v8 = math.pi**(8/2) / math.gamma(8/2 + 1)
print(f'Peak n={peak_n:.4f}: {peak_vol:.6f}')
print(f'V_8/V_peak ratio: {v8/peak_vol:.6f}')
print(f'1/137 = {1/137:.6f}')
print(f'Wyler alpha approx: {v8/peak_vol:.8f}')
```

### 5.5 Lambert W verifier and constants as committed (`smnnip` inversion engine, April 13; verbatim excerpt)

```python
    ALPHA = 1.0 / 137.035999084

    # Omega: Lambert W fixed point — largest self-referential loop that closes
    # Omega * e^Omega = 1  =>  Omega ~ 0.56714...
    OMEGA = 0.56714329040978384            # computed below and verified

    # d_star: flat curvature locus
    # d* = Omega / ln(10) ~ 0.246
    # Relationship: d* * ln(10) ~ Omega (gap = 0.00070 — the open derivation)
    D_STAR = OMEGA / math.log(10.0)

    # The 0.00070 gap — this is what the engine is trying to close
    OMEGA_GAP = OMEGA - (D_STAR * math.log(10.0))

# Verify Lambert W fixed point numerically (no trust without verification)
def _verify_lambert_w(omega, tolerance=1e-12):
    """
    Omega is the fixed point of f(x) = x * e^x - 1 = 0.
    Equivalently: omega * e^omega = 1.
    We verify by iteration: x_{n+1} = e^{-x_n}
    """
    x = 0.5
    for _ in range(1000):
        x_new = math.exp(-x)
        if abs(x_new - x) < tolerance:
            break
        x = x_new
    residual = abs(x - omega)
    return x, residual
```
(This D_STAR = OMEGA/ln10 line is the tautology that was patched on April 14 to D_STAR_SPEC = 0.24600.)

### 5.6 Rerun script used for this primer (2026-11-12): `rerun_ceilings.py`, verbatim

```python
"""
rerun_ceilings.py — reproduce every recoverable number from the April 2026
ceiling-descent experiment (entropy chase -> Omega, polar S/I field -> d*).
Pure re-derivation; nothing read from prior output.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 40

print("=" * 72)
print("1. CEILINGS")
print("=" * 72)
c = mp.mpf(299792458)                 # m/s, exact (SI definition)
hbar = mp.mpf("1.054571817e-34")      # J s, exact (SI 2019)
G = mp.mpf("6.67430e-11")             # m^3 kg^-1 s^-2, CODATA 2018
kB = mp.mpf("1.380649e-23")           # J/K, exact (SI 2019)
T_P = mp.sqrt(hbar * c**5 / G) / kB   # Planck temperature, K
omega_H = mp.e ** mp.pi               # Hagedorn ceiling (dimensionless, framework notation)
print(f"c        = {mp.nstr(c, 12)} m/s (exact)")
print(f"T_Planck = {mp.nstr(T_P, 20)} K  (from hbar, c, G, k_B)")
print(f"omega_H  = e^pi = {mp.nstr(omega_H, 30)}")
print(f"2/ln(omega_H) = {mp.nstr(2/mp.log(omega_H), 30)}  (= 2/pi)")

print()
print("=" * 72)
print("2. ENTROPY CHASE  —  x = e^{-x}")
print("=" * 72)
Omega = mp.lambertw(1).real
print(f"Omega = W(1) = {mp.nstr(Omega, 35)}")
print(f"residual Omega - e^-Omega = {mp.nstr(Omega - mp.e**(-Omega), 5)}")
# fixed-point iteration as recorded in smnnip code (_verify_lambert_w)
x = 0.5
for n in range(1000):
    xn = math.exp(-x)
    if abs(xn - x) < 1e-12:
        break
    x = xn
print(f"iteration x_(n+1)=e^-x_n from 0.5: {x!r} after {n} steps")
T_star = Omega * T_P
print(f"T* = Omega * T_Planck = {mp.nstr(T_star, 20)} K")
print(f"log10(T* / K)          = {mp.nstr(mp.log10(T_star), 20)}")
print(f"log10(T*/T_Planck)     = {mp.nstr(mp.log10(Omega), 25)}")
print(f"-log10(Omega)          = {mp.nstr(-mp.log10(Omega), 25)}")
print(f"Omega/ln(10)           = {mp.nstr(Omega/mp.log(10), 25)}  (identical: ln(1/Omega)=Omega)")
# recorded digit functions, evaluated literally
Dmin_literal = math.ceil(float(mp.log10(T_star / T_P)))
print(f"D_min(T*) = ceil(log10(T*/T_P)) evaluated literally = {Dmin_literal}")
print("note: recorded value 31.905 equals log10(T* in kelvin), not the ceil() as written")
# machine-epsilon claim: both sides are log10 of the same float
a = math.log10(float(Omega)); b = math.log10(math.exp(-float(Omega)))
print(f"|log10(x) - log10(e^-x)| at float Omega = {abs(a-b):.3e}")

print()
print("=" * 72)
print("3. THE GAP")
print("=" * 72)
ln10 = mp.log(10)
for label, d in [("d*_spec 0.24600", mp.mpf("0.246")),
                 ("d*_RG   0.24682", mp.mpf("0.24682")),
                 ("Omega/ln10     ", Omega/ln10)]:
    print(f"{label}: d*·ln10 = {mp.nstr(d*ln10, 20)}   gap to Omega = {mp.nstr(Omega - d*ln10, 12)}")
print(f"(Omega/ln10 - 0.246)*ln10 = {mp.nstr((Omega/ln10 - mp.mpf('0.246'))*ln10, 15)}")

print()
print("=" * 72)
print("4. INERTIA CHASE — RG fixed point g e^{g/g0} = g0  ->  g = g0*Omega")
print("=" * 72)
for g0 in [1.0, 1/137.035999084]:
    g = g0 * float(Omega)
    print(f"g0={g0:.12g}: g*={g:.17g}  residual g e^(g/g0) - g0 = {g*math.exp(g/g0)-g0:.3e}")

print()
print("=" * 72)
print("5. POLAR FIELD S(r,theta), I(r,theta) — April 10 widget, ported 1:1")
print("=" * 72)
def logN(x, b):
    return math.log(x) if b == math.e else math.log(x) / math.log(b)
def entropy(r, th, alpha, base, cfrac):
    if r < 0.001: return 0.0
    lr = logN(r + 1, base)
    v = cfrac * (1 - math.exp(-alpha * lr)) + 0.08 * math.sin(6.28 * lr + th) * math.exp(-0.3 * r)
    return max(0.0, min(cfrac, v))
def inertia(r, th, depth, base):
    if r < 0.001: return 0.0
    lr = logN(r + 1, base)
    v = 1 / (1 + math.exp(-(lr - depth * 0.5))) + 0.12 * math.cos(6.28 * lr - th + math.pi/2) * math.exp(-0.2 * r)
    return max(0.0, min(1.0, v))

def dstar_scan(alpha, depth, cfrac, base, n_r=6000, n_th=720):
    best = (9, None, None)
    for th in np.linspace(-math.pi, math.pi, n_th, endpoint=False):
        for r in np.linspace(0.1, 3.0, n_r)[1:-1]:
            d = abs(entropy(r, th, alpha, base, cfrac) - inertia(r, th, depth, base))
            if d < best[0]:
                best = (d, r, th)
    return best

for (alpha, depth, cfrac, base, tag) in [
        (0.137, 1.57, 1.0, math.e, "widget defaults, ln"),
        (0.137, 1.57, 1.0, 10.0,   "widget defaults, log10"),
        (1/137.035999084, math.pi/2, 1.0, math.e, "alpha=1/137.036, tau=pi/2, ln")]:
    d, r, th = dstar_scan(alpha, depth, cfrac, base, n_r=1500, n_th=360)
    print(f"{tag:34s}: min|S-I| = {d:.3e} at r = {r:.6f}, theta = {th:+.4f}")

print()
print("radial-only curves (theta-independent base terms, no oscillation):")
def S0(r, alpha, base=math.e): return 1 - math.exp(-alpha * logN(r + 1, base))
def I0(r, depth, base=math.e): return 1 / (1 + math.exp(-(logN(r + 1, base) - depth * 0.5)))
for alpha, depth in [(0.137, 1.57), (1/137.035999084, math.pi/2)]:
    rs = np.linspace(1e-6, 50, 200001)
    diff = [S0(r, alpha) - I0(r, depth) for r in rs]
    sign_changes = [rs[i] for i in range(1, len(rs)) if diff[i-1]*diff[i] < 0]
    print(f"alpha={alpha:.6g}, depth={depth:.6g}: S0(0.246)={S0(0.246,alpha):.6f}  I0(0.246)={I0(0.246,depth):.6f}  "
          f"crossings in (0,50]: {sign_changes[:3]}  min|S0-I0|={min(abs(v) for v in diff):.4f}")

print()
print("recorded 'verbatim' forms (RH proof v3 §3.6):")
a, tau = 1/137.036, math.pi/2
d = 0.246
Sd = 1 - math.exp(-a*math.log(d+1)); Id = 1/(1+math.exp(-(math.log(d+1)-tau/2)))
print(f"S(0.246) = {Sd:.10f}   I(0.246) = {Id:.10f}   d = 0.246")

print()
print("=" * 72)
print("6. GAUSSIAN CURVATURE CHECK  (never computed in the record)")
print("=" * 72)
# graph surface z = F(x,y) with F = S - I on the polar field, K = (F_xx F_yy - F_xy^2)/(1+F_x^2+F_y^2)^2
def F(xx, yy, alpha=0.137, depth=1.57):
    r = math.hypot(xx, yy); th = math.atan2(yy, xx)
    return entropy(r, th, alpha, math.e, 1.0) - inertia(r, th, depth, math.e)
def K_at(xx, yy, h=1e-4, **kw):
    f = lambda a, b: F(a, b, **kw)
    fx = (f(xx+h,yy)-f(xx-h,yy))/(2*h); fy = (f(xx,yy+h)-f(xx,yy-h))/(2*h)
    fxx = (f(xx+h,yy)-2*f(xx,yy)+f(xx-h,yy))/h**2
    fyy = (f(xx,yy+h)-2*f(xx,yy)+f(xx,yy-h))/h**2
    fxy = (f(xx+h,yy+h)-f(xx+h,yy-h)-f(xx-h,yy+h)+f(xx-h,yy-h))/(4*h*h)
    return (fxx*fyy - fxy**2)/(1+fx**2+fy**2)**2
for r in [0.1, 0.2, 0.246, 0.3, 0.5, 1.0]:
    Ks = [K_at(r*math.cos(t), r*math.sin(t)) for t in np.linspace(0, 2*math.pi, 64, endpoint=False)]
    print(f"r={r:<6}: K(S-I) mean={np.mean(Ks):+.4e}  min={min(Ks):+.4e}  max={max(Ks):+.4e}")

print()
print("=" * 72)
print("7. A_fermat (floor) — values on record")
print("=" * 72)
A_pi = 1/mp.mpf("137.035999084")
print(f"A_pi = 1/137.035999084 = {mp.nstr(A_pi, 25)}  (CODATA 2018)")
wyler = (9/(8*mp.pi**4)) * (mp.pi**5/(2**4*mp.factorial(5)))**(mp.mpf(1)/4)
print(f"Wyler: (9/8pi^4)(pi^5/(2^4 5!))^(1/4) = {mp.nstr(wyler, 20)}  -> 1/alpha = {mp.nstr(1/wyler, 15)}")
for n in range(1, 9):
    print(f"  V_{n} = pi^(n/2)/Gamma(n/2+1) = {mp.nstr(mp.pi**(mp.mpf(n)/2)/mp.gamma(mp.mpf(n)/2+1), 15)}")
phi = (1+mp.sqrt(5))/2
print(f"phi = {mp.nstr(phi, 25)};  sum phi^-n (n>=0) = {mp.nstr(1/(1-1/phi), 25)} = phi^2 = {mp.nstr(phi**2,25)}")
print(f"golden prime spiral step 2pi/phi^2 = {mp.nstr(2*mp.pi/phi**2, 25)} rad")
```

Additional checks run alongside (inline):

```python
# Bekenstein substitution check
import mpmath as mp; mp.mp.dps=30
c=mp.mpf(299792458);hbar=mp.mpf('1.054571817e-34');G=mp.mpf('6.67430e-11');kB=mp.mpf('1.380649e-23')
TP=mp.sqrt(hbar*c**5/G)/kB; lP=mp.sqrt(hbar*G/c**3)
print('l_P', mp.nstr(lP,15)); print('hbar c/(kB TP)', mp.nstr(hbar*c/(kB*TP),15)); print('R=l_P/2pi', mp.nstr(lP/(2*mp.pi),15))
print('TP rec 1.416784e32 -> T*', mp.nstr(mp.lambertw(1).real*mp.mpf('1.416784e32'),15))
# -> l_P 1.61625502392855e-35 ; R = 2.57234976355338e-36 m ; T* 8.03519539559935e+31

# 3.05e-16 reproduction attempt
import math
O=0.5671432904097838729999686622; TP=1.416784e32
a=math.log10(O*TP); b=math.log10(math.exp(-O)*TP)
print(abs(a-b))   # -> 0.0
```

The fine d* scan (§3.3 table) used the same `entropy`/`inertia` functions with θ ∈ [−0.2, 0.2] (4001 points) × r ∈ [0.15, 0.8] (6501 points).

---

## 6. Derived vs assumed

| Step | Status |
|---|---|
| c = 299 792 458 m/s; T_Planck = √(ħc⁵/G)/k_B | Definitions (SI/CODATA) |
| Choosing T_Planck as the entropy ceiling, and c as the inertia ceiling | Assumed (design choice: "the largest ceilings… against the speed of causality and the Planck temperature") |
| ω_H = e^π as the Hagedorn ceiling | Assumed (notation, chosen so 2/ln ω_H = 2/π); not used in the original runs |
| D_max = floor(log10(S/k_B)), D_min = ceil(log10(T/T_P)) | Assumed definitions |
| "D_max saturates at T_Planck" | Assumed; does not follow from the Bekenstein form given (linear in T, r unspecified) |
| D_max = D_min ⇒ S/k_B = T/T_P | Derived only if the floor/ceil are dropped (the equality of logs is used, not of the integer functions) |
| S/k_B = T/T_P ⇒ T/T_P = e^(−T/T_P) | **Assumed.** Bekenstein substitution gives r = l_P/(2π) for all T, not an exponential |
| x = e^(−x) has the unique real solution Ω = W(1) | Derived (established mathematics) |
| T* = Ω·T_P = 8.0351963128… × 10³¹ K | Derived from the assumed equation |
| \|log10(T*/T_P)\| = Ω/ln10 = 0.24630720147… | Derived (identity ln(1/Ω) = Ω) |
| Gap 0.000707357533248635 = (Ω/ln10 − 0.246)·ln10 | Derived (rounding of 0.24631 to 0.246) |
| "3.05 × 10⁻¹⁶ match" | Recorded, not reproducible; any exact algebraic identity evaluates to ~0 in floating point |
| g·e^(g/g0) = g0 | Assumed (stated, no β-function on record) |
| g* = g0·Ω | Derived from the assumed equation |
| Gemini α-line (inertia from c) and its intersection at 0.246 | Unrecovered; not verifiable from Claude's record |
| S(r,θ), I(r,θ) forms and all their numeric constants | Assumed (hand-built visual model) |
| "d* ring" at r ≈ 0.256 in the widget | Derived (computed nearest approach); S ≠ I anywhere (min gap 0.147) |
| "Tangency", "K = 0 at d*", "shared tangent = critical line" | Asserted, never computed; RERUN K ≠ 0 at r = 0.246 |
| S(d*) = I(d*) = d* ≈ 0.246 for the 1-D forms | False as written (0.0016 vs 0.3623) |
| Α_π = 1/137.035999084 as A_fermat | Assumed (assigned by notation; CODATA value) |
| "Fermat prime generator" → A_fermat | Not on record |
| d*_spec = 0.24600 "independently confirmed in Berry-Keating literature" | From Gemini deep research (Gemini_Deep_Report.txt). The cited sources (Młynarski; GSJP stability abscissa) were not checked in any Claude session |

---

## 7. Rerun instructions for Claude Code

1. Run §5.6 `rerun_ceilings.py` (needs `mpmath`, `numpy`). Confirm every RERUN number above to the digits shown.
2. Get the Gemini α-line session from the user. Without it, Version B of the inertia chase (§2.2) cannot be reproduced. Do not reconstruct it silently.
3. Make one explicit decision before the new run: entropy ceiling = T_Planck (original) or ω_H = e^π (later notation). Run both and report them separately if unsure.
4. For any "tangency / K = 0" claim: state which surface's K is computed (graph of S, of I, of S − I, or a metric built from them). Compute it numerically and report the sign pattern around the ring.
5. Report d* three ways and never merge them: (a) |log10(Ω)| = Ω/ln10 = 0.2463072014734225780494036 from the entropy chase; (b) d*_spec = 0.24600 (code constant, Gemini/BK citation); (c) whatever the rebuilt c-bounded inertia curve gives.
6. Ask the user what "Fermat prime generator" refers to (file path or session) before building anything with that name.
