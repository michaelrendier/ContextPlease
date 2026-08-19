# Sedenion arithmetic: CPU vs Intel UHD 620 — 2026-08-08

**Asked:** does "transform into sedenion maths, compute, return to reals" give a
computational discount versus GPU parallelization? Can hyperindexed code
approach RAM access speeds?

**Hardware:** i7-8550U (4C/8T, 15 W mobile), Intel UHD 620 (24 CUs, 1150 MHz,
fp64 capable), ~25 GB/s DRAM. `intel-opencl-icd` installed this session.

## Results — 2²⁰ sedenion products, fp32, 512 FLOP each

| implementation | time | GFLOP/s | vs 1 core |
|---|---|---|---|
| numpy, untiled | 326 ms | 1.65 | 0.54× |
| numpy, cache-tiled | 176 ms | 2.92 | 1.0× |
| C / AVX2, 1 thread | 177 ms | 3.03 | 1.04× |
| C / AVX2, 4 threads | 45 ms | 11.87 | 3.9× |
| C / AVX2, 8 threads | 33 ms | 16.19 | 5.3× |
| **iGPU UHD 620, zero-copy** | **18.5 ms** | **29.09** | **9.7×** |
| *RAM ceiling (memory-bound floor)* | *8.1 ms* | *66* | *21.7×* |

All GPU results verified `correct=True` against the CPU reference.

## Findings

**The discount is real and it is a cache-line fact.**

    16 × fp32 = 64 bytes = exactly ONE cache line
    16 × fp64 = 128 bytes = two lines → 1.61 vs 3.05 GFLOP/s measured

Cache tiling alone bought 1.85× with no algorithmic change. Arithmetic
intensity is only **2.7 FLOP/byte**, so the sedenion product is *memory-bound* —
RAM speed is the correct ceiling to measure against, which is why Cody's
"approaching RAM access speeds" framing is the right one.

**Answer on RAM speed: about halfway.** iGPU reaches 44% of the DRAM copy
ceiling, 8-thread CPU 24%. The iGPU shares system DRAM, so zero-copy works and
there is no PCIe tax — both processors face the same memory wall.

**⚠ This cuts against climbing the Cayley–Dickson tower.** T32/fp32 = 2 cache
lines, T64/fp32 = 4. The sedenion is the unique cache-line-aligned sweet spot
on x86-64; going up for resolution forfeits the alignment that produced the
discount.

**⚠ It does NOT touch RSA factoring.** Indexing is throughput-bound, so a 10×
layout win is a 10× win outright. Factoring is search-bound: GNFS on RSA-2048
is ~10²⁰ operations, and 10× leaves ~10¹⁹. The gap is ~30 orders of magnitude.
No hypercomplex reformulation is known to change the asymptotics. Where the
10× *does* pay: `chart_of` / `address_census` over the 164,283-word vocabulary.

## Files

- `sedbench.py` — **INVALID, kept as a record.** Recursive `cd_mul` allocated
  hundreds of temporaries per call; measured numpy's allocator, not the
  algebra (0.06 GB/s). The STREAM triad was also wrong — `s*c` made a
  temporary. Superseded by `sedbench2.py`.
- `sedbench2.py` — corrected. Flat 16×16 sign table (256 terms), cache tiling
  sweep, honest bandwidth ceiling via `np.copyto`.
- `sedbench_gpu.py` — OpenCL kernel generated from the sign table, zero-copy
  via `USE_HOST_PTR`, plus a threaded-CPU comparison.
- `sedmul.c` / `sedmul` — C/AVX2/OpenMP baseline. Exists because the 4-thread
  *Python* number (1.05×) was GIL-bound and would have flattered the GPU by ~5×.
- `det_check.py` — **the important one.** Verifies det(L_q) = N(q)² exactly
  (ratio 1.000000) and spec(L_q) = {±i, ±i} for every unit pure-imaginary q.

## The det result — why it matters beyond this benchmark

The UDEO v2/v3 landmark signature used each quaternion block's 4×4
regular-representation determinant. That determinant is a **function of the
norm alone** — every angular degree of freedom was discarded before any
comparison. `hot`/`love`/`up`/`true` collapsing to one bucket was not
pigeonholing; the statistic is *constant on spheres*.

T64 would not have helped: det = N^k at every level of the tower. This
supersedes the "insufficient resolution" diagnosis recorded in the
`project_zd_holes_are_portals` memory, now corrected.

Replacement statistics must be **angular**: the assessor/Fano-line address from
`chart_of`, or the spectrum of the off-diagonal coupling block of
M(a,b) = [[L_a, −R_b∘κ], [L_b∘κ, R_a]] — the only part not norm-determined.
