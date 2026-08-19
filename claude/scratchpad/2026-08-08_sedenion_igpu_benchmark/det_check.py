import numpy as np, itertools
# quaternion left-regular 4x4 rep
def Lq(q):
    a,b,c,d = q
    return np.array([[a,-b,-c,-d],[b,a,-d,c],[c,d,a,-b],[d,-c,b,a]],float)
rng = np.random.default_rng(0)
print("det(L_q) vs N(q)^2:")
for _ in range(5):
    q = rng.normal(size=4)
    N = float(q@q)
    print(f"  det={np.linalg.det(Lq(q)):+.6f}   N^2={N**2:+.6f}   ratio={np.linalg.det(Lq(q))/N**2:.6f}")
print("\neigenvalues of L_q for unit PURE imaginary q (a0=0):")
for _ in range(3):
    q = rng.normal(size=4); q[0]=0; q/=np.linalg.norm(q)
    ev = np.linalg.eigvals(Lq(q))
    print("  ", np.round(np.sort_complex(ev),6))
