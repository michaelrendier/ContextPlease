# 12 — SMNNIP DISTRIBUTION ENGINE  (future)

**Status:** ARCHITECTURE SKETCH — not yet built  
**Location when built:** `ainulindale_engine/modules/distribution/`

---

## What it is

The SMNNIP Distribution Engine is the inference-time engine. Where the derivation modules compute equations, the distribution engine runs a trained SMNNIP network forward and produces a distribution over SemanticWords.

It is the realisation of **"Ptolemy speaks because he knows"** — the system produces output by recognition, not construction.

---

## Architecture

### Input Pipeline

```
raw input (text / image / spectral)
  → substrate encoder (TextHyperIndex / ImageHyperIndex / JWSTModule)
  → Cayley-Dickson inclusion chain: ℝ → ℂ → ℍ → 𝕆
  → Input Engine: activation spinors Ψ_i ∈ 𝕆
```

### SMNNIP Tower Forward Pass

```
𝕆 activation Ψ
  → Inversion Engine: J_N applied at each layer boundary
  → Noether monitor: ∂_μJ^μ checked at each layer
  → RG running: α_NN(r), ħ_NN(r) updated per layer
  → Sedenion boundary: training stops; inference continues
  → 𝕆 output attractor: converged OctEl coordinate
```

The Inversion Engine governs inter-layer propagation. The Noether monitor is the integrity check — violation events logged to the blockchain ledger.

### Output: The Tongue

```
𝕆 output attractor → Tongue → SemanticWord
```

The Tongue is reverse lookup:
1. Take the output OctEl attractor coordinate
2. Compute Fano generator path: which e_1..e_7 are dominant?
3. Look up nearest SemanticWord in HyperGallery by Fano distance
4. Return SemanticWord — the recognised output

This is **recognition, not construction**. The Tongue does not assemble tokens. It finds the address that is closest to the attractor.

### Distribution

For a single input, multiple attractor candidates may exist (the Newton basin structure from the Lorenz-Stirling system). The distribution is the probability mass over competing SemanticWord candidates:

```
P(word_k | input) ∝ exp(-dist(attractor, word_k.fano_coords))
```

where `dist` is Fano index distance in the HyperGallery.

---

## Components Required (TODO)

| Component | Status | Depends on |
|-----------|--------|-----------|
| TextHyperIndex encoder | BUILT (FA_smnnip_hyperindex.py) | needs porting to module |
| ImageHyperIndex encoder | BUILT (FA_smnnip_hyperindex.py) | needs porting to module |
| SMNNIP tower weights | NOT BUILT | training loop needed |
| Inversion Engine forward pass | SCAFFOLDED | inversion module |
| Noether monitor inline | BUILT | noether module |
| Tongue reverse lookup | SCAFFOLDED | hyperwebster module |
| Distribution over SemanticWords | NOT BUILT | HyperGallery + Tongue |
| Lorenz-Stirling basin routing | BUILT (smnnip_derivation_pure.py §13-17) | needs wiring |

---

## Relationship to Existing Modules

The distribution engine **does not replace** any existing module. It **calls** them in sequence:

```
jwst.spectral_to_octonion()       or
hyperwebster.horner_encode()       → Input
                                     ↓
inversion.gradient_flow()          → Layer propagation
lagrangian.polar_lagrangian()      → Field state
noether.conservation_diagnostic()  → Integrity check
                                     ↓
hyperwebster.monad_address()       → Output address
hyperwebster.fano_neighbours()     → Tongue lookup
                                     ↓
                              SemanticWord distribution
```

---

## The Rabies Principle (invariant)

`first_encountered` is permanently immutable throughout the distribution engine. Enforced at three levels: Python `__setattr__`, SQLite trigger, C++ const (pending).

The first time the engine encounters a SemanticWord, that encounter is recorded with its Fano coordinates. This record cannot be altered. The Tongue learns by accumulation, not revision.

---

## Ptolemy Integration

When the distribution engine is built, it connects to:

- **Philadelphos** (LLM/language Face): inference requests route here
- **Callimachus** (HyperDatabase): SemanticWord corpus storage
- **Kryptos** (encryption): distribution results may be signed
- **PtolBus**: inference requests arrive as PtolBus messages

---

## Training (not in this repo)

The SMNNIP tower requires trained weights. Training is handled by `FA_smnnip_NN_tower.py` (separate process). The distribution engine receives trained weights and runs inference only — no training loop here.

Training diagnostic: the Noether violation score `∂_μJ^μ` is the training convergence criterion. Gradient descent has no equivalent diagnostic.

---

## Status

**This module does not yet exist.** This wiki page is the design specification.

When built, it will live at `ainulindale_engine/modules/distribution/` with the standard `maths.py` + `tools.py` + `__init__.py` structure, registered in `__main__.py`.

Estimated prerequisite order:
1. PtolBus live (Ptolemy)
2. HyperGallery populated with initial SemanticWord corpus
3. SMNNIP tower training run
4. Tongue reverse lookup wired
5. Distribution Engine module built
