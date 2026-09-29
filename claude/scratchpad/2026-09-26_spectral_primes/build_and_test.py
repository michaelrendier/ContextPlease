"""
Core computation for 'Spectral Representation of the Primes' — spin/wobble
decomposition of the theta-spiral construction (tonight's addendum), plus
the explicit-formula reconstruction of psi(x) as the concrete, checkable
demonstration that primes live in the wobble (oscillatory, zero-driven
minor loop), not the spin (smooth theta'(t) carrier, major loop).
"""
import mpmath as mp
mp.mp.dps = 30

N_ZEROS = 60

def get_zeros(n):
    return [mp.zetazero(k).imag for k in range(1, n+1)]

def spin_series(t_values):
    """Major loop: theta'(t), the smooth carrier rate. No prime content."""
    return [mp.diff(mp.siegeltheta, t) for t in t_values]

def wobble_series(t_values, theta_primes):
    """Minor loop: spacing - 2*pi/theta'(t) at each zero. This is where the
    fluctuation (and, per classical Weil/von Mangoldt, the primes) lives."""
    out = []
    for i in range(len(t_values)-1):
        spacing = t_values[i+1] - t_values[i]
        predicted = 2*mp.pi / theta_primes[i]
        out.append(spacing - predicted)
    return out

def psi_explicit_formula(x, zero_imag_parts):
    """Truncated von Mangoldt explicit formula:
    psi(x) = x - sum_rho x^rho/rho - ln(2pi) - (1/2)ln(1-x^-2)
    summed over rho = 1/2+i*gamma and its conjugate 1/2-i*gamma (real part
    doubled). This is the SAME zero set as spin_series/wobble_series above
    -- one smooth term (x, no zero info at all) plus one oscillatory term
    built entirely from the zeros.
    """
    x = mp.mpf(x)
    smooth = x - mp.log(2*mp.pi) - mp.mpf('0.5')*mp.log(1 - x**-2)
    osc = mp.mpf(0)
    for gamma in zero_imag_parts:
        rho = mp.mpc(mp.mpf('0.5'), gamma)
        osc += 2 * mp.re(x**rho / rho)
    return smooth - osc, smooth, osc

def true_psi(x):
    """Exact psi(x) = sum of ln(p) over prime powers p^k <= x."""
    x = float(x)
    total = 0.0
    n = 2
    while n <= x:
        m = n
        is_prime = True
        d = 2
        while d*d <= m:
            if m % d == 0:
                is_prime = False
                break
            d += 1
        if is_prime:
            k = 1
            while n**k <= x:
                import math
                total += math.log(n)
                k += 1
        n += 1
    return total

if __name__ == "__main__":
    zeros = get_zeros(N_ZEROS)
    print(f"Got {len(zeros)} zeros, first={float(zeros[0]):.6f}, last={float(zeros[-1]):.6f}")

    print("\n=== SPIN (major loop, theta'(t)) ===")
    thp = spin_series(zeros)
    print("theta'(t) range:", float(thp[0]), "->", float(thp[-1]))
    # check monotonic, no peaks
    diffs = [float(thp[i+1]-thp[i]) for i in range(len(thp)-1)]
    n_negative = sum(1 for d in diffs if d < 0)
    print(f"non-monotonic steps: {n_negative} / {len(diffs)}  (0 = perfectly monotonic = no resonance)")

    print("\n=== WOBBLE (minor loop, spacing deviation) ===")
    wob = wobble_series(zeros, thp)
    wob_f = [float(w) for w in wob]
    mean_w = sum(wob_f)/len(wob_f)
    var_w = sum((w-mean_w)**2 for w in wob_f)/len(wob_f)
    print(f"mean={mean_w:.4f}  stdev={var_w**0.5:.4f}  n={len(wob_f)}")

    print("\n=== EXPLICIT FORMULA: psi(x) reconstruction at/near primes ===")
    test_points = [2, 2.5, 3, 4, 5, 6, 7, 8, 10, 11, 12]
    for x in test_points:
        recon, smooth, osc = psi_explicit_formula(x, zeros)
        exact = true_psi(x)
        print(f"x={x:5}  psi_exact={exact:8.4f}  psi_recon(N={N_ZEROS})={float(recon):8.4f}  "
              f"diff={float(recon)-exact:+.4f}")

def tilt_residual_series(t_values, sigma=mp.mpf('0.7')):
    """The 'real-axis tilt' signal from ADDENDUM sec B: apply the same
    theta(t)-rotation off the critical line and take the imaginary residual
    (which is exactly zero on sigma=1/2, per that addendum)."""
    out = []
    for t in t_values:
        s = mp.mpc(sigma, t)
        rotated = mp.e**(1j*mp.siegeltheta(t)) * mp.zeta(s)
        out.append(mp.im(rotated))
    return out

if __name__ == "__main__":
    print("\n=== TILT vs WOBBLE — direct correlation check ===")
    tilt = tilt_residual_series(zeros)
    tilt_f = [float(x) for x in tilt]
    # align: wobble has len(zeros)-1 entries (spacing between consecutive zeros)
    # tilt has len(zeros) entries (one per zero) -- compare tilt[i] to wob[i]
    n = min(len(tilt_f), len(wob_f))
    a = tilt_f[:n]
    b = wob_f[:n]
    mean_a = sum(a)/n
    mean_b = sum(b)/n
    cov = sum((a[i]-mean_a)*(b[i]-mean_b) for i in range(n))/n
    var_a = sum((x-mean_a)**2 for x in a)/n
    var_b = sum((x-mean_b)**2 for x in b)/n
    corr = cov / (var_a**0.5 * var_b**0.5)
    print(f"n={n}  corr(tilt_residual, wobble_deviation) = {corr:+.4f}")
    print(f"tilt range: {min(a):.4f} .. {max(a):.4f}")
    print(f"wobble range: {min(b):.4f} .. {max(b):.4f}")

def crossing_shape_test(gamma_n, sigma_range):
    """At a fixed zero-height t=gamma_n, scan sigma near 1/2. The 'crossing'
    of the Real Tilt (the rotated trajectory's position) with the Axis
    (Re=Im=0) is tested: does |rotated value| have its minimum exactly at
    sigma=1/2, or does it drift?"""
    out = []
    for sigma in sigma_range:
        s = mp.mpc(sigma, gamma_n)
        rotated = mp.e**(1j*mp.siegeltheta(gamma_n)) * mp.zeta(s)
        out.append((float(sigma), float(mp.re(rotated)), float(mp.im(rotated)), float(abs(rotated))))
    return out

if __name__ == "__main__":
    print("\n=== CROSSING SHAPE — does the Real-Tilt/Axis crossing move in sigma? ===")
    gamma_1 = zeros[0]  # first zero, t=14.1347...
    sigma_scan = [mp.mpf('0.5') + mp.mpf(d)/1000 for d in range(-20, 21, 2)]
    results = crossing_shape_test(gamma_1, sigma_scan)
    print(f"{'sigma':>8} {'Re':>10} {'Im':>10} {'|value|':>10}")
    min_row = min(results, key=lambda r: r[3])
    for sigma, re, im, mag in results:
        marker = "  <-- MIN" if (sigma, re, im, mag) == min_row else ""
        print(f"{sigma:8.4f} {re:10.4f} {im:10.4f} {mag:10.6f}{marker}")

    print("\n=== Does the crossing MOVE across different zeros? (t marches, sigma stays pinned) ===")
    for gamma in zeros[:5]:
        sigma_fine = [mp.mpf('0.5') + mp.mpf(d)/2000 for d in range(-6, 7, 2)]
        res = crossing_shape_test(gamma, sigma_fine)
        min_row = min(res, key=lambda r: r[3])
        print(f"t=gamma={float(gamma):10.4f}  min |value| at sigma={min_row[0]:.4f}  |value|={min_row[3]:.2e}")
