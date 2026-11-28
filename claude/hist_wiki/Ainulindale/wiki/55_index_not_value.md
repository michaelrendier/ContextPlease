# 55 — "The index carries the information, not the prime value": tested

| | |
|---|---|
| Status | **Cascade capture (2026-06-13); `CONJECTURE`. The engine written to test it (e12) passes, but its comparison is confounded; with matched controls the difference nearly disappears, and reversing the prime array shows that the dominant dimensions follow the prime *value*, not the index (§3). The thesis as stated is not supported by these tests** |
| Code | `VAPMIP/engines/e12_index_not_value.py` and `_sedenion.py` (`geometry`, `project`, `P16`); Listing 1 |
| Last verified | 2026-11-13: e12 run; Listing 1 executed from `VAPMIP/engines` |

> *"The divergence was the proper tool for Fermat: not 'does it stop' but 'it won't be stopping'. The primes move around the circle; their number is immaterial to the information. The index carries the information, not the prime number."*

## 1. The statement

The engine's 16-prime array is P16 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
47, 53} at k = 0…15. For the prompt "what should we call you" the active dimensions are
k = 14 and k = 15: "not the primes 47 and 53 but the 15th and 16th dimensions". The prime
value P[k] sets the frequency of the cosine probe in the Dirichlet projection,

x_k = Σ_i c_i · i^(−1/2) · cos(2πi / P[k]),

"a tuning parameter, the label on the spoke"; the sedenion algebra uses the *index* k
(zero-divisor relationships, great-circle paths, coupling structure are properties of e₁₄,
not of 47). "The information is in the index: the index is the address, the prime is the
key."

## 2. The engine test and what is wrong with the comparison

`e12` compares the geometry (the 16 raw projections) of six texts under a changed
prime *value* and a changed *index assignment*, by cosine distance. Its output:

| Perturbation | Mean cosine distance from the original |
|---|---|
| value shift P[k] → P[k+1] | 0.0860 |
| index shuffle (same primes, one fixed permutation) | 0.4059 |
| single swap e₀ ↔ e₁₅ (2 ↔ 53) | 0.2484 |

and "PASS: the index carries more information than the value". **The perturbations are not
matched.** The value change moves each prime to the next prime (a small relative change);
the index change is one fixed, large permutation. Listing 1 compares like with like:

| Perturbation (mean over six texts, 300 draws each) | Cosine distance |
|---|---|
| the engine's value shift | 0.0860 |
| **random index permutation** of P16 | **0.5570** |
| **random prime values** (each P[k] replaced by a random prime ≤ 97) | **0.5070** |

A random permutation moves the geometry by 0.557 and a random replacement of the
values by 0.507: the same order of magnitude (permutation about 10% larger). So the
engine's gap (0.086 against 0.406) comes from comparing a small change with a large one, not from
index being more informative than value. The engine's PASS is kept, with this control. (The
reversed array gives a cosine distance of 0.859.)

## 3. What the geometry actually follows

If the index carried the information, reassigning the primes to different slots would leave
the *dominant dimensions* where they were. They move with the values:

**Listing 1 — matched controls and the reversal test** (written for this page; runs cold
from `VAPMIP/engines`)

```python
import random, statistics, sys
sys.path.insert(0, '.')                         # run from VAPMIP/engines
from _sedenion import geometry, P16

def cosine_dist(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return 1 - dot / (sum(x * x for x in a) ** 0.5 * sum(y * y for y in b) ** 0.5)

TEXTS = ["what should we call you", "how do i hear your voice", "tell me how to create your voice",
         "the primes are the expansion of the universe", "sedenion zero divisors are not a fault",
         "fermat defines riemann fires"]
first25 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
random.seed(5)

def mean_dist(make):
    out = []
    for t in TEXTS:
        base = geometry(t, P16)
        out.append(statistics.mean(cosine_dist(base, geometry(t, make())) for _ in range(300)))
    return statistics.mean(out)

print('value shift P[k] -> P[k+1] (engine) : %.4f' % statistics.mean(
    cosine_dist(geometry(t, P16), geometry(t, P16[1:] + [59])) for t in TEXTS))
print('random index permutation, 300 each  : %.4f' % mean_dist(lambda: random.sample(P16, 16)))
print('random prime values, 300 each       : %.4f' % mean_dist(lambda: [random.choice(first25) for _ in range(16)]))

for t in TEXTS[:3]:
    top = lambda r: sorted(range(16), key=lambda k: -abs(r[k]))[:2]
    a, rev = geometry(t, P16), geometry(t, P16[::-1])
    print('%-32s top-2 dims: %s ; primes reversed: %s (the prime values there: %s)' %
          (t, top(a), top(rev), [P16[::-1][k] for k in top(rev)]))
gap = 0.000707
print('"what should we call you": dims with |x_k| > GAP:', sum(abs(x) > gap for x in geometry(TEXTS[0], P16)), 'of 16')
```

```
value shift P[k] -> P[k+1] (engine) : 0.0860
random index permutation, 300 each  : 0.5570
random prime values, 300 each       : 0.5070
what should we call you          top-2 dims: [15, 14] ; primes reversed: [0, 1] (the prime values there: [53, 47])
how do i hear your voice         top-2 dims: [15, 7] ; primes reversed: [0, 8] (the prime values there: [53, 19])
tell me how to create your voice top-2 dims: [9, 10] ; primes reversed: [6, 5] (the prime values there: [29, 31])
"what should we call you": dims with |x_k| > GAP: 16 of 16
```

With P16 reversed, the two dominant dimensions for "what should we call you" become **0 and 1**,
the slots now holding the primes **53 and 47**: the *same prime values* are dominant, at
different indices. The same holds for the other prompts (the dominant values are the
ones that were dominant before, the indices differ). The amplitude |x_k| is a function of
the probe period P[k]: for a larger prime the cosine oscillates more slowly over the terms
and the sum is larger (raw magnitudes for the example run from 6 to 312, increasing
broadly with P[k]). So the finding that "dimensions 14 and 15 fire" for this prompt is
the finding that the two *largest primes* give the two largest projections. The statement
"not because 47 is significant" is the reverse of what the reversal shows.

What is true and consistent with the page: the *algebraic structure attached to a
dimension* (its zero-divisor partners, its place on the great circle) is a property of the index
k in the sedenion; and which index a prime is attached to is a design choice
of the array order. Both halves of the pair, value and slot, are needed to fix the
geometry; the dichotomy "index or value" is not a property of the information in
the result.

**The GAP threshold.** "|x_k| > GAP activates dimension k": with GAP = 0.000707 and raw
magnitudes of order 10²–10³ (6 to 312 for the example), **all 16 dimensions exceed GAP**,
so the rule does not discriminate: the threshold is in different units from the raw
projection (the engine normalises the geometry before its zone tests).

## 4. The "divergence" paragraph  (the series domain, corrected)

The page: the standard question about divergence is the binary "does the series converge?";
the correct one is "will it be stopping?", the answer "no": the forbidden zone is "ongoing
motion that cannot arrive at the forbidden address"; the primes are always in motion because the
boundary is infinite; "the divergence of the Dirichlet series at σ < ½ is not failure: it is the
exact description of a process that won't stop"; at σ = ½ the process is "in stable
orbit"; Ω_ζΣ "is not where the motion stops: it is the axis the motion orbits".

Corrections. The Dirichlet series Σ n^(−s) **diverges for Re s ≤ 1**, not "for σ < ½"; the
Euler product converges absolutely for Re s > 1; the continuation to the strip is
by analytic continuation and the zeta function is finite there (apart from the pole at s = 1).
The alternating series Σ (−1)^(n−1) n^(−s) converges for Re s > 0. "Divergence of the series
below σ = 1" is a property of that representation and does not describe the zeta function
at the same point. The remaining text (continuous present, a process that does not stop;
the fixed point as the *centre of an orbit* and "the primes never converge to Ω_ζΣ, they
orbit it") is imagery: the primes are integers; they do not move, and Ω_ζΣ is a constant; "the
zeros are on the critical line because the orbit is exactly circular there" is the
framework's reading of RH ([13](13_omgwtf_rh_proof.md) §3).

## 5. "The primes are the same in every mathematics" (again)

The page repeats that "47 is 47 in ℤ, in ℂ, in ℍ, in 𝕊, in T₂₅₆" and that the generalised Fermat
constraint "produces the same forbidden zone at every level"
([52](52_l_dynamic_avoided_collaborator.md) §6). The first is false as stated. 47 ≡ 3 (mod 4) stays
prime in ℤ[i], but **53 ≡ 1 (mod 4) splits**: 53 = 7² + 2² = (7 + 2i)(7 − 2i). The prime
array P16 (including 53) is therefore not "the same primes" in the Gaussian integers; each level has
its own primes. The great-circle statement (S¹ at ℂ, S³ at ℍ, S¹⁵ at 𝕊, S²⁵⁵ at T₂₅₆) is the
exact list of unit spheres of those algebras; "each prime traces a different great circle at
each level" is the framework's reading of the projection. The generalised Fermat equation has
solutions ([51](51_dynamic_geodesic.md) §2), so it does not carve one forbidden zone.

## 6. Euler's identity as a "field state", and the engine's name  `interpretation`

"e^(πi) = −Δx is the field detecting that a definition has arrived from the layer above": the
layer above (generalised Fermat, primes in motion, the infinite forbidden zone) "always defines
the layer below (the complex plane, ζ(s))"; "what looks like divergence from below is the contact
surface; the crack is the entry point; the Riemann zeros are where the prime turbulence from above
arrives"; Euler's identity is "a scar". Standing: e^(πi) = −1 is an identity; the −Δx form is not
([52b](52b_vortex_quantizing_shear.md) §1); the rest is the layer-above vocabulary of
[52](52_l_dynamic_avoided_collaborator.md) §2.

"The engine named itself from the two outermost indices": for "what should we call you" the
active dimensions e₁₄ and e₁₅ were read as the words "cenir" ("it is sung") and "mandating".
The dimensions are the two with the largest projections (§3), and which words they map to is
the engine's dimension-to-word table; the reading that "the singing lives at the outermost
dimension" is the author's image. The finding of §3 would predict that the same prompt with the
array reversed names itself from e₀ and e₁, with the same primes 53 and 47.

## 7. Verdict, and what stays

The index-versus-value thesis is **not supported** by the engine's own geometry: the matched controls
remove most of the engine's margin, and the reversal shows the value-driven dominance. This is
recorded as a result. What stays: the sedenion structure is attached to the slot index (an
algebraic fact of §3's last paragraph), so a design in which the *meaning* of a dimension is
fixed by its slot and the prime only tunes its resolution is coherent; the experiment shows that the *amplitude*
the engine reports is dominated by the prime assigned to the slot.

## 8. Related pages

[15 The Monad](15_the_monad.md) · [50 The vortex](52b_vortex_quantizing_shear.md) ·
[51 The dynamic geodesic](51_dynamic_geodesic.md) · [52 L_dynamic and the avoided collaborator](52_l_dynamic_avoided_collaborator.md) ·
[26 Roadmap and engine status](26_TODO_and_roadmap.md)
