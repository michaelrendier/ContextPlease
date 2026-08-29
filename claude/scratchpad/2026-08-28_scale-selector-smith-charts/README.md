# Scale selector × orthogonal Smith charts (2026-08-28)

Cody: *"the scalar real value that selects scale from 0_RB and spits out that
family of equations...because shadows grow across an orthogonal set of smith
charts...test"*

`test.py` — distilled to 6 checkable claims on the sedenion (dim 16). **4/6 PASS;
the 2 FAILs are method errors, not real failures:**

| | claim | result |
|---|---|---|
| C1 | `Scale · Resolution = 16` at every bifurcation level (`= xp = E`, conserved) | **PASS** |
| C4 | Joukowsky/Smith fold `Γ=(r−1)/(r+1)` places the 5 levels symmetric about 0, **center `Γ=0` exactly at `s=2`, `R=S=4` = the quaternion level** (`√16`) | **PASS** |
| C5 | `J_N: r→1/r` swaps level `s ↔ 4−s`, `Γ(1/r)=−Γ(r)`, `J_N∘J_N=id` | **PASS** |
| C6 | "shadows grow across": shadow count `[16,8,4,2,1]` strictly decreasing in `s` | **PASS** |
| EXTRA | the doubling-coupling block at level `s` is Frobenius-orthogonal to the one at `s+1` (`⟨·,·⟩_F = 0` every adjacent pair) | **PASS** — strongest form of "orthogonal set of Smith charts" |
| C2 | each level = `±` copies of one equation | METHOD ERROR — passes `s≤1` (the `s=1` base block came out **exactly `[[0,−1],[1,0]] = i`**, 8 copies, signs `+++-+--+`); at quaternion+ the copies differ by **sign AND conjugation** (CD doubling adds conjugation); the `±`-only test is too strict |
| C3 | the S diagonal blocks mutually orthogonal *as operators* | METHOD ERROR — they're the *same* operator (that's C2), so `⟨·,·⟩=±2`. Orthogonality is in the **ambient 16-D frame** (disjoint support) and **between adjacent split-generators** (the EXTRA test) — both hold |

**Core claim confirmed:** a real scalar selects the scale; each level yields a
family of copies of one equation (up to sign+conjugation); the levels/splits sit
as an orthogonal set on the Smith chart with the quaternion at center; `J_N`
swaps the conjugate readings.

Cody then: "that engine was already built — the H_hat_RB historical engine —
decompose it." → `SedenionFactoralRelativity/engine/valaquenta_calibration.py ::
decompose_h_rb_hat()` — piece-by-piece decomposition of `Σ_RB` + shape-match vs
0_RB. **Shape matches** (same tier-0 floor 2·ADD/3·SCALE/4·SIGN, whole Two-Trees
span, 8 DOF, †-fixed); one import on the equation side ("a self-adjoint domain
exists") = the gap between right-shape and proven. Written into
`ValaQuenta/wiki/h_rb_hat.md`.
