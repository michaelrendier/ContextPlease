#!/usr/bin/env python3
"""
Sedenion-blocked arithmetic vs parallelization, on the i7-8550U.

The question under test is NOT "does sedenion algebra beat GNFS at factoring"
(it does not; no mechanism). It is Cody's actual empirical claim: that a
16-wide hypercomplex block layout gives a memory-access discount, and whether
that discount can approach RAM bandwidth.

Measured:
  0. STREAM-triad memory bandwidth ceiling  (the number to "approach")
  1. sedenion CD multiply, numpy 16-wide structured  (fp64 and fp32)
  2. identical FLOPs, RANDOM-GATHER layout           (unstructured hyperindex)
  3. torch multithreaded                             (parallel proxy)
"""
import time, numpy as np, os

def bench(fn, *a, reps=5, warmup=1):
    for _ in range(warmup): fn(*a)
    ts = []
    for _ in range(reps):
        t = time.perf_counter(); fn(*a); ts.append(time.perf_counter() - t)
    return min(ts)

# ---------------------------------------------------------------- CD multiply
def cd_mul(x, y):
    """Vectorized Cayley-Dickson product. x,y shape (N, 2^k). Recursive."""
    n = x.shape[1]
    if n == 1:
        return x * y
    h = n // 2
    a, b = x[:, :h], x[:, h:]
    c, d = y[:, :h], y[:, h:]
    return np.concatenate([cd_mul(a, c) - cd_mul(cd_conj(d), b),
                           cd_mul(d, a) + cd_mul(b, cd_conj(c))], axis=1)

def cd_conj(x):
    n = x.shape[1]
    if n == 1: return x
    h = n // 2
    out = np.empty_like(x)
    out[:, :h] = cd_conj(x[:, :h]); out[:, h:] = -x[:, h:]
    return out

# ---------------------------------------------------------------- 0. ceiling
def stream_triad(n_mb=256):
    n = (n_mb * 1024 * 1024) // 8
    a = np.ones(n); b = np.ones(n); c = np.ones(n); s = 3.0
    t = bench(lambda: np.add(b, s * c, out=a), reps=3)
    return (3 * n * 8) / t / 1e9, t     # GB/s (2 read + 1 write)

# ---------------------------------------------------------------- main
if __name__ == "__main__":
    print(f"threads: numpy sees OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS','unset')}\n")

    bw, _ = stream_triad()
    print(f"[0] STREAM-triad memory bandwidth ceiling : {bw:6.2f} GB/s\n")

    N = 1 << 20   # 1,048,576 sedenions
    rng = np.random.default_rng(0)

    for dt, name in ((np.float64, "fp64"), (np.float32, "fp32")):
        x = rng.normal(size=(N, 16)).astype(dt)
        y = rng.normal(size=(N, 16)).astype(dt)
        itemsize = np.dtype(dt).itemsize
        print(f"--- {name}: one sedenion = {16*itemsize} bytes "
              f"({16*itemsize/64:.2f} cache lines) ---")

        # 1. structured 16-wide
        t = bench(lambda: cd_mul(x, y), reps=3)
        bytes_moved = 3 * N * 16 * itemsize
        print(f"[1] CD mul, structured 16-wide : {t*1e3:8.2f} ms  "
              f"{bytes_moved/t/1e9:6.2f} GB/s  ({100*bytes_moved/t/1e9/bw:5.1f}% of ceiling)  "
              f"{t/N*1e9:6.1f} ns/sedenion")

        # 2. same FLOPs, random gather (unstructured index)
        perm = rng.permutation(N)
        xs, ys = x[perm], y[perm]
        def scattered():
            return cd_mul(x[perm], y[perm])
        t2 = bench(scattered, reps=3)
        print(f"[2] CD mul, random-gather      : {t2*1e3:8.2f} ms  "
              f"{bytes_moved/t2/1e9:6.2f} GB/s  ({100*bytes_moved/t2/1e9/bw:5.1f}% of ceiling)  "
              f"{t2/t:5.2f}x slower than structured")
        print()

    # 3. torch multithreaded
    try:
        import torch
        torch.set_num_threads(4)
        xt = torch.from_numpy(rng.normal(size=(N,16)).astype(np.float32))
        yt = torch.from_numpy(rng.normal(size=(N,16)).astype(np.float32))
        def tmul(x, y):
            n = x.shape[1]
            if n == 1: return x * y
            h = n//2
            a,b = x[:,:h], x[:,h:]; c,d = y[:,:h], y[:,h:]
            return torch.cat([tmul(a,c) - tmul(tconj(d),b),
                              tmul(d,a) + tmul(b,tconj(c))], dim=1)
        def tconj(x):
            n = x.shape[1]
            if n == 1: return x
            h = n//2
            return torch.cat([tconj(x[:,:h]), -x[:,h:]], dim=1)
        t3 = bench(lambda: tmul(xt, yt), reps=3)
        bm = 3*N*16*4
        print(f"[3] CD mul, torch 4-thread fp32: {t3*1e3:8.2f} ms  "
              f"{bm/t3/1e9:6.2f} GB/s  ({100*bm/t3/1e9/bw:5.1f}% of ceiling)")
    except Exception as e:
        print("[3] torch failed:", e)
