# 99 — Emmy Noether: the mathematics this framework uses

**Companion to** [43_emmy_noether_sedenion.md](43_emmy_noether_sedenion.md)
(the naming decision) and [98_provenance_and_citations.md](98_provenance_and_citations.md).
This page states, precisely, which of Emmy Noether's results are load-bearing
here and where each is invoked — so the dependence is citable, not gestural.

> *"I do not see that the sex of the candidate is an argument against her
> admission as Privatdozent. After all, we are a university, not a bathing
> establishment."* — David Hilbert, Göttingen faculty meeting, 1915.

---

## Two theorems, both used

### 1. Noether's theorem — [Noether1918]

**Noether, E. (1918). *Invariante Variationsprobleme.* Nachr. d. König.
Gesellsch. d. Wiss. zu Göttingen, Math.-phys. Klasse, 235–257.**
English: Tavel transl. (1971), *Transport Theory and Statistical Physics*
1(3), 183–207 — arXiv:physics/0503066.

Every continuous symmetry of the action produces a conserved current,
`∂_μ Jᵘ = 0`.

**Where it is load-bearing:**
- The functional equation `ξ(s) = ξ(1−s)` is a continuous symmetry of the action
  `L_dynamic = ∫ J_red · J_blue ds`. Its conserved boundary current is `J₃`. The
  unique point where all three currents satisfy `∂_μ Jᵘ = 0` is `σ = ½` — so the
  critical line is a **Noether consequence, not an assumption**. (D-CS_Memory
  §5, §42; wiki/05, wiki/06.)
- `R̂† = B̂` (Red and Blue adjoint) is the operator form of the same symmetry.
- The failed-prediction record is `J_blue`: the reverse current of every forward
  prediction. Conservation is why it must be kept.

**What is NOT claimed:** that σ = ½ has been *proved* to be forced by Noether
balance for ζ. The proof path is written (D-CS_Memory §42, companion D-M) and
step 3 is equivalent to RH. Stated as OPEN.

### 2. Noether's ring theory — [Noether1921]

**Noether, E. (1921). *Idealtheorie in Ringbereichen.* Mathematische Annalen
83(1–2), 24–66.** DOI:10.1007/BF01464225.

The ascending chain condition (Noetherian rings); the isomorphism theorems for
rings; primary decomposition (Lasker–Noether).

**Where it is load-bearing:**
- The Emmy Noether Sedenion 𝕊_EN is a **ring**, and its ideal structure is
  finite and tractable *because it is Noetherian*. Every decomposition of 𝕊_EN
  into subalgebras / ideals / quotients uses her isomorphism theorems.
- The zero divisors are **ideals in her sense**, not pathologies — the
  zero-divisor set is a union of associated primes (primary decomposition). This
  is the "ring-theory spine": *an element falls ⟺ its quotient ring has zero
  divisors* (wiki/92; `SedenionFactoralRelativity/engine/lineage.py` G1–G6).
- `Ω(n)` (prime-factor count with multiplicity) = the length of a number's
  **generational lineage** — a primary-decomposition datum, not a statistic.

Scholarly edition & history: **[Kosmann2011]** Kosmann-Schwarzbach, Y. (2011).
*The Noether Theorems: Invariance and Conservation Laws in the Twentieth
Century.* Springer.

---

## Why the algebra carries her name

Historical, from wiki/43: Noether proved the theorem (1918) that is the spine
of D-M and D-P; built the abstract ring theory (1920s) that makes the sedenion
tractable; lectured under Hilbert's name because Göttingen would not let her
lecture under her own; was expelled in 1933; died at 53 at Bryn Mawr, two years
into her first real academic appointment. The 16-D Cayley–Dickson algebra is
named the **Emmy Noether Sedenion** across all papers in the series.

Tribute material: `Ainulindale/tribute/Emmy_Noether_Deep_Dive.txt`,
`Ainulindale/tribute/Emmy_Noether_Masters_Tribute.txt`.

---

## Appears in

wiki/05, wiki/06, wiki/43, wiki/47, wiki/61, wiki/92; D-CS_Memory §5, §19, §42,
§A.9; VAPMIP_Paper §"Engine 05–06"; every conservation-law claim in the series.
