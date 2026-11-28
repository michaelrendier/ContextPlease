# 134 — The Library (the reading list behind the convergence claims)

| | |
|---|---|
| Location | `/home/rendier/Documents/books/jeremy/` on the author's workstation (113 files, 356 MB). **Not part of any repository.** The directory name is that of the person who assembled the reading list; he is named only in the citation of that work (row L1 in §1) |
| Repository copies | the two open-access arXiv papers only: `Ainulindale/references/library_convergence/` (sha256 matches the library files). Everything else is cited by path and hash, because of licence terms and size |
| Cited from | `FourthAgePapers/addenda/addendum_VII_library_convergence.md`; [98](98_provenance_and_citations.md) §A.12; the First-Age documents in `Ainulindale/AgeFirst/` |
| Last verified | 2026-11-13: every non-article file's title page read (text layer or OCR); the 65 articles' titles read; SHA-256 recorded for the books |

## 1. What the library is

A working library of the sources that the framework's "convergence"
argument points at: the exceptional-structure side (E8, the Leech lattice,
birdtracks, generating functions) and a body of articles in which another
discipline (sacred geometry, music, the I Ching, the genetic code) is read as
a description of the same eight-fold object. The convergence argument is
Addendum VII: several programmes, each approaching E8/octonion structure from
its own field, and the claim that they describe one object.

Status of the argument. The mathematics in §2 is established literature. That
each programme, and the articles of §3, describe *the same object as the
framework's tower* is the framework's reading (`THEORETICAL`); it is not a
statistical result and no independence test was run (see the withdrawal of the
sigma valuation in [24](24_claude_conclusion.md)). The reading list was also
assembled by someone else who reports it overlapped the project's list; that is
provenance, not validation.

| Row | Item | Role |
|---|---|---|
| L1 | the `jeremy/` library as a whole (Broner, 2026, reading-list assembly) | the independent assembly cited in Addendum VII §7; anecdotal (Addendum's own status) |

## 2. The books and papers

All title pages were read from the files. SHA-256 is truncated to 16 hex
characters; full hashes are recomputed with `sha256sum` on the path.

| Row | File (under `MATH_BOOKS/`) | Work, as on the title page | Pages | sha256 | Held in repo? |
|---|---|---|---|---|---|
| M1 | `E8packing.pdf` | M. S. Viazovska, *The sphere packing problem in dimension 8*, arXiv:1603.04246v1 [math.NT], 14 Mar 2016 (later Ann. of Math. 185 (2017) 991–1015) | 23 | `20b663456fb359cc` | yes (`references/library_convergence/`) |
| M2 | `LEECH/Leech.pdf` | H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, *The sphere packing problem in dimension 24*, arXiv:1603.06518v1 [math.NT], 21 Mar 2016 | 12 | `b9cec6cbe4194df9` | yes |
| M3 | `LEECH/Leech1.pdf` | J. Leech, *Some sphere packings in higher space* | 26 | `5ff6cda8a210533d` | no (copyright) |
| M4 | `LEECH/Leech2.pdf` | J. Leech, *Notes on sphere packings* | 17 | `2093014cecfe8053` | no (copyright) |
| M5 | `Group Theory - P. Cvitanovic_files/GroupTheory.pdf` | P. Cvitanović, *Group Theory: Birdtracks, Lie's, and Exceptional Groups*, Princeton University Press; "version 9.0.1, April 8, 2011" | 289 | `d82807e108c52bcc` | no |
| M6 | `gfology2.pdf` | H. S. Wilf, *generatingfunctionology* (© 1990, 1994 Academic Press; Internet edition) | 231 | `aeecec4df4fbb81b` | no (licence limits reproduction to institutions of higher learning) |
| M7 | `numbertheory.pdf` | V. Shoup, *A Computational Introduction to Number Theory and Algebra*, Version 2 | 598 | — | no |
| M8 | `geometry.pdf` | K. S. Kedlaya, *Geometry Unbound*, version of 17 Jan 2006 (GFDL 1.2) | 142 | — | no |
| M9 | `semi_riemannian_geometry.pdf` | S. Sternberg, *Semi-Riemann Geometry and General Relativity*, 24 Sep 2003 (course notes) | 251 | — | no |
| M10 | `mathematical_methods-three.pdf` | J. Nearing, *Mathematical Tools for Physics*, Univ. of Miami, © 2003 | 444 | — | no |
| M11 | `mathematical-biology.pdf` | J. R. Chasnov, *Mathematical Biology*, lecture notes for MATH 4333, HKUST | 119 | — | no |
| M12 | `adv_calc.pdf` | J. M. Erdman, *A ProblemText in Advanced Calculus*, Portland State, version 1 Jul 2014 | 377 | — | no |
| M13 | `STRANG/Calculus.pdf`, `STRANG/Guide/` (8 files), `STRANG/Manual/` (8 files) | G. Strang, *Calculus* with the MIT RES.18-001 study guide and manual | 671 (text) | — | no |
| M14 | `Calculus/` (8 files) | AP Calculus and 17calculus exam and course-description files | — | — | no |

M1–M6 are the sources the framework's text actually relies on. M7–M14 are
general reference and teaching material; no wiki claim leans on them.

What each of M1–M6 is cited for, and where the framework's reading goes beyond
the source:

- **M1, M2 (Viazovska; Cohn et al.).** E8 is the densest sphere packing in
  ℝ⁸ and the Leech lattice Λ₂₄ the densest in ℝ²⁴ (proved; `ESTABLISHED`). The
  framework identifies E8 with the lattice of integral octonions, the 240 roots
  with the shortest vectors, and the optimality with a bound on the Noether
  constraint surface of the 𝕆 stratum; and chains Leech → Co₀ → Monster →
  j-function → modular forms → Wiles → Fermat lattice → Blue channel. Each
  link of that chain is the framework's reading (`THEORETICAL`); the proofs
  themselves are about sphere packing and do not mention octonions.
- **M3, M4 (Leech).** The original constructions of the lattice. Bibliographic
  details (journal, year) are not on the title pages and are **not asserted
  here**; to be confirmed against the journal before they enter [98](98_provenance_and_citations.md).
- **M5 (Cvitanović).** Birdtracks and the exceptional groups; the
  Freudenthal–Tits magic square as built from the four division algebras
  (`ESTABLISHED`). The framework reads the interaction terms of L_NN as
  generating birdtrack graphs and the (𝕆, 𝕆) entry E₈ as the full octonionic
  coupling (`THEORETICAL`). The wiki's 2008 date is the book's first edition;
  the file is version 9.0.1 (2011).
- **M6 (Wilf).** Generating functions as an algebraic language for discrete
  mathematics (`ESTABLISHED`). The framework observes that the Horner encoding
  of [09](09_hyperwebster_engine.md) is positional accumulation in the same
  sense: an analogy ("philosophical alignment", Addendum VII's own wording).

## 3. The Phillips articles (`StephenPhillips/`)

73 files: `Article01.pdf` … `Article65.pdf` (Articles 40, 47, 50 in parts; a
duplicate of 52), `ESP_of_Quarks.pdf`, and `TableOfContents.doc`. The author of
all of them is Stephen M. Phillips (Bournemouth, UK), who hosted the articles on
his own website. They are not peer-reviewed physics.

**What they are.** A single programme of numerical correspondences: the
counts that define the E8 × E8′ heterotic superstring (roots, 248, 496, 168,
336, 1680, …) are matched against counts in sacred geometries (the Tree of Life,
the Platonic solids, the Disdyakis Triacontahedron, the Sri Yantra), in music
(the seven Greek modes, Pythagorean scales), in the I Ching, in anatomy (206
bones) and in the genetic code (64 codons). They are the "interdisciplinary
views of one object" of the First-Age documents: each field's structure is read
as an encoding of the same eight-fold exceptional object.

**Status in this wiki.** `EXTERNAL`, not reviewed for correctness here, and
not adopted. A match of counts between two systems is not a derivation of
either from the other, and the files contain no derivation of the string
parameters from a field theory. They are listed because they are the stated
source of the cross-disciplinary reading and because the cited counts
(E8 has 240 roots; E8 × E8 has 480 roots and dimension 496) are
independently checkable mathematics, which the wiki uses on its own terms.

| Theme | Articles (title as printed) |
|---|---|
| Superstring and the Tree of Life | 1 (physical nature of superstring), 2 (the physical plane and its relation to the UPA/superstring), 5 (the superstring as microcosm of the spiritual macrocosm), 6 (ten-whorl structure of the superstring encoded in the 41-Tree), 7–10 (encoding of structure numbers 137, 248, 168, 251, 336, 1680 in Tree, square, dodecagon), 15 (the mathematical connection between superstrings and their micro-psi description: a pointer towards M-theory) |
| Sacred geometries, polyhedra | 3 (Platonic solids), 22–25, 27, 29, 30, 33–36, 41, 44, 48, 53–56, 58–60, 62–63 (the Disdyakis Triacontahedron, Triakis Tetrahedron, polyhedral Tree of Life, Sri Yantra, Gosset 4₂₁ polytope, 24-cells, regular polygons and the ten Sephiroth) |
| E8 and exceptional structure | 28 (roots of E8 in the Inner Tree and the Disdyakis Triacontahedron), 44 (496 roots of E8 × E8′), 45 (1680 circularly polarised oscillations as harmonics of the Pythagorean scale), 47 (parts 1–2: sacred geometries embody parameters of the heterotic superstring and the DNA codon pattern), 52 (EHYEH, YAH, YAHWEH prescribing the root structure and dimension of E8), 55 (Platonic solids embody the five exceptional Lie groups), 59 (the (3+3) enfolded polygons and E8 × E8′ root structure), 63 (the sacred geometrical nature of the 4₂₁ polytope) |
| Music | 12 (new Pythagorean aspects of music), 13 (the music of superstrings), 14 (why the ancient Greek modes are sacred), 16 (tone intervals of the seven octave species and octonion algebra), 26, 31, 37, 38 (the seven musical scales and the polyhedral Tree), 42 (eight church modes and the human skeleton), 51 (Fibonacci numbers and the Pythagorean scale) |
| I Ching and the eight-fold way | 18 ("I am One who becomes Two … Eight", Coffin of Petamon), 19 (I Ching and the eight-fold way), 20–21 (I Ching table, the 3×3×3 array of cubes, the Klein configuration), 39 (correspondence between the Inner Tree of Life, the Sri Yantra and the I Ching), 43 (the {3,7} tessellation and the 168 automorphisms of the Klein quartic) |
| Anatomy and the genetic code | 32 (bone and classical acupoint compositions), 33–34 (the human axial skeleton, the 206 bones), 41, 46 (sacred geometries encode the 64 codons of mRNA and the 64 anticodons of tRNA) |
| Number sequences | 17 (the logarithmic spiral basis of the Titius–Bode law), 50 (parts 1–2: the golden ratio, Fibonacci and Lucas numbers in sacred geometries), 51 |
| Astrology | 61 (the Tree of Life basis of an astrological era) |
| Other | 4 (Godnames prescribe the Inner Tree of Life), 11 (Plato's Lambda), 49 (how sacred geometries are equivalent maps of all levels of reality), 57, 64, 65 (titles not on their first pages) |

A theme row lists the article numbers it covers; where a number is shared
(Articles 41, 51) it is listed once under its best fit. The titles are as
printed on the articles' first pages (several files were typeset with a
doubled font that makes text extraction garble the titles; they were decoded
and read).

**ESP of Quarks (`ESP_of_Quarks.pdf`, 256 pp., image-only).** Stephen M.
Phillips, *Extra-Sensory Perception of Quarks* (The Theosophical Publishing
House, Wheaton/Madras/London, 1980; title page read by OCR). It relates the
"ultimate physical atom" described in Besant and Leadbeater's *Occult
Chemistry* to the quark model. It is the origin of the articles' programme and
is cited as a source of the correspondence idea, with the status above.

## 4. What is and is not in the repositories

| Material | Where |
|---|---|
| M1, M2 | `Ainulindale/references/library_convergence/` (open access; hash-checked) |
| M3–M14, Phillips | the library only, at the path above |
| Citation rows | `~/.clauderc_citations` (rows flipped from QUEUED to HOLDING on 2026-11-13); [98](98_provenance_and_citations.md) §A.12 |
| Works named in Addendum VII that are **not** in the library | Cosic (RRM, 1997 book), Wyler (1969), Smith, Dixon (1994), Furey (2014–2022): see §5 |

The Literature Download Protocol keeps a copy of every item in
`ContextPlease/claude/references/` with a line in its `INDEX.md`. That step is
deferred during the housekeeping pass and is listed as pending in §6.

## 5. Corrections needed in Addendum VII (`FourthAgePapers`, not edited here)

| Addendum text | Issue |
|---|---|
| §5 "The Wyler derivation is the A_π derivation … A_π = 1/137.036 is the Berry–Keating domain floor" | A_fermat is not α_fs (ruling 2026-11-13; [17](17_alpha_omega_d_star.md) §0). Wyler's 1969 expression is a numerological formula for α and is not accepted as a derivation; the Addendum's displayed formula is also garbled (Wyler's is α = (9/8π⁴)·(π⁵/(2⁴·5!))^(1/4)) |
| §8 convergence table, "Seven independent programmes" | the programmes are not tested for independence; the count is rhetorical |
| §7 "85% of core references" | an unverified figure |
| Part II "Euler's identity is a theorem of H_hat_RB" | withdrawn: [22](22_constant_facets.md) §6 |
| "Dixon's theorem" | a published proposal: [19](19_cayley_dickson_tower.md) §3 |
| Chain Leech → … → Blue channel | a reading, not a derivation (§2 above) |

## 6. Pending

- Add a line for each held item to `ContextPlease/claude/references/INDEX.md` (deferred with the ContextPlease protocol).
- Confirm the journal details of Leech 1964 and 1967 before they enter [98](98_provenance_and_citations.md).
- Obtain and title-verify Cosic, Wyler, Dixon and Furey, which Addendum VII and the First-Age documents cite but the library does not contain.
- Propagate the §5 corrections to `FourthAgePapers`.

## 7. Related pages

[19 Cayley–Dickson tower](19_cayley_dickson_tower.md) · [22 Constant facets](22_constant_facets.md) ·
[23 Resonant recognition](23_resonant_recognition.md) · [24 Archived assessment](24_claude_conclusion.md) ·
[98 Provenance and citations](98_provenance_and_citations.md) · [101 The Cayley–Dickson literature](101_the_cayley_dickson_literature.md)
