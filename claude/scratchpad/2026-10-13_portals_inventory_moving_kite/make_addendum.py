"""Appends the 2026-10-13 addendum + raw outputs to VAPMIP/docs/wiki/Boxkite-Deformation-Record-2026-10-12.md (idempotent: replaces a previous addendum)."""
import os
R = '/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-10-13_portals_inventory_moving_kite/'
DOC = '/home/rendier/Projects/ThePlace/VAPMIP/docs/wiki/Boxkite-Deformation-Record-2026-10-12.md'
s = open(DOC, encoding='utf-8').read()
marker = "\n\n---\n\n# Addendum 2026-10-13"
if marker in s: s = s[:s.index(marker)]
add = marker + r''' — genealogy, portals, G₂ decomposition, moving-kite invariants, Lambert-W, the paper update

**What this addendum adds** (second pass of the session; everything is in `.claude/scratchpad/2026-10-13_portals_inventory_moving_kite/`, outputs in Appendix C):

1. **The factorisation** of the box-kite into relations, from nothing to a strut — written up as its own page, `Boxkite-Relational-Atlas.md`. Headline [MEASURED]: an Assessor is an *ordered pair of distinct
   points of the Fano plane* `P` (`7 × 6 = 42`), the strut label `s = a⊕b` is the third point of their line, chart `s` is the plane with the point `s` removed (its three antipodal pairs are the three lines through `s`),
   edges are pairs on different lines through `s`, and the whole structure comes from one choice (the antiflag `(e₈, P)`) and one cocycle (the Cayley–Dickson signs).
2. **Sub-algebra census (corrects genealogy.py's first pass):** 35 quaternion lines; of the 15 order-8 subgroups, **8 are octonions and 7 are not** (not alternative, composition fails).
3. **The sign gauge:** every face of every kite carries sign-holonomy −1 (all 8 frustrated); the best diagonal assignment satisfies 8 of 12 edges.
4. **Portals:** all 84 diagonals lie on one continuous `G₂`-orbit (83 of 83 reached, residual ≤ 1e-12); the struts are not separate. Inside a zero divisor: a 3-sphere of partners with the four lattice neighbours as an orthonormal frame.
5. **`G₂` decomposition:** `ℝ¹⁶ = ℝe₀ ⊕ ℝe₈ ⊕ 7 ⊕ 7`; fixed subspace `span(e₀, e₈)` = the `{2:14}` pointer.
6. **Definition-level checks:** the octonions are a Clifford module under left multiplication and the sedenions are not (the failure is the non-alternativity); both hexagon identities hold for `(φ, β)` — the table is an algebra in a braided monoidal category; the 35 lines of `PG(3,2)` ↔ the 35 points of the Klein quadric.
7. **Moving-kite readings:** invariants (norm, `e₀`/`e₈` weights, lower/upper split, singular spectra of `L_v`, `R_v`, associator norm) versus frame-relative readings (chart energies, `local_curvature`, every Walsh coefficient including ptol's `Γ`, the `σ_RB` tilt).
8. **The three Lambert-W values** reproduced to 40 digits with three methods; `W(−1/e)` is a double root.
9. **The scalar/scaled split is now explicit.** The pencil / string / flashlight / `Φ(w)` / tension-law machinery (§§2–3, §9–10 of this record) belongs to the **seven ordered pairs — a discrete, static object, the scalar context box kite**. It was wrongly extended to the scaled Mind's-Eye kite in Phase 40 §7; that is corrected there. The scaled kite has to move as de Marrais's kite moves (§§5.3 and 6 above and the atlas §6–§8).
11. **Lambert W as a fixed-point multiplier and its UNS values** (`2026-10-13_lambert_dynamics_uns/`, output in Appendix C): four tests → three values (W₀ and W₋₁ meet at the double root); `W(1)` in UNS is `d*_taut`, `W(−1/e)` in UNS is `−log₁₀ e`; `−W(λ)` is the fixed-point multiplier of `e^{−λx}` (flip at `λ = e`, no further cascade), `−W(−λ)` that of `e^{λx}` (fold at `λ = 1/e`); the double root is a Whitney fold and the cardioid cusp is the same multiplier `+1`. Atlas §10.
10. **The paper** (`ScalarContextPropagation` v4.0 and its README, branch `scalar-context-propagation`) gained §9.7 (the seven ordered pairs laid out: 3 axes + pivot + 3 shadows, the station as `e_a·exp(η e_r φ)`, the one-signed-phase law, Listing 9.7 + transcript, bracketing and firing order) and §9.8 (how they differ from de Marrais's chart) and new appendix scripts 12–13; edited in a git worktree, **uncommitted**.

### Corrections log, continued

| # | Said earlier | Corrected to | Where found |
|---|---|---|---|
| 10 | Phase 40 §7: string machinery applied to the *scaled* Mind's-Eye kite | The pencil / string is the discrete scalar object; the scaled kite is a different object (the moving `G₂` kite). Scope note added to Phase 40. | Cody, 2026-10-13 |
| 11 | genealogy.py: "order 8: 50 subgroups", 0 octonions | The census included 35 order-4 spans; correct: 15 order-8, **8 octonions + 7 non-alternative** | genealogy2.py |
| 12 | genealogy.py: "faces whose three vertices can all mutually annihilate: 0" read as a finding | It is the sign frustration (all 8 faces have holonomy −1), measured directly in genealogy2.py | genealogy2.py |
| 13 | lambert3.py first run: Newton at `W(−1/e)` printed no ratios | scipy returns `nan` at the branch point, which broke my root; with the exact root −1 the error ratio tends to ½ (double root) | lambert3.py |

# Appendix C — verbatim captured output, 2026-10-13 scripts
'''
for name in ('../2026-10-13_lambert_dynamics_uns/output_lambert_uns.txt', 'output_lambert3.txt', 'output_genealogy.txt', 'output_genealogy2.txt', 'output_g2decomp.txt', 'output_portals.txt', 'output_invariants.txt', 'output_spinor_braid.txt'):
    p = R + name
    add += "\n### " + name + (" (first pass — superseded by genealogy2)" if name == 'output_genealogy.txt' else "") + "\n\n```\n" + (open(p, encoding='utf-8').read().rstrip('\n') if os.path.exists(p) else '(not found)') + "\n```\n"
open(DOC, 'w', encoding='utf-8').write(s + add)
print(len(s), '->', len(s + add))
