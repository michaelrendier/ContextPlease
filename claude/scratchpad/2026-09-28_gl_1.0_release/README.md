# GenerationalLineage 1.0.0 — release log (2026-09-28)

Tag `v1.0.0` → 5885e7f · release https://github.com/michaelrendier/GenerationalLineage/releases/tag/v1.0.0 · follow-up 8639b07.
Licence GNU GPL v3.0 (`GPL-3.0-only`, SPDX on every source file). Skill used: `cs-paper-code-conventions` (Cody said
"cs-paper-structure*"; no skill of that name exists — the code-conventions one was applied: Convention A for the whole repo,
D for the tutorials (generated REPL transcripts), B nowhere new, C's checklist slot = wiki/Reproducibility.md).

## Bugs the clean-clone method found (all fixed before/after release)
1. On a plain clone `verify_all()` FAILED: `oscilloscope` imports `telperion_engine` from a sibling repo. → Core/Extended split,
   `requires: sibling-repos`, skipped-not-passed reporting (`_ok/_complete/_skipped`), `python3 -m engine`.
2. `from tools import transcript` was shadowed by ValaQuenta/h_rb_hat/tools.py, because `engine.maths` puts sibling dirs at the FRONT
   of sys.path. → developer scripts live in `devtools/`. (Recorded as Known limitation 2.)
3. `devtools/transcript.py --check-all` reported the Extended-only tutorial stale on Core (would have failed CI's Core job).
4. (After release) 10 of 21 README Python blocks were fragments using names defined only in prose; 1 called a function without args;
   1 showed an uncaught AscentNotFree. → fixed + `test_every_python_block_in_the_readme_runs`.
Also: `lines.descend` now forwards extra positional args (stencil/hyper_linear); `stencil` registered; `from engine import *` filtered;
`un_sieve` exported.

## Measured (fresh venvs, from GitHub clones)
Core: `27 ran / 27 passed / 1 skipped`; tests `151 passed, 2 skipped` (150/2 at the tag). Extended (4 sibling repos beside): `28/28/0`;
`153 passed` (152 at the tag). numpy 2.4.6 (local) and 2.5.3 (fresh pip). All 40 Core transcripts regenerate byte-identically.

## Not done / needs Cody
- CI workflow NOT enabled: token has `repo` scope only; GitHub refuses workflow files without `workflow` scope. Definition shipped as
  `.github/ci-workflow.yml` + `.github/README.md`. Not run on GitHub yet.
- AUTHORS credits Claude as a coding assistant (strike if unwanted). SPDX is `GPL-3.0-only` (or-later is a one-line change).
- References.md was compiled from the standard bibliographic record (not fetched); it says so.
- README §§0–4.18 prose not audited line-by-line beyond counts and the code blocks; ValaQuenta/wiki/generational_lineage_map.md and
  other sibling-repo docs still cite the old FactoralDecomposition paths.
- Other repos' licences (TuringStack MIT; ValaQuenta/Ainulindale/PtolemyDesktop none) untouched.

## Follow-up: README older-prose consistency pass (d94ab90, same day)
Line-by-line audit of README §§0–8 + appendices against the live engine. Found & fixed: §5 listed 40/44 relations (PW13–16 missing; all
listed names were correct); `fermat_path(3233)` documented excursion 8 (actual 0); `pathway_residues(mult=1)` "often fails" on an example
where it succeeds (now N=1451951 → multiplier 3, step 86); `decompose()` output missing `root`; pasted `report_emergence` had old field
names; §4.6 "IoC not built here yet" (cipher builds it); Status enum members are HOLDS/FALSE/UNJUDGED (values print MATHS-FAULT/CODE-FAULT);
GenerationalLineageEngine (base, R-series) vs FactoralLineageEngine (subclass, runs all); session-speak; sibling-repo / private-dotfile
pointers unresolvable to outsiders; §4.8 out of order. NEW: tutorials 17 (pathway/tuning) and 18 (factoral spiral) → 43 tutorials.
GENERATED now (build_docs): §5 tables (from run_lineage log; ids R/F/G/FR/PW map exactly onto the prose's R5, F3, G5, PW11–PW16),
Emerger report, Appendix A (Clay), tutorial-index count. NEW TESTS: every README anchor + every relative link in README/wiki resolves.
Measured (clean envs): Core 156 passed/2 skipped; Extended 158 passed. `build_docs --check` also passes on Core.
Gotchas: `python3 engine/oscilloscope.py N` writes factorial_oscilloscope.svg into the REPO ROOT regardless of cwd (overwrote the tracked
file during my check; restored via git checkout) — documented in §4.8, not changed. Calibration report figures verified (46/22/6/18, 0.957).
FOR CODY: G5's claim string and README §7 mention "SHA-1 IVs are a null subalgebra" / the UDEO white paper's retracted lemma — already
public, but your memory says SHA-1-specific UDEO detail is your call under the CVE embargo; I did not alter it.

## Follow-up 2: UDEO decoupling + drop TuringStack (1512bc0)
Cody corrections: (1) IV-nilpotency finding was NOT in service of UDEO -- it tested GL's own trace-Laplacian machinery, SHA-1 IVs
were one real-world check case. (2) No formal embargo; informal ask = don't share until CVE assigned; eval still pending (after
boxkite paper). (3) repo-root SVG write is fine, expected behaviour on the clone owner's own machine. (4) REJECTED my first phrasing
"not work done for or as part of any other project" -- forensic-psychology point: denying involvement ("nothing to see here") reads
as volunteering information and prompts forensic analysts into forward motion. Corrected wording everywhere to "work touching other
projects not scoped here" (his exact suggested phrase, applied to all 4 instances: README §7, wiki session-origin, wiki G5 section,
NEWS.md).
Code fix: engine/maths.py dropped `from udeo_poc import CayleyDickson` (TuringStack) -- replaced with GL's own `engine.lineage.
cd_mul_gf2`, checked BIT-IDENTICAL at dim 8..2048 and up to 8x faster. TuringStack is no longer a required sibling: Extended layer
is now 3 repos (AbrikosovTree, ValaQuenta, FourthAgePapers), not 4. Updated everywhere: INSTALL.md, README.md (generated install
block regenerates from INSTALL.md automatically), NEWS.md, CONTRIBUTING.md, wiki/Reproducibility.md, .github/ci-workflow.yml,
engine/__init__.py comment, examples/90_extended_fermat_facet.py + transcript.
Verified TWICE: (a) local real siblings, 28/28 0 skipped, 158 passed; (b) completely fresh `git clone` from GitHub of GL +
AbrikosovTree + ValaQuenta + FourthAgePapers only (no TuringStack anywhere on disk) -- same result, transcripts/docs not stale.
Also note: an earlier bash attempt (`rm -rf` on a SCRATCHPAD clone of TuringStack, not the real repo) was rejected by the user mid-
turn; abandoned that approach and used a wholly fresh clone instead, which is cleaner anyway.
