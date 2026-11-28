# 146 — The zeta pathway in Universal Native Space

| | |
|---|---|
| Written | 2026-11-24 |
| Scope | the critical-line path as a rotation with a signed radial driver; the spring along t; where the primes are on it; how it compares with the Aizawa skeleton |
| Requested by | Cody, 2026-11-24: "it's not flattening artifact...it's a top down view from a pole. it's missing the spring model. ... build me something for the Universal Native Space Riemann Zeta pathway and ensure that there is enough detail to see where the primes are ... let the Riemann Zeta function describe its own path to compare to the aizawa attractor." |
| Code | `ValaQuenta/modules/zeta_uns_path/` · tests `Testing/test_zeta_uns_path.py` (20) · notebook `29_zeta_uns_path.ipynb` · wiki `wiki/zeta_uns_path.md`, toolbox 46 · viewer `RiemannHypothesisProof/visualizations/javascript/webgl_aizawa_vs_zeta_uns.html` |
| Confidence | ESTABLISHED (Hardy, Riemann-Siegel); CALCULATED for the driver, the prime resonance and the zero spectrum; the Aizawa comparison is structural only |

> **Note from the assistant.** Written by a transformer (Claude Sonnet 5.5, `claude-sonnet-5-5`) working with Cody Allison in Claude Code. Cody does not tell the model what result he wants; the checks were written before the runs, and where one failed the failure is recorded here.

## 1. What Cody asked

That the zeta function draw its own path, in Universal Native Space, next to the Aizawa attractor, with enough detail to see the primes, and that it be a top-down view from a pole with a spring model, not a flattening artefact.

## 2. What the path is

zeta(1/2 + it) = exp(-i theta(t)) Z(t). The angle turns at -theta'(t), about -(1/2) ln(t/2 pi). The radius Z is real and signed: at each zero the path goes through the axis and out the other side. In UNS cylinder coordinates (rho = log10|zeta| + 3, phi = arg zeta, height = t) this is a spring along t with the zeros on its axis. Aizawa turns at a constant rate with a radius that can never reach the axis; the zeros are exactly the axis passages it forbids.

## 3. The driver and the primes

Z'/Z (the analogue of Aizawa's z - b) is the sum over the zeros of the pole kernels 2t/(t^2 - gamma^2) plus a smooth part: away from the zeros the spread drops from 0.573 to 0.007 when the zero sum is subtracted (25,000 zeros). The primes enter in two places that can be seen: the prime spring (one step per prime, turned by -t ln p) and the zero spectrum, whose spikes sit at x = ln p^k, 28 to 750 times above background for every prime to 47.

## 4. A failure worth keeping

The first browser render showed 32 rigid spokes from the pole. Sampling by equal steps of theta puts every point on 32 fixed angles of the flat point; the spokes were the sampling, not the curve. A golden-ratio jitter on the phase grid removed it, and a test now guards it. Headless Firefox also does not capture WebGL canvases in screenshots; the viewer has a `?snap=1` option for that.

## 5. Not here

The Euler product does not converge on the critical line, so the prime spring is a picture of partial sums. The Aizawa comparison is structural and says nothing about the Riemann Hypothesis. Still open: the phase-offset reading of the diagonal prime-generating quadratics, and whether an orthogonal wave (a Dirichlet character) sits beside zeta.
