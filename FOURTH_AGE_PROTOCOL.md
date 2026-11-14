# The Fourth Age Protocol (DRAFT, 2026-11-14)

**Status.** A first draft assembled from rules the author has already stated and that are recorded in `README.md` §1, in the standing-feedback memory and in `FourthAgePapers/README.md` and `TODO.md`. It is written so that a model starting cold does not need the rules re-typed. **Section 4 lists what could not be sourced; those items are the author's to supply or correct.** Where this draft and the author's statement differ, the author's statement wins.

Scope: every paper, engine and notebook in `FourthAgePapers/`, and by extension any new paper from the Ainulindalë family. `FourthAgePapers` is a sub-project of Ainulindalë; the Ainulindalë wiki ([133](../Ainulindale/wiki/133_canonical_maths.md) notation, [135](../Ainulindale/wiki/135_engine_findings_ledger.md) ledger) is the authoritative reference for the maths.

## 1. The two prime directives (README §1; these override defaults)

1. **No renormalization, no fitted parameters. Ever.** No fudge factors, no free constants tuned to a target, no curve-fitting to force agreement; a result falls out of the mathematics as written or it does not. If a result disagrees with theory or data, report the disagreement; do not close the gap. A needed constant is derived or cited, never chosen because it makes the output look right. If you cannot say where a number came from, you fitted it. (Rank: highest. A scoped, one-time exception can only be granted by the author, and was once, as a build-tool toward a derivation and not a conclusion.)
2. **All failures stay in the code and the data.** Do not delete, silence or tidy a failing test, broken branch, NaN, divergence or anomalous result; no `try/except` that hides a failure; no negative result quietly dropped from a report. Record the failure **and its diagnosis** ("tried X, didn't work" is nearly worthless; the mechanism stops it being retried). Fix a failure only when asked to fix that specific one. In a white paper: "Failure Stays In The Code": a failure is a runnable, asserting notebook cell or a transcript, not apology prose.

## 2. The paper rule

**One Paper. One Claim. One Prediction (Ptolemy/0_RB). One Engine. One set of notebooks. One wiki page (written last).** (Prediction pillar added 2026-09-25.) The engine derives and tests the claim; the notebooks record the derivation; the wiki page is written last. Engines are designed inside ValaQuenta first and copied to their home; ValaQuenta keeps a canonical copy.

Exceptions the author has named: an **analysis result** or a **code paper** carries no claim and no prediction and says so in its first lines (examples: `CollatzShift`, `AdditionMatrixOrbits`); a **notepad** (`Crawford_NavierStokes`) is not a paper; a **software-engineering paper** independent of Ainulindalë (`MindsEyePapersHands`) uses none of the Ainulindalë maths.

### Lifecycle (order of work)
1. Registration: README with scope, claim, prediction, status line (STUB / DRAFT / RUN / DONE). A stub says what is missing.
2. Predictions are committed in `01_predictions` **before** any data is examined.
3. Engine, then notebooks run with outputs (a notebook with no executed cell is a skeleton, not a result).
4. Supporting documentation first (wiki, notebooks, citations); **the paper last**; nothing is pushed as "finished" before the paper is.
5. A white paper on a mechanism is cold and code-only, no narrative; provenance is citation tags only (see §3).

### Statuses and labels
- Academic: `ESTABLISHED`, `MEASURED`, `DERIVED`, `THEORETICAL`, `CONJECTURE`, `OPEN`. Keeping `OPEN` / `THEORETICAL` / `CONJECTURE` is deliberate: it is the TODO list and the "asking for review" posture.
- CS: `CALCULATED` is a **suffix** on any result the paper's own code produces (`THEORETICAL:CALCULATED`, `OPEN:CALCULATED`): calculated, not derived. Do not drop an academic label because code exists.
- Citations: no tag = built against on purpose; `Post-Hoc:` = a correspondence noticed after the code worked.

## 3. Writing rules (cs-paper-code-conventions §7–§9)

- The **assistant note comes first**: the model's name and id, that a transformer wrote the paper with the skill running (link to the skill in ContextPlease), who the author is and is not, his method of not telling the model the result he wants, what kind of paper it is.
- Code is shown as listings that run cold (a short `OURS` mechanism), named and pointed at (a long or established one), boxed pseudocode marked `THEORETICAL` (unbuilt), or a literal `>` transcript (a console session). No Σ/Π block describing a loop.
- Every number is arithmetic (a listing prints it) or measured (a transcript, with the script path). A claim the code could not reproduce is not reported as a result.
- Introduction = the problem and the intended way around it (250–600 words), no results table, no history. The abstract states the problem engineered against.
- A paper that uses GenerationalLineage describes the engine in its own section **before** its results and says engine and paper share an author and an assistant.
- Ends with an appendix: what in ContextPlease was used, and what ContextPlease is.
- Generated from the engines (`make_paper.py` with a `--check` mode) where the paper is a code paper.
- Maths in Unicode glyphs, never LaTeX.
- Do not draft a paper the author has not discussed; take his content section by section; check git and the code before asking anything the repositories answer.

## 4. Working rules that apply while doing the work

- **Modify, do not rewrite**: start from the latest file and change it in place; archive stale build artefacts only.
- **Never rewrite history**: no amend, rebase, filter-repo or force-push; no force-adding ignored files. Failed results and their corrections both stay.
- **Chase every anomaly** (rank just below no-renormalization): an anomalous-but-legal result is investigated to a verdict (wrong maths, wrong framing, a bad reducer, or maths not yet accounted for), not noted and skipped.
- **Forward-propagating maths**: maths added to the project must propagate forward; no design that needs backward reconstruction or search.
- **Guarantees, not probabilities**: prefer exact and exhaustive over sampled; explicit failure over a confident wrong answer; a PACE fallback where no guarantee exists.
- **Testing refines the design question** in front of it; it is not licence to refactor.
- **Correct the maths, do not grade the ambition**: the Clay modules exist to probe the reach of ∅_RB, not to win prizes; never imply ∅_RB solves or subsumes an established open programme (Langlands, GUT).
- **Tell the author when he is wrong**; he uses it as an input to his own improvement loop.
- **Branches** (author, 2026-11-14): current work or machinery that is **large, or in progress,** may have its own branch, to keep the kinds of code separate (code purity is the purpose); small result scripts stay on `main`; no `main` merge of a branch without asking.
- **Overlapping papers are not merged**; each pair gets a line in both READMEs saying how they differ.
- **Noether-framed papers stay as written** (that is where the maths started); the retired-premise note goes beside the claim.
- **Outbound requests** carry a Mozilla user agent; public works only; a login or paywall is a stop. Downloads of another person's work follow the Literature Download Protocol. One cross and one telescope download at a time.
- **Credentials**: only the GitHub token; never the Monad's seed token.
- **Notation**: write the subscripted form of any letter that collides (α_fs, A_fermat, α_NN; σ_ζ, σ-strata, σ_RB; Ω_ζΣ, ω_H; d* and its four faces). `Ĥ_RB` is the maths name; `0_RB` / `∅_RB` is VAPMIP / Monad notation.
- **Verification trust**: read the code and run it; do not trust a recorded number that has not been reproduced (several records in the repositories did not reproduce; they are kept and marked).

## 5. Use cases, so they need not be re-typed

| Situation | Do |
|---|---|
| A test fails or a notebook errors | keep it; record the failure and the diagnosis; do not fix unless asked |
| A result disagrees with theory or data | report the disagreement; do not tune a constant |
| A result is better than expected | chase it as an anomaly before trusting it |
| A number appears in a draft with no script behind it | find the script or mark the number `OPEN`; do not report it |
| An old claim is corrected | add a dated note beside it; keep the original |
| A paper is a stub | the README says what is missing; do not write the paper |
| Two stubs share an idea | say so in both READMEs; ask before merging them |
| Noether current / balance wording is met | the premise is retired (s ↔ 1 − s is a discrete involution); use the J_red + J_blue = J_green balance language and ledger X-4 |

## 6. Recorded 2026-11-14, and what is still not sourced

- `CryptoVulnerability`: a CVE application went to MITRE (legacy web interface) many months ago; MITRE asked that a public-facing link exist and that the vulnerability not be shared before a CVE is assigned; waiting on MITRE. Not shared until then.
- Huchra's Lens was removed from FourthAgePapers (the target did not meet the BulletCluster requirements).

Still to be supplied or corrected by the author:

- The full list of prime directives and protocols beyond the two stated in `README.md` §1 and the standing feedback above (the author notes that more were defined than were shared with Gemini).
- What "done" means for a paper with a prediction that has not been run (kept open, or reported as untested).
