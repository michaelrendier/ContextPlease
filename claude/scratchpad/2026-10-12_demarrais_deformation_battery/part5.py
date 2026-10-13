import sys, math, cmath, subprocess
import numpy as np
from cdalg import *
asr = bk.assessors()
DV = np.array([diag_vec(a, b, s) for (a, b) in asr for s in (1, -1)])
W1 = 0.5671432904097838
def apply_f(x, a, b, f):
    dp, dm = bk.diagonal_amplitudes(list(x), a, b); z = complex(dp, dm); w = f(z)
    y = x.copy(); y[a] = (w.real + w.imag) / math.sqrt(2); y[b + 8] = (w.real - w.imag) / math.sqrt(2); return y
funcs = [('Joukowsky z+c/z, c=Omega_ZS', lambda z: z + W1 / z), ('Moebius (z-1)/(z+1)', lambda z: (z - 1) / (z + 1)),
         ('exp(z)', cmath.exp), ('z^2', lambda z: z * z), ('tanh(z/2)', lambda z: cmath.tanh(z / 2)),
         ('rotate z by pi/2', lambda z: z * 1j), ('conj', lambda z: z.conjugate()), ('1/z', lambda z: 1 / z),
         ('z * e^{0.3 i}', lambda z: z * cmath.exp(0.3j)), ('z + 0.3 (shift, real)', lambda z: z + 0.3), ('z + 0.3 i (shift, imag)', lambda z: z + 0.3j)]
print("CS-04b  same test, magnitudes lam in {0.3, 1.0, 2.5}: fraction of (plane, diagonal) cases still zero divisors, d+ line / d- line")
print("   %-30s %-24s %-24s %-24s" % ("f", "lam=0.3 (d+ | d-)", "lam=1.0 (d+ | d-)", "lam=2.5 (d+ | d-)"))
for name, f in funcs:
    cells = []
    for lam in (0.3, 1.0, 2.5):
        r = []
        for sg in (1, -1):
            keep = tot = 0
            for (aa, bb) in asr[::3]:
                x = lam * diag_vec(aa, bb, sg) / math.sqrt(2)
                try: y = apply_f(x, aa, bb, f)
                except ZeroDivisionError: continue
                n = np.linalg.norm(y)
                if n < 1e-12: continue
                d0 = min(np.linalg.norm(mul(y, DV[j])) for j in range(84)) / n
                tot += 1; keep += d0 < 1e-9
            r.append("%d/%d" % (keep, tot))
        cells.append(" | ".join(r))
    print("   %-30s %-24s %-24s %-24s" % ((name,) + tuple(cells)), flush=True)

PTOL = '/home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptol'
def ptolv(p):
    out = subprocess.run([PTOL, '-r', p], capture_output=True, text=True).stdout.split('\n'); v = []; i = 0
    while out[i].strip() != '---': v.append(float(out[i])); i += 1
    return np.array(v[:16])
subj = {'nuclear': ["neutron generation", "pressurized water reactor", "control rods absorb neutrons", "fission releases heat"],
        'cooking': ["bake the bread dough", "simmer the tomato sauce", "whisk eggs and sugar", "roast the chicken slowly"],
        'music': ["tune the violin strings", "the drummer keeps rhythm", "compose a symphony in minor key", "sing the chorus"],
        'weather': ["the storm brings heavy rain", "cold front moves east", "hurricane forms over warm ocean", "morning fog over the valley"]}
H16 = np.array([[(-1) ** bin(i & j).count('1') for j in range(16)] for i in range(16)], float)
rows = []; lab = []
for s, ps in subj.items():
    for p in ps:
        v = ptolv(p); en = v * v; en = en / en.sum()
        r = bk.chart_of(list(v), check_zd=False); ce = np.array([r['chart_energy'][k] for k in range(1, 8)]); ce = ce / ce.sum()
        rows.append(dict(chart=ce, walsh=(H16 @ en)[1:], amp=np.abs(v), energy=en)); lab.append(s)
def sep(key):
    X = np.array([r[key] for r in rows]); lab_ = np.array(lab)
    inter, intra = [], []
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            (intra if lab_[i] == lab_[j] else inter).append(np.linalg.norm(X[i] - X[j]))
    # leave-one-out 1-NN accuracy
    ok = 0
    for i in range(len(X)):
        d = [(np.linalg.norm(X[i] - X[j]), lab_[j]) for j in range(len(X)) if j != i]
        ok += min(d)[1] == lab_[i]
    return np.mean(inter) / np.mean(intra), ok / len(X)
print("\nSC-04  which live reading of the address carries topic?  16 prompts, 4 subjects (chance 1-NN = 0.25)")
print("   %-34s %-18s %s" % ("feature of the projected address", "inter/intra dist", "leave-one-out 1-NN"))
for key, name in (('chart', '7 chart energies (box-kite lens)'), ('walsh', '15 Walsh coefficients of v^2 (chi_1..15)'),
                  ('energy', '16 raw energies v_k^2'), ('amp', '16 raw |v_k|')):
    s, a = sep(key); print("   %-34s %-18.3f %.3f" % (name, s, a), flush=True)
