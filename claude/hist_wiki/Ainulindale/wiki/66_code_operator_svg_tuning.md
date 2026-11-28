# 66 — The `<code>` Operator in SVG: the Tuning Layer

| | |
|---|---|
| Scope | a `<code>` block inside an SVG document as the operating-point record of the resonator engine; why a viewer ignores it; the NULL/zero reading |
| Origin | 2026-06-14, session SedenionSpectralRelativity / `sedenion_resonators` |
| Code | `SedenionSpectralRelativity/sedenion_resonators.py` (resonators), `ptol_layer.py` (SVG writer) |
| Confidence | the SVG behaviour: ESTABLISHED (Listing 1) · the engine reading its own `<code>` block: a design specification, not confirmed in code on this pass · the zero-divisor reading of `<code>`…`</code>`: `INTERPRETATION` |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. The mechanism

An SVG file can carry an element the renderer does not know. The page's proposal is a
`<code>` block holding the tuning parameters of the resonator:

```
<code>
  sigma: 0.5
  omega: 0.56657
  primes: [11, 13, 17, 19]
  mode: witches_hat
  turns: 16
</code>
```

A viewer ignores it, the engine reads it as the operating point, and the visible paths
are generated from it. In the two resonators the shared object is the sedenion Dirichlet
path, and what differs is the projection: `mode: witches_hat` gives a conical projection
(z = height); `mode: galactic` a polar projection (z ≈ 0). So the `<code>` layer is
the parameters of the projection, and changing it changes the resonator's shape.

**Listing 1 — a renderer ignores an unknown element and a parser keeps it** (written for this page; needs `rsvg-convert` and python3; runs cold)

```bash
cat > a.svg <<'X'
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120"><circle cx="60" cy="60" r="40" fill="teal"/></svg>
X
cat > b.svg <<'X'
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120"><code>sigma: 0.5
omega: 0.56657
primes: [11, 13, 17, 19]
mode: witches_hat</code><circle cx="60" cy="60" r="40" fill="teal"/></svg>
X
rsvg-convert a.svg -o a.png; rsvg-convert b.svg -o b.png
sha256sum a.png b.png | cut -c1-16
python3 -c "import xml.etree.ElementTree as ET; print([(e.tag.split('}')[1], (e.text or '').split(chr(10))[0]) for e in ET.parse('b.svg').getroot()])"
```

```
a9079149e5a13d6d  a.png
a9079149e5a13d6d  b.png
[('code', 'sigma: 0.5'), ('circle', '')]
```

The two renderings are byte-identical (same hash), and an XML parser sees the
`<code>` element with its text. So the claim "the viewer ignores it; the engine can read it"
is true of the format. The observer sees the shape, and the file also holds the
parameters that produced it (provided the writer put them there).

## 2. What the page claims beyond the format

**"The visual output is parameter-free."** The page says the geometry has zero free
parameters, determined entirely by the `<code>` content, and that the `<code>` layer starts
NULL. Both cannot be said of the same object: if the picture is determined by the
`<code>` block, the block is the parameter set. The NULL-versus-zero distinction the
page draws ([15](15_the_monad.md): NULL means vacant and every parameter open; zero
means a determined value) is a statement about the block: it starts NULL and is filled by
the first word. The picture then has no further freedom given the block.

**The prime lists.** The example sets `primes: [11, 13, 17, 19]` against the full
`[2, 3, …, 53]` for the Fano resonator and the sedenion resonator. The octonion's eight
channels e₀–e₇ carry the primes 2–19 in the engine's assignment, so a four-prime list is
an example and not the octonion channel set. The page's statement that the difference
between the two blocks is the zero-divisor wobble ([68](68_precession_wobble_signature.md))
is the author's reading of the 𝕆/𝕊 comparison.

## 3. The zero-divisor reading  `INTERPRETATION`

The page reads the tag pair `<code>`…`</code>` as a zero-divisor pair: the opening and
closing tags multiply to zero visual output and their product defines the parameter space
in which all visual content lies; the void between them is the vacuum state, and
parameters written into it break its symmetry, the broken symmetry being the resonator's
shape. As in [62](62_hands_on_paper_minds_eye_caustic.md) §6 and
[64](64_l_dynamic.md) §7, the tag pair is a notation for the two-direction picture: an
XML tag pair is not a pair of algebra elements, and no product is computed. The
reading stands as the framework's way of describing where the engine's NULL turns into a
defined value.

## 4. The invisible layer and the pipeline

```
input text → P1 prime hash → prime channel → <code>prime_channel</code>
                                                    ↓
                                          Dirichlet at that prime
                                                    ↓
                                          SVG path at σ = ½
                                                    ↓
                                          observer sees the shape, not the code
```

The sheet-music analogy: the `<code>` layer is the score and the SVG is the
performance. Listing 1 shows the consequence that makes this literal for the file
format: the rendering is identical with or without the layer, and the layer is
present in the file for any reader that parses it. Whether `ptol_layer.py` writes and
`ptol.c` reads such a block in the current code is a code-state question for the audit
of those files; the page records the specification (the tuning mechanism the speaking
architecture was missing).

## 5. Related pages

[15 the Monad](15_the_monad.md) · [62 the two caustics](62_hands_on_paper_minds_eye_caustic.md) ·
[65 primes as repellors](65_primes_repellors_drift_meaning.md) · [68 precession and the wobble](68_precession_wobble_signature.md)
