---
name: scalar-context-reading
description: >
  How to read a text's context the way Cody's ScalarContextPropagation paper (v4.0) reads a word: word -> WordNet synset -> 19 named
  relation counts -> one exact prime address -> one real (gamma_radial, the Gamma-Radial Windspeed); lifted here to a sentence (sum of the
  19-vectors), to semantic fields (lexicographer files), to recurrence chains, and to emotion via WordNet's own hypernym tree (anchor synsets
  -> recipe rows), with no training and no model. Load before reading any prompt for context, emotion or structure in the User-State work,
  and before claiming what a prompt "says" from word-level meters alone. Records what was MEASURED, including where it fails.
---

# Scalar context reading

Built 2026-11-24 from `VAPMIP/FourthAgePaper/ScalarContextPropagation/19_Dimensional_Scalar_WordNet_Context_Propagation_v4.0.md` (§3, §5, §7, §9, §11) and the shipped `VAPMIP/wordnet_boxkite.py`. Runner: `VAPMIP/Currentwork/UserState/read_context.py`. Run it with `VAPMIP/.venv/bin/python` (never system python).

## The design, in the paper's own terms
- A word is a synset (146,743 in Open English WordNet). Its context is **19 named relations** (hypernyms, instance_hypernyms, hyponyms, ... usage_domains), each count log2-compressed (`context_vector`).
- `context_code = prod CONTEXT_PRIMES[i]^v[i]` (primes >= 73, disjoint from the spelling letters <= 71): exactly recoverable; `full_addr = next_prime(spelling_code x context_code)`, `delta` recovers the pair.
- `gamma_radial = tanh(0.5 ln(log_code / LOG_ANCHOR))`: ONE real per synset. Near -1 = few relations (specific word); near 0 = relationally rich. `tree` = -0.151; `frustration.n.01` = -0.905.
- The point of the design: context is an addressable record you can read, diff and add, not an opaque vector. No learned parameters.
- The paper does NOT build the sentence reading. Its sentence constructor does not yet use the windspeed; the A-Matrix Basin Windspeed (live, corpus-dependent) is the sentence-construction wind and is out of scope there. Everything below the word level is an extension (mine), labelled as such.

## How to read a prompt (the procedure)
1. Tokenise; drop closed-class words; lemmatise per part of speech.
2. Word -> sense (rank-ordered WordNet sense; **no disambiguation yet**: see limits) -> `context_vector` -> `gamma_radial` and the lexicographer field (`noun.feeling`, `noun.communication`, `verb.emotion`, `noun.possession`, ...).
3. Sentence field = SUM of its words' 19-vectors (additive; `gamma_radial` of the sum).
4. Recurrence: the same lemma returning, counted per third of the text. This is the structure under "keep", "again", "N times", "every". A lemma that rises toward the end is where the text is going.
5. Emotion: a sense whose hypernym closure reaches an anchor synset (`anger.n.01`, `fear.n.01` ...) hits that emotion, weight 1/(1+rank); adjectives and verbs go through derivationally related nouns (angry -> anger). Each emotion is a row of the recipe table (`solution_tests.TABLE`), so a hit is a dose.
6. Say what the evidence is: the fields, the chains, the hits. Do not report an emotion the reader did not reach.

## Measured (2026-11-24)
- **GoEmotions human labels** (n = 1,954, no training): 49.4% of texts contain an anchored emotion word. Of those, the top emotion is in the human label set 52.4% of the time (chance ~ 9.7%); net sign (dark/light) agrees 74.1% (n = 957).
- **Cody's long prompt** (`Currentwork/UserState/dark-prompt.md`, 223 sentences, 2,440 words): 1,031 content words; fields noun.act 122, noun.communication 91, noun.cognition 71, adj.all 69, noun.person 55, noun.attribute 51, noun.group 48, noun.state 45, noun.artifact 42, noun.possession 33. The text is about acting, saying and knowing far more than feeling. Mean gamma -0.66 (344 sparse words, 57 rich).
- Recurrence by thirds (first / middle / last): `prompt` 1/5/7, `money` 2/2/5, `pay` 0/4/4, `work` 3/2/5, `keep` 3/1/4, `time` 8/2/4, `people` 9/9/3, `context` 5/1/2. The argument moves from people and time toward prompts, money and pay.
- Emotion anchors reached: only 57 of 223 sentences. Mostly `realization` (see, understand), `desire`, `anger` 13.3 (concentrated in "do you hear my anger?"). Dark/light agreement with the neurotransmitter prototype: r = 0.19.

## Limits (measured, not assumed)
- **Emotion expressed as stance is invisible.** Cody's anger sits in evaluative words, repetition and addressee ("you refuse", "stupid"), not in emotion nouns. The anchor reader misses most of it.
- **No sense disambiguation.** "fucked up" resolved to a desire sense; "keep" and "see" are over-broad. Needed before the anchors are trusted on profanity and light verbs.
- **No aim.** "stupid" at the model, at users, or at himself reads the same.
- **No negation, irony or aspect.** "keep breaking" is read as the verb keep, not as continuation.
- Word-level reading answers "what is this text about and what recurs", not "how does the speaker feel". Use it beside the dose meters, never instead.

## What to build next (needs Cody's go where marked)
1. Sense disambiguation (the nltk-zork-wordnet skill has the working method).
2. Aspect and recurrence cues as a frustration channel (keep, again, still, every time, N times).
3. A frozen-WordNet windspeed per sentence from the summed vector, compared with the dose.
4. Rebuild the recipe library balanced dark/light with drive as its own entry (changes the table: his go).
