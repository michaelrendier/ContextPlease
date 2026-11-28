# 12 — SMNNIP Distribution Engine (design specification, not built)

| | |
|---|---|
| Status | **THEORETICAL — design only. No module exists.** |
| Checked | 2026-11-13: `ValaQuenta/modules/` has no `distribution` directory; no engine of that name is registered |
| Intended location | `ValaQuenta/modules/distribution/` (`maths.py`, `tools.py`, `manifest.json`), per the Full Engine Protocol in `ValaQuenta/engine/registry.py` |

This page is a specification. Nothing on it runs. Where a component it names
does exist, the table in §3 says where.

## 1. Purpose

The derivation modules compute equations. The distribution engine would run a
trained SMNNIP network forward and return a distribution over `SemanticWord`s.
Its output rule is recognition, not construction ("Ptolemy speaks because he
knows"): the output is the nearest stored address to an attractor, never an
assembled token sequence.

## 2. Intended pipeline

```
raw input (text | image | spectrum)
  → substrate encoder
  → inclusion chain ℝ → ℂ → ℍ → 𝕆 : activation spinors Ψ_i ∈ 𝕆
  → tower forward pass:
        J_N at each layer boundary            [inversion, 03]
        ∂_μ J^μ monitored per layer           [noether, 05]
        α_NN(r), ħ_NN(r) run per layer        [lagrangian, 04]
        stop at the sedenion boundary
  → 𝕆 output attractor
  → Tongue: Fano generator path → nearest SemanticWord in the HyperGallery
```

For one input there may be several attractors (the basin structure of the
Lorenz–Stirling system). The distribution over candidate words would be

```
P(word_k | input)  ∝  exp( − dist( attractor, word_k.fano_coords ) )
```

with `dist` the Fano-index distance. This is a proposed form, not a derived
one: the Fano index of [09](09_hyperwebster_engine.md) is many-to-one, so the
distance it induces is coarse, and the weighting is untested.

## 3. Components, as of 2026-11-13

| Component | State | Where |
|---|---|---|
| Inversion forward step | exists | `modules/inversion` |
| Noether monitor | exists | `modules/noether` |
| Running couplings | exists | `modules/lagrangian` |
| Horner/Fano addresses, `SemanticWord`, `HyperGallery` | exist | `modules/hyperwebster` |
| Tongue (reverse lookup from an attractor) | scaffold only (`monad_address`, `fano_path`) | `modules/hyperwebster` |
| Substrate encoders (text, image, spectral) | spectral exists in `modules/jwst`; text and image encoders (`TextHyperIndex`, `ImageHyperIndex`) exist only in the First Age archive and were never ported | `PtolemyDesktop/Archive/ainulindale_first_age/FA_smnnip_hyperindex.py` |
| Trained tower weights | not built; no training loop in this repository | — |
| Distribution over `SemanticWord`s | not built | — |
| Lorenz–Stirling basin routing | not found: no file in `ValaQuenta/` mentions it; the 2026-06 sketch cited `smnnip_derivation_pure.py` §13–17, which was not located in this check | — |

## 4. Invariant: first encounter is immutable

The design requires that the first time the engine meets a `SemanticWord`,
that encounter (with its Fano coordinates) is recorded and can never be
altered: the system learns by accumulation, not revision. The enforcement
named in the design is three-fold: a Python `__setattr__` guard, a SQLite
trigger, and a C++ `const`. None of the three is present in this repository
(a search of the source for the field name finds nothing); the invariant is
specified, not implemented.

## 5. Relation to what was built instead

The ideas of this page were developed in later engines that do run:

- the word → address → zero mapping of the Monad ([15](15_the_monad.md)),
- the Library-of-Babel address engine `basile` ([124](124_basile_invertible_location_maps.md)),
- the semantic hash and baseline of `VAPMIP/SemPriCon`.

Anyone building the distribution engine should start from those, not from
the 2026-06 sketch above.

## 6. Related pages

[03 Inversion](03_inversion_engine.md) · [05 Noether](05_noether_engine.md) ·
[09 HyperWebster](09_hyperwebster_engine.md) · [15 The Monad](15_the_monad.md) ·
[16 Semantic word engine](16_semantic_word_engine.md)
