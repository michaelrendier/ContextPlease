# 60 — The Heart as a J₂ Circuit

| | |
|---|---|
| Scope | the claim that the heart is a J₂ involution; what the circulation does and does not share with the framework's structure |
| Origin | 2026-06-13 cascade capture |
| Code | `ValaQuenta/notebooks/core/14_heart_j2_involution.ipynb` ("Engine 18", `e18_heart_j2_involution.py`); copy in `FourthAgePapers/ScalarContextPropagation/repo_appendix/j2_involution/` |
| Confidence | the anatomy and the volume balance: ESTABLISHED · the J₂ and algebra assignments: `INTERPRETATION` · "the circuit is an involution": corrected below |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The notebook's own cells were not re-run |

## 1. What holds

| Statement | Status | Note |
|---|---|---|
| Four chambers, two sides | ESTABLISHED | 4 = 2² as a count: left/right × atrium/ventricle |
| Right side carries deoxygenated blood to the lungs, left side oxygenated blood to the body | ESTABLISHED | |
| Systemic flow equals pulmonary flow in steady state, so the volume balance J_R + J_B = 0 in the sign convention where the two flows are opposite in sense | ESTABLISHED as conservation of blood volume | an ordinary conservation law; not an instance of Noether's theorem |
| The sinoatrial node paces the heart without an external clock | ESTABLISHED | |
| Left = Red, right = Blue (the colour split) | `INTERPRETATION` | the clinical colour code (red oxygenated, blue deoxygenated) is the origin of the match |

## 2. What does not hold as written

**The circuit is not an involution.** The earlier text states: "Apply twice: Right →
Lungs → Left → Body → Right. J₂² = identity", but the sequence written is one pass,
the full cycle. A cycle through six stations RA → RV → Lungs → LA → LV → Body → RA
is a 6-cycle, and a 6-cycle has order 6, not 2. Listing 1 computes this. An
involution would need a map that is its own inverse (a swap, e.g. exchanging the two
sides), which a one-way circulation is not.

**The sinoatrial node is a limit cycle, not a fixed point.** The pacemaker produces a
sustained oscillation, which is a stable periodic orbit; a stable fixed point would be
a heart that stops. The sentence "the SA node is the fixed point of its own
dynamics, so it is σ = ½" conflates the two. Listing 1 shows a standard
relaxation oscillator (Van der Pol, μ = 1, used as the textbook model of a
self-sustained cardiac-type oscillation) approaching the same cycle from three
starts and not approaching a point. The rate is also not 1 Hz exactly: at 72 beats per
minute it is 1.2 Hz, with cardiac output 5.04 L/min at a 70 mL stroke volume.

**The algebra assignment is not consistent.** The table assigned ℂ to the right
chambers and ℍ to the left, which are dimensions 2 and 4; the heart's chambers
come in matched pairs on each side, so a side-by-side assignment of different
algebras has no anatomical basis. The count 4 = 2² can be stated without it.

**Listing 1 — the three checks** (written for this page; needs numpy; runs cold)

```python
import numpy as np
step = {i: (i + 1) % 6 for i in range(6)}              # RA RV Lungs LA LV Body -> next
ident = {i: i for i in range(6)}
compose = lambda f, g: {i: f[g[i]] for i in f}
p, order = dict(step), 1
while p != ident: p = compose(step, p); order += 1
print('one pass of the circuit is a 6-cycle; order =', order, '(an involution needs order 2)')
def vdp(s, mu=1.0): x, y = s; return np.array([y, mu * (1 - x * x) * y - x])
def rk4(s, dt):
    k1 = vdp(s); k2 = vdp(s + dt / 2 * k1); k3 = vdp(s + dt / 2 * k2); k4 = vdp(s + dt * k3)
    return s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
for s0 in ([0.01, 0.0], [4.0, 4.0], [-3.0, 1.0]):
    s = np.array(s0); amp = []
    for i in range(200000):
        s = rk4(s, 0.001)
        if i > 100000: amp.append(s[0])
    print('start', s0, '-> settles to a cycle with max x = %.4f (not to a point)' % max(amp))
print('cardiac output at 70 mL x 72 bpm = %.2f L/min ; beat frequency = %.2f Hz' % (0.070 * 72, 72 / 60))
```

```
one pass of the circuit is a 6-cycle; order = 6 (an involution needs order 2)
start [0.01, 0.0] -> settles to a cycle with max x = 2.0086 (not to a point)
start [4.0, 4.0] -> settles to a cycle with max x = 2.0086 (not to a point)
start [-3.0, 1.0] -> settles to a cycle with max x = 2.0086 (not to a point)
cardiac output at 70 mL x 72 bpm = 5.04 L/min ; beat frequency = 1.20 Hz
```

## 3. The two-stroke picture  `INTERPRETATION`

Diastole (filling) and systole (ejection) are a two-stroke cycle, and the
framework's (I|O) two-stroke engine ([03](03_inversion_engine.md)) is a
structure with the same form: a compression stroke and an expansion stroke about a
turning point. The match is in the shape of the cycle (two phases, a return), and
it is useful as a mnemonic. It does not make the heart an inversion r → 1/r, and no
listing here computes one.

The framework's J₂ is the half-swap of the 16-component sedenion halves, which is
an involution but not an automorphism ([52c](52c_j2_involution_riemann_fermat.md);
`0/256` pairs preserved). The heart's circuit is a different object: a one-way
cycle. The correspondence the page can keep is that both are paired-sides structures
(red/blue, left/right).

## 4. The "third biological system" claim

The earlier text lists DNA (antiparallel strands), protein folding and the heart as
"J₂ engines". Antiparallel DNA strands are complementary under base pairing and
reverse orientation, a real duality; the protein-folding and heart entries are
analogies of the same kind. None of the three has been tested against the J₂
definition in [52c](52c_j2_involution_riemann_fermat.md). The statement that the
universe "builds the same engine at every scale" is the author's reading.

## 5. What the notebook computes

Read from the notebook's cells (2026-11-13; the cells were read, not re-run):

| Cell | What it does | What its result means |
|---|---|---|
| discrete state machine | steps (oxygenation, side, phase) through RA → Lungs → LA → Body → RA | a cyclic sequence returning to its start: the 4-stage cycle of §2, not an involution |
| SA node | iterates σ ← σ + 0.3 (J_B − J_R)/(J_R + J_B), with J_R = σ^½ and J_B = (1 − σ)^½ | converges to σ = ½ from every start because J_R = J_B is solved at ½ by construction; a property of the update rule |
| stroke volume | SV = 70 exp(−(σ − ½)²/0.02) mL, zero below d* | an assumed Gaussian; the earlier text's "matches medical data at σ = ½" is not a comparison the notebook makes |
| perturbation | a shift of σ below GAP "self-corrects" and above GAP is "arrhythmia" | re-run with the notebook's own rule (20 steps, damping 0.3): every shift tested (1×10⁻⁴, 1×10⁻³, GAP, 2·GAP, 5·GAP, 0.1, 0.2) ends within 2×10⁻⁴ of ½, so the "arrhythmia" branch never fires and GAP plays no role; the claimed threshold at GAP is not produced by the model |

The notebook therefore shows that the model it defines converges and is
peaked where it was built to be. It makes no measurement on a heart. The
physically relevant behaviour is Listing 1: convergence to a limit cycle, with no
σ in it. The notebook's final cell ("J₂ at every scale of biology") is a list of
five analogies (DNA, protein, heart, brain hemispheres, cell division) with no
computation.

## 6. Related pages

[03 Inversion engine](03_inversion_engine.md) · [43 Emmy Noether sedenion](43_emmy_noether_sedenion.md) ·
[51 the J₂ involution](52c_j2_involution_riemann_fermat.md) · [47 the Two Trees](47_the_two_trees.md)
