import nbformat as nbf, sys
H="import sys, os\nsys.path.insert(0, os.path.abspath('../../..'))\n"
def build(path, title, intro, cells):
    nb=nbf.v4.new_notebook(); nb.cells=[nbf.v4.new_markdown_cell(f"# {title}\n\n{intro}")]
    for kind,src in cells:
        nb.cells.append(nbf.v4.new_markdown_cell(src) if kind=="md" else nbf.v4.new_code_cell(src))
    nb.metadata["kernelspec"]={"display_name":"Python 3","language":"python","name":"python3"}
    nbf.write(nb,path)

build("notebooks/engines/22_circle_atlas.ipynb","22 — The Circle Atlas",
"**H_hat_RB and the Complete Shape of Mathematics: every viewport run TO and FROM the circle.** Status: `THEORETICAL:CALCULATED` — each viewport's closure is ESTABLISHED numerics; reading the TO/FROM pairs as the entry and exit of fixed-point space is the project's framing.\n\n**Orientation / aperture** (observer-position): the unit circle in ℂ as the common target; one viewport in view at a time; sedenion axes 1..15. **Rule:** a mapping algorithm, not a fit — a failure is printed as a failure.",
[("code",H+"from ValaQuenta.modules.circle_atlas import maths as M\nfrom ValaQuenta.modules.pi_derivations import maths as PI\nprint('emergent pi =', PI.emergent_pi()['value'], '(first zero of the cosine series, doubled)')"),
 ("md","## 1. The atlas: TO (enter) and FROM (exit), one line per viewport"),
 ("code","for e in M.atlas():\n    t=e['to']; f=e['from']\n    print(f\"{e['id']:15s} TO {'closes' if t['ok'] else 'NOT raw'} (res {t['residual']:.1e})  FROM {'ok' if f['ok'] else 'NO'}  pi: {e['pi_route']}\")"),
 ("md","## 2. Berry–Keating H = xp is a recorded failure until it is Wick-rotated"),
 ("code","e=M.entry('berry_keating'); print(e['to'])"),
 ("md","## 3. The Lagrangian is NOT run backwards: its FROM has a fibre\nL, 3L and L + d/dt(F) share the stationary path (action gradient ≈ 0 for each)."),
 ("code","e=M.entry('lagrangian'); print(e['to']['transform']); print(e['from'])"),
 ("md","## 4. Sedenion: 15 exact circles, 336 annihilating circle-point pairs, SIGN on e₈…e₁₅"),
 ("code","e=M.entry('sedenion'); print(e['to']); print(e['from']); print(M.sign_carriers())"),
 ("md","## 5. Sign-posts: the road in, the road out, the π route"),
 ("code","for r in M.signposts():\n    print(r['id'], '|', r['enters'][:70], '|', r['pi'])"),
 ("md","## 6. Gaps (not hidden)"),
 ("code","g=M.gaps(); print('no pi route:', g['no_pi_route']); print('TO fails raw:', g['to_fails_raw'])\nfor x in g['named_gaps']: print('-', x['viewport'])"),
 ("md","## 7. Repository census (text count, where to look — not proof)"),
 ("code","c=M.census()\nfor r,v in c.items():\n    if v.get('missing'): continue\n    print(f\"{r:30s} files {v['files']:4d} lines {v['lines']:7d} with-hits {v['files_with_hits']:4d} pi {v['tokens']['pi']:5d} circle {v['tokens']['circle']:5d} wave {v['tokens']['wave']:5d}\")"),
 ("md","## 8. Import probe — which modules do not load"),
 ("code","r=M.import_probe(); print(len(r['ok']), 'import;', len(r['failed']), 'fail'); print(r['failed'])"),
 ("md","## 9. Self-check"),
 ("code","v=M.verify(); print(all(v.values()), [k for k,x in v.items() if x is not True])"),
])
build("notebooks/engines/23_pi_derivations.ipynb","23 — The Pi Derivation Toolset",
"**Every route to π, none reading `math.pi`, each labelled by what of the circle its inputs already hold.** Status: `ESTABLISHED:CALCULATED`. The emergent π is `cos_zero`: twice the first positive zero of the cosine power series — no diameter, circumference, angle or polygon.\n\n**Orientation / aperture:** real and complex arithmetic; one route in view at a time.",
[("code",H+"from ValaQuenta.modules.pi_derivations import maths as M"),
 ("md","## 1. The emergent π"),
 ("code","print(M.emergent_pi())"),
 ("md","## 2. All routes"),
 ("code","for r in M.all_routes():\n    print(f\"{r['id']:24s} {str(r['value'])[:20]:22s} err {r['error']:.1e}  circle_in={r['circle_in']}\")"),
 ("md","## 3. The circle audit — where is the circle already in the inputs?"),
 ("code","for k,v in M.circle_audit().items(): print(f'{k:12s}', v)"),
 ("md","## 4. The project's U(1) normalisation (2/π)·π = 2 is an identity"),
 ("code","import math\nfor fake in (3.0, 3.14159, 22/7, 100.0): print(fake, (2/fake)*fake)\nprint(M.derive('u1_normalisation'))"),
 ("md","## 5. Self-check"),
 ("code","v=M.verify(); print(all(v.values()), [k for k,x in v.items() if x is not True])"),
])
