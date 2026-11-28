# 111 — Alcubierre and Reverse GR (the Equation Tree's Ancestor)

| | |
|---|---|
| Scope | the acknowledged methodological influence of Alcubierre's "write the geometry first, then solve Einstein's equations backwards" on the equational-decomposition tooling |
| Intake | citation pass, 2026-09-04 session; [98](98_provenance_and_citations.md). **Acknowledged influence**, not an independent parallel: the author names it directly |
| Verification (2026-11-13) | the reference was resolved against Crossref (title, volume, pages, year agree); the Formulary counts were reproduced by running the generator in dry mode (§2) |
| Confidence | the citation: ESTABLISHED · the methodology's lineage from Alcubierre's move: the author's attribution |

## 1. The reference

**[Alcubierre1994]** M. Alcubierre, *The warp drive: hyper-fast travel within general relativity*, *Class. Quantum Grav.* 11(5), L73–L77 (1994), doi:10.1088/0264-9381/11/5/001 (verified). Write down the spacetime geometry you want (a travelling bubble), then run Einstein's equations **backwards**, from the metric to the stress–energy tensor it requires, instead of forwards from matter to geometry. (Standard background: any metric defines some T_μν through G_μν = 8πT_μν; whether that T_μν obeys the usual energy conditions is a separate question, and Alcubierre's bubble requires negative
energy density. The methodological point borrowed here is the direction of the inference, not the physics of the bubble.)

## 2. What it anchors  `ESTABLISHED` (the counts)

The **equational-decomposition methodology**: take an equation, move each term to the other side of the "=", and keep the formula for that variable too; solve backward for every quantity, not only the "output". This is Alcubierre's reverse move generalised from GR to any equation.

- `PtolemyDesktop/Archimedes/Maths/researcher/_generate.py`: the Formulary generator. Run 2026-11-13 in dry mode (`python3 -m Archimedes.Maths.researcher._generate --dry` from `PtolemyDesktop`): **38 modules, 503 base + 1236 rearranged = 1739 formulae**, as recorded. For each equation it keeps every rearrangement with a closed form (F = ma yields F = m·a, m = F/a, a = F/m).
- `GenerationalLineage/engine/shape.py`: "find evidence for missing operators": decompose an equation to the tier-0 floor and read what is missing to close it (the reverse of "here is the equation, solve it"; used in [106](106_the_navier_stokes_problem.md) §5).
- The planned **equation tree** (like the Operator Tree, `GenerationalLineage/wiki/The-Operator-Tree.md`): explore the jurisdiction of operators by walking backward from a target quantity.

## 3. Cite in

`Archimedes/CANONICAL_MATHS.md` header; `GenerationalLineage/wiki/The-Operator-Tree.md`; the shape-completion / missing-operator write-up.

## 4. Related pages

[98](98_provenance_and_citations.md) · [97](97_units_as_the_equation_index.md) (the units as the equation index) · [110](110_qm_in_gr_gr_in_qm.md)
