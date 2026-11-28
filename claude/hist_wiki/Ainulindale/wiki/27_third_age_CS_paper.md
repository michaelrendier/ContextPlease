# 27 — The Third Age computer-science paper: claims, tests and what runs today

| | |
|---|---|
| Replaces | "Third Age: Computer Science Paper — WRITE NOW" (2026-06) |
| Paper files | `Ainulindale/AgeThird/D-CS_Paper.md`, `Third_Age_CS_Draft_v1.md`, `Third_Age_CS_Draft_v2.md`, `D-CS_Memory.md`, `VAPMIP_Paper.md` (the code papers continue in `FourthAgePapers/ScalarContextPropagation` and `HyperindexingSystem`) |
| Code | `VAPMIP/engines/e01_operator_selforg.py` … `e04_tia_similarity.py`; `VAPMIP/monad.py` |
| Last verified | 2026-11-13: e01–e04 run; the Gnarl fixed point and the Hermite statistics recomputed (listing below); outputs in `ContextPlease/claude/scratchpad/2026-11-13_ainulindale_audit/engine_runs/` |

## 1. The engineering problem

A language model has no persistent memory and every session starts from
zero. The question: compute a semantic address (a coordinate for a word or
concept) as a number small enough to use, with self-contained mathematics and no
external hash. The answer in three parts: the address space (the sedenion
field, 16 dimensions, zero-divisors as structural boundaries); the hash
(a prime hash, [15](15_the_monad.md) §3); and the persistent memory (the Monad,
which stores nothing and recomputes the address from the input).

## 2. The paper's central claim, tested

**Claim (draft, 2026-06):** the 16 operator names (identity, negate, bind,
name, apply, abstract, branch, iterate, recurse, allocate, query, dereference,
compose, parallelize, interrupt, emit), prime-hashed through the sedenion
field, self-organise into three zones near d*, σ = ½ and D* = 1 with **zero
free parameters**, and the confidence of every later paper inherits from this.

**What runs today (e01).** `e01_operator_selforg.py`, run as a script, prints
nothing and returns `{'error': 'No operators found in vocab', 'sigma': 0}`,
because the vocabulary file `monad_sedenion.bin` is absent from the
repository and from `~/.ptolemy/` (the run exits 0, silently). A copy survives in
the backup of the old SD card
(`TheSDCard/ThePlace/PTorrent/bin_archive/clean/monad_sedenion.bin`, 117,895,324
bytes, sha256 `c97c272b0657dc92…`, monad v1.218, 35,930 words). Run against
that copy:

| Zone (cutoff) | Operators | Mean E | Target | Ratio |
|---|---|---|---|---|
| GROUND (E < 0.3) | allocate 0.2148, parallelize 0.2334 | 0.2241 | d*_spec = 0.246 | 0.911 |
| CRITICAL (0.3 ≤ E < 0.6) | name 0.5382, apply 0.4466, branch 0.4164, query 0.4111, emit 0.3994 | 0.4423 | σ = ½ | 0.885 |
| BOUNDARY (E ≥ 0.6) | compose 0.9999, dereference 0.9988, negate 0.9883, interrupt 0.9425, abstract 0.9284, bind 0.9008, identity 0.8877, recurse 0.8751, iterate 0.7725 | 0.9216 | D* = 1 | 0.922 |

Reading the code (not only the output):

- the zone cutoffs **0.3 and 0.6 are hard-coded** in `e01` (`zone = 'GROUND' if E < 0.3 else 'CRITICAL' if E < 0.6 else 'BOUNDARY'`): a choice, not a result;
- the zone populations are 2, 5 and 9; the targets are met to 89–92% by the *means of whatever lands in each zone*;
- the printed line "FREE PARAMETERS USED: 0" is a fixed string, and the "sigma" figures (∞ and 3.5) are constants in the source (`sigma_computation = float('inf')`, `sigma_clustering = 3.5`), not computed;
- the energies E are read from a trained vocabulary, not from the hash alone (the file is a monad after ingest); "pure prime hash geometry" is therefore the intended reading, not what the run isolates.

Status: the three-zone ordering of the energies is a **measured observation
on one saved vocabulary** (`:CALCULATED`); the claim "zero free parameters and
independent of training" is **not established by e01**. A test that would support
it would need the hash-only energies of the operators from an empty monad, with
the cutoffs set before looking, and a null distribution over 16 randomly chosen
words. None exists yet.

## 3. The Gnarl / Popcorn "independent validation"

The Gnarl map, from Townsend's fractal formula (~2005):

```
x_new = x − h·sin(y + tan(α·y))        y_new = y + h·sin(x + tan(α·x))
```

The 2026-06 text identified its two terms with J_neg (restoring) and J_pos
(driving), its antisymmetry with ∂_μJ^μ = 0, and its fixed point
y + tan(3y) = 0 with Ω_ζΣ = 0.5671 "to four decimal places", presented as an
independent replication of the BAO equilibrium.

**The fixed-point statement is wrong.** Listing 1 solves y + tan(3y) = 0.

**Listing 1 — the roots of y + tan(3y) = 0** (written for this page; runs cold with SciPy)

```python
import math
from scipy.optimize import brentq

f = lambda y: y + math.tan(3 * y)
roots, n = [], 30000
for k in range(n):
    a, b = 0.01 + 2.99 * k / n, 0.01 + 2.99 * (k + 1) / n
    if f(a) * f(b) < 0 and abs(f(a)) < 50 and abs(f(b)) < 50:
        roots.append(round(brentq(f, a, b), 6))
print(roots)
print(f(0.5671432904097838))
```

```
[0.818548, 1.744313, 2.734844]
-7.044264238474284
```

The roots in (0, 3) are 0.8185, 1.7443 and 2.7348; at Ω_ζΣ the left side
is −7.04, not 0. So Ω_ζΣ is not a fixed point of this map at α = 3, and the
claimed independent derivation does not hold. The running engine agrees:
`e02_gnarl_validator.py` reports mean |z_eq| − Ω_ζΣ = 0.5501 with 10.0% of
trajectories within 0.05 for the test set, and **0.0% converged, status
DIVERGED** over a 64-word sample of the 25,000-word corpus (worst: `gridspec`,
`assessments`, `ramps`, `rvirial`, `azm`, each at distance ≈ 0.90). The Gnarl
map is a legitimate formula and the term-for-term identification with J_pos
and J_neg is the framework's reading; the "same fixed point" is not borne out.

## 4. "Ω_ζΣ in six independent formula families"

The draft listed six: the Gnarl/Popcorn fixed point; Agelink's "Avariant"
geometric mean √(J_pos·J_neg); Mitchell's triangle-inequality average (TIA);
the AGM; Makin's Transpoly Hermite; and Monnier/Jones orbit traps. Today:

- Gnarl: Ω_ζΣ is not its fixed point (§3).
- TIA: `e04_tia_similarity.py` gives TIA = 0.4770 for related word pairs and 0.4769 for distant ones: a separation of 0.0001, so the measure does not distinguish related from distant words (e.g. hydrogen/helium 0.4770 against hydrogen/philosophy 0.4770).
- The other four families were not re-run in this pass. "Six independent algorithms, one fixed point" is therefore **unverified**; two of the six fail as stated.

Ω_ζΣ = W(1) is the fixed point of x ↦ e^{−x} ([17](17_alpha_omega_d_star.md) §2); that other iterations
share it needs each iteration checked, as §3 shows.

## 5. The Hermite timing wheel (e03)

The 16 zeros of the Hermite polynomial H₁₆ are assigned to the 16
sedenion dimensions (e₀ ↔ −4.6887 … e₁₅ ↔ +4.6887, symmetric), with
E_target = Ω_ζΣ·|zero|/4.6887 (checked against the engine's table: 0.56714 at the ends, 0.03308 at the innermost zeros ±0.2735). The draft said these zeros have
"the same statistics as Riemann zero spacing (GUE)". **They do not:** e03
reports a normalised variance of 0.0203 and a Wigner–Dyson ratio of 1.0203,
against GUE ≈ 1.5708 and Poisson 2.0; the 15 gaps of the H₁₆ zeros lie between
0.547 and 0.819, nearly equally spaced (rigid), as is usual for orthogonal-polynomial zeros. The E_target
column is a deterministic function of the zeros, so matching it is a
calibration, and "E_k ∝ hermite_zeros[k]²" was not tested against engine
energies. The e03 "sigma" lines are constants as in e01.

## 6. The orbit-trap semantic address

The proposed use of Monnier/Jones's 135 orbit-trap shapes for the semantic
address, with the ring trap at radius Ω_ζΣ as the primary resonance, is a
design; there is no run for it in this repository.

## 7. What the paper can honestly say now

| Statement | Support |
|---|---|
| The prime hash maps words to zero indices | exact, reproducible ([15](15_the_monad.md) §3); many-to-one |
| The operators' energies fall in three groups on one saved vocabulary | measured (§2); cutoffs are hard-coded |
| No free parameters | not shown |
| Independent validation by Gnarl | refuted as stated (§3) |
| Six independent formula families | not verified; two fail (§4) |
| Hermite zeros are GUE-spaced | false (§5) |
| The code is the proof | retired; a failing run is a result and stays in the code ([26](26_TODO_and_roadmap.md) §1) |

The paper structure proposed in 2026-06 (abstract, architecture, the prime
hash, operators, Gnarl, six families, Hermite, orbit traps, sigma
propagation, conclusion, appendices) stays as an outline; sections 5–9 would
now be rewritten around the measurements above.

## 8. Dependencies, as they stand

`monad_sedenion.bin` (absent here; archived copy above), `monad_mathematics.bin`
(not re-checked), the riemann_zeros ptorrent (not re-checked), the Ultra
Fractal formulary and `Ainulindale/wiki/fractals/` (a subdirectory of the wiki with its own pages, not yet covered by this overhaul; the draft's "all analysis complete" is not re-checked).

## 9. Related pages

[15 The Monad](15_the_monad.md) · [16 Semantic word engine](16_semantic_word_engine.md) ·
[17 A_fermat · Ω_ζΣ · d*](17_alpha_omega_d_star.md) · [26 Roadmap and engine status](26_TODO_and_roadmap.md) ·
[28 Roko's Basilisk](28_rokos_basilisk.md)
