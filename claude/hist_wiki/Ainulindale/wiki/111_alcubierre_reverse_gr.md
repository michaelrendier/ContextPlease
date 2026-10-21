# 111 — Alcubierre and reverse GR (the equation tree's ancestor)

[98_provenance_and_citations.md](98_provenance_and_citations.md). Citation-pass
intake, 2026-09-04 session. **Acknowledged influence**, not an independent
parallel — Cody names it directly — but the methodological ancestor of the
equational-decomposition tooling, so it earns a page and a citation-queue slot.

---

- **[Alcubierre1994]** Alcubierre, M. (1994). *The warp drive: hyper-fast
  travel within general relativity.* Class. Quantum Grav. 11(5), L73–L77.
  doi:10.1088/0264-9381/11/5/001. — Write down the spacetime geometry you
  want (a travelling bubble), then run Einstein's equations **backwards** —
  from the metric to the stress–energy tensor it requires — instead of
  forwards from matter to geometry.

## What it anchors

The **equational-decomposition methodology**: take an equation, move each term
to the other side of the `=`, and keep the formula for *that* variable too —
solve backward for every quantity, not just the "output". This is Alcubierre's
reverse move generalised from GR to any equation.

- `PtolemyDesktop/Archimedes/Maths/researcher/_generate.py` — the Formulary
  generator: 503 base equations → 1739, each solved for every variable with a
  closed form.
- `GenerationalLineage/engine/shape.py` — "find evidence for missing
  operators": decompose an equation to the tier-0 floor, read what is missing
  to close it (the reverse of "here is the equation, solve it").
- The planned **equation tree** (like the Operator Tree) — explore the
  jurisdiction of operators by walking backward from a target quantity.

## Cite in

`Archimedes/CANONICAL_MATHS.md` header; `GenerationalLineage/wiki/The-Operator-Tree.md`;
the shape-completion / missing-operator write-up.
