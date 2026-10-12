# Measure character frequency of real JSON text on this machine, in minified-equivalent form:
# every char inside strings (incl. the quotes) + every non-whitespace char outside strings.
# Insignificant whitespace outside strings is not counted (it is absent from minified JSON).
# Printable ASCII only (0x20-0x7E); duplicate files (same sha256) are counted once.
import os, re, sys, hashlib, collections
SKIP = ('/proc', '/sys', '/dev', '/tmp/claude-1000', '/home/rendier/Projects/ThePlace/ContextPlease',
        '/home/rendier/Projects/ThePlace/FourthAgePapers')
TOK = re.compile(r'"(?:[^"\\]|\\.)*"|[^"]+', re.S)
WS = re.compile(r'[ \t\r\n]+')
cnt = collections.Counter(); seen = set(); nfiles = nbytes = 0
for root, dirs, files in os.walk('/'):
    if root.startswith(SKIP) or '/scratchpad' in root:
        dirs[:] = []; continue
    for f in files:
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        try:
            if os.path.islink(p) or os.path.getsize(p) > 20_000_000: continue
            b = open(p, 'rb').read()
        except OSError: continue
        h = hashlib.sha256(b).digest()
        if h in seen: continue
        seen.add(h)
        t = b.decode('utf-8', 'ignore')
        for m in TOK.finditer(t):
            s = m.group()
            if s[0] != '"': s = WS.sub('', s)
            cnt.update(c for c in s if 32 <= ord(c) <= 126)
        nfiles += 1; nbytes += len(b)
print('files', nfiles, 'bytes', nbytes, 'chars counted', sum(cnt.values()))
order = sorted((chr(c) for c in range(32, 127)), key=lambda c: (-cnt[c], c))
open('json_freq.tsv', 'w').write(''.join(f'{c!r}\t{cnt[c]}\n' for c in order))
open('json.perm', 'w', newline='').write(''.join(order))
print(''.join(order))
