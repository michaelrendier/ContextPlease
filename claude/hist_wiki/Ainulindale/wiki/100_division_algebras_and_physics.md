# 100 — Division Algebras and Physics: the Nearest Prior Art

| | |
|---|---|
| Scope | the prior work (Dixon, Furey, Günaydin–Gürsey, Baez) on the Standard-Model symmetry group from division algebras; what Ainulindalë takes from it; how the framework differs; what is not claimed |
| Companion to | [98](98_provenance_and_citations.md) §A.6, [19](19_cayley_dickson_tower.md) §3 |
| Verification (2026-11-13) | Furey 2016 (arXiv:1611.09182, *Standard model physics from an algebra?*), Furey 2018 (arXiv:1806.00612 and *Eur. Phys. J. C* 78, 375, DOI) and Baez 2002 (arXiv:math/0105155; *Bull. AMS* 39(2), 145–205, DOI) were checked against the public records, titles and volumes agreeing ([98](98_provenance_and_citations.md) §E). Dixon 1994 (Kluwer, ISBN 0-7923-2890-6) and Günaydin–Gürsey 1973 (*J. Math. Phys.* 14, 1651) are books/older papers and were not machine-verified |
| Confidence | the citations: as in §E · the framework's reading: `THEORETICAL`; priority is **not** claimed (§3) |

The framework's statement that "the Cayley–Dickson tower encodes the Standard-Model gauge group" has direct, serious prior art, and honesty requires naming it wherever the claim appears.

## 1. The prior work

- **[Dixon1994]** G. M. Dixon, *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics* (Kluwer, 1994): the algebra T = ℂ ⊗ ℍ ⊗ 𝕆 as the substrate for one generation of Standard-Model fermions; the gauge group from division-algebra structure.
- **[Furey2016]** C. Furey, *Standard model physics from an algebra?*, PhD thesis, Waterloo, arXiv:1611.09182.
- **[Furey2018]** C. Furey, *SU(3)_C × SU(2)_L × U(1)_Y (× U(1)_X) as a symmetry of division algebraic ladder operators*, *Eur. Phys. J. C* 78, 375, arXiv:1806.00612: an explicit realisation of the SM symmetry group as a symmetry of ladder operators built from ℂ ⊗ 𝕆 (and ℂ ⊗ ℍ ⊗ 𝕆).
- **[GunaydinGursey1973]** F. Gürsey & M. Günaydin, *Quark structure and octonions*, *J. Math. Phys.* 14, 1651: octonions → SU(3) colour, the early result the modern programme grew from.
- Review context: **[Baez2002]**, *The Octonions*, §§4–5 (G₂, F₄, E₆ and physics).

## 2. What Ainulindalë takes

The reading ℂ → U(1), ℍ → SU(2), 𝕆 → SU(3) (approximately), and that the property lost at each Cayley–Dickson doubling (order, commutativity, associativity, alternativity) is where that layer's gauge structure lives. The loss ladder is a verified fact of the algebra ([19](19_cayley_dickson_tower.md) Listing 1); the identification of the groups with the layers is the published Dixon/Furey proposal, cited as such wherever it appears ([13](13_omgwtf_rh_proof.md), [19](19_cayley_dickson_tower.md),
[43](43_emmy_noether_sedenion.md), README §References; D-CS_Memory §7). The linear relabelling σ = 1 − k/4 that places the three forces at σ = ¾, ½, ¼ is the framework's own ([69](69_tri_layer_emergence.md) §3).

## 3. Where it differs, and what is not claimed

1. The gauge structure here is read off a **derived Lagrangian** (L_NN / L_dynamic), claimed term-for-term isometric with the observed Standard-Model Lagrangian, instead of being built into a division-algebra fermion model. Under the author's scope ruling of 2026-11-13 the Standard Model Lagrangian "fitted as it is" belongs to Ainulindalë and the VAPMIP Lagrangian is the **derived backup analogue**, found while building a way to drop dimensions from calculations by using larger puzzle pieces ([98](98_provenance_and_citations.md) §B).
2. The target is a CS / persistent-memory engineering result, not a physics model: the SM isometry is a consequence noticed afterwards, and α_F = 1/137 is read as an error check, not a coupling to be fitted (the fine-structure constant and A_fermat are distinct, [96](96_the_riemann_fermat_horizon.md) §5).
3. The framework goes one rung further, to the sedenion 𝕊, where zero divisors appear, and treats that rung as the operating algebra, because the Zero Lattice exists only there.
4. 0_RB, the null-but-present composite operator, has no counterpart in the division-algebra SM literature.

**Not claimed:** priority over Dixon or Furey on the tower → gauge-group correspondence. That correspondence is theirs; the framework uses it and builds elsewhere. (Dixon, Furey and Wyler's α formula are queued for the full citation pass: [134](134_the_library.md) §6, ledger X-7.)

## 4. Appears in

[13](13_omgwtf_rh_proof.md), [19](19_cayley_dickson_tower.md), [43](43_emmy_noether_sedenion.md), [98](98_provenance_and_citations.md); README §References; D-CS_Memory §7; VAPMIP_Paper "Engine 13", §A.5.
