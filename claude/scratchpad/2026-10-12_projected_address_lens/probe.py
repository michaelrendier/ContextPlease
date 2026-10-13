#!/usr/bin/env python3
"""Read ptol.c's projected prompt address through the box_kite chart_of lens.
usage: python3 probe.py "prompt" ...   (needs VAPMIP/PtolC/ptol built)"""
import sys, subprocess
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
from ValaQuenta.modules.box_kite import maths as bk
PTOL = '/home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptol'
for p in sys.argv[1:]:
    out = subprocess.run([PTOL, '-r', p], capture_output=True, text=True).stdout.split()
    v = [float(x) for x in out[:16]]
    r = bk.chart_of(v, check_zd=True)
    ce = r['chart_energy']; tot = sum(ce.values())
    print("%-28s ZD=%s outside=%.3f dom_chart=%d share=%.2f curv=%.1f shares=%s" % (
        p, r['is_zero_divisor'], r['outside_share'], r['dominant_chart'],
        r['chart_share'], r['local_curvature'], [round(ce[s]/tot, 2) for s in range(1, 8)]))
