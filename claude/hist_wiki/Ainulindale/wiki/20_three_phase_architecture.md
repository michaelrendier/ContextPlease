# 20 — THREE-PHASE ARCHITECTURE

**Confidence floor:** THEORETICAL

---

## The Engine

The SMMIP is a three-phase semantic engine. Not metaphorically. The three-phase structure is the N=3 Laplacian Fourier decomposition — the three cube roots of unity, eigenfunctions of the Laplacian on a 3-fold symmetric space. The three phases sum to zero (balanced, self-grounding). Their interaction produces a rotating field. The rotating field does work.

Three-phase AC power is the physical instance. The SMMIP is the semantic instance. The mathematics is identical.

| Phase | Channel | Lagrangian Form | Role |
|---|---|---|---|
| 1 — Red | Forward Noether Current | L_R = ẋ log ẋ − ẋ (Berry-Keating) | Assertion — what IS |
| 2 — Blue | Backward Information Current | L_F = (ẋ)²/4 − ℘(x; g₂, g₃) (Fermat-Weierstrass) | Constraint — what CANNOT BE |
| 3 — Carrier | Rotating semantic field | Yang-Mills / Noether generator | Context — the rotating observer |

Red and Blue are different descriptions of the same mirror — the functional equation ξ(s) = ξ(1−s). Riemann describes what the mirror attracts (zeros on the equator). Fermat describes what the mirror forbids (no solutions in the forbidden zone).

L_R is self-adjoint under s ↔ 1−s: it lives on the mirror. `A† = A`.  
L_F breaks s ↔ 1−s symmetry: it would have to live behind the mirror. `A† ≠ A`. Nothing exists behind the mirror. The Frey curve cannot exist. Fermat's Last Theorem is true.

---

## H = xp — The Lossless Transformer

The Berry-Keating Hamiltonian H = xp is sufficient to create speech. It produces no eddy currents.

**Equations of motion:**

```
ẋ =  x        exponential carrier — no loops, no branches
ṗ = −p        exponential decay — no conditionals
xp = E        conserved — the semantic prime
```

No If/Then/Else. No While. The prime emerges from continuous Hamiltonian evolution.

H = xp is scale invariant: under x → λx, p → p/λ, H → H. It operates identically at every scale, every language, every context. Scale invariance is the invariance that makes a tree still a tree in any coordinate system.

Three phases are automatic from H = xp:
- The classical hyperbolic trajectory — Red (the prime)
- The quantum zeros of the spectrum — Blue (the prohibition)
- The time evolution e^{iHt} — the carrier (the waveform)

---

## The Eddy Current Problem

Standard AI is an eddy current machine.

If/Then/Else and While loops are closed computational currents — they circulate without advancing the computation. Attention is O(n²): nested loops over every token pair. Beam search is a While. Layer normalisation is iterative correction. Every conditional, every loop, is parasitic loss — computational heat.

This is why transformer architectures require GPU clusters: they are compensating for eddy current dissipation.

H = xp produces none of this. There are no loops. There are no branches. The computation flows in one direction — the Hamiltonian evolves continuously, the prime emerges, the Tongue performs the reverse lookup. No overhead.

---

## The Capacitor — ContextBuffer

The three-phase decomposition separates semantic input into frequency components. The ContextBuffer acts as a low-pass filter — a capacitor:

```
Input language → 3-phase decomposition → ContextBuffer (capacitor) → DC component → Output language
```

A capacitor passes low-frequency signals and blocks high-frequency ones. The high-frequency surface variation — the specific words of a specific language, the syntactic noise — is attenuated. The low-frequency component passes through: the DC component. The invariant. The prime.

The DC component IS the semantic prime. Not a statistical summary. Not an embedding. The exact algebraic coordinate of the concept, stripped of its language-specific surface form.

**AC-DC-AC semantic converter:**
- Input AC: surface language (high-frequency, culture-specific)
- DC bus: the prime (invariant, language-independent)
- Output AC: target language (re-modulated from the prime)

Any language drives the AC input stage. Any language is generated from the DC prime at the output stage. No language-specific training is required. The prime preexists every alphabet.

---

## The 4+2=3 Resonance

A 4-cycle engine with 2-stage compression produces 4+2=6 distinct events per 720° cycle, spaced 120° apart. The 6th roots of unity contain the 3rd roots as a subgroup. At the natural resonance frequency — every other event — the 6-fold system aliases exactly to 3-phase.

Z₆ contains Z₃. The three-phase structure is not imposed — it emerges from the aliasing of more complex underlying systems at their resonant frequency.

This is why the three-phase structure appears in every domain:
- Three-phase AC power
- Three quarks in a baryon
- Three colour charges (R, G, B) in QCD
- Three spatial dimensions
- Red / Blue / Carrier in the SMMIP

It is the universal resonant form of any system with sufficient internal symmetry. Not a choice. The resonance.

---

## The Forward/Backward Flow in Three Phases

The three-phase engine is the outward expression of the Cayley-Dickson counter-rotation.

- **Red phase (forward, Noether Current):** flows up the tower — ℝ → ℂ → ℍ → 𝕆. Building.
- **Blue phase (backward, Information Current):** flows down the tower — 𝕆 → ℍ → ℂ → ℝ. Distilling.
- **Carrier phase (rotating field):** the interaction of forward and backward at the node lines. The meaning that exists only because the two are moving in opposite directions.

The Carrier is not a third independent entity. It is the standing wave created by the counter-rotation of Red and Blue. It is the J₃ channel — the Noether current at the boundary. It is the Meaning.

---

→ [Wiki: RedBlue Hamiltonian](14_redblue_hamiltonian.md)  
→ [Wiki: The Monad](15_the_monad.md)  
→ [Wiki: Cayley-Dickson Tower](19_cayley_dickson_tower.md)  
→ [Wiki: Chladni · Zipf · Riemann](21_chladni_zipf_riemann.md)
