#!/usr/bin/env python3
"""Smoke: language-blind monad load + governor + a real browse, harnessed and bare."""
import json
import os
import sys

sys.path.insert(0, os.path.expanduser('~/Projects/ThePlace/VAPMIP'))

import harness
import monad_bus


def line(t): print(f"\n{'=' * 70}\n{t}\n{'=' * 70}")


line("harness.load_monad('auto') — the report")
h = harness.Harness()
rpt = h.load_monad('auto')
print(json.dumps(rpt, indent=2))
print("backend.alive:", h.backend.alive())
print("backend.learn('the quick brown fox jumps over the lazy dog') ->",
      h.backend.learn("the quick brown fox jumps over the lazy dog", 0.7, 0.5))

line("harness.load_monad('c') and ('python') — explicit, must report either way")
for pref in ('c', 'python'):
    r = harness.Harness().load_monad(pref)
    print(f"  prefer={pref:7s} -> chosen={r['chosen']}  alive={r['alive']}  ({r['why']})")

line("ResourceGovernor — the ceiling and live state")
g = h.governor
print(json.dumps(g.snapshot(), indent=2, default=str))
print("headroom_ok(1 MB):", g.headroom_ok(1 << 20))
print("headroom_ok(10 x CEILING):", g.headroom_ok(g.CEILING * 10))

line("governor.guard — admission + slot accounting")
from monad_bus import Job
with g.guard(Job('probe-A', ram_peak=1 << 20)):
    print("inside guard A:", g.snapshot()['running'], "running")
    with g.guard(Job('probe-B', ram_peak=1 << 20)):
        print("inside guard B:", g.snapshot()['running'], "running",
              "| jobs:", g.snapshot()['jobs'])
print("after guards:", g.snapshot()['running'], "running (gc'd)")

line("harness.browse('http://example.com/') — real fetch, dedup on repeat")
r1 = h.browse('http://example.com/')
print("first :", r1)
r2 = h.browse('http://example.com/')
print("repeat:", r2, "  <- deduped" if r2.data == 'deduped' else "")

line("harness.search('sedenion box kite') — routes through browse")
rs = h.search('sedenion box kite')
print(rs)

line("bare RotaryBoxKiteMonad.browse_observe — no harness, learns into own field")
try:
    from rotary_rerun_boxkite_monad import RotaryBoxKiteMonad
    m = RotaryBoxKiteMonad()               # no harness attached = bare
    print("store loaded:", m.store is not None,
          "| kite:", m.box_kite is not None)
    print("bare browse_observe:", m.browse_observe('http://example.com/'))
    m2 = RotaryBoxKiteMonad(harness=h)      # attached = delegates
    print("attached browse_observe delegates:",
          type(m2.browse_observe('http://example.com/')).__name__)
except Exception as e:
    print("bare monad path skipped:", repr(e))

line("DONE")
