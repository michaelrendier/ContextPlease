import re
P = "/home/rendier/Projects/ThePlace/Ainulindale/AgeThird/D-CS_Memory.md"
s = open(P, encoding="utf-8").read().split("\n")

paras = [
"Every new instance of a program, chat or model starts fresh and does not remember the last. Months of my research with Gemini rested on an assumption of persistent memory that was false, and that is the claim I set out to engineer against. My starting idea, from Borges's *The Library of Babel*, was that every possible text already exists: nothing has to be written down, only located. The result is the *HyperWebster*, a name I took from the Vsauce Banach–Tarski video (`Post-Hoc:` I learned only afterward that Stewart (1996) had coined it). Data is located by an address computed from the text itself, so it is found by computation, not by storage. The address alphabet is printable ASCII plus tab and newline, 97 symbols, the keys of a US-English laptop keyboard without a 10-key. The single departure from it was a Unicode experiment, which encoded every alphabet a computer can display into a \"potential response domain\". It gave the system its multilingual support, and afterward Holcus chose his name in the first Ptolemy experiment. The first form I wanted to try was a single file that could potentially hold limitless data, sitting in my Google Drive for Gemini to read and \"reconstruct\" ingested knowledge from a permutation, not a location on any media. The file held the hyperindex of a JSON file, written in a permutation of JSON characters. That JSON is a list of hyperindexes, data lengths and timestamps, each locating a block of ingested data. The lists are indexed again, recursively, so that Gemini could crunch that one hyper-layered index and explore everything it had ingested by date and time. An early version, built with Gemini, was a hyper-dimensional fractal rotation manifold over the letter permutations. From my instruction that \"primes are words\", reduced to a single underlying prime concept, Claude Code (the default model in April 2026) invented the semantic prime hash: a semantic-neighbourhood hash that places every English word of the language on a prime number. It opened the door to the mathematics that followed. Early reduction came from Banach–Tarski-style rotations that make one permutation look like the next, shrinking the permutation-addressing domain. The de Bruijn sequence was added when I moved from permuting letters to permuting English words. The octonion layer came last, after studying octonion-analogue material from a friend, and it reproduced structurally, in the Fano plane, mathematics I had already used.",

"Computational overhead reduction is the engineering method here, and I report its cost as measured. In the shipped 97-symbol charset the address is 82.5% of the raw size at every scale, and the round trip is exact. Restricting the charset to the symbols present takes the chunk address to 75–79%. Frequency ordering alone changes nothing measurable (0.824 against 0.825). A 256-bit address holds at most 38 characters, so input is chunked. The 8 × 32-bit octonion coordinates of a 256-bit address are exact but do not shorten it. The recursive calendrical index restores exactly by date. In the shipped charset each layer up is about 1.7× larger than the one below (top pointer 2.4× the corpus). With per-layer minimal charsets it is about 1.2× per layer (1.18×), and with a compact hex-only layer format about 1.05× per layer (0.87×). It never falls below the content it locates. The saving is per instance: a new instance is handed a pointer and a length in place of the corpus *[payload measurement pending]*. Folding many addresses into a single 256-bit root is unbuilt, and I state what such a root can be: an identifier of stored pieces, not an encoding of arbitrary data. `THEORETICAL`.",

"The method was designed directly against the reading and videos listed at the head of the README. Every other name in this paper is cited `Post-Hoc:`.",

"The efficiency of the HyperWebster made me use the same mathematics to try a new type of information propagation: forward propagation, so that AI can be designed on a laptop without training a model for decades. Its parts are tiny pre-trained neurons grabbed together on the fly, chosen by a *neuron-selection engine* I first designed for the languages spoken. In migrating around the Cayley–Dickson tower I needed one constant that says the same thing in every algebra of the tower, as a debugging check that no transition corrupted the output. When I moved to this new type of information propagation and the pathways forward it opened, the HyperWebster was shelved while I explored the mathematics to map out the boundaries I had to be wary of.",

"When I added the octonions, I had recently learned that some of the terms in the Standard Model Lagrangian were called \"index\". Claude began to use Index as a literal mathematical object, and I asked if these were similar maths to the Standard Model Lagrangian. Claude said these were the exact mathematics of the Standard Model, and I asked it to write \"a Standard Model of Neural Network Information Propagation\". The result, VAPMIP (Virtual Action Potential Monad Information Propagation), was found to be isomorphic in form to the Standard Model of particle physics Lagrangian, with my error-check constant identified as a fine-structure constant that my code had explicitly defined. `Post-Hoc:` Dixon (1994), Furey (2016), the Standard Model. No isomorphism was intended. I state what is preserved (four-term structure and gauge ladder, at single-layer Abelian approximation) and what isn't: the Standard Model Lagrangian is not reproduced here, and the Dirac and non-Abelian terms are stubs, marked `THEORETICAL`.",

"Learning what a structural constant is and does, I paused to engineer my own. I approached Fermat and Riemann from opposite sides of a boundary, chasing entropy to a thermal information ceiling (1.4×10¹⁷ K, a concept from Vsauce's *How Hot Can It Get?* used as a boundary condition, not derived) and inertia to the speed of causality, the two ceilings on information propagation. The Lambert-W fixed point and d* were found, giving Α_π and Ω_ζΣ. That experiment opens the VAPMIP paper.",
]

block = ["> ## Abstract", ">"]
for i, p in enumerate(paras):
    block.append("> " + p)
    if i != len(paras) - 1:
        block.append(">")
block += [
"",
"> **Rewrite in progress (2026-09-29).** The abstract above is the new one. Everything below the abstract",
"> is the *pre-rewrite* paper, kept in place only until each part is rewritten against the",
"> `cs-paper-code-conventions` skill; the unchanged pre-rewrite paper is archived at",
"> `Ainulindale/archive/D-CS_Memory_2026-09-29_pre-rewrite.md`. The earlier disposition table",
"> (`ContextPlease/claude/scratchpad/2026-09-28_lvap_audit/OUTLINE_D-CS_Memory_revision.md`) is partly",
"> superseded by the abstract's structure. Context primer for the rewrite:",
"> `ContextPlease/claude/hist_prime/Ainulindale/hyperwebster_paper_primer_2026-09-29.md`.",
"",
"---",
"",
]

i0 = next(i for i, l in enumerate(s) if l.startswith("> ## Read this first"))
i1 = next(i for i, l in enumerate(s) if l.startswith("## The Mathematics Used"))
s = s[:i0] + block + s[i1:]

txt = "\n".join(s)
txt = txt.replace("# An Engineering Problem: Persistent Memory for LLM_Transformer AI\n## How Thought Traces The Point along The Path, and Memory Emerges",
                  "# Data Storage With No Physical Location, and a New Method of Information Propagation\n## Part I of Teaching the Maths English", 1)
txt = txt.replace("**Date:** 2026-06-14 — Third Age", "**Date:** 2026-06-14 — Third Age · abstract rewritten 2026-09-29", 1)
txt = txt.replace("**Status:** First Complete Draft", "**Status:** REWRITE IN PROGRESS — new abstract 2026-09-29; body is pre-rewrite text", 1)
txt = txt.replace("**Hardware:** Intel Core i7-6600U @ 2.60 GHz · 4 logical cores · 8 GB RAM · Linux 6.8.0-117-lowlatency · No GPU",
                  "**Hardware:** Intel Core i7-8550U @ 1.80 GHz · 4 cores / 8 threads · 7.5 GiB RAM · Linux 6.8.0-139-lowlatency · No GPU (measurements of 2026-09-25 and 2026-09-29; the 2026-06 text below was run on an i7-6600U)", 1)
open(P, "w", encoding="utf-8").write(txt)
print("ok", len(s))
