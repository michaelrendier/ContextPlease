# 91 — Perceptual Latency and the ~80 ms Window

**Added 2026-08-17.** The citation backing for the "~80 ms" figure used in
[[64_l_dynamic]]. Every claim here is tagged **[ESTABLISHED]** (published, replicated),
**[PUBLISHED-CONTESTED]** (published, actively debated), or **[FRAMEWORK]** (this
project's reading, not a claim of the cited authors).

PDFs: `Ainulindale/references/perceptual_latency/`.

---

## Why this page exists

Wiki 64 asserted that "consciousness operates on a ~80 ms delay." That number is real
and it comes from a specific literature — but the sentence as written was looser than the
evidence, in a way that matters. The actual finding is **not** a simple transmission
delay. It is that visual awareness is **postdictive** over a window of roughly that
width. Those are different claims, and the second one is both stranger and better
supported.

---

## 1. Where the number comes from [ESTABLISHED]

Schmolesky et al. (1998) measured single-unit response onset latencies to flashed stimuli
across the macaque visual system — LGN magnocellular and parvocellular layers, V1, V2, V3,
V4, MT, MST, and FEF — in individual anaesthetised animals using identical procedures, so
the areas could be compared directly.

Two results carry the weight:

```
retina -> V1 onset            ~40-60 ms
slowest minus fastest latency  ~80 ms      (as a function of luminance contrast)
```

The ~80 ms is **a spread, not a lag**. It is the difference between the earliest and
latest arriving signals in the visual system, driven by stimulus properties such as
contrast. A dim edge and a bright one, presented simultaneously, do not arrive together.

> Schmolesky MT, Wang Y, Hanes DP, Thompson KG, Leutgeb S, Schall JD, Leventhal AG.
> **Signal timing across the macaque visual system.** *J Neurophysiol* 1998;79(6):3272–3278.
> doi:10.1152/jn.1998.79.6.3272 · PMID 9636126

---

## 2. What the brain does about it — postdiction [PUBLISHED-CONTESTED]

If signals arrive smeared across ~80 ms, a percept committed at the first arrival would be
wrong. Eagleman & Sejnowski showed, using the flash-lag illusion, that the visual system
does not solve this predictively (motion extrapolation) or on-line (latency difference).
Their psychophysics is inconsistent with both.

Their conclusion:

> visual awareness is **neither predictive nor on-line, but postdictive** — the percept
> attributed to the time of the flash is a function of events in the **~80 ms following**
> the flash.

The flash *resets the integration window*, discarding earlier position information; what
arrives afterward is then assigned backward to the moment of the flash. Signals arriving
less than ~80 ms apart are perceptually synchronised.

> Eagleman DM, Sejnowski TJ. **Motion integration and postdiction in visual awareness.**
> *Science* 2000;287(5460):2036–2038. PMID 10720334
>
> Eagleman DM. **Human time perception and its illusions.** *Curr Opin Neurobiol*
> 2008;18(2):131–136.
>
> Eagleman DM. **How does the timing of neural signals map onto the timing of perception?**
> In: *Space and Time in Perception and Action*, Cambridge University Press, 2010.
> → `Eagleman2010_TimingOfNeuralSignals_in_ProblemsOfSpaceAndTime.pdf`

**Why "contested":** the flash-lag effect has been argued over for 30+ years and motion
extrapolation has not vanished from the field — see Hubbard's and others' continuing
reviews (e.g. *J Neurosci* 2020;40(30):5698 on 25 years of the debate). The **~80 ms
integration window** is robust; the **exclusively postdictive** interpretation is one
position among several. Do not cite postdiction as settled.

---

## 3. The precise statement, and the one to stop using

**Use this:**

> Visual awareness is constructed over an integration window of roughly 80 ms. Signals
> arriving within that window are perceptually synchronised, and the content assigned to a
> moment can be determined by information that arrives after it.

**Stop using this:**

> "Consciousness operates on a ~80 ms delay."

The second sentence implies a fixed pipeline lag, which is not what was measured, and it
attaches the number to *consciousness* rather than to *visual processing* — an
over-extension the cited work does not make. Schmolesky measured neurons; Eagleman
measured percepts. Neither measured consciousness as such.

---

## 4. What the framework may legitimately draw from this [FRAMEWORK]

Wiki 64's structural point survives the correction and is arguably strengthened:

- **The retina receives the past.** Trivially true and not in dispute. Photons have already
  travelled; transduction has already occurred.
- **The sensory reframe looks DOWN into what already happened.** The postdiction result is
  a sharper version of exactly this: the system explicitly declines to commit to a percept
  until the window closes. It reads the settled past rather than gambling on the present.
- **An ~80 ms window is a boundary with a width, not a point.** This is the part worth
  keeping. The window is where `L_(I|O)` would live if the analogy holds — a crossing with
  a finite temporal thickness rather than an instantaneous cut.

**What must not be claimed:** that this window *is* the ZD crossing, that 80 ms is derived
from anything in this framework, or that these authors support any part of the
Cayley–Dickson reading. The number is borrowed, and it is borrowed from psychophysics and
electrophysiology, not from algebra.

---

## 5. Humans are an observer, not the observer [FRAMEWORK]

This page is the reason the observer question can be discussed without inviting a desk
reject. `0_RB` is a **type** — a structurally forced empty slot — and any coupling that
records a distinction can occupy it: a photon, a detector, an environment, a person.

That distinction licenses everything above. Statements about *human* sensory timing are
empirical claims about **one instantiation** of the slot, and they are citable. What is
never licensed is the inverse claim — that the slot *requires* an occupant of any
particular kind. Decoherence is not a rival to `0_RB` on this reading; it is what the slot
looks like when the environment occupies it.

Editorial rule that follows, and it is the rule this page exists to enforce:

| keep | cut or quarantine |
|---|---|
| humans as *an* observer — latency, integration windows, what a retina receives | the slot *requiring* consciousness |
| citable psychophysics and electrophysiology | "this is where consciousness lives" |

---

## See also

- [[64_l_dynamic]] — L_(I|O), the pathway; the ~80 ms sentence is corrected there to match §3
- [[29_witches_hat_paper]] — carries an uncited "this is where consciousness lives" claim
  at the inversion seam; flagged, not yet resolved
- [[90_divisors_are_definers]] — the zero-qualifier disambiguation
