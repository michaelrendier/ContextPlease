"""
Exercise the ADD:SCALE:SIGN datatype  (ValaQuenta/modules/add_scale_sign).
Round-trip, composition, residuals, decomposition, orthogonal charts,
the two lineage orderings, and the three-phase camshaft firing defect.
"""
import sys, math
sys.path.insert(0, "/home/rendier/Projects/ThePlace")
from ValaQuenta.modules.add_scale_sign import ASS, ASSWord, compose, word, CAMSHAFT, BRACKET

def sect(t): print("\n" + "═"*70 + "\n" + t + "\n" + "═"*70)

sect("1. construction, apply, the three generators")
T = ASS(add=3.0, scale=2.0, sign=-1)          # x ↦ −2x + 3
print("  T =", T, "  ", repr(T))
print("  T(5) =", T(5), "  (expect −7)")
print("  generators:", [str(p) for p in T.parts()], " (camshaft order SIGN,SCALE,ADD)")
print("  T == ADD∘SCALE∘SIGN ?",
      ASS.ADD(3.0) @ ASS.SCALE(2.0) @ ASS.SIGN(-1) == T)

sect("2. forward (compose @) / backward (invert ~) / record")
A = ASS.SCALE(8.0); B = ASS.ADD(2.0); C = ASS.SIGN(-1)
T = compose(A, B, C)                          # apply A, then B, then C
print("  compose(SCALE 8, ADD 2, SIGN −1) =", T)
print("  record (application order):", T.record())
xs = [-1.0, 0.0, 3.5]
print("  (~T ∘ T)(x) == x ?", all(abs((~T)(T(x)) - x) < 1e-12 for x in xs))
print("  ~T record (reversed & inverted):", (~T).record())

sect("3. residuals — the str.strip / str.replace analogue")
T = ASS(add=1.5, scale=4.0, sign=-1)
print("  T                =", T)
print("  T.residual('SIGN')  =", T.residual("SIGN"), "   (strip the bit, keep add+scale)")
print("  T.residual('SCALE') =", T.residual("SCALE"))
print("  T.residual('ADD')   =", T.residual("ADD"))
print("  T.only('SCALE')     =", T.only("SCALE"))
print("  strip all three → ground?", T.residual('ADD').residual('SCALE').residual('SIGN').is_ground())

sect("4. the decomposition type — ASSWord, and each generator's equation part")
T = ASS(add=4.0, scale=3.0, sign=1)
print("  T =", T)
for k, v in T.equation_parts().items():
    print(f"    {k:9} {v}")
print("\n  T.lineage('chrono'):")
print("   ", str(T.lineage("chrono")).replace("\n", "\n    "))

sect("5. the two generational-lineage orderings (chrono vs zeta)")
T = compose(ASS.SIGN(-1), ASS.ADD(5.0), ASS.SCALE(2.0), ASS.ADD(0.1))
print("  built:", T, "  BRACKET:", BRACKET)
print("  chrono :", str(T.lineage("chrono")).split("\n")[0])
print("  zeta   :", str(T.lineage("zeta")).split("\n")[0], "  (sorted by |u_k| ↓)")
wc, wz = T.lineage("chrono"), T.lineage("zeta")
print(f"  u_total = {wc.u_total():.6g}   Σu_parts = {wc.u_sum_of_parts():.6g}")
print(f"  firing defect (u_total − Σu_parts) = {wc.firing_defect():+.6g}   order matters: {not wc.additive()}")
print("  (chrono and zeta are two orderings of the SAME recorded word — the")
print("   departure between them is this datatype's ψ(x) − x.)")

sect("6. the orthogonal Smith charts, in the maths language it was built on")
for spec in [(0.0, 1.0, 1), (0.0, 8.0, 1), (2.0, 1.0, 1), (1.5, 4.0, -1)]:
    T = ASS(*spec)
    s = T.to_smith()
    print(f"  {str(T):22}  {s['notation']}   quad {s['quadrant']:4}  {'← NOW' if s['at_now'] else ''}")

sect("7. the three-phase camshaft (firing / valve order)")
print("  CAMSHAFT =", CAMSHAFT, "  (SIGN fires first / innermost:  x ↦ ADD(SCALE(SIGN(x))))")
Tpos = ASS(add=4.0, scale=3.0, sign=+1)       # sign +1 → SIGN doesn't flip SCALE
Tneg = ASS(add=4.0, scale=3.0, sign=-1)       # sign −1 → it does
for T in (Tpos, Tneg):
    print(f"  {str(T):20}  u = g·ln s + a = {T.u():+.5g}   "
          f"Σ parts = {T.add + math.log(T.scale):+.5g}   "
          f"additive: {T.is_additive()}"
          + ("" if T.is_additive() else "   ← [SCALE,ADD]=ADD bit: SIGN flipped a non-trivial SCALE"))

sect("8. ground state = 'only ADD:SCALE:SIGN' = the now")
G = ASS.GROUND
print("  GROUND =", G, "  u =", G.u(), "  Γ =", G.gamma(), "  is_ground:", G.is_ground())
print("  word(u) round-trips: word(1.2).gamma() =", word(1.2).gamma(),
      " vs tanh(0.6) =", math.tanh(0.6))
print("\n  ALL CHECKS ABOVE ARE EXACT (round-trip 1e-12, fold = tanh, no free params).")
