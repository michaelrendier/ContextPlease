# 117 — Rising & Johansson: the Spidroin Terminal-Domain Switches

| | |
|---|---|
| Scope | the two spidroin terminal domains (an always-on link and a pH-triggered link) as the biological parallel of the composition model's two link types |
| Intake | citation pass, 2026-09-04 session; [98](98_provenance_and_citations.md). **Independent parallel**: the context-triggered and always-on links were designed from the web-cycle discussion and map one-to-one onto the two terminal domains |
| Verification (2026-11-13) | **Hagn et al. 2010** (*Nature* 465(7295), 239–242) and **Rising & Johansson 2015** (*Nat. Chem. Biol.* 11(5), 309–315) resolved against Crossref. **Askarieh et al. 2010** (*Nature* 465, 236–238) was not located by the search (it returned a protein-structure deposit with the same title). **The Landreh 2017 entry is incomplete** (no title or journal), and a search for it returned a 2012 NMR structure record of the N-terminal domain, so it is listed as unverified |
| Confidence | the mechanism as published: as recorded in the sources (the pH values are quoted, not re-read) · the mapping onto `BIND` and `TRANSITION`: `INTERPRETATION` |

## 1. The references

- **[Askarieh2010]** G. Askarieh, M. Hedhammar, K. Nordling, A. Saenz, C. Casals, A. Rising, J. Johansson & S. D. Knight, *Self-assembly of spider silk proteins is controlled by a pH-sensitive relay*, *Nature* 465, 236–238 (2010): the **N-terminal domain** as a pH-sensitive relay (not located in the checks; see the header). The earlier page attributed the constitutive disulfide-locked parallel homodimer to the C-terminal domain, "an always-on link that pre-aligns the repeats" (quoted from the earlier page).
- **[Hagn2010]** F. Hagn, L. Eisoldt, J. G. Hardy et al., *A conserved spider silk domain acts as a molecular switch that controls fibre assembly*, *Nature* 465, 239–242 (2010) (verified): the C-terminal domain as an assembly switch.
- **[Landreh2017]** M. Landreh, A. Rising, J. Presto, H. Jörnvall & J. Johansson (2017), reviews of the N-terminal domain as a **pH-sensitive dimerisation switch**: monomeric and soluble at pH ≈ 7 (storage), dimerising below pH ≈ 5.7 in the duct via protonation of conserved glutamates, a context-triggered link that daisy-chains spidroins into one network only when local conditions are right. **Entry incomplete and unverified** (title and journal absent from the record; the specific pH value is as quoted on the earlier page).
- **[Rising2015]** A. Rising & J. Johansson, *Toward spinning artificial spider silk*, *Nat. Chem. Biol.* 11, 309–315 (2015) (verified): the mini-spidroin design distilling N-terminal domain – repeat – C-terminal domain.

## 2. What it anchors  `INTERPRETATION`

The idea-grammar's two links in `VAPMIP/boxkite_orbweaver_monad.py` and `Tuning-the-Engine/35`:

- **`BIND(structural)`** = the dimer that is always on: the section skeleton, committed up front.
- **`TRANSITION(on=context)`** = the pH switch: a "however / therefore" that forms only when the surrounding argument has dropped into the right regime.

The mapping is a design analogy: the biology is the cited work; the two link types in the composition engine were specified from the web-cycle discussion and have not been tested against the biochemistry. (Which of the two terminal domains carries the always-on and which the pH-triggered role should be rechecked against the papers when the Askarieh and Landreh entries are located, since the earlier page and the 2010 title assign the pH relay to different terminal domains.)

## 3. Cite in

`VAPMIP/docs/wiki/Tuning-the-Engine/35_the_spider_web_composition_cycle.md`.

## 4. Related pages

[98](98_provenance_and_citations.md) · [113](113_vollrath_knight_silk_spinning.md) · [118](118_citation_pass_2026_09_04.md)
