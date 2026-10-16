"""Q7 — does ptol.c's 16-number question go straight into the scaled boxkite kernel, and do the two compute the same sigma_self?
Feed ptol's normalised vector (ptol -r) to MindEyeBoxKiteKernel.eye.continuous_snapshot and compare sigma_self; also the hub facts."""
import sys, os, subprocess, io, contextlib, math
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP"); sys.path.insert(0, "/home/rendier/Projects/ThePlace/PtolemyDesktop"); sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP/paper")
import evidence as ev
q = io.StringIO()
with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
    import scaled_mind_eye_boxkite_kernel_monad as sme
    k = sme.MindEyeBoxKiteKernel()
hub = k.hub_report()
print("hub: e0_is_outside =", hub["e0_is_outside"]["e0_is_outside_the_geometry"], "| gluing reading:", str(hub["fixed_point_gluing"]["reading"])[:160], "| hub weight", hub["hub_fixed_point_weight"])
print("struts:", list(k.kite.struts), " assessors in strut 1:", k.kite.kite(1)[:2])
ev._P = ev.primes_from_source()
print(f"\n{'prompt':45s} {'ptol sigma_self':>16s} {'kernel sigma_self':>18s} {'|diff|':>9s}  is_ZD  windspeed  fixed_point_weight")
for p in ev.PROMPTS:
    v = ev.vector(p.encode(), 0.5)
    with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
        snap = k.eye.continuous_snapshot(v)
    sp = ev.p_red(v)
    fpw = sme.bk.fixed_point_weight(v)
    print(f"{p[:45]:45s} {sp:16.10f} {snap['sigma_self']:18.10f} {abs(sp-snap['sigma_self']):9.1e}  {snap['is_zero_divisor']!s:5s} {snap['a_matrix_basin_windspeed']:+.5f}  {fpw:.5f}")
print("\nptol.c vector component 0 (e0 weight) squared = fixed_point_weight check:", [round(ev.vector(p.encode(),0.5)[0]**2,5) for p in ev.PROMPTS])
