# Monad energy per reply, from battery discharge (2026-10-13, AC unplugged)
`energy.py 5000`: 40 s idle, 5000 replies through `ptolemy -r -n` (stdin loop of 4 prompts: "what is a tree", "examine the reactor", "go north", "ask about primes"), 40 s idle. Samples of BAT0 power_now every 0.5 s.
Result: idle mean 8.96 W (sd 1.40; first idle 7.57 W, second 10.35 W: the baseline drifted by 2.8 W); load mean 9.255 W over 139 samples; 5000 replies in 129.3 s = 25.9 ms/reply.
Delta over mean idle 0.296 W (= 2.1 uWh per reply) is SMALLER THAN THE BASELINE DRIFT: the monad's incremental power is below this method's resolution. Do not quote 2.1 uWh as a measurement.
Defensible numbers: whole laptop (display, radios, OS, everything) during the run averaged 9.255 W, so whole-system energy per reply = 9.255 W x 25.9 ms = 0.240 J = 66.6 uWh (0.0666 mWh). Upper bound on the monad's own share, using the lower idle baseline (7.57 W): 1.68 W x 25.9 ms = 12 uWh per reply.
Against a public typical-query figure of ~0.3 Wh: whole-system 66.6 uWh is about 4,500 times lower; the incremental share is unresolved (smaller).
Battery readings: energy_now 24.140 Wh at start, 23.810 after the load phase, 23.550 at the end.
