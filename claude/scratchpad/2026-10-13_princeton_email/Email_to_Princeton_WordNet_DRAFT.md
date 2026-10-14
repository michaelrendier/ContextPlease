**DRAFT — not sent.** Prepared 2026-10-13 for Cody Michael Allison to review and send himself.

**To:** Prof. Christiane Fellbaum (director of the Princeton WordNet project) — fellbaum@princeton.edu *(listed on Princeton's Linguistics people page; verify before sending)*
**Alternate / cc to consider:** the project list address `wordnet@princeton.edu` *(only found on a 2001-era software-directory mirror — confirm on wordnet.princeton.edu first)*; John P. McCrae, Open English WordNet (github.com/globalwordnet/english-wordnet) if you want the community fork's view on additions.
**Subject:** An offline WordNet-based language engine built on the C library — and a question about proposing missing senses

Dear Professor Fellbaum,

I am an independent systems builder (ORCID 0009-0007-7239-6760). For about six months I have been building a language engine that runs entirely offline on a laptop, and WordNet is its foundation. I am writing to thank you and the Princeton team, to show you one thing I did with the database, and to ask one question.

**What I did with WordNet.**
- Every word is stored with a fixed 19-slot vector: for its first sense, the log-compressed count of its targets under each of WordNet's pointer types (hypernym, hyponym, holonyms, meronyms, attributes, entailments, causes, also-sees, verb groups, similar-to, and the three domain types). Words are addressed by a prime-number hash, and a single scalar derived from the vector travels with each word.
- I rebuilt this table in C directly against the WordNet C library (`wordnet-dev`, `index_lookup`, `read_synset`), counting only synset-level pointers, and checked it against the same numbers computed through NLTK in Python. The C build holds 154,725 entries in about 12.7 MB and is memory-mapped at run time.
- The engine's front door is an Infocom-style verb-governed sentence parser (Zork's), and I am now extending it with NLTK and WordNet to pull topics, subjects, verbs and senses out of a prompt.

**What I found, honestly.** In very small tests (seven sentences, not a benchmark), plain Lesk, most-frequent-sense, and a PageRank variant over the pointer graph each picked the electrical sense of *reactor* for "neutron generation in different reactor types". Supplying a topic bag taken from a search overview of the subject fixed *reactor* and *generation*. I also noticed that *pressurized water reactor* has no synset (the nearest is `water-cooled_reactor`), and that *nuclear reactor*, *atom bomb* and *neutron* are linked only through very high ancestors, so the topical link that a reader sees is not a typed edge. I am planning an overlay that records such links and missing senses separately from the base database, with provenance, rather than modifying WordNet itself.

**My question.** If I collect candidate additions of this kind (missing senses with a gloss and a proposed hypernym, and topical links between existing synsets), is there a channel through which the WordNet team would want to receive them, and in what form? I would also welcome a correction if I have misread how any of the pointer counts should be taken.

**Attribution.** The work uses WordNet 3.0 and cites Miller (1995), *WordNet: A Lexical Database for English*, Communications of the ACM 38(11), and Fellbaum (ed., 1998), *WordNet: An Electronic Lexical Database*, MIT Press. The code is released under the GPL v3 at github.com/michaelrendier (VAPMIP, ValaQuenta). I want to make sure that I carry the WordNet license and copyright notice correctly in anything I redistribute, and I would be glad to be told if I should do anything differently.

Thank you for a resource that made a laptop-sized language engine possible.

Sincerely,
Cody Michael Allison (Michael Rendier)
the.wandering.god@gmail.com
ORCID 0009-0007-7239-6760
