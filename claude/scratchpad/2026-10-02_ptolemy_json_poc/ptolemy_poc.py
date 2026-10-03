"""Proof of concept: ptolemy.json (1 entry) -> TABLES.json -> ROWS.json -> text. Every ingest:
reconstruct TABLES from ptolemy.json, append, reindex, overwrite ptolemy.json.
Only ptolemy.json is kept on disk. No hashing."""
import os, re, sys, time
import hyperindex as H

HERE = os.path.dirname(os.path.abspath(__file__))
ASCII = H.load_perm(os.path.join(HERE, 'perm/ascii.perm'))
NORM = {'’': "'", '‘': "'", '“': '"', '”': '"', '—': '-'}

def normalise(raw):
    t = raw.replace('\r\n', '\n').replace('\r', '\n')
    for k, v in NORM.items(): t = t.replace(k, v)
    bad = sorted(set(c for c in t if c not in set(ASCII)))
    if bad: raise ValueError('outside the 97: %r' % bad)
    return t

def dante(path):
    raw = open(path, encoding='utf-8').read()
    a = raw.index('*** START OF'); a = raw.index('\n', a) + 1
    return normalise(raw[a:raw.index('*** END OF')].strip('\n'))

# ---- canonical JSON entry (fixed key order, no whitespace, one per line) ----
def entry(addr, n, ts, perm):
    return '{"HYPERINDEX":"%d","DATALENGTH":%d,"TIMESTAMP":"%s","PERM":"%s"}\n' % (addr, n, ts, perm)

_E = re.compile(r'\{"HYPERINDEX":"(-?\d+)","DATALENGTH":(\d+),"TIMESTAMP":"([^"]*)","PERM":"([a-z]+)"\}\n')
def parse(text):
    out, pos = [], 0
    while pos < len(text):
        m = _E.match(text, pos)
        if not m: raise ValueError('bad entry at %d' % pos)
        out.append((int(m[1]), int(m[2]), m[3], m[4])); pos = m.end()
    return out

PERMS = {}
def perm(name):
    if name not in PERMS: PERMS[name] = H.load_perm(os.path.join(HERE, 'perm/%s.perm' % name))
    return PERMS[name]

def write_atomic(path, s):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='ascii') as f: f.write(s)
    os.replace(tmp, path)

# ---- chunkers: a partition of the text; join == text ----
def whole(t): return [t]
def canto(t):
    parts = re.split(r'(?m)^(?=Inferno: Canto )', t)
    return [p for p in parts if p]
def stanza(t):
    return re.findall(r'.*?\n\n+|.+\Z', t, flags=re.S)
def lines(t): return t.splitlines(keepends=True)
def fixed(n): return lambda t: [t[i:i+n] for i in range(0, len(t), n)]
CHUNKERS = {'whole': whole, 'canto': canto, 'stanza': stanza, 'line': lines, 'fixed1000': fixed(1000)}

# ---- the machine ----
def load_tables(top_path):
    if not os.path.exists(top_path): return ''
    (a, n, ts, p), = parse(open(top_path, encoding='ascii').read())
    return H.text_at(a, n, perm(p))

def ingest(top_path, doc, chunker, ts):
    tables = load_tables(top_path)                                   # reconstruct TABLES from the one file
    rows = ''.join(entry(H.address(c, ASCII), len(c), ts, 'ascii') for c in chunker(doc))   # ROWS.json
    tables += entry(H.address(rows, perm('json')), len(rows), ts, 'json')                   # append, reindex ROWS
    J = perm('json')
    write_atomic(top_path, entry(H.address(tables, J), len(tables), ts, 'json'))            # reindex TABLES, overwrite
    return len(rows), len(tables)

def reconstruct(top_path):
    """ptolemy.json alone -> list of documents (each = join of its rows)."""
    docs = []
    for a, n, ts, p in parse(load_tables(top_path)):
        rows = parse(H.text_at(a, n, perm(p)))
        docs.append(''.join(H.text_at(ra, rn, perm(rp)) for ra, rn, _, rp in rows))
    return docs
