"""Ordered (bijective base-N) address over a .perm ordering. No hashing anywhere."""
import sys
sys.set_int_max_str_digits(0)
try:
    from gmpy2 import mpz as _I      # speed only; identical results
except Exception:
    _I = int

_pw = {}
def _pow(N, e):
    k = (N, e)
    if k not in _pw: _pw[k] = _I(N) ** e
    return _pw[k]

def _fold(d, N):
    if len(d) <= 48:
        v = _I(0)
        for x in d: v = v * N + x
        return v
    m = len(d) // 2
    return _fold(d[:m], N) * _pow(N, len(d) - m) + _fold(d[m:], N)

def _unfold(v, k, N):
    if k <= 48:
        out = [0] * k
        for i in range(k - 1, -1, -1):
            v, r = divmod(v, N); out[i] = int(r)
        return out
    b = k // 2
    hi, lo = divmod(v, _pow(N, b))
    return _unfold(hi, k - b, N) + _unfold(lo, b, N)

def offset(k, N):                       # number of words shorter than k
    return (_pow(N, k) - 1) // (N - 1)

def load_perm(path):
    out = []
    for ln in open(path, encoding='ascii'):
        ln = ln.split('#')[0].strip()
        if ln: out.append(chr(int(ln, 16)))
    return out

def address(text, perm):
    N = len(perm); idx = {c: i for i, c in enumerate(perm)}
    try: d = [idx[c] for c in text]
    except KeyError as e: raise ValueError('character %r not in perm' % e.args[0])
    return int(offset(len(d), N) - 1 + _fold(d, N)) if d else -1

def text_at(a, k, perm):
    N = len(perm)
    if k == 0: return ''
    plain = _I(a) + 1 - offset(k, N)
    if not (0 <= plain < _pow(N, k)): raise ValueError('address does not have length %d' % k)
    return ''.join(perm[i] for i in _unfold(plain, k, N))
