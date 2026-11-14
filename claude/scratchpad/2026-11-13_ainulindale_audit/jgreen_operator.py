"""JG-op: J_red + J_blue = J_green = 0_RB (- 0_BR), tested on the OPERATOR form of H_hat_RB
(ValaQuenta/modules/h_rb_hat/maths.py docstring):  H = sum_p p^-s [R_p (x) d  +  d^† (x) B_p],  R_p^† = B_p.
Finite stand-in: red term X = sum_p w_p R_p (x) D ; blue term = X^† (the adjoint). Random complex matrices, 3 'primes'.
Readings of 0_BR tried:  (a) 0_BR := adjoint of 0_RB   (b) 0_BR := ordered-product reversal (see jgreen.py)."""
import numpy as np
rng=np.random.default_rng(7); n=4
def rc(): return rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
primes=[2,3,5]; s=0.5
D=rc()
X=sum(p**-s*np.kron(rc(),D) for p in primes)          # red term  R_p (x) d
Xd=X.conj().T                                          # blue term  = (red term)^† since B_p = R_p^†, d^†
H=X+Xd                                                 # H_hat_RB (unsigned sum)  -> "J_red + J_blue = H_hat_RB" (old notation)
A=X-Xd                                                 # signed (orientation-reversed blue)
nrm=np.linalg.norm
print("OP-1 H=X+X^† self-adjoint: |H-H^†| = %.1e"%nrm(H-H.conj().T))
print("OP-2 A=X-X^† anti-self-adjoint: |A+A^†| = %.1e ; i*A self-adjoint: %.1e"%(nrm(A+A.conj().T),nrm(1j*A-(1j*A).conj().T)))
print("OP-3 reading (a): 0_RB:=H, 0_BR:=H^† -> 0_RB-0_BR = %.1e  (H is self-adjoint, so the difference is identically 0)"%nrm(H-H.conj().T))
print("OP-4 reading (a'): 0_RB:=X (red term), 0_BR:=X^† -> 0_RB-0_BR = A = signed J_red+J_blue exactly: |A-(X-Xd)| = %.1e ; |A| = %.2f"%(nrm(A-(X-Xd)),nrm(A)))
print("OP-5 dot/cross: H = 2 Re-part (symmetric, 'dot'), A = 2i Im-part (antisymmetric, 'cross'); H and A are never equal: |H-A| = %.2f, |H|=%.2f |A|=%.2f"%(nrm(H-A),nrm(H),nrm(A)))
print("OP-6 H as the sum of its own two terms is a tautology: J_red+J_blue=H holds by DEFINITION (old notation), and equals 0_RB only if 0_RB:=H (Cody 2026-11-13: H_hat_RB elsewhere, 0_RB in the Monad).")
print("OP-7 the three candidate J_green: (i) H=X+X^† [self-adjoint, symmetric]; (ii) X-X^† [anti-self-adjoint, cross]; (iii) [J_blue,J_red] trine commutator (sedenion test, trine.py). (i)!=(ii) by OP-5; they agree only if the 'minus' is the orientation sign on J_blue (JG-4).")
