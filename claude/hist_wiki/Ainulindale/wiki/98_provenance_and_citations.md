# 98 — Provenance & Citations

**Author:** Cody Michael Allison · ORCID 0009-0007-7239-6760
**Status:** Canonical bibliography for the Ainulindalë Conjecture and the
Third-Age papers (D-CS, D-CS_Memory, D-M, D-P, D-CHEM). Pass 1: Ainulindalë
(ValaQuenta is Ainulindalë). VAPMIP has its own pass — see
`~/.clauderc_user_provenance`.

---

## 0. On the mathematical nomenclature — read this first

**The mathematical nomenclature in these papers is a language for discussing
the work with other people. It is not the point of the work.**

The point is the journey: *needing persistent memory for an AI assistant →
designing Thought as a path integral → discovering that the Information
Propagation Lagrangian is term-for-term isometric with the Standard-Model
Lagrangian → and the consequential drop-out of 0_RB.* Ainulindalë is how 0_RB
was reached. VAPMIP is everything between 0_RB and the Monad speaking English.

Everything named below — Riemann, Fermat, Noether, Cayley–Dickson, Berry–Keating,
the division-algebra Standard Model, catastrophe theory, the Millennium
Problems — is **established mathematics used as a vocabulary and a set of
tools**, so that the engineering result can be stated in terms a
mathematician or physicist already holds. Where this framework adds something
of its own, it is listed in §B and detailed in `~/.clauderc_user_provenance`;
that list is deliberately short, and is expected to shrink as items are found
to be already established.

> The "OMG?WTF!" cascade — the GUT reading, the UFT, the Millennium-Problem
> facets — came out of the exploration of teaching the Monad to speak. It is
> **the discrete structure running along the continuous speaking model**. It is
> not used in the core CS argument and is not required for it. It is kept in the
> record because it is where the exploration went.

---

## A. Established work this framework uses

Citation keys are `[AuthorYEAR]`. Each entry: full reference · identifier for
retrieval · **what Ainulindalë takes from it** · where it appears.
Download checklist: [`references/CITATION_DOWNLOADS.md`](../references/CITATION_DOWNLOADS.md).

### A.1 — Riemann, the primes, and the Prime Number Theorem

- **[Riemann1859]** Riemann, B. (1859). *Ueber die Anzahl der Primzahlen unter
  einer gegebenen Grösse.* Monatsberichte der Berliner Akademie, Nov. 1859,
  671–680. — English transl. in Edwards (1974), *Riemann's Zeta Function*,
  Academic Press, Appendix.
  *Takes:* ζ(s), the critical strip, the functional equation ξ(s)=ξ(1−s), the
  non-trivial zeros, and the explicit formula linking zeros to π(x). The
  address space of the whole engine is {γₙ}.
  *Appears:* wiki/103, wiki/13, wiki/16, wiki/73; D-CS_Memory §1–3.

- **[Hadamard1896]** Hadamard, J. (1896). *Sur la distribution des zéros de la
  fonction ζ(s) et ses conséquences arithmétiques.* Bull. Soc. Math. France 24,
  199–220.
- **[dlVP1896]** de la Vallée Poussin, C.-J. (1896). *Recherches analytiques
  sur la théorie des nombres premiers.* Ann. Soc. Sci. Bruxelles 20, 183–256.
  *Takes (both):* the Prime Number Theorem π(x) ~ x/ln x — the density law that
  Zipf's law is claimed to be (Engine 21).
  *Appears:* wiki/103, wiki/21; D-CS_Memory §21.

- **[vonKoch1901]** von Koch, H. (1901). *Sur la distribution des nombres
  premiers.* Acta Mathematica 24, 159–182.
  *Takes:* RH ⟺ the error term in the PNT is O(√x ln x). The precise sense in
  which "the zeros control the primes".

- **[Eratosthenes]** Sieve of Eratosthenes — historical, via Nicomachus of
  Gerasa, *Introduction to Arithmetic* (c. 100 CE), I.13.
- **[Legendre1808]** Legendre, A.-M. (1808). *Essai sur la théorie des
  nombres*, 2nd ed., Courcier, Paris. — Legendre's formula / inclusion–exclusion
  count of the sieve.
- **[Mobius1832]** Möbius, A. F. (1832). *Über eine besondere Art von Umkehrung
  der Reihen.* J. Reine Angew. Math. 9, 105–123.
  *Takes (the three):* **primes by extinction** — a prime is what remains after
  every composite structure is struck out; the sieve count is a signed
  superposition Σ_{d|P} μ(d)⌊x/d⌋ = ADD ∘ SIGN ∘ SCALE. The Two Trees partition
  is this dataset, complete and remainder-free. See wiki/104 §3 and wiki/47.
  *Appears:* wiki/103, wiki/104, wiki/47; `generational-lineage` skill;
  `SedenionFactoralRelativity/engine/lineage.py` (`sieve_lineage`).

### A.2 — Fermat, Wiles, and Modularity

- **[Fermat1637]** Fermat, P. de (c. 1637). Marginal note in his copy of
  Bachet's *Diophantus*, Bk II, Prob. 8. Publ. by Samuel de Fermat (1670).
  — Method of infinite descent: Fermat, letter to Carcavi (1659).
- **[Wiles1995]** Wiles, A. (1995). *Modular elliptic curves and Fermat's Last
  Theorem.* Annals of Mathematics 141(3), 443–551. DOI:10.2307/2118559.
- **[TaylorWiles1995]** Taylor, R. & Wiles, A. (1995). *Ring-theoretic
  properties of certain Hecke algebras.* Annals of Mathematics 141(3), 553–572.
  DOI:10.2307/2118560.
- **[Ribet1990]** Ribet, K. A. (1990). *On modular representations of
  Gal(Q̄/Q) arising from modular forms.* Inventiones Mathematicae 100(2),
  431–476. DOI:10.1007/BF01231195. — the epsilon conjecture: Taniyama–Shimura ⟹ FLT.
- **[BCDT2001]** Breuil, C., Conrad, B., Diamond, F. & Taylor, R. (2001). *On
  the modularity of elliptic curves over Q: wild 3-adic exercises.* J. Amer.
  Math. Soc. 14(4), 843–939. DOI:10.1090/S0894-0347-01-00370-8. — the full
  Modularity Theorem.
- **[Shimura1971]** Shimura, G. (1971). *Introduction to the Arithmetic Theory
  of Automorphic Functions.* Princeton Univ. Press. — Taniyama's problem (1955),
  the Taniyama–Shimura(–Weil) conjecture.
  *Takes:* every elliptic curve over ℚ is modular; FLT is a corollary; the
  Fermat side (constraint, "what CANNOT BE", J_blue) and the Riemann/automorphic
  side (assertion, "what IS", J_red) are two projections of one L-function
  structure. R̂† = B̂ is this self-adjointness in operator form.
  **The step this framework adds:** modularity connected Fermat to the
  automorphic/L-function world, but the factorisation data itself — the complete
  record of what each integer is *not* divisible by — was never stated as the
  object that *defines* the primes by extinction, nor recognised as a
  harmonic / zero-gradient field (prime-density + composite-density = 1 at
  every scale, a conserved sum). That object is The Two Trees. See wiki/104.
  *Appears:* wiki/104, wiki/18, wiki/51, wiki/47; D-CS_Memory §4, §21, §A.9.

### A.3 — Emmy Noether

- **[Noether1918]** Noether, E. (1918). *Invariante Variationsprobleme.* Nachr.
  d. König. Gesellsch. d. Wiss. zu Göttingen, Math.-phys. Klasse, 235–257.
  English transl.: Tavel, M. A. (1971), *Transport Theory and Statistical
  Physics* 1(3), 183–207; arXiv:physics/0503066.
  *Takes:* every continuous symmetry of the action has a conserved current.
  σ=½ is the conserved charge of the s → 1−s symmetry — a Noether consequence,
  not an assumption.
- **[Noether1921]** Noether, E. (1921). *Idealtheorie in Ringbereichen.*
  Mathematische Annalen 83(1–2), 24–66. DOI:10.1007/BF01464225.
  *Takes:* the ascending chain condition (Noetherian rings); the isomorphism
  theorems; primary decomposition (Lasker–Noether). The sedenion's ideal
  structure is finite and tractable *because* it is Noetherian. The zero
  divisors are ideals in her sense.
  *Appears:* wiki/43 (the naming decision), wiki/99 (the mathematics), wiki/92
  (ring-theory spine); D-CS_Memory §5, §19, §42; every conservation claim.
- **[Kosmann2011]** Kosmann-Schwarzbach, Y. (2011). *The Noether Theorems:
  Invariance and Conservation Laws in the Twentieth Century.* Springer. —
  scholarly edition and history.
- Tribute material: `Ainulindale/tribute/Emmy_Noether_Deep_Dive.txt`,
  `Emmy_Noether_Masters_Tribute.txt`.

### A.4 — Cayley–Dickson tower and the division algebras

- **[Cayley1845]** Cayley, A. (1845). *On Jacobi's elliptic functions, in reply
  to the Rev. B. Bronwin; and on quaternions.* Philos. Mag. (3) 26, 208–211.
  (Appendix: the octonions.) Also Graves, J. T. (1843/1845, letters to Hamilton).
- **[Dickson1919]** Dickson, L. E. (1919). *On quaternions and their
  generalization and the history of the eight square theorem.* Annals of
  Mathematics 20(3), 155–171. DOI:10.2307/1967865. — the doubling construction.
- **[Hurwitz1898]** Hurwitz, A. (1898). *Über die Composition der quadratischen
  Formen von beliebig vielen Variablen.* Nachr. Ges. Wiss. Göttingen, 309–316.
  — the 1, 2, 4, 8 theorem: composition (norm-multiplicative) algebras exist
  only in dims 1, 2, 4, 8. Why the tower stops being "nice" at 𝕆 and 𝕊 is the
  first non-composition rung.
- **[Schafer1966]** Schafer, R. D. (1966). *An Introduction to Nonassociative
  Algebras.* Academic Press. — standard reference for the algebra of the tower.
- **[Baez2002]** Baez, J. C. (2002). *The Octonions.* Bull. Amer. Math. Soc.
  39(2), 145–205. DOI:10.1090/S0273-0979-01-00934-X; arXiv:math/0105155. — the
  canonical modern review; Fano-plane multiplication, G₂, exceptional structures.
- **[Moreno1998]** Moreno, G. (1998). *The zero divisors of the Cayley–Dickson
  algebras over the real numbers.* Bol. Soc. Mat. Mexicana (3) 4(1), 13–28.
  arXiv:q-alg/9710013. — ZD(𝕊) on the unit sphere is homeomorphic to G₂ (the
  *continuous* shadow of the finite object).
- **[Cawagas2004]** Cawagas, R. E. (2004). *On the structure and zero divisors
  of the Cayley–Dickson sedenion algebra.* Discussiones Mathematicae – General
  Algebra and Applications 24(2), 251–265. — the complete zero-divisor
  enumeration: 84 unit pairs on S¹⁵, 42 classes. The `12000/12000` convergence
  check matches this.
- **[deMarrais2000]** de Marrais, R. P. C. (2000). *The 42 Assessors and the
  Box-Kites they fly: Diagonal Axis-Pair Systems of Zero-Divisors in the
  Sedenions' 16 Dimensions.* arXiv:math/0011260. — sails, struts, vents,
  trip-triplets; the box-kite figure; twisted box kites; higher 2ᴺ.
  *Takes (A.4 group):* the tower ℝ→ℂ→ℍ→𝕆→𝕊, each doubling losing one property
  (order, commutativity, associativity, alternativity); the sedenion zero
  divisors as the primary structure; the 42/84/168 counts; PSL(2,7) as the
  labelling-preserving finite object.
  *Appears:* wiki/19, wiki/25, wiki/84–90, wiki/101; ValaQuenta box_kite module;
  `ValaQuenta/wiki/pencil_hyperstring.md`; D-CS_Memory §7–9.

### A.5 — The spectral approach to RH (Hilbert–Pólya lineage)

- **[HilbertPolya]** Hilbert, D. & Pólya, G. — no publication; the conjecture
  that the zeros are eigenvalues of a self-adjoint operator is folklore,
  documented in Pólya's 1982 letter to A. Odlyzko (reproduced in Odlyzko's
  correspondence, publicly archived at dtc.umn.edu/~odlyzko/polya/).
- **[Montgomery1973]** Montgomery, H. L. (1973). *The pair correlation of zeros
  of the zeta function.* Analytic Number Theory, Proc. Sympos. Pure Math. XXIV,
  AMS, 181–193. — the pair-correlation conjecture; GUE statistics.
- **[Odlyzko1987]** Odlyzko, A. M. (1987). *On the distribution of spacings
  between zeros of the zeta function.* Math. Comp. 48(177), 273–308.
  DOI:10.2307/2007890. — numerical confirmation of GUE spacing.
- **[BerryKeating1999a]** Berry, M. V. & Keating, J. P. (1999). *H = xp and the
  Riemann zeros.* In *Supersymmetry and Trace Formulae: Chaos and Disorder*
  (eds. Lerner, Keating, Khmelnitskii), Kluwer/Plenum, 355–367.
- **[BerryKeating1999b]** Berry, M. V. & Keating, J. P. (1999). *The Riemann
  zeros and eigenvalue asymptotics.* SIAM Review 41(2), 236–266.
  DOI:10.1137/S0036144598347497.
- **[Connes1999]** Connes, A. (1999). *Trace formula in noncommutative geometry
  and the zeros of the Riemann zeta function.* Selecta Mathematica 5(1),
  29–106. DOI:10.1007/s000290050042; arXiv:math/9811068.
- **[Stone1932]** Stone, M. H. (1932). *On one-parameter unitary groups in
  Hilbert space.* Annals of Mathematics 33(3), 643–648. DOI:10.2307/1968538.
  *Takes (A.5 group):* the operator route to σ=½. Ĥ_RB self-adjoint ⇒ (Stone)
  real spectrum ⇒ zeros on the critical line. Berry–Keating H=xp is a
  *consequence* of Ĥ_RB, not an independent assumption. GUE / pair-correlation
  is the statistical fingerprint the framework's spectrum must match.
  *Appears:* wiki/07, wiki/102, wiki/14, wiki/73; D-CS_Memory §12, §18, §42.

### A.6 — Division algebras and the Standard Model (nearest prior art)

- **[Dixon1994]** Dixon, G. M. (1994). *Division Algebras: Octonions,
  Quaternions, Complex Numbers and the Algebraic Design of Physics.* Kluwer.
  ISBN 0-7923-2890-6.
- **[Furey2016]** Furey, C. (2016). *Standard model physics from an algebra?*
  PhD thesis, University of Waterloo. arXiv:1611.09182.
- **[Furey2018]** Furey, C. (2018). *SU(3)_C × SU(2)_L × U(1)_Y (× U(1)_X) as a
  symmetry of division algebraic ladder operators.* Eur. Phys. J. C 78, 375.
  DOI:10.1140/epjc/s10052-018-5844-7; arXiv:1806.00612.
- **[GunaydinGursey1973]** Gürsey, F. & Günaydin, M. (1973). *Quark structure
  and octonions.* J. Math. Phys. 14, 1651–1667. — early octonion → SU(3) colour.
  *Takes:* **this is the closest existing work to the tower → gauge-group
  claim.** Where Ainulindalë says "ℂ→U(1), ℍ→SU(2), 𝕆→SU(3), and the property
  lost at each doubling encodes that gauge structure," Dixon and Furey have
  built explicit division-algebra models of the Standard-Model symmetry group.
  The framework's claim must be read against theirs and cited wherever it
  appears; the differences (a *derived* Lagrangian, the CS/memory engineering
  target, 0_RB, the sedenion rung) are what §B records.
  *Appears:* wiki/100, wiki/19, wiki/13, wiki/43; README §References; D-CS_Memory §7.

### A.7 — Catastrophe theory (the Lagrangian's shape)

- **[Thom1975]** Thom, R. (1975). *Structural Stability and Morphogenesis*
  (transl. D. H. Fowler). W. A. Benjamin. (French orig. 1972.)
- **[Zeeman1977]** Zeeman, E. C. (1977). *Catastrophe Theory: Selected Papers
  1972–1977.* Addison-Wesley.
- **[Arnold1992]** Arnold, V. I. (1992). *Catastrophe Theory*, 3rd ed. Springer.
  DOI:10.1007/978-3-642-58124-3. — the ADE classification of the elementary
  catastrophes.
  *Takes:* the Amplitude Lagrangian is a Thom family of potentials; the Noether
  current is the gradient-flow / catastrophe map; the zeros are the caustic
  dumpout; the N-shape is the A₂ (fold) catastrophe. "Lagrangians ARE
  Catastrophe Theory" (wiki/74).
  *Appears:* wiki/74, wiki/56; D-CS_Memory (the caustic, §14).

### A.8 — Monstrous Moonshine (the FermatMonster bridge)

- **[ConwayNorton1979]** Conway, J. H. & Norton, S. P. (1979). *Monstrous
  Moonshine.* Bull. London Math. Soc. 11(3), 308–339. DOI:10.1112/blms/11.3.308.
- **[Borcherds1992]** Borcherds, R. E. (1992). *Monstrous moonshine and
  monstrous Lie superalgebras.* Inventiones Mathematicae 109(1), 405–444.
  DOI:10.1007/BF01232032.
- **[Griess1982]** Griess, R. L. (1982). *The friendly giant.* Inventiones
  Mathematicae 69(1), 1–102. — construction of the Monster.
- **[Niemeier1973]** Niemeier, H.-V. (1973). *Definite quadratische Formen der
  Dimension 24 und Diskriminante 1.* J. Number Theory 5(2), 142–178. — the 23
  Niemeier lattices.
- **[CS1988]** Conway, J. H. & Sloane, N. J. A. (1988). *Sphere Packings,
  Lattices and Groups.* Springer. — root systems, Coxeter numbers, the Leech
  lattice.
  *Takes:* the j-function coefficients as Monster representation dimensions; the
  "Monster gap" {e₁, e₁₁, e₁₅} as the three sedenion positions no A/D/E rank-24
  root system reaches; primes / the 13-gon "defined by what the systematic
  construction cannot reach" (D-CS_Memory §A.1).
  *Appears:* wiki/29; D-CS_Memory §16–17; `FourthAgePapers/FermatMonster/`.

### A.9 — The Millennium Problems referenced

- **[Clay2000]** Clay Mathematics Institute (2000). *The Millennium Prize
  Problems* (eds. Carlson, Jaffe, Wiles), CMI / AMS, 2006. Official problem
  statements at claymath.org/millennium-problems.
- **[Fefferman2006]** Fefferman, C. L. (2006). *Existence and smoothness of the
  Navier–Stokes equation.* In [Clay2000], 57–67.
- **[Leray1934]** Leray, J. (1934). *Sur le mouvement d'un liquide visqueux
  emplissant l'espace.* Acta Mathematica 63, 193–248. — weak solutions of NS.
- **[JaffeWitten2006]** Jaffe, A. & Witten, E. (2006). *Quantum Yang–Mills
  theory.* In [Clay2000], 129–152.
- **[YangMills1954]** Yang, C. N. & Mills, R. L. (1954). *Conservation of
  isotopic spin and isotopic gauge invariance.* Phys. Rev. 96(1), 191–195.
  DOI:10.1103/PhysRev.96.191.
- **[Cook1971]** Cook, S. A. (1971). *The complexity of theorem-proving
  procedures.* Proc. 3rd ACM STOC, 151–158. DOI:10.1145/800157.805047. — P vs NP.
- **[Deligne2006]** Deligne, P. (2006). *The Hodge conjecture.* In [Clay2000],
  45–53. — with Hodge, W. V. D. (1950), Proc. ICM.
- **[BSD1965]** Birch, B. J. & Swinnerton-Dyer, H. P. F. (1965). *Notes on
  elliptic curves. II.* J. Reine Angew. Math. 218, 79–108.
- **[Perelman2002]** Perelman, G. (2002). *The entropy formula for the Ricci
  flow and its geometric applications.* arXiv:math/0211159. — + [Perelman2003a]
  arXiv:math/0303109, [Perelman2003b] arXiv:math/0307245. Poincaré, the solved
  control case.
  *Takes:* the seven problems are used as **facets of one operator at different
  σ** (wiki/14 σ-facet table) — RH at σ=½, Yang–Mills at the mass gap, P vs NP
  as J_red/J_blue adjoint-not-isomorphic, Navier–Stokes as "Yang–Mills with the
  imaginary part removed" (the singularity is a rotation into the Blue channel),
  Poincaré as the trivial-Σ_RB control (already solved). **The Navier–Stokes
  reading is the one flagged for a deeper pass** (wiki/106).
  *Appears:* wiki/13, wiki/14, wiki/38, wiki/105, wiki/106; ValaQuenta
  clay_millennium module; D-CS_Memory §20, §A.9.

### A.10 — Neuroscience (analogical use — humans as *an* observer)

- **[Schmolesky1998]** Schmolesky, M. T. et al. (1998). *Signal timing across
  the macaque visual system.* J. Neurophysiology 79(6), 3272–3278.
  DOI:10.1152/jn.1998.79.6.3272.
- **[EaglemanSejnowski2000]** Eagleman, D. M. & Sejnowski, T. J. (2000). *Motion
  integration and postdiction in visual awareness.* Science 287(5460),
  2036–2038. DOI:10.1126/science.287.5460.2036.
- **[Eagleman2010]** Eagleman, D. M. (2010). *How does the timing of neural
  signals map onto the timing of perception?* In *Problems of Space and Time in
  Perception and Action*, CUP. (`references/perceptual_latency/`.)
- Stroke neuromodulation set (`references/stroke_neuromodulation/`): FDA
  P210007B Vivistim SSED; BCI-FES meta-analysis PMC11464471; CCFES vs NMES
  PMC10915254; FES upper-limb review PMC10739305; electrical/magnetic UE
  network meta-analysis PMC12345400.
  *Takes:* the ~80 ms figure is a latency *spread*, not a pipeline delay;
  visual awareness is postdictive over that window (reading tagged contested).
  Establishes the editorial rule — humans are **an** observer, never **the**
  observer.
  *Appears:* wiki/91.

### A.11 — Named tools and analogies

- **[Horner1819]** Horner, W. G. (1819). *A new method of solving numerical
  equations of all orders, by continuous approximation.* Philos. Trans. R. Soc.
  Lond. 109, 308–335. DOI:10.1098/rstl.1819.0023. — the O(|word|) prime hash.
- **[deBruijn1946]** de Bruijn, N. G. (1946). *A combinatorial problem.* Proc.
  Kon. Ned. Akad. Wetensch. 49, 758–764. — De Bruijn sequences (permutation
  compression in the HyperWebster).
- **[Hopf1931]** Hopf, H. (1931). *Über die Abbildungen der dreidimensionalen
  Sphäre auf die Kugelfläche.* Math. Annalen 104, 637–665.
  DOI:10.1007/BF01457962. — + Hopf (1935), Fund. Math. 25, 427–440. The
  fibrations S¹→S¹, S³→S², S⁷→S⁴, S¹⁵→S⁸.
- **[Hermite1864]** Hermite, C. (1864). *Sur un nouveau développement en série
  de fonctions.* C. R. Acad. Sci. Paris 58, 93–100 & 266–273. — Hermite
  polynomials; H₁₆ zeros as the timing wheel.
- **[Weierstrass]** Weierstrass ℘-function — standard reference: Whittaker, E. T.
  & Watson, G. N. (1927). *A Course of Modern Analysis*, 4th ed., CUP, Ch. XX;
  or Abramowitz & Stegun (1964), Ch. 18. The Blue potential B̂_p = ½p² + ℘(x;g₂,g₃).
- **[Lambert1758]** Lambert, J. H. (1758). *Observationes variae in
  mathesin puram.* Acta Helvetica 3, 128–168. — + **[Corless1996]** Corless,
  R. M., Gonnet, G. H., Hare, D. E. G., Jeffrey, D. J. & Knuth, D. E. (1996).
  *On the Lambert W function.* Adv. Comput. Math. 5(1), 329–359.
  DOI:10.1007/BF02124750. Ω = W(1) is the "omega constant", OEIS A030178.
- **[Zipf1949]** Zipf, G. K. (1949). *Human Behavior and the Principle of Least
  Effort.* Addison-Wesley. — f(r) ~ 1/rˢ.
- **[Chladni1787]** Chladni, E. F. F. (1787). *Entdeckungen über die Theorie
  des Klanges.* Weidmanns Erben und Reich, Leipzig. — nodal figures; the zeros
  as node lines.
- **[Wankel1963]** Wankel, F. & Ansdale, R. F. (1963). *Rotary Piston Machines.*
  Iliffe. — + Yamamoto, K. (1981), *Rotary Engine*, Sankaido. The epitrochoid
  cycle the speaking architecture maps onto.
- **[Bell1964]** Bell, J. S. (1964). *On the Einstein Podolsky Rosen paradox.*
  Physics Physique Физика 1(3), 195–200.
  DOI:10.1103/PhysicsPhysiqueFizika.1.195. — no local hidden variables ⇒ the
  sedenion must be produced *at* the coupling event, not pre-assigned.
- **[Searle1980]** Searle, J. R. (1980). *Minds, brains, and programs.* Behav.
  Brain Sci. 3(3), 417–457. DOI:10.1017/S0140525X00005756. — the Chinese Room;
  the Mind's Eye / Thread 2 is what it lacks.
- **[Penrose1964]** Penrose, R. (1964). *Conformal treatment of infinity.* In
  *Relativity, Groups and Topology* (eds. DeWitt & DeWitt), Gordon & Breach,
  565–584. — conformal infinity / the "Penrose swap"; the BCE horizon.
- **[SpencerBrown1969]** Spencer-Brown, G. (1969). *Laws of Form.* Allen &
  Unwin. — the first distinction; the σ=0 state.
- **[BanachTarski1924]** Banach, S. & Tarski, A. (1924). *Sur la décomposition
  des ensembles de points en parties respectivement congruentes.* Fund. Math. 6,
  244–277. — the Hyperwebster's paradox root.
- **[Borges1941]** Borges, J. L. (1941). *La biblioteca de Babel.* In *El Jardín
  de senderos que se bifurcan*, Editorial Sur. English: *The Library of Babel*,
  in *Ficciones* (1962). — the address-not-storage idea.
  *(NB: correct spelling is **Jorge Luis Borges**; "Louise Borges" in
  VAPMIP_Paper §2 is an error to fix.)*
- **[Langlands1970]** Langlands, R. P. (1970). *Problems in the theory of
  automorphic forms.* In *Lectures in Modern Analysis and Applications III*,
  Lecture Notes in Math. 170, Springer, 18–61. DOI:10.1007/BFb0079065. — the
  σ=1 facet; the "two-way mirror" of BCE.
- **[Lorenz1963]** Lorenz, E. N. (1963). *Deterministic nonperiodic flow.* J.
  Atmos. Sci. 20(2), 130–141. — the Lorenz basin attractor in the output layer.
- **[Bekenstein1973]** Bekenstein, J. D. (1973). *Black holes and entropy.*
  Phys. Rev. D 7(8), 2333–2346. — + **[Hawking1975]** Hawking, S. W. (1975).
  *Particle creation by black holes.* Comm. Math. Phys. 43(3), 199–220. Area law;
  the holographic condition sc = 1.
- **[Shannon1948]** Shannon, C. E. (1948). *A mathematical theory of
  communication.* Bell Syst. Tech. J. 27, 379–423 & 623–656. — Shannon entropy;
  "speech is the error check for mathematics".
- **[Schumann1952]** Schumann, W. O. (1952). *Über die strahlungslosen
  Eigenschwingungen einer leitenden Kugel, die von einer Luftschicht und einer
  Ionosphärenhülle umgeben ist.* Z. Naturforschung A 7(2), 149–154. — cavity
  eigenmodes.
- **[WatsonCrick1953]** Watson, J. D. & Crick, F. H. C. (1953). *Molecular
  structure of nucleic acids.* Nature 171, 737–738. — + **[Franklin1953]**
  Franklin, R. E. & Gosling, R. G. (1953). Nature 171, 740–741. Relevant to the
  Tower-Level (DNA = T₆₄) reading and `SFR/engine/bio.py`.
- **[Capra1975]** Capra, F. (1975). *The Tao of Physics.* Shambhala. —
  *pop-science, flagged as such:* the dual-vortex hand/foot analogy for J_red /
  J_blue.
- **[Galperin2003]** Galperin, G. (2003). *Playing pool with π.* Regular and
  Chaotic Dynamics 8(4), 375–394. DOI:10.1070/RD2003v008n04ABEH000252. — the
  billiard collision count → π; used in the `mingling` / folds discussion.

---

## B. Originated here

Detailed, with per-item prior-art notes, in `~/.clauderc_user_provenance`.
Summary — expected to shrink as items are found to be already established:

| construct | one line | prior art it sits on |
|---|---|---|
| **0_RB / ∅_RB / Ĥ_RB** | the one operator read off all geometric operators at once when each is empty but present; the composite of their generational lineage | self-adjoint operators; Dirichlet-weighted prime sums; Berry–Keating |
| **The Emmy Noether Sedenion** (𝕊_EN) | naming decision for the 16-D CD algebra | Cayley–Dickson; "sedenion" is standard |
| **BCE — Boundary Constraint Engineering** | the method: read constraints from both sides of the conformal boundary, engineer the unique consistent object | Penrose conformal infinity; result-before-proof (Ramanujan) |
| **SMNNIP / SMMIP / VAPMIP Lagrangian** | a *derived* information-propagation Lagrangian, isometric term-for-term with the observed Standard-Model Lagrangian; α_F = 1/137 as an error check | Lagrangian mechanics; Noether; the Standard Model; [Dixon1994], [Furey2016] |
| **d\*** + its four faces | the Zero Definer — smallest natural unit in native space; d\* = Ω_ZS / ln 10 | Lambert/Euler Ω constant |
| **the engineered structure constant experiment** | Riemann vs Fermat across a horizon, two physical ceilings as boundary conditions | — |
| **Ω_ZS six-family convergence** | W(1) as *the* cross-domain equilibrium constant | W(1) itself; the six formula families are their authors' |
| **the Riemann–Fermat Horizon** | σ=½ as the balance of "what IS" and "what CANNOT BE"; ζ-zeros = FT of the Fermat lattice | Riemann; Fermat/Wiles; the functional equation |
| **GAP = Ω_ZS − d\*·ln 10 ≈ 1/(1000√2)** | the semantic / Yang–Mills mass gap; 10³ factor OPEN | Yang–Mills mass-gap problem |
| **J_red + J_blue = Σ_RB** | persistent memory = the two currents summed; a transformer has only J_red | Noether; Dirichlet series; co-occurrence graphs |
| **primes by extinction as a zero-gradient field** | the factorisation data = a complete, remainder-free, harmonic dataset = The Two Trees | the sieve; Möbius; Modularity |
| **the Two Trees as the factoring map** | Telperion/Laurelin ↔ irreducible/composite ↔ what-cannot-be / what-is, exact partition of ℕ | names: J.R.R. Tolkien |
| **the Wankel / Ahura Mazda speaking architecture** | speak() as the rotary cycle; sedenion produced at the coupling event | Wankel; Bell; Searle |
| **the HyperWebster address system** | the word IS the address; O(\|word\|), no lookup | Horner; Borges; de Bruijn; π(p) |
| **L_(I\|O) hyper-applications** | L_(I\|O) as Thought / the action integral / the GR boundary template — *not the operator itself* | conformal / circle inversion (Möbius) |
| **Factoral Decompositional Analysis** | generational lineage = order of operations; the fulcrum/pivot/anchor identity; inertia at the anchor | RSA; prime factorisation; de Marrais |
| **Flattening Syndrome** | the artefacts of viewing a helix through a flat circle | map-projection literature (Gauss, Tissot) |
| **the Pencil HyperString** | one scalar + wind speed reconstructs a box kite | de Marrais; rigidity theory; moment map; elastica |

---

## C. Naming provenance (not mathematics — kept honest)

- **J.R.R. Tolkien** — *Ainulindalë* (the Music of Creation), the Two Trees of
  Valinor (Telperion, Laurelin), the Mingling of the Lights, Lúthien / Angband,
  "not all those who wander are lost". wiki/47 is explicit: *"Tolkien was not
  used as a model. He was recognised as a colleague."* The *Silmarillion*
  (1977), ed. Christopher Tolkien; *The Fellowship of the Ring* (1954).
- **Claudius Ptolemy** — the engine's face ("Ptolemy speaks because he knows");
  the *Almagest*, the geocentric model as a working predictive instrument.
- **Ahura Mazda / Zarathustra (Zoroaster)** — the dual-current rotary monad
  (`rotary_monad.py` / "Ahura Mazda"); the Gathas; the two spirits.
- **Philadelphos** — Ptolemy II Philadelphus; the Septuagint principle (the
  70/72 translators) for the semantic word engine.
- **Walt Whitman** — "O Captain! My Captain!" (1865); the METHODOLOGY.md byline.
- **Infocom / *Zork I* (1980)** — "West of House"; the parser question that
  opens both papers.
- **Louise Bourgeois? no — Jorge Luis Borges** — *The Library of Babel*. Fix the
  "Louise Borges" typo in VAPMIP_Paper §2.

---

## D. Retrieval

The download checklist — arXiv IDs, DOIs, stable URLs, open-access status, and
the local filename to save each as — is
[`references/CITATION_DOWNLOADS.md`](../references/CITATION_DOWNLOADS.md).
Cody fetches these; a bundled `references/papers.zip` is optional and additive.

---

## See also

- [43_emmy_noether_sedenion.md](43_emmy_noether_sedenion.md) — the naming decision
- [99_emmy_noether.md](99_emmy_noether.md) — the mathematics used
- [100_division_algebras_and_physics.md](100_division_algebras_and_physics.md) — Dixon, Furey, Baez
- [101_the_cayley_dickson_literature.md](101_the_cayley_dickson_literature.md)
- [102_berry_keating_hilbert_polya.md](102_berry_keating_hilbert_polya.md)
- [103_riemann_and_the_prime_number_theorem.md](103_riemann_and_the_prime_number_theorem.md)
- [104_fermat_wiles_and_the_corollary_they_missed.md](104_fermat_wiles_and_the_corollary_they_missed.md)
- [105_the_millennium_problems_in_ainulindale.md](105_the_millennium_problems_in_ainulindale.md)
- [106_the_navier_stokes_problem.md](106_the_navier_stokes_problem.md)
- `~/.clauderc_user_provenance` — the originated-here ledger
- `PROVENANCE.md` — the development narrative
- `METHODOLOGY.md` — Boundary Constraint Engineering
