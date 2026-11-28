# 91 — Perceptual Latency and the ~80 ms Window

| | |
|---|---|
| Scope | the citation backing for the "~80 ms" figure used in [64](64_l_dynamic.md); what the measurements say; the precise sentence to use and the one to stop using; what the framework may and may not draw from it |
| Added | 2026-08-17 |
| Files | `Ainulindale/references/perceptual_latency/Eagleman2010_TimingOfNeuralSignals_in_ProblemsOfSpaceAndTime.pdf` (the only PDF on disk) |
| Tags | every claim below is tagged **[ESTABLISHED]** (published, replicated), **[PUBLISHED-CONTESTED]** (published, actively debated) or **[FRAMEWORK]** (this project's reading, not a claim of the cited authors) |
| Verification | 2026-11-13: the Eagleman 2010 PDF's title page and summary were read (chapter 14, *How does the timing of neural signals map onto the timing of perception?*, D. M. Eagleman; its summary states that ~80 ms is an important duration in perception, mirrored in the physiology as the 80 ms difference between the slowest and fastest latencies in recordings from several primate visual areas). The journal citations of §§1–2 are quoted from the 2026-08-17 page and were **not re-fetched** (no PDF on disk) |

## 0. Why this page exists

[64](64_l_dynamic.md) asserted that "consciousness operates on a ~80 ms delay". The number is real and comes from a specific literature, but the sentence was looser than the evidence. The finding is not a simple transmission delay: it is that visual awareness is **postdictive** over a window of roughly that width. Those are different claims, and the second is
both stranger and better supported.

## 1. Where the number comes from  [ESTABLISHED]

Schmolesky et al. (1998) measured single-unit response-onset latencies to flashed stimuli across the macaque visual system (LGN magnocellular and parvocellular layers; V1, V2, V3, V4; MT, MST; FEF) in individual anaesthetised animals with identical procedures, so that areas could be compared directly. Two results carry the weight:

```
retina → V1 onset               ~40–60 ms
slowest minus fastest latency   ~80 ms    (as a function of luminance contrast)
```

The ~80 ms is **a spread, not a lag**: the difference between the earliest and latest arriving signals, driven by stimulus properties such as contrast. A dim edge and a bright one presented together do not arrive together. The Eagleman chapter on disk states the same
figure for the same recordings (see Verification above).

> Schmolesky MT, Wang Y, Hanes DP, Thompson KG, Leutgeb S, Schall JD, Leventhal AG. **Signal timing across the macaque visual system.** *J Neurophysiol* 1998;79(6):3272–3278. doi:10.1152/jn.1998.79.6.3272 · PMID 9636126 (as recorded; not re-fetched)

## 2. What the brain does about it: postdiction  [PUBLISHED-CONTESTED]

If signals arrive smeared across ~80 ms, a percept committed at the first arrival would be wrong. Eagleman and Sejnowski used the flash-lag illusion to show that the visual system does not solve this predictively (motion extrapolation) or on-line (latency difference); their psychophysics is inconsistent with both. Their conclusion: visual awareness is **neither predictive nor on-line but postdictive**: the
percept attributed to the time of a flash is a function of events in the ~80 ms following it. The flash resets the integration window and discards earlier position information; what arrives afterwards is assigned backward to the moment of the flash; signals arriving less than ~80 ms apart are perceptually synchronised.

> Eagleman DM, Sejnowski TJ. **Motion integration and postdiction in visual awareness.** *Science* 2000;287(5460):2036–2038. PMID 10720334 · Eagleman DM. **Human time perception and its illusions.** *Curr Opin Neurobiol* 2008;18(2):131–136. · Eagleman DM. **How does the timing of neural signals map onto the timing of perception?** In: *Space and Time in Perception and Action*, Cambridge University Press, 2010 (PDF on disk). (As recorded; only the last was opened.)

**Why contested:** the flash-lag effect has been argued over for 30+ years and motion extrapolation has not vanished from the field; the earlier page cites continuing reviews of the debate (a *J Neurosci* 2020 volume 40, issue 30 reference, not re-checked). The ~80 ms integration window is robust; the **exclusively postdictive** interpretation is one position among several. Do not cite postdiction as settled.

## 3. The precise statement, and the one to stop using

**Use this:** visual awareness is constructed over an integration window of roughly 80 ms. Signals arriving within that window are perceptually synchronised, and the content assigned to a moment can be determined by information that arrives after it.

**Stop using this:** "Consciousness operates on a ~80 ms delay." The second sentence implies a fixed pipeline lag, which is not what was measured, and attaches the number to *consciousness* rather than to *visual processing*, an over-extension the cited work does not make. Schmolesky measured neurons; Eagleman measured percepts; neither measured consciousness as such. (This is the wording now in [64](64_l_dynamic.md) §4.)

## 4. What the framework may legitimately draw  [FRAMEWORK]

[64](64_l_dynamic.md)'s structural point survives and is arguably strengthened:

- **The retina receives the past.** Trivially true: photons have already travelled and transduction has occurred.
- **The sensory reframe looks down into what already happened.** Postdiction is a sharper version: the system declines to commit to a percept until the window closes and reads the settled past rather than gambling on the present.
- **An ~80 ms window is a boundary with a width, not a point.** This is the part worth keeping: it is where L_(I|O) would live if the analogy holds, a crossing with finite temporal thickness rather than an instantaneous cut.

**Not to be claimed:** that this window *is* the zero-divisor crossing; that 80 ms is derived from anything in this framework; that these authors support any part of the Cayley–Dickson reading. The number is borrowed from psychophysics and electrophysiology, not from algebra.

## 5. Humans are an observer, not the observer  [FRAMEWORK]

0_RB is a **type**: a structurally forced empty slot that any coupling recording a distinction can occupy (a photon, a detector, an environment, a person). So statements about human sensory timing are empirical claims about one instantiation of the slot and are citable; what is never licensed is the inverse claim that the slot *requires* an occupant of a particular kind. Decoherence is not a rival to 0_RB on
this reading: it is what the slot looks like when the environment occupies it. Editorial rule:

| keep | cut or quarantine |
|---|---|
| humans as *an* observer: latency, integration windows, what a retina receives | the slot *requiring* consciousness |
| citable psychophysics and electrophysiology | "this is where consciousness lives" |

## 6. Related pages

[64 L_(I|O)](64_l_dynamic.md) · [29 the Witches Hat paper](29_witches_hat_paper.md) (carries an uncited "this is where consciousness lives" claim at the inversion seam; flagged, unresolved) · [90 divisors are definers](90_divisors_are_definers.md)
