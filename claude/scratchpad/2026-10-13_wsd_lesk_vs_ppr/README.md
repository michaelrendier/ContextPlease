# Lesk vs most-frequent-sense vs personalised PageRank (2026-10-13)
Seven hand-picked sentences (tiny, illustrative, NOT a benchmark). Correct = my reading of the WordNet definitions.
Result: each method got 2/7. PPR: nuclear_reactor right on both reactor sentences, wrong on generation (n.02 genetic, wanted n.06 heat/electricity), bank (ridge / gambling funds), both plants.
Lesk: reactor wrong on the target prompt, right on the "first reactor" sentence and bank-river. MFS: right on bank-river and power-plant only.
PPR graph: 117,659 synsets, 285,946 directed typed edges (the 19 RELATION_METHODS, undirected), 13.9 s to build, ~50-80 ms per query in numpy (unoptimised; graph must be prebuilt).
Reading: taxonomy-only edges lack the topical tie (neutron-reactor-generation); an associative/gloss edge family is needed. Run in PtolemyDesktop/.venv.
