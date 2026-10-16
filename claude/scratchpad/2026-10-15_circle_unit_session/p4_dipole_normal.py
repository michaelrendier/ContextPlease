"""P4 — how Dipole Energy U = -MB cos(theta) becomes a Normal-distribution bell: the thermal (Boltzmann) route, with simulation.
Chain:  U(theta) = -MB cos(theta)  --Boltzmann e^{-U/kT}-->  von Mises exp(kappa cos(theta))  --large kappa-->  Gaussian, sigma^2 = 1/kappa = kT/MB
        N dipoles: total energy --CLT--> Gaussian.   Both are maximum-entropy: random settles into order."""
import numpy as np, math
from scipy.special import i0, i1
from scipy.stats import skew, kurtosis, entropy
rng = np.random.default_rng(5)
def metropolis(kappa, n=200000, burn=20000, step=None):
    step = step or min(1.5, 2.4/math.sqrt(max(kappa, 1)))
    th = rng.uniform(-math.pi, math.pi); out = np.empty(n); acc = 0
    for i in range(n+burn):
        p = th + rng.normal(0, step); d = kappa*(math.cos(p) - math.cos(th))
        if d >= 0 or rng.random() < math.exp(d): th = p
        if i >= burn: out[i-burn] = th
    return (out + math.pi) % (2*math.pi) - math.pi
print("(1) one dipole at inverse temperature kappa = MB/kT: sampled theta vs von Mises vs Gaussian")
print(f"{'kappa':>6} {'sd(theta)':>10} {'1/sqrt(kappa)':>14} {'<cos>':>8} {'I1/I0':>8} {'KL(vM||sample hist)':>20} {'skew':>7} {'ex.kurt':>8}")
for kappa in (0.5, 2, 10, 50, 200):
    th = metropolis(kappa, n=120000)
    bins = np.linspace(-math.pi, math.pi, 121); h, _ = np.histogram(th, bins, density=True); c = 0.5*(bins[1:]+bins[:-1])
    vm = np.exp(kappa*np.cos(c))/(2*math.pi*i0(kappa)); m = h > 0
    kl = float(np.sum(vm[m]*np.log(vm[m]/h[m]))*(bins[1]-bins[0]))
    print(f"{kappa:6} {th.std():10.4f} {1/math.sqrt(kappa):14.4f} {np.cos(th).mean():8.4f} {i1(kappa)/i0(kappa):8.4f} {kl:20.5f} {skew(th):7.3f} {kurtosis(th):8.3f}")
print("   -> <cos> = I1/I0 (2D von Mises); sd -> 1/sqrt(kappa) for large kappa; excess kurtosis -> 0 (Gaussian) as kappa grows")
print("\n(2) the ENERGY itself: U/MB = -cos(theta).  Its distribution at kappa: mean and variance")
for kappa in (0.0, 2, 10, 50):
    th = metropolis(kappa, n=100000) if kappa else rng.uniform(-math.pi, math.pi, 100000)
    U = -np.cos(th); r = i1(kappa)/i0(kappa)
    var_theory = 0.5 if kappa == 0 else 1 - r/kappa - r*r        # E[cos^2] = 1 - I1/(kappa I0)  (since I2 = I0 - 2 I1/kappa)
    print(f"   kappa={kappa:4}: mean U = {U.mean():+.4f} (theory {-r:+.4f})  var U = {U.var():.4f}  (theory {var_theory:.4f})   sd U/MB = {U.std():.4f}")
print("   uniform (kappa=0): sd(U)/MB = 1/sqrt(2) = %.4f in 2D" % (1/math.sqrt(2)))
print("   fluctuation-dissipation check: Var(U) = kT^2 C  -> C/k = kappa^2 Var(cos)")
print("\n(3) N independent dipoles: total energy is a SUM -> central limit theorem")
for N in (1, 4, 30, 400):
    kappa = 2.0
    th = np.array([metropolis(kappa, n=3000, burn=2000)[::1] for _ in range(1)])[0] if False else None
    # use exact sampling from von Mises for speed
    samp = rng.vonmises(0.0, kappa, size=(20000, N)); E = -np.cos(samp).sum(axis=1)
    print(f"   N={N:4}: skew {skew(E):+.3f}  excess kurtosis {kurtosis(E):+.3f}  (Gaussian: 0, 0)")
print("\n(4) maximum entropy: von Mises has the largest entropy among circle densities with the same <cos>")
th = np.linspace(-math.pi, math.pi, 200001)[:-1]; dth = th[1]-th[0]
kappa = 3.0; vm = np.exp(kappa*np.cos(th))/(2*math.pi*i0(kappa)); target = float(np.sum(np.cos(th)*vm)*dth)
H = lambda p: -float(np.sum(p[p > 0]*np.log(p[p > 0]))*dth)
best = None
for s in np.linspace(0.3, 2.0, 400):                          # wrapped normal tuned to the same <cos>=exp(-s^2/2)
    if abs(math.exp(-s*s/2) - target) < 2e-4: best = s; break
wn = sum(np.exp(-(th + 2*math.pi*k)**2/(2*best**2)) for k in range(-4, 5))/(best*math.sqrt(2*math.pi))
tri = np.maximum(0, 1 - np.abs(th)/2.2)*0 + np.exp(-np.abs(th)*1.3); tri /= tri.sum()*dth                # Laplace-like on the circle
print(f"   same <cos> = {target:.4f}: H(von Mises) = {H(vm):.5f}, H(wrapped normal) = {H(wn):.5f}  -> vM larger by {H(vm)-H(wn):.5f}  (they differ slightly: both near-Gaussian)")
print("   Gaussian on the line: max entropy for given variance (Shannon 1948); on the circle: von Mises for given <cos> (Jaynes 1957)")
