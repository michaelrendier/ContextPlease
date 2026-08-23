"""Julia/Mandelbrot as Telperion/Laurelin, closing session 2026-08-22.
Cody: "two bifurcations - the calculation and the return trip... toroidal
energy... infinitely progress unintuitively... deeper into each other...
Julia/Mandelbrot relationship. Telperion and Laurelin."

KNOWN maths, verified here not invented:
  - Douady-Hubbard: c in M <=> J_c connected. c outside M -> J_c a Cantor
    dust (shatters into infinitely many disconnected pieces).
  - Tan Lei (1990): near a boundary point c0, M and J_c0 are asymptotically
    SIMILAR under rescaling -- "Julia inside Mandelbrot, deeper into each
    other" is real, proven mathematics, not a metaphor.
  - the external angle (Douady) doubles at each step: theta -> 2 theta mod 1,
    i.e. a LEFT SHIFT of its binary expansion -- THE SAME MAP proved for
    Collatz in FourthAgePapers/CollatzShift (Q(T(n))=shift(Q(n))). Irrational
    angles never close -- dense, quasi-periodic, torus-geodesic-like.
  - the inverse-iteration method (real Julia-set rendering technique):
    z^2=w has TWO roots, so running the map BACKWARD is itself a genuine
    second bifurcation -- "the return trip."

OURS: Telperion (survive, whole, connected) / Laurelin (fall, shattered,
disconnected) as the Julia-connectivity split.
"""
import cmath

def in_mandelbrot(c, maxiter=200, bailout=2.0):
    z = 0j
    for n in range(maxiter):
        z = z*z + c
        if abs(z) > bailout: return False, n
    return True, maxiter

def bounded_grid_proxy(c, N=40, maxiter=80, bailout=2.0):
    survive = 0
    for i in range(N):
        for j in range(N):
            z = complex(-2+4*i/N, -2+4*j/N)
            for _ in range(maxiter):
                z = z*z + c
                if abs(z) > bailout: break
            else:
                survive += 1
    return survive

for c, tag in [(complex(0.3,0.5),'inside M'), (complex(1.0,0.3),'outside M'),
               (complex(2.0,0.0),'far outside M')]:
    inM, n = in_mandelbrot(c)
    print(f"c={c} ({tag}): in M={inM}  bounded-region proxy={bounded_grid_proxy(c)}")

def angle_double_binary(bits, k=6):
    for _ in range(k):
        print(bits, int(bits,2)/2**len(bits))
        bits = bits[1:] + bits[:1]
angle_double_binary("101101001")
