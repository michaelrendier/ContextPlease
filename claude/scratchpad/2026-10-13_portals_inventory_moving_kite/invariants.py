#!/usr/bin/env python3
"""MOVING KITE — which readings survive a continuous G2 deformation (the kite moving), and which only survive the finite group?
Each reading is evaluated at v and at g v, g = exp(t D), D a random derivation, t = 0.7; the max change is reported."""
import subprocess, math
import numpy as np
from scipy.linalg import expm
from common import *
Ds = derivations(); rng = np.random.default_rng(8)
E = np.eye(16)
PTOL = '/home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptol'
def ptolv(p):
    out = subprocess.run([PTOL, '-r', p], capture_output=True, text=True).stdout.split('\n'); v = []; i = 0
    while out[i].strip() != '---': v.append(float(out[i])); i += 1
    return np.array(v[:16])
H16 = np.array([[(-1) ** bin(i & j).count('1') for j in range(16)] for i in range(16)], float)
def assoc_norm(v):          # K(v) = sum_{ij} |[v, e_i, e_j]|^2  (basis independent)
    tot = 0.0
    for i in range(16):
        for j in range(16):
            tot += np.linalg.norm(m(m(v, E[i]), E[j]) - m(v, m(E[i], E[j]))) ** 2
    return tot
def sigma_rb(x):
    psi = np.array([x[k] + 1j * x[(k + 8) % 16] for k in range(16)]); s = np.array([psi[k] * np.conj(psi[k ^ 4]) for k in range(16)])
    return s.real.sum(), s.imag.sum(), sorted(np.round(np.abs(s), 9))[:2]
def readings(v):
    ce = bk.chart_projection(list(v)); tot = sum(ce.values())
    r = bk.chart_of(list(v), check_zd=False); W = H16 @ (v * v) / (v @ v)
    return {
     'norm': np.linalg.norm(v),
     'e0 weight (fixed_point_weight)': v[0] ** 2 / (v @ v),
     'e8 weight': v[8] ** 2 / (v @ v),
     'outside_share (e0+e8)': r['outside_share'],
     'lower / upper energy split': r['energy_split']['lower'],
     'chart_energy[1] (7 chart energies)': ce[1] / tot,
     'chart_energy[4]': ce[4] / tot,
     'local_curvature (top-3 basis triples)': r['local_curvature'],
     'Walsh W_4 (= ptol Gamma)': W[4], 'Walsh W_9': W[9],
     'sigma_RB  sum tilt': sigma_rb(v)[0],
     'sigma_RB  sum axis': sigma_rb(v)[1],
     'sing. values of L_v, smallest': np.linalg.svd(Lmat(v), compute_uv=False)[-1],
     'sing. values of L_v, largest': np.linalg.svd(Lmat(v), compute_uv=False)[0],
     'sing. values of R_v, smallest': np.linalg.svd(Rmat(v), compute_uv=False)[-1],
     'associator norm K(v)': assoc_norm(v),
    }
samples = {'random unit vector': rng.normal(size=16)}
for p in ("neutron generation", "the cat sat on the mat"): samples['ptol: ' + p] = ptolv(p)
for k in samples: samples[k] = samples[k] / np.linalg.norm(samples[k])
change = {}
for name, v in samples.items():
    D = sum(c * Di for c, Di in zip(rng.normal(size=14), Ds)); D = D / np.linalg.norm(D) * 2.0; g = expm(0.7 * D)
    a, b = readings(v), readings(g @ v)
    for k in a: change.setdefault(k, []).append(abs(a[k] - b[k]))
print("MAX CHANGE of each reading when the address is moved by a continuous G2 deformation g = exp(0.7 D)   (3 vectors: random + 2 prompts)")
print("   %-44s %-12s %s" % ("reading", "max change", "invariant under the moving kite?"))
for k, v in change.items(): print("   %-44s %-12.3e %s" % (k, max(v), "YES" if max(v) < 1e-9 else "no"))
print("\nSAME readings under the FINITE group (168 frame-preserving index maps; sign-blind readings):  all chart/lattice readings permute covariantly (part 3 SC-02); the moving-kite invariants above need no relabelling at all.")
print("\nsigma_RB frame: tilt = Re sum_k psi[k] conj psi[k^4], psi[k] = x[k] + i x[k^8]; the pairing k <-> k^4 is the red/blue pairing (Hadamard character chi_4), the pairing k <-> k^8 is the Cayley-Dickson doubling pair.")
for name, v in list(samples.items())[1:]:
    tl, ax, sm = sigma_rb(v); print("   %-34s sum tilt %+.6f  sum axis %+.2e  (axis sum is identically 0)" % (name, tl, ax))
