import json, sys
sys.path.insert(0, "/home/rendier/Projects/ThePlace")
from ValaQuenta.modules.lagrangian_sm.tools import LagrangianSMModule
from ValaQuenta.modules.witches_hat.tools import WitchesHatModule

def steps(*pairs): return [{"n": i + 1, "op": a, "english": b} for i, (a, b) in enumerate(pairs)]

sm_ops = [("L_SM", "the Standard Model Lagrangian density", "ESTABLISHED"), ("G, W, B", "gauge fields of SU(3), SU(2), U(1)", "ESTABLISHED"), ("H", "the Higgs doublet", "ESTABLISHED"),
          ("D_μ", "covariant derivative with the three gauge couplings", "ESTABLISHED"), ("V(H)", "Higgs potential -μ²H†H + λ(H†H)²", "ESTABLISHED"), ("Y", "Yukawa matrices", "ESTABLISHED")]
sm_eq = {
 "verify": ("Every closure check of the construction as a number.", steps(("anomaly_check", "sum the anomaly coefficients over one generation"), ("group_checks", "close the algebras and test Jacobi"), ("ew_mass_matrix_symbolic", "diagonalise the boson mass matrix"), ("parameter_count", "count the parameters"))),
 "fields": ("The fields with their (SU(3), SU(2), Y) quantum numbers and the number of degrees of freedom.", steps(("field_content", "list the multiplets"), ("degrees_of_freedom", "count Weyl fermions, scalars and gauge bosons"))),
 "anomalies": ("The anomaly coefficients that must vanish for the gauge theory to exist.", steps(("field_content", "take left-handed Weyl fields, conjugating the right-handed ones"), ("sum", "Σ Y³, Σ T(R) Y, Σ Y in exact rational arithmetic"))),
 "hypercharges": ("Hypercharges solved from anomaly cancellation given the multiplets and Y_H = 1/2: unique, equal to the observed values.", steps(("Yukawa invariance", "Y_u = Y_Q + Y_H, Y_d = Y_Q - Y_H, Y_e = Y_L - Y_H"), ("anomalies", "3Y_Q + Y_L = 0 and 6Y_Q - 3Y_u - 3Y_d + 2Y_L - Y_e = 0"), ("solve", "Y_Q = 1/6, Y_L = -1/2"))),
 "su5": ("The source of the anomaly cancellation: the fifteen Weyl fermions fill 5-bar + 10 of SU(5), and the hypercharge is a traceless SU(5) generator.", steps(("generator", "diag(-1/3,-1/3,-1/3,1/2,1/2) on the 5"), ("antisymmetric square", "10 = pairs; the 5-bar is the conjugate"), ("compare", "match the content of field_content, traces, A(10) + A(5-bar)"))),
 "groups": ("SU(2) and SU(3) generators, structure constants, Jacobi identity and Casimirs.", steps(("su2_generators, su3_generators", "build σ/2 and λ/2"), ("structure_constants", "f = -2i Tr([T,T]T)"), ("check", "closure, Jacobi, Casimir"))),
 "parameters": ("The independent real parameters of the most general renormalisable Lagrangian.", steps(("yukawa_real", "2n² per complex Yukawa matrix"), ("flavour symmetry", "subtract broken U(3)^k generators"), ("add", "3 gauge + 2 Higgs + θ_QCD"))),
 "ew_symbolic": ("The W, Z and photon masses from |D H|² with H = (0, v/√2).", steps(("covariant derivative", "A = g T·W + g' Y B"), ("quadratic form", "(A H)†(A H)"), ("Hessian", "mass matrix of (W1, W2, W3, B)"), ("eigenvalues", "g²v²/4 (twice), (g²+g'²)v²/4, 0"))),
 "higgs_symbolic": ("V(h) in the unitary gauge expanded in h.", steps(("substitute", "H†H = (v+h)²/2, μ² = λ v²"), ("expand", "read the h², h³, h⁴ coefficients"))),
 "higgs": ("λ, μ², depth and self-couplings from the measured m_h and v.", steps(("fermi_vev", "v = (√2 G_F)^(-1/2)"), ("pdg_mass", "m_h"), ("λ", "m_h²/2v²"))),
 "ew_tree": ("Tree-level electroweak couplings and masses against PDG.", steps(("e, g, g'", "from α(M_Z) and sin²θ_W"), ("m_W, m_Z", "g v/2, √(g²+g'²) v/2"), ("compare", "percentage difference from the PDG masses"))),
 "yukawas": ("y = √2 m/v for the charged fermions.", steps(("pdg_masses", "read the masses"), ("divide", "√2 m / v"))),
 "ckm": ("CKM and PMNS matrices, unitarity and the Jarlskog invariant.", steps(("ckm_matrix", "standard parametrisation"), ("unitarity_residual", "max |V†V - 1|"), ("jarlskog", "Im(V_us V_cb V*_ub V*_cs)"))),
 "zcouplings": ("Z couplings of every fermion.", steps(("T3, Q", "quantum numbers"), ("g_L, g_R, g_V, g_A", "T3 - Q s², -Q s², T3 - 2Q s², T3"))),
 "vertices": ("The number of distinct interaction vertex types.", steps(("count", "bosonic, gauge-fermion, Yukawa, QCD"))),
 "running": ("One-loop running of the gauge couplings and the scales where pairs meet.", steps(("gauge_initial", "couplings at M_Z"), ("b_i", "41/10, -19/6, -7"), ("crossings", "solve 1/α_i = 1/α_j"))),
 "compare": ("L_SM, L_NN, L_(I|O) and L_dynamic side by side, measured.", steps(("measured_exponents", "double each field and read the degree"), ("bias_conventions", "hat or bowl"), ("one_over_phi_on_bias", "is 1/φ applied"), ("lio_integrand", "is J_red J_blue constant"))),
 "exponents": ("The degree of each term in the fields, Standard Model against the coded L_NN.", steps(("evaluate", "each term at field amplitude a and 2a"), ("log ratio", "n = log2(f(2a)/f(a))"))),
 "loops": ("Each particle's one-loop (Coleman-Weinberg) term in the Higgs potential at h = v.", steps(("particle_content_for_potential", "field-dependent masses m_i(h) and degrees of freedom n_i"), ("coleman_weinberg", "n m^4/(64 pi^2) [ln(m^2/mu^2) - c]"))),
 "hat_temperature": ("The hat at temperature T: brim radius and depth in the high-temperature expansion.", steps(("D, E, T0", "from m_W, m_Z, m_t and v"), ("V(h,T)", "D (T^2 - T0^2) h^2 - E T h^3 + lam_T h^4/4"), ("minimise", "global minimum is the brim"))),
 "hat": ("The SM Higgs hat as a model dict for the path-of-action tools.", steps(("higgs_sector", "λ, μ²"), ("witches_hat.lagrangian_sm", "wrap as a model"))),
}
out = {"engine": "lagrangian_sm", "display": "L_SM: the Standard Model Lagrangian",
       "descriptive": "Builds the Standard Model Lagrangian from its gauge group and field content, checks it (anomalies, group identities, symbolic masses, parameter count) against measured PDG numbers, and measures the coded L_NN and L_(I|O) against it. TO: the Lagrangian's terms, parameters and tree-level observables as plain data. All of it is ESTABLISHED physics; the comparison measures the other Lagrangians' code and states where the structure matches and where it does not.",
       "operators": [{"symbol": a, "english": b, "role": b, "tier": c} for a, b, c in sm_ops],
       "ordering": steps(("choose group and content", "SU(3)×SU(2)×U(1) with the observed multiplets"), ("write the Lagrangian", "most general renormalisable gauge-invariant terms"), ("break the symmetry", "Higgs doublet takes a vev"), ("read the spectrum", "masses, couplings, mixing")),
       "equations": {k: {"descriptive": v[0], "ordering": v[1]} for k, v in sm_eq.items()}}
json.dump(out, open("/home/rendier/Projects/ThePlace/ValaQuenta/engine/proof_locale/lagrangian_sm.json", "w"), indent=1, ensure_ascii=False)
# the witches_hat locale was a copy of circle_atlas: rebuild from its own formulary
wm = WitchesHatModule(); eqs = {}
for e in wm.formulary(): eqs[e.name] = {"descriptive": e.process, "ordering": steps((e.display.split(":")[0].lower(), e.process))}
wh = {"engine": "witches_hat", "display": "The Witch's Hat Engine: snapshot, focus, aim, defocus",
      "descriptive": "Builds a static snapshot of the hat potential, the brim and the classical path bundle (adjustable size, depth, shape, energy, aim) and measures the focus. TO: the hat and its paths as plain data. The rendering is done elsewhere. Higgs numbers, path mechanics and pair correlations are ESTABLISHED; the fermion-hole hat and the cone of dynamic action are the author's THEORETICAL reading.",
      "operators": [{"symbol": "V", "english": "hat potential", "role": "central potential, hilltop 0, brim -1", "tier": "ESTABLISHED"}, {"symbol": "W", "english": "abbreviated action", "role": "integral of sqrt(2(E-V)) ds along a path", "tier": "ESTABLISHED"}, {"symbol": "aim", "english": "launch offset from the radial", "role": "0 gives the point focus at E = 0", "tier": "ESTABLISHED"}],
      "ordering": steps(("hat_shape", "choose the potential"), ("trace", "follow paths from the brim"), ("focus_resolution", "measure the closest approach")), "equations": eqs}
json.dump(wh, open("/home/rendier/Projects/ThePlace/ValaQuenta/engine/proof_locale/witches_hat.json", "w"), indent=1, ensure_ascii=False)
print(len(sm_eq), "SM equations;", len(eqs), "witches_hat equations")
