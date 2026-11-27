# clean-house

**Skill:** `~/.claude/skills/clean-house/` · mirror `ContextPlease/claude/skills/clean-house/`
**Created:** 2026-11-26 · **Owner of the method:** Cody Michael Allison (Michael Rendier)

## What it is

The Housekeeping, or Clean House, Protocol: a repeatable pass over one repository that brings its maths, code, documentation and environments up to date, **reruns and retests everything**, removes staleness, labels the errors left by the claude.ai era, propagates changes to every repository that uses the code, adds visualizations (discussed with the author first) and writes the next version of a paper, or a rough draft if none exists. It joins the Full Engine Protocol, the ContextPlease Protocol and the FourthAgePaper Protocol.

## Why (the author's words, 2026-11-26)

* **Peer-review-ish, Computer Science compliant, not mathematically compliant.** "I'm not asking so much for confirmation of the maths, the code does that by itself, but I need to know about the fixed point space / full shape of mathematics types of explorations and naming conventions." The repositories are to be read by software engineers who can run the maths on a laptop without internet or GPU.
* **A claim without an engine or machinery should be fixed at some point.** A complete rerun of every piece of code and every claim, updated or not, is how mistaken wordings are found; what survives against current references is authoritative.
* **The claude.ai era.** Claims from before Claude Code (claude.ai web sessions left holes in the repositories; see `PTOLEMY_DOCS` for the dates) are not deleted: "it's still the historical record that my pathway through the dark room has shared space with." They show up as stale and are labelled (`Oops:`, "bad model") with the rerun verdict.
* **Hedging** is for RiemannHypothesisProof, where it is a to-do; elsewhere it exists only to carry `:CALCULATED`.
* **Anomalies are chased to their source, no matter what.** "It's the discarded spaces of the world I've found most of this work in": which is why there is no fitting and no renormalization. The infinitesimals that get discarded show whether an inward or outward vortex is being flattened into a divergent slice, and carry periodic wave patterns; waveforms are not 2D objects, they are resonant cavities in the radio silence.
* **Environments.** The system Python is broken; ValaQuenta's `.venv` is the root with every package; every other repository, and every paper in FourthAgePapers, gets its own `.venv` at once, with `requirements.txt` and `INSTALL.md`, and every program the code calls, Python or not, is listed there.

## Procedure

The step-by-step is the SKILL.md (steps 0 to 13: freeze, environments, census, maths, code, rerun and retest everything, weed the claude.ai era, naming conventions and the shape of the explorations, docs, propagate, context files, visuals, paper, verify and close). Unit of a pass: one repository; ValaQuenta per engine; FourthAgePapers per paper.

## First passes (measured, 2026-11-25 and 2026-11-26)

The protocol was assembled from ValaQuenta engines 0 to 3. What those passes found, as examples of what the steps catch:

| step | finding | where recorded |
|---|---|---|
| maths | d* carried in three inconsistent forms in about 120 files; one source and the four faces now | `RESTRUCTURE_CHANGELOG.md`, `PROPAGATION_LEDGER.md` |
| rerun | the `constants` engine still said "π φ e √ i are outputs" and "Euler's identity is a theorem of this engine", which Ainulindale wiki 22 §6 had withdrawn | changelog, engine 2 |
| propagation | "70 % baseline" for the gap primes was an observed rate, not chance; the sweep also found two stale copies of a retracted lemma in TuringStack and FourthAgePapers | ledger X-60, X-61 |
| anomaly chase | the two-digit excess of nilpotent primes led to the closed form of the square law (weight parity, a ring homomorphism, Thue-Morse) and to a look-elsewhere P = 0.0016 | ledger X-63, wiki 78 §7 |
| visuals | a gallery page's self-check against the Python engine caught a data-file fault on its first run | engine 3, paper §6.5 |
| environments | four repositories had no `.venv`; the root lacked tensorflow, whisper, pyrtlsdr, gmpy2 | `tools/repo_venv.py`, ledger |

## Files

`tools/repo_venv.py` (environments, system software block, refresh), `tools/vq_venv_sync.py` (root first, downstream refresh), `tools/propagate.py`, `tools/dstar_block.py`, `tools/gen_toolbox.py`, `tools/flowchart.py` and `tools/flowlib.py`, `paper/make_paper.py`, `RESTRUCTURE_CHANGELOG.md`, `PROPAGATION_LEDGER.md`, per-repository `CLEAN_HOUSE_LEDGER.md` (to come).

## Open items

The cutoff date of the claude.ai era and the `Oops:` label (the author may choose another); Witch's Hat children onto the `witches-hat` branch; CI (a package named in `pyproject.toml` but gitignored); Midline without digits; the Sanderson compression video link; four failing registry and docstring tests; the ArdaQuenta visualizers.

## Licence

GPL-3.0-only, with the rest of the author's code and maths.
