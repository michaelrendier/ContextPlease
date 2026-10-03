# Hyperindexing code read + tests (2026-09-29)
Paper: FourthAgePapers/HyperindexingSystem (Cody, 2026-09-29: "this paper is about Permutations").
Read: Callimachus/HyperWebster-Data-Storage/{hyperwebster,hyperwebster-hash,infinite-data,infinite-data-vector-shaders(118-233),hyperwebster_manifold,hyperwebster_archimedes,hypergallery}.py;
Callimachus/v09/{core/charset,core/hyperwebster,gallery/hypergallery,database/hyperdatabase}.py; hyperwebster_layer3.py; Kryptos/{Ciphers/Vigenere,kcf}.py;
Archimedes/Maths/MidlineIndex.py (docstring); ValaQuenta/modules/hyperwebster/maths.py; VAPMIP/engines/e17_hyperindexing.py.
NOT yet read: acquire.py body, ptolemy_ingest.py body, GLSL half of the shaders file, VAPMIP monad.py hash, notebooks, DataStorageNoLocation branch, Kryptos analysis.py bodies (only signatures).

| test | file | result |
|---|---|---|
| T1 spectral_address_range (the JWST search) | t1_spectral_range.py | 129/4096 satisfying images in range; 129/513 in-range satisfy; satisfying set = 512 disjoint runs |
| T2 index_image cache key (first 16/32 values) | t2_cache_collision.py | two different images get ONE label; regenerate(b) returns a |
| T3 CharacterManifold bits | t3_manifold.py | sum(sub_bits) 6144 vs naive 6600 vs floor 4718 at L=1000 (independent C(L,c) overcounts) |
| T4 VocabFactorizer reduction | t4_vocab.py | reported 4.6-13x; with vocab+punct stored: 0.76-0.80x (worse than raw) |
| T5 PRIVATE charset = monoalphabetic substitution | t5_private_charset.py | identity holds; rank-matching alone recovers 44.7% of positions; keyspace 97! = 2^505 |
| T6 charset orders in the code base | t6_charset_orders.py | 3 different 97-orders -> 3 different addresses for "hello"; keyboard->Unicode perm cycle type [92,3,2] |
| T7 permutation content | t7_orbit_permutations.py | transposition offset identity holds; exact multiset rank = (count vector, rank): 0.79 of naive at L=1000-4000 |
| T8 Rabies trigger | t8_rabies_trigger.py | trigger names non-existent column; never fires |
Other code findings (no test needed): infinite-data.py calls nonexistent locate_text and uses undefined PTOL_ROOT at import; kcf.hw_address is not bijective (0-based plain base-N, ord%N fallback) and its "charset permutation" is sha256(charset)[:8] XOR, not the N! permutation index charset.py promises; ValaQuenta horner_encode is non-bijective (length stored) and maps unknown chars to 0; OrbitCache promises offset addressing but implements an exact-string cache; v09 _pixels_to_int carries a dead stub loop.
