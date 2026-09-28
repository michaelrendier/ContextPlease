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
