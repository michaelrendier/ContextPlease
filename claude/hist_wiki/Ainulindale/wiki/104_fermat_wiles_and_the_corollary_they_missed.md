# 104 — Fermat, Wiles, Modularity, and the Corollary Claimed Beyond Them

| | |
|---|---|
| Scope | the Fermat side as the Blue channel ("what cannot be"); the citation backing; what the proof established; and one specific claim of the framework (primes by extinction as a complete, remainder-free dataset, the Two Trees), stated so it can be checked or refuted |
| Companion to | [98](98_provenance_and_citations.md) §A.2 |
| Verification (2026-11-13) | DOIs checked: Wiles 1995 (*Ann. Math.* 141(3), 443), Taylor–Wiles 1995 (141(3), 553), Ribet 1990 (*Invent. Math.* 100, issue 1, 431–476), BCDT 2001 (*JAMS* 14(4), 843–939). Fermat, Shimura 1971 and Tannery–Henry were not machine-verified. The sieve statements were re-run (Listing 1) |
| Confidence | the sources and the Legendre recurrence: ESTABLISHED · the partition: ESTABLISHED (exact) · "zero-gradient harmonic field": `THEORETICAL`, a reading offered for argument · the priority claim ("the corollary they missed"): not assessed; see §3 |

## 1. The sources

- **[Fermat1637]** P. de Fermat, marginal note in Bachet's *Diophantus*, Bk II, Prob. 8, published by Samuel de Fermat 1670; infinite descent: letter to Carcavi 1659 (*Œuvres*, ed. Tannery–Henry).
- **[Ribet1990]** K. A. Ribet, *On modular representations of Gal(Q̄/Q) arising from modular forms*, *Invent. Math.* 100(1), 431–476: the epsilon conjecture, Taniyama–Shimura ⟹ Fermat's Last Theorem.
- **[Wiles1995]** A. Wiles, *Modular elliptic curves and Fermat's Last Theorem*, *Ann. Math.* 141(3), 443–551. **[TaylorWiles1995]** R. Taylor & A. Wiles, *Ring-theoretic properties of certain Hecke algebras*, 141(3), 553–572. **[BCDT2001]** C. Breuil, B. Conrad, F. Diamond & R. Taylor, *On the modularity of elliptic curves over ℚ: wild 3-adic exercises*, *JAMS* 14(4), 843–939: the full Modularity Theorem.
- **[Shimura1971]** G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton UP): Taniyama's problem (1955), the Taniyama–Shimura(–Weil) conjecture.

## 2. What the proof established, in this framework's language

Wiles (completed by Taylor–Wiles, generalised by BCDT) proved that every elliptic curve over ℚ is a modular form, an automorphic object with its own L-function. FLT follows via Ribet: a Fermat solution would give a Frey curve that could not be modular. In Ĥ_RB terms ([14](14_redblue_hamiltonian.md), [18](18_fermat_lattice.md), [52c](52c_j2_involution_riemann_fermat.md)): Fermat encodes where integer power-triples cannot be (the forbidden lattice, the negative space, the Blue channel by wiki 51 and 104's convention); the Riemann/automorphic
side encodes what is (the prime distribution, the Euler product, the zeros); modularity is the bridge, and R̂† = B̂ is the operator form. "Wiles's proof already couples what cannot be to the Riemann/automorphic world": standard, as far as it goes. (Colour/Tree labels differ between pages; the open conflict is recorded in [96](96_the_riemann_fermat_horizon.md) §2.)

## 3. The step this framework adds, stated for checking or refutation

The claim: modularity connected the Fermat *constraint* to L-functions; what was not stated is that the **factorisation data itself** (the complete record, for every integer, of what it is not divisible by) defines the primes by extinction and is a **harmonic / zero-gradient field**.

1. **Primes by extinction.** Strike every multiple of 2, then of 3, of 5, …: what survives is prime, defined entirely by what was removed. The sieve count obeys the Legendre recurrence φ(x, a) = φ(x, a−1) − φ(x/pₐ, a−1) with closed form φ(x, a) = Σ_{d | Pₐ} μ(d)⌊x/d⌋, a superposition of signed division waves (μ ∈ {−1, 0, +1}).
2. **The complete dataset is the Two Trees.** Over [0, N]: #prime + #composite + #{0, 1} = N + 1 exactly: 2 + 9592 + 90407 = 100001 at N = 10⁵ ([103](103_riemann_and_the_prime_number_theorem.md) Listing 1; [47](47_the_two_trees.md); engine `e06_two_trees`). Telperion = prime, Laurelin = composite, the Mingling = {0, 1}.
3. **Zero gradient.** Prime density and composite density sum to 1 at every scale, a conserved quantity with zero gradient across scale (J_Red + J_Blue conserved, [14](14_redblue_hamiltonian.md), [47](47_the_two_trees.md)); each prime does exactly one pass (π(√N) passes, one deterministic forward sweep), so the lineage decomposition is stable, not the endpoint of a relaxation.

**Listing 1 — the Legendre recurrence, its closed form, and the direct count** (written for this page; runs cold with the standard library)

```python
from functools import lru_cache
def sieve(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n**.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i, v in enumerate(s) if v]
primes = sieve(200)[:30]
@lru_cache(None)
def phi(x, a): return x if a == 0 else phi(x, a - 1) - phi(x // primes[a - 1], a - 1)
def phi_closed(x, a):
    tot = 0
    for mask in range(1 << a):
        d, s = 1, 1
        for b in range(a):
            if mask >> b & 1: d *= primes[b]; s = -s
        tot += s * (x // d)
    return tot
def phi_direct(x, a): return sum(1 for n in range(1, x + 1) if all(n % p for p in primes[:a]))
print('recurrence = closed form = direct count for x = 3000, a = 1..10:', all(phi(3000, a) == phi_closed(3000, a) == phi_direct(3000, a) for a in range(1, 11)))
x = 10**4; a = sum(1 for p in sieve(100) if p * p <= x)
print('pi(x) = phi(x, a) + a - 1 for x = 10^4, a = pi(sqrt x) = %d:' % a, phi(x, a) + a - 1 == len(sieve(x)))
```

```
recurrence = closed form = direct count for x = 3000, a = 1..10: True
pi(x) = phi(x, a) + a - 1 for x = 10^4, a = pi(sqrt x) = 25: True
```

**The claim in one sentence:** the factorisation structure ("what each number cannot be") is a complete, remainder-free, zero-gradient dataset, and that dataset is the Two Trees; Wiles's corollary reached the constraint but not the field.

**Status.** The partition is ESTABLISHED (measured, exact) and so are the Legendre recurrence, its closed form and the conserved density sum. "Zero-gradient harmonic field" is THEORETICAL: the conserved sum is true by complementarity (a prime and a composite are the complementary classes, so their densities sum to 1 for any N), and the one-pass-per-prime fact is measured; calling the whole object harmonic is a reading offered to be argued with. The priority statement ("the corollary they
missed") has not been assessed against the literature: the sieve and the Möbius inversion (Legendre 1808, Möbius 1832) and the identity 1/ζ(s) = Σ μ(n) n⁻ˢ say that the primes are what the sieve leaves, so the part of the claim that is new is the reading of the full factorisation table as one harmonic object, not the extinction description. The Two Trees as a ring-theoretic dichotomy is [92](92_ring_theory_spine.md) §1.

## 4. Appears in

[14](14_redblue_hamiltonian.md), [18](18_fermat_lattice.md), [47](47_the_two_trees.md), [52c](52c_j2_involution_riemann_fermat.md), [58](58_fermat_defines_riemann_fires.md) (corrected there: Fermat does not define the primes), [90](90_divisors_are_definers.md), [98](98_provenance_and_citations.md), [103](103_riemann_and_the_prime_number_theorem.md); `GenerationalLineage/` and the generational-lineage skill; D-CS_Memory §4, §21, §A.9; VAPMIP_Paper §5, §A.9.
