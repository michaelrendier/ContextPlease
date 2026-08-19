# Residue sieving and digit-window factoring: the exact bounds — 2026-08-08

**Asked (Cody):** the last digits of an RSA modulus constrain the last digits of
its prime factors. How much computational overhead does that pre-check remove?
Can the geometries be designed so the computation runs "downhill"? The Go
analogy: remove the illegal moves and the number drops — how far does it drop
here?

**Verdict: it removes none.** Three separate mechanisms were tested; all three
are real named techniques, and all three are bounded well short of useful.
Recorded because a negative result with an exact bound belongs in an appendix.

## `sieve_bounds.py`

**1. Last-digit constraint: reduction factor exactly 1.000×.** Not small —
*none*. For any modulus m coprime to N, q ≡ N·p⁻¹ (mod m) is **determined** by
p. The constraint binds the *pair* and is satisfied automatically for every
candidate p. Verified at m = 10, 100, 1000: all 4 / 40 / 400 unit residues
survive.

**2. What does help: wheel factorization.** Density of candidates coprime to
all primes ≤ B is ∏(1−1/p) → e^(−γ)/ln B (Mertens).

| sieve primes ≤ | density | speedup |
|---|---|---|
| 10 | 0.229 | 4.4× |
| 100 | 0.120 | 8.3× |
| 10⁶ | 0.041 | 24.6× |

The whole family is bounded by ~1/ln B — logarithmic. Sieving every prime under
a billion buys ~37×.

**3. Scale.** RSA-2048: naive 10³⁰⁵ candidate primes, GNFS ~10³⁵ operations.
GNFS already buys 10²⁷⁰ orders of magnitude; the best possible residue sieve
buys 10^1.6 — and GNFS *already contains it* (the "sieve" in Number Field Sieve
is this technique, industrialized).

**4. Go.** 1024-bit primes 10³⁰⁵ vs Go's 10¹⁷⁰ legal positions = 1.8× the orders
of magnitude, not 5×. **The analogy breaks structurally:** Go pruning compounds
because Go is a tree ~200 plies deep, so a per-level cut multiplies. Factoring
is a *flat* search in one unknown — a filter applies once, and nothing compounds.

## `digit_window.py`

**Modulus can't end in 26** — two odd primes give an odd product; N ends in
1, 3, 7, or 9.

**The core misconception:** last digits multiply **mod 100**, i.e. they *wrap*.
Integer factorization of the residue is not preserved.

    211 × 311 = 65621        both prime
    N ends in 21 (= 3 × 7), but p and q both end in 11.
    11 × 11 = 121 → wraps to 21.

Exhaustively: for *every* target ending, all 40 residues coprime to 100 remain
possible for p.

**The digit-window / Hensel lifting idea.** With p = p_k + a·10^k and
q = q_k + b·10^k, matching one further digit of N gives

    a·q_k + b·p_k ≡ (N − p_k·q_k)/10^k   (mod 10)

**One equation, two unknowns.** Branching factor 10 per decimal digit (2 per
bit), nothing pruned: 10³⁰⁹ leaves = the brute-force count unchanged.

> **Generalization worth keeping:** there is no equation in p alone. N gives one
> equation in two unknowns, and every derived constraint inherits that. The only
> way to get an equation in p by itself is to factor.
>
> Same shape as the 2026-08-08 sedenion result: the diagonal blocks
> L_a, R_a are norm-determined and carry nothing; all information lives in the
> **coupling** between the halves and cannot be decoupled.

**Where partial digits genuinely do work: Coppersmith (1996).** Knowing the low
or high **half** of p's bits factors N in polynomial time via lattice reduction.
RSA-2048 needs ~154 of p's ~308 digits. The threshold is sharp — below half,
nothing. Two digits is not a partial win; it is below the point where the method
has traction.

## On "can we make it downhill?"

A downhill structure is *equivalent to* a polynomial-time factoring algorithm —
not an obstacle to this approach specifically, but the definition of the problem.
The precise obstruction: **multiplication destroys locality.** Change p by 1 and
N changes by q ≈ 10³⁰⁸. No metric on candidates makes a near-miss measurably
"warmer" — trial division gets no signal from a candidate off by one versus one
off by 10³⁰⁰. That is what one-way means operationally, and it is why no imposed
geometry yields a slope: any geometry must be computed from N, and N carries no
local information.

## Also settled here

Counting information ≠ factoring information. Granting RH outright gives no
factoring advantage — it sharpens error terms in π(x) and gives deterministic
Miller primality under GRH, but the distribution of primes and the factorization
of a specific N are decoupled.
