"""Der(A) = { D : D(xy) = D(x)y + xD(y) }  -- the Lie algebra of Aut(A).
The Leibniz condition is LINEAR in D, so dim Der(A) is a null-space dimension.
"""
import numpy as np, sys
sys.path.insert(0,'/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/2026-08-08_sedenion_igpu_benchmark')
from sedbench2 import cd_mul_slow as mul

def structure_constants(n):
    C = np.zeros((n,n,n))
    for i in range(n):
        ei = np.zeros(n); ei[i]=1
        for j in range(n):
            ej = np.zeros(n); ej[j]=1
            C[i,j,:] = mul(ei,ej)
    return C

def dim_der(n, tol=1e-8):
    C = structure_constants(n)
    # unknowns D[a,b] flattened as a*n+b ; equations indexed by (i,j,m)
    # sum_k C[i,j,k] D[m,k] - sum_k D[k,i] C[k,j,m] - sum_k D[k,j] C[i,k,m] = 0
    N2 = n*n
    AtA = np.zeros((N2,N2))
    rows = []
    for i in range(n):
        for j in range(n):
            for m in range(n):
                r = np.zeros(N2)
                for k in range(n):
                    r[m*n+k] += C[i,j,k]
                    r[k*n+i] -= C[k,j,m]
                    r[k*n+j] -= C[i,k,m]
                rows.append(r)
            if len(rows) >= 4096:
                R = np.array(rows); AtA += R.T@R; rows=[]
    if rows:
        R = np.array(rows); AtA += R.T@R
    ev = np.linalg.eigvalsh(AtA)
    ev = np.clip(ev, 0, None)
    scale = max(ev.max(), 1e-30)
    return int(np.sum(ev/scale < tol)), N2

print(f"{'algebra':22s}{'dim':>6s}{'dim Der(A)':>12s}   identification")
ID = {1:'0            (trivial)', 2:'0            Aut = Z/2, discrete',
      4:'3            so(3) -> Aut = SO(3)', 8:'14           g2 -> Aut = G2  EXCEPTIONAL',
      16:'?', 32:'?'}
for n, name in ((2,'C  complex'),(4,'H  quaternion'),(8,'O  octonion'),
                (16,'S  SEDENION'),(32,'T32')):
    d, N2 = dim_der(n)
    exp = ID.get(n,'?')
    print(f"{name:22s}{n:>6d}{d:>12d}   expected {exp}")

print("\n=== does Der(S) annihilate e0 AND e8? (representation-theoretic prediction) ===")
import numpy as np
def der_basis(n, tol=1e-8):
    C = structure_constants(n); N2=n*n; rows=[]
    for i in range(n):
        for j in range(n):
            for m in range(n):
                r=np.zeros(N2)
                for k in range(n):
                    r[m*n+k]+=C[i,j,k]; r[k*n+i]-=C[k,j,m]; r[k*n+j]-=C[i,k,m]
                rows.append(r)
    A=np.array(rows)
    U,S,Vt=np.linalg.svd(A, full_matrices=True)
    ns=Vt[np.sum(S>tol*S.max()):]
    return [v.reshape(n,n) for v in ns]

B = der_basis(16)
print(f"  basis of Der(S): {len(B)} generators")
for idx in (0, 8, 1, 9):
    mx = max(np.linalg.norm(D[:,idx]) for D in B)
    print(f"    max |D(e_{idx})| over all generators = {mx:.2e}   "
          f"{'ANNIHILATED (trivial rep)' if mx<1e-8 else 'moved (nontrivial rep)'}")
