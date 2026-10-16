"""Q6 — why is sigma_self(sigma) non-monotone for inputs >= 20 chars? Hypothesis tested: the break happens at small sigma (weights i^-sigma stop decaying)."""
import sys, random, math
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP/paper")
import evidence as ev
ev._P = ev.primes_from_source()
rnd = random.Random(5)
words = ev._words()
grid = [i/20 for i in range(21)]
first_drop = []; mono_upper = 0; n = 0; nonmono = 0; mono_by_range = {"[0,.5]": 0, "[.5,1]": 0}
for _ in range(600):
    s = " ".join(rnd.choice(words) for _ in range(rnd.randint(4, 12)))
    if len(s) < 20: continue
    c = [ev.sigma_self(s.encode(), g) for g in grid]; n += 1
    drops = [i for i in range(20) if c[i+1] < c[i] - 1e-12]
    if drops: nonmono += 1; first_drop.append(grid[drops[0]])
    if all(c[i+1] >= c[i]-1e-12 for i in range(10, 20)): mono_by_range["[.5,1]"] += 1
    if all(c[i+1] >= c[i]-1e-12 for i in range(0, 10)): mono_by_range["[0,.5]"] += 1
print(f"inputs >=20 chars: {n}; non-monotone on [0,1]: {nonmono}")
print("monotone rising on [0,.5]:", mono_by_range["[0,.5]"], " on [.5,1]:", mono_by_range["[.5,1]"])
import collections
print("location of first drop (sigma):", dict(sorted(collections.Counter(first_drop).items())))
print("fraction of first drops at sigma < 0.5:", sum(1 for d in first_drop if d < 0.5)/len(first_drop))

# where is the minimum of sigma_self(sigma) for long inputs, and how does sigma_self(0) compare with the minimum?
import collections
rnd = random.Random(6); amin = collections.Counter(); ratio = []
for _ in range(300):
    s = " ".join(rnd.choice(words) for _ in range(rnd.randint(4, 12)))
    if len(s) < 20: continue
    c = [ev.sigma_self(s.encode(), g) for g in grid]; i = min(range(21), key=lambda j: c[j]); amin[grid[i]] += 1; ratio.append(c[0]/c[i])
print("argmin sigma of sigma_self for long inputs:", dict(sorted(amin.items())))
print("sigma_self(0) / min: median", sorted(ratio)[len(ratio)//2])
# pure-noise control: random bytes (no linguistic structure)
rb = random.Random(1); am2 = collections.Counter()
for _ in range(200):
    s = bytes(rb.randrange(97, 123) for _ in range(40)); c = [ev.sigma_self(s, g) for g in grid]; am2[grid[min(range(21), key=lambda j: c[j])]] += 1
print("control, random lowercase 40-byte strings, argmin sigma:", dict(sorted(am2.items())))
