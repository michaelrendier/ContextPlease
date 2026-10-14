"""Benchmark a monad whose speaking entry point is NOT what the console's loader looks for (it wants say()/generate()).
usage: child2.py module Class method kind   (kind: str | resp | doc | pool)"""
import sys, time, json, io, contextlib, importlib
mod, cls, meth, kind = sys.argv[1:5]; name = f'{mod}.{cls}.{meth}'
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP')
PROMPTS = ["finger pointer", "what is a tree", "neutron generation in different reactor types",
           "good morning", "can you play the piano?", "the first reactor was built after neutrons were discovered"]
def rss():
    for l in open('/proc/self/status'):
        if l.startswith('VmRSS'): return int(l.split()[1]) / 1024
def emit(d): print('BENCH_JSON:' + json.dumps(d, default=str)); sys.stdout.flush()
out = {'name': name, 'rss_start_mb': round(rss(), 1), 'adapter': kind}; q = io.StringIO()
try:
    t = time.perf_counter()
    with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
        m = importlib.import_module(mod)
        if kind == 'pool':
            obj = m.read(); out['rss_console_mb'] = out['rss_start_mb']
        else:
            obj = getattr(m, cls)(); out['rss_console_mb'] = out['rss_start_mb']
    out['load_s'] = round(time.perf_counter() - t, 2); out['rss_loaded_mb'] = round(rss(), 1)
except BaseException as e:
    out['error'] = f'{type(e).__name__}: {str(e)[:300]}'; emit(out); sys.exit(0)
def speak(p):
    if kind == 'str': return getattr(obj, meth)(p)
    if kind == 'resp': return getattr(obj, meth)(p).text
    if kind == 'doc': return getattr(obj, meth)(p).render()
    if kind == 'pool':
        toks = [w for w in p.lower().replace('?', '').split() if len(w) > 2]
        pool = obj.basin(toks, k=12)
        return 'pool: ' + ', '.join(pool)
calls = []
for rnd in (1, 2):
    if rnd == 2: w0 = time.time(); c0 = time.process_time()
    for p in PROMPTS:
        t = time.perf_counter()
        try:
            with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
                r = speak(p)
            err = None
        except BaseException as e:
            r, err = None, f'{type(e).__name__}: {str(e)[:200]}'
        calls.append({'round': rnd, 'prompt': p, 'ms': round((time.perf_counter() - t) * 1000, 1), 'reply': (str(r)[:300] if r is not None else None), 'error': err})
    if rnd == 2: w1 = time.time(); c1 = time.process_time()
out.update(calls=calls, rss_end_mb=round(rss(), 1), warm_t0=w0, warm_t1=w1, warm_cpu_s=round(c1 - c0, 3)); emit(out)
