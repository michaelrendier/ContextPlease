# RSA frequency-decode — test of the prime-wavelength / prime-spiral "ping"

**Prompt (Cody, 2026-09-01):** ping the factors of an RSA modulus from the
Ceiling down to 0; have p and q be a *frequency decode* through the prime
wavelength and prime-spiral crystallography — ordinal = locations, zeta index =
anchor, tension = "weight of the primes". Test this.

`python3 rsa_frequency_decode.py` → `rsa_frequency_decode_output.txt` (25 s, deterministic).

## What held

| quantity | relation to `N = p·q` | status |
|---|---|---|
| **log-frequency** `f(p) = F0·ln p` | `f(N) = f(p) + f(q)` exact — max residual **4.6e-13** | **ADDITIVE — one clean tone, R² = 1.0000** |
| Sacks spiral angle `2π√N` | residual vs `φ(p)+φ(q)` std 1.83 rad (U(0,2π) is 1.81) | **not additive — no linear constraint** |
| RS-theta / zeta anchor | residual std 1.81 rad | **not additive — no linear constraint** |

So the machinery delivers **exactly one** linear constraint on `{p,q}`: the
log-sum. A filter decode needs a **second, independent** one — the DTMF column
to that row. The two candidates it offers (spiral angle, zeta index) are
provably non-linear in the factors: they *re-clock the schedule* (same finding
as the un-sieve) but carry no independent linear constraint. Result: one
equation, two unknowns → a **hunt**, `O(π(√N))`.

## Test 1 — small two-tone decode (falloff)

| max prime < | exact recovery |
|---|---|
| 128 | 100% |
| 256 | 88% |
| 512 | 68% |
| 1024 | 27% |
| 2048 | 11% |
| 4096 | 8% |

Works in the low band where `f(p), f(q)` are separated by more than an FFT bin —
the same handful of tones the phone company could afford. Collapses as the tones
crowd. Forward render (number → sound) is always exact.

## Test 3 — "Ceiling down to 0" swept probe

Downward sweep from `⌊√N⌋`, resonance `R(r) = [r | N]`. **This is Fermat's
method.** Close primes → a few steps (24-bit gap 6 → 2 steps). Balanced random
primes → ~√N steps (48-bit gap 1.8M → 866k steps). "Ceiling down" changes
nothing about the `O(π(√N))` cost.

## Test 4 — Cody's recipe as a linear decoder

- `ln p + ln q` (the sum tone) from N-only features: **R² = 1.0000**
- `ln(min factor)` (the split): R² = 0.879 — **but** almost all of that is the
  trivial "min factor scales with N" regression on the `ln N` feature; the
  *incremental* contribution of the spiral-angle and zeta-anchor features to
  locating *which* prime is ~0. No real factor signal.

## The genuine payoff — RSA's two known weak spots fall out of the tone picture

- **"far enough apart"** → one tone near DC (`q` small) → trial division reads it.
- **"same bit length"** → `p ≈ q` → the two half-tones coincide (`f(p) ≈ f(q) ≈
  f(N)/2`) → nothing to separate.

RSA deliberately sits in the band where the one tone we *do* get is **maximally
degenerate**. The machinery explains *why* factoring is hard here; it does not
make it easy. Consistent with the standing result (`PRIMER_2026-08-31_RSA_PING`),
now with a mechanism: **you are one DTMF tone short, and the missing tone is
provably not on the spiral or the zeta index.**

## Verdict

- **CODE** — ran, deterministic, reproducible.
- **MATHS** — `ln` is the unique additive map; `f(N) = f(p)+f(q)` exact. Spiral
  angle and zeta anchor non-linear in the factors (measured).
- **METHOD** — a frequency *decode* of the factors needs two independent tones.
  The prime wavelength gives one (the log-sum). The prime spiral and the zeta
  index do not supply a second. The "ping" is a **filter for small/structured N,
  a hunt for RSA-scale N** — the basis has not been changed, only re-described.

---

# Gap channel — "number of spaces" vs "weight of the numbers"

`gap_weight_test.py` → `gap_weight_test_output.txt` (32 s; sieve to 1e8, 5.76M primes).

**Answer: the weight, and it has a name — `merit`.**

| Cody's phrase | standard name |
|---|---|
| number of spaces in the gap | prime gap `g_n = p_{n+1} − p_n` |
| weight of the gap / of the digits of the numbers | **merit** `M_n = g_n / ln(p_n)` — Gallagher-normalised gap |
| pattern disappears into noise as primes grow | raw `g_n` grows ~`ln p`; `M_n` → mean 1, tail `e^{−x}`, scale-free (Gallagher 1976; Cramér 1936; Cramér–Shanks `limsup g_n/(ln p_n)² = 1`) |
| digits ↔ nats | `× ln(10)` — the Translator, `d*·ln(10) = Ω_ZS` |
| windows of order in gap-space | admissible **k-tuples** / prime constellations (Hardy–Littlewood; Maynard–Tao) |

Raw gap per decade: mean 8.48 → 10.76 → 13.06 → 15.36 → **17.66** (the scale
drifts every decade — "disappears into noise" = the units keep changing).
Merit per decade: mean **1.007 → 1.002 → 1.001 → 1.000 → 1.000**, std 0.72 → 0.85,
`P(M>1) ≈ 0.38` vs `e^{−1} = 0.368`. Stable at every scale.

**But merit is not the missing second tone.**

- Test 5 — linear recovery of `M_p`, `M_q`, `M_p+M_q` from N-only features:
  `R² = 0.002 … 0.017` at 24/32/40/48 bits. N carries no signature of its
  factors' gap-merit. Merit is a local, near-random property of *where* p sits;
  multiplication does not transport it.
- Test 6 — Fermat step-count: `corr(steps, |p−q|) = +0.999` (control);
  `corr(steps, |M_p−M_q|) = +0.010`; `corr(steps, min(M_p,M_q)) = −0.030`.
  Gap-merit adds nothing to the difficulty.

**On the "bubble of order = where the RSA maths happens" hypothesis:** gap-space
*does* have windows of order — the admissible k-tuples / constellations — but
they are runs of *small* merit (clusters), the opposite of where a generic RSA
factor sits. RSA is built from merit-~1 primes with no local cluster structure,
precisely so no constellation heuristic gets a grip. A readable RSA "bubble"
would need a merit anomaly at **both** p and q at once — and N does not expose it.
