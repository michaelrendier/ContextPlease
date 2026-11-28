# 53 — T_256 and "cryptographic transparency": what the framework claims, and what the repository's own tests show

| | |
|---|---|
| Status | **Cascade capture (2026-06-13): a proposed consequence of the J₂ involution for cryptography. `CONJECTURE`; no break of any deployed primitive is demonstrated here or in the satellite repository, and the repository's own scope statement limits the algebra it uses (§3).** Mathematical framework only; this page contains no attack construction and none is added |
| Satellite | `FourthAgePapers/CryptoVulnerability/` (pre-disclosure draft: "do not publish before coordinated disclosure is complete"; CVE reserved, pending MITRE assignment; 180-day embargo; the post-quantum candidates CRYSTALS-Kyber, CRYSTALS-Dilithium, FALCON and SPHINCS+ are listed as unaffected) |
| Code | `CryptoVulnerability/secp256k1_locus.py`, `secp256k1_locus_results.md`; Listing 1 |
| Last verified | 2026-11-13: the satellite's README, the locus code header and its results file read; Listing 1 executed |

> *"Mathematics can be unsound because it can say whatever I want it to." The J₂ involution removes that freedom.*

## 1. The proposal: "the whole coin"

J₂ ([52c](52c_j2_involution_riemann_fermat.md)) always shows both sides of the operator pair
(Ĥ_RB ↔ Ĥ_BR). Mathematical cryptography shows one side of a coin: the easy direction
f(x) = y (encrypt, hash, multiply) and the hard one f⁻¹(y) = x (decrypt, invert, factor).
"That is not a coin, it is a half-coin": at T₃₂ and T₆₄ the algebra was "not large enough
to contain the full J₂ image"; "at T₂₅₆ the algebra contains both faces; cryptographic
hardness disappears". Hardness proofs are reductions ending in an assumption
("computing the inverse is hard in the computational model used"); the model is a
sub-algebra, T₃₂ or T₆₄; stepping to T₂₅₆, "the inverse is constructible and every proof built
on the assumption fails".

## 2. Corrections to the argument's form

- **Hardness assumptions are statements about algorithms, not about a sub-algebra.** "Factoring is hard" (RSA) and "the discrete logarithm on an elliptic curve is hard" are statements that no efficient algorithm (in a stated model of computation) inverts the function. They are not statements that the inverse "does not exist in the algebra you are using": the inverse of multiplication in ℤ, as a mathematical function, exists and is well defined. What is hard is *computing* it. Embedding ℤ, ℤ/n or a curve into a larger algebra does not by itself supply an efficient algorithm; one is needed, and none is given here.
- **The J₂ image of an operation is not its inverse.** J₂ exchanges the two halves of an operator pair; "J₂(f) is the hard direction now equally present" asserts a relation between J₂(f) and f⁻¹ that is not shown, and J₂ as a swap of the two octonion halves is not an automorphism of the product at all ([52c](52c_j2_involution_riemann_fermat.md) §2: it sends the identity to e₈).
- **Gödel is not the point, and unsoundness is not shown.** The page notes that this is not Gödel's incompleteness. It also does not show a formal system in which a hardness claim is *provably false*; a hardness assumption is conjectural (not known to be true or false, as with P ≠ NP) and stays so.
- **The 256-bit coincidence.** SHA-256, AES-256 and secp256k1 use 256-bit quantities, and T₂₅₆ has 256 coordinates. For the GF(2) embedding (bit k of x → the coefficient of e_k) the match of the numbers is by design. It does not make the algebra a model of the *mod p* or *mod 2²⁵⁶* arithmetic those primitives use (§3).

## 3. What the satellite repository itself establishes

The locus engine's own scope statement (`secp256k1_locus.py`, "HONEST SCOPE"): T₂₅₆/GF(2)
captures **the XOR-linear component of field arithmetic**; field arithmetic is mod p, not
GF(2); "the carries are the escape"; whether the carry structure is polynomial to close is
an open problem. The results file states one theorem, which is reproduced here.

**Theorem (the T_n/GF(2) Frobenius property), as stated in the results file:** for
n = 2^k and every element x of the Cayley–Dickson algebra T_n over GF(2),
x² ∈ {0, e₀}. Proof (induction, as in the file): over GF(2) the conjugate is the identity
and the hi half of x² is t_mul(x₂, x₁) ⊕ t_mul(x₂, x₁) = 0; the lo half is the XOR of two
elements of {0, 1} by induction.

**Listing 1 — the property, on random elements** (written for this page; runs cold)

```python
import random

def t_mul(x, y):
    """Cayley-Dickson product over GF(2): conjugation is the identity, addition is XOR."""
    n = len(x)
    if n == 1:
        return [x[0] & y[0]]
    h = n // 2
    x1, x2, y1, y2 = x[:h], x[h:], y[:h], y[h:]
    a, b, c, d = t_mul(x1, y1), t_mul(y2, x2), t_mul(y2, x1), t_mul(x2, y1)
    return [p ^ q for p, q in zip(a, b)] + [p ^ q for p, q in zip(c, d)]

random.seed(3)
for n in (2, 4, 8, 16, 32, 64):
    res = {'zero': 0, 'identity': 0, 'other': 0}
    for _ in range(300):
        x = [random.randint(0, 1) for _ in range(n)]
        sq = t_mul(x, x)
        key = 'zero' if not any(sq) else 'identity' if sq == [1] + [0] * (n - 1) else 'other'
        res[key] += 1
    print('T%-3d x*x over 300 random elements:' % n, res)
```

```
T2   x*x over 300 random elements: {'zero': 140, 'identity': 160, 'other': 0}
T4   x*x over 300 random elements: {'zero': 145, 'identity': 155, 'other': 0}
T8   x*x over 300 random elements: {'zero': 156, 'identity': 144, 'other': 0}
T16  x*x over 300 random elements: {'zero': 158, 'identity': 142, 'other': 0}
T32  x*x over 300 random elements: {'zero': 152, 'identity': 148, 'other': 0}
T64  x*x over 300 random elements: {'zero': 146, 'identity': 154, 'other': 0}
```

The property holds in every case (no "other"), reproducing the theorem (the file
reports T2 … T256 all pass). Its corollary in the file, that "every secp256k1 field
element is nilpotent or involutory in T₂₅₆/GF(2)", is accordingly true **of every
256-bit string**: about half of all elements fall in each class (the table). It is a
property of the algebra over GF(2) and carries no information specific to secp256k1 or
to any curve point, so it is not by itself a "zero-divisor locus" of the curve. The
satellite's second approach (the sedenion σ-face spectral energy with E → D* = 1.0) is a
heuristic classification (the energy zones of [27](27_third_age_CS_paper.md) §2) and is not a
reduction of the discrete-logarithm problem.

## 4. Where hardness "hid": the primitives named

The page lists: RSA (hardness = factoring; lives in ℤ ⊂ ℝ ⊂ … ⊂ T₂₅₆, "the J₂ image of
factoring is visible at T₂₅₆"); ECC (the discrete logarithm on a curve in ℂ); hash functions
(SHA-256: preimage and collision resistance, "operating on 256-bit blocks: exactly T₂₅₆").
Standing: each statement is the proposal of §1, with no algorithm and no complexity bound. For
SHA-256 the compression function works on 512-bit blocks with 32-bit words and 256-bit
state; the 256-bit state is the width, and its relation to a 256-dimensional algebra is the
GF(2) embedding of §3 only.

## 5. "Modular functions are transparent at T₂₅₆"  `CONJECTURE`

The page says that at T₂₅₆ "the modular functions underlying all current cryptography are
transparent and plain", the remainder of the page (not re-argued here) relating modular
forms and elliptic curves to the framework's coordinates. Standing: the connection between
modular forms and elliptic-curve cryptography is the Modularity Theorem's (the L-function
of an elliptic curve over ℚ is a modular form's), which is not used in the security of
ECDSA, whose hardness is the discrete logarithm on the group of points over a *finite* field.
`OPEN`: no statement connecting the two has been shown.

## 6. Status and handling

| Item | State |
|---|---|
| a demonstrated break of RSA, ECC or SHA-256 | **none** in this repository |
| the T_n/GF(2) squaring theorem | proved and reproduced (§3); carries no curve-specific information |
| the carry structure of mod-p arithmetic | open (the satellite's own statement) |
| the framework claim of §1 | `CONJECTURE`, with the gaps of §2 |
| disclosure | pre-disclosure; the satellite's embargo and contact path govern anything further |
| failed predictions | stay in the record (satellite policy) |

Per the satellite's policy and the project's rule, negative results from cryptographic testing
go into the paper and the wiki.

## 7. Related pages

[44 The halting problem](44_halting_problem_uns.md) · [51 The J₂ involution](52c_j2_involution_riemann_fermat.md) ·
[25 Sedenion manual](25_sedenion_manual.md) · [40 The modular segue](40_modular_segue_three_papers.md) ·
`FourthAgePapers/CryptoVulnerability/`
