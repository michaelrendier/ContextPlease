import numpy as np
from cdalg import *
asr = bk.assessors()
def zd_planes(mus):
    T = table(mus); planes = [(a, b + 8) for (a, b) in asr]
    cap, info = [], []
    for p1 in range(42):
        i1, i2 = planes[p1]
        for p2 in range(42):
            j1, j2 = planes[p2]
            M = np.stack([T[i1, j1], T[i1, j2], T[i2, j1], T[i2, j2]], axis=1)       # 16 x 4
            u_, s_, vh = np.linalg.svd(M)
            k = int(np.sum(s_ < 1e-9)) + (4 - len(s_))
            null = vh[4 - k:].conj().T if k else None                                 # 4 x k
            if k == 0: continue
            sols = []
            if k == 1:
                n = null[:, 0]; Dt = n[0] * n[3] - n[1] * n[2]
                if abs(Dt) < 1e-9: sols.append(n)
            elif k == 2:
                N1, N2 = null[:, 0], null[:, 1]
                f = lambda t1, t2: (t1 * N1[0] + t2 * N2[0]) * (t1 * N1[3] + t2 * N2[3]) - (t1 * N1[1] + t2 * N2[1]) * (t1 * N1[2] + t2 * N2[2])
                A = f(1, 0); C = f(0, 1); B = f(1, 1) - A - C
                if abs(A) < 1e-12 and abs(C) < 1e-12 and abs(B) < 1e-12: sols.append(('family', None))
                else:
                    disc = B * B - 4 * A * C
                    if abs(A) > 1e-12:
                        for rt in np.roots([A, B, C]):                                # t1/t2 ratio
                            if abs(np.imag(rt)) < 1e-9 or np.iscomplexobj(mus) or any(np.iscomplex(m) and np.imag(m) != 0 for m in mus):
                                sols.append(rt * N1 + N2)
                    elif abs(B) > 1e-12:
                        sols.append(N2); sols.append(-C / B * N1 + N2 if False else N1)
                    else:
                        sols.append(N1)
            else:
                sols.append(('family', None))
            if sols:
                cap.append((p1, p2)); info.append((k, sols))
    return planes, cap, info
def summarise(mus):
    planes, cap, info = zd_planes(mus)
    deg = np.zeros(42, int)
    for (p1, p2) in cap: deg[p1] += 1
    strut = lambda p: asr[p][0] ^ asr[p][1]
    within = sum(1 for (p1, p2) in cap if strut(p1) == strut(p2))
    nulls = {}
    for k, _ in info: nulls[k] = nulls.get(k, 0) + 1
    kap = set()
    for (p1, p2), (k, sols) in zip(cap, info):
        for s in sols:
            if isinstance(s, tuple): kap.add('family'); continue
            n = s
            if abs(n[0]) > 1e-9:
                kx = n[2] / n[0]
                kap.add(complex(np.round(kx, 4)) if np.iscomplexobj(kx) and abs(np.imag(kx)) > 1e-9 else float(np.round(np.real(kx), 4)))
    return dict(capable_ordered_plane_pairs=len(cap), planes_with_a_partner=int((deg > 0).sum()),
                degree_set=sorted(set(deg.tolist())), within_chart=within, nullity_hist=nulls,
                kappa_x=sorted(kap, key=lambda z: (abs(z) if not isinstance(z, str) else 1e9))[:8])
