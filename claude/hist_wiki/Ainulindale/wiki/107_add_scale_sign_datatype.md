# 107 — The ADD:SCALE:SIGN Datatype — Formal Specification

**Status:** ESTABLISHED (the group is elementary; every method is
code-verified — round-trip 1e-12, fold = tanh, firing defect exact).
**Engines:** `ValaQuenta/modules/add_scale_sign/` (value type + EquationModule)
· `SedenionFactoralRelativity/engine/add_scale_sign.py` (engine + tool in the
decomposer suite) · decomposition maths (four-question test, roll-down):
`VAPMIP/add_scale_sign.py` (not duplicated).
**Reference:** `.clauderc_canonical_maths` "ADD:SCALE:SIGN — the tier-0
datatype". **Related:** [[95_the_scale]], [[92_ring_theory_spine]],
`generational-lineage` skill §§0–3.

---

## 1. Object

An `ASS` value is an element of the tier-0 floor

    Aff(1,ℝ)  =  ℝ ⋊ (ℝ_{>0} × ℤ/2)  =  ADD ⋊ (SCALE × SIGN)

represented by a triple `(add a, scale s>0, sign g∈{−1,+1})` acting as the map

    T_{(a,s,g)} : x  ↦  g·s·x + a

`ASS` is immutable. It records the atomic generators that built it
(`.steps`, application order) — forward, backward and record-keeping in one
type.

## 2. Generators and their equation parts

| generator | map | equation part `Δ` | cost |
|---|---|---|---|
| `ADD(a)`   | `x ↦ x + a` | `a` | free (translation; the flow / count) |
| `SCALE(s)` | `x ↦ s·x`   | `ln s` | **the work** (log-gain; the fold) |
| `SIGN(g)`  | `x ↦ g·x`   | `g ∈ {−1,+1}` | free (one bit; `det ±1`) |

Identities: `(0, 1, +1)` — the Mingling (off both Two Trees).

## 3. The word and the fold (the generalized equation)

Every `ASS` element has a **word**

    u(a,s,g)  =  g·ln s  +  a

and a position on the Smith / Joukowsky fold

    Γ  =  tanh(u / 2)

For a composite of generators `T = ⨟_k T_k`,

    u(T)  =  Σ_k [ g_k·ln s_k + a_k ]        Γ(T) = tanh(u(T)/2)

The fold is the **generating function of `Aff(1,ℝ)` acting on `ln x`**; `u` is
the signed ADD:SCALE:SIGN word-length.

**Ground state.** `a→0, s→1, g→+1  ⇒  u=0  ⇒  Γ=0  ⇒  x = the anchor.` This is
the identity / the now / the viewport (SCALE at unit gain). "Readiness = ground
state = only ADD:SCALE:SIGN" is the predicate `T.is_ground()`.

## 4. Operations (the manipulation surface — the `str` analogy)

| category | method | semantics |
|---|---|---|
| apply | `T(x)` | `g·s·x + a` |
| **forward** | `A @ B` / `A.then(B)` | composition; `(A @ B)(x) = A(B(x))` — `B` fires first |
| **backward** | `~T` | inverse `(−g·a/s, 1/s, g)`; **reverses and inverts the record** |
| **residual** (`str.strip`) | `T.residual('SIGN')` | reset one generator to its identity, keep the rest |
| complement | `T.only('SCALE')` | keep one generator, drop the other two |
| split | `T.parts()` | `(SIGN(g), SCALE(s), ADD(a))` — camshaft order |
| **decompose** | `T.lineage(order)` | → `ASSWord` (§6) |
| chart | `T.to_smith()` | §7 |
| record | `T.steps`, `T.record()` | the immutable `(a,s,g)` log — Paper's Hands / the Long Path |

Group laws (`compose`):
`(a₂,s₂,g₂) ∘ (a₁,s₁,g₁) = (a₂ + s₂·g₂·a₁, s₂·s₁, g₂·g₁)`.
Only non-trivial bracket: `[SCALE, ADD] = ADD`.

## 5. Firing order — the three-phase camshaft

    CAMSHAFT = (SIGN, SCALE, ADD)          SIGN innermost:
      x  ↦  ADD( SCALE( SIGN(x) ) )        T = ADD(a) @ SCALE(s) @ SIGN(g)

**Firing defect.** `u(T) − (a + ln s)  =  (g − 1)·ln s`
(verified exact). Zero iff `g = +1` or `s = 1`; otherwise `−2·ln s`. Non-zero
⇔ the SIGN flipped a non-trivial SCALE ⇔ *the same quantity was defined twice*
— structurally the Bell composed-rotation defect (Wiki: the native-space Bell
test). Concurrency model: three threads, one per phase, rotating independently;
**the interference pattern of the three phases is the pathway.**

## 6. `ASSWord` — the datatype's own decomposition type

`T.lineage(order)` returns an ordered word of the recorded generators.

- `order='chrono'` — application order (*when* each generator fired; the record).
- `order='zeta'` — sorted by spectral weight `|u_k|` descending (*how much* each
  generator moves the fold).

The departure between the two orderings is this datatype's `ψ(x) − x` — the
generational-lineage-as-chronology vs generational-lineage-as-ζ-order
distinction, made concrete and measurable.

`ASSWord.firing_defect()`, `.additive()`, `.as_equation()`, iteration.

## 7. The orthogonal Smith charts

`T.to_smith()` reads the element in the maths language it was built on:

    Γ_SCALE  =  tanh(½·ln s)      (multiplicative / E–W ring)
    Γ_ADD    =  tanh(½·a)         (additive / N–S ring)
    parity   =  g                 (which quadrant sheet)

Ground state → `(0, 0, +1)` = the centre / the now. The two rings are
conformally orthogonal; SIGN selects the sheet.

## 8. Worked example — the fast inverse square root

`1/√x = exp(−½·ln x)` is the `ASS` word `SIGN(−1) ∘ SCALE(½)` applied to
`ln x`. The Quake III routine (`0x5f3759df`) computes exactly this in the
IEEE-754 exponent field — the hardware's native `log₂`:

- `i >> 1` — SCALE by ½, done as a **shift** (the SCALE-multiply is *skipped*);
- `MAGIC − …` — the ADD (bias/offset);
- the sign bit is untouched — SIGN.

The float mantissa makes the map piecewise-linear → "good enough" (≈ 3.4 % raw);
one Newton step is the **residual** (≈ 0.17 %). `SedenionFactoralRelativity/engine/add_scale_sign.py`
`fisr_word(x)`. This is why the hack is brilliant: it recognised `1/√x` as an
ADD:SCALE:SIGN word and evaluated it in the representation where two of the
three generators are free.

## 9. Reconstruction claim, stated with its scope

The three generators span `Aff(1,ℝ)` — the 1-D similarity group. Every operation
the `generational-lineage` roll-down reaches (`root_irreducible`, `ROOT_OF`,
`AFF1`; tiers 0–3) terminates on a word in `{ADD, SCALE, SIGN}`. Within that
domain the `(ADD, SCALE, SIGN)` axes are a **3-D field** and every operation is
a point / word in it. This is the concrete content of "this reduces
everything"; it is not a claim about mathematics outside the decomposition
domain.

## 10. `J_green` (conjecture, Cody 2026-08-28)

`J_red` and `J_blue` are the two octonion halves ([[wiki 14]] / D-CS §8, §11);
their coupling *is* the sedenion = `0_RB`. Read in the `(ADD, SCALE, SIGN)`
basis that coupling is a single 3-vector field — **`J_green`** (green = red +
blue, additively). Proposed identity:

    J_red  ⊕  J_blue   =   (ADD:x , SCALE:y , SIGN:z)   =   J_green   =   0_RB

THEORETICAL. The `⊕` is the coupling (a per-channel product, not a scalar sum —
`.clauderc_canonical_maths` "s_rb[k] = J_red[k]·J_blue[k]"), read on the tier-0
floor. Consistent with `decompose_h_rb_hat`'s finding that `Σ_RB` decomposes as
`2·ADD / 3·SCALE / 4·SIGN`.

## 11. The Two Trees containment (Cody 2026-08-28)

LAURELIN (composite, "what IS") is *all around* TELPERION (irreducible, "what
CANNOT BE") — the derived operations are dense, the three irreducibles are
sparse. Yet TELPERION *hugs* LAURELIN — every composite is built from the
irreducibles, so the three are *inside* each. `T.parts()` extracts the three
generators that every element hugs. Mutual embedding; the same self-similar
containment the Mandelbrot interior/exterior relation shows.

## 12. Related conjecture — string theory as the M ⟂ J residual

The Mandelbrot set (parameter space, `z₀ = 0`, `c` varies) and the Julia sets
(dynamical space, `c` fixed, `z₀` varies) are the two orthogonal viewpoints of
`z ↦ z² + c`. Cody's conjecture: **string theory is the residual of that
orthogonal pair** — the same "residual" as the error check ([[wiki 105]] /
`~/.clauderc_user_provenance §1.20`) and the BAO spectral residue. THEORETICAL,
no engine yet; recorded as the natural next probe from §1.20.
