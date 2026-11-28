# 30 — D-Λ: the cosmological constant as the second lobe

| | |
|---|---|
| Status | **Proposal (`THEORETICAL`/`INTERPRETATION`) with one reproduced address observation (§3) and the open step stated (§5).** The earlier header "three claims at σ = ∞" is withdrawn: the "σ" figures were assigned labels, not computed ([24](24_claude_conclusion.md) §2) |
| Depends on | [29](29_witches_hat_paper.md) |
| Code | `VAPMIP/monad.py` (`_word_zero_idx`); Listing 1 below |
| Last verified | 2026-11-13: Listings 1 and 2 executed; Planck 2018 values used as quoted |

## 1. The reading of Einstein's equation  `interpretation`

```
G_μν + Λ g_μν = 8πG T_μν
```

The framework reads the geometric term G_μν as the backward, compressive
current J_neg (the infalling lobe), the matter term T_μν as the forward,
expansive current J_pos (the escaping lobe), and Λ g_μν as the waveform's
second lobe written as a metric term: "J_neg + Λg_μν = J_pos", "the vacuum
applying itself". The identification is a reading of the equation, not a
derivation of Λ; "Λ must exist because the Hawking waveform has two halves"
is the claim to be tested, and no test of it is in this repository.

History, corrected. Einstein **introduced** Λ in 1917 to obtain a static
universe; after Hubble's expansion (1929) he abandoned it (the "greatest
mistake" remark is reported by Gamow). The earlier page said he "removed the
J_neg term in 1917"; he added it then and dropped it after 1929. The 1998
supernova results (Perlmutter; Schmidt and Riess; the 2011 Nobel Prize) show
acceleration, which requires a Λ-like term in the standard model. The phrase "σ > 40" of
the earlier page is not sourced and is removed.

## 2. The waveform as the Mexican hat  `interpretation`, geometry exact

Take V(r) = −μ²r² + λr⁴. The earlier page called the brim both "the V minimum"
and "the zero crossing". They are different radii (Listing 1):

| Feature | Radius | Value |
|---|---|---|
| centre r = 0 | 0 | V = 0, a local maximum |
| minimum (the "brim" as the vacuum ring) | r = μ/√(2λ) | V = −μ⁴/(4λ) |
| zero crossing | r = μ/√λ | V = 0 |

so the zero crossing sits at √2 times the minimum's radius. Which is "the
brim" (σ = ½, the node) has to be chosen; the page's "minimum **and** zero
crossing" does not hold for this V.

**Listing 1 — the features of V(r)** (written for this page; runs cold)

```python
import math
mu, lam = 1.0, 1.0
V = lambda r: -mu**2 * r**2 + lam * r**4
r_min, r_zero = mu / math.sqrt(2 * lam), mu / math.sqrt(lam)
print('V(0)       =', V(0.0))
print('minimum at =', round(r_min, 6), ' V =', round(V(r_min), 6))
print('zero at    =', round(r_zero, 6), ' V =', round(V(r_zero), 12))
print('ratio      =', round(r_zero / r_min, 6))
```

```
V(0)       = 0.0
minimum at = 0.707107  V = -0.25
zero at    = 1.0  V = 0.0
ratio      = 1.414214
```

The two lobes (Red, up, J_pos, matter, `e₁₅ emit`; Blue, down, J_neg, dark
energy, `e₁₄ interrupt`) are drawn with the blue lobe larger "because dark energy is
69% and matter 31%". That is an illustration of the animation; the asymmetry of a
drawn potential is not a derivation of Ω_Λ/Ω_m. The Sombrero Galaxy (M104) as "a
single lobe", and the EHT images as "photographs of the Higgs vacuum", are
imagery and not claims on this page.

## 3. A reproduced address observation (`:CALCULATED`)

The earlier page said the prime hash puts *vacuum*, *negative*, *lambda* and
*infinite* on one sedenion dimension, e₄ (*apply*), and *higgs* and *chaos* on e₀
(*identity*). Here "dimension" is the zero index modulo 16 (`idx % 16`, as in
`e01_operator_selforg.py`).

**Listing 2 — the dimension of six words** (`VAPMIP/monad.py`:
`_word_zero_idx`, imported; run from `ThePlace` as below)

```python
import importlib.util
spec = importlib.util.spec_from_file_location('vm', 'VAPMIP/monad.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for w in ('vacuum', 'negative', 'lambda', 'infinite', 'higgs', 'chaos'):
    i = m._word_zero_idx(w)
    print(f'{w:9} zero idx {i:5d}  idx%16 = {i % 16:2d}')
```

```
vacuum    zero idx  2436  idx%16 =  4
negative  zero idx  5476  idx%16 =  4
lambda    zero idx  3636  idx%16 =  4
infinite  zero idx  5188  idx%16 =  4
higgs     zero idx  5680  idx%16 =  0
chaos     zero idx  5728  idx%16 =  0
```

**The observation reproduces under the current hash.** How surprising it is:
over the 73,445 dictionary words the residues mod 16 are close to uniform
(counts 4,367–4,980 for each residue), and four randomly drawn words share one
residue in 0.015% of 20,000 draws (expected 1/16³ = 0.024%). So four-in-one
is rare for random words. But the six words were chosen by the author after
the fact, and the number of semantic groups that could have been tried is not
recorded, so no significance is claimed. A fair test would fix a list of
semantically defined word groups in advance and count how many share a
residue. None exists yet.

## 4. Ω_ζΣ and the value of Λ  `OPEN`

Ω_ζΣ = W(1) = 0.5671433 is the fixed point of x ↦ e^(−x)
([17](17_alpha_omega_d_star.md) §2). Flat ΛCDM:
H(z) = H₀√(Ω_m(1+z)³ + Ω_Λ). The matter–Λ equality (ρ_m = ρ_Λ) is at
(1+z) = (Ω_Λ/Ω_m)^{1/3}; with Planck 2018 (Ω_Λ = 0.6889, Ω_m = 0.3111) this gives
**z = 0.3034** (the earlier page said 0.308). Its stated claim, that some
function f gives Ω_Λ = f(Ω_ζΣ, Ω_b h²), is **the open step**: no f is given.
(The three other steps listed: Ω_ζΣ from the prime hash [a fixed point, not a hash
output]; Ω_b h² from the CMB; Λ = 3H₀²Ω_Λ/c², standard.) The earlier page's
"zero free parameters" for step 1 is not shown ([27](27_third_age_CS_paper.md) §2).

## 5. The asymmetry and the future  (corrected)

The earlier page argued that the universe is approaching Ω_ζΣ as the
de Sitter equilibrium, and that Ω_Λ,eff(z) should fall toward Ω_ζΣ with
redshift. In flat ΛCDM, Ω_Λ(a) = Ω_Λ/(Ω_Λ + Ω_m a⁻³), which tends to **1** as
a → ∞ (the de Sitter state is pure Λ), not to 0.567; and looking back it falls
through 0.567 at z = 0.191 on the way to 0 (Ω_Λ(z=1) = 0.217, Ω_Λ(z=3) = 0.033).
So "Ω_Λ = 0.689 > Ω_ζΣ means we have passed the equilibrium" has no
counterpart in the standard solution. DESI Year-1 (2024) combined with other
data shows a mild preference for evolving dark energy (w ≠ −1) of a few σ,
depending on the supernova sample; whether w(z) tracks anything related to
Ω_ζΣ is a testable *proposal* with no calculation here. `OPEN`.

## 6. Λ and the Higgs field  `CONJECTURE`

The Higgs potential is the Mexican hat, with its vacuum expectation value at the
ring minimum, and Λ is read as "the Higgs field at horizon scale". The two
scales are 55 orders of magnitude apart in energy density and the standard
problem (why the vacuum energy is so small) is not addressed by the
identification. The prime hash puts *higgs* and *chaos* on e₀ and *lambda* on e₄
(§3); whether that has a physical meaning is not shown.

## 7. Open steps (unchanged in substance)

1. Derive f(Ω_ζΣ, Ω_b h²) = Ω_Λ explicitly.
2. Compare evolving-dark-energy data (DESI) with a stated prediction for w(z).
3. Formalise the Higgs ↔ Λ identification across energy scales.
4. An engine and notebook: a Friedmann solver with the Ω_ζΣ constraint.
5. A pre-registered test of the address observation of §3.

The animations the earlier page embedded (`sombrero_static.png`,
`witches_hat_v2.gif` under `../animations/`) are not in the repository.

## 8. Related pages

[27 Third Age CS paper](27_third_age_CS_paper.md) · [29 The witches hat](29_witches_hat_paper.md) ·
[17 A_fermat · Ω_ζΣ · d*](17_alpha_omega_d_star.md) · [31 Cavitation, causality, Fermat](31_cavitation_causality_fermat.md) ·
[108 De Sitter cavitation](108_desitter_cavitation.md)
