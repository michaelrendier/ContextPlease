"""
"what EXACT information can I get from just a temperature — can we decompose
temperatures?"  (Cody, 2026-08-28)

Two parts:
 A. the exact list — everything a single T fixes, with known constants only.
 B. the decomposition — T against the four-question test (skill §3), and the
    T = 1/β = J_N(scale) relationship checked on the fold.
"""
import math

# ── constants (SI, CODATA-ish) ───────────────────────────────────────────
k_B   = 1.380649e-23           # J/K   (exact, SI 2019)
h     = 6.62607015e-34         # J·s   (exact)
hbar  = h / (2 * math.pi)
c     = 299792458.0            # m/s   (exact)
sigma = 2 * math.pi**5 * k_B**4 / (15 * h**3 * c**2)   # Stefan–Boltzmann
b_wien = 2.897771955e-3        # m·K   (Wien displacement, exact-ish)
zeta3 = 1.2020569031595943

def exact_from_T(T, label):
    print(f"\n── T = {T:.6g} K   ({label}) ──")
    lam_max = b_wien / T                                   # Wien peak (flux/λ)
    nu_max  = 2.821439 * k_B * T / h                       # Wien peak (flux/ν)
    j       = sigma * T**4                                 # W/m²  radiated power density
    u_rad   = 4 * j / c                                    # J/m³  radiation energy density
    n_gamma = 16 * math.pi * zeta3 * (k_B * T / (h * c))**3  # photons / m³
    E_mean  = 2.701178 * k_B * T                           # J    mean photon energy
    s_dens  = (4.0/3.0) * u_rad / T                        # J/(K·m³) radiation entropy density
    landauer = k_B * T * math.log(2)                       # J    min energy to erase one bit
    kT_eV   = k_B * T / 1.602176634e-19
    print(f"  λ_max (Wien)          = {lam_max:.6e} m")
    print(f"  ν_max                 = {nu_max:.6e} Hz")
    print(f"  j = σT⁴               = {j:.6e} W/m²")
    print(f"  u_rad = 4j/c          = {u_rad:.6e} J/m³")
    print(f"  n_γ  ∝ T³             = {n_gamma:.6e} photons/m³")
    print(f"  <E_γ> = 2.701 kT      = {E_mean:.6e} J   = {E_mean/1.602176634e-19:.4f} eV")
    print(f"  s_rad = (4/3)u/T ∝ T³ = {s_dens:.6e} J/(K·m³)")
    print(f"  Landauer kT ln2       = {landauer:.6e} J   (min erase energy / bit)")
    print(f"  kT                    = {kT_eV:.6e} eV")
    return lam_max

print("═" * 70)
print("A.  EXACT INFORMATION FROM A SINGLE TEMPERATURE  (known constants only)")
print("═" * 70)
print("""
  A temperature alone (no other measurement) EXACTLY fixes, for a black body
  in equilibrium:
    · the peak wavelength / frequency of its spectrum      λ_max = b/T
    · the total radiated power per area                    j = σT⁴
    · the radiation energy density                         u = 4j/c = aT⁴
    · the photon number density                            n_γ = (16πζ(3)/(hc)³)(kT)³
    · the mean photon energy                               <E> = 2.701 kT
    · the radiation entropy density                        s = (4/3)(u/T) ∝ T³
    · the Landauer bound (min energy to erase one bit)     kT ln2
    · the thermal de Broglie wavelength of a species       Λ = h/√(2πmkT)   (needs m)
  Every one of these is an EXACT function of T — no fit, no free parameter.
  T is a COMPLETE spectral address for an equilibrium field.
""")
exact_from_T(2.72548, "CMB today")
exact_from_T(1.416784e32, "Planck temperature")

print("\n\n" + "═" * 70)
print("B.  DECOMPOSITION — T against the four-question test (skill §3)")
print("═" * 70)
print("""
  Q1 count or ratio of something else?   T = ∂U/∂S  — energy PER unit entropy.
     A RATIO. → tier 3, DERIVED.  (same verdict for P = −∂U/∂V, energy per
     volume; both are intensive = ∂(energy)/∂(extensive) = ratios.)
  Q2 fixed set?                          no.
  Q3 changes length?                     via β only (below).
  Q4 needs an added constraint?          "at constant V" (for T) / "at constant
     S" (for P) — each is a COROLLARY of U with one variable held. → not
     primitive.

  So temperature is NOT a tier-0 primitive. Its lineage:

     β  = 1/(kT)   is the primitive one — the exponential RATE in e^{−βE}
                    (canonical ensemble). ln p(E) = −βE + const  ⇒  β is a
                    SLOPE in log-probability space  ⇒  β = SCALE (a gain).
     T  = 1/(kβ)   is the J_N INVERSE of that scale:  r → 1/r.
                    Temperature lives on the far side of the fold from β.

     GENERATIONAL LINEAGE OF TEMPERATURE
       tier 0   SCALE            β  (the rate in e^{−βE})
       tier 1   J_N(SCALE)       1/β                      (r → 1/r)
       tier 3   RATIO            T = (1/k)·(1/β) = ∂U/∂S   (energy per entropy)

     GENERATIONAL LINEAGE OF PRESSURE
       tier 0   SCALE            number density n = N/V
       tier 0   SCALE            β
       tier 3   RATIO            P = n·kT = n/β = −∂U/∂V   (momentum flux
                                 = energy per volume)
""")

# ── check: T and β are J_N images on the fold ────────────────────────────
def gamma(Z, Z0):  return (Z - Z0) / (Z + Z0)

print("  CHECK — T ↔ β as a J_N (r→1/r) pair on the fold:")
print(f"  {'T (K)':>12s} {'β·k = 1/T':>14s} {'Γ(T; T0=300)':>14s} {'Γ(β; β0=1/300)':>16s}  sum")
T0 = 300.0
for T in [2.72548, 100.0, 300.0, 1000.0, 1.416784e32]:
    beta_k = 1.0 / T
    gT = gamma(T, T0)
    gB = gamma(beta_k, 1.0 / T0)
    print(f"  {T:>12.4g} {beta_k:>14.4e} {gT:>14.6f} {gB:>16.6f}  {gT + gB:>+.2e}")
print("  Γ(T) + Γ(1/T) = 0 exactly  ⇒  T is the J_N reflection of β about r=1.")

print("""

  C.  THERMODYNAMICS = 0_RB  (the structural claim)
  ─────────────────────────────────────────────────
     dU = T dS − P dV      ← the fundamental thermodynamic relation

     matches  Σ_RB = 0_RB − 0_BR   term for term:
       T dS   →  the entropy / J_blue / TELPERION / backward term
                 (d* = "entropy side", canonical_maths)
       P dV   →  the inertia / J_red / LAURELIN / forward term
                 (Ω_ZS = "inertia side", canonical_maths ;  P = momentum flux)
       −      →  the ANTISYMMETRY (0_RB − 0_BR, cross not dot — canonical_maths
                 "same algebraic signature as a cross product")
       U      →  the conserved E in  Scale·Resolution = xp = E

     In the generalized equation  Γ = tanh(½ Σ_k [ g_k·ln s_k + a_k ]):
       ln s_k  (SCALE)  =  the  d(ln V)  expansions   → the P dV work
       g_k     (SIGN)   =  the sign of  dS            → heat in / out
       a_k     (ADD)    =  the conserved particle counts (dN)

     ⇒  inertia : pressure  ::  entropy : temperature.  0_RB read on the fold
        IS the first law.
""")
