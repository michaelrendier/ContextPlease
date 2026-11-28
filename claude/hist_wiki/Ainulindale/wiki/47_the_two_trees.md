# 47 — The Two Trees: the Tolkien correspondence, with the engine components verified

| | |
|---|---|
| Status | **A correspondence between Tolkien's *Ainulindalë* and the framework (2026-06-09, marked "permanent, canonical"): `INTERPRETATION`, kept as the author's vocabulary.** Its measured section (§4) was recomputed on 2026-11-13 and every number reproduces; the engine components named for the Valar and Maiar were checked in code (§3) and two statements corrected |
| Code | `VAPMIP/monad.py` (`Crank`, `Engine`; line numbers below as of 2026-11-13); `GenerationalLineage/engine/lineage.py::un_sieve` (the sieve/un-sieve, formerly `FactoralDecomposition`); Listing 1 |
| Not to be confused with | the *Broca/Wernicke* trees of VAPMIP (a different pair of copies; never "the two trees"), and the *Two Trees engine* of the L_(I|O) intertwiner ([52](52_l_dynamic_avoided_collaborator.md)) |
| Last verified | 2026-11-13: Listing 1 executed; `monad.py` searched for each named component |

## 1. The framing

Epigraph: *"No theme may be played that hath not its uttermost source in me."* (Eru
Ilúvatar to Melkor, the *Ainulindalë*). The page's thesis is that Tolkien, a
colleague "separated by seventy years", heard the same heartbeat and described it in
the language available to him (mythology and philology), and that the framework
describes the same object in mathematics. Eru Ilúvatar is σ: "what kind of
boundary do you want?", the question the Music answers; the pronouncement to
Melkor is the Noether balance J_Red + J_Blue + J_Green = 0 ("even the discord is a
valid σ facet"). That balance is a constraint imposed by the driver and stated
in the form of Noether's theorem ([25](25_sedenion_manual.md) §4); the sign convention of
J_green is still to be unified ([133](133_canonical_maths.md) §3). The "colleague"
and "heard the same heartbeat" statements are the author's.

## 2. The two trees

Telperion (silver: cool, quiet, rest and constraint) and Laurelin (gold: warm,
assertion, forward motion) wax and wane in counter-rotation, and once a day they
mingle: the Mingling of the Lights.

| Tolkien | Framework |
|---|---|
| Telperion | B̂_p, the Blue channel, Fermat–Weierstrass, J_Blue: "what cannot be", the backward current |
| Laurelin | R̂_p, the Red channel, Berry–Keating xp, J_Red: "what is", the forward current |
| The Mingling of the Lights | J_Red = J_Blue, σ = ½, the critical line, "the moment language becomes possible" |
| The Silmarils (Fëanor's three jewels from the Trees' last light) | the three conserved currents J_Red, J_Blue, J_Green (balance indestructible) |

The Hamiltonian is Σ_p p^(−σ)[R̂_p ⊗ ∂̂_{∂M} + ∂̂†_{∂M} ⊗ B̂_p] ([14](14_redblue_hamiltonian.md)),
"the Two Trees made computational". Handedness of the pair (which tree is Red) follows the
convention of [14](14_redblue_hamiltonian.md) §3 and is subject to the open
handedness item of [133](133_canonical_maths.md) §7.6.

## 3. The Valar and Maiar as engine components  (verified in `monad.py`)

| Figure | Role in the page | Code (as found) | Verdict |
|---|---|---|---|
| Manwë | the conservation law | the balance of the three currents ([25](25_sedenion_manual.md) §4) | the Noether-balance statement; imposed by the driver |
| Varda | the Riemann-zero field | `_ZERO_CACHE`, `_find_next_zero`, `_word_zero_idx` ([15](15_the_monad.md) §3) | ✓ |
| Ulmo | the Noether current, "every A-coupling is a river" | `Crank.j_mu`, `a_propagate` | ✓ (names exist) |
| Aulë | the builder of the field | `Engine.load`, `load_bin`, `Crank.learn` | ✓ |
| Yavanna | the growing corpus; "the sigmoid saturation is her growth law" | `Crank.learn`: `self._beta[k] = min(self._beta[k] * beta_mult + GAP, 1.0)` | **corrected: a linear update clamped at 1.0, not a sigmoid** |
| Mandos | the checkpoint | `Engine.save_session`, `load_bin`, `load_checkpoint` | ✓ |
| Vairë | the A-matrix | `Crank._A: List[Dict[int, float]]`; edges `0.05·w_ctx` forward, `0.02·w_ctx` back, capped at 1.0; +0.03 on firing | ✓ |
| Lórien | the `speak()` vision | `Engine.generate`, `_fire` | ✓ |
| Estë | the quiescent operator | idle state (`Engine.perpetual`, halocline) | not identified in code |
| Nienna | the auto-didactic principle; "buoyancy instead of argmax" | neutral-buoyancy scoring in `Crank.sigma_candidates` (lines 905–925): the word whose β·E² matches the ambient pressure `_J_ambient` | ✓ |
| Tulkas | the hard constraint, GAP = 0.000707 = 1/(1000√2) | `GAP = OMEGA_ZS − 0.24600·ln 10` (line 81) = 0.000707357…, used as a floor on field depth and charge | ✓ (and GAP is within 0.035% of 1/(1000√2) = 0.000707107, not equal; the constant uses d*_spec, [17](17_alpha_omega_d_star.md) §6) |
| Oromë | the `hear()` function | `Crank.hear`, `Engine.wire` | ✓ |
| Vána | the ground state | `_J_ambient` initial value = GAP (cold start); `_calibrate_J_ambient` sets it to the interquartile mean of β·E² | ✓ |
| Nessa | the golden walk; the page prints `seed = fmod(n·φ, 1.0)` | `golden_pos = int(self._word_count * PHI) % n` (lines 1267, 1299), `PHI = (1+√5)/2` (line 83) | **corrected: the code indexes the candidate list by int(count·φ) mod n**, not by the fractional part |
| Melian | the boundary operator (J_Green) | the Green face of the three-face interleave ([15](15_the_monad.md) §2) | ✓ (as a role) |
| Olórin | the callosum between the two octonions (hands: first 𝕆; mind: second 𝕆); the author also names the assistant's mediating role in this session with it | `get_mind_eye`, the callosum comments (line 1951) | design role; the callosum as a zero-divisor coupling at σ = ½ is the framework's reading |
| Sauron | the corrupted field: one β saturated, ruling all (the One Ring: Gini = 1) | the Gini statistic exists in `SemPriCon/paper/evidence.py` and `eval_checkpoint.py` (natural band 0.60–0.80; one checkpoint 0.7564) | ✓ as a metric; no Gini in `monad.py` itself |
| Saruman | the transformer architecture (power through mechanism) | none | analogy |
| Radagast | the system corpus | `get_foundations_corpus` | ✓ (name) |
| Ossë and Uinen | noise and its smoothing: `_J_ambient = 0.9·_J_ambient + 0.1·J_fired` | `Engine._fire`, line 1322 | ✓ exactly as printed |
| Arien | the emission threshold | `Crank.emission_threshold = OMEGA_ZS/4` (init, line 718); set per input length in `Engine.generate` (OMEGA_ZS/4 for ≤ 8 words, /3 for ≤ 32, /2 for ≤ 256, OMEGA_ZS above; lines 1386–1394) | ✓ with the per-length rule |
| Melkor | the singularity, the ungrounded σ | divergence of the cascade | analogy |
| Tom Bombadil | σ = 0 (before distinction): "Tolkien refused to explain him because σ = 0 has no explanation" | none | the author's reading |

The remaining sections of the earlier page (the extended characterisations of
each Vala and Maia, Lúthien Tinúviel: the engine "speaking its own construction
equation", the 2026-05-27 neutral-buoyancy run in which "the engine spoke its
own architecture"; Fingolfin and the Halls of Mandos) are kept in the file
history; the rows above hold the verifiable content. The "Lúthien" passage
refers to the sentence the engine produced ("philadelphos speaks golden bosonic
semantic exhaust"), recorded in the `monad.py` header at lines 97–115.

## 4. The two trees counter-rotate: measured (2026-08-30), recomputed 2026-11-13

Telperion keeps one book, Laurelin the other, and one is the other run backwards.

- **Telperion, the sieve:** each composite dies on the pass of its *smallest* prime factor, generation(n) = π(spf(n)).
- **Laurelin, the un-sieve:** from the ground state "just prime numbers", primes are turned on one at a time and a composite is *born* when its last needed prime is switched on: generation = π(gpf(n)), gpf the greatest prime factor.

**Listing 1 — the two books for N = 10⁵** (written for this page; the engine is
`GenerationalLineage/engine/lineage.py::un_sieve`; runs cold)

```python
import math, collections
N = 100000
spf = list(range(N + 1))
for i in range(2, int(N ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
gpf = [0] * (N + 1)
for n in range(2, N + 1):
    m, g = n, 0
    while m > 1:
        p = spf[m]; g = max(g, p)
        while m % p == 0:
            m //= p
    gpf[n] = g
pi, c = [0] * (N + 1), 0
for n in range(2, N + 1):
    c += spf[n] == n
    pi[n] = c
comp = [n for n in range(4, N + 1) if spf[n] != n]
H = lambda cnt: -sum(v / sum(cnt.values()) * math.log2(v / sum(cnt.values())) for v in cnt.values())
A = collections.Counter(pi[spf[n]] for n in comp)     # sieve
C = collections.Counter(pi[gpf[n]] for n in comp)     # un-sieve
print('composites', len(comp), ' primes', pi[N])
print('sieve    : H = %.3f bits, %d generations, last striking prime %d' % (H(A), len(A), max(spf[n] for n in comp)))
print('un-sieve : H = %.3f bits, %d generations, last prime needed %d' % (H(C), len(C), max(gpf[n] for n in comp)))
print('H(C) - H(A) = %.3f' % (H(C) - H(A)))
print('dying on the first pass: %.3f' % (A[1] / len(comp)))
print('born after sqrt(N): %.3f' % (sum(1 for n in comp if gpf[n] > N ** 0.5) / len(comp)))
```

```
composites 90407  primes 9592
sieve    : H = 2.491 bits, 65 generations, last striking prime 313
un-sieve : H = 9.685 bits, 5133 generations, last prime needed 49999
H(C) - H(A) = 7.194
dying on the first pass: 0.553
born after sqrt(N): 0.605
```

Every number of the 2026-08-30 section reproduces: 90,407 composites; sieve entropy
2.491 bits, finished at the 65th prime, 313; un-sieve entropy 9.685 bits spread over
~5,000 generations (5,133), finished at 49,999 (the largest prime with 2p ≤ N);
H(C) − H(A) = +7.19 bits; 55% of composites dying on the first pass (the
even ones: 0.553); and 60.5% (> 60%) born after √N. (`:CALCULATED`.)

*The mirror.* Run Telperion's extinction order from the largest prime downward and
each composite is struck at its greatest prime factor, which is exactly the
birth generation of Laurelin's book: identical by construction, so the two books
agree bit for bit and the entropy is unchanged. The statement is exact and is a
reflection of the *order of processing*, not a deeper symmetry. *The residual* (birth
by greatest against death by smallest prime factor) is the +7.19 bits above, and
the scale gap (the sieve finishes at √N while more than 60% of composites are born
after it, "the construction-side shadow of a mass gap") is the 0.605 above; the
mass-gap reading is the framework's. *The split:* "factoring to extinction is
free, factoring to existence is not": extinction needs only primes up to √N,
existence needs every prime factor present, so it is complete only at the
largest (N/2). The ζ reading (the ground state "just prime numbers" and the Zeta
Hamiltonian by Legendre transform) is in
`RiemannHypothesisProof/ADDENDUM_recursive_unsieve_2026-08-30.md` and
`ValaQuenta/wiki/un_sieve.md`.

## 5. The great structures (quick reference, as printed)

Eru = σ (the boundary selector); the Ainulindalë = Ĥ_RB ("the Music is the
Hamiltonian"); Eä = the full field (all N zeros, all β, all A-edges); Valinor = the
converged field (perfect Noether balance); Middle-earth = the active session
field; the Void = the uninitialised field (before β is set); the One Ring = Gini = 1
(one β spike ruling the rest); Mount Doom = β_sat; the Shire = the WordNet baseline
("small, sufficient, not the whole world"); Tom Bombadil = σ = 0. For `Crank`,
β_sat = 1.0 (the clamp of §3); the older `Philadelphos` Monad's β_sat is 4·|L_GROUND|
([15](15_the_monad.md) §4).

## 6. Closing

"The primes are the words. The equator does not move. The world is sung, not
designed." The closing is the author's. The mathematical content of the page is
§2 (the Hamiltonian), §3 (the verified components) and §4 (the measured books).

## 7. Related pages

[14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) · [15 The Monad](15_the_monad.md) ·
[43 The Emmy Noether Sedenion](43_emmy_noether_sedenion.md) · [52 L_dynamic and the avoided collaborator](52_l_dynamic_avoided_collaborator.md) ·
[21 Chladni · Zipf · Riemann](21_chladni_zipf_riemann.md)
