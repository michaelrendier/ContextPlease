#!/usr/bin/env python3
"""
un_sieve_zeta.py — the recursive un-sieve, clocked by the ZETA FUNCTION
instead of the ordinal prime count.

Prior test (un_sieve.py): primes turned on in ordinal order 2,3,5,7,...
Here they are turned on in orders derived from zeta:

  ordinal       key = p                                   (control)
  zeta_weight   key = -(ln p)/sqrt(p)  descending         (sigma=1/2 von Mangoldt
                                                           amplitude; peaks at p=7,
                                                           near e^2 -- the Mingling)
  theta         key = theta(2 pi p^2)                     (Riemann-Siegel theta at
                                                           the height t_p = 2 pi p^2
                                                           where prime p enters the
                                                           RS main sum; monotone in p
                                                           => a second control)
  Zsign         key = ( sign Z(2 pi p^2), p )             (split the primes by the
                                                           SIGN of the Riemann-Siegel
                                                           Z-function at RS entry --
                                                           one SIGN bit, from zeta)
  spiral        key = ( theta(t_p) mod 2pi , sign Z )     (winding phase on the zeta
                                                           spiral + the Z-sign bit)

Then a TIME embedding: birth "time" tau(n) = gamma_{rank(gpf(n))} using the REAL
Riemann zeros gamma_k. Ordinal arrival times are 1,2,3,... (uniform); zeta
arrival times are the actual zero heights (GUE-spaced). Uniformly bin tau and
see whether the birth-time distribution / the C-vs-A residual picks up the
zero-spacing fingerprint.

RANK-INVARIANCE: for any *reordering* of the primes, the C and A histograms
are the same multiset of bin counts relabelled -> H(C), H(A), H(C)-H(A) are
exactly invariant. What moves is (a) the generation RANGE/span, (b) the
SHAPE/location of the C-A residual, and -- only for the time embedding, where
bin membership depends on real spacings -- (c) the entropy itself.
"""
from __future__ import annotations
import math
import time as _time


# ---------------------------------------------------------------- factor tables
def spf_gpf(N):
    spf = [0] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > N:
                break
            spf[i * p] = p
    gpf = [0] * (N + 1)
    for n in range(2, N + 1):
        m, g = n, 1
        while m > 1:
            p = spf[m]
            g = p
            while m % p == 0:
                m //= p
        gpf[n] = g
    return spf, gpf, primes


def entropy(hist):
    tot = sum(hist)
    if tot == 0:
        return 0.0
    h = 0.0
    for c in hist:
        if c:
            q = c / tot
            h -= q * math.log2(q)
    return h


# --------------------------------------------------- Riemann-Siegel theta (float)
_LN2PI = math.log(2 * math.pi)

def theta_rs(t):
    """Asymptotic Riemann-Siegel theta, good to ~1e-9 for t > 10.
    theta(t) = t/2 ln(t/2pi) - t/2 - pi/8 + 1/(48 t) + 7/(5760 t^3) + ..."""
    return (0.5 * t * (math.log(t) - _LN2PI) - 0.5 * t - math.pi / 8
            + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t ** 3))


# --------------------------------------------------------------- the four reads
def four_reads(N, spf, gpf, order):
    rank = {p: i for i, p in enumerate(order)}
    P = len(order)
    asc = lambda p: rank[p]
    desc = lambda p: P - 1 - rank[p]
    comps = [n for n in range(4, N + 1) if spf[n] != n]
    gens = {
        "A": [asc(spf[n]) for n in comps],
        "B": [desc(gpf[n]) for n in comps],
        "C": [asc(gpf[n]) for n in comps],
        "D": [desc(spf[n]) for n in comps],
    }
    hists, summ = {}, {}
    for k, g in gens.items():
        h = [0] * P
        for x in g:
            h[x] += 1
        hists[k] = h
        nz = [i for i, c in enumerate(h) if c]
        summ[k] = dict(gen_range=(nz[0], nz[-1]), span=nz[-1] - nz[0] + 1,
                       entropy=entropy(h), top_share=h[nz[0]] / len(comps))
    A, D = gens["A"], gens["D"]
    mirror = all(D[i] == P - 1 - A[i] for i in range(len(comps)))
    hA, hC = hists["A"], hists["C"]
    resid = [hC[g] - hA[g] for g in range(P)]
    absmass = sum(abs(v) for v in resid)
    big = sorted(range(P), key=lambda g: -abs(resid[g]))[:8]
    head = [(g, order[g], resid[g]) for g in sorted(big)]
    return dict(summ=summ, mirror=mirror,
                HC_minus_HA=entropy(hC) - entropy(hA),
                absmass=absmass, head=head)


def build_orders(primes, siegel_primes=None):
    """siegel_primes: subset of `primes` for which siegelz is evaluated
    (Zsign/spiral). None -> skip those two orders."""
    th = {p: theta_rs(2 * math.pi * p * p) for p in primes}
    orders = {
        "ordinal": list(primes),
        "zeta_weight": sorted(primes, key=lambda p: math.log(p) / math.sqrt(p),
                              reverse=True),
        "theta": sorted(primes, key=lambda p: th[p]),
    }
    if siegel_primes:
        from mpmath import mp, siegelz
        mp.dps = 15
        t0 = _time.time()
        zs = {}
        for p in siegel_primes:
            zs[p] = 1 if float(siegelz(2 * math.pi * p * p)) >= 0 else -1
        print(f"    [siegelz x {len(siegel_primes)}: {_time.time()-t0:.1f}s  "
              f"pos={sum(1 for v in zs.values() if v>0)} "
              f"neg={sum(1 for v in zs.values() if v<0)}]", flush=True)
        orders["Zsign"] = sorted(siegel_primes, key=lambda p: (zs[p], p))
        orders["spiral"] = sorted(siegel_primes,
                                  key=lambda p: (th[p] % (2 * math.pi), zs[p]))
    return orders


def run_rank(N, do_siegel):
    print(f"\n{'='*74}\nRANK-BASED  N = {N:,}\n{'='*74}", flush=True)
    spf, gpf, primes = spf_gpf(N)
    P = len(primes)
    comps_n = sum(1 for n in range(4, N + 1) if spf[n] != n)
    ext_b = max(p for p in primes if p * p <= N)
    birth_b = max(p for p in primes if 2 * p <= N)
    born_after = sum(1 for n in range(4, N + 1)
                     if spf[n] != n and gpf[n] > ext_b)
    print(f"primes {P:,}  composites {comps_n:,}  ext_boundary {ext_b}  "
          f"birth_boundary {birth_b}  born_after {born_after:,} "
          f"({born_after/comps_n*100:.1f}%)", flush=True)

    sp = primes if do_siegel else None
    orders = build_orders(primes, siegel_primes=sp)
    for k, v in orders.items():
        print(f"  {k:12s} head: {v[:10]}", flush=True)

    res = {}
    for name, order in orders.items():
        # Zsign/spiral only cover siegel_primes; for N where that == all primes,
        # fine. Here do_siegel is only set when siegel_primes == primes.
        r = four_reads(N, spf, gpf, order)
        res[name] = r
        s = r["summ"]
        print(f"\n--- order = {name} ---", flush=True)
        for k in "ABCD":
            q = s[k]
            print(f"  {k}: H={q['entropy']:.4f}b  range={q['gen_range']}  "
                  f"span={q['span']:<5d} top_share={q['top_share']*100:5.1f}%")
        print(f"  D==reverse(A): {r['mirror']}   H(C)-H(A)={r['HC_minus_HA']:+.4f}b"
              f"   resid|mass|={r['absmass']:,}")
        print("  residual head (gen, prime, hC-hA):")
        for g, p, v in r["head"]:
            print(f"      gen {g:>4}  prime {p:>6}  {v:+8d}")

    print(f"\n{'-'*74}\nINVARIANCE  (H(A), H(C), H(C)-H(A) identical across "
          f"rank orderings)\n{'-'*74}", flush=True)
    print(f"{'order':12s} {'H(A)':>10s} {'H(C)':>10s} {'H(C)-H(A)':>12s} "
          f"{'A span':>8s} {'C span':>8s} {'resid|mass|':>12s}")
    for name, r in res.items():
        print(f"{name:12s} {r['summ']['A']['entropy']:10.5f} "
              f"{r['summ']['C']['entropy']:10.5f} {r['HC_minus_HA']:+12.5f} "
              f"{r['summ']['A']['span']:8d} {r['summ']['C']['span']:8d} "
              f"{r['absmass']:12,d}")
    return res


def run_time_embed(N, nbins=160):
    print(f"\n{'='*74}\nTIME EMBEDDING (real Riemann zeros)  N = {N:,}\n{'='*74}",
          flush=True)
    from mpmath import mp, zetazero
    mp.dps = 15
    spf, gpf, primes = spf_gpf(N)
    P = len(primes)
    comps = [n for n in range(4, N + 1) if spf[n] != n]
    print(f"  fetching {P} Riemann zeros ...", flush=True)
    t0 = _time.time()
    gam = [float(zetazero(k + 1).imag) for k in range(P)]
    print(f"    {_time.time()-t0:.1f}s   gamma_1={gam[0]:.4f}  "
          f"gamma_{P}={gam[-1]:.2f}", flush=True)

    rank = {p: i for i, p in enumerate(primes)}
    gmax = gam[-1]

    def h_zero(times):
        h = [0] * nbins
        for t in times:
            h[min(nbins - 1, int(t / gmax * nbins))] += 1
        return h

    def h_uni(idxs):
        h = [0] * nbins
        for i in idxs:
            h[min(nbins - 1, int((i + 1) / P * nbins))] += 1
        return h

    bz = [gam[rank[gpf[n]]] for n in comps]
    dz = [gam[rank[spf[n]]] for n in comps]
    bi = [rank[gpf[n]] for n in comps]
    di = [rank[spf[n]] for n in comps]
    hCz, hAz = h_zero(bz), h_zero(dz)
    hCu, hAu = h_uni(bi), h_uni(di)

    print(f"\n  uniform-time bins: H(A)={entropy(hAu):.4f}  H(C)={entropy(hCu):.4f}"
          f"  H(C)-H(A)={entropy(hCu)-entropy(hAu):+.4f}")
    print(f"  zero-time    bins: H(A)={entropy(hAz):.4f}  H(C)={entropy(hCz):.4f}"
          f"  H(C)-H(A)={entropy(hCz)-entropy(hAz):+.4f}")
    print("  -> if the two H(C)-H(A) differ, the zero SPACING (not just order)"
          "\n     has entered the construction cost.", flush=True)

    res = [hCz[b] - hAz[b] for b in range(nbins)]
    m = sum(res) / nbins
    rc = [v - m for v in res]
    den = sum(v * v for v in rc)
    def acf(lag):
        return (sum(rc[b] * rc[b + lag] for b in range(nbins - lag)) / den
                if den else 0.0)
    print("\n  C-A residual autocorrelation (zero-time bins):")
    for lag in (1, 2, 3, 4, 5, 8, 12, 20):
        print(f"    lag {lag:3d}:  acf = {acf(lag):+.4f}")
    print(f"\n  mean zero spacing = {(gam[-1]-gam[0])/(P-1):.4f}  "
          f"(uniform-time spacing == 1 by construction)", flush=True)


if __name__ == "__main__":
    run_rank(100_000, do_siegel=False)      # ordinal / zeta_weight / theta
    run_rank(12_000, do_siegel=True)        # + Zsign / spiral (siegelz)
    run_time_embed(8_000, nbins=160)        # real zeros
