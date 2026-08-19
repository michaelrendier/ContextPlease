#!/usr/bin/env python3
"""
v2 — corrected. v1 measured numpy's allocator, not the algebra.

Sedenion product as a flat 16x16 sign table: 256 (i,j,sign) terms.
z[k] = sum_{(i,j,s) -> k} s * x[i] * y[j]      512 FLOP per product.

Tests Cody's actual claim: does 16-wide hypercomplex blocking give a
memory-access discount, and can it approach RAM bandwidth?
"""
import time, numpy as np

def bench(fn, reps=5, warmup=1):
    for _ in range(warmup): fn()
    return min((lambda t=time.perf_counter(): (fn(), time.perf_counter()-t)[1])() for _ in range(reps))

# -------------------------------------------------- build the sedenion table
def cd_mul_slow(x, y):
    n = len(x)
    if n == 1: return np.array([x[0]*y[0]])
    h = n//2
    a,b,c,d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([cd_mul_slow(a,c) - cd_mul_slow(cd_conj(d), b),
                           cd_mul_slow(d,a) + cd_mul_slow(b, cd_conj(c))])
def cd_conj(x):
    n = len(x)
    if n == 1: return x.copy()
    h = n//2
    return np.concatenate([cd_conj(x[:h]), -x[h:]])

DIM = 16
TABLE = []                       # (i, j, k, sign)
for i in range(DIM):
    for j in range(DIM):
        ei = np.zeros(DIM); ei[i] = 1.0
        ej = np.zeros(DIM); ej[j] = 1.0
        p = cd_mul_slow(ei, ej)
        k = int(np.nonzero(p)[0][0])
        TABLE.append((i, j, k, float(p[k])))
assert len(TABLE) == 256
BY_K = [[(i,j,s) for (i,j,kk,s) in TABLE if kk == k] for k in range(DIM)]

# -------------------------------------------------- kernels  (layout: (16,N))
def sed_mul_stream(x, y, z):
    """No tiling — streams all 16 columns from RAM for every output."""
    for k in range(DIM):
        terms = BY_K[k]
        i,j,s = terms[0]
        np.multiply(x[i], y[j], out=z[k])
        if s < 0: np.negative(z[k], out=z[k])
        for (i,j,s) in terms[1:]:
            if s > 0: z[k] += x[i]*y[j]
            else:     z[k] -= x[i]*y[j]

def sed_mul_tiled(x, y, z, tile):
    """Tiled so all 16 columns of a chunk sit in cache across all 256 terms."""
    N = x.shape[1]
    for lo in range(0, N, tile):
        hi = min(lo+tile, N)
        xv, yv, zv = x[:,lo:hi], y[:,lo:hi], z[:,lo:hi]
        for k in range(DIM):
            terms = BY_K[k]
            i,j,s = terms[0]
            np.multiply(xv[i], yv[j], out=zv[k])
            if s < 0: np.negative(zv[k], out=zv[k])
            for (i,j,s) in terms[1:]:
                if s > 0: zv[k] += xv[i]*yv[j]
                else:     zv[k] -= xv[i]*yv[j]

# -------------------------------------------------- main
if __name__ == "__main__":
    n = 1 << 25
    a = np.ones(n); b = np.ones(n)
    t = bench(lambda: np.copyto(a, b), reps=3)
    BW = 2*n*8/t/1e9
    print(f"[0] memory bandwidth ceiling (copy, 256 MB) : {BW:6.2f} GB/s\n")

    N = 1 << 20
    rng = np.random.default_rng(0)
    for dt, name in ((np.float32,"fp32"), (np.float64,"fp64")):
        isz = np.dtype(dt).itemsize
        x = np.ascontiguousarray(rng.normal(size=(16,N)).astype(dt))
        y = np.ascontiguousarray(rng.normal(size=(16,N)).astype(dt))
        z = np.zeros((16,N), dtype=dt)
        flops = 512*N
        compulsory = 3*16*N*isz          # x + y + z, touched once
        print(f"--- {name}: one sedenion = {16*isz} B = {16*isz/64:.2f} cache line(s) ---")

        t1 = bench(lambda: sed_mul_stream(x,y,z), reps=3)
        print(f"[1] untiled (streams RAM)  : {t1*1e3:7.1f} ms  {flops/t1/1e9:6.2f} GFLOP/s  "
              f"{compulsory/t1/1e9:5.2f} GB/s eff  {t1/N*1e9:6.1f} ns/sed")
        ref = z.copy()

        best = None
        for tile in (2048, 8192, 32768, 131072):
            tt = bench(lambda: sed_mul_tiled(x,y,z,tile), reps=3)
            mark = ""
            if best is None or tt < best[1]: best = (tile, tt); mark = ""
            print(f"    tiled {tile:>7}       : {tt*1e3:7.1f} ms  {flops/tt/1e9:6.2f} GFLOP/s  "
                  f"speedup {t1/tt:4.2f}x")
        assert np.allclose(z, ref, rtol=1e-4, atol=1e-4), "tiled result mismatch!"
        tile, t2 = best
        print(f"[2] BEST tile={tile}: {t2*1e3:7.1f} ms  {flops/t2/1e9:6.2f} GFLOP/s  "
              f"{t2/N*1e9:6.1f} ns/sed  -> {t1/t2:4.2f}x over untiled")
        print(f"    arithmetic intensity = {flops/compulsory:6.1f} FLOP/byte "
              f"(compute-bound if > {'%.1f'%(1.0)} ; RAM ceiling implies "
              f"{BW*flops/compulsory:.1f} GFLOP/s available)\n")
