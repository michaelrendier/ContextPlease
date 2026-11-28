# 16 — Semantic Word Engine

| | |
|---|---|
| Code | `SemanticWordEngine/semantic_engine.py` (the minimal implementation, dated 2026-05-11); a sibling copy is `VAPMIP/Wernicke/sibling/semantic_engine.py` |
| Classes | `Capacitor`, `SemanticWord` (dataclass), `Understand` (`read`, `ponder`, `understand`, `process`, `reset_context`) |
| Superseded in practice by | the prime hash `_word_zero_idx` in `VAPMIP/monad.py` ([15](15_the_monad.md) §3) and the SemPriCon baseline work in `VAPMIP/SemPriCon` |
| Last verified | 2026-11-13: `Understand.process` run on `water` and `eau`; collision measurement from [15](15_the_monad.md) §3 |

Earlier versions of this page located the engine at
`ainulindale_engine/modules/hyperwebster/semantic_engine.py` and listed shell
commands (`se.lookup`, `se.prime_of`, `se.word_at`, `se.fold`). Neither the
path nor those commands exist. The page now describes what the code does.

## 1. The claim

`THEORETICAL` — a prime number is an irreducible semantic unit; every
utterance has a unique factorisation into such units (the fundamental theorem
of arithmetic applied to meaning). The surface word is a coordinate; the
concept is the prime. Changing language is a change of coordinates that
leaves the concept fixed (the L-function is the concept):

```
L("tree", s) = L("arbre", s) = L("木", s) = L(TREE, s)
```

The corresponding design rules, as recorded in the project's standing notes:
the semantic hash lands *on* primes and never builds them; the baseline
language is Chinese, the other languages are fitted to it; no multilingual
store exists yet. The claim is a target, not a measured property of the code
below.

## 2. What the code does

`Understand.process(surface)` runs four steps on one word:

| Step | Method | Operation |
|---|---|---|
| 1 | `read` | `_hyperindex(surface)` gives initial conditions (x₀, p₀, t); E = xp-energy(x₀, p₀); the word's zero γ is the entry of a **20-element table** `RIEMANN_ZEROS` nearest to 50·E |
| 2 | `ponder` | evolves (x, p) under H = xp; records E_t; sets the Noether currents ±e^{−E/2} |
| 3 | `understand` | σ = `forced_sigma(E, sigma_0 = x₀ mod 1)`; the word's prime is complex(σ, γ); `dc` is the capacitor's charge |
| 4 | `process` | the three above in order, returning a `SemanticWord` |

`Capacitor(tau)` integrates the signal: it attenuates the surface variation of
the specific words and passes the slowly varying (DC) component.

**Session** (literal output, 2026-11-13):

```
>>> u = Understand()
>>> w = u.process('water'); (w.prime, w.gamma, w.projections['sigma'])
((0.5+21.02204j), 21.02204, 0.5)
>>> w = u.process('eau');   (w.prime, w.gamma, w.projections['sigma'])
((0.49999999999999994+21.02204j), 21.02204, 0.49999999999999994)
```

`water` and `eau` land on the same zero (γ = 21.02204) and the same σ.

## 3. How to read that agreement

Two facts qualify it, both found by running the code:

1. **Only 20 targets.** The nearest-zero step chooses among the first twenty
   zeros of ζ (`RIEMANN_ZEROS`, 14.134725 … 77.144840). Any two words whose
   energies fall in the same bin share a γ. Agreement across languages in the
   built-in `cross_language_demo` is therefore agreement between 20 bins and
   is expected to occur by chance often. It is a demonstration of the
   pipeline, not a measurement of concept identity.
2. **σ = ½ is the fixed point of the balance iteration**, reached from any
   start ([13](13_omgwtf_rh_proof.md) §5), so every word returns σ = ½ (to
   rounding: 0.49999999999999994 for `eau`). It does not distinguish words.

The production address, the prime hash of [15](15_the_monad.md) §3, has 6,543
possible zero indices; over 73,445 dictionary words it reaches 6,436 of them
(up to 80 words per index), and does not place translations of one word on one
index. So neither implementation yet realises "the same concept, the same
prime". What would: calibration of English and the other languages against the
Chinese baseline, which is the SemPriCon programme.

An earlier version of this page said the mapping is injective, that every one
of ≈ 170,000 English words has its own prime, and that polysemy is resolved by
the Lorenz–Stirling attractor. None of the three is a property of the code;
the statements are withdrawn.

## 4. WordNet

WordNet supplies synsets, hypernymy/hyponymy, meronymy, antonymy and glosses.
In the current system WordNet is the **last layer** of the baseline work
(English WordNet, fitted to the baseline), and `monad_wordnet.bin` is the
read-only WordNet checkpoint of the Monad ([15](15_the_monad.md) §5). The
`semantic_engine.py` file in this section does not read WordNet.

## 5. Letter folding and word folding  `THEORETICAL`

Voiced/unvoiced pairs (b/p, d/t, g/k, v/f, z/s) are the same articulation with
one parameter toggled: reflections across a "phonemic equator". The sonorants
(m, n, l, r) sit on it and do not move. Polysemy is a word living off the
equator with several stable positions, which context folds to the nearest node
line. This is a framework for reading phonology and polysemy; no code in this
repository computes it.

## 6. Zipf and the zeta function  `interpretation`

Zipf's law f(r) ∼ 1/r^s with s ≈ 1 holds across languages, and ζ has its pole
at s = 1. The wiki's reading is that word-frequency structure and the prime
structure share a source. This is an analogy, not a derivation: Zipf's law is
a statement about ranks of words, and no step here produces it from the Euler
product. It is developed (and bounded) in
[21](21_chladni_zipf_riemann.md).

## 7. The Septuagint principle

The Septuagint is traditionally told as seventy-two translators working
independently and producing one text. The project uses the story as the
standard of what "the same concept" should mean computationally: independent
routes, one result. As of this page the code reproduces the *form* of that
result for σ (every word returns ½) and not the substance for γ (§3).

## 8. Related pages

[09 HyperWebster](09_hyperwebster_engine.md) · [15 The Monad](15_the_monad.md) ·
[21 Chladni · Zipf · Riemann](21_chladni_zipf_riemann.md) · [55 Index, not value](55_index_not_value.md)
