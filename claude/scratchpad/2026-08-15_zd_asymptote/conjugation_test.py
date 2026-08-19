#!/usr/bin/env python3
"""
TESTING Operating-L_(I|O) §5.3 — the one item still marked
"conjecture, no script yet".

THE CONJECTURE, as written this morning:

    Phase 27.4 measured that at R = e the apex path factorises EXACTLY:

        z(phi) = 2R cos(A) e^(iB)      real envelope  x  pure phase

    and the claim was:   STEM = the real envelope
                         INFLECTION = the pure phase

    with the prediction that clean morphological factorisation is a
    sigma = 1/2 phenomenon -- off the critical line, stem and inflection
    stay entangled.

WHAT WOULD MAKE IT TRUE, OPERATIONALLY

If the stem is a MAGNITUDE and the inflection is a DIRECTION, then within one
verb family:

    P-A  the magnitudes |v| should cluster        (one stem, one envelope)
    P-B  the directions should SPREAD             (inflections are phase)
    P-C  across families the common DIRECTIONS should differ more than
         within a family -- otherwise "direction = inflection" is vacuous

Measured on the phonetic face (CMUdict), which Phase 27.2 established is the
only existing construction with real angular content (residual 0.402).

THIS IS A TEST, NOT A DEMONSTRATION. It can fail, and how it fails is the
result.
"""
import sys, math
sys.path.insert(0, '/home/rendier/Projects/ThePlace/VAPMIP')
sys.path.insert(0, '/home/rendier/Projects/ThePlace')
import numpy as np
from nltk.corpus import cmudict

CMU = cmudict.dict()

# ── a phoneme -> feature vector, in the spirit of phonetic_face.py ───────────
VOWELS = set('AA AE AH AO AW AY EH ER EY IH IY OW OY UH UW'.split())
VOICED = set('B D DH G JH L M N NG R V W Y Z ZH'.split())
STOPS  = set('B D G K P T'.split())
FRIC   = set('DH F HH S SH TH V Z ZH'.split())
NASAL  = set('M N NG'.split())
LIQUID = set('L R W Y'.split())


def phone_vec(ph):
    base = ''.join(c for c in ph if not c.isdigit())
    stress = int(ph[-1]) if ph[-1].isdigit() else 0
    return np.array([
        1.0 if base in VOWELS else 0.0,
        1.0 if base in VOICED else 0.0,
        1.0 if base in STOPS  else 0.0,
        1.0 if base in FRIC   else 0.0,
        1.0 if base in NASAL  else 0.0,
        1.0 if base in LIQUID else 0.0,
        stress / 2.0,
        1.0,
    ])


def word_vec(w):
    """16-D: mean phoneme features (8) then final-phoneme features (8).
    The second half is where an inflection lands -- English inflects at the end."""
    pr = CMU.get(w.lower())
    if not pr:
        return None
    ph = pr[0]
    mean = np.mean([phone_vec(p) for p in ph], axis=0)
    last = phone_vec(ph[-1])
    return np.concatenate([mean, last])


FAMILIES = {
    'walk':  ['walk', 'walks', 'walking', 'walked', 'walker'],
    'talk':  ['talk', 'talks', 'talking', 'talked', 'talker'],
    'jump':  ['jump', 'jumps', 'jumping', 'jumped', 'jumper'],
    'play':  ['play', 'plays', 'playing', 'played', 'player'],
    'teach': ['teach', 'teaches', 'teaching', 'taught', 'teacher'],
    'go':    ['go', 'goes', 'going', 'went'],
}


def stats(vs):
    V = np.array(vs)
    mags = np.linalg.norm(V, axis=1)
    U = V / mags[:, None]
    c = U.mean(0); c /= np.linalg.norm(c)
    cos = np.clip(U @ c, -1, 1)
    return mags, c, np.sqrt(np.maximum(0, 1 - cos**2))


print("=" * 76)
print("§5.3 TEST — is the stem a magnitude and the inflection a direction?")
print("=" * 76)
fam_vecs, fam_dirs = {}, {}
print(f"\n  {'family':>8} {'n':>3} {'mean |v|':>9} {'CV of |v|':>10} "
      f"{'mean ang.residual':>18}")
for stem, words in FAMILIES.items():
    vs = [word_vec(w) for w in words]
    vs = [v for v in vs if v is not None]
    if len(vs) < 3:
        continue
    mags, c, res = stats(vs)
    fam_vecs[stem] = vs; fam_dirs[stem] = c
    print(f"  {stem:>8} {len(vs):>3} {mags.mean():>9.4f} "
          f"{mags.std()/mags.mean():>10.4f} {res.mean():>18.4f}")

print("""
  CV = coefficient of variation of the magnitudes. P-A predicts SMALL (one
  stem = one envelope). The angular residual is the directional spread within
  the family -- P-B predicts it is NOT zero.
""")

allv = [v for vs in fam_vecs.values() for v in vs]
_, _, res_all = stats(allv)
within = np.mean([stats(vs)[2].mean() for vs in fam_vecs.values()])
D = np.array(list(fam_dirs.values()))
cross = []
for i in range(len(D)):
    for j in range(i + 1, len(D)):
        cross.append(math.degrees(math.acos(np.clip(D[i] @ D[j], -1, 1))))

print("=" * 76)
print("SCORING")
print("=" * 76)
cvs = [np.std(np.linalg.norm(np.array(v), axis=1)) / np.mean(np.linalg.norm(np.array(v), axis=1))
       for v in fam_vecs.values()]
print(f"  P-A  magnitudes cluster within a family")
print(f"         mean CV of |v| within families : {np.mean(cvs):.4f}")
print(f"  P-B  directions spread within a family")
print(f"         mean angular residual within   : {within:.4f}")
print(f"  P-C  families differ in direction MORE than members do")
print(f"         mean angle BETWEEN family stems: {np.mean(cross):.2f} deg")
print(f"         (within-family spread, as angle: "
      f"{math.degrees(math.asin(min(1, within))):.2f} deg)")
sep = math.degrees(math.asin(min(1, within)))
print(f"""
  P-C verdict: between-family separation {'EXCEEDS' if np.mean(cross) > sep else 'DOES NOT EXCEED'}
               within-family spread  ({np.mean(cross):.2f} vs {sep:.2f} deg)
""")
