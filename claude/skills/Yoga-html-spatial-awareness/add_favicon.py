#!/usr/bin/env python3
"""add_favicon.py -- give every tracked HTML page that lacks an icon the project favicon (idempotent; changes nothing else).
   usage: add_favicon.py REPO_DIR [--href URL] [--only FILE ...] [--dry]
   Default href: https://michaelrendier.github.io/assets/favicon.png (one origin serves every project page of michaelrendier.github.io).
   Inserts one <link rel="icon" type="image/png" href="..."> right after the opening <head> tag; skips pages that already have rel=icon.  Prints the files changed."""
import os, re, subprocess, sys
a = sys.argv[1:]; repo = os.path.abspath(a[0]); href = 'https://michaelrendier.github.io/assets/favicon.png'; only = None; dry = '--dry' in a
if '--href' in a: href = a[a.index('--href') + 1]
if '--only' in a: only = [x for x in a[a.index('--only') + 1:] if not x.startswith('--')]
files = only or [f for f in subprocess.run(['git', '-C', repo, 'ls-files', '*.html', '*.htm'], capture_output=True, text=True).stdout.split('\n') if f]
done = []
for f in files:
    p = os.path.join(repo, f); raw = open(p, 'rb').read()
    try: t = raw.decode('utf-8')
    except UnicodeDecodeError: t = raw.decode('latin-1'); enc = 'latin-1'
    else: enc = 'utf-8'
    if re.search(r'rel=["\'](shortcut )?icon["\']', t, re.I): continue
    m = re.search(r'<head[^>]*>', t, re.I)
    if not m: print('SKIP (no <head>):', f); continue
    t2 = t[:m.end()] + f'\n<link rel="icon" type="image/png" href="{href}">' + t[m.end():]
    if not dry: open(p, 'wb').write(t2.encode(enc))
    done.append(f)
print(('would change ' if dry else 'changed ') + str(len(done)) + ' file(s)'); [print(' ', f) for f in done]
