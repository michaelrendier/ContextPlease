---
name: clean-house
description: Cody's Housekeeping / Clean House Protocol. A repeatable pass over one repository (ValaQuenta: per engine; FourthAgePapers: per paper) that updates the maths, code, docs and environments, RERUNS AND RETESTS EVERYTHING, removes staleness, weeds out claude.ai-era errors with a visible label, propagates to every repository that uses the code, adds visuals (discussed with him first) and a next version or rough draft of the paper. Load before any housekeeping, "clean house", staleness, propagation, venv, or peer-review-readiness work on a repository.
---

# Clean House (Housekeeping) Protocol

Written 2026-11-26 from the author's brief and from the first passes (ValaQuenta engines 0-3). Peers: the Full Engine Protocol, the ContextPlease Protocol, the FourthAgePaper Protocol. Narrative and lineage: `ContextPlease/claude/hist_wiki/skills/clean-house.md`.

## 0. Purpose and the standard it serves
* **Goal:** every repository ready for peer review, *ish*: **Computer Science compliant, not mathematically compliant.** The code is the maths and it confirms itself; the repository must be runnable, tested, documented, current, authoritative and installable on a laptop with no internet and no GPU. The author is not asking for confirmation of the maths; he wants to know the **fixed-point space / full shape of the kinds of mathematical exploration and the naming conventions** (step 6).
* **A claim without an engine or machinery is a to-do.** Every claim in a README, wiki page, paper or notebook ties to code that produces it, a test that checks it, and a current authoritative reference; otherwise it gets machinery, or a visible label, at some point in the pass.
* **ValaQuenta is the code root.** A change there propagates to every repository that uses the code (`tools/propagate.py`, plus a sweep by name and by claim). Its engineering paper is the foundational root of every piece of Python: one main section per engine.
* **Python conventions are python.org's** (PEP 8, PEP 257, the Python docs) as the parent conventions. Pure Python first: it shows the mechanics; faster twins (tensorflow, gmpy2) are speed versions of the same thing and stay, tested against the pure ones.

## 1. Standing rules the pass runs under
1. **Unit of a pass.** One repository, except **ValaQuenta (one engine at a time)** and **FourthAgePapers (one paper at a time)**. It will shortly include the ArdaQuenta visualizers. BulletCluster keeps its own venv (telescope pins). Witch's Hat (`DM_GalacticCavity`) has one venv covering its child papers, and its code belongs on the `witches-hat` branch (open: moving the children there).
2. **Permission.** Updates (maths, code, docs, environments, propagation, staleness fixes, tests, ledgers, commits and pushes of those) run **without asking**. **Ask first** for: visuals (propose, discuss, then build), anything that deletes information (withdraw and label instead), the rough-draft paper (after the visuals discussion), a decision outside the scope of the current work, an anomaly whose resolution changes the framing.
3. **Chase every anomaly to its source, no matter what** (the Standing Protocol, below only *No Renormalization*). No fitting, no renormalization: what is discarded (infinitesimals, residuals, "noise") is where the information is. Report the verdict, including "this is the bound". A legal-but-unexpected result is a data point, never a "negative result".
4. **Failed results stay** in code and docs as recorded retractions (the ledger: `Ainulindale/wiki/135_engine_findings_ledger.md`). Nothing is reverted to an older name; nothing is silently deleted.
5. **Hedging.** Mathematical and academic hedging is for `RiemannHypothesisProof` (there it is a to-do, not a courtesy to anyone). Everywhere else hedging exists only to carry the CS suffix `:CALCULATED` (appended to ESTABLISHED / OURS / THEORETICAL / OPEN for a result this repository's own code produced). Plain statements: "measured", the number, the script.
6. **Maths notation in Unicode, never LaTeX; no bare sigma** (every sigma carries its name); symbols per `@RCCM_SYMBOLS`; d* shows all four faces (`engine.constants.dstar_comment_block()`).
7. **The system Python is broken.** Never use it. Everything runs in a `.venv` (step 1 of the pass).
8. **You are the research assistant who watches from the inside.** At the end of a pass, **suggest pathways forward**: what the structure points to, what to test next, what to build. You may stop to clarify, report an anomaly, or ask for a decision.

## 2. The pass, step by step
**Step 0. Freeze.** `git status`, branch, last commit, the test baseline (full suite, which tests already fail and why), CI status (`gh run list`). Nothing starts dirty without a note. Push ContextPlease first if it holds work.

**Step 1. Environments** (`ValaQuenta/tools/repo_venv.py`, `tools/vq_venv_sync.py`).
* `ValaQuenta/.venv` is the **root**: it receives every pip/python package any code in `github.com/michaelrendier/` needs, automatically (`vq_venv_sync.py --packages ...`; never uninstall, never silently downgrade; a version conflict is surfaced). An addition to the root triggers `repo_venv.py --refresh --all`, so downstream environments catch up (and `--refresh REPO` on use).
* Every other repository (every paper in FourthAgePapers) gets its own `.venv` **at once if missing**, holding only what that repository needs: `python3 tools/repo_venv.py REPO --apply`. Existing `.venv`: add the code (`pip install -e ../ValaQuenta`).
* Every `.venv` has `requirements.txt` (pip3) and `INSTALL.md` (Linux/macOS and Windows commands). **INSTALL.md also lists every non-Python program** the repository's files call (Blender, ImageMagick, rsvg-convert, Firefox, espeak, a C compiler, TeX, ...), with whether it is installed and the apt line; the tool writes this block from a scan of the source.
* Pip-package readiness: ValaQuenta, GenerationalLineage and SedenionSpectralRelativity must be installable as pip packages (`pyproject.toml`, package list matches the tree, `pip install .` works in a clean venv). CI must be green.

**Step 2. Census.** Files, languages, entry points, which engines the repository imports (`grep` for `ValaQuenta`), which repositories import it, the **staleness catalog**, and the **claim census**: every claim in README / wiki / papers / notebooks with its machinery (code, test, reference) or "none".

**Step 3. Update the maths.** Bring in the canonical maths (`~/.clauderc_canonical_maths`) by **re-measuring**, not copying; update constants and names; check units. Anomalies: chase (rule 3). Record in the engine's wiki page and the ledger.

**Step 4. Update the code.** Single source for constants; PEP 8 / 257; docstrings with field lists; names as the code names them; tests for every new function; manifest and registry current; `:CALCULATED` labels. Where code is called twice it becomes its own tool.

**Step 5. RERUN AND RETEST EVERYTHING.** (The author's addition: "updated or not".)
* Run every test, every script, every notebook (re-executed clean), every doctest and listing, every gallery self-check, every number quoted in a document. Regenerate every generated file (toolbox, API pages, flow charts, paper with `--check`).
* For each claim in the census record one outcome: **HOLDS** (reproduced), **HOLDS-WITH-CHANGE** (reproduced, wording or number corrected), **FAILS** (does not reproduce: withdrawn and kept as a retraction), **UNRUNNABLE** (cannot run here: why, and what would make it run), **NO-MACHINERY** (a claim with no engine: to-do, labelled). Write them in the repository's `CLEAN_HOUSE_LEDGER.md` (one line per claim: where, outcome, evidence path, date).
* A complete rerun is the method by which mistaken wordings are found; a claim that survives a rerun against current references is authoritative.

**Step 6. Weed the claude.ai era.** Text from before Claude Code (claude.ai web sessions) left errors and confident but unverified claims in the repositories. Find them by: the dated records (`ContextPlease/claude/hist_prime/PTOLEMY_DOCS`, 89 design notes packaged 2026-05-04; git history; file dates), status words like DERIVED or PROVEN with no run, references that do not exist, numbers that do not reproduce. **Do not delete them: they are the historical record the author's pathway shares space with.** Mark each with the tag **`Oops:`** (same family as `Post-Hoc:`): `Oops: claude.ai era, <what was wrong>, rerun <date>: <verdict>`. A reproduced old claim keeps its wording and loses the suspicion. The claude.ai era ends where `PTOLEMY_DOCS` was made: the author moved to Claude Code then (the design record is dated 2026-05-04), so material from before that move is the era; the author left the label to the assistant (`Oops:`, "oops, bad model").

**Step 7. Naming conventions and the shape of the explorations.** Per pass, update: the symbol/name disambiguation notepad (`ValaQuenta/wiki/DISAMBIGUATION_NOTES.md`), and a one-paragraph classification of each engine by the kind of mathematics and space it explores (fixed points, spectra, algebra, geometry, information) so the whole shape stays visible.

**Step 8. Docs.** README as code reference (API style, python.org conventions); wiki split into API (ValaQuenta) and narrative (Ainulindale wiki); toolbox page regenerated and the index repass (Full Engine Protocol part 6); manifest provenance; notebooks; citation pass (once per conversation); licences (`~/.clauderc_licenses`); a README ContextPlease section.

**Step 9. Propagate.** `tools/propagate.py ENGINE [--apply]`; then a sweep by name and by claim over every repository (`grep -rIlE`); correct downstream docs and code; each downstream repository follows steps 1 and 8 for what it touched; append to `PROPAGATION_LEDGER.md`. Archives and `Tuning-the-Engine` are not edited: their correction is a ledger row.

**Step 10. Context files.** `.clauderc*` blocks, `ContextPlease` (archive, mirror, push first), memory.

**Step 11. Visuals: discuss first.** Propose the list (what each shows, what it does not), the author chooses, then build. Kinds: interactive pages (raw Canvas 2D or WebGL, no libraries, no network, `html-spatial-awareness` rules), each with an **About panel** (what, how to read, what it shows, what it does not, numbers to check), its GitHub sources and literature, and a **self-check of its JavaScript against the Python engine on load**; image galleries (`ContextPlease/claude/galleries`); code flow charts (`tools/flowchart.py`, ISO 5807, final only after updates, tests, visuals and docs are done); transcripts. Register in the central index (`build_index.py`, `michaelrendier.github.io`); the published site must include them (CI). Show the code, its flow, and its operation in action: several ways.

**Step 12. Paper.** After the visuals discussion: the next version, or a rough draft if none exists (`cs-paper-code-conventions`; assistant note first; labels; ContextPlease appendix). ValaQuenta paper: each engine is its own main section (engine 0 = section 3). FourthAgePapers: the paper's own. Generated from the code with a `--check` mode.

**Step 13. Verify and close.** Full tests; CI green; clean-clone install from INSTALL.md alone; links; then commit and push every repository touched (never rewrite history; GITHUB_TOKEN only), changelog, ledgers, memory, and a short report: what changed, what was withdrawn, anomalies and their verdicts, decisions needed, **suggested pathways**.

## 3. Open items (as of 2026-11-26)
CI (`modules/basile` named in `pyproject.toml` but gitignored); the text-only Midline address (`FourthAgePapers/HyperindexingSystem/TODO.md`, not to be built until the author says go); the 4 pre-existing failing tests (docstrings, registry); ArdaQuenta visualizers. Settled 2026-11-27: the claude.ai era ends at the move to Claude Code (PTOLEMY_DOCS); the Witch's Hat family is on the `witches-hat` branch with one `.venv`.
