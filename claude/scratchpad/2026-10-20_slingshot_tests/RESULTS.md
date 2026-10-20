# Slingshot vs GR: numerical tests (2026-10-20)

## T1  Shapiro/geometric delay scale 4GM(1+z_l)/c³
| lens | M (Msun) | 4GM/c³ |
|---|---|---|
| stellar BH | 10 | 0.000197 s |
| intermediate | 1e+04 | 0.197 s |
| Sgr A* | 4.3e+06 | 84.7 s |
| M87* | 6.5e+09 | 1.48 d |
| TON 618 | 6.6e+10 | 15.1 d |
| cluster core (Refsdal-like) | 1e+14 | 62.4 yr |
| cluster | 1e+15 | 624 yr |
Image-pair delays for a point mass are this × [½ y√(y²+4) + ln((√(y²+4)+y)/(√(y²+4)−y))], y = source offset / θ_E.
Only masses ≳1e9 Msun give delays of days or more; stellar-mass lenses give ≲1e-3 s and unresolved images.

## T2  Static Schwarzschild lens: net frequency change over a full pass (null geodesic, RK4)
b=    10 M: deflection 5.9040e-01 rad (weak-field 4M/b = 4.0000e-01, +15πM²/4b² = 5.1781e-01); blueshift at r_min 1.13781; E-conservation drift 1.1e-14; exit/enter end-point factors 1.000000000
b=   100 M: deflection 4.1223e-02 rad (weak-field 4M/b = 4.0000e-02, +15πM²/4b² = 4.1178e-02); blueshift at r_min 1.01026; E-conservation drift 1.8e-14; exit/enter end-point factors 1.000000000
b=  1000 M: deflection 4.0118e-03 rad (weak-field 4M/b = 4.0000e-03, +15πM²/4b² = 4.0118e-03); blueshift at r_min 1.00100; E-conservation drift 1.7e-14; exit/enter end-point factors 1.000000000
Falling in gives ν×(1−2M/r)^-½, climbing out gives the inverse: product 1 for ANY static lens. A gain needs ∂g/∂t ≠ 0.

## T3  S-A formula f_exit/f_enter = (1 + 2GM/rc²)^α at r = n r_s  (2GM/rc² = r_s/r = 1/n)
| n = r/r_s | α=0.5 Δm | α=1 Δm | α=2 Δm | α for Δm=−0.2 | GR infall blueshift (1−1/n)^-½ − 1 |
|---|---|---|---|---|---|
| 3 | -0.1562 | -0.3123 | -0.6247 | 0.64 | 0.2247 |
| 10 | -0.0517 | -0.1035 | -0.2070 | 1.93 | 0.05409 |
| 100 | -0.0054 | -0.0108 | -0.0216 | 18.51 | 0.005038 |
| 1000 | -0.0005 | -0.0011 | -0.0022 | 184.30 | 0.0005004 |
| 10000 | -0.0001 | -0.0001 | -0.0002 | 1842.16 | 5e-05 |
S-A's 'Δm ≈ −0.2 at r = 10 r_s' therefore needs α ≈ 1.94, outside its own stated range 0–1 (max Δm there: −0.103).
α is not derived anywhere: it is the free parameter.

## T4  S2 at Sgr A* (pericentre 2018): bound on α from the measured redshift
r_s/r_p = 7.074e-04;  GR gravitational 3.537e-04 + transverse Doppler 3.256e-04 = 6.793e-04  (204 km/s)
With f = 0.9 ± 0.175: α = 0.10 ± 0.17  →  |α| ≲ 0.43 at ~2σ.  (S-A needs α up to 1 for 'maximum assist'.)
Caveat: S-A is a formula for an in-and-out pass; S2's photons are emitted at the star and escape. Applying it here is my reading.

## T5  Size of a ∂g/∂t effect (S-B's v·∂g/∂t) for a cluster lens like MACS J1149
Φ/c² ≈ (σ/c)² = 2.50e-05;  light crossing 2R/c = 6.52e+06 yr;  dynamical time R/σ = 6.52e+08 yr
net fractional frequency change over one crossing ≈ Φ/c² · t_cross/t_dyn = 2.5e-07  (Rees–Sciama-type);  Δm ≈ 2.7e-07 mag
Refsdal data precision: SX colour F125W−F160W = 0.2 ± 0.3 mag (Kelly+ 2016), same as S1–S4 within errors.
Required for S-A's Hubble-tension story: ~8 % accumulated; per-cluster 3e-07 would need ~3e+05 such crossings.

## T6  Refsdal delay vs the standard calculation
Delay = geometric path difference + Shapiro delay (Fermat potential τ), both GR. Kelly+ 2016: SX appeared 11 Dec 2015 at the
blind-predicted place; 'consistent with the blind predictions of a fraction of the models' and 'most models predict shorter delays'.
A slingshot term ∝ ∂g/∂t is zero for a static lens (T2), so by S-B's own form it adds NOTHING to this delay. The result is the
GR prediction confirmed; it cannot separate S-B from GR unless S-B's term is nonzero for a static cluster, and no number for it exists.

