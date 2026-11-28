# 101 — The Cayley–Dickson Literature

| | |
|---|---|
| Scope | the sources for the tower ℝ → ℂ → ℍ → 𝕆 → 𝕊, its property-loss ladder and the sedenion zero-divisor structure; what the framework takes and its one refinement |
| Companion to | [98](98_provenance_and_citations.md) §A.4 |
| Verification (2026-11-13) | arXiv records checked: Moreno (q-alg/9710013, 1997), de Marrais (math/0011260, 2000), Baez (math/0105155); DOIs checked: Dickson 1919 (*Ann. Math.* 20(3), 155), Baez 2002, and Cawagas 2004 (DOI 10.7151/dmgaa.1088 returned by a bibliographic search). Cayley 1845, Hurwitz 1898 and Schafer 1966 were not machine-verified ([98](98_provenance_and_citations.md) §E) |
| Confidence | the construction and the counts: ESTABLISHED (re-run in [19](19_cayley_dickson_tower.md), [71](71_zd_statement_machine.md), [84](84_the_box_kite_debugger.md), [89](89_the_seven_octonions.md)) · the "lost property is the signal" reading: `THEORETICAL` |

## 1. The construction and its algebra

- **[Cayley1845]** A. Cayley, *On Jacobi's elliptic functions … and on quaternions*, *Philos. Mag.* (3) 26, 208–211: the octonions, in an appendix (independently J. T. Graves, letters to Hamilton, 1843).
- **[Dickson1919]** L. E. Dickson, *On quaternions and their generalization and the history of the eight square theorem*, *Ann. Math.* 20(3), 155–171: the doubling (a, b)·(c, d) = (ac − d̄b, da + bc̄). This is the product the wiki's listings use; [19](19_cayley_dickson_tower.md) Listing 1 writes it with the halves named (a₁, a₂) and (b₁, b₂): (a₁b₁ − conj(b₂)a₂, b₂a₁ + a₂conj(b₁)), term for term the same formula.
- **[Hurwitz1898]** A. Hurwitz, *Über die Composition der quadratischen Formen von beliebig vielen Variablen*, *Nachr. Ges. Wiss. Göttingen*, 309–316: normed composition algebras exist only in dimensions 1, 2, 4, 8.
- **[Schafer1966]** R. D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press).
- **[Baez2002]** J. C. Baez, *The Octonions*, *Bull. AMS* 39(2), 145–205: Fano-plane multiplication, G₂, the exceptional series.

**Takes:** each doubling sacrifices exactly one property: ℝ → ℂ order, ℂ → ℍ commutativity, ℍ → 𝕆 associativity, 𝕆 → 𝕊 alternativity (and division: 𝕊 is the first rung with zero divisors); "the lost property **is** the signal" encodes that layer's gauge structure ([01](01_overview.md), [19](19_cayley_dickson_tower.md)). Hurwitz's theorem is why 𝕆 is the last "nice" rung and 𝕊 the first hard boundary.

## 2. The sedenion zero-divisor structure

- **[Moreno1998]** G. Moreno, *The zero divisors of the Cayley–Dickson algebras over the real numbers* (preprint 1997, *Bol. Soc. Mat. Mexicana* 1998): the norm-one zero divisors of 𝕊 are homeomorphic to the exceptional Lie group **G₂**.
- **[Cawagas2004]** R. E. Cawagas, *On the structure and zero divisors of the Cayley–Dickson sedenion algebra*, *Discuss. Math. GAA* 24(2), 251–265: the complete enumeration. In this wiki's counting ([71](71_zd_statement_machine.md), [84](84_the_box_kite_debugger.md), reproduced 2026-11-13): **84** zero-divisor diagonals eᵢ ± eⱼ on **42** index pairs (the Assessors), 168 unordered zero-product pairs counting every sign pattern, 336 ordered. The framework's `12000/12000` convergence check is recorded as reproducing the enumeration (not re-run).
- **[deMarrais2000]** R. P. C. de Marrais, *The 42 Assessors and the Box-Kites they fly* (arXiv:math/0011260): the box-kite figure, the sail / strut / vent / trip-triplet vocabulary, twisted box-kites, higher 2ᴺ.

**Takes:** the 42/84/168/336 counts; the seven box-kites (octahedra, K₂,₂,₂); the 42 zero-divisor pairs as the primary structure bridging the two octonion halves (e₀–e₇ and e₈–e₁₅). **The framework's refinement:** the labelling-preserving finite object is PSL(2, 7) (order 168), not G₂; G₂ is the continuous shadow that forgets which Fano line is which ([84](84_the_box_kite_debugger.md); the page's reading of de Marrais; Moreno's homeomorphism is a "blow-up" that loses the finite structure).

Downstream: `ValaQuenta/wiki/box_kite.md`, `ValaQuenta/wiki/pencil_hyperstring.md` (the box-kite with a load-bearing tether and a wind-deformation reconstruction; provenance table on that page).

## 3. Appears in

[19](19_cayley_dickson_tower.md), [25](25_sedenion_manual.md), [84](84_the_box_kite_debugger.md)–[90](90_divisors_are_definers.md), [98](98_provenance_and_citations.md); ValaQuenta `box_kite` and `derivation_chain` modules; D-CS_Memory §7–9; VAPMIP_Paper §5–6.
