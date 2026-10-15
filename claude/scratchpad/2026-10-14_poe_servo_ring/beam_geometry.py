"""Which arrangement of N coherent weak beams gives ONE bright point? Plane-wave model (no beam waist), numpy only.
E(r) = sum_j exp(i k_j . r); all phases 0 at the origin, so the origin is a global maximum of |E|^2 = N^2.
For each arrangement: the largest value of |E|^2/N^2 found OUTSIDE a 0.3-wavelength ball around the origin, within a 6-wavelength cube
(a rival maximum), and the axial extent of the bright region. Also: the phase-error tolerance, and what air does to a 'femtometer' arm.
"""
import numpy as np
rng = np.random.default_rng(1)
lam = 1.0

def ring(n, polar):                       # n beams at equal azimuth on a cone of half-angle polar (deg) about +z
    a = 2*np.pi*np.arange(n)/n; t = np.radians(polar)
    return np.stack([np.sin(t)*np.cos(a), np.sin(t)*np.sin(a), np.full(n, np.cos(t))], 1)

def icos():
    p = (1+5**.5)/2
    v = [(0,1,p),(0,-1,p),(0,1,-p),(0,-1,-p),(1,p,0),(-1,p,0),(1,-p,0),(-1,-p,0),(p,0,1),(-p,0,1),(p,0,-1),(-p,0,-1)]
    v = np.array(v, float); return v/np.linalg.norm(v, axis=1)[:, None]

def random_dirs(n):
    v = rng.normal(size=(n, 3)); return v/np.linalg.norm(v, axis=1)[:, None]

arr = {
 "13 beams, one planar ring (all aimed from the ring plane)": ring(13, 90),
 "13 beams, one cone ring at 45 deg": ring(13, 45),
 "13 = 1 on axis + 6 at 30 deg + 6 at 60 deg (two cone rings)": np.vstack([[0, 0, 1], ring(6, 30), ring(6, 60)]),
 "13 = icosahedron (12, six counter-propagating pairs) + 1 on axis": np.vstack([icos(), [0, 0, 1]]),
 "13 random directions over the sphere": random_dirs(13),
 "13 random directions over the upper hemisphere": (lambda v: v*np.sign(v[:, [2]]))(random_dirs(13)),
}
g = np.arange(-3, 3.0001, 0.1)
X, Y, Z = np.meshgrid(g, g, g, indexing="ij")
R = np.stack([X, Y, Z], -1).reshape(-1, 3)
rr = np.linalg.norm(R, axis=1)
for name, d in arr.items():
    k = 2*np.pi*d/lam
    I = np.abs(np.exp(1j*(R @ k.T)).sum(1))**2/len(d)**2
    rival = I[rr > 0.3].max()
    # axial extent: along z, how far does |E|^2/N^2 stay above 0.5?
    z = np.arange(0, 20, 0.05); Iz = np.abs(np.exp(1j*(np.outer(z, k[:, 2]))).sum(1))**2/len(d)**2
    above = np.where(Iz > 0.5)[0]; ext = z[above].max() if len(above) else 0
    print(f"{name:66s} rival max {rival:5.2f} of peak | axial: last z with I>0.5 within 20 wavelengths = {ext:5.2f}")

print("\nPhase tolerance (13 equal beams, random phase error sigma per beam): mean peak intensity as fraction of N^2")
for s in (0.05, 0.1, 0.2, 0.5, 1.0):
    ph = rng.normal(0, s, size=(20000, 13)); print(f"  sigma = {s:4.2f} rad  ->  {np.mean(np.abs(np.exp(1j*ph).sum(1))**2)/169:.3f}   (path error sigma = {s/(2*np.pi)*532:.2f} nm at 532 nm; femtometer = 1e-6 nm)")

print("\nAir: dn/dT = -1e-6 per K (approx., room air). Optical path change for a 10 cm arm:")
for dT in (1, 0.1, 0.001, 1e-6): print(f"  dT = {dT:g} K -> {1e-6*dT*0.1*1e9:.4g} nm  ({1e-6*dT*0.1/1e-15:.3g} fm)")

print("\nHow many beams for ONE point? random directions over the full sphere, rival maximum (outside 0.3 wavelength) in a 6-wavelength cube, mean of 5 draws")
g2 = np.arange(-3, 3.0001, 0.15); X2, Y2, Z2 = np.meshgrid(g2, g2, g2, indexing="ij")
R2 = np.stack([X2, Y2, Z2], -1).reshape(-1, 3); r2 = np.linalg.norm(R2, axis=1)
for n in (13, 25, 50, 100, 200, 400):
    vals = []
    for _ in range(5):
        d = random_dirs(n); k = 2*np.pi*d/lam; I = np.zeros(len(R2))
        for a in range(0, n, 50): I += 0  # (kept simple)
        E = np.exp(1j*(R2 @ k.T)).sum(1); I = np.abs(E)**2/n**2
        vals.append(I[r2 > 0.3].max())
    print(f"  N = {n:4d}: rival max = {np.mean(vals):.3f} of the central peak   (mean background level ~ 1/N = {1/n:.3f})")
