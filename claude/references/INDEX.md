# Literature Download Protocol: the ledger
**Protocol (Cody, 2026-10-14).** Whenever another person's work is downloaded: (1) add the citation and the file here and to `~/.clauderc_citations` (by repo); (2) keep the file under `ContextPlease/claude/references/<paper-or-repo>/`; (3) mirror it in the appropriate spot of the repo or paper that cites it (for a paper: a `references/` directory beside it); (4) verify the file by reading its own title page before recording it; (5) list cited works that could not be downloaded, with the reason, so they can be fetched by hand. Anything cited or downloaded should be available.

| citation | paper / repo | local copy (ContextPlease) | mirrored beside the paper | retrieved | status |
|---|---|---|---|---|---|
| Bernstein & Lagarias (1996), The 3x+1 conjugacy map, Canad. J. Math. 48, 1154-1169 | CollatzShift | `references/CollatzShift/Bernstein_Lagarias_1996_retypeset.pdf` (+ Umich preprint) | `FourthAgePapers/CollatzShift/references/` | 2026-10-14 | downloaded, verified |
| Lagarias, The 3x+1 problem: an annotated bibliography (1963-1999), arXiv:math/0309224v13 | CollatzShift | `references/CollatzShift/Lagarias_annotated_bibliography_arXiv_math0309224.pdf` | `FourthAgePapers/CollatzShift/references/` | 2026-10-14 | downloaded, verified |
| Bernstein (1994), A non-iterative 2-adic statement of the 3N+1 conjecture, Proc. AMS 121, 405-408 | CollatzShift | none | none | - | NOT downloaded (publisher HTTP 403); fetch by hand |
| Terras (1976), A stopping time problem on the positive integers, Acta Arith. 30, 241-252 | CollatzShift | none | none | - | NOT downloaded (no free PDF found); fetch by hand |
| Lagarias (1985), The 3x+1 problem and its generalizations, Amer. Math. Monthly 92, 3-23 | CollatzShift | none | none | - | NOT downloaded (JSTOR) |
| Everett (1977), Iteration of the number theoretic function f(2n)=n, f(2n+1)=3n+2, Adv. Math. 25, 42-45 | CollatzShift | none | none | - | NOT downloaded |
| Letherman, Schleicher, Wood (1999), The (3n+1)-problem and holomorphic dynamics, Experiment. Math. 8 | CollatzShift | none | none | - | NOT downloaded (Project Euclid landing page) |

Earlier downloads recorded elsewhere: `Ainulindale/references/` (permutation papers, cs_hashing_overhead, `CITATION_DOWNLOADS.md`). They predate this ledger and have not been re-indexed here.
