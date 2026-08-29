# 103 — Riemann, the primes, and the Prime Number Theorem

[98_provenance_and_citations.md](98_provenance_and_citations.md) §A.1. The
address space of the whole engine is the set of non-trivial zeros `{γₙ}`. This
page is the citation backing for that.

---

## The sources

- **[Riemann1859]** Riemann, B. (1859). *Ueber die Anzahl der Primzahlen unter
  einer gegebenen Grösse.* Monatsberichte der Berliner Akademie, Nov. 1859,
  671–680. English translation in Edwards, H. M. (1974), *Riemann's Zeta
  Function*, Academic Press (Dover reprint 2001), Appendix.
  — ζ(s) = Σ n⁻ˢ = Πₚ (1 − p⁻ˢ)⁻¹; analytic continuation; the functional
  equation `ξ(s) = ξ(1−s)`; the non-trivial zeros in the critical strip; the
  **explicit formula** linking Σ over zeros to π(x).
- **[Hadamard1896]** Hadamard, J. (1896). *Sur la distribution des zéros de la
  fonction ζ(s)…* Bull. Soc. Math. France 24, 199–220.
- **[dlVP1896]** de la Vallée Poussin, C.-J. (1896). *Recherches analytiques sur
  la théorie des nombres premiers.* Ann. Soc. Sci. Bruxelles 20, 183–256.
  — independently, the **Prime Number Theorem**: `π(x) ~ x / ln x`, proved via
  ζ(s) ≠ 0 on `Re(s) = 1`.
- **[vonKoch1901]** von Koch, H. (1901). *Sur la distribution des nombres
  premiers.* Acta Mathematica 24, 159–182. — `RH ⟺ π(x) = Li(x) + O(√x ln x)`;
  the precise sense in which "the zeros control the primes".
- **[Mobius1832]** Möbius, A. F. (1832). Crelle 9, 105–123 — the μ function and
  series inversion. **[Legendre1808]** *Essai sur la théorie des nombres*, 2nd
  ed. — the sieve count by inclusion–exclusion. **[Eratosthenes]** the sieve
  itself (via Nicomachus, c. 100 CE).

## What Ainulindalë takes

- **The zeros are the coordinate system.** A word hashes to a prime `p`
  (Horner); `π(p)` is its index; `γ_{π(p)}` on `σ = ½` is its address. No
  lookup table (wiki/09, wiki/16; VAPMIP_Paper §7).
- **The explicit formula is `L_dynamic` visualised** — the ζ spiral, with
  amplitude dots at the zeros (D-CS_Memory §22).
- **Zipf's law IS the PNT.** `f(r) ~ 1/rˢ` (word frequency vs rank) and
  `π(x) ~ x/ln x` both follow from the analytic structure of ζ(s); every
  measurement of Zipf's law in natural language was a measurement of the prime
  distribution (wiki/21; [Zipf1949]).
- **Primes by extinction.** A prime is what survives the sieve — what *cannot*
  be removed. The sieve count is a signed superposition
  `φ(x,a) = Σ_{d|Pₐ} μ(d)⌊x/d⌋` — a two-term (Legendre) recurrence, Fibonacci in
  shape, with a prime-scaled second term. This is the Blue tree (Telperion,
  "what CANNOT BE"). The complete, remainder-free version of this dataset is
  **The Two Trees** — see [104_fermat_wiles_and_the_corollary_they_missed.md](104_fermat_wiles_and_the_corollary_they_missed.md)
  §3 and wiki/47. Measured: `SedenionFactoralRelativity/engine/lineage.py`
  (`sieve_lineage`, `sieve_recurrence`); `generational-lineage` skill.

**What is NOT claimed:** a proof of RH. The framework offers a coordinate
system in which RH and its neighbours are simultaneously visible (wiki/13).

---

## Appears in

wiki/09, wiki/13, wiki/16, wiki/21, wiki/42, wiki/47, wiki/72, wiki/73, wiki/98,
wiki/103, wiki/104; D-CS_Memory §1–3, §21–22; VAPMIP_Paper §7, §12.
