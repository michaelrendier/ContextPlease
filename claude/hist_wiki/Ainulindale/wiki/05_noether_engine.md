# 05 — Noether Engine ∂_μ J^μ = 0

| | |
|---|---|
| Module | `noether` — `ValaQuenta/modules/noether/` |
| Class | `NoetherModule` |
| Version | 0.111 |
| Confidence floor | THEORETICAL |
| API page | `ValaQuenta/wiki/noether.md` |
| Notebook | `ValaQuenta/notebooks/core/05_noether.ipynb` |
| Last verified | 2026-11-13, against the live registry (6 equations) |

## 1. Definition

Each continuous symmetry of L_NN ([04](04_lagrangian_engine.md)) carries a
conserved current, J^μ, with ∂_μ J^μ = 0. The module computes the current
for the gauge group of each algebra stratum and the size of its violation.

| Stratum | Symmetry | Current | Generators (`N_GEN`) |
|---|---|---|---|
| ℝ | trivial | — | 0 |
| ℂ | U(1) phase | J^μ = g Ψ̄ Ψ | 1 |
| ℍ | SU(2) isospin | J^μ_a = g Ψ̄ T^a Ψ | 3 |
| 𝕆 | G₂/SU(3) | J^μ_a = g Ψ̄ T^a Ψ | 8 |

## 2. Violation diagnostic

The violation is the finite-difference size of the change in J between
successive layers:

```
violation = |∂_μ J^μ|  ≈  mean | J_curr − J_prev |
```

It is classified by the thresholds in `noether.maths.THRESHOLDS`
(`PASS` = 0.2, `MARGINAL` = 0.5):

| Violation | Status | Meaning |
|---|---|---|
| < 0.2 | PASS | symmetry conserved |
| 0.2 – < 0.5 | MARGINAL | boundary stress |
| ≥ 0.5 | VIOLATION | an algebra boundary has been crossed |

**Listing 1 — the classifier** (`modules/noether/maths.py`,
`conservation_status`; extracted: docstring removed, thresholds inlined from
`THRESHOLDS`, runs cold)

```python
THRESHOLDS = {'PASS': 0.2, 'MARGINAL': 0.5}

def conservation_status(violation):
    if violation < THRESHOLDS['PASS']:
        return 'PASS'
    elif violation < THRESHOLDS['MARGINAL']:
        return 'MARGINAL'
    return 'VIOLATION'
```

On a single call with no previous J (`J_prev` is `None`) the violation is 0.0
and the status is PASS; a meaningful value needs a second layer.

Resonance artifacts (`resonance_artifacts`) are oscillations in the J⁰
history, detected by counting zero-crossings across layer steps; the period
estimate is 2·N_layers / N_crossings. This is a diagnostic, not a derived
quantity.

## 3. The ledger

Every violation event can be recorded to a SHA-256 hash chain
(`NoetherLedger`). A block is:

| Field | Content |
|---|---|
| `index` | position in the chain |
| `timestamp` | `time.time()` |
| `algebra`, `gauge` | stratum name and gauge group |
| `violation`, `status` | magnitude and its classification |
| `J` | the current vector, rounded to 8 places |
| `prev_hash` | hash of the previous block (genesis = 64 zeros) |
| `metadata` | optional, present only if supplied |
| `hash` | SHA-256 of the JSON-serialised block, keys sorted, excluding `hash` |

The chain is append-only and tamper-evident: `verify()` returns
`{'valid', 'broken_at', 'length'}`. An empty chain verifies as valid with
length 0. The hash is the ordinary SHA-256 of the standard library; the ledger
is an integrity record, not a consensus mechanism. The planned export to
Kryptos / PtolBus is not wired in this repository.

## 4. Equations

| Name | Tier | Parameters |
|---|---|---|
| `conservation_diagnostic` | THEORETICAL | `psi_norms`, `g`, `algebra` |
| `violation_scan` | THEORETICAL | `psi_norms`, `g` |
| `resonance_artifacts` | THEORETICAL | `n_steps`, `g`, `algebra` |
| `blockchain_record` | ESTABLISHED | `algebra`, `violation`, `g` |
| `blockchain_verify` | ESTABLISHED | — |
| `blockchain_summary` | ESTABLISHED | — |

## 5. Session

```
>>> registry.run('noether.conservation_diagnostic', {'psi_norms': [0.5, 0.4, 0.3], 'g': 0.01, 'algebra': 1})
{'J': [0.005], 'J_prev': None, 'violation': 0.0, 'status': 'PASS', 'conserved': True, 'delta_J': 0.005, 'algebra': 'ℂ', 'gauge': 'U(1)', 'n_gen': 1, ...}
>>> registry.run('noether.blockchain_verify', {})
{'valid': True, 'broken_at': None, 'length': 0}
```

## 6. Boundaries

- The thresholds 0.2 and 0.5 are engineering settings, not derived values.
- That the violation score serves as a training convergence criterion in
  place of gradient descent is a design claim; no trained network is in this
  repository (see [12](12_smnnip_distribution_engine.md)).

## 7. Related pages

[04 Lagrangian](04_lagrangian_engine.md) · [06 Noether information](06_noether_information_engine.md) ·
[43 Emmy Noether and the sedenion](43_emmy_noether_sedenion.md) · [99 Emmy Noether](99_emmy_noether.md)
