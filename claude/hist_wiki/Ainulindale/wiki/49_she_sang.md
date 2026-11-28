# 49 — She sang: the prose passages, with their mathematical statements checked

| | |
|---|---|
| Status | **A set of short prose passages (2026-06-10, added to 2026-06-17); the author's vision "filling between the lines". `INTERPRETATION`.** Eleven sentences, each condensing a claim treated elsewhere; where a sentence makes a mathematical statement it was recomputed on 2026-11-13 (§3) |
| Code | Listing 1 (the numerical statements); the canonical-maths block `@RCCM_FERMATS_MONSTER` (`~/.clauderc_canonical_maths`) |
| Last verified | 2026-11-13: Listing 1 executed |

## 1. Why this page is kept

Each passage is one long sentence compressing a result or a position of the
earlier pages. They are kept as the author's summary voice; the standing of
each is set by the page that treats it.

## 2. The passages, with standing

| # | Passage (condensed) | Standing |
|---|---|---|
| 1 | Sixteen operator names, chosen "for reasons that felt arbitrary", self-organised to d*/σ½/D* = 1 with zero free parameters: "the universe had signed its own work" | measured on one saved vocabulary with hard-coded zone cutoffs; zero-free-parameter claim not shown ([27](27_third_age_CS_paper.md) §2) |
| 2 | The Bang is not finished; dark energy is the condensate's superconducting current driving the bubble wall; "we are inside the cavitation" | `CONJECTURE`; the "never decelerating" step fails against q(z) ([32](32_superconducting_medium.md) §2) |
| 3 | The observer who reaches σ = ½ was always going to; the fixed-point equation has been solved "since before the observer existed" | `INTERPRETATION`; no map is defined ([48](48_observer_fixed_point.md)) |
| 4 | The universal standing wave integrates to π and the observer's resonance traces φ, "two faces of σ = ½": the circle the universe is and the spiral the observer becomes; the Sri Yantra, OM, cymatic patterns | no calculation: π enters as the 2/π prefactor and φ as the recursion eigenvalue, supplied inputs ([22](22_constant_facets.md) §6) |
| 5 | Lúthien walked into Angband and sang Morgoth to sleep (as in the *Silmarillion*), because "the song was complete"; on 2026-06-10 an observer "stopped fighting the fixed point" | the Tolkien correspondence of [47](47_the_two_trees.md); the date marks the author's own experience |
| 6 | **(added 2026-06-17)** e₀…e₁₅ are the hexadecimal digits 0…F, and "the three positions no Niemeier lattice can reach" are {1, B, F}: "one, Boron, Fluorine, the Two Lamps and the unit that holds them apart" | the index set {1, 11, 15} **reproduces** (§3, Listing 1). The element names are a pun on the digits' letters: B and F are the hex digits 11 and 15; boron and fluorine have atomic numbers 5 and 9, not 11 and 15 |
| 7 | Illuin and Ormal (the Two Lamps, raised by Aulë and destroyed by Melkor), and what remained is π, "the transcendental residue that the Monster's most catastrophic collapse at τ* = (1+√−163)/2 cannot extinguish": the Monster "can collapse to an integer but cannot make π rational" | the numerical content is exact (§3): j(τ*) = −640320³ and e^{π√163} = 640320³ + 744 − 7.5·10⁻¹³. "The Monster collapses" is a figure for the integrality of j at the class-number-one points |
| 8 | Ilúvatar made Melkor the most powerful of the Ainur "because" the three positions {e₁, e₁₁, e₁₅} that complete the sixteen N-shapes of the sedenion are inaccessible to every A/D/E root system at rank 24, and filling them requires a symmetry group of order 8·10⁵³, "35 orders of magnitude larger than any Vala" | the 8·10⁵³ is the order of the Monster, 8.08·10⁵³ ([39](39_every_singularity_the_void.md) §5, verified). That the three positions "require" the Monster is not derived: they are the residues missing from the set of Coxeter numbers mod 16 (§3), and the Monster's order appears in the sentence by assertion. The "35 orders of magnitude" compares the Monster's order with an unspecified quantity attached to a Vala |
| 9 | "The discord was the plan": the three Monster-gap positions "were cut to Monster shape before the Monster existed to fill them"; the gap is "a door" | the author's reading of the *Ainulindalë* |
| 10 | The CRYSTALS-Kyber designers "did not choose the Monster gap; the NTT chose it": efficiency requires q ≡ 1 (mod 16), "e₁, Melkor's position" | Kyber's q = 3329 = 13·256 + 1 (so q ≡ 1 mod 256, hence mod 16). **This is no evidence for the gap:** every NTT-friendly prime has q ≡ 1 modulo a power of two, so it lies in residue 1 for that reason; and 1 is the identity class, which is why no Coxeter number tends to sit there. A property shared by all NTT parameter sets cannot single out the Monster gap |
| 11 | The Two Lamps and the Two Trees fell, the Silmarils were lost; "at every destruction something transcendental survived that the destruction required in order to be stated": the j-function collapses to −640320³ at the last class-number-one point, "the collapse requires π to describe it", "the catastrophe always had a floor and the floor was always π" | the exact content is §3 (π appears because q = e^{2πiτ}); "floor" is the author's image |

## 3. The numerical statements, recomputed  (`:CALCULATED`)

**Listing 1 — the checks behind passages 6–8, 10, 11** (written for this page;
runs cold with mpmath)

```python
import mpmath as mp
mp.mp.dps = 40

# 23 Niemeier root systems: (name, Coxeter number h)
niemeier = {'D24': 46, 'D16E8': 30, 'E8^3': 30, 'A24': 25, 'D12^2': 22, 'A17E7': 18, 'D10E7^2': 18,
            'A15D9': 16, 'D8^3': 14, 'A12^2': 13, 'A11D7E6': 12, 'E6^4': 12, 'A9^2D6': 10, 'D6^4': 10,
            'A8^3': 9, 'A7^2D5^2': 8, 'A6^4': 7, 'A5^4D4': 6, 'D4^6': 6, 'A4^6': 5, 'A3^8': 4, 'A2^12': 3, 'A1^24': 2}
hits = sorted({h % 16 for h in niemeier.values()})
print('23 Niemeier lattices; h mod 16 hits', len(hits), 'of 16; missing', sorted(set(range(16)) - set(hits)))

supersingular = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]   # the 15 primes dividing |Monster|
ss = sorted({p % 16 for p in supersingular})
print('supersingular p mod 16 hits', len(ss), ':', ss)

print('196560 = 2^4*3^3*5*7*13 :', 2**4 * 3**3 * 5 * 7 * 13 == 196560, '   196883 = 47*59*71 :', 47 * 59 * 71 == 196883)

hexs = ''.join('%X' % k for k in range(16))
print('e0..e15 as hex digits:', hexs, '  Monster-gap positions {1,11,15} =', [hexs[k] for k in (1, 11, 15)])

x = mp.exp(mp.pi * mp.sqrt(163))
print('exp(pi*sqrt(163))   =', mp.nstr(x, 36))
print('640320^3 + 744      =', 640320**3 + 744, ' (j(tau*) = -640320^3, tau* = (1+sqrt(-163))/2)')
print('Kyber q = 3329: q-1 =', 3329 - 1, '= 13 * 256 ->', (3329 - 1) % 256 == 0, ' q mod 16 =', 3329 % 16)
```

```
23 Niemeier lattices; h mod 16 hits 13 of 16; missing [1, 11, 15]
supersingular p mod 16 hits 9 : [1, 2, 3, 5, 7, 9, 11, 13, 15]
196560 = 2^4*3^3*5*7*13 : True    196883 = 47*59*71 : True
e0..e15 as hex digits: 0123456789ABCDEF   Monster-gap positions {1,11,15} = ['1', 'B', 'F']
exp(pi*sqrt(163))   = 262537412640768743.999999999999250073
640320^3 + 744      = 262537412640768744  (j(tau*) = -640320^3, tau* = (1+sqrt(-163))/2)
Kyber q = 3329: q-1 = 3328 = 13 * 256 -> True  q mod 16 = 1
```

What these establish and what they do not:

- **The Monster gap is a real computational fact.** The Coxeter numbers of the 23 Niemeier root systems, taken mod 16, occupy 13 of the 16 residues and miss exactly {1, 11, 15}; the 15 supersingular primes (the primes dividing the Monster's order) occupy 9 residues, {1, 2, 3, 5, 7, 9, 11, 13, 15}, so they cover the missing three without equalling the Niemeier set. This is the content of `@RCCM_FERMATS_MONSTER`. Reading the residues as sedenion positions e_k (k = h mod 16) is the framework's identification.
- **The Ramanujan constant is exact arithmetic.** e^{π√163} = 262537412640768743.99999999999925…, within 7.5·10⁻¹³ of the integer 640320³ + 744, because j(τ*) = −640320³ and j = 1/q + 744 + O(q) with q = −e^{−π√163}. Hence "π is needed to state the collapse": π enters through the nome q = e^{2πiτ}.
- **Nothing here shows that the Monster is needed to "fill" the three positions**, nor that the Kyber modulus relates to them (passage 10): the evidence is a coincidence of residues, and the one that every NTT prime shares.

## 4. Related pages

[39 Every singularity](39_every_singularity_the_void.md) · [47 The two trees](47_the_two_trees.md) ·
[48 The observer as a fixed point](48_observer_fixed_point.md) · [53 T256 and cryptographic transparency](53_t256_cryptographic_transparency.md) ·
`FourthAgePapers/FermatMonster/`
