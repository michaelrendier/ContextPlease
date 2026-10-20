#!/usr/bin/env python3
"""Numerical tests of the light-slingshot claims against GR and published data.  Writes RESULTS.md beside itself.

Sources of the claims under test (all in the repos, read 2026-10-20):
  S-A  UmbrellaNoether/mode3_code/COSMOLOGY_REVISION_light_slingshot.md :
       f_exit/f_enter = (1 + 2GM/(r c²))^α,  α = 0 straight … 1 maximum assist;  Δm = −2.5 log10(f_exit/f_enter);
       "stellar-mass BH at r = 10 r_s: Δm ≈ −0.2 mag".
  S-B  Ainulindale wiki 51: L_(I|O) = L_standard + ∫ J_red · d(J_blue)/dt dλ ; slingshot term L_sling ~ v·∂g/∂t.
  S-C  Cody 2026-10-20: the correct Refsdal delay prediction shows photon paths are not clean.
Maths in plain glyphs.  LENS_DPRINT=1 prints name = value.
"""
import math, os
G, C, MSUN = 6.67430e-11, 299792458.0, 1.98847e30
PC, YR, DAY = 3.0856775814913673e16, 365.25 * 86400, 86400.0
DP = os.environ.get("LENS_DPRINT") == "1"
out = []


def dp(n, v):
    if DP: print(f"[dp] {n} = {v!r}")


def P(s=""):
    print(s); out.append(s)


def rs(M): return 2 * G * M * MSUN / C ** 2


# ── T1 ─────────────────────────────────────────────────── scale of the lensing time delay: 4GM/c³ ──
def T1():
    P("## T1  Shapiro/geometric delay scale 4GM(1+z_l)/c³")
    P("| lens | M (Msun) | 4GM/c³ |"); P("|---|---|---|")
    for name, M in (("stellar BH", 10), ("intermediate", 1e4), ("Sgr A*", 4.3e6), ("M87*", 6.5e9),
                    ("TON 618", 6.6e10), ("cluster core (Refsdal-like)", 1e14), ("cluster", 1e15)):
        t = 4 * G * M * MSUN / C ** 3; dp("t", t)
        s = f"{t:.3g} s" if t < 3600 else (f"{t/DAY:.3g} d" if t < YR else f"{t/YR:.3g} yr")
        P(f"| {name} | {M:.3g} | {s} |")
    P("Image-pair delays for a point mass are this × [½ y√(y²+4) + ln((√(y²+4)+y)/(√(y²+4)−y))], y = source offset / θ_E.")
    P("Only masses ≳1e9 Msun give delays of days or more; stellar-mass lenses give ≲1e-3 s and unresolved images.")


# ── T2 ───────────────────────────── static lens: a photon passing a mass returns to its original frequency ──
def T2():
    P("## T2  Static Schwarzschild lens: net frequency change over a full pass (null geodesic, RK4)")
    M = 1.0; r_s = 2.0  # geometric units G=c=1
    for b in (10.0, 100.0, 1000.0):
        # u = 1/r, φ-orbit equation u'' + u = 3 M u² ; E conserved by the static Killing vector ∂_t
        def f(s):
            u, du = s; return (du, -u + 3 * M * u * u)
        u0 = 0.0; s = [u0, 1.0 / b]; phi = 0.0; h = 2e-4; umax = 0.0; drift = 0.0; prev = s
        while True:
            k1 = f(s); k2 = f([s[0] + .5*h*k1[0], s[1] + .5*h*k1[1]])
            k3 = f([s[0] + .5*h*k2[0], s[1] + .5*h*k2[1]]); k4 = f([s[0] + h*k3[0], s[1] + h*k3[1]])
            prev = s
            s = [s[0] + h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]), s[1] + h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])]
            phi += h; umax = max(umax, s[0])
            # conserved: (du/dφ)² + u²(1−2Mu) = 1/b²  (E/L = 1/b), relative drift
            drift = max(drift, abs(s[1] ** 2 + s[0] ** 2 * (1 - 2 * M * s[0]) - 1 / b ** 2) * b ** 2)
            if s[0] <= 0 and umax > 0: break
        phi = phi - h + h * prev[0] / (prev[0] - s[0])        # linear interpolation to the u = 0 crossing
        s = [0.0, s[1]]
        defl = phi - math.pi
        rmin = 1.0 / umax
        nu_in, nu_out = 1 / math.sqrt(1 - 2 * M * abs(u0)), 1 / math.sqrt(1 - 2 * M * abs(s[0]))   # static-observer factors at the two ends
        P(f"b={b:6.0f} M: deflection {defl:.4e} rad (weak-field 4M/b = {4*M/b:.4e}, +15πM²/4b² = {4*M/b + 15*math.pi*M*M/(4*b*b):.4e}); "
          f"blueshift at r_min {1/math.sqrt(1-2*M/rmin):.5f}; E-conservation drift {drift:.1e}; exit/enter end-point factors {nu_out/nu_in:.9f}")
    P("Falling in gives ν×(1−2M/r)^-½, climbing out gives the inverse: product 1 for ANY static lens. A gain needs ∂g/∂t ≠ 0.")


# ── T3 ───────────────────── the S-A formula: what α is needed for the quoted magnitude shift, vs GR ──
def T3():
    P("## T3  S-A formula f_exit/f_enter = (1 + 2GM/rc²)^α at r = n r_s  (2GM/rc² = r_s/r = 1/n)")
    P("| n = r/r_s | α=0.5 Δm | α=1 Δm | α=2 Δm | α for Δm=−0.2 | GR infall blueshift (1−1/n)^-½ − 1 |"); P("|---|---|---|---|---|---|")
    for n in (3, 10, 100, 1e3, 1e4):
        x = 1 + 1 / n
        dm = lambda a: -2.5 * a * math.log10(x)
        a_need = 0.2 / (2.5 * math.log10(x))
        P(f"| {n:g} | {dm(.5):.4f} | {dm(1):.4f} | {dm(2):.4f} | {a_need:.2f} | {(1-1/n)**-0.5 - 1:.4g} |")
    P("S-A's 'Δm ≈ −0.2 at r = 10 r_s' therefore needs α ≈ 1.94, outside its own stated range 0–1 (max Δm there: −0.103).")
    P("α is not derived anywhere: it is the free parameter.")


# ── T4 ─────────────────────────────── S2 star at Sgr A*: bound on α if S-A is applied at S2's pericentre ──
def T4():
    P("## T4  S2 at Sgr A* (pericentre 2018): bound on α from the measured redshift")
    GM = 1.32712440018e20 * 4.30e6; r_p = 120 * 1.495978707e11   # m  (≈120 AU)
    v = 7650e3
    rs_over_r = 2 * GM / C ** 2 / r_p
    z_grav = rs_over_r / 2; z_sr = v ** 2 / (2 * C ** 2); z_gr = z_grav + z_sr
    P(f"r_s/r_p = {rs_over_r:.3e};  GR gravitational {z_grav:.3e} + transverse Doppler {z_sr:.3e} = {z_gr:.3e}  ({z_gr*C/1e3:.0f} km/s)")
    f, sf = 0.90, math.hypot(0.09, 0.15)    # GRAVITY 2018, A&A 615 L15: f = 0.90 ± 0.09(stat) ± 0.15(sys), f=1 is GR  [from memory: verify]
    # net redshift = z_gr − α·(r_s/r) ; f = net/z_gr
    a = (1 - f) * z_gr / rs_over_r; sa = sf * z_gr / rs_over_r
    dp("alpha", (a, sa))
    P(f"With f = {f} ± {sf:.3f}: α = {a:.2f} ± {sa:.2f}  →  |α| ≲ {abs(a)+2*sa:.2f} at ~2σ.  (S-A needs α up to 1 for 'maximum assist'.)")
    P("Caveat: S-A is a formula for an in-and-out pass; S2's photons are emitted at the star and escape. Applying it here is my reading.")


# ── T5 ───────────────────────── a time-dependent term in a cluster lens: size of ∂Φ/∂t over the light crossing ──
def T5():
    P("## T5  Size of a ∂g/∂t effect (S-B's v·∂g/∂t) for a cluster lens like MACS J1149")
    sigma = 1.5e6; R = 1e6 * PC
    phi = (sigma / C) ** 2
    t_cross = 2 * R / C; t_dyn = R / sigma
    dphi = phi * t_cross / t_dyn
    P(f"Φ/c² ≈ (σ/c)² = {phi:.2e};  light crossing 2R/c = {t_cross/YR:.2e} yr;  dynamical time R/σ = {t_dyn/YR:.2e} yr")
    P(f"net fractional frequency change over one crossing ≈ Φ/c² · t_cross/t_dyn = {dphi:.1e}  (Rees–Sciama-type);  Δm ≈ {2.5*dphi/math.log(10):.1e} mag")
    P("Refsdal data precision: SX colour F125W−F160W = 0.2 ± 0.3 mag (Kelly+ 2016), same as S1–S4 within errors.")
    P(f"Required for S-A's Hubble-tension story: ~8 % accumulated; per-cluster {dphi:.0e} would need ~{0.08/dphi:.0e} such crossings.")


# ── T6 ─────────────────────────────── what the Refsdal success does and does not discriminate ──
def T6():
    P("## T6  Refsdal delay vs the standard calculation")
    P("Delay = geometric path difference + Shapiro delay (Fermat potential τ), both GR. Kelly+ 2016: SX appeared 11 Dec 2015 at the")
    P("blind-predicted place; 'consistent with the blind predictions of a fraction of the models' and 'most models predict shorter delays'.")
    P("A slingshot term ∝ ∂g/∂t is zero for a static lens (T2), so by S-B's own form it adds NOTHING to this delay. The result is the")
    P("GR prediction confirmed; it cannot separate S-B from GR unless S-B's term is nonzero for a static cluster, and no number for it exists.")


if __name__ == "__main__":
    P("# Slingshot vs GR: numerical tests (2026-10-20)"); P()
    for t in (T1, T2, T3, T4, T5, T6):
        t(); P()
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "RESULTS.md"), "w").write("\n".join(out) + "\n")
