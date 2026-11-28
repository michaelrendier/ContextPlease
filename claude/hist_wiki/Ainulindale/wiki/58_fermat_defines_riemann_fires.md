# 58 — Two Operations: an Ordinal Order and a Firing Order

| | |
|---|---|
| Scope | the claim "Fermat defines the primes, Riemann fires them"; the engine's firing order (ascending |v[k]|); what the explicit formula does and does not order |
| Origin | 2026-06-13 cascade capture; title kept from the original ("Fermat defines. Riemann fires.") |
| Code | `ptol.c` / `ptol_layer.py` (the spiral order = ascending |v[k]|), `VAPMIP/monad.py` (Dirichlet projection) |
| Confidence | the explicit formula and the primes' definition: ESTABLISHED · the engine's firing order as a measured property of the projection: `MEASURED` (recorded output, not re-run here) · "the engine's order is the Riemann spiral": `INTERPRETATION` |
| Last verified | 2026-11-13: Listing 1 executed; the "what should we call you" firing order is recorded output and was not regenerated |

## 1. Two orderings of one set

The author's statement: Fermat gives the primes in **ordinal** order (2, 3, 5, …);
the Riemann spiral gives a **firing** order, different at each input; the
difference between them carries the content of the input. The engine's side of this
is concrete and testable (§3). The mathematical side needs two corrections.

## 2. Corrections to the mathematics  `ESTABLISHED`

**Correction A. Fermat does not define the primes.** A prime is an integer > 1 with
no divisors other than 1 and itself. Fermat's Last Theorem (Wiles 1995) says
xⁿ + yⁿ = zⁿ has no positive integer solutions for n > 2; it is a statement about
equations and does not characterise the primes. If "prime" meant "not a sum of two
perfect powers", Listing 1 shows it would be wrong in both directions.

**Correction B. The explicit formula orders zeros, not primes, and not by x.**

```
ψ(x) = x − Σ_ρ x^ρ/ρ − ln 2π − ½ ln(1 − x⁻²)
```

The sum runs over the zeros ρ. At fixed x the size of one zero's term is
|x^ρ/ρ| = x^½/|ρ|. The factor x^½ is the same for every zero, so the ranking of the
zeros by contribution is the ranking by 1/|ρ|, which is the order of increasing
height γ. **It does not change with x.** The earlier text said the order "changes
with x" and is "not the ordinal order"; for the amplitudes of the explicit formula
the order is the fixed ordinal order of the zeros. Listing 1 confirms this.

**Listing 1 — the two corrections** (written for this page; needs mpmath; runs cold)

```python
import mpmath as mp
zs = [mp.zetazero(k).imag for k in range(1, 21)]
def order(x):
    amp = [abs(mp.mpf(x) ** (0.5 + 1j * t) / (0.5 + 1j * t)) for t in zs]   # |x^rho / rho|
    return sorted(range(1, 21), key=lambda k: -amp[k - 1])
base = order(10)
print('rank order of |x^rho/rho|, largest first, x = 10:', base)
print('same for every x in 2..1e12 ?', all(order(x) == base for x in (2, 3, 7, 100, 1e4, 1e8, 1e12)))
N = 200
pw = {x**l for x in range(1, 15) for l in range(2, 9) if x**l < N}
express = {a + b for a in pw for b in pw if a + b <= N}
isp = lambda n: n > 1 and all(n % d for d in range(2, int(n**.5) + 1))
P = [n for n in range(2, N + 1) if isp(n)]
print('primes <= 200 that ARE a sum of two perfect powers:', [p for p in P if p in express])
print('composites <= 200 that are NOT (first 12):', [n for n in range(4, N + 1) if not isp(n) and n not in express][:12])
```

```
rank order of |x^rho/rho|, largest first, x = 10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
same for every x in 2..1e12 ? True
primes <= 200 that ARE a sum of two perfect powers: [2, 5, 13, 17, 29, 31, 37, 41, 43, 53, 59, 61, 73, 89, 97, 101, 109, 113, 127, 137, 149, 157, 173, 181, 193, 197]
composites <= 200 that are NOT (first 12): [4, 6, 14, 15, 21, 22, 27, 30, 38, 39, 42, 46]
```

Twenty-six of the primes up to 200 are sums of two perfect powers (5 = 1²+2²,
13 = 2²+3²), and composites such as 6, 14, 15 are not. The set "not a sum of two
perfect powers" is therefore a different set from the primes.

## 3. The engine's firing order  `MEASURED` (recorded output)

The engine does produce an input-dependent order, and it comes from a different
place from the explicit formula. The Dirichlet projection

```
x_k = Σ_i c_i · i^(−½) · cos(2πi / P[k])        P[k] = the 16 primes 2 … 53
```

gives sixteen values |v[k]| that depend on the input coefficients cᵢ. Sorting by
ascending |v[k]| is the "spiral order" the SVG draws. For the recorded prompt
"what should we call you" the ordinal order is k = 0 (p = 2), 1 (3), 2 (5), 3 (7) … and the
firing order began k = 5 (p = 13), 3 (p = 7), 0 (p = 2), 10 (p = 31) … 14 (p = 47),
15 (p = 53), ending on e₁₅ at +0.558 with the word "mandating". Those are the
values as recorded on 2026-06-13; this pass did not regenerate them (the engine
call needs the English monad file and the prompt-to-coefficient step of
`ptol_layer.py`).

What can be said without them: the order is set by the cᵢ and the cosines. It is a
property of the projection, and it carries information about the input exactly as a
spectrum does. That is the substance of the author's point, and it is
independent of any claim about ζ.

## 4. What stays, and the status

| Statement | Status |
|---|---|
| A prompt's projection onto 16 prime-indexed cosines gives an input-specific order of the sixteen primes | `MEASURED` |
| The departure of that order from 2, 3, 5, … is the content the engine reads | `INTERPRETATION` (a design reading; no information measure is computed) |
| The order is "the Riemann spiral for this x" | `NOT SUPPORTED`: the explicit-formula order is fixed (Listing 1); the engine order comes from the cosine kernel and the cᵢ |
| "Fermat defines the primes" | corrected (Correction A); the primes are defined by divisibility |
| The Fermat near-miss shows the truncated spiral firing wrongly | `INTERPRETATION`; the near-miss is an arithmetic coincidence at 10 digits ([56](56_telescope_caustic_zeno.md) Listing 1), not a spiral output |

## 5. Related pages

[51 the J₂ involution and quantised Fermat](52c_j2_involution_riemann_fermat.md) ·
[55 index not value](55_index_not_value.md) · [57 the boundary ascending](57_boundary_ascending.md) ·
[62 caustics](62_hands_on_paper_minds_eye_caustic.md) · [133 canonical maths](133_canonical_maths.md)
