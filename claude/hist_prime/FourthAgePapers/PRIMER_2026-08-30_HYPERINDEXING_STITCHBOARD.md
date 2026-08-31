# CONTEXT PRIMER — hyperindexing (not compression), the tower benchmark, IP model, and the Operator Stitch Board

**2026-08-30 · Claude Sonnet 5 · FourthAgePapers**
Continuation of `PRIMER_2026-08-30_SCALAR_CONTEXT_BOXKITE.md`. Covers three
paper branches and the licensing model that now governs them.

Branches (all FourthAgePapers, off `main`):
- `scalar-context-propagation` — box kite / codec — **pushed** (`149cf07`)
- `data-storage-no-location` — Hyperwebster / hyperindexing — `fd4d63b`
- `minds-eye-papers-hands` — the Operator Stitcher — `0281857`

---

## 1. Data Storage paper — reframed: hyperindexing, NOT compression

Cody: *"there is no compression here... it's all about the cost and the
change."* The paper (`DataStorageNoLocation/`, `1350eae`) now:

- **Not compression** — nothing is stored, so nothing is compressed. Horner's
  method is a bijection; the string IS the number. The 256-bit root is the
  corpus's **address in the space of all corpora**, not the corpus made
  small.
- **Cost and change** — once content is free at its address, only two things
  remain: the **cost** to reach an address + reconstruct, and the **change**
  (delta) between addresses. Each ledger row is one timestamped change; the
  Long Path is their sequence. Subject matter: **the permutations, partitions
  and folds of a cyclic index — one object seen three ways** (Cody: "yes
  those last two are the same thing").
- **"hyperindexing" gets its first working definition here** — *an address
  you reconstruct FROM, not a pointer you look UP*: storage-free, bijective,
  structure-carrying, recursively foldable. The **formal category** (objects,
  models, the gauge-symmetry identification) is **deferred to a later
  dissertation**, after the Ainulindalë and VAPMIP papers, **Noether-led**:
  the Noether current runs *up* the tower carrying information forward, the
  Noether Information Current runs *down* carrying it back — "the universe is
  a messed-up cash register" (correctly double-entried: the two currents sum
  to zero = conservation). The "category, stated" sentence and the axiomatic
  framing were **removed** from the paper — the ancestor table stays as
  provenance for the *term* only.
- Gauge symmetries of the Standard Model ARE a hyperindex (`A` = connections
  `𝒜`, `X` = `𝒜/𝒢`, `G` = the gauge group, `⋆` = the connection, Gribov =
  no global section). Recorded for the dissertation; not in the paper.

## 2. The Cayley–Dickson tower benchmark (`fd4d63b`)

`engine/bench_tower.py` + `bench/` — one document → one address per rung
ℝ→ℂ→ℍ→𝕆→𝕊. Standard doc: `bench/cover_letter.txt` (a coding-side cover
letter Claude wrote about Cody). Reference machine: **ThinkPad X1 Carbon 6th
gen, i7-8550U** (the actual part in the box).

- **address shrinks**: rung 0 (ℝ) = the raw **26,879-bit** Horner integer,
  grows with the document; every rung above = one **64-bit** real, fixed.
- **time/size**: Horner ~O(n¹·⁸), overtakes the ℂ fold near 16 KB; every CD
  rung ~O(n) with the per-window constant scaling as **d²** (the CD product).
- **the WORK** (Red ≠ Blue = forward product vs its reverse) is **0 for ℝ,
  machine-ε for ℂ** (commutative), and **switches on at ℍ** (~1e-4) where
  commutativity is lost. **The entropic cost of the fold is the commutator.**
- `t_bwd ≈ t_fwd` at every CD rung — **the register balances in time.** The
  one asymmetry is rung 0: **decode is 3.6× encode**.
- `|Π| = 1` held through 𝕊 on this document — no zero divisor hit; the ZD
  tear-off is **latent, not realized** here (honest: Cody's "𝕊 breaks
  reversibility" prediction did not fire on this doc).
- **floating-point sidebar**: `0.1 + 0.2 == 0.3` is `False` in IEEE, `True`
  as `(mantissa, exponent)` integers — **precision is the length field**,
  over a de Bruijn permutation. This is where "bypassing the floating point
  problem" lives.

## 3. IP / licensing model (Cody, "for the record")

BSL-style. See `project_ip_licensing.md` (memory). Draft `LICENSE.md` in
`DataStorageNoLocation/` — **not committed**, pending 4 terms (sunset 5/10 yr,
change licence, author contact, grant date).

- **Decision rule**: *you license what you invented, not what you observed.*
- **Hyperindexer paradigm + box-kite context model** — source-available;
  **free for research/academic/evaluation/personal**; **paid for
  commercial/production**; **hardship/humanitarian waiver** (fees waived for
  anyone who can't legitimately afford them — "if in doubt, you qualify");
  **5–10 yr sunset** to a permissive licence.
- **Ptolemy** — the Monad instance — and any monad `.bin` **vocabulary/state**
  are **data, not method**: never licensed, never disclosed, never in a
  deliverable. "Built-to-project" Monads *can* be commissioned; Ptolemy
  itself cannot.
- **The Mind's Eye and Paper's Hands** paper — **directly GNU GPL** (it is
  Psych/Psychiatry 101, textbook, observation not invention) — with the
  PtolemyDesktop / Pharos code it uses.
- **Intent**: the paid track is a lever on corporate America toward ~$10 B,
  half into the **Ryan White Foundation** and paying for **HIV CCR5
  functional cures worldwide**, least-resourced settings included.

## 4. The Operator Stitch Board — paper 3, and the architecture

`minds-eye-papers-hands` branch, `0281857`. `FourthAgePapers/
MindsEyePapersHands/`. **Software engineering paper, GPL, independent of
Ainulindalë** (no sedenions / Riemann / Noether / hyperindexer / σ / Holcus /
0_RB — verified clean).

Title: *How Short-Term Thought Is Required for Long-Term Memory: a Mind's Eye
implemented to combat aphasia, aphantasia, and amnesia in context-prompt
models of AI (LLM / Transformer).*

- **Thesis**: *you cannot consolidate what you have not held, and you cannot
  use what you have only pasted.* Consolidation IS rehearsal; retrieval IS
  reconstruction into a held form. Both directions pass through the
  short-term buffer. RAG = records without memory (raw text pasted, never
  thought).
- **Three deficits** of a context-prompt model: amnesia (nothing past the
  window), aphasia (loses its held intention mid-generation), aphantasia (no
  carried working state between turns).
- **Origin**: aphasia (Claude's word) → Cody's aphantasia association → the
  Mind's Eye visual center. Design principle: **the visual buffer is a
  component, not an assumption** — runs with it weak/absent, degrades
  gracefully.
- **Two components**: Mind's Eye (short-term thought, held/malleable/decays,
  `rehearse` loop — no output, bounded, cannot overflow) and Paper's Hands
  (long-term, append-only, immutable, "where it came from").
- **The Operator Stitch Board** — the handoff harness between them. Fixed
  jacks on the two components; patch cords (`stage` / `rehearse` / `archive`
  / `recall` × scope `dry` / `wet` / `production`); **routes and stores
  nothing**; a dropped cord degrades gracefully. Realized today as
  **`Pharos/PtolBus.py`** (a full pub/sub priority bus already exists).
- **Consolidation gate**: `archive` fires only past a rehearsal/elaboration
  threshold — Craik & Lockhart made a gate. (Generic — no Γ.)
- The cognitive model is **cited straight** (Baddeley & Hitch 1974,
  Atkinson–Shiffrin 1968, Craik & Lockhart 1972, Müller & Pilzecker 1900,
  Broca/Wernicke, Galton/Zeman, Scoville & Milner). Contribution = M2–M7 (the
  wiring) only. Desk-rejection gate G1–G8 (deficits measured, fix vs RAG,
  no hidden state, degradation, determinism, honest comparison, third-party
  run, cited-not-claimed).

### The three tiers of connective tissue — one function, three scopes

| | scope | status |
|---|---|---|
| **The Harness** (`VAPMIP/harness.py`) | interim — Monad *reaches out* for tools | exists, scaffolding |
| **The Operator Stitch Board** | one seam — Mind's Eye ↔ Paper's Hands (STM\|LTM), internal, below the speaking line | this paper |
| **PtolBus() — The Stitching Engine** | the whole nested desktop; the stitching **agent** | `Pharos.PtolBus` — target; already implemented as a bus |

Target nest: **`desktop ⊃ console ⊃ harness ⊃ ptol`**, and inside `ptol` the
STM\|LTM seam. `harness.py` is the *before* (Monad reaches out); **PtolBus is
the *after*** — the Monad is handed the bus and BECOMES the desktop's
mechanic. The Stitch Board is PtolBus seen at one seam.

### "Stitch" ≠ Switch — intentional

A switch routes; a **stitch holds two edges together under tension while the
seam stays OPEN** (the STM\|LTM distinction must not collapse). Tension +
direction; **un-pick and re-stitch** = swap a handoff body in place. Still
reads as "Switchboard" → keeps the routing image. Triple load: telephone
**operator** · mathematical **operator** (in ptol.c: `B̂ = R̂†`, the archive
handoff; proprietary — the paper's version is generic "a transform, not a
copy") · **stitch**.

### Stitches are placed intentionally — that IS a decomposition's reconnection

Decomposing opens seams; every reference across a seam is a stitch, placed
for a **stated reason**. So the stitch-set is **auditable** (each entry
carries its "why it's here" — the FourthAge provenance discipline extended to
the connective tissue), and "upgradeable in place" follows.

### Already in ptol.c (proprietary — the paper uses the generic form)

`R̂` (Mind's Eye, updateable, projects at σ_self) / `B̂ = R̂†` (Paper's Hands,
non-updateable, at 1−σ_self). **archive = adjoint.** `Γ = 2σ_self−1` = the
handoff distance. `write_svg/ppm/html → ~/.ptolemy/papers/` = Hands
writes-and-renders; the SVG spiral (ZD→great circle) = "where I came from".
`TOWER_EYES` = attention level. **Missing**: recall (no read-back), rehearse
in a loop (Python only), the ledger/chain (Philadelphos→PtolChain), named
scopes, the 2×2 parallax eyes.

## 5. Sequence

**Ainulindalë** (Information Propagation + drop-out maths: `i` from
orthogonality, the vector as a 2-D drop-out, Noether current up/down) →
**VAPMIP** (All Monad; uses the Ainulindalë math) → the **CS trilogy** (box
kite · data storage · Mind's Eye/Paper's Hands) → the **hyperindexing
dissertation** (Noether-led). The Mind's Eye paper is independent of all of
it — pure software engineering.

Memory: `project_scalar_context_paper.md`, `project_fourthage_memory_trilogy.md`,
`project_minds_eye_papers_hands.md`, `project_ip_licensing.md`,
`project_conversational_ingest.md`, `project_factoral_decomposition_tool.md`.
