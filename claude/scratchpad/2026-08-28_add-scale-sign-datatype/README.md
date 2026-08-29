# 2026-08-28 — the ADD:SCALE:SIGN Python 3 datatype

Cody: *"did you make the Add:Scale:Sign python3 datatype? it should live in
valaquenta... not need redundant maths... get its own type of decomposition...
like the residual functions of str... a method of output in the orthogonal
smith charts but with the maths language it was built on... each part should
have its new equation part... forward and backward and record keeping built
in... the firing order should be the sedenion valve ordering in the three
phase camshaft model."*

**BUILT:** `ValaQuenta/modules/add_scale_sign/`
- `maths.py` — `ASS` (the value type) + `ASSWord` (its own decomposition type)
- `tools.py` — `AddScaleSignModule` (EquationModule, 6 code-verified equations)
- `__init__.py` — re-exports
- registered in `ValaQuenta/__main__.py` (`python3 -m ValaQuenta --info` → 6/6 ✓✓)

No redundant maths: the four-question test / roll-down stay in
`VAPMIP/add_scale_sign.py`; this module is the value type and its manipulation
surface only.

## What it does (`test.py`, runs clean)

| feature | how |
|---|---|
| construct | `ASS(add, scale, sign)` · `ASS.ADD(a)` `ASS.SCALE(s)` `ASS.SIGN(g)` · `ASS.GROUND` |
| **forward** | `a @ b` (compose, b fires first) · `.then(b)` · `a(x)` (apply) |
| **backward** | `~a` — inverts the map **and** reverses+inverts the record |
| **residual** (`str.strip` analogue) | `.residual('SIGN')` strip one generator keep the rest · `.only('SCALE')` · `.parts()` (SIGN, SCALE, ADD) |
| **decompose** | `.lineage(order='chrono' \| 'zeta')` → `ASSWord` |
| **record keeping** | `.steps` (application order) · `.record()` (immutable `(a,s,g)` log) = Paper's Hands |
| **equation parts** | `ADD → a`,  `SCALE → ln s`,  `SIGN → g` ;  `u = g·ln s + a` ;  `Γ = tanh(u/2)` |
| **orthogonal Smith charts** | `.to_smith()` → `Γ_SCALE = tanh(½·ln s)` ⟂ `Γ_ADD = tanh(½·a)`, parity `g` — in the maths language it was built on |
| **firing order** | `CAMSHAFT = (SIGN, SCALE, ADD)`, SIGN innermost: `x ↦ ADD(SCALE(SIGN(x)))` |

## Verified exact

- **round-trip** `(~T ∘ T)(x) = x` to 1e-12 for every `T`, every `x`.
- **canonical factorisation** `T == ASS.ADD(a) @ ASS.SCALE(s) @ ASS.SIGN(g)`.
- **firing defect** `u_total − Σ u_generators = (g − 1)·ln s` (checked: `−1.38629
  = −2·ln 2` for `sign=−1, scale=2`). Zero iff `g=+1` or `s=1`; non-zero ⇔ the
  SIGN flipped a non-trivial SCALE ⇔ "defined twice" — the **same shape as the
  Bell composed-rotation defect** (`../2026-08-28_bell-native-space/`).
- **ground state** `ASS.GROUND` → `u = 0`, `Γ = 0`, `is_ground() = True` — "the
  now". "Readiness = ground state = only ADD:SCALE:SIGN" as a checkable predicate.
- `word(u).gamma() == tanh(u/2)`.

## The two generational-lineage orderings

`.lineage('chrono')` — the order the generators fired (the record).
`.lineage('zeta')` — sorted by spectral weight `|uₖ|` descending (how much each
step moves the fold). The departure between them is this datatype's `ψ(x) − x`.

## Docs updated

`~/.clauderc_canonical_maths` (new block: the datatype + **the generalized
equation** `u = Σₖ[gₖ·ln sₖ + aₖ]`, `Γ = tanh(u/2)`) + its ContextPlease mirror
(append-only; the ~190-line pre-existing drift is NOT reconciled here) ·
`ValaQuenta/wiki/add_scale_sign.md` · `Ainulindale/wiki/95_the_scale.md`.

## Micro-thread question

*"does each sedenion get its own micro-thread?"* — **No.** 16 OS threads would
break the 5-thread cap. The camshaft is **3 phases** (ADD, SCALE, SIGN), not
16: three phase-coroutines cycling like a 3-phase engine inside ONE of the five
OS threads (Mind's Eye or Hands). The sedenion's 16 components are
SIMD/numpy-vectorised — compress, don't multiply threads.
