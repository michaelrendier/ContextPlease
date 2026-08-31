# CONTEXT PRIMER — "Pinging" an RSA modulus: can the pathway view factor N?

**2026-08-31 · Claude Sonnet 5 · for anyone joining late.**

## What this is (the short version)

Cody asked whether the project's **un-sieve** / pathway machinery — the
"un-derivation engine" that runs number construction *forward* from the ground
state "just primes" — could be aimed at an **RSA modulus** `N = p·q` and made
to hand back its factors: *ping N, get its composite trajectory*. Several
concrete mechanisms were proposed over the session (a zero-divisor-anchored
spiral, a "tune per prime until it rings N" resonance, the Ulam spiral as the
search structure).

**Answer: no — and the framework explains *why* rather than threatening RSA.**
Every mechanism decomposes to a **corollary of Fermat–Coppersmith** (needs the
primes close, or half their bits known, to have a bracket) or to an
**analytic-resonance** search that still costs `√N` terms. A well-formed
balanced RSA-2048 modulus is the adversarial worst case with every exploitable
structure designed out. What the pathway view *does* give is a clean,
**forward-propagating** account of why factoring is hard and where the small
wins actually live.

---

## Terms a late joiner needs

- **The un-sieve (UNS).** Dual of the sieve of Eratosthenes. The sieve watches
  composites *die* on the pass of their smallest prime, `generation(n) =
  π(spf(n))`. The un-sieve watches them be *born*, from "just primes", the
  moment their last needed prime is switched on, `generation(n) = π(gpf(n))`.
  Engine: `FactoralDecomposition/engine/lineage.py::un_sieve`. Measured facts:
  `D == reverse(A)` exactly; `H(C) − H(A) = +7.19` bits (the *existence
  penalty*); extinction completes at `√N` (prime **313** for `N = 10⁵`), birth
  not until `N/2` (49 999); 60.5 % of composites are "born" after the
  extinction boundary. See `RiemannHypothesisProof/ADDENDUM_recursive_unsieve
  _2026-08-30.md`.
- **ADD : SCALE : SIGN.** The tier-0 floor. `N = a² − b² = (a+b)(a−b)` is the
  **SIGN axis**; Fermat's method searches it, 1-dimensionally.
- **The Two Trees.** TELPERION = prime = "what cannot be" = the *forward /
  free* direction (extinction). LAURELIN = composite = "what IS" = the
  *backward / priced* direction (existence). MINGLING = σ = ½, the critical
  line, `k ≡ n/2`.
- **Tape / no-tape.** Reverse-mode autodiff (backprop) is cheap *only given
  the recorded forward graph* (Baur–Strassen). Multiplication erases its
  operands; the sieve strike keeps no record. So **factoring is reverse-mode
  AD on a computation whose tape was wiped** — you must rebuild the un-recorded
  forward pass before any adjoint can run. That rebuild is the `+7.19`
  bits/scale. See memory `feedback-forward-propagating-maths`.

---

## The answer, in five moves

### 1. Forward vs backward = tape vs no-tape (why RSA is a trapdoor)

Multiply `p·q → N`: one pass, free, keeps no tape. Factor `N → p,q`: rebuild
the erased tape, priced. "Brute-forcing a Noether current" = recovering the
symmetry generator from a conserved charge with **no orbit data** — and the
generator *is* the factorisation. RSA's private key `d` is the saved tape;
the attacker gets `N` with the tape destroyed. "Reverse-mode with no graph"
is the definition of a good trapdoor. Instinct (the lizard-brain archive,
`B̂ = R̂†`) is the replayed forward pass off a *stored* tape; it *requires
remembering what was learned already*. Paper's Hands = the tape.

### 2. The zeta-order test — ζ re-clocks, it does not discount

`un_sieve_zeta.py` re-ran all four reads with the ordinal prime rank replaced
by five zeta-derived orders (`ln p/√p`, Riemann–Siegel `θ`, the sign of the
RS `Z`-function, the spiral phase, ordinal control). **`H(C) − H(A) =
+7.19355` bits is invariant to five decimals under every one** — the
existence penalty is a *combinatorial invariant of ℕ*, not an artefact of
counting primes in order. Zeta order only moves the **payment schedule**: an
oscillatory clock (`Zsign`, `spiral`) smears the compact extinction front
across 25–50× more generations and forces you past thousands of primes that
strike nothing before the boundary prime 313 — the exact shape of enumerating
*illegal moves in Go*. **The ordinal (smallest-prime-first) order is the
unique zero-rejection order**; that is why it is the canonical
minimum-entropy decomposition. The one thing that *does* move the gap:
clocking birth by the **real Riemann zeros** `γ_k` instead of the integers
drops `H(C) − H(A)` ≈ 15 % (`+4.30 → +3.66` b, `N = 8 000`) — the first
quantitative sense in which *ζ is the tape*. Written up as
`ADDENDUM_recursive_unsieve_2026-08-30.md` §B.1 / §D.1.

### 3. The address type system — an RSA modulus is "a word with no letters"

- **Letters** = primes `≤ √N` — the "working" primes that strike factors. In
  the Monad's 16-bit hash, `√(2¹⁶) = 256`, so **54 letter-primes** (`π(256)`).
  Closed set. Telperion.
- **Reserved slots** = primes `√N < p ≤ N` — never letters; a bare
  single-morpheme address, the "unassigned Unicode block".
- **Words** = composites. `√N`-smooth composites are built entirely from the
  alphabet; composites with `gpf > √N` are "tagged" by one large prime that
  serves as the lexeme's **serial number** (60.5 % of composites carry one).
- **An RSA modulus `N = p·q` with `p, q` both huge is a word that is 100 %
  two large-prime tags and 0 % alphabet** — unpronounceable, pure serial
  number. *That* is why it is hard: there is no alphabetic structure to read
  off. The un-sieve's "existence is expensive" at its pathological limit.

(The round-trip test — `semantic_hash_roundtrip.py` on the live 146 743-word
store — confirmed the context/semantic layers are 100 % invertible; the one
deliberate lossy step is `compress_count` at ~1 % of entries. Separate
result, folded into `FourthAgePapers/ScalarContextPropagation` G1/G2.)

### 4. The spiral / crystallography — the screw is real, the step is unknown

On a **log-polar spiral** (`r = e^{αt}`, `θ = βt`; radius `= ln n`),
multiplication by `p` is a **rigid screw** by `(ln p, β ln p)`. So `N = p·q`
sits **exactly one `p`-step past `q`** and one `q`-step past `p` — Cody's
image ("the spiral pings the modulus right after factor 2") is *literally
true*. But the step size is `ln p`, the **unknown**. `ln N = ln p + ln q` is
plain ADD — the additive shadow of the product — i.e. factoring restated.
Sweeping step sizes = trial division; anchoring the sweep at `√N` (half the
winding) and stepping outward for a square = **Fermat**.

- **Inward spiral `N → q → 1`** = division = **FREE**, *given the first step*.
  Verification is a two-step pushforward; discovery of the first step is the
  `√N` cost. The extinction/existence split, visualised.
- **Zero-divisor anchor is degenerate.** A ZD `q` has `N(q) = 0`, so `L_q` is
  singular — a multiplicative spiral anchored there has a collapsed direction.
  The corrected landmark stands: `det(L_q) = N(q)²` is a **norm invariant**,
  not a resolution; passing through a ZD leaves a *crossing record*, not
  factor information (memory `project-zd-holes-are-portals`).
- **The useful anchor is `√N`** (half-winding) → gives Fermat, the best
  geometric attack, good only for close primes.

**Ulam spiral specifics.** The prime-rich diagonals are quadratics `4n² + bn +
c`; two parallels differ by their constant term `c` — a **phase offset from
the perfect-square spine `4n² + 4n + 1`**. Prime-rich ⇔ class-number-1
discriminant (`−163` for Euler's `n²+n+41`, Rabinowitz `p ∈ {2,3,5,11,17,41}`).
The 4-fold straight-diagonal look is a **flattening artifact** of the square
winding number; on the Sacks / `√n` spiral the diagonals dissolve into smooth
radial curves. Anti-flatten coordinate: `u = ln x` (memory
`project-flattening-syndrome`). In UNS colouring: a thin prime-diagonal spine
under a stack of `gpf`-cohort moiré layers ordered by `π(gpf)`.

### 5. The complexity verdict — c-factor vs α-drop, granularity + jurisdiction

`L_N[α, c] = exp(c·(ln N)^α (ln ln N)^{1−α})`.

- **Orders of magnitude come only from dropping `α`:** trial `1` → quadratic
  sieve `½` → GNFS `⅓` → Shor `→ 0`. Or from *per-instance* structure: close
  primes (Fermat/Coppersmith, poly if `|p−q| < N^{¼}`), smooth `p ± 1`
  (Pollard), known high bits (Coppersmith), primes shared across many keys
  (batch GCD).
- **Cody's ~97 % reduction (≈ 33×) is a `c`-factor** — it *subtracts*
  `ln(1/0.03) ≈ 3.5` nats from `ln L`. At RSA-768 (`ln L ≈ 34`) that's 10 %;
  RSA-2048 (`≈ 81`) 4 %, ~210 modulus bits; 20 000 digits (`≈ 336`) 1 %.
  Sublinear frontier shift; the fraction of keyspace it unlocks → 0.
- **Granularity.** "x-length in digits" is a **log-axis quantization**. The
  cost surface is *flat inside each digit-class pixel* (`ln L` varies < 1 %
  across a whole 20k-digit band) — difficulty is a property of the digit
  class, not the number. There is no finer signal to exploit. Higher
  magnitude = finer grit = more resolution elements, same flat colour.
- **Jurisdiction.** The `c`-factor lives in the **arithmetic-implementation**
  jurisdiction (how fast you multiply, how compact the representation — the
  hyperindexer / box-kite territory). The `α`-drop lives in the
  **algorithmic-structure** jurisdiction. Cody's reduction has standing only
  in the first and cannot reach the lever in the second.
- **"The ripples are drowned out by the white-topped waves."** Physically
  exact: ripples *are* capillary (surface-**tension**) waves; whitecaps *are*
  wind-driven gravity waves. The `c`-factor / fine structure is a fixed
  ~3.5-nat ripple; `ln L` is the swell, growing as `(ln N)^{⅓}`; wind speed =
  `ln N` = the digit count. Closes back to the session's opening principle —
  *"the tension is not important… only the wind speed."* Ripples read only in
  dead calm: right at the feasibility shoreline (RSA-768 → 1024).

---

## Bottom line

**No new generator.** The pathway / crystallography view *visualises* and can
*tighten* Fermat–Coppersmith and the analytic-resonance direction; it cannot
manufacture a bracket for a well-formed balanced modulus. Where it has teeth:
unbalanced `N` (ECM), close primes, smooth `p ± 1`, shared primes — all
designed out of well-generated RSA-2048. A `c`-factor is a `c`-factor.

The lasting products of the thread are elsewhere: the **forward-propagation
design rule** (memory `feedback-forward-propagating-maths`), the **zeta-order
invariance** result (`ADDENDUM` §B.1/§D.1), and the **address type system**
(letters ≤ √N / reserved / words / tagged words).

## Artifacts

- `ContextPlease/claude/scratchpad/2026-08-30_prime-dna/` — `un_sieve_zeta.py`
  + `_RESULTS.md`, `semantic_hash_roundtrip.py` + `_RESULTS.md`,
  `energy_bench.py`, all outputs.
- `RiemannHypothesisProof/ADDENDUM_recursive_unsieve_2026-08-30.md` §B.1, §D.1.
- `FourthAgePapers/ScalarContextPropagation` (branch) — energy §"The price,
  measured", G1/G2 round-trip subsection.
- Prior primer: `PRIMER_2026-08-30_UNSIEVE_BERRY_KEATING.md` (same dir).

## Cross-refs

`[[project-two-trees-lio]]`, `[[project-null-operator-rb]]`,
`[[project-zd-holes-are-portals]]`, `[[project-flattening-syndrome]]`,
`[[feedback-forward-propagating-maths]]`,
`[[project-factoral-decomposition-tool]]`,
`[[project-minds-eye-papers-hands]]`.
