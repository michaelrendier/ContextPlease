#!/usr/bin/env python3
"""Sedenion product: CPU-1thread vs CPU-4thread vs Intel UHD 620 (OpenCL).

iGPU shares system DRAM -> zero-copy is possible, no PCIe tax.
Both processors face the SAME ~25 GB/s memory ceiling.
"""
import time, numpy as np, os
import pyopencl as cl
from concurrent.futures import ThreadPoolExecutor
from sedbench2 import BY_K, DIM, sed_mul_tiled, bench

N = 1 << 20
FLOPS = 512 * N
rng = np.random.default_rng(0)
x = np.ascontiguousarray(rng.normal(size=(16, N)).astype(np.float32))
y = np.ascontiguousarray(rng.normal(size=(16, N)).astype(np.float32))
z = np.zeros((16, N), dtype=np.float32)

# ---------------------------------------------------------------- reference
sed_mul_tiled(x, y, z, 32768)
REF = z.copy()
t_1t = bench(lambda: sed_mul_tiled(x, y, z, 32768), reps=3)
print(f"[CPU 1 thread, tiled ] {t_1t*1e3:7.1f} ms   {FLOPS/t_1t/1e9:6.2f} GFLOP/s")

# ---------------------------------------------------------------- 4 threads
def threaded(nthreads=4):
    chunk = (N + nthreads - 1)//nthreads
    def work(t):
        lo, hi = t*chunk, min((t+1)*chunk, N)
        sed_mul_tiled(x[:,lo:hi], y[:,lo:hi], z[:,lo:hi], 32768)
    with ThreadPoolExecutor(nthreads) as ex:
        list(ex.map(work, range(nthreads)))
t_4t = bench(lambda: threaded(4), reps=3)
assert np.allclose(z, REF, rtol=1e-4, atol=1e-4)
print(f"[CPU 4 threads       ] {t_4t*1e3:7.1f} ms   {FLOPS/t_4t/1e9:6.2f} GFLOP/s   "
      f"{t_1t/t_4t:4.2f}x over 1 thread")

# ---------------------------------------------------------------- OpenCL
lines = []
for k in range(DIM):
    terms = " ".join(f"{'+' if s>0 else '-'} x{i}*y{j}" for (i,j,s) in BY_K[k])
    lines.append(f"    z[{k}*N + g] = {terms.lstrip('+ ')};")
loads = "\n".join(f"    const float x{i} = x[{i}*N + g];" for i in range(16))
loads += "\n" + "\n".join(f"    const float y{i} = y[{i}*N + g];" for i in range(16))
SRC = f"""
__kernel void sedmul(__global const float *x, __global const float *y,
                     __global float *z, const int N) {{
    int g = get_global_id(0);
    if (g >= N) return;
{loads}
{chr(10).join(lines)}
}}
"""
ctx = cl.create_some_context(interactive=False)
q = cl.CommandQueue(ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)
prg = cl.Program(ctx, SRC).build()
mf = cl.mem_flags

# zero-copy: iGPU maps host memory directly, no transfer
xb = cl.Buffer(ctx, mf.READ_ONLY  | mf.USE_HOST_PTR, hostbuf=x)
yb = cl.Buffer(ctx, mf.READ_ONLY  | mf.USE_HOST_PTR, hostbuf=y)
zg = np.zeros((16, N), dtype=np.float32)
zb = cl.Buffer(ctx, mf.WRITE_ONLY | mf.USE_HOST_PTR, hostbuf=zg)

def gpu_run():
    e = prg.sedmul(q, (N,), None, xb, yb, zb, np.int32(N))
    e.wait(); return e
e = gpu_run()
t_k = (e.profile.end - e.profile.start)/1e9
t_gpu = bench(lambda: gpu_run(), reps=5)
cl.enqueue_copy(q, zg, zb); q.finish()
ok = np.allclose(zg, REF, rtol=1e-3, atol=1e-3)
print(f"[iGPU UHD620 zerocopy] {t_gpu*1e3:7.1f} ms   {FLOPS/t_gpu/1e9:6.2f} GFLOP/s   "
      f"{t_1t/t_gpu:4.2f}x over 1 thread, {t_4t/t_gpu:4.2f}x over 4   correct={ok}")
print(f"    kernel-only (no enqueue overhead): {t_k*1e3:6.1f} ms  {FLOPS/t_k/1e9:6.2f} GFLOP/s")

compulsory = 3*16*N*4
print(f"\n    compulsory traffic {compulsory/1e6:.0f} MB ; at 24.9 GB/s ceiling the "
      f"memory-bound floor is {compulsory/24.9e9*1e3:.1f} ms  "
      f"({FLOPS/(compulsory/24.9e9)/1e9:.0f} GFLOP/s)")
