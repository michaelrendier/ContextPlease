---
name: lean
description: Lean 4 + Mathlib, the proof language. Read, write, build and CRITICALLY AUDIT Lean code: what a compile proves and does not (the statement, the axioms), how to check a claimed proof such as the Nov 2026 Alpöge/Claude Riemann Hypothesis release, and how Cody's exact identities (zero-divisor counts, Fano/associator facts, d*, Ω) could become kernel-checked statements next to the measured ones. Load for any .lean file, lake project, proof-assistant question, or when a result says "formalised in Lean".
---

# lean

Built 2026-11-20 after the Alpöge/Claude Riemann Hypothesis claim ("only Lean was released"). **Not run on this machine**: Lean/elan/lake are NOT installed here (checked 2026-11-20). Everything below is from knowledge, marked `verify` where the exact name or version should be confirmed on first use. Installing needs the elan installer (a remote script) and about 5 GB for Mathlib: ask Cody before installing; use a per-project directory, no system Python involved.

## 1. What Lean is, in one paragraph
A programming language and proof assistant. A theorem is a **type**; a proof is a **term** of that type; the small **kernel** checks the term. If it compiles with no `sorry` and no extra axioms, the kernel accepts that *the stated proposition* follows from Lean's logic (dependent type theory) plus three standard axioms (`propext`, `Classical.choice`, `Quot.sound`). The language is Lean 4; the library of mathematics is **Mathlib** (`leanprover-community/mathlib4`); the build tool is **lake**; the toolchain manager is **elan** (`lean-toolchain` file pins the version).
Not to be confused: Lean's coercion arrow `↑` (a "lift" of a ℕ to ℝ) is bookkeeping; theta lifts in the Alpöge description are automorphic forms. Different words, same English.

## 2. The one rule that matters: a compile proves the statement, not the story
**Compiling shows the theorem as typed is proved. It does not show the typed theorem is the one you care about.** Check, in this order:
1. **The final statement.** Read the type of the headline theorem. For RH it should be Mathlib's own `RiemannHypothesis` (`verify` the exact definition: all non-trivial zeros of `riemannZeta` have real part 1/2; the trivial zeros at −2(n+1) and the pole at 1 are excluded), **not a locally redefined `def RH`**. A project that defines its own RH, or restricts a quantifier, can compile and prove something weaker.
2. **Axioms.** In a scratch file: `#print axioms TheTheorem`. Acceptable: `propext`, `Classical.choice`, `Quot.sound`. Alarm: `sorryAx` (an unproved hole), any custom `axiom`, `Lean.ofReduceBool` / `Lean.trustCompiler` (from `native_decide`: trusts the compiler, not the kernel).
3. **Escape hatches.** Grep the whole project: `sorry`, `admit`, `axiom `, `native_decide`, `unsafe`, `implemented_by`, `extern`, `@[csimp]`, `opaque`, `set_option maxRecDepth`, `set_option debug.`, `macro`/`syntax`/`elab` that rewrite goals, `noncomputable` abuse is fine but note it, `local notation` that shadows a standard symbol, `open ... in` shadowing.
4. **Definitions the statement depends on.** Every `def` the headline theorem mentions must be read: a theorem about `MyZeta` is not about `riemannZeta`. Trace the dependency tree of the statement (`#print` the theorem, then each constant).
5. **Rebuild from scratch.** `lake build` in a clean clone with the pinned toolchain and the pinned Mathlib commit; do not trust a prebuilt `.olean`. For independence also run the independent checker `lean4checker` (replays the kernel on the compiled environment; `verify` name) or `Lean4Lean`.
6. **Statement vs English.** Compare the Lean statement with the paper/claim line by line; this is where mistranslation hides (the Numberphile reaction mentioned it happening between the Lean and human texts of the Navier–Stokes proof).
7. **Size and provenance.** 250,000+ generated pages is a build-time and review-time problem, not a validity problem; the kernel does not care. But the *statement and its definitions* are small and human-readable; audit those first.

Report the audit as: statement read / axioms listed / escape hatches grepped / clean rebuild done / independent checker done, each yes or no.

## 3. Reading Lean quickly
- `theorem name (x : ℝ) (h : 0 < x) : 0 < x ^ 2 := by positivity`: hypotheses before the colon, goal after, `by` starts tactics.
- Types: `ℕ ℤ ℚ ℝ ℂ`; `Fin n`; `Finset`; `Set`; `∀ x, P x`; `∃ x, P x`; `→` implication; `↔` iff; `¬`; `∧ ∨`.
- `#eval`, `#check`, `#print`, `#print axioms`, `example : ... := ...` (an unnamed theorem), `variable`, `namespace`, `open`, `import Mathlib` (one import for everything; slow first build).
- Term-style proofs: `⟨a, b⟩` constructs a pair/∃; `fun x => ...`; `rfl` for definitional equality; `h.1`, `h.2` project.

## 4. Writing proofs: tactic toolbox
`intro`, `exact`, `apply`, `refine`, `constructor`, `rcases`/`obtain` (destructure), `cases`, `induction n with ...`, `rw [h]`, `simp`, `simp only [...]`, `ring`, `field_simp`, `linarith`, `nlinarith`, `positivity`, `norm_num`, `omega` (ℕ/ℤ linear arithmetic), `decide` (finite, small), `gcongr`, `calc` chains, `by_contra`, `push_neg`, `use`, `ext`, `funext`, `exact?` / `apply?` / `rw?` / `simp?` (search for the lemma), `sorry` (only as a marked placeholder, never shipped).
Workflow: state the theorem with `sorry`, run the build, replace one hole at a time; read the goal state in the infoview (or `trace_state`); find lemma names with `exact?` or Mathlib's docs (`leanprover-community.github.io/mathlib4_docs`), search by type with Loogle / `#find` (`verify`).

## 5. Project layout
```
MyProject/
  lean-toolchain          # e.g. leanprover/lean4:v4.x.0 (pin it)
  lakefile.toml           # or lakefile.lean; requires mathlib at a pinned rev
  lake-manifest.json      # exact commits
  MyProject.lean          # root import
  MyProject/Basic.lean
```
Commands: `lake new MyProject math` (Mathlib template; `verify`), `lake exe cache get` (download prebuilt Mathlib oleans, avoids an hours-long build), `lake build`, `lake env lean file.lean`. Lean is single-version-per-project: never mix a Mathlib commit with another toolchain.

## 6. Install (ask first; not done)
elan from `https://github.com/leanprover/elan` (the installer script `elan-init.sh`; read it before running; it writes `~/.elan`), then `lake` projects fetch their own toolchain from `lean-toolchain`. Disk: about 5 GB with Mathlib's cache. VS Code extension `lean4` gives the infoview; in a terminal use `lake env lean`. No system Python needed.

## 7. Using it for Cody's work (proposals, none built)
Lean is the *exact* column that sits beside the *measured* column. Good fits, each a finite or algebraic fact that `decide`/`simp`/`ring`/`norm_num` can close:
- Sedenion multiplication table facts: the 84 zero-divisors on 42 index pairs, the 35 quaternion XOR-triples at dim 16, the box-kite octahedra (χ = 14), Fano plane incidence, the associator count 1848 of 4096 triples. A `decide` over `Fin 16` closes them (small search; `verify` runtime).
- The generator relations `[θ, D] = −D`, `P D P = −D`, `[P, θ] = 0`: provable in an algebra of operators on a function space (heavier; start with the abstract relations on a free algebra).
- Number-theory identities already in the engines: Δ = ln 10 · (Ω/ln 10 − d*_spec) is trivial algebra (it says exactly that the mass gap is a difference of two numbers, which Lean would make impossible to hide); Lambert W(1) facts need Mathlib's `Real.exp`/W lemmas.
- Never claim in prose that something is "proved in Lean" unless it passes §2. Use the label `KERNEL-CHECKED` (distinct from `MEASURED` and `ESTABLISHED`): statement as typed, Mathlib commit, `#print axioms` output. A kernel-checked statement of a *definition* (e.g. a locally defined d*) proves nothing about the physical claim.
- Pair it with the executable ledger idea (`rhp/ledger.py`): each ledger line gets, where possible, a `.lean` twin.

## 8. Pitfalls
- A green build with `sorry` prints only a warning. Treat warnings as failures when auditing.
- `decide` on big finite types can time out or hit `maxRecDepth`; raising limits is allowed but note it. `native_decide` is a different trust level.
- Universe and coercion errors (`ℕ` to `ℝ` casts: `(n : ℝ)`, `Nat.cast`) are the usual beginner stalls; `push_cast`, `norm_cast` help.
- Mathlib renames lemmas often; an old proof may not build on a new Mathlib. Pin.
- Autoformalised proofs can be correct and unreadable; reviewing the *statement* is not optional.
- `import Mathlib` takes a long time to load; for quick tests import only the file you need.

## 9. First-use checklist (to run when Lean is installed)
`lean --version`; `lake --version`; make a scratch project; prove `example : 2 + 2 = 4 := by norm_num`; run `#print axioms` on a theorem that uses `Classical.choice`; build a sedenion `Fin 16` XOR table and `decide` a small fact; then update this skill: drop `verify` marks that were confirmed, record the toolchain version and Mathlib commit used.
