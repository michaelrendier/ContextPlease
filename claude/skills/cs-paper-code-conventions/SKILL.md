---
name: cs-paper-code-conventions
description: Standard conventions for presenting Python/code machinery inside a computer-science paper — when to show a runnable code Listing vs. when to describe an API in prose vs. when to use boxed pseudocode vs. a literal REPL transcript, how to caption/number/cite each, and the "perpetual now" rule that every Listing must read cold, without silently assuming the reader carried forward state from an earlier one. Use when writing or revising any paper in FourthAgePapers (or any other engineering-structure paper) that has running code behind a claim, whenever the draft is leaning on dense mathematical notation (Σ, ∫, custom symbols) to describe something that is actually a short function, whenever a section has more than one code Listing and you need to check none of them depends on invisible state from an earlier one, whenever the artifact is a console/REPL session rather than a function, or when the user says "show the code, not the maths" / asks how a CS paper should present code / asks to check a paper's code-block conventions.
version: 0.3.0
---

# CS Paper Code Conventions

The standing failure mode this skill corrects: writing a mechanism as a
mathematical formula (`H(w) = Σ_k ord(w_k)·95^(|w|−1−k)`) when the actual
artifact is eight lines of Python that already runs. That is leaning
mathematically on something that is not, in its native form, mathematics —
it is code. Established via direct research on real papers
(2026-09-19), not assumed.

## 0. Four real conventions, verified by reading the actual sources — not one

There is no single "how CS papers show code." Four different, equally
legitimate conventions exist, verified directly (not from memory):

**A — The software paper: no code in the body at all.**
Pedregosa et al., *Scikit-learn: Machine Learning in Python* (JMLR 12,
2011, `arxiv.org/abs/1201.0490`) — the paper most people cite as "the"
Python ML software paper — contains **zero code blocks**. Six pages,
all prose. The API is described entirely through inline `monospace`
identifiers in running text ("the central object is an `estimator`, that
implements a `fit` method... transformers... implement a `transform`
method"), one benchmark table, and "source code... can be downloaded
from `http://scikit-learn.sourceforge.net`." The paper describes the
*shape* of the interface; the repository is the code.

**B — The literate/annotated paper: the paper IS the notebook.**
Sasha Rush et al., *The Annotated Transformer* (Harvard NLP,
`nlp.seas.harvard.edu/annotated-transformer`) — a full re-presentation
of *Attention Is All You Need* — alternates markdown prose and complete,
runnable code cells, in the original paper's own order, each code block
placed immediately after the paragraph/equation it implements (verified
directly: `EncoderDecoder`, `Generator`, `Encoder` classes each follow
the one or two sentences of prose that motivate them, not a separate
appendix). Kept in sync with an executable `.py` via `jupytext` — the
paper *is* a notebook export, not a description of one. Original LaTeX
math is kept inline exactly as the source paper had it; the annotator's
own commentary is typographically set apart (blockquoted) from restated
original text, so a reader always knows which voice is speaking. Runnable
example code is gated behind a flag (`RUN_EXAMPLES`, `is_interactive_notebook()`)
so the paper can be read as a document or executed as a script without
forking the source.

**C — The mainstream ML paper: boxed pseudocode + a code-availability
statement, not literal source.** The convention used by the large
majority of NeurIPS/ICML-style papers: numbered, boxed `Algorithm`
environments in language-agnostic pseudocode (never a real language's
literal syntax), a one-line "Code available at [URL]" statement (often a
footnote), and, increasingly, a **Reproducibility Checklist** appendix —
a fixed list of yes/no/N-A items (data availability, hyperparameters,
compute used, seeds, number of runs) that a reviewer can scan without
reading the paper body. The checklist format is the closest existing
precedent to this project's own provenance-label system (`ESTABLISHED` /
`OURS` / `FIRST STATED HERE` / `THEORETICAL` / `THEORETICAL:CALCULATED` in
`FourthAgePapers/*/README.md` §2 or §0) — same job, per-component instead
of per-paper.

**D — The computational-algebra-system paper: a literal REPL transcript,
in the system's own language, not pseudocode and not a full listing.**
Bosma, Cannon, Playoust, *The Magma Algebra System I: The User Language*
(J. Symbolic Comput. 24, 1997 — verified directly, 2026-09-27) presents
its examples as bare interactive-session transcripts, prompt included:
input lines start with a literal `>`, followed by the system's own
printed output, exactly as a user would see it at a terminal (e.g. a
free-group element constructed, assigned, then echoed back by typing its
name alone at the next prompt) — not fenced as a language's syntax
block, not boxed as `Algorithm`, not narrated in prose first. This is
the natural convention wherever the "code" *is* a sequence of commands
typed at a live evaluator and the reader is meant to be able to retype
them at their own prompt and see the same output — the paper is a
transcript of a session, not a description of a program. Directly
relevant to this project's own console tools (`derivation`'s curses
SymPy console, `ptol.c`'s shell) — a worked example there is Convention
D, not B: show the literal prompt and its literal echoed result, not a
function definition.

A large multi-file simulation suite takes a fifth shape worth naming
separately from A, though it is a scaled-up case of A, not a new
convention: Jansen & Urbach, *tmLQCD: A Program Suite to Simulate Wilson
Twisted Mass Lattice QCD* (Comput. Phys. Commun. 180, 2009,
`arXiv:0905.3331` — verified directly, 2026-09-27), a gauge-theory
(lattice QCD) codebase paper, carries **no inline code at all** across
44 pages — the Hybrid Monte Carlo algorithm and its variants are
described in closed-form update equations (the physics, in real
mathematical notation, because the *algorithm* genuinely is math here),
and the actual C code is covered by ordinary software-manual sections
("Prerequisites," "Configuring the package," "Building and Installing,"
"Benchmark Executable") that tell a reader how to obtain, build, and run
the suite, never what any specific function's body contains. This is
Convention A pushed to its natural limit: when the codebase is large
enough that no excerpt would be representative, the paper stops trying
to excerpt it at all and documents the *installation and use* of the
whole thing instead — the same move scikit-learn makes at six pages,
here stretched to forty-four because the domain (lattice gauge theory)
needs that much closed-form setup before "how to run it" makes sense.

## 1. Which one to use — decide per component, not per paper

Do not pick one convention for the whole paper. Decide **per component**,
the same granularity the provenance label already uses:

- **Established, cited, off-the-shelf mechanism, ships from a library**
  (Miller–Rabin primality, sieve of Eratosthenes, WordNet lookup) → **A**.
  Name it, cite it, point at the file and function that calls it. Do not
  reproduce it as a formula or a listing — it is not this paper's
  contribution and re-deriving it in notation implies more originality
  than is true.
- **A short (≤ 40 line), OURS or FIRST-STATED-HERE mechanism that IS the
  paper's contribution** (the Horner hash, the pencil accessor, the
  combined-address construction) → **B**. Show the real function verbatim
  as a numbered Listing, immediately after the paragraph that motivates
  it, exactly as it runs in the repo today — not a paraphrase, not a
  formula standing in for it. If the mechanism only *becomes* clear by
  reading the code (e.g. why two prime tiers can't collide), the listing
  carries weight the prose can't.
- **A long or many-file mechanism** (the full monad, the box-kite module)
  → **A**, with a path + function name, same as scikit-learn's "download
  the source" move. A 40-line listing of a 2,000-line file is not
  transparency, it's a sample.
- **An open/THEORETICAL construction with no running code yet** → **C**'s
  pseudocode box, clearly labeled `THEORETICAL`, so a reader can see the
  intended shape without being told it already runs.
- **An interactive session at a live console/REPL is the actual artifact**
  (a `derivation` curses-console walkthrough, a `ptol.c` shell trace) →
  **D**. Show the literal prompt and its literal echoed output, not a
  function body — the point is "type this, see this," reproducibility
  at the prompt, not reproducibility of a definition.

## 2. Mechanical rules once a Listing (convention B) is chosen

- Fence it as real code (` ```python `), not a math block. If it isn't
  valid Python today, it doesn't get a Listing — it gets C's pseudocode
  box and the `THEORETICAL` label instead.
- Number and caption it: `**Listing 3 — token → prime address (`monad.py`,
  `_word_zero_idx`)**`. Reference it by number in prose afterward
  ("Listing 3 is what actually runs"), the same way de Marrais or any
  cited paper is referenced by name, not restated each time.
- One listing = one complete, runnable unit (a function or a small class),
  not a fragment that only makes sense pasted into a larger file. If it
  needs an import to run standalone, include the import line.
- State the source path and whether it is verbatim or extracted (this
  project's own `001_original_2026-05-27_word_zero_idx.py` header —
  "Extracted verbatim from `VAPMIP/monad.py` as it stood at commit
  `204c75d`... Confirmed byte-identical... today" — is the right model:
  it tells a reader exactly what they're looking at and how stale it
  might be).
- Reserve actual mathematical notation (Σ, Π, ζ, ↦) for results that are
  genuinely mathematics first and code second — a closed-form identity,
  a conserved quantity, a group-theoretic fact. A hash function, a sieve,
  a string encoder are code first; write them as code.

## 3. What NOT to do (the failure this skill exists to stop)

Do not write `H(w) = Σ_k ord(w_k) · 95^(|w|−1−k)` for something that is
`v = 0; for ch in w: v = v*95 + (ord(ch)-32)`. The formula is not wrong,
but it is the wrong register — it borrows mathematics's authority for
something that has no proof obligation, only a running-or-not obligation.
A reader who wants to check it has to re-derive code from notation instead
of reading the four lines that are already sitting in the repo. This is
the concrete thing to watch for when revising a draft: any Σ/Π/↦ block
that is describing a loop, not a theorem, is a candidate to become a
Listing instead.

## 4. Applying this to an engineering-structure paper specifically

For papers following the `CollatzShift`/"departure from the template"
posture (provenance label per component, no claim beyond what's proven —
see `FourthAgePapers/ScalarContextPropagation/README.md` §0), convention
B is the natural default for every `OURS`/`FIRST STATED HERE` component,
because the paper's whole posture is "here is the code, it works, look at
it" rather than "here is a proof." Convention A stays correct for every
`ESTABLISHED` component (don't re-derive de Marrais's box kite in
notation; cite it and point at `maths.py`). Convention C's checklist slot
is already filled by the paper's own desk-rejection gate (G1–G10) — do
not also bolt on a generic NeurIPS checklist; the project already has the
sharper, component-scoped version of the same idea.

## 5. The "perpetual now" — every listing is a fresh arrival, not a checkpoint

Named by Cody (2026-09-27): an old console RPG's opening-town NPCs still
say their day-one line if you walk back through after finishing the
game — that dialogue layer was never wired to the player's progress, so
it reads the same on visit one and visit forty. A paper's code listings
should have the same property, deliberately: **no Listing may assume
the reader is silently carrying forward variable values, object state,
or "what we did three listings ago."** Convention B (§0) already
requires each listing to be "one complete, runnable unit... not a
fragment that only makes sense pasted into a larger file" (§2) — this
section names *why*, and extends it past syntax into content: even when
a later listing genuinely consumes an earlier one's output, restate
that input inline (a literal value, a one-line stub, a `# from
Listing 3: addr = 91847...`) rather than relying on the reader having
mentally executed the paper in reading order.

The audience these papers are written for (§4 — "assumes minimal
knowledge of the codebase") is not assumed to have read every prior
page attentively or in one sitting. A reader who jumps straight to
Listing 7 because a citation pointed them there must be able to read it
cold, the same way a save file loaded mid-game still gets correct
dialogue in the first town. A paper that requires "you saw this mutate
in Listing 4" to understand Listing 7 has made the reader's position in
the document part of the program's state — the same "opaque, not
independently readable" failure this project's own papers exist to
argue against in the *model's* representations; the rule says the
prose has to clear that bar too, not just the mechanism it describes.

**Verification note (2026-09-27):** checked directly against the 8
papers fetched for `ScalarContextPropagation`'s citation pass
(`Ainulindale/references/cs_hashing_overhead/`) — Bloom 1970, Broder
1997, Weinberger 2009, Jégou 2011, Matias's FKS exposition, Mikolov
2013, Miller 1995, Elhage 2022. None of these actually carry a
sequential, multi-listing code narrative — they describe mechanisms in
prose plus closed-form notation (Convention A/C territory, §0), not a
run of dependent Listings — so this specific batch does not
independently confirm the pattern one way or the other. The clean
positive example stays the one already in this skill: *The Annotated
Transformer* (§0-B), whose per-class listings (`EncoderDecoder`,
`Generator`, `Encoder`...) each stand next to the sentence that
motivates them without requiring the reader to have run the previous
cell to follow the next one. Recorded here rather than overclaimed —
sound on its own technical-writing merits, but this citation batch
happens not to be where it was directly observed.

**Mechanical check**, when a draft has more than one Listing in a
section: read each in isolation, as if the ones before it didn't exist.
If it doesn't parse that way, it's carrying invisible reader-state —
restate the missing piece inline. A Listing may still *reference* an
earlier one by number in prose ("as in Listing 3") — that's citation,
not a dependency. Genuine pipelines are fine (Listing 5 really does
consume Listing 4's output); what's not fine is a *silent* one. Show
the seam.

## Sources (verified directly, 2026-09-19; §5 added 2026-09-27; Convention D added 2026-09-27)

- Pedregosa, F. et al. *Scikit-learn: Machine Learning in Python.* JMLR 12
  (2011), 2825–2830. `arxiv.org/abs/1201.0490` — read in full (6 pp.);
  confirmed zero code blocks.
- Rush, A. et al. *The Annotated Transformer.* Harvard NLP.
  `nlp.seas.harvard.edu/annotated-transformer` — fetched and parsed
  directly; confirmed prose/code interleaving order and the
  `jupytext`-paired-script production method.
- Bosma, W., Cannon, J., Playoust, C. *The Magma Algebra System I: The
  User Language.* J. Symbolic Comput. 24 (1997), 235–265. 874 citations
  (verified 2026-09-27). Downloaded and read directly
  (`Ainulindale/references/cs_hashing_overhead/Bosma_1997_magma_algebra_system.pdf`);
  confirmed the `>`-prompt transcript convention (Convention D) firsthand.
- Jansen, K., Urbach, C. *tmLQCD: A Program Suite to Simulate Wilson
  Twisted Mass Lattice QCD.* Comput. Phys. Commun. 180 (2009), 2717–.
  `arXiv:0905.3331`. Downloaded and read directly (same directory,
  `JansenUrbach_2009_tmLQCD.pdf`, 44 pp.); confirmed zero inline code
  blocks and the software-manual structure described above.
- The 8 papers in `Ainulindale/references/cs_hashing_overhead/` (Bloom
  1970, Broder 1997, Weinberger 2009, Jégou 2011, Matias/FKS, Mikolov
  2013, Miller 1995, Elhage 2022) — checked directly for §5's pattern;
  none carry a multi-listing code narrative, noted honestly rather than
  forced to fit.

## 6. Applying it to an API reference, not a paper (ValaQuenta, 2026-09-28)

The same conventions worked for an API reference site (Sphinx). Worked example:
`ValaQuenta/docs/gen_listings.py` builds `docs/listings.rst`.

- **A** for everything: the API pages name each function and point at its file;
  the README's Code Reference is an index (import path, one line, links), never a listing.
- **B** for five short OURS mechanisms, but *generated*, not pasted: the generator
  extracts each unit from source by name (docstrings removed, statements verbatim), joins
  it with exactly the constants and imports it needs so it is ONE self-contained unit,
  executes it cold in an empty namespace, and records the REPL output it printed. The
  page says "extracted", the line count and the source path. `tests/test_listings.py`
  re-runs the extraction and compares it to the real module, so a listing that stops
  running fails CI — the "perpetual now" rule (§5) enforced by machine, not by reading.
- **D** for the README's `>>>` session, which `tests/test_readme.py` runs as a doctest.
  Running it found a real bug the first time (registering 38 modules printed 38 lines).
- A listing that needs a class shell (a method) is shown inside a minimal `class X:` wrapper
  and labelled as extracted.
