# Does the character ordering of a .perm change the hyperindex address size? (2026-10-06)

`ord.py` — measures bijective base-N address bit-length (hyperindex.address, the PoC engine) under different
orderings of the same alphabet, on Dante stanzas (N=65), the canonical JSON entries (N=35) and Jupiter.html (N=664).

**Result.** Ordering moves an address by at most log2(N) bits in total, however long the document: the address is
≈ Nⁿ·(1/(N−1) + d₀/N + d₁/N² + …), so only the leading digits matter. Best ordering = by how chunks BEGIN
(chunk-start frequency), worth ~4–6 bits per chunk; text-first vs punctuation-first and frequency order are noise.
What changes size is N (alphabet size). Frequency order only helps with a variable-length code (not this bijection).
