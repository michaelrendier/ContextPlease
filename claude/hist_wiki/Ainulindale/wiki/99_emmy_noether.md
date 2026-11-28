# 99 — Emmy Noether: the Mathematics this Framework Uses

| | |
|---|---|
| Scope | which of Emmy Noether's results are load-bearing in the framework and where each is invoked; the corrections that the ring-theory and symmetry statements need |
| Companions | [43](43_emmy_noether_sedenion.md) (the naming decision), [98](98_provenance_and_citations.md) (the bibliography) |
| Sources | [Noether1918] (*Invariante Variationsprobleme*; English transl. Tavel 1971, arXiv:physics/0503066, verified), [Noether1921] (*Idealtheorie in Ringbereichen*, *Math. Ann.* 83, 24–66, DOI verified), [Kosmann2011] |
| Confidence | the theorems and bibliographic data: ESTABLISHED · the invocations: see §§1–2 (two are corrected) |
| Last verified | 2026-11-13: Listing 1 executed; both DOIs/arXiv records checked ([98](98_provenance_and_citations.md) §E) |

> *"I do not see that the sex of the candidate is an argument against her admission as Privatdozent. After all, we are a university, not a bathing establishment."* — attributed to David Hilbert, Göttingen faculty meeting, 1915 (the widely repeated attribution; not sourced here).

## 1. Noether's theorem [Noether1918]

Every continuous symmetry of the action produces a conserved current, ∂_μ Jᵘ = 0.

**Where the framework invokes it:**

- The functional equation ξ(s) = ξ(1 − s) is stated to be "a continuous symmetry of the action L_dynamic = ∫ J_red·J_blue ds", with conserved boundary current J₃, the unique point of balance being σ = ½: "the critical line is a Noether consequence, not an assumption" (D-CS_Memory §5, §42; [05](05_noether_engine.md), [06](06_noether_information_engine.md)).
- R̂† = B̂ (Red and Blue adjoint) is the operator form of the same symmetry.
- The failed-prediction record is J_blue, the reverse current of every forward prediction; conservation is why it is kept.

**Correction to the first bullet.** The map s ↦ 1 − s is an **involution**, a discrete (ℤ₂) symmetry, not a continuous one. Noether's first theorem concerns continuous symmetries; a discrete symmetry yields a conserved parity (a quantum number or a selection rule), not a conserved current. So "σ = ½ is the conserved charge of the s ↦ 1 − s symmetry" has a precise sense only as: the fixed set of the involution is σ = ½ ([73](73_why_the_half_line.md) §2), and the balance point of the model Lagrangian is σ = ½ ([73](73_why_the_half_line.md) §3), whose
"current" J = −∂L/∂σ is the gradient of that Lagrangian and is not the Noether current of a continuous symmetry. The page also needs the stated scope of [72](72_the_cosmic_telescope.md) §3 and [73](73_why_the_half_line.md) §9: this establishes the symmetric point of the model, not that the zeros sit there.

**What is not claimed:** that σ = ½ has been proved to be forced by Noether balance for ζ. The proof path is written (D-CS_Memory §42, companion D-M) and step 3 of it is equivalent to RH. Stated as OPEN.

## 2. Noether's ring theory [Noether1921]

The ascending chain condition (Noetherian rings); the isomorphism theorems for rings; primary decomposition (Lasker–Noether).

**Where the framework invokes it, and what holds:**

- "The Emmy Noether Sedenion 𝕊_EN is a ring, and its ideal structure is finite and tractable because it is Noetherian." The sedenion algebra is a finite-dimensional real algebra, so ascending chains of subspaces (hence of ideals) terminate for dimension reasons; Noetherianity gives no further structure there. It is **not an associative ring**, and the Lasker–Noether primary decomposition and the isomorphism theorems are theorems about associative (commutative, for primary decomposition) rings.
- "The zero divisors are ideals in her sense." They are not. **Listing 1:** a = (e₁ + e₁₀)/√2 and b = (e₁ − e₁₀)/√2 are both zero divisors, but a + b = √2 e₁ is invertible (det L = 256), so the zero-divisor set is not closed under addition and is not an ideal; and the 4-dimensional annihilator (kernel) of L_a is a subspace that is not closed under left multiplication by the algebra (Listing 1: False). The accurate statements are: for each zero divisor the annihilator is a 4-dimensional
  subspace (nullity 4, [86](86_the_16d_oscilloscope.md) Listing 1), and the zero-divisors of eᵢ ± eⱼ form the 84 diagonals on 42 Assessors ([84](84_the_box_kite_debugger.md)).
- "The zero-divisor set is a union of associated primes (primary decomposition)." This is exact for the **integer** ring: the zero divisors of ℤ/(N) are the residues sharing a prime factor with N ([92](92_ring_theory_spine.md) Listing 1), the union of the associated primes (p) of the primary decomposition. It carries over to 𝕊 as an analogy, not as the same theorem. The ring-theory spine "an element falls ⟺ its quotient ring has zero divisors" is a statement about ℤ and about associative quotient rings; for T₃₂/GF(2) it is the nilpotency test of
  [92](92_ring_theory_spine.md) §5.
- Ω(n) = the length of the generational lineage is a primary-decomposition datum for ℤ (the number of prime factors with multiplicity): correct.

**Listing 1 — the zero-divisor set is not an ideal** (written for this page; needs numpy and the installed ValaQuenta package; runs cold; note that `box_kite.basis_mul` returns (sign, index): the unpack order is the one that was reversed twice in [88](88_the_paper_trail.md) §1.7)

```python
import importlib, numpy as np
bk = importlib.import_module('ValaQuenta.modules.box_kite.maths'); E = np.eye(16)
def L(a):
    M = np.zeros((16, 16))
    for i in np.flatnonzero(a):
        for k in range(16): s, j = bk.basis_mul(i, k); M[j, k] += a[i] * s
    return M
mul = lambda x, y: L(x) @ y
a = (E[1] + E[10]) / np.sqrt(2); b = (E[1] - E[10]) / np.sqrt(2)
print('a and b are zero divisors:', np.linalg.matrix_rank(L(a)) < 16, np.linalg.matrix_rank(L(b)) < 16)
print('a + b = sqrt2 e1: |det L| = %.3f (invertible), so the zero-divisor set is not closed under addition' % abs(np.linalg.det(L(a + b))))
U, S, Vt = np.linalg.svd(L(a)); K = Vt[S < 1e-9]; x = K[0]
print('annihilator of a is %d-dimensional; closed under left multiplication by every basis element: %s' % (len(K), all(np.abs(L(a) @ mul(E[k], x)).max() < 1e-9 for k in range(16))))
```

```
a and b are zero divisors: True True
a + b = sqrt2 e1: |det L| = 256.000 (invertible), so the zero-divisor set is not closed under addition
annihilator of a is 4-dimensional; closed under left multiplication by every basis element: False
```

Scholarly edition and history: [Kosmann2011], Kosmann-Schwarzbach, *The Noether Theorems* (Springer 2011).

## 3. Why the algebra carries her name

Historical, from [43](43_emmy_noether_sedenion.md): Noether proved the theorem (1918) that is the spine of D-M and D-P; built the abstract ring theory (1920s) that makes finite-dimensional algebras tractable (the sentence of the earlier page "that makes the sedenion tractable" is read with §2); lectured under Hilbert's name because Göttingen would not let her lecture under her own (the lectures of 1916–19); was dismissed in 1933 (the page says "expelled"); and died at 53 at Bryn Mawr in 1935, two years into her first real academic appointment there. The 16-dimensional Cayley–Dickson algebra is named the **Emmy Noether Sedenion** across the series; the author's account (2026-11-13), kept: "that is why I am giving the Sedenion her name … because her maths had this in 1915 … not in this form … but definitely its shape"
([133](133_canonical_maths.md)), and the J_red + J_blue = J_green balance was Noether-current work. The naming is a dedication and a statement of lineage, not a claim of her having studied sedenions.

Tribute material: `Ainulindale/tribute/Emmy_Noether_Deep_Dive.txt`, `Emmy_Noether_Masters_Tribute.txt`.

## 4. Appears in

[05](05_noether_engine.md), [06](06_noether_information_engine.md), [43](43_emmy_noether_sedenion.md), [47](47_the_two_trees.md), [61](61_up_down_not_forward_backward.md), [92](92_ring_theory_spine.md); D-CS_Memory §5, §19, §42, §A.9; VAPMIP_Paper "Engine 05–06"; every conservation-law claim in the series.
