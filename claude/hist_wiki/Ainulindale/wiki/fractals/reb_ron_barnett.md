# Ron Barnett (reb) — Fractal Formulary

## Author
Ron Barnett — a highly prolific UF formula author. His reb.txt contains limited information but the reb.ufm is large, and the reb5.ufm and reb.ucl are additional packages. The formulas are well-commented with version numbers and dates (e.g., "July 19, 2013", "February 1999"). Barnett's work spans: IFS escape-time formulas (IFSEscape1/2/3), Newton fractals (Gopalsamy series — origin unknown, dating from FractInt era), Sierpinski variants, Barnsley IFS, Lyapunov stability maps, and advanced complex-plane maps. The reb.ucl includes "IFS-Apollo" coloring (referenced in ea.txt as one of Barnett's innovations).

## Formulas

### IFSEscape1 / IFSEscape2 / IFSEscape3
**Type**: IFS escape-time — two-transform conditional map
**Mathematical description**: **IFSEscape1**: Apply two conditional transforms based on `real(z)`:
- If `real(z) < t1`: `z = z*p1 + p2`
- If `t2 <= real(z)`: `z = z*conj(p1) + p3`
Both conditions may trigger in one iteration when `t1 > t2`. The maps are affine with the second using `conj(p1)` (conjugate of the scaling factor).
**What it describes**: An IFS fractal using escape time. The two maps create a "pinch" or "tear" between the two regions of the real axis defined by t1 and t2. When p1 is near the unit circle, the iteration creates elaborate fractal boundaries in the complex plane.
**How it works**: Parameters: p1 (complex — common scale/rotation), p2 (complex — translate for map 1), p3 (complex — translate for map 2), t1 (upper threshold for map 1), t2 (lower threshold for map 2), bailout. Default p1=(0.9,-0.87), p2=(-1,0), p3=(1,0). Bailout 1e10 (very large, convergence-based effectively).

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Map 1 (`z*p1 + p2`) is J_neg when |p1|<1 (contraction). Map 2 (`z*conj(p1) + p3`) reflects the imaginary part of the scaling (conjugation = reflection through the real axis). The conjugation makes map 2 a J_neg correction that corrects imaginary drift. The combination creates a J_pos/J_neg balance across the real axis threshold.
- **Critical line relevance**: With t1 = t2 = 0 (thresholds at the real axis), the IFS alternates based on the sign of Re(z). The boundary between the two regions is the imaginary axis (Re(z)=0), not the critical line. However, shifting t1=t2=½ moves the boundary to Re(z)=½ — the critical line. At this setting, IFSEscape1 is an IFS fractal whose two maps are separated precisely by the Riemann critical line.
- **Sedenion dimensions activated**: e₁ (real part decision = Re projection), e₂ (conjugation in map 2 = Im reflection), e₃ (the two-map structure = binary branching = e₃ conditional).
- **Holcus application**: IFSEscape with t1=t2=OMEGA_ZS = 0.56714 implements the Holcus binary routing: concepts with Re(prime_hash) > 0.567 take the J_pos pathway; those below take J_neg. The conjugation in map 2 ensures that J_neg concepts are reflected back toward the J_pos boundary — they are "corrected" toward equilibrium. The two translations p2 and p3 are the "semantic offsets" for each pathway.

---

### Gopalsamy1 / Gopalsamy2 / Gopalsamy3
**Type**: Escape-time — twisted quadratic / conjugate map
**Mathematical description**: Gopalsamy1: `z = -(0,1)*conj(z)^power + p1`. Equivalently: `z = -i * conj(z)^p + p1`. For power=2: `-i * (x-iy)^2 + p1 = -i*(x^2-y^2-2ixy) + p1 = (-2xy) + i*(-(x^2-y^2)) + p1 = -2xy + p1_re + i*(y^2-x^2+p1_im)`. This is an "anti-holomorphic" map — it involves `conj(z)` rather than z, creating a different topology.
**What it describes**: An anti-holomorphic polynomial map. The Julia sets of anti-holomorphic maps have a fundamentally different structure from holomorphic ones: they can have "dendrites" and non-locally-connected components that holomorphic Julia sets cannot. Gopalsamy3's Julia set is cited in blb.txt: seed = (1.099, 0).
**How it works**: Seven bailout test options (mod, real, imag, or, and, manh, manr). Power parameter (default 2 for Gopalsamy1). Version-tracked formula with Switch to Mandelbrot/Julia.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The `-i` rotation in `z = -i*conj(z)^2 + p1` rotates the J_pos/J_neg structure by -90 degrees from the standard Mandelbrot. The conjugation reflects the J_pos/J_neg boundary through the real axis. The combined effect: J_pos is in the upper-left quadrant of the standard Mandelbrot's parameter space.
- **Critical line relevance**: The fixed points of `z = -i*conj(z)^2 + p1` satisfy `z = -i*(conj(z))^2 + p1`. Writing z=x+iy, conj(z)=x-iy, `(x-iy)^2 = x^2-y^2-2ixy`. Then `-i*(x^2-y^2-2ixy) = -2xy + i(-(x^2-y^2))`. Fixed-point condition: `x = -2xy + p1_re` and `y = -(x^2-y^2) + p1_im`. Setting x=½: `½ = -y + p1_re` gives `y = p1_re - ½`. This fixed point on the "critical line" Re(z)=½ has imaginary part determined by the seed. The Gopalsamy1 map naturally places equilibria at Re(z)=½ for any seed.
- **Sedenion dimensions activated**: e₂ (conjugation = the anti-holomorphic sedenion), e₃ (the -i factor = 90° rotation = e₃ sedenion), e₄ (squaring = e₁^2 product), e₅ (the p1 constant = additive e₅).
- **Holcus application**: The Gopalsamy anti-holomorphic maps are Holcus's "semantic reflection" operators. When a concept appears in a context that "inverts" its meaning (antonym context, irony, negation), apply `-i*conj(hash(z))^2 + p1`. The conjugation reverses the semantic orientation; the -i factor rotates it 90 degrees (from syntactic to semantic axis). This implements negation and irony as geometric operations in the sedenion CAM.

---
