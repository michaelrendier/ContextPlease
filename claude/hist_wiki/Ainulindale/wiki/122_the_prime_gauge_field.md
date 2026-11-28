# 122 — The Prime Gauge Field

| | |
|---|---|
| Scope | Weyl's move (scale as a local freedom) applied to the Smith-chart map: two candidate connections, one provably flat and one not; the closed form of the curvature; its zero locus against the pre-registered prediction |
| Measured | 2026-09-21; continues [121](121_fast_inverse_square_root_of_the_two_trees.md) |
| Engine | `ValaQuenta/modules/prime_gauge_field/` (engine page `ValaQuenta/wiki/prime_gauge_field.md`); the paper `FourthAgePapers/FastInverse/README.md`; `GenerationalLineage/engine/toolsets/scale.py` (Γ, unmodified) |
| Confidence | the closed form F = 2 Im Γ′ and its zero locus: ESTABLISHED (re-run symbolically, Listing 1) · "the right local-gauge object": not argued (§3) |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The engine's 2000-point sample was not re-run |

## 1. The question 121 left open

[121](121_fast_inverse_square_root_of_the_two_trees.md) found that Γ(s) = (s − 1)/(s + 1) carries no classical gauge curvature (the Schwarzian derivative is 0): true, and narrower than it looks, because it tested one fixed, global Möbius map. Weyl's own 1918 move (the origin of the word "gauge", H. Weyl, *Gravitation und Elektrizität*, *Sitzungsber. Preuss. Akad. Wiss.* 1918; a 1923 reprint resolved in the checks) was to make **scale itself** a local, position-dependent freedom and read the curvature of that connection. That version was never run; this page runs it.

## 2. Two connections, one provably flat, one not  `ESTABLISHED`

- A = ∇(log|Γ|): flat everywhere for any holomorphic scalar (it is a gradient: Poincaré lemma). Not a fact about Γ; forced by any object of that shape. It confirms that 121's negative result was never Γ-specific.
- A = (Re Γ(s), Im Γ(s)): Γ itself read as a genuine ℝ² connection, not collapsed to one complex value. Its curvature is F = ∂ₓA_y − ∂_yAₓ. Since ∂ₓΓ = Γ′ and ∂_yΓ = iΓ′, ∂ₓ(Im Γ) = Im Γ′ and ∂_y(Re Γ) = −Im Γ′, so **F(s) = 2·Im(Γ′(s))**, with Γ′ = 2/(s + 1)².

**Listing 1 — the curvature in closed form and its zero locus** (written for this page; needs sympy; runs cold)

```python
import sympy as sp, random
x, y = sp.symbols('x y', real=True); s = sp.symbols('s'); z = x + sp.I * y
Gs = (s - 1) / (s + 1); G = Gs.subs(s, z)
u = sp.simplify(sp.re(sp.expand_complex(G))); v = sp.simplify(sp.im(sp.expand_complex(G)))
F = sp.simplify(sp.diff(v, x) - sp.diff(u, y)); Gp = sp.simplify(sp.diff(Gs, s)).subs(s, z)
print('F - 2 Im(Gamma\') =', sp.simplify(F - 2 * sp.im(sp.expand_complex(Gp))))
print('F =', sp.factor(F))
f = sp.lambdify((x, y), F, 'math'); random.seed(1)
pts = [(random.uniform(-4, 4), random.uniform(-4, 4)) for _ in range(2000)]
print('F on t = 0 (real axis): max |F| = %.1e ; on sigma = -1: max |F| = %.1e ; off both (2000 random points): min |F| = %.3e' % (max(abs(f(a, 0)) for a, _ in pts), max(abs(f(-1, b)) for _, b in pts), min(abs(f(a, b)) for a, b in pts)))
```

```
F - 2 Im(Gamma') = 0
F = -8*y*(x + 1)/(x**2 + 2*x + y**2 + 1)**2
F on t = 0 (real axis): max |F| = 0.0e+00 ; on sigma = -1: max |F| = 0.0e+00 ; off both (2000 random points): min |F| = 6.142e-04
```

The closed form F = −8y(x + 1)/(x² + 2x + y² + 1)² is exact and vanishes **only** where y = 0 (the real axis, t = 0) or x = −1 (σ = −1, the vertical line through Γ's own pole). The page's "finite-difference error ~10⁻¹¹" check is the engine's; the symbolic result here supersedes it. So the curvature is non-zero almost everywhere on the s-plane (the minimum over 2000 random points off both lines is 6.1×10⁻⁴, small only because some points lie near a line).

## 3. The prediction, checked: half right  (kept)

[121](121_fast_inverse_square_root_of_the_two_trees.md)'s stated prediction, before this was computed: the flat locus is the construction's vacuum, where the local gauge freedom does nothing. Measured zero locus of F:

- **the real axis** (t = 0): Γ is real-valued there; the "phase" degree of freedom the connection is built from does nothing: a legitimate reading of "vacuum", and it matches.
- **σ = −1**: the vertical line through Γ's pole. **Not named in the prediction; new.** Reported as new, not retrofitted.

So the prediction is half right: the trivial-phase locus behaves as the vacuum was expected to; the pole line is a second, unpredicted flat locus, and the record keeps them separate.

**What this does and does not settle.** It settles that a genuinely local reading of Telperion's own scale connection *can* carry curvature: the flat Schwarzian result concerned one global construction, not a ceiling on what a local-scale object built from Γ can do. It does not settle whether (Re Γ, Im Γ) as a 1-form is *the* right local-gauge object or one convenient candidate among several: no uniqueness argument was made; it is the most direct reading of "Γ itself as a connection" and nothing more is claimed. (The name "prime gauge field" is the framework's; the object is a standard curvature computation for a specific 1-form built from a Möbius map.)

## 4. Related pages

[121](121_fast_inverse_square_root_of_the_two_trees.md) · [93](93_qm_gr_by_tree.md) (the same GR-is-a-boundary-phenomenon theme, different mechanism; with the base-rate correction recorded there) · [95](95_the_scale.md) · [98](98_provenance_and_citations.md)
