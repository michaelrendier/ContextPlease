# 121 — The Fast Inverse Square Root of the Two Trees

| | |
|---|---|
| Scope | two claims, each tested before being written down: (1) Laurelin's "fast inverse square root" is Wiener's continued-fraction attack, which works exactly when the representation carries the answer; (2) the Smith-chart map Γ(s) = (s − 1)/(s + 1) is already a valid source-free 2D vacuum field (a harmonic conjugate pair) |
| Measured | 2026-09-21; continues [47](47_the_two_trees.md) and [93](93_qm_gr_by_tree.md) |
| Code | `GenerationalLineage/engine/ping.py` (`op_wiener`), `engine/toolsets/scale.py` (`Gamma`, `local_scale_factor`); `.claude/scratchpad/2026-09-21_smith_apollonian_uft_probe/`; the paper `FourthAgePapers/FastInverse/README.md` |
| Confidence | both claims: ESTABLISHED as mathematics (re-run independently, §§2–3) · the Telperion/Laurelin assignment: an open naming question (§1) · "free lunch" as an interpretation of the shared shape: `INTERPRETATION` |
| Last verified | 2026-11-13: Listings 1 and 2 executed (an independent Wiener implementation; a symbolic check); their output is quoted below. `op_wiener` itself was not re-run |

## 1. The naming used here, stated up front

[93](93_qm_gr_by_tree.md) flagged an unresolved tangle: Telperion and Laurelin are assigned to the lower/upper octonion inconsistently across the repositories ([135](135_engine_findings_ledger.md), X-20). This page adds a **third** pairing and does not resolve the other two:

```
Laurelin  = INSIDE  = bounded, quantised, the ascent/Emerger jurisdiction (work, search, cost > 0: GenerationalLineage's DECOMPOSITION/EMERGER split, engine/lines.py)
Telperion = OUTSIDE = unbounded, continuous, the descent/DECOMPOSITION jurisdiction (free, deductive, cost = 0)
```

This matches the session's working image: the Apollonian gasket is a packed structure of bubbles with only insides, never anything "between" them; SCALE (L_k: x ↦ kx) is the topological complement, only ever outside. L_(I|O), the established intertwiner, is the map between the two languages. (The author's remark of 2026-11-10, "Fermat N-shape = Laurelin, Riemann N-holes = Telperion", is a fourth statement; which labelling is canonical is still to be settled, [96](96_the_riemann_fermat_horizon.md) §2.)

## 2. Claim 1: the fast inverse square root of Laurelin (inside)  `ESTABLISHED`

**The real routine** exploits the fact that IEEE 754's bit layout already encodes an approximate log₂(x), turning a hard nonlinear operation into one integer shift-and-subtract plus one Newton step: fast wherever the representation carries that gift ([107](107_add_scale_sign_datatype.md) §8 measures its error: 3.44 % raw, 0.175 % after one step).

**Laurelin's instance, already built:** `GenerationalLineage/engine/ping.py`, `op_wiener()`. Given N and the public exponent e, the continued-fraction convergents of e/N recover the private exponent d directly, in O(log N), with no search, **exactly when d is small enough to be a convergent**. Outside that regime it returns `fired: False` and reports the work spent (the engine's regime table: "floor — GNFS/Shor only" for a properly generated modulus). The representation (the continued fraction of e/N) carries the answer only in the narrow regime where the object's own arithmetic encodes it, "the identical shape as the float bit-hack".

**Listing 1 — an independent Wiener attack, and where it stops** (written for this page; needs sympy; runs cold)

```python
import math, random
from sympy import randprime, mod_inverse
def convergents(a, b):
    h0, h1, k0, k1 = 0, 1, 1, 0
    while b:
        q = a // b; a, b = b, a - q * b; h0, h1 = h1, q * h1 + h0; k0, k1 = k1, q * k1 + k0; yield h1, k1
def wiener(e, N):
    for k, d in convergents(e, N):
        if k == 0 or (e * d - 1) % k: continue
        phi = (e * d - 1) // k; s = N - phi + 1; disc = s * s - 4 * N
        if disc >= 0 and math.isqrt(disc) ** 2 == disc: return d
    return None
random.seed(7); bits = 256
p = randprime(2**(bits // 2 - 1), 2**(bits // 2)); q = randprime(p + 1, 2 * p); N = p * q; phi = (p - 1) * (q - 1); bound = round(N ** .25 / 3)
print('N has %d bits; Wiener bound N^(1/4)/3 = 2^%.1f' % (N.bit_length(), math.log2(bound)))
for name, dbits in (('small d (< bound/4)', int(math.log2(bound)) - 2), ('d just below bound', int(math.log2(bound)) - 1), ('d = 64 bits above bound', int(math.log2(bound)) + 64), ('random full-size d', bits)):
    while True:
        d = random.getrandbits(dbits) | 1 | (1 << (dbits - 1))
        if math.gcd(d, phi) == 1: break
    e = mod_inverse(d, phi); print('  %-26s d has %3d bits -> Wiener recovers d: %s' % (name, d.bit_length(), wiener(e, N) == d))
```

```
N has 256 bits; Wiener bound N^(1/4)/3 = 2^62.4
  small d (< bound/4)        d has  60 bits -> Wiener recovers d: True
  d just below bound         d has  61 bits -> Wiener recovers d: True
  d = 64 bits above bound    d has 126 bits -> Wiener recovers d: False
  random full-size d         d has 256 bits -> Wiener recovers d: False
```

Wiener's theorem (1990): if d < N^(1/4)/3 (with q < p < 2q) then d is a convergent of e/N. The measurements agree: the 60- and 61-bit exponents fall below 2^62.4 and are recovered; at 126 bits and at full size the attack returns nothing. This is the cleanest executable instance of "fast only where the representation carries the answer".

## 3. Claim 2: the fast inverse square root of Telperion (outside), Smith chart, Maxwell  `ESTABLISHED`

The claim tested: that Γ(s) = (s − 1)/(s + 1) is not merely "a continuous ruler" by analogy, but that its real and imaginary parts are exactly the object a source-free 2D magnetostatic potential is: a harmonic conjugate pair. Checked symbolically, z = x + iy:

**Listing 2 — Cauchy–Riemann, Laplace, divergence and curl, the derivative and the Schwarzian** (written for this page; needs sympy; runs cold)

```python
import sympy as sp
x, y = sp.symbols('x y', real=True); z = x + sp.I * y; G = (z - 1) / (z + 1)
u = sp.simplify(sp.re(sp.expand_complex(G))); v = sp.simplify(sp.im(sp.expand_complex(G)))
print('u =', sp.factor(u)); print('v =', sp.factor(v))
print('Cauchy-Riemann u_x - v_y =', sp.simplify(sp.diff(u, x) - sp.diff(v, y)), '; u_y + v_x =', sp.simplify(sp.diff(u, y) + sp.diff(v, x)))
print('Laplacians:', sp.simplify(sp.diff(u, x, 2) + sp.diff(u, y, 2)), sp.simplify(sp.diff(v, x, 2) + sp.diff(v, y, 2)))
V = (sp.diff(u, x), sp.diff(u, y)); print('div grad u =', sp.simplify(sp.diff(V[0], x) + sp.diff(V[1], y)), '; curl grad u =', sp.simplify(sp.diff(V[1], x) - sp.diff(V[0], y)))
s = sp.symbols('s'); Gs = (s - 1) / (s + 1); d1 = sp.diff(Gs, s)
print('dGamma/ds =', sp.simplify(d1), '; Schwarzian =', sp.simplify(sp.diff(Gs, s, 3) / d1 - sp.Rational(3, 2) * (sp.diff(Gs, s, 2) / d1) ** 2))
```

```
u = (x**2 + y**2 - 1)/(x**2 + 2*x + y**2 + 1)
v = 2*y/(x**2 + 2*x + y**2 + 1)
Cauchy-Riemann u_x - v_y = 0 ; u_y + v_x = 0
Laplacians: 0 0
div grad u = 0 ; curl grad u = 0
dGamma/ds = 2/(s + 1)**2 ; Schwarzian = 0
```

All six identities are exact (symbolic, away from the single pole at s = −1), dΓ/dz = 2/(z + 1)², matching `scale.py`'s `local_scale_factor` = |dΓ/ds| = 2/(s + 1)², and the Schwarzian derivative of the Möbius map is 0, as it must be.

**What this establishes, stated precisely.** For any holomorphic function the real and imaginary parts form a harmonic conjugate pair (textbook complex analysis), and that pair is the same mathematics used for a 2D magnetic scalar potential, a 2D electrostatic potential in vacuum and a 2D irrotational incompressible flow potential. Γ being holomorphic (a Möbius map, Schwarzian 0) makes this automatic, not special to Γ. **What is specific to Γ** is that Telperion's own map, the one carrying `scale.py`'s GR-jurisdiction label, is **already** a valid vacuum field of this type, with no adjustment: "Telperion's free lunch", the representation's holomorphy
already carrying the Maxwell-shaped structure, the way Laurelin's e/N already carries d in the small-d regime. Two jurisdictions, two representations, the same free-head-start shape in each: an analogy of shape, supported by the two listings.

## 4. Where this sits

Neither claim is new machinery: both are existing, shipped objects (`op_wiener`, `scale.py`'s Γ) read under the same lens. Nothing here re-opens [93](93_qm_gr_by_tree.md)'s verdict (QM and GR are tower rungs, not tree halves): this page's Telperion/Laurelin split is the inside/outside (bounded/unbounded) pairing, a different axis, explicitly not the same as 93's octonion-content pairing. The Weyl-gauge continuation is [122](122_the_prime_gauge_field.md).

## 5. Related pages

[47](47_the_two_trees.md) · [93](93_qm_gr_by_tree.md) · [122](122_the_prime_gauge_field.md) · [95](95_the_scale.md) · [107](107_add_scale_sign_datatype.md) · `.claude/scratchpad/2026-09-21_smith_apollonian_uft_probe/` (the earlier pass where the Schwarzian-zero fact, that Γ carries no gauge curvature, was first checked)
