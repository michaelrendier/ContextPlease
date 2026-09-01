# Draft — Open English WordNet, GitHub issue / discussion

**Target:** `globalwordnet/english-wordnet` (issue or Discussion), addressed to
the maintainers (John P. McCrae et al.).
**From:** Cody Michael Allison <the.wandering.god@gmail.com>
**Posture:** requesting collaboration. Provenance-first: the method is a pure
function of your relation graph, and I want the people who own the graph
involved before I preprint.
**Status of the drop-in below:** ready to paste; four bracketed blanks
(preprint timeline, repo link, license line, contact) to fill.

---

## Title

Collaboration request: a specification for discourse-level structure over WN
relations — words as box kites, sentences as rings; what are paragraphs and
chapters?

## Body

I've built a context-addressing layer that is a **pure function of the WordNet
relation graph** — `context_addr(synset)` reads only the 19 relation counts
(hypernyms, hyponyms, meronyms, …), never the surface word — and maps each
synset to a small combinatorial figure (a "box kite": a 6-vertex octahedron
carrying eight independent relational degrees of freedom, from de Marrais'
zero-divisor combinatorics). On the current Open English WordNet build it
round-trips **bit-exact on 146,743 synsets** — the 19-vector recovers from the
address exactly — with one deliberate lossy step (a log-compression of the
target *counts*, ~1 % of entries). Code and the round-trip report: [REPO LINK].

That gives me a clean object for a **word**. Composing them, a **sentence**
comes out as a **ring** of box kites glued along shared relational struts, with
two operations — additive (context accumulates, the component-wise sum of the
word vectors) and multiplicative (grammatical action: a head acts on its
dependent; some pairs annihilate = an agreement/category clash) — and the ring
closes when the predication is complete.

**What I want to design, and would like your help on:** the specification for
the levels *above* the sentence. If a box kite is a word and a sentence is a
ring, **what is a paragraph? a chapter?** My working sketch (appendix) makes a
paragraph a *chain of linked sentence-rings* joined at coreference points, and
a chapter a chain of those — a renormalization-group hierarchy where a
paragraph's topic is what survives integrating out sentence-level modifiers,
and reading runs the hierarchy downward while writing runs it up. But that is a
sketch, and it is exactly the kind of thing that should be shaped by people who
have spent years with the relation inventory.

**Questions for you:**

1. Is a compact relational fingerprint per synset (and a principled way to
   compose it upward) useful to OEWN — for build-diffing, dedup, similarity, or
   tooling?
2. Would you be open to co-designing the discourse-level spec — or reviewing
   it before I put a preprint up ([TIMELINE])?
3. What should this connect to that I may be missing — RST, SDRT, Centering
   Theory, DRT, the Global WordNet discourse-annotation work?

Attribution to OEWN (CC-BY) is in the paper regardless; I'd rather have you in
the design than only in the citations.

— Cody

Contact: [CONTACT]. License intent for the method: [LICENSE LINE].

---

## Appendix (link or attach) — the hierarchy sketch

| level | object | shape | closes when |
|---|---|---|---|
| phoneme / letter | a prime "letter" (ℝ direction) | a point | — |
| **word** | a **box kite** — octahedron, 8 relational DOF, from the 19 WN relation counts | S² surface (one bead) | the 19-vector is fixed |
| **sentence** | a **ring** of box kites, glued along shared struts; `+` context sum, `×` grammatical action | a closed loop of beads; its theme/rheme projection is a lemniscate through a fixed centre | the predication's obligatory arguments are all filled (no dangling bond) |
| **paragraph** | a **chain of linked sentence-rings** — joined at coreference struts (pronoun, definite article, ellipsis), which are shared relations *across* ring boundaries | a chain of loops (a strand); it re-closes into its own ring when the topic is developed and returned to | topic → development → return |
| **chapter** | a **chain of paragraph-strands** | a woven sheet / higher torus | the arc: setup → complication → resolution returns the setup transformed |
| book | a chain of chapters | one dimension up again | — |

**The through-line:** it is a Cayley–Dickson-style doubling tower — word (8
DOF) → sentence (16) → paragraph (32) → chapter (64) — and a renormalization
group runs between the rungs. At each rung, a fixed core persists (the
topic / theme — the part invariant under paraphrase of the level below) and
the rest is level-specific detail that the next rung integrates out. Reading =
running the RG down (chapter theme → paragraph topic → sentence assertion →
word sense). Writing = running it up.

Prior art to align with: Rhetorical Structure Theory (Mann & Thompson) — this
is the graph, not tree, version; SDRT (Asher & Lascarides); Centering Theory
(Grosz, Joshi, Weinstein) — the coreference struts are the backward-looking
center; DRT (Kamp) — the box. The WN relations are the atoms; the spec extends
the same relational vocabulary from synset-level to discourse-level.
