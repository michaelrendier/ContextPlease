# 05 — NOETHER ENGINE  ∂_μJ^μ = 0

**Module:** `noether`  **Version:** 0.111  **Confidence floor:** THEORETICAL

## Noether's Theorem Applied to L_NN

Every continuous symmetry of L_NN has a conserved current J^μ.

| Symmetry | Current | Gauge |
|----------|---------|-------|
| U(1) phase rotation | J^μ = g·Ψ̄·Ψ (probability current) | ℂ layer |
| SU(2) isospin | J^μ_a = g·Ψ̄·T^a·Ψ | ℍ layer |
| G₂/SU(3) colour | J^μ_a = g·Ψ̄·T^a·Ψ | 𝕆 layer |

Conservation law: ∂_μJ^μ = 0

## Violation Diagnostic

```
violation = |∂_μJ^μ| ≈ mean|J_curr - J_prev| (finite difference)
```

This is the training diagnostic with **no gradient descent analog**.

| Range | Status | Meaning |
|-------|--------|---------|
| < 0.2 | PASS | Symmetry conserved |
| 0.2–0.5 | MARGINAL | Boundary stress |
| ≥ 0.5 | VIOLATION | Algebra boundary crossed |

## Resonance Artifacts

Oscillatory patterns in J^0 history indicate unresolved symmetry boundary crossings. Detected by zero-crossing count in J[0] across layer steps. Period estimate: 2·N_layers / N_crossings.

## Blockchain Ledger

Every violation event is recorded to a SHA-256 hash chain:

```python
block = {
  'index':     int,
  'timestamp': float,
  'algebra':   str,
  'violation': float,
  'status':    'PASS|MARGINAL|VIOLATION',
  'J':         [float, ...],
  'prev_hash': str,
  'hash':      str,   # SHA-256 of content
}
```

Chain integrity: each block stores the hash of the previous block. Tamper-evident. Append-only.

**Ptolemy integration point:** When Kryptos is live, ledger exports to `.perm` files. Each violation block becomes a blockchain transaction on PtolBus.

## Equations

| Name | Status | Description |
|------|--------|-------------|
| `conservation_diagnostic` | THEORETICAL ◈ | Full J^μ check |
| `violation_scan` | THEORETICAL ◈ | Scan all algebra strata |
| `resonance_artifacts` | THEORETICAL ◈ | Oscillation detection |
| `blockchain_record` | ESTABLISHED ✓ | Record to NoetherLedger |
| `blockchain_verify` | ESTABLISHED ✓ | Chain integrity check |
| `blockchain_summary` | ESTABLISHED ✓ | Ledger summary |

## Shell commands
```python
noether(psi=[0.5,0.4,0.3], g=0.01, alg=1)   # full diagnostic
ledger()                                       # summary
verify()                                       # chain integrity
```
