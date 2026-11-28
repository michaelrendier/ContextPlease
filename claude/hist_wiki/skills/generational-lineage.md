# generational-lineage

**Skill:** `~/.claude/skills/generational-lineage/` · mirror `ContextPlease/claude/skills/generational-lineage/`
**Created:** 2026-08-18 (VAPMIP session) · **Version 0.2.0:** 2026-11-27 · **Owner of the method:** Cody Michael Allison (Michael Rendier)

## What it is

Track the descent of every operation in a calculation, decompose it against the Two Trees domain, and watch for emergent geometries: is a named operator primitive or derived, is a result a discovery or a restatement. The floor of the decomposition is three irreducibles, ADD, SCALE and SIGN.

## What changed on 2026-11-27 (0.2.0)

Cody: "since add:scale:sign is the base of GenerationalLineage, update your generational-lineage skill". Section 1b was added: the floor is a datatype, `ASS` in `ValaQuenta/modules/add_scale_sign/` (version 0.3), and the skill now records what the clean-house pass measured about it:

* the group Aff(1, ℝ) = ℝ ⋊ (ℝ>0 × ℤ/2), composition (right factor fires first), the inverse, exactness in `Fraction` arithmetic (5832 triples);
* `[SCALE, ADD] = ADD` as a statement about the group: the commutators `x⁻¹y⁻¹xy` are the translations `a·(1/s − 1)` and `−2a`; SIGN and SCALE commute;
* the word `u = g·ln s + a` is a readout of one element and **not** a homomorphism; the firing defect is `(g − 1)·ln s`;
* the Smith charts (SCALE east–west, ADD north–south; the code had them swapped until 0.3, ledger X-71);
* the Long Path (`trajectory`, `collisions`, the Recamán flip test, chrono against zeta order);
* the exact 18-element window is not a subgroup; the finite subgroups of Aff(1, ℝ) have order 1 or 2.

A standing check was added: write a self-check from the documentation, not from the code (it is how X-71 was found).

## Where it lives

Record page `ValaQuenta/wiki/add_scale_sign.md`; findings ledger `Ainulindale/wiki/135_engine_findings_ledger.md` (X-70, X-71); gallery `ValaQuenta/gallery/add_scale_sign/`; downstream copy `GenerationalLineage/engine/add_scale_sign.py`; paper §9 of the ValaQuenta engineering white paper.
