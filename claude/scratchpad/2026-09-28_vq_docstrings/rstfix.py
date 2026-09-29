"""Make existing docstrings valid reST without changing their words.
 - indented regions inside prose -> literal blocks ('::' + blank lines)
 - '|' and '*' outside double-backtick spans and literal blocks -> escaped
Field-list part (from first ':param'-style line) only gets '|' escaped."""
import ast, re, sys, glob, textwrap
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import docedit

FIELD = re.compile(r'^:(param|type|returns?|rtype|raises|ivar|cvar|var|keyword)\b')

def esc(line):
    parts = re.split(r'(``[^`]*``)', line)
    out = []
    for p in parts:
        if p.startswith('``') and p.endswith('``') and len(p) > 4:
            out.append(p); continue
        p = re.sub(r'(?<!\\)\|', r'\\|', p)
        p = re.sub(r'(?<!\\)\*', r'\\*', p)
        out.append(p)
    return ''.join(out)

def esc_pipe(line):
    parts = re.split(r'(``[^`]*``)', line)
    return ''.join(p if (p.startswith('``') and len(p) > 4) else re.sub(r'(?<!\\)\|', r'\\|', p) for p in parts)

def indent(l): return len(l) - len(l.lstrip(' '))

def normalise(doc):
    lines = doc.split('\n')
    k = next((i for i, l in enumerate(lines) if FIELD.match(l)), len(lines))
    prose, fields = lines[:k], lines[k:]
    out = []
    i = 0
    base = 0
    n = len(prose)
    while i < n:
        l = prose[i]
        if not l.strip():
            out.append(''); i += 1; continue
        if indent(l) > base and (not out or out[-1].strip() or True):
            # start of an indented region: gather until a non-blank line with indent <= base
            j = i
            while j < n and (not prose[j].strip() or indent(prose[j]) > base):
                j += 1
            # trim trailing blanks of the region
            e = j
            while e > i and not prose[e-1].strip(): e -= 1
            region = prose[i:e]
            # already a literal block or reST construct? keep only if previous paragraph ends with '::'
            prev = next((x for x in reversed(out) if x.strip()), '')
            if prev.rstrip().endswith('::') and out and not out[-1].strip():
                out.extend(region)
            else:
                if out and out[-1].strip() and out[-1].rstrip().endswith(':') and not out[-1].rstrip().endswith('::'):
                    out[-1] = out[-1].rstrip() + ':'
                    out.append('')
                elif not prev.rstrip().endswith('::'):
                    if out and out[-1].strip(): out.append('')
                    out.extend(['::', ''])
                else:
                    if out and out[-1].strip(): out.append('')
                out.extend(region)
            if e < n: out.append('')
            i = e
            continue
        # normal prose line
        out.append(esc(l))
        # a following non-blank, non-indented line is fine; blank handled above
        i += 1
    res = '\n'.join(out).rstrip('\n')
    if fields:
        res = res + '\n\n' + '\n'.join(esc_pipe(x) for x in fields)
    # collapse >2 blank lines
    res = re.sub(r'\n{3,}', '\n\n', res)
    return res

def run(path, write=True):
    src = open(path).read(); tree = ast.parse(src)
    edits = {}
    for q, k, n in docedit.items(tree):
        d = ast.get_docstring(n)
        if not d: continue
        nd = normalise(d)
        if nd != d: edits[q] = {'doc': nd}
    if edits and write:
        docedit.apply(path, edits)
    return len(edits)

if __name__ == '__main__':
    tot = 0
    for f in sys.argv[1:]:
        c = run(f); tot += c
    print('changed', tot)
