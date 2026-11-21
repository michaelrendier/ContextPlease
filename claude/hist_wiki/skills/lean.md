# lean

**Skill:** `~/.claude/skills/lean/` · mirror `ContextPlease/claude/skills/lean/` · **Created:** 2026-11-20 (author: Cody Michael Allison): "you have used the lifting language in those explorations... i need you to give yourself a lean code skill... the computer language for proofs."

Lean 4 + Mathlib: reading, writing, building and **auditing** Lean code. The central rule: a compile proves the *statement as typed*, not that it is the statement you care about; audit the final statement, the axioms (`#print axioms`), the escape hatches (`sorry`, `native_decide`, custom axioms, local redefinitions), and rebuild from scratch. Written after the Alpöge/Claude Riemann Hypothesis release, whose evidence is Lean code only.

Not run here: Lean is not installed (checked 2026-11-20); install needs Cody's go. Proposals for Cody's work (a kernel-checked column beside the measured one) are in §7 of the skill; none built.
