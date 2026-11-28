# 103 — Riemann, the Primes and the Prime Number Theorem

| | |
|---|---|
| Scope | the citation backing for the statement that the address space of the engine is the set of non-trivial zeros {γₙ}; the sources; what the framework takes; the "Zipf's law is the PNT" claim, corrected; primes by extinction and the Two Trees partition |
| Companion to | [98](98_provenance_and_citations.md) §A.1 |
| Verification (2026-11-13) | no DOI or arXiv identifier exists for the 1859–1901 sources, so none was machine-verified ([98](98_provenance_and_citations.md) §E). The arithmetic claims were re-run (Listing 1) |
| Confidence | the sources and the theorems: ESTABLISHED (as recorded) · the address-space statement: a design (§2) · "Zipf's law IS the PNT": **withdrawn** (§2) |

## 1. The sources

- **[Riemann1859]** B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*, *Monatsberichte der Berliner Akademie*, Nov. 1859, 671–680 (English translation in H. M. Edwards, *Riemann's Zeta Function*, Academic Press 1974; Dover 2001): ζ(s) = Σ n⁻ˢ = Πₚ (1 − p⁻ˢ)⁻¹; analytic continuation; the functional equation ξ(s) = ξ(1 − s); the non-trivial zeros in the critical strip; the explicit formula linking a sum over the zeros to π(x).
- **[Hadamard1896]** J. Hadamard, *Sur la distribution des zéros de la fonction ζ(s) …*, *Bull. Soc. Math. France* 24, 199–220. **[dlVP1896]** C.-J. de la Vallée Poussin, *Recherches analytiques sur la théorie des nombres premiers*, *Ann. Soc. Sci. Bruxelles* 20, 183–256: independently, the **Prime Number Theorem** π(x) ~ x/ln x, via ζ(s) ≠ 0 on Re s = 1.
- **[vonKoch1901]** H. von Koch, *Sur la distribution des nombres premiers*, *Acta Math.* 24, 159–182: RH ⟺ π(x) = Li(x) + O(√x ln x), the precise sense in which "the zeros control the primes".
- **[Mobius1832]** A. F. Möbius, *Crelle* 9, 105–123: the μ function and series inversion. **[Legendre1808]** *Essai sur la théorie des nombres*, 2nd ed.: the sieve count by inclusion–exclusion. **[Eratosthenes]**: the sieve itself (via Nicomachus, c. 100 CE).

## 2. What Ainulindalë takes

- **The zeros are the coordinate system.** A word hashes to a prime p (Horner); π(p) is its index; γ_{π(p)} on σ = ½ is its address; there is no lookup table ([09](09_hyperwebster_engine.md), [16](16_semantic_word_engine.md); VAPMIP_Paper §7). Measured detail: the hash is many-to-one (73,604 words onto 6,436 zero indices, up to 80 words per index, [57](57_boundary_ascending.md) Listing 2), so the address is an index into a set of zeros that many words share, a path address and not an injective encoding.
- **The explicit formula is the zeta spiral** with amplitude dots at the zeros (D-CS_Memory §22): the formula is verified in [83](83_the_archimedes_screw.md) §3. (The page's older phrase "`L_dynamic` visualised" uses the deprecated alias; the pathway variable is L_(I|O), [64](64_l_dynamic.md).)
- **Primes by extinction.** A prime is what survives the sieve. The sieve count is a signed superposition φ(x, a) = Σ_{d | Pₐ} μ(d)⌊x/d⌋, a two-term (Legendre) recurrence; Listing 1 of [104](104_fermat_wiles_and_the_corollary_they_missed.md) checks it. This is the Blue tree (Telperion, "what cannot be"); the complete remainder-free version is **The Two Trees** ([104](104_fermat_wiles_and_the_corollary_they_missed.md) §3, [47](47_the_two_trees.md)); measured in `GenerationalLineage/engine/lineage.py` (`sieve_lineage`, `sieve_recurrence`) and the generational-lineage skill.

**Withdrawn: "Zipf's law IS the PNT."** The earlier text said that f(r) ~ 1/rˢ (word frequency against rank) and π(x) ~ x/ln x "both follow from the analytic structure of ζ(s)", so that "every measurement of Zipf's law in natural language was a measurement of the prime distribution" ([21](21_chladni_zipf_riemann.md); [Zipf1949]). Zipf's law is an empirical regularity of word frequencies; the PNT is a theorem about primes. The two statements have different forms: the n-th prime obeys pₙ ~ n ln n, which is **not** a power law of the Zipf kind (a Zipf law has a constant log–log slope, while the log–log slope of pₙ against n is 1.27, 1.17 and 1.12 over successive decades,
Listing 1, and tends to 1 only logarithmically). What can be said is narrower: a word-to-prime hash maps the *ranks* of the vocabulary onto primes, and so imports the prime density into the engine's address space; that is a property of the hash, not an explanation of Zipf's law. `CONJECTURE`, untested against a word-frequency corpus.

**Listing 1 — the two-trees partition, the densities, and the log–log slope of the primes** (written for this page; needs numpy; runs cold)

```python
import numpy as np, math
N = 10**5; sv = np.ones(N + 1, bool); sv[:2] = False
for i in range(2, int(N**.5) + 1):
    if sv[i]: sv[i*i::i] = False
P = np.flatnonzero(sv); npr = len(P)
print('pi(10^5) = %d ; {0,1} = 2 ; composites = %d ; total = %d (N+1 = %d)' % (npr, N + 1 - 2 - npr, 2 + npr + (N + 1 - 2 - npr), N + 1))
for X in (10**2, 10**3, 10**4, 10**5):
    c = int((P <= X).sum()); print('X=%6d prime density %.4f, composite+{0,1} density %.4f, sum %.4f ; pi(X) ln X / X = %.4f' % (X, c / (X + 1), 1 - c / (X + 1), 1.0, c * math.log(X) / X))
slope = lambda a, b: (math.log(P[b - 1]) - math.log(P[a - 1])) / (math.log(b) - math.log(a))
print('log-log slope of p_n vs n over n = 10..100, 100..1000, 1000..9592:', [round(slope(a, b), 4) for a, b in ((10, 100), (100, 1000), (1000, 9592))])
```

```
pi(10^5) = 9592 ; {0,1} = 2 ; composites = 90407 ; total = 100001 (N+1 = 100001)
X=   100 prime density 0.2475, composite+{0,1} density 0.7525, sum 1.0000 ; pi(X) ln X / X = 1.1513
X=  1000 prime density 0.1678, composite+{0,1} density 0.8322, sum 1.0000 ; pi(X) ln X / X = 1.1605
X= 10000 prime density 0.1229, composite+{0,1} density 0.8771, sum 1.0000 ; pi(X) ln X / X = 1.1320
X=100000 prime density 0.0959, composite+{0,1} density 0.9041, sum 1.0000 ; pi(X) ln X / X = 1.1043
log-log slope of p_n vs n over n = 10..100, 100..1000, 1000..9592: [1.2708, 1.1655, 1.1216]
```

The partition 2 + 9592 + 90407 = 100001 reproduces; π(X) ln X / X falls toward 1 slowly (1.15 → 1.10), the PNT's rate. (The prime-plus-composite density sum of 1 is true by complementarity, which is why [104](104_fermat_wiles_and_the_corollary_they_missed.md) §3 reads it with care.)

**What is not claimed:** a proof of RH. The framework offers a coordinate system in which RH and its neighbours are simultaneously visible ([13](13_omgwtf_rh_proof.md)).

## 3. Appears in

[09](09_hyperwebster_engine.md), [13](13_omgwtf_rh_proof.md), [16](16_semantic_word_engine.md), [21](21_chladni_zipf_riemann.md), [42](42_rh_proof_no_primes.md), [47](47_the_two_trees.md), [72](72_the_cosmic_telescope.md), [73](73_why_the_half_line.md), [98](98_provenance_and_citations.md), [104](104_fermat_wiles_and_the_corollary_they_missed.md); D-CS_Memory §1–3, §21–22; VAPMIP_Paper §7, §12.
