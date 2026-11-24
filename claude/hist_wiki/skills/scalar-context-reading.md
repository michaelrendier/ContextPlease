# scalar-context-reading

**Skill:** `~/.claude/skills/scalar-context-reading/` · mirror `ContextPlease/claude/skills/scalar-context-reading/` · **Created:** 2026-11-24 (author: Cody Michael Allison): "create a reading skill ... out of VAPMIP/ScalarContextPropagation/ ... teach yourself how to read context like i have designed", an experiment on his long frustrated prompt (`VAPMIP/Currentwork/UserState/dark-prompt.md`).

Reads a text with the paper's mechanism: word -> synset -> 19 relation counts -> prime address -> `gamma_radial`; lifted (my extension, labelled) to sentence sums, semantic fields, recurrence by thirds, and emotion anchors via WordNet's hypernym tree mapped to recipe rows.

**Findings at creation (measured):**
- GoEmotions human labels, no training: 49.4% coverage; top emotion in the human set 52.4% (chance ~9.7%); net sign 74.1%.
- On the long prompt: only 57 of 223 sentences reach an emotion anchor; r = 0.19 with the dose prototype; the structure that shows is recurrence (prompt 1/5/7, money 2/2/5, pay 0/4/4 by thirds) and fields (communication, cognition, act far above feeling).
- Limits: stance-carried anger is invisible; no sense disambiguation ("fucked up" -> desire); no aim, negation or aspect.
