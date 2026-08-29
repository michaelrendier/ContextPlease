# 101 — The Cayley–Dickson literature

[98_provenance_and_citations.md](98_provenance_and_citations.md) §A.4. The
sources for the tower ℝ → ℂ → ℍ → 𝕆 → 𝕊, its property-loss ladder, and the
sedenion zero-divisor structure.

---

## The construction and its algebra

- **[Cayley1845]** Cayley, A. (1845). *On Jacobi's elliptic functions… and on
  quaternions.* Philos. Mag. (3) 26, 208–211. — the octonions, in an appendix.
  (Independently: Graves, J. T., letters to Hamilton, 1843.)
- **[Dickson1919]** Dickson, L. E. (1919). *On quaternions and their
  generalization and the history of the eight square theorem.* Annals of
  Mathematics 20(3), 155–171. DOI:10.2307/1967865. — the doubling map
  `(a,b)·(c,d) = (ac − d̄b, da + bc̄)`.
- **[Hurwitz1898]** Hurwitz, A. (1898). *Über die Composition der quadratischen
  Formen von beliebig vielen Variablen.* Nachr. Ges. Wiss. Göttingen, 309–316.
  — normed composition algebras exist **only** in dimensions 1, 2, 4, 8.
- **[Schafer1966]** Schafer, R. D. (1966). *An Introduction to Nonassociative
  Algebras.* Academic Press. — the standard textbook treatment.
- **[Baez2002]** Baez, J. C. (2002). *The Octonions.* Bull. AMS 39(2), 145–205.
  arXiv:math/0105155. — the canonical modern review: Fano-plane multiplication,
  automorphism group G₂, the exceptional series.

**Takes:** each doubling sacrifices exactly one property — ℝ→ℂ order, ℂ→ℍ
commutativity, ℍ→𝕆 associativity, 𝕆→𝕊 alternativity (and division: 𝕊 is the
first rung with zero divisors). "The lost property **is** the signal" — it
encodes that layer's gauge structure (wiki/01, wiki/19). Hurwitz's theorem is
why 𝕆 is the last "nice" rung and 𝕊 the first hard boundary.

## The sedenion zero-divisor structure

- **[Moreno1998]** Moreno, G. (1998). *The zero divisors of the Cayley–Dickson
  algebras over the real numbers.* Bol. Soc. Mat. Mexicana (3) 4(1), 13–28.
  arXiv:q-alg/9710013. — the norm-one zero divisors of 𝕊 are homeomorphic to
  the exceptional Lie group **G₂**.
- **[Cawagas2004]** Cawagas, R. E. (2004). *On the structure and zero divisors
  of the Cayley–Dickson sedenion algebra.* Discuss. Math. GAA 24(2), 251–265.
  — the complete enumeration: **84** unit zero-divisor pairs on S¹⁵, **42**
  equivalence classes. The framework's `12000/12000` convergence check
  reproduces this exactly.
- **[deMarrais2000]** de Marrais, R. P. C. (2000). *The 42 Assessors and the
  Box-Kites they fly.* arXiv:math/0011260. — the box-kite figure, the sail /
  strut / vent / trip-triplet vocabulary, twisted box kites, higher 2ᴺ.

**Takes:** the 42/84/168/336 counts; the seven box kites (octahedra, K₂,₂,₂); the
42 zero-divisor pairs as the primary structure bridging the two octonion halves
(e₀–e₇ and e₈–e₁₅). **The framework's refinement:** the labelling-preserving
finite object is **PSL(2,7)** (order 168), not G₂ — G₂ is the *continuous shadow*
that forgets which Fano line is which (wiki/84; ValaQuenta box_kite module).
Moreno's homeomorphism is a "blow-up" that loses the finite structure, exactly
as de Marrais argued.

Downstream, in this repo: `ValaQuenta/wiki/box_kite.md`,
`ValaQuenta/wiki/pencil_hyperstring.md` (the box kite gets a load-bearing tether
and a wind-deformation reconstruction — provenance table on that page).

---

## Appears in

wiki/19, wiki/25, wiki/84–90, wiki/98, wiki/101; ValaQuenta box_kite +
derivation_chain modules; D-CS_Memory §7–9; VAPMIP_Paper §5–6.
