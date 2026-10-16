# CONTEXT PRIMER — the VAPMIP paper, rebuilt around ptol.c and its Python twin (2026-10-15)

**State: text generated, uncommitted, unpushed, not yet shown. NO engine development until the paper is written and shown (Cody).**

## Cody's directives (this session)
- The paper gets the current working Monad `PtolC/ptol.c` and its matching Python monad, which Cody CONFIRMED is **`scaled_mind_eye_boxkite_kernel_monad.py`** (not `ptolemy_monad.py`, my earlier assumption; that one is used inside the scaled monad's adapter for sentence context).
- Skip Ainulindale and the Hyperindexing system; VAPMIP's English-teaching work stands on its own. Skip the narrative (it goes back into Ainulindale).
- Engineered-operators protocol, with these names: 0_RB = **Fixed Point / Fixed Question**; L_(I|O) = **Inside Out**; UFT = **Discrete Words Along Continuous Ideas**. No theory names in the paper.
- Licence: the Monad and "Teaching the Maths English" are Cody's; the harness and everything else is GPL v3. So mechanism (E/F/D) for the Monad; verbatim (B) only for GPL parts. Which files count as "the Monad" is my reading; LICENSE/NOTICE NOT edited.

## UPDATE (later 2026-10-15)
Outline and abstract are to be discussed section by section BEFORE anything on the paper is committed; machinery only, ArXiv convention; the language of FIELDS (words, context, semantics, phonetics) is used to avoid pointing at a unified field theory. His claim under discussion: 0_RB IS the boxkite. Repo-checked: e₀ is in no kite (bk.e0_is_outside); seven kites are disconnected octahedra sharing only the hub e₀/e₈; gluing beyond the hub is CONJECTURE; his 2026-08-03 note says 0_RB is "the water, not the machine". New finding: red/blue split differs (ptol.c cos/sin channels {0-3,8-11}/{4-7,12-15}; the kernel and rotary_rerun red = k≥8), so σ_self is not one shared quantity. Notebooks committed and pushed (VAPMIP 596e4a8). The generated paper in `VAPMIP/paper/` is a measured first pass on the wrong twin and carries a SUPERSEDED banner.

## What exists
`VAPMIP/paper/`: `evidence.py` (all measurements, fresh), `template.md`, `make_paper.py` (`--check` = committed text vs fresh run, ignoring date, timing and ⟦…⟧ spans), `build_pdf.sh` (TMPDIR-aware), output `Forward_Propagation_of_Information.md` / `.pdf`. Run with `PtolemyDesktop/.venv/bin/python`. Run `ptol` only with HOME in scratch (it writes SVG/PPM to ~/.ptolemy); `ptolemy -r -n` never saves; the resident service folds into `PtolC/monad3_c.bin` by itself.
Old draft `docs/paper_drafts/Forward_Propagation_of_Information_DRAFT.md` (24-module, 12-voice survey) is untouched and superseded in scope; its PDF is at ~/Desktop/SpaceClaude/.
Scratch evidence: `ContextPlease/claude/scratchpad/2026-10-15_vapmip_paper/` (q1 surface, q2 twin+parity, q3 conservation claim, q4 eyes/monotone, q5 parser, q6 U-shape).

## Results kept as results
Python restatement of the projection = `ptol -r` to 5e-11 (16 components, 6 prompts) and = all five eyes. ptol.c header claims not reproduced: "J_red×J_blue = d* conserved at all σ" (P_r·P_b spans 0.02–0.25, ≤¼; neutron-prompt 0.24606/0.24611 near 0.2460 = chance, ~9% among 30); "σ_self→1 at σ=1, →0 at σ=0" (medians 0.41/0.15). σ_self(σ) monotone only for <10-char inputs; ≥20 chars it is U-shaped (min σ≈0.3, same for random letters). Twin replies vary with PYTHONHASHSEED for 2 of 6 prompts (set order; Phase 32); deterministic per seed. Compiled words are off-topic shadow words; the twin supplies on-topic words. Parser tables: C 197 verbs vs Python 207; 5 conflicts (break, compose, print, scan, write) from Python last-write-wins vs C first-match; C header's "mirrors exactly" is false.
Two of my own mistakes, corrected and recorded: a one-line slice that shifted the sixteen values by one (the `eye:` header is on stderr); a first-draft Euler gcd in the circle study.

## Open / for Cody
1. Is `ptolemy_monad.py` the intended "matching python monad"? 2. Which files are "the Monad" (publish mechanism only) vs GPL? Add the licence structure to NOTICE? 3. Fix or leave: hash-seed dependence, parser table disagreement, the ptol.c header comments (all untouched — no development). 4. Energy is cited from the 2026-10-13/14 run, not re-measured (needs unplugged laptop). 5. Commit/push of `VAPMIP/paper/` and `notebooks/tuning_the_engine/` (both untracked) awaits his word — Monad licence applies to the VAPMIP repo.
