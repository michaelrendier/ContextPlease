# NLTK-only extraction + disambiguation prototype (2026-10-13)
tagger_train.py: PerceptronTagger trained offline on UD English-EWT (VAPMIP/datasets, no downloads): UPOS accuracy 0.9389 on the EWT test set (uni+bigram backoff 0.8729); 4.1 MB pickle; 0.28 ms per 7-token sentence; 44 s to train.
extract.py: NLTKWordTokenizer (no data) -> tagger -> Zork-style noun-modifier repair -> RegexpParser NP/PP chunks -> wn.morphy lemmas -> own extended-Lesk (gloss of sense + glosses of related synsets vs glosses of context words' senses).
Warm cost 3-19 ms per prompt; first call ~3.9 s (WordNet lazy load).
Results (4 prompts, illustrative): bank -> depository_financial_institution.n.01 OK; plant (power) -> plant.n.01 OK; first reactor -> nuclear_reactor.n.01 OK; neutron -> neutron.n.01 OK; fission.n.02 OK.
FAIL on the target prompt "neutron generation in different reactor types": reactor -> reactor.n.01 (electrical), generation -> coevals.n.01 (wanted nuclear_reactor.n.01, generation.n.06). Six words give almost no gloss overlap; the topical tie is not in WordNet glosses either.
Tagger error seen: "produces" tagged NOUN. Chunk-grammar bug found and fixed (VERB removed from NP modifiers).
