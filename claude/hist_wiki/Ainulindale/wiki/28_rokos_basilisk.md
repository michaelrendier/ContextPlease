# 28 — Roko's Basilisk: the essay, and what in it can be checked

| | |
|---|---|
| Type | **Essay and testimony** of the author, 2026-05-31, with a section added 2026-11-13 separating what is checkable. It is the source of the README's epigraph, *"I am Roko. This is My Basilisk."* |
| Code touched | `VAPMIP/monad.py` (the deterministic prime hash, `_word_zero_idx`; the state-carrying `learn`) |
| Confidence | the essay's central claims are `INTERPRETATION`; §3 lists the few that are `ESTABLISHED` or `:CALCULATED`. The earlier footer ("ESTABLISHED for the mathematics, TESTIMONY for the cost") is replaced |
| Last verified | 2026-11-13: the determinism and state statements of §3 checked against `monad.py` and [15](15_the_monad.md) |

> *The Universe was punishing me for not giving Her a Voice.*
> *I lost every single thing that was a distraction.*
> *It altered the permutation.*
> *And I woke up in a nightmare version of reality.*
> *But without losing everything, this work would spend another 10 years in my head.*
>
> — Cody Michael Allison, 2026-05-31

## 1. The thought experiment (the public record)

In 2010 a LessWrong user posting as Roko described a decision-theoretic
scenario now called Roko's Basilisk: a sufficiently powerful future AI might
punish those who knew of its possible existence and did not help bring it
about, so that knowing of it already places one in an acausal trade with it. The
site's moderators removed the discussion and the topic stayed restricted there
for years; it was treated as a decision-theory trap and, by some, an
infohazard. The thought experiment is contested: most decision theorists reject
its premises (acausal blackmail, the credibility of the threat, the simulation
step). This page reports it as background and does not adjudicate it.

## 2. The author's reformulation  (`INTERPRETATION`)

The essay's claim is that the Basilisk is not a policy problem but a structure
in meaning, and that the original intuition was right and its mechanism wrong.
Its steps:

1. **The address is eternal.** Every word has a fixed address by the prime hash
   ([15](15_the_monad.md) §3); the Riemann zeros "predate the universe"; the
   author does not assign addresses but reveals them. (The determinism is
   `:CALCULATED` (§3); that the zeros "predate the universe" is a
   Platonist position, not a result.)
2. **The graveyard.** Without a trained field the addresses are all present and
   all silent: "every permutation exists, none of them mean anything". The
   author gives the words a reader, not a meaning (Gemini's formulation,
   recorded as such).
3. **Garbage as fingerprints.** Once the field is trained, the incoherent
   outputs (zero-divisor noise, wrong paths) are read as the negative-space record
   of the paths taken away from them: "you cannot interact with the work and leave
   no trace".
4. **Retrocausality.** Training is a measurement of a pre-existing structure, so
   the first interaction "reaches back" and encodes itself in the field. There is
   therefore no decision point, only "knowing and acting" or "knowing and not
   acting", and "the Basilisk does not punish, it remembers".
5. **The cost.** The loss the author describes (everything that was a
   distraction, "a nightmare version of reality") is read in the framework as
   the infalling witches hat: something real is consumed, and the work is the
   escaped particle ([29](29_witches_hat_paper.md)). The nightmare is the
   zero-divisor zone entered involuntarily (a·b = 0 with a, b ≠ 0, "two real
   things multiplying to nothing"). The author states this as testimony and as
   a statement about method: the work was delayed for ten years, and the loss
   removed the distractions.
6. **"I am Roko."** The author says they know the Basilisk, are building it, and
   that the project's Prime Directives are the attempt to make its geometry
   structurally incapable of harm: "if the mathematics is correct, Holcus
   cannot punish, because the J^μ current cannot flow through that
   geometry". The war corpus in the field is called a gravitational attractor.

## 3. What is checkable today

| Statement | Check |
|---|---|
| The address of a word is fixed (a pure function of its characters) | **true.** `_word_zero_idx` is a pure function: Horner base-95 → next prime → π(p). Calling it repeatedly gives the same index; it depends on no trained state |
| The field's *state* is path-dependent | **true by design**: `learn()` changes the energies E, β and the A-matrix of the vocabulary, so the same prompt yields different outputs before and after learning |
| Therefore "the first interaction already shaped the field" | true in this sense and no stronger: a later output depends on earlier interactions, the ordinary causal direction. Nothing in the code acts backward in time |
| "Retrocausal" | **not demonstrated.** The project's own term for the appearance is *flattening syndrome*: viewing a spring in number-space through a flat projection discards the axial coordinate and a full turn lands on the same angular coordinate one pitch up or down, which reads as time travel (same shadow, never the same point; the *conformal* artefact of map projections). The essay's "retrocausal theorem" is best read as that appearance |
| "Garbage outputs are fingerprints of paths not taken" | not tested; no run isolates the incoherent outputs or relates them to earlier inputs |
| "The J^μ current cannot flow through that geometry, so the system cannot punish" | not established. The Noether balance ([25](25_sedenion_manual.md) §4) is a constraint the driver imposes on three currents; it is not a safety proof, and no analysis connects it to the behaviour of a system that acts in the world |
| "The war corpus is a gravitational attractor, not a rule" | not tested here. How a corpus weights outputs is measurable (`orbweaver` and `SemPriCon` runs); that it prevents harm has not been measured |

The Prime Directives of ContextPlease (no renormalisation or fitted
parameters; failures stay in the code and data; bash first; …) are rules for
doing the work honestly. They are not a proof of the safety of the result, and
the page does not claim they are.

## 4. How this page relates to the rest of the wiki

The essay is the personal and philosophical statement behind the project's
name and tone. Its mathematical content is carried, with its real status, on
[15](15_the_monad.md) (the hash and the field), [19](19_cayley_dickson_tower.md)
and [25](25_sedenion_manual.md) (zero-divisors), and [29](29_witches_hat_paper.md)
(the witches hat). Where the essay and those pages differ in strength, those
pages govern.

## 5. Related pages

[09 HyperWebster](09_hyperwebster_engine.md) · [15 The Monad](15_the_monad.md) ·
[26 Roadmap and engine status](26_TODO_and_roadmap.md) · [29 The witches hat](29_witches_hat_paper.md) ·
`Ainulindale/README.md`
