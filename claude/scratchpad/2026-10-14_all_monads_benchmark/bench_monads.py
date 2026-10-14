"""Benchmark every monad that the console's `discover_monads()` lists (VAPMIP/*monad*.py), one subprocess each, with whole-laptop power sampled from the battery."""
import glob, json, os, subprocess, sys, threading, time, statistics as st
HERE = os.path.dirname(os.path.abspath(__file__)); VP = '/home/rendier/Projects/ThePlace/VAPMIP'
PY = '/home/rendier/Projects/ThePlace/PtolemyDesktop/.venv/bin/python'
B = '/sys/class/power_supply/BAT0/'
EXTRA = [('VQ_rotary_monad','ValaQuenta','speak','str'),('ZD_rotary_monad','AhuraMazda','speak','str'),('rotary_monad','AhuraMazda','speak','str'),('ptolemy_monad','PtolemyMonad','process_input','resp'),('boxkite_orbweaver_monad','OrbWeaverMonad','weave','doc'),('monad_english_io','MonadEnglish','basin','pool')]
names = sorted(os.path.splitext(os.path.basename(h))[0] for h in glob.glob(VP + '/*monad*.py') if not os.path.basename(h).startswith('_'))

results = []
jobs = [([PY, os.path.join(HERE, 'child.py'), n], n) for n in names] if len(sys.argv) <= 1 or sys.argv[1] != 'extra' else [([PY, os.path.join(HERE, 'child2.py')] + list(e[:4]), f'{e[0]}.{e[1]}.{e[2]}') for e in EXTRA]
OUT = 'results_extra.json' if len(sys.argv) > 1 and sys.argv[1] == 'extra' else 'results.json'
def sampler(stop, buf):
    while not stop.is_set():
        try: buf.append((time.time(), int(open(B + 'power_now').read()) / 1e6))
        except Exception: pass
        time.sleep(0.5)
for cmd, n in jobs:
    buf = []; stop = threading.Event(); th = threading.Thread(target=sampler, args=(stop, buf)); th.start()
    t0 = time.time(); status = open(B + 'status').read().strip()
    try:
        p = subprocess.run(cmd, cwd=VP, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300)
        line = [l for l in p.stdout.splitlines() if l.startswith('BENCH_JSON:')]
        r = json.loads(line[-1][11:]) if line else {'name': n, 'error': f'no result (exit {p.returncode}) ' + (p.stderr or '')[-300:]}
    except subprocess.TimeoutExpired:
        r = {'name': n, 'error': 'timeout 300 s'}
    stop.set(); th.join()
    r['wall_s'] = round(time.time() - t0, 1); r['battery_status'] = status
    if r.get('warm_t0') and buf:
        w = [x[1] for x in buf if r['warm_t0'] <= x[0] <= r['warm_t1']]
        calls = [c for c in r.get('calls', []) if c['round'] == 2 and not c['error']]
        if w and calls:
            r['warm_mean_W'] = round(st.mean(w), 2)
            tot = sum(c['ms'] for c in calls) / 1000; r['warm_ms_mean'] = round(tot / len(calls) * 1000, 1)
            r['whole_system_uWh_per_reply'] = round(r['warm_mean_W'] * (tot / len(calls)) / 3600 * 1e6, 1)
    results.append(r); print(n, '->', r.get('error') or f"load {r.get('load_s')}s warm {r.get('warm_ms_mean')} ms", flush=True)
    json.dump(results, open(os.path.join(HERE, OUT), 'w'), indent=1, default=str)
