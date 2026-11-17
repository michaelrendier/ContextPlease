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
("md","## 4b. Sphere and hypersphere, and the n-ball\nA circle lives in every sphere; the sedenion's unit sphere S¹⁵ is a sphere of circles that is not closed under the product."),
 ("code","import math\nfor k in ('sphere','hypersphere'):\n    e=M.entry(k); print(k, e['to']['ok'], e['to']['residual'])\nprint(M.entry('hypersphere')['to']['norm_defect_of_unit_products'])\nt=M.ball_table()\nfor r in t['rows']: print(r['n'], round(r['V'],5), round(r['S_{n-1}'],5), r['ball/cube'])\nprint('peak V at n =', t['peak_volume_dim'], '; peak area at n =', t['peak_area_dim'], '; V_n=(2pi/n)V_(n-2) residual', t['recursion_residual'])"),
 ("md","## 4c. Recursive field axes and what the 15 imaginary operations do to the Real component\nThe axis is any point of S¹⁴; the 15 are one basis. Re(exp(θe_k)·z) = r cos θ − y_k sin θ for every k."),
 ("code","print(M.entry('field_axis')['to'])\nr=M.real_component_effect(); print('all laws hold:', r['all_laws_hold'])\nfor row in r['rows']: print(row['axis'], row['planes'])"),
 ("md","## 4d. The two native units: ln 10 (decades) and π (half-turns)"),
 ("code","print(M.entry('native_units')['to']); print(M.entry('native_units')['from']['independence'])\nz=-3+4j; a,b=M.native_coords(z); print(z,'->',(a,b),'->',M.from_native(a,b))"),
 ("md","## 4e. The box-kite as a spectral emitter and interpreter\nEmit: the operator L_d of a zero-divisor diagonal is skew, its flow has lines at 0, √2, 2 (|d|=√2). Interpret: the lines say 'zero divisor'; the nullspace (eigenvectors) names the four annihilating partners and so the kite."),
 ("code","k=M.kite_spectrum()\nfor kk,v in k.items(): print(kk, ':', v)"),
  ("md","## 4f. Attach a string: the same kite, read from an anchor\nThe bare spectrum is one signature for all 84 diagonals. From an anchor a, the reading of b is σ(L_a L_b): the 84 split into 7 classes (sizes 2, 2, 4, 4 inside the anchor's own kite; 8, 32, 32 outside). This is the De Marrais-kite analogue of the scalar kite's string; the scaled kite (moving under G2) is not computed here."),
 ("code","r=M.anchored_readings(); print({k:v for k,v in r.items() if k!='constructs'})\nfor c in r['constructs']: print('-', c['name'], '|', c['reads'])"),
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
("md","## 5b. Modular route: π from the Heegner number 163, and what sets the speed of Ramanujan–Chudnovsky\nThe series are exact identities; their speed (digits gained per term) is the decade coordinate of e^{π√d} minus log₁₀ of a fixed integer."),
 ("code","import math\nprint(M.derive('heegner_163')['value'], 'error at 60 digits:', M.heegner_error(60))\nfor d,c in ((163,1728),(58,256)):\n    s=M.series_speed(d); print(d, s, 'log10(%d) = %.4f'%(c, math.log10(c)))"),
 ("md","## 5c. π from a 3-ball counted on a lattice"),
 ("code","print(M.derive('ball3_lattice'))"),
  ("md","## 6. Self-check"),
 ("code","v=M.verify(); print(all(v.values()), [k for k,x in v.items() if x is not True])"),
])
