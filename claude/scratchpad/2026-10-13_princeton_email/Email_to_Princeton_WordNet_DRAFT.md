**DRAFT v2 — not sent.** Updated 2026-10-13 after Cody approved sending the paper to Princeton for a first look; for Cody to review and send himself (planned: 2026-10-14).

**To:** Prof. Christiane Fellbaum, director of the Princeton WordNet project — fellbaum@princeton.edu *(from Princeton's Linguistics people page; confirm before sending)*
**Also consider:** `wordnet@princeton.edu` *(only seen on a 2001-era software-directory mirror; confirm on wordnet.princeton.edu)*.
**Attach:** `19_Dimensional_Scalar_WordNet_Context_Propagation_v4.0_2026-10-13.pdf` (42 pp., in this folder; rebuilt from the current text, includes §9.7/§9.8).
**Subject:** A WordNet-based offline language engine, a paper for a first look, and a question about proposing missing senses

Dear Professor Fellbaum,

I am an independent systems builder (ORCID 0009-0007-7239-6760). For about six months I have been building a language engine that runs entirely offline on a laptop, and WordNet is its foundation. I am writing first to the WordNet project at Princeton: to thank you and the team, to send you the paper that describes the work, and to ask for your candid reading of it, including where I have gotten WordNet wrong.

**The paper.** *19 Dimensional Scalar WordNet Context Propagation* (attached; code, executed notebooks and a round-trip report are in the repository: https://github.com/michaelrendier/FourthAgePapers/tree/scalar-context-propagation/ScalarContextPropagation). It reads only the 19 relation-pointer counts of each synset and maps them to a compact address; on the Open English WordNet build the round trip recovered the 19-vector exactly for 146,743 of 146,743 synsets, with one deliberate lossy step (a log compression of the counts, affecting about 1.1% of individual relation slots). Those figures are from my earlier note to the Open English WordNet maintainers and were not re-run for this email.

**What I did with the C library.** I also rebuilt a snapshot of the same 19 counts directly against the WordNet C library (`wordnet-dev`: `index_lookup`, `read_synset`), counting only synset-level pointers and checking it against NLTK's numbers. That table holds one entry per word's first sense (154,725 entries, about 12.7 MB) and is memory-mapped at run time. The engine's front door is an Infocom-style verb-governed parser, which I am now extending with NLTK and WordNet to pull topics, subjects, verbs and senses from a prompt.

**What I found, honestly.** In very small tests (seven sentences, not a benchmark), plain Lesk, most-frequent-sense and a PageRank variant over the pointer graph each chose the electrical sense of *reactor* for "neutron generation in different reactor types". A topic bag taken from a search overview fixed *reactor* and *generation*. *Pressurized water reactor* has no synset (the nearest is `water-cooled_reactor`), and *nuclear reactor*, *atom bomb* and *neutron* are joined only through very high ancestors, so the topical link a reader sees is not a typed edge. I plan to record such links and missing senses in an overlay, with provenance, separate from the base database.

**My questions.** (1) Is there a channel through which the team would want to receive candidate additions of this kind (missing senses with a gloss and proposed hypernym, topical links between existing synsets), and in what form? (2) Would you be willing to read the paper and tell me what is wrong with it? I would rather have a hard reading now than a polite one later.

**Attribution.** The work uses WordNet 3.0 and cites Miller (1995), *WordNet: A Lexical Database for English*, Communications of the ACM 38(11), and Fellbaum (ed., 1998), *WordNet: An Electronic Lexical Database*, MIT Press. The code is GPL v3 (github.com/michaelrendier: VAPMIP, ValaQuenta, Ainulindale, FourthAgePapers). I want to carry the WordNet license and copyright notice correctly in anything I redistribute, and I would be glad to be told if I should do anything differently.

Thank you for a resource that made a laptop-sized language engine possible.

Sincerely,
Cody Michael Allison (Michael Rendier)
the.wandering.god@gmail.com · github.com/michaelrendier · ORCID 0009-0007-7239-6760

---
*Checks before sending (Claude, 2026-10-13):* (1) confirm both Princeton addresses; (2) re-check that the four repo links return HTTP 200 and that the branch link opens (the earlier OEWN note asks for the same re-check on send day); (3) look at the WordNet license text yourself, because no WordNet license/copyright notice was found in VAPMIP, ValaQuenta or Ainulindale; (4) the Sep 27 note `EMAIL_WORDNET_OEWN.txt` (to the Open English WordNet maintainers) is separate and is consistent with this one on posture; the 146,743 (Open English WordNet synsets) and 154,725 (first-sense C snapshot) figures describe different artefacts.
