"""Header-image options for GenerationalLineage (1280x640 SVG, the GitHub social-preview ratio). The flow chart is drawn from the code's own real output:
factor_lineage(360), ASS.descend(-12, ref 3), build_up's 6 firing orders; the toolset list is engine.LINE_TOOLSETS (30)."""
import sys, html
sys.path.insert(0, '/home/rendier/Projects/ThePlace/GenerationalLineage')
from engine import LINE_TOOLSETS as TS
SANS = "'DejaVu Sans', Verdana, Helvetica, Arial, sans-serif"; MONO = "'DejaVu Sans Mono', Consolas, Menlo, monospace"
e = html.escape
def t(x, y, s, size=16, fill='#e8ecf8', w='normal', fam=SANS, anchor='start', extra=''):
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" {extra}>{e(s)}</text>'
def box(x, y, w, h, stroke, fill, rx=10, sw=2): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def arrow(x1, y1, x2, y2, col, mk): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="3" marker-end="url(#{mk})"/>'
def chip(x, y, w, h, fill, txt, tc='#000', size=15, fam=SANS, w_='bold'): return box(x, y, w, h, fill, fill, rx=h/2, sw=1) + t(x + w/2, y + h/2 + size*0.35, txt, size, tc, w_, fam, 'middle')
def defs(P):
    return f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{P['bg0']}"/><stop offset="1" stop-color="{P['bg1']}"/></linearGradient>
<radialGradient id="glow" cx="0.3" cy="0.4" r="0.7"><stop offset="0" stop-color="{P['glow']}" stop-opacity="0.22"/><stop offset="1" stop-color="{P['glow']}" stop-opacity="0"/></radialGradient>
<marker id="aG" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto"><path d="M0,0 L14,7 L0,14 z" fill="{P['down']}"/></marker>
<marker id="aV" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto"><path d="M0,0 L14,7 L0,14 z" fill="{P['up']}"/></marker>
<marker id="aN" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto"><path d="M0,0 L14,7 L0,14 z" fill="{P['mut']}"/></marker></defs>'''
def toolset_panel(P, x, y, w, h, ncol=2):
    names = list(TS); out = [box(x, y, w, h, P['line'], P['card'], 12)]
    out.append(t(x + 18, y + 34, '30 TOOLSETS', 22, P['gold'], 'bold')); out.append(t(x + 18, y + 56, 'one contract: descend · build_up · verify', 14, P['mut']))
    cw = (w - 36) / ncol; rows = (len(names) + ncol - 1) // ncol; top = y + 84; rh = (h - 84 - 56) / rows
    for i, n in enumerate(names):
        c, r = divmod(i, rows); cx = x + 18 + c * cw; cy = top + r * rh; ln = TS[n]['line']
        col = P['both'] if ln == 'both' else (P['dec'] if ln == 'decomposition' else P['eme'])
        out.append(f'<circle cx="{cx+6}" cy="{cy+rh*0.5-3}" r="5" fill="{col}"/>'); out.append(t(cx + 18, cy + rh*0.5 + 2, n, 15, P['fg'], 'normal', MONO))
    ly = y + h - 28
    for j, (lab, col) in enumerate((('both lines', P['both']), ('descent only', P['dec']), ('ascent only', P['eme']))):
        lx = x + 18 + j * (w - 36) / 3; out.append(f'<circle cx="{lx+5}" cy="{ly-4}" r="5" fill="{col}"/>'); out.append(t(lx + 16, ly, lab, 13, P['mut']))
    return ''.join(out)
def wrap(P, body, title_x=24):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" width="1280" height="640" role="img" aria-label="Generational Lineage: the Add Scale Sign decomposition flow and the 30 toolsets">{defs(P)}'
            f'<rect width="1280" height="640" fill="url(#bg)"/><rect width="1280" height="640" fill="url(#glow)"/>{body}</svg>')
DARK = dict(bg0='#0a1022', bg1='#111b3a', glow='#3b82f6', card='#0f1730', line='#2c3a6b', fg='#e8ecf8', mut='#a3b0d6', gold='#f2c14e', down='#6ee7a1', up='#c4a8ff', both='#5ad1ff', dec='#f2c14e', eme='#c4a8ff', red='#ff8a8a', chipfg='#000')
LIGHT = dict(bg0='#fbfaf4', bg1='#eef2fb', glow='#f2c14e', card='#ffffff', line='#b9c3e0', fg='#101a33', mut='#4a5780', gold='#8a5a00', down='#0b7a43', up='#5b2fb8', both='#0a6fa8', dec='#a86a00', eme='#6b3fd0', red='#b3261e', chipfg='#000')

def flow_vertical(P):
    o = []; down, up = P['down'], P['up']
    o.append(t(24, 44, 'GENERATIONAL LINEAGE', 32, P['gold'], 'bold')); o.append(t(24, 68, 'exact factoral decomposition on two lines: descent is free, ascent is paid, or refused', 15, P['mut']))
    o.append(box(24, 84, 832, 40, P['line'], P['card'])); o.append(t(440, 110, 'any object: integer 360 · operator · word · signal · group', 17, P['fg'], 'bold', SANS, 'middle'))
    o.append(arrow(440, 124, 440, 142, P['mut'], 'aN'))
    o.append(box(24, 144, 832, 58, P['line'], P['card'])); o.append(t(36, 166, 'two_trees(n): the exact partition', 15, P['mut'], 'bold', MONO))
    for i, (lab, col) in enumerate((('TELPERION  prime', P['gold']), ('LAURELIN  composite', P['both']), ('MINGLING  {0, 1}', P['up']))): o.append(chip(34 + i * 270, 172, 252, 24, col, lab, '#000', 14))
    # lanes
    o.append(arrow(240, 202, 240, 222, down, 'aG')); o.append(arrow(640, 222, 640, 202, up, 'aV'))
    o.append(box(24, 224, 404, 232, down, P['card'], 10, 2)); o.append(t(38, 248, 'DESCENT  ·  free  ·  cost 0', 17, down, 'bold'))
    o.append(t(38, 270, 'factor_lineage(360): peel a prime, recurse', 14, P['mut'], 'normal', MONO))
    tree = ['360 → 2', ' └ 180 → 2', '    └ 90 → 2', '       └ 45 → 3', '          └ 15 → 3 · 5']
    for i, ln in enumerate(tree): o.append(t(46, 296 + i * 22, ln, 17, P['fg'], 'normal', MONO))
    o.append(t(38, 418, 'leaves [2, 2, 2, 3, 3, 5]  ·  5 generations', 15, P['gold'], 'bold', MONO)); o.append(t(38, 440, 'every leaf rolls down: root_irreducible(op)', 14, P['mut'], 'normal', MONO))
    o.append(box(452, 224, 404, 232, up, P['card'], 10, 2)); o.append(t(466, 248, 'ASCENT  ·  paid, or refused', 17, up, 'bold'))
    o.append(t(466, 272, 'build_up(target)', 15, P['mut'], 'normal', MONO))
    o.append(box(466, 282, 376, 86, up, 'none', 8, 1)); o.append(t(478, 304, 'search the 6 firing orders of', 14, P['fg'])); o.append(t(478, 326, '{ SIGN, SCALE, ADD }', 17, P['gold'], 'bold', MONO)); o.append(t(478, 350, '[SCALE, ADD] = ADD  →  order matters', 14, P['mut'], 'normal', MONO))
    o.append(arrow(654, 368, 654, 384, up, 'aV'))
    o.append(box(466, 386, 376, 58, P['red'], 'none', 8, 2)); o.append(t(478, 408, 'hit: cost = orders tried (6)', 14, P['fg'], 'normal', MONO)); o.append(t(478, 430, 'undetermined: AscentNotFree', 15, P['red'], 'bold', MONO))
    # floor
    o.append(arrow(240, 456, 240, 476, down, 'aG')); o.append(arrow(640, 476, 640, 456, up, 'aV'))
    o.append(box(24, 478, 832, 92, P['gold'], P['card'], 12, 3)); o.append(t(40, 504, 'TIER-0 FLOOR   Aff(1, ℝ) = ADD ⋊ (SCALE × SIGN)', 17, P['gold'], 'bold', MONO))
    o.append(t(40, 530, 'x ↦ sign · scale · x + add', 18, P['fg'], 'bold', MONO))
    o.append(t(40, 556, 'descend(−12, ref 3):  SIGN −  ·  SCALE 4  ·  ADD 0   (three lookups, no search)', 15, P['mut'], 'normal', MONO))
    for i, (lab, col) in enumerate((('SIGN', P['red']), ('SCALE', P['both']), ('ADD', P['down']))): o.append(chip(580 + i * 92, 494, 84, 30, col, lab, '#000', 15))
    o.append(box(24, 580, 832, 44, P['line'], P['card'])); o.append(t(440, 608, 'verify(): round trip 1e-12  ·  44 self-checked relations  ·  Noether: one conserved sum on both lines', 14.5, P['fg'], 'normal', SANS, 'middle'))
    o.append(toolset_panel(P, 876, 16, 388, 608))
    return wrap(P, ''.join(o))

def flow_horizontal(P):
    o = []; down, up = P['down'], P['up']
    o.append(t(24, 44, 'GENERATIONAL LINEAGE', 32, P['gold'], 'bold')); o.append(t(24, 68, 'read it down for free · build it up and pay · or be refused', 15, P['mut']))
    cols = [(24, 'READ', 'descent · free', down), (302, 'FLOOR', 'tier 0 · ADD ⋊ (SCALE × SIGN)', P['gold']), (580, 'REBUILD', 'ascent · paid, or refused', up)]
    for x, h, sub, col in cols:
        o.append(box(x, 92, 262, 470, col, P['card'], 12, 3)); o.append(t(x + 16, 124, h, 24, col, 'bold')); o.append(t(x + 16, 146, sub, 13, P['mut'], 'normal', MONO))
    o.append(arrow(286, 330, 300, 330, P['mut'], 'aN')); o.append(arrow(564, 330, 578, 330, P['mut'], 'aN'))
    # READ
    o.append(t(40, 182, 'two_trees(n)', 14, P['mut'], 'bold', MONO)); o.append(chip(40, 192, 230 - 8, 22, P['gold'], 'TELPERION · prime', '#000', 13)); o.append(chip(40, 220, 222, 22, P['both'], 'LAURELIN · composite', '#000', 13)); o.append(chip(40, 248, 222, 22, P['up'], 'MINGLING · {0, 1}', '#000', 13))
    o.append(t(40, 304, 'factor_lineage(360)', 14, P['mut'], 'bold', MONO))
    for i, ln in enumerate(['360 → 2', ' └180 → 2', '   └90 → 2', '     └45 → 3', '       └15 → 3·5']): o.append(t(40, 330 + i * 22, ln, 16, P['fg'], 'normal', MONO))
    o.append(t(40, 462, '[2,2,2,3,3,5]', 16, P['gold'], 'bold', MONO)); o.append(t(40, 484, '5 generations · ω = 6', 14, P['mut'], 'normal', MONO)); o.append(t(40, 520, 'cost = 0', 22, down, 'bold'))
    # FLOOR
    o.append(t(318, 190, 'x ↦ sign·scale·x + add', 17, P['fg'], 'bold', MONO))
    for i, (lab, col, d) in enumerate((('SIGN', P['red'], 'read the sign'), ('SCALE', P['both'], '|x| ÷ |ref|'), ('ADD', P['down'], 'the offset'))): o.append(chip(318, 212 + i * 72, 112, 30, col, lab, '#000', 16)); o.append(t(444, 233 + i * 72, d, 14, P['mut'], 'normal', MONO)); 
    o.append(t(318, 440, 'descend(−12, ref 3)', 14, P['mut'], 'bold', MONO)); o.append(t(318, 464, '→ SIGN −  SCALE 4  ADD 0', 15, P['fg'], 'normal', MONO)); o.append(t(318, 520, 'three lookups', 18, P['gold'], 'bold'))
    # REBUILD
    o.append(t(596, 182, 'build_up(target)', 14, P['mut'], 'bold', MONO)); o.append(t(596, 214, 'try every firing order', 15, P['fg']))
    for i, p in enumerate(['SIGN SCALE ADD', 'SIGN ADD SCALE', 'SCALE SIGN ADD', 'SCALE ADD SIGN', 'ADD SIGN SCALE', 'ADD SCALE SIGN']): o.append(t(596, 242 + i * 24, f'{i+1}  {p}', 15, P['gold'] if i == 0 else P['fg'], 'bold' if i == 0 else 'normal', MONO))
    o.append(t(596, 410, '[SCALE, ADD] = ADD', 15, P['mut'], 'normal', MONO)); o.append(t(596, 432, 'so the order matters', 14, P['mut'])); o.append(t(596, 476, 'cost = 6 orders tried', 15, up, 'bold', MONO)); o.append(t(596, 510, 'undetermined →', 15, P['fg'])); o.append(t(596, 534, 'AscentNotFree', 18, P['red'], 'bold', MONO))
    o.append(box(24, 576, 818, 48, P['line'], P['card'])); o.append(t(433, 606, 'verify() · round trip 1e-12 · 44 self-checked relations · Noether: one conserved sum', 14.5, P['fg'], 'normal', SANS, 'middle'))
    o.append(toolset_panel(P, 876, 16, 388, 608))
    return wrap(P, ''.join(o))

def flow_radial(P):
    import math
    o = []; down, up = P['down'], P['up']; cx, cy = 500, 356
    o.append(t(24, 44, 'GENERATIONAL LINEAGE', 32, P['gold'], 'bold')); o.append(t(24, 68, 'everything is built from three operations: ADD, SCALE, SIGN', 15, P['mut']))
    for r, col in ((232, P['line']), (176, P['line'])): o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="3 7"/>')
    outer = [('integer', 'lineage · stencil'), ('word', 'lyndon · re_pair'), ('operator', 'jordan_chevalley'), ('signal', 'spectral · logperiodic'), ('group', 'pohlig_hellman'), ('sequence', 'berlekamp_massey'), ('cipher', 'periodicity · unicity'), ('circle', 'circle · matrix_flow')]
    for i, (a, b) in enumerate(outer):
        ang = -math.pi / 2 + i * 2 * math.pi / len(outer); x = cx + 232 * math.cos(ang); y = cy + 232 * math.sin(ang)
        o.append(box(x - 84, y - 24, 168, 48, P['line'], P['card'], 10)); o.append(t(x, y - 4, a, 16, P['fg'], 'bold', SANS, 'middle')); o.append(t(x, y + 15, b, 12, P['mut'], 'normal', MONO, 'middle'))
        x2 = cx + 192 * math.cos(ang); y2 = cy + 192 * math.sin(ang); x1 = cx + 140 * math.cos(ang); y1 = cy + 140 * math.sin(ang)
        d_=0.09; xa=cx+192*math.cos(ang-d_); ya=cy+192*math.sin(ang-d_); xb=cx+140*math.cos(ang-d_); yb=cy+140*math.sin(ang-d_)
        o.append(arrow(cx+192*math.cos(ang+d_), cy+192*math.sin(ang+d_), cx+140*math.cos(ang+d_), cy+140*math.sin(ang+d_), down, 'aG')); o.append(arrow(xb, yb, xa, ya, up, 'aV'))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="128" fill="{P["card"]}" stroke="{P["gold"]}" stroke-width="3"/>')
    o.append(t(cx, cy - 88, 'tier-0 floor', 14, P['gold'], 'bold', MONO, 'middle'))
    tri = [(cx, cy - 58, 'SIGN', P['red']), (cx - 66, cy + 28, 'SCALE', P['both']), (cx + 66, cy + 28, 'ADD', P['down'])]
    o.append(f'<polygon points="{cx},{cy-58} {cx-66},{cy+28} {cx+66},{cy+28}" fill="none" stroke="{P["mut"]}" stroke-width="2"/>')
    for x, y, lab, col in tri: o.append(chip(x - 38, y - 15, 76, 30, col, lab, '#000', 15))
    o.append(t(cx, cy + 74, 'x ↦ sign·scale·x + add', 14, P['fg'], 'bold', MONO, 'middle')); o.append(t(cx, cy + 96, 'ADD ⋊ (SCALE × SIGN)', 13, P['mut'], 'normal', MONO, 'middle'))
    o.append(box(24, 96, 196, 92, down, P['card'], 10)); o.append(t(36, 120, 'DESCENT', 16, down, 'bold')); o.append(t(36, 142, 'free · cost 0', 14, P['fg'], 'normal', MONO)); o.append(t(36, 164, '360 → 2·2·2·3·3·5', 14, P['gold'], 'normal', MONO)); o.append(t(36, 181, '5 generations', 12, P['mut'], 'normal', MONO))
    o.append(box(24, 480, 196, 118, up, P['card'], 10)); o.append(t(36, 504, 'ASCENT', 16, up, 'bold')); o.append(t(36, 526, 'paid, or refused', 14, P['fg'], 'normal', MONO)); o.append(t(36, 548, '6 firing orders', 14, P['gold'], 'normal', MONO)); o.append(t(36, 568, 'AscentNotFree', 14, P['red'], 'bold', MONO)); o.append(t(36, 588, '[SCALE,ADD] = ADD', 12, P['mut'], 'normal', MONO))
    o.append(toolset_panel(P, 876, 16, 388, 608))
    return wrap(P, ''.join(o))

OPTS = {'option1_vertical_dark': flow_vertical(DARK), 'option2_horizontal_light': flow_horizontal(LIGHT), 'option3_radial_dark': flow_radial(DARK)}
for n, s in OPTS.items(): open(n + '.svg', 'w').write(s)
print({n: len(s) for n, s in OPTS.items()})
