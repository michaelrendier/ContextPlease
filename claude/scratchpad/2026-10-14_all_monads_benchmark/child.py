"""Benchmark ONE monad exactly as the console's `/monad use <name>` loads it (ptolemy_console.load_monad_by_name), headless.
Prints one line: BENCH_JSON:{...}"""
import sys, os, time, json, io, contextlib, importlib, traceback
name = sys.argv[1]
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP'); sys.path.insert(0, '/home/rendier/Projects/ThePlace/PtolemyDesktop')
PROMPTS = ["finger pointer", "what is a tree", "neutron generation in different reactor types",
           "good morning", "can you play the piano?", "the first reactor was built after neutrons were discovered"]
def rss():
    for l in open('/proc/self/status'):
        if l.startswith('VmRSS'): return int(l.split()[1]) / 1024
def emit(d):
    print('BENCH_JSON:' + json.dumps(d, default=str)); sys.stdout.flush()
out = {'name': name, 'rss_start_mb': round(rss(), 1)}
quiet = io.StringIO()
try:
    t = time.perf_counter()
    with contextlib.redirect_stdout(quiet), contextlib.redirect_stderr(quiet):
        import ptolemy_console as pc
    out['console_import_s'] = round(time.perf_counter() - t, 2); out['rss_console_mb'] = round(rss(), 1)
    class Dummy:
        kind = 'dummy'; enabled = True
        def say(self, t): return ("(fallback: next monad)", {})
        def status(self): return 'dummy'
    t = time.perf_counter()
    with contextlib.redirect_stdout(quiet), contextlib.redirect_stderr(quiet):
        m = pc.load_monad_by_name(name, Dummy())
    out['load_s'] = round(time.perf_counter() - t, 2); out['rss_loaded_mb'] = round(rss(), 1)
    out['adapter'] = type(m).__name__; out['kind'] = getattr(m, 'kind', '')
except BaseException as e:
    out['error'] = f'{type(e).__name__}: {str(e)[:300]}'; emit(out); sys.exit(0)
calls = []
cpu_w0 = cpu_w1 = wall_w0 = wall_w1 = None
for rnd in (1, 2):
    if rnd == 2: wall_w0 = time.time(); cpu_w0 = time.process_time()
    for p in PROMPTS:
        t = time.perf_counter()
        try:
            with contextlib.redirect_stdout(quiet), contextlib.redirect_stderr(quiet):
                r = m.say(p)
            reply = r[0] if isinstance(r, tuple) else r
            err = None
        except BaseException as e:
            reply, err = None, f'{type(e).__name__}: {str(e)[:200]}'
        calls.append({'round': rnd, 'prompt': p, 'ms': round((time.perf_counter() - t) * 1000, 1), 'reply': (str(reply)[:240] if reply is not None else None), 'error': err})
    if rnd == 2: wall_w1 = time.time(); cpu_w1 = time.process_time()
out['calls'] = calls; out['rss_end_mb'] = round(rss(), 1)
out['warm_t0'] = wall_w0; out['warm_t1'] = wall_w1; out['warm_cpu_s'] = round(cpu_w1 - cpu_w0, 3)
emit(out)
