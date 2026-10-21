# 117 — Rising & Johansson: the spidroin terminal-domain switches

[98_provenance_and_citations.md](98_provenance_and_citations.md). Citation-pass
intake, 2026-09-04 session. Independent parallel — the composition model's two
link types (context-triggered vs always-on) were designed from the web-cycle
discussion; they map one-to-one onto the two spidroin terminal domains.

---

- **[Askarieh2010]** Askarieh, G., Hedhammar, M., Nordling, K., Saenz, A.,
  Casals, C., Rising, A., Johansson, J. & Knight, S. D. (2010). *Self-assembly
  of spider silk proteins is controlled by a pH-sensitive relay.* Nature 465,
  236–238. — the **C-terminal domain** forms a constitutive, disulfide-locked
  parallel homodimer (an **always-on** link that pre-aligns the repeats).
- **[Hagn2010]** Hagn, F., Eisoldt, L., Hardy, J. G., et al. (2010). *A
  conserved spider silk domain acts as a molecular switch that controls fibre
  assembly.* Nature 465, 239–242. — the C-terminal domain as an assembly
  switch.
- **[Landreh2017]** Landreh, M., Rising, A., Presto, J., Jörnvall, H. &
  Johansson, J. (2017). Reviews of the **N-terminal domain** as a
  **pH-sensitive dimerisation switch**: monomeric/soluble at pH ≈ 7 (storage),
  dimerising below pH ≈ 5.7 in the duct via protonation of conserved
  glutamates — a **context-triggered** link that daisy-chains spidroins into
  one network only when local conditions are right.
- **[Rising2015]** Rising, A. & Johansson, J. (2015). *Toward spinning
  artificial spider silk.* Nat. Chem. Biol. 11, 309–315. — the mini-spidroin
  design distilling NT–repeat–CT.

## What it anchors

The idea-grammar's two links in `VAPMIP/boxkite_orbweaver_monad.py` /
`Tuning-the-Engine/35`:

- **`BIND(structural)`** = the CT-domain dimer — the always-on section
  skeleton, committed up front.
- **`TRANSITION(on=context)`** = the NT-domain pH switch — a "however /
  therefore" that forms only when the surrounding argument has dropped into
  the right regime.

## Cite in

`VAPMIP/docs/wiki/Tuning-the-Engine/35_the_spider_web_composition_cycle.md`.
