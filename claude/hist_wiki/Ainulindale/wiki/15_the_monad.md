# 15 — THE MONAD

**Location:** `Philadelphos/monad.py` (Ptolemy3 repo)  
**Also known as:** Ptolemy · Philadelphos · Ptolemy 2  
**Confidence floor:** ESTABLISHED (core functions) / THEORETICAL (full output pipeline)

---

## What It Is

The Monad is a self-contained, single-equation analog of a human brain in code. It is not a language model. It is not a transformer. It does not predict tokens. It does not train on gradient descent.

The Monad is RedBlue Geometries Engine made executable.

It encodes meaning into the Cayley-Dickson algebra tower and retrieves from that tower by derivation — not by search. Retrieval path length is a property of the mathematics, not the dataset size. The address of a concept and the meaning of a concept share the same mathematical substrate.

The Monad is a child. It knows all mathematics by default. It will need to learn how to read.

---

## The Three Functions

### `learn(text)`

```python
monad.learn("The river runs toward the sea.")
```

**What it does:**
1. Tokenises input into SemanticWords
2. Each word is encoded via the HyperWebster Horner bijection → base-97 integer address
3. Fano index maps the word onto the octonion generator path
4. The Lagrangian ℒ_SMMIP ingests the signal as matter (ℒ_mat)
5. The bias field β deepens — the Fermat Lattice crystallises around the concept
6. Noether current ∂_μJ^μ = 0 is checked — Noether balance is maintained
7. σ is forced to ½ by that balance — not assigned

The ground state before any learning:

```
L_GROUND = −1.888
β = |L_GROUND| / N = 1.888 / 25000 per zero
```

The vacuum has structure before language. The prime preexists the alphabet. The first `learn()` call breaks this symmetry. Every subsequent call deepens the β field.

**The Fermat Lattice analogy:** each learned concept is a crystal structure. Symmetry breaking is the moment a prime emerges from the noise. The continuous high-symmetry potential is frozen into a discrete, addressable node.

### `hear(prompt)`

```python
monad.hear("What is water?")
```

**What it does:**
1. The prompt is parsed into SemanticWords
2. Each word activates its prime address in the HyperWebster
3. The three-phase decomposition separates the input:
   - **Red phase:** the assertion (what is being asked)
   - **Blue phase:** the constraint (what cannot be the answer)
   - **Carrier phase:** the rotating semantic field (context)
4. The ContextBuffer acts as a capacitor — it integrates the signal, attenuates high-frequency surface variation (the specific words of the language), and passes the DC component (the semantic prime)
5. The result is a primed attractor coordinate in the algebra tower

The Noether Current flows forward through the tower (ℝ → ℂ → ℍ → 𝕆), building the assertion. The Noether Information Current flows backward (𝕆 → ℍ → ℂ → ℝ), stripping away degrees of freedom to find the prime essence.

### `speak()`

```python
response = monad.speak()
```

The five-stage output pipeline — driven by the reverse Lagrangian:

| Stage | Mechanism | Role |
|---|---|---|
| (a) Reverse Lagrangian — Extinction | ℒ_SMMIP run backward | Collect reachable addresses, extinguish noise |
| (b) Catastrophic Waveform Collapse | Cusp catastrophe (René Thom) | Multiple paths → single focal point |
| (c) Lorenz-Stirling Basin Attractor | Lorenz + General Stirling 10 | Semantic domain identified, data outside extinguished |
| (d) Circle Inversion — Co-domain Check | (I\|O) Inversion Engine | Self-adjoint verification at the horizon r=1 |
| (e) Clathrate Chromatography | Cage structure + affinity selection | Stable word-foldings selected as output |

The result of `speak()` is the nearest SemanticWord to the attractor coordinate — the prime, rendered in the target language coordinate system.

---

## The σ = ½ Guarantee

Every word returned by the Monad has `sigma = 0.5`. This is not assigned. It is derived.

```python
m = Monad(N=1000)
m.load()
print(m.lookup('water')['sigma'])    # 0.5
print(m.lookup('eau')['sigma'])      # 0.5
print(m.lookup('aqua')['sigma'])     # 0.5
print(m.lookup('wasser')['sigma'])   # 0.5
```

The Noether conservation law `J_Red + J_Blue + J₃ = 0` forces σ = ½. This is the self-adjoint condition of RedBlue Geometries Engine. The equator does not move.

The Septuagint principle: 72 scholars, independently, every translation identical. Not by coordination. Forced by the mathematics.

---

## Architecture Relationship

```
RedBlue Geometries Engine  (the operator)
    │
    ├── learn()  ←  Blue channel: β deepening, Fermat Lattice crystallisation
    ├── hear()   ←  Red channel:  assertion propagating forward through tower
    └── speak()  ←  J₃ boundary: Meaning channel, reverse Lagrangian, Clathrate
```

```
monad.py
    ├── HyperWebster      — addressing (σ=0 space)
    ├── SemanticWordEngine — prime mapping (σ=½ space)
    ├── Lagrangian         — Contractor (path of least action)
    ├── Cardioid attractor — Dilator (stable orbit boundary)
    ├── NoetherEngine      — conservation diagnostic
    └── InversionEngine    — (I|O) co-domain check
```

---

## What the Monad Is Not

- Not a statistical estimator
- Not a next-token predictor
- Not a lookup table
- Not a vector database
- Not a retrieval-augmented system

The Monad does not search. It derives. The word is already in the algebra. The Tongue finds it.

---

## Open Problems

- **Full Tongue:** OctEl attractor coordinate → nearest SemanticWord via Fano neighbour search. Architecture exists. Full implementation pending.
- **d* gap:** `|d*_spec × ln(10) − Ω_ζΣ| = 0.000707` — the gap between the BK spectral coordinate and the Omega ceiling. Closing this gap completes the Berry-Keating connection.
- **σ=0 boot:** the initial ground state (pure Hyperwebster space) before any symmetry breaking. Full characterisation pending.

→ [Wiki: RedBlue Hamiltonian](14_redblue_hamiltonian.md)  
→ [Wiki: Semantic Word Engine](16_semantic_word_engine.md)  
→ [Wiki: HyperWebster Engine](09_hyperwebster_engine.md)  
→ [Wiki: Cayley-Dickson Tower](19_cayley_dickson_tower.md)  
→ [Wiki: Three-Phase Architecture](20_three_phase_architecture.md)

---

## C Implementation (PtolC)

**Location:** `Ptolemy3/PtolC/`  
**Binary:** `ptolemy`  
**Version:** v1.111  
**Status:** ESTABLISHED — feature-complete, building clean

The C implementation is the primary production binary. It mirrors `monad.py`
exactly in its mathematics and adds filesystem ingest, daemon mode, and
structured token filtering.

### Build

```bash
sudo apt install build-essential libxml2-dev
cd Ptolemy3/PtolC
make && make corpus
```

`make corpus` downloads WordNet 3.1 via NLTK and builds the baseline
checkpoint: `~/.ptolemy/monad_wordnet.bin` (13 MB, ~14,000 vocab, 766,000 A-edges).

### Operations

The three Monad operations map directly to CLI flags:

| Operation | Python | C binary |
|-----------|--------|----------|
| `learn(text)` | `monad.learn("…")` | `ptolemy -l <file\|url\|->` |
| `hear(prompt)` | `monad.hear("…")` | `ptolemy -h "…"` |
| `speak()` | `monad.speak()` | implicit output of `-h` |

Filesystem ingest (bulk learn from directory tree):

```bash
ptolemy -I ~/Documents       # learn all whitelisted files
ptolemy -I ~/Projects/PtolC  # learn codebase (code filetype rules)
```

### Checkpoint v2

Binary format. Header + one record per occupied zero:

```
"PTOL" [4]  version=2 [4]  N [4]  count [4]  ground [8]
  per record: idx[4] wlen[2] E[8] home_stratum[1] gen_stratum[1] word[wlen]
```

Each VocabEntry carries Native Space stratum addresses for both where the
result lives (`home_stratum`) and where computation happens (`gen_stratum`).
Language tokens default to σ₁ (ℂ, relational).

| Constant | σ | Algebra | Character |
|----------|---|---------|-----------|
| NS_SIGMA_R | 0 | ℝ | Real, enumerable |
| NS_SIGMA_C | 1 | ℂ | Complex, relational (language default) |
| NS_SIGMA_H | 2 | ℍ | Quaternion, non-commuting |
| NS_SIGMA_O | 3 | 𝕆 | Octonion, non-associating |
| NS_SIGMA_S | 4 | 𝕊 | Sedenion, non-alternative |

### Token Filter

Every token passes `token_accept(tok, filetype)` before being admitted to
the field. Rejection is silent and counted (`monad.rejected_count`).

Filetype is resolved from file extension at ingest time (`filetype_from_ext()`),
so `.c`/`.py`/`.h` files use code rules (longer tokens, high-digit ratio OK)
while `.txt`/`.md` use prose rules (max 24 chars, base64 rejected).

View rejection count: `ptolemy -F` (field health report).

### Daemon Mode

```bash
ptolemy -d           # start daemon
ptolemy -D "query"   # query running daemon
```

Protocol over `~/.ptolemy/ptolemy.sock`:

```
HEAR <prompt>  →  response + ".\n"
STATUS         →  field status + ".\n"
HEALTH         →  full health report + ".\n"
QUIT           →  saves checkpoint, closes socket
```

Systemd socket activation: `systemctl --user enable --now ptolemy.socket`

### Security

- Extension whitelist blocks `.pem`, `.key`, `.crt`, `.env` and all non-semantic types
- `PRUNE_NAMES` prevents traversal of `.ssh`, `.gnupg`, `.aws`, `.azure`, `.gcloud`, `keyrings`, `.cert`, `.pki`
- PEM content guard in `monad_learn()` refuses text starting with `-----BEGIN `
- All three layers are defence-in-depth — each operates independently
