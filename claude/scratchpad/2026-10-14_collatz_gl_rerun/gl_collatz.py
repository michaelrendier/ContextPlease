"""Run the Collatz map through the CURRENT GenerationalLineage engine (1.0.0 + toolsets) and re-check the CollatzShift paper's inner workings.
Nothing here changes either repository. Provenance tags: MEASURED (exhaustive/exact), CONTROL (random null), FINDING (a reading of the numbers)."""
import sys, math, random, time, json, statistics as st
from fractions import Fraction
sys.path.insert(0, '/home/rendier/Projects/ThePlace/GenerationalLineage')
import importlib.util
_sp = importlib.util.spec_from_file_location('e_collatz_shift', '/home/rendier/Projects/ThePlace/FourthAgePapers/CollatzShift/engine/e_collatz_shift.py'); _cs = importlib.util.module_from_spec(_sp); sys.modules['e_collatz_shift'] = _cs; _sp.loader.exec_module(_cs)
from engine.add_scale_sign import ASS, ASSWord, CAMSHAFT, compose
from engine.toolsets import lyndon, permutation, periodicity, berlekamp_massey, re_pair
from engine import lines as GLlines
T, parity_word, parity_vector, branch_affine = _cs.T, _cs.parity_word, _cs.parity_vector, _cs.branch_affine
out = {}
def sec(t): print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)

sec('0. state of the engine: GL toolsets self-verify')
t = time.time(); v = GLlines.verify_all(); 
ok = {k: (r.get('ok', r.get('holds', r.get('all_hold', r.get('passed')))) if isinstance(r, dict) else r) for k, r in v.items()}
print(len(v), 'toolsets;', 'pass flags:', ok, f'{time.time()-t:.1f}s')

sec('1. T on each branch, written as ASS elements (x -> sign*scale*x + add)')
EVEN = ASS(add=0.0, scale=0.5, sign=1)           # n/2
ODD = ASS(add=0.5, scale=1.5, sign=1)            # (3n+1)/2
print('even branch :', EVEN, '| residual without SIGN identical:', EVEN.residual('SIGN') == EVEN)
print('odd branch  :', ODD, '| residual without SIGN identical:', ODD.residual('SIGN') == ODD)
print('ODD as composition  ADD(1/2) @ SCALE(3/2) == ODD :', (ASS.ADD(0.5) @ ASS.SCALE(1.5)) == ODD)
print('ASS.SIGN(-1) (the engine\'s SIGN) occurs in either branch: ', EVEN.sign == -1 or ODD.sign == -1)
print('CAMSHAFT (engine firing order, innermost first):', CAMSHAFT, '| Collatz odd branch fires SCALE then ADD')
print('ADD-first alternative  (n+a)*3/2 reproduces (3n+1)/2 only with a = 1/3, not an integer:', Fraction(3, 2) * Fraction(1, 3) == Fraction(1, 2))

sec('2. exhaustive: composing the branch ASS elements along ANY parity word gives T^k on its class (all words of length k <= 12)')
def compose_word(w):
    el = ASS.SCALE(1.0)
    for b in w: el = (ODD if b else EVEN) @ el
    return el
bad = 0; n_checked = 0
for k in range(1, 13):
    # every residue class j mod 2^k, its actual parity word
    for j in range(1 << k):
        w = parity_word(j, k); el = compose_word(w); d = sum(w)
        n_checked += 1
        if el.scale != 3 ** d / 2 ** k: bad += 1; continue
        n = j + (1 << k) * 3                       # a lift
        m = n
        for _ in range(k): m = T(m)
        if abs(el(float(n)) - m) > 1e-6 * max(1, m): bad += 1
print(f'classes checked {n_checked}, mismatches {bad}  (scale == 3^d/2^k exactly and el(n) == T^k(n) on a lift)')
out['ass_composition_mismatches'] = bad

sec('3. the engine\'s Long-Path memory (set membership, Recaman rule) on Collatz orbits')
def word_of_orbit(n):
    steps = []; m = n
    while True:
        steps.append(ODD if m & 1 else EVEN)
        m = T(m)
        if m == 1: break
    return steps
rows = []
for n in (27, 97, 871, 6171, 77031):
    steps = word_of_orbit(n)
    w = ASSWord(steps=tuple(steps) + (ODD, EVEN), order='collatz', source=compose(*steps))   # two more steps: 1 -> 2 -> 1 (ODD at 1, then EVEN at 2)
    col = w.collisions(float(n), tol=0)
    first = col[0] if col else None
    rows.append((n, len(steps), first[:2] if first else None))
    print(f'n={n:6d}  stopping time (steps to 1) = {len(steps):4d}  first revisit of a value: steps {first[0]}->{first[1]} at value {first[2]}' if first else f'n={n} no collision')
out['first_collision'] = rows

sec('4. permutation toolset on the parity-vector bijection Q_k : Z/2^k -> Z/2^k')
cyc = {}
for k in range(1, 15):
    Q = [parity_vector(j, k) for j in range(1 << k)]
    r = permutation.descend(Q)
    cyc[k] = (len(r['cycles']), r['order'], r['sign'], r['fixed_points'])
    print(f"k={k:2d}  size {1<<k:6d}  cycles {len(r['cycles']):5d}  fixed points {r['fixed_points']:3d}  order {r['order']}  sign {r['sign']:+d}  longest cycle {max(map(len, r['cycles']))}")
out['Q_cycle_summary'] = cyc

sec('4b. Q_k: isometry check, power-of-two cycle lengths, fixed points (the numbers whose parity word is their own binary digits)')
Qs = {k: [parity_vector(j, k) for j in range(1 << k)] for k in range(1, 15)}
iso_bad = sum(1 for k in range(2, 15) for j in range(1 << k) if Qs[k][j] % (1 << (k - 1)) != Qs[k - 1][j % (1 << (k - 1))])
print('Q_k(n) mod 2^(k-1) == Q_(k-1)(n mod 2^(k-1)) for all n, k = 2..14: violations =', iso_bad, ' (so Q is an isometry of the 2-adic metric, level by level)')
allpow2 = True
for k in range(1, 15):
    seen = [False] * (1 << k)
    for j in range(1 << k):
        if seen[j]: continue
        L = 0; m = j
        while not seen[m]: seen[m] = True; m = Qs[k][m]; L += 1
        if L & (L - 1): allpow2 = False
print('every cycle length of Q_k, k = 1..14, is a power of two:', allpow2)
fp = {k: [j for j in range(1 << k) if Qs[k][j] == j] for k in (3, 4, 5, 6)}
print('fixed points of Q_k:', fp)
out['Q_isometry_violations'] = iso_bad; out['Q_all_cycles_power_of_two'] = allpow2
sec('5. factor moves on orbit parity streams, with a random control of the same length (CONTROL first)')
def stream(n):
    s = []; m = n
    while m != 1: s.append(m & 1); m = T(m)
    s.append(1); s.append(0)        # 1 -> 2 -> 1
    return s
def metrics(bits):
    sx = ''.join(map(str, bits))
    bm = berlekamp_massey.descend(bits)
    rp = re_pair.descend(sx)
    ly = lyndon.descend(sx)
    pr = periodicity.descend(sx)
    return dict(n=len(bits), L=bm['linear_complexity'], determined=bm['determined'], repair_ratio=round(rp['compression_ratio'], 3), repair_depth=rp['depth'], lyndon_factors=ly['omega'], min_period=pr['min_period'])
rng = random.Random(20261014)
for n in (27, 97, 871, 6171, 77031):
    s = stream(n); real = metrics(s)
    ctrl = [metrics([rng.randint(0, 1) for _ in range(len(s))]) for _ in range(40)]
    print(f'n={n:6d} len {len(s):4d} | Collatz: L={real["L"]} (N/2={len(s)//2}) repair {real["repair_ratio"]} depth {real["repair_depth"]} lyndon {real["lyndon_factors"]} period {real["min_period"]}'
          f'  | control(40): L mean {st.mean(c["L"] for c in ctrl):.1f} sd {st.pstdev(c["L"] for c in ctrl):.1f}, repair {st.mean(c["repair_ratio"] for c in ctrl):.3f}, lyndon {st.mean(c["lyndon_factors"] for c in ctrl):.1f}')
per = metrics([1, 0] * 20)
print('periodic parity word (10)^20 for comparison:', per)

sec('6. the first-run faults of the paper, re-found with the engine\'s own tools')
# necklace filter: primitive necklaces of length k with d ones, via Lyndon words
def lyndon_words(k, d):
    cnt = 0
    for x in range(1 << k):
        w = format(x, f'0{k}b')
        if w.count('1') != d: continue
        r = lyndon.descend(w)
        if r['omega'] == 1 and r['all_lyndon']: cnt += 1
    return cnt
def necklaces_naive(k, d):
    seen = set()
    for x in range(1 << k):
        w = format(x, f'0{k}b')
        if w.count('1') != d: continue
        seen.add(min(w[i:] + w[:i] for i in range(k)))
    return len(seen)
for k, d in ((4, 2), (6, 3), (8, 4)):
    print(f'k={k} d={d}: rotation-minimal words {necklaces_naive(k, d)}  vs  primitive (Lyndon) words {lyndon_words(k, d)}   (the paper\'s first fault was reporting the first as cycles)')
json.dump(out, open('gl_collatz_results.json', 'w'), indent=1, default=str)
