# 100 — Division algebras and physics: the nearest prior art

[98_provenance_and_citations.md](98_provenance_and_citations.md) §A.6. This page
exists because the framework's "the Cayley–Dickson tower encodes the Standard
Model gauge group" claim has **direct, serious prior art**, and honesty requires
naming it wherever the claim appears.

---

## The prior work

- **[Dixon1994]** Dixon, G. M. (1994). *Division Algebras: Octonions,
  Quaternions, Complex Numbers and the Algebraic Design of Physics.* Kluwer.
  ISBN 0-7923-2890-6. — the algebra **T = ℂ ⊗ ℍ ⊗ 𝕆** as the substrate for one
  generation of Standard-Model fermions; the gauge group from division-algebra
  structure.
- **[Furey2016]** Furey, C. (2016). *Standard model physics from an algebra?*
  PhD thesis, University of Waterloo. arXiv:1611.09182.
- **[Furey2018]** Furey, C. (2018). *SU(3)_C × SU(2)_L × U(1)_Y (× U(1)_X) as a
  symmetry of division algebraic ladder operators.* Eur. Phys. J. C 78, 375.
  arXiv:1806.00612. — an explicit realisation of the SM symmetry group as a
  symmetry of ladder operators built from ℂ⊗𝕆 (and ℂ⊗ℍ⊗𝕆).
- **[GunaydinGursey1973]** Gürsey, F. & Günaydin, M. (1973). *Quark structure
  and octonions.* J. Math. Phys. 14, 1651–1667. — octonions → SU(3) colour, the
  early result the modern programme grew from.
- Review context: **[Baez2002]**, *The Octonions*, §§4–5 (G₂, F₄, E₆ and
  physics).

## What Ainulindalë takes, and how it differs

**Takes:** the reading that ℂ → U(1), ℍ → SU(2), 𝕆 → SU(3) (approx.), and that
the property lost at each Cayley–Dickson doubling (order, commutativity,
associativity, alternativity) is where that layer's gauge structure lives.
This is Dixon/Furey territory and is cited as such (wiki/13, wiki/19, wiki/43,
README §References; D-CS_Memory §7).

**Differs — and this is what `~/.clauderc_user_provenance` §B records:**
1. The gauge structure here is read off a **derived Lagrangian** (L_NN /
   L_dynamic), claimed term-for-term isometric with the observed SM Lagrangian,
   rather than built into a division-algebra fermion model.
2. The target is a **CS / persistent-memory engineering result**, not a physics
   model — the SM isometry is a consequence noticed post-hoc, and α_F = 1/137 is
   read as an **error check**, not a coupling to be fitted.
3. The framework goes one rung further, to the **sedenion 𝕊** — where zero
   divisors appear — and treats that rung (not 𝕆) as the operating algebra,
   because the Zero Lattice only exists there.
4. **0_RB** — the null-but-present composite operator — has no counterpart in
   the division-algebra SM literature.

**What is NOT claimed:** priority over Dixon or Furey on the tower → gauge-group
correspondence. That correspondence is theirs. The framework uses it and builds
elsewhere.

---

## Appears in

wiki/13, wiki/19, wiki/43, wiki/98; README §References; D-CS_Memory §7;
VAPMIP_Paper §"Engine 13", §A.5.
