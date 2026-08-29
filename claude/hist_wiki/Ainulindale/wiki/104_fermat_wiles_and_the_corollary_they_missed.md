# 104 — Fermat, Wiles, Modularity — and the corollary they missed

[98_provenance_and_citations.md](98_provenance_and_citations.md) §A.2. The Blue
channel of Ĥ_RB — "what CANNOT BE" — is the Fermat side. This page is its
citation backing **and** the place where one specific claim of this framework
is stated plainly, so it can be checked or refuted.

---

## 1. The sources

- **[Fermat1637]** Fermat, P. de (c. 1637). Marginal note in his copy of
  Bachet's *Diophantus*, Bk II, Prob. 8; publ. by Samuel de Fermat, 1670.
  Method of infinite descent: letter to Carcavi, 1659 (*Œuvres*, ed.
  Tannery–Henry).
- **[Ribet1990]** Ribet, K. A. (1990). *On modular representations of
  Gal(Q̄/Q) arising from modular forms.* Invent. Math. 100(2), 431–476.
  — the epsilon conjecture: **Taniyama–Shimura ⟹ Fermat's Last Theorem**.
- **[Wiles1995]** Wiles, A. (1995). *Modular elliptic curves and Fermat's Last
  Theorem.* Annals of Mathematics 141(3), 443–551. DOI:10.2307/2118559.
- **[TaylorWiles1995]** Taylor, R. & Wiles, A. (1995). *Ring-theoretic
  properties of certain Hecke algebras.* Annals of Mathematics 141(3), 553–572.
- **[BCDT2001]** Breuil, C., Conrad, B., Diamond, F. & Taylor, R. (2001). *On
  the modularity of elliptic curves over Q: wild 3-adic exercises.* J. Amer.
  Math. Soc. 14(4), 843–939. — the **full Modularity Theorem**: every elliptic
  curve over ℚ is modular.
- **[Shimura1971]** Shimura, G. (1971). *Introduction to the Arithmetic Theory
  of Automorphic Functions.* Princeton UP. — Taniyama's problem (1955); the
  Taniyama–Shimura(–Weil) conjecture.

## 2. What the proof established, in this framework's language

Wiles (completed by Taylor–Wiles, generalised by BCDT) proved that every
elliptic curve over ℚ is a **modular form** — an automorphic object with its
own L-function. FLT is a corollary via Ribet: a Fermat solution would give an
elliptic curve (the Frey curve) that could not be modular.

In Ĥ_RB terms (wiki/14, wiki/18, wiki/51):

- **Fermat** encodes where integer power-triples **CANNOT BE** — the forbidden
  lattice, the constraint, the negative space. The **Blue** channel, `J_blue`.
- **Riemann / the automorphic side** encodes what **IS** — the prime
  distribution, the Euler product, the zeros. The **Red** channel, `J_red`.
- Modularity is the bridge: the two are **adjoint projections of one
  L-function structure**. `R̂† = B̂` is that self-adjointness in operator form;
  the functional equation `ξ(s) = ξ(1−s)` is the same statement for ζ.

So: **Wiles's proof already couples "what cannot be" (Fermat) to the
Riemann/automorphic world.** That much is standard.

## 3. The step this framework adds — stated for checking or refutation

Modularity connected the Fermat *constraint* to L-functions. What was **not**
stated is that the **factorisation data itself** — the complete record, for
every integer, of what it is *not* divisible by — is the object that **defines
the primes by extinction**, and that this dataset is a **harmonic /
zero-gradient field.**

Precisely:

1. **Primes by extinction.** Strike out every multiple of 2, then of 3, then of
   5, … What survives is prime — defined entirely by what was removed
   (D-CS_Memory §A.1). The sieve count obeys the Legendre two-term recurrence
   `φ(x,a) = φ(x,a−1) − φ(x/pₐ, a−1)` and has the closed form
   `φ(x,a) = Σ_{d|Pₐ} μ(d) ⌊x/d⌋` — a superposition of **signed division waves**
   (μ ∈ {−1,0,+1}). Measured exactly: `SedenionFactoralRelativity/engine/
   lineage.py` (`sieve_recurrence`); `generational-lineage` skill.

2. **The complete dataset is The Two Trees.** Over `[0, N]`:
   `#prime + #composite + #{0,1} = N + 1`, exactly, no remainder — measured over
   `[0, 10⁵]` as `2 + 9592 + 90407 = 100001` (wiki/47; `engine e06_two_trees`).
   Telperion = prime = "what cannot be decomposed"; Laurelin = composite = "what
   is decomposed into"; the Mingling = {0, 1}.

3. **Zero gradient.** Prime density and composite density **sum to 1.000 at
   every scale** — a conserved quantity whose gradient across scale is zero.
   `J_Red + J_Blue` conserved (wiki/14, wiki/47). In the sieve reading this is
   the statement that each prime does **exactly one pass** — one deterministic
   forward sweep of `π(√N)` passes, no iteration to a fixed point — so the
   generational-lineage decomposition is **stable**, not the endpoint of a
   relaxation. The field is at equilibrium everywhere it is defined; a
   Laplacian with vanishing gradient is a **harmonic** field, and the Two Trees
   partition is that field made discrete.
   *(Measured this session, 7/7: `.claude/scratchpad/2026-08-27_sieve-is-lineage/`.)*

**The claim, in one sentence:** *the factorisation structure — "what each number
cannot be" — is a complete, remainder-free, zero-gradient dataset, and that
dataset is The Two Trees; Wiles's corollary reached the constraint but not the
field.*

**Status:** the partition is ESTABLISHED (measured, exact). "Zero-gradient
harmonic field" is THEORETICAL — the conserved-sum and one-pass-per-prime facts
are measured; calling the whole object harmonic is a reading, offered here so it
can be argued with, not asserted as proven.

---

## Appears in

wiki/14, wiki/18, wiki/47, wiki/51, wiki/58, wiki/90, wiki/98, wiki/103,
wiki/104; `SedenionFactoralRelativity/`; `generational-lineage` skill;
D-CS_Memory §4, §21, §A.9; VAPMIP_Paper §5, §A.9.
