# 15 — The Monad

| | |
|---|---|
| Current implementation | `VAPMIP/monad.py` v2.0.0 (4,527 lines): classes `Crank`, `Engine`; C counterpart in `VAPMIP/PtolC/` |
| Earlier implementation | `PtolemyDesktop/Philadelphos/monad.py` (1,276 lines): class `Monad(N)` with `learn`, `hear`, `speak`, `lookup` |
| Also known as | Ptolemy · Philadelphos · Ptolemaious Holcaios Philadelphos |
| Last verified | 2026-11-13: both files read; §3 listing executed against `VAPMIP/monad.py`; §3 collision measurement run on `/usr/share/dict/words` |

## 1. What it is

A single-wire engine over the sedenion algebra. It is not a language model,
not a transformer, and it does not train by gradient descent. Text (or audio
bands, or numbers, or a raw sedenion) enters through one call, and everything
after that is mechanical.

```
wire(data, source)  →  sedenion  →  field update / retrieval / firing
```

The Monad is the RedBlue engine made executable ([14](14_redblue_hamiltonian.md)).
In the code's own words (`monad.py` header): CAM = the Emmy Noether sedenion
(timing, geometry); CRANK = the Ĥ_RB field engine (the Noether current J^μ).
The dual flow is J_pos (Riemann, response, "what is") against J_neg (Fermat,
prompt, "what cannot be"); the next word lives at σ ≈ ½, "π/2 of the
cardioid".

Notation note: this file is where the Null Operator's `0_RB` notation lives;
elsewhere the operator is Ĥ_RB ([127](127_names_of_the_null_operator.md)).

## 2. The sixteen operators

The sedenion dimensions are the engine's computational primitives
(`monad.py` header):

| e₀ | e₁ | e₂ | e₃ | e₄ | e₅ | e₆ | e₇ |
|---|---|---|---|---|---|---|---|
| identity | negate | bind | name | apply | abstract | branch | iterate |

| e₈ | e₉ | e₁₀ | e₁₁ | e₁₂ | e₁₃ | e₁₄ | e₁₅ |
|---|---|---|---|---|---|---|---|
| recurse | allocate | query | dereference (anaphor) | compose | parallelize (three-face) | interrupt | emit |

The window builds the Cayley–Dickson tower as it fills: 1 word → ℝ, 2 → ℂ,
4 → ℍ, 8 → 𝕆, 16 → 𝕊 (the full cardioid). The three-face Wankel (e₁₃) takes
the Red face (highest J_pos, content words), the Blue face (lowest age,
context words) and the Green face (the connective dimension that binds content
to grammar), interleaved in a φ-walk.

## 3. How a word gets an address (P1, the prime hash)

A word is mapped to a zero index of ζ in three steps: read the word as a
base-95 integer (printable ASCII), take the next prime at or above it (within
the first 2¹⁶ + 1), and take that prime's rank π(p). The rank is the index of
the Riemann zero the word is attached to.

**Listing 1 — word → zero index** (`VAPMIP/monad.py`: `_horner_hash`,
`_next_prime`, `_word_zero_idx`, with the sieve and π-table that the module
builds at import; extracted and joined into one unit, docstrings removed, runs cold)

```python
PRIME_CAP = 1 << 16
sv = [True] * (PRIME_CAP + 2); sv[0] = sv[1] = False
for i in range(2, int(len(sv) ** 0.5) + 1):
    if sv[i]:
        for j in range(i * i, len(sv), i):
            sv[j] = False
pi_table, c = [0] * len(sv), 0
for k in range(len(sv)):
    c += sv[k]
    pi_table[k] = c

def horner_hash(w, base=95, offset=32):
    v = 0
    for ch in w:
        v = v * base + max(0, ord(ch) - offset)
    return abs(v)

def next_prime(v):
    v = max(2, int(v) % (PRIME_CAP + 1))
    while v <= PRIME_CAP + 1:
        if sv[min(v, PRIME_CAP + 1)] or v > PRIME_CAP:
            return v
        v += 1
    return 65537

def word_zero_idx(w):
    p = next_prime(horner_hash(w))
    return max(1, pi_table[min(p, PRIME_CAP + 1)])

print([word_zero_idx(w) for w in ('water', 'eau', 'aqua', 'wasser', 'tree', 'arbre')])
```

```
[2009, 4122, 4310, 1204, 2273, 1478]
```

These are the values `_word_zero_idx` returns in `monad.py`.

**Measured properties** (2026-11-13, `/usr/share/dict/words`, lowercase
alphabetic entries):

| Measurement | Value |
|---|---|
| distinct words | 73,445 |
| distinct zero indices they reach | 6,436 |
| range of indices | 1 … 6543 (the module comment says 6542; π(65537) = 6543 because 65537 is prime) |
| largest number of words sharing one index | 80 |

The address is therefore **many-to-one**: about eleven words per index on
average. It is an address into a finite table of 6,543 zeros, not an
injective encoding of words. Translation equivalents do not share an
index (`water` 2009, `eau` 4122, `aqua` 4310, `wasser` 1204). The claim that
a concept is a prime, and that synonyms across languages land on one prime,
is the project's `THEORETICAL` position; the mechanism that is supposed to
produce it is calibration to a baseline language, in
`VAPMIP/SemPriCon`, and is not what P1 computes ([16](16_semantic_word_engine.md)).

Zeros are generated on demand by Newton's method on the Riemann–Siegel
Z-function and cached (`_ZERO_CACHE` holds the first 50 exactly, from LMFDB;
beyond that the forward scan is used). The energy of a word is
E = |sin(π·γ/(γ+1))| for its zero γ.

## 4. The earlier `Monad` class (`Philadelphos/monad.py`)

Kept because the older wiki pages and papers describe it. Its three
operations:

| Method | Role | Channel ([14](14_redblue_hamiltonian.md) §2) |
|---|---|---|
| `learn(text)` | tokenise; encode each word; deepen the bias field β | Blue |
| `hear(text)` | parse a prompt; activate addresses; return `(index, weight)` pairs | Red |
| `speak(query, max_tokens)` | output; `speak_raw` returns the underlying `(float, float)` pairs | Green |
| `lookup(word)` | the record for one word, including `sigma` | — |

`lookup` returns σ = 0.5 for every word. This is a fixed point of the
balance iteration `_forced_sigma`, shown running in
[13](13_omgwtf_rh_proof.md) §5: it is a property of that iteration and says
nothing about where any zero of ζ lies. The ground-state constant
`L_GROUND = −1.888` is an engine input (`monad.py` line 120).

The five-stage `speak` pipeline described in earlier versions of this page
(reverse-Lagrangian extinction, catastrophic collapse, Lorenz–Stirling basin,
circle-inversion check, clathrate chromatography) is the design of the output
stage; it is `THEORETICAL`, and its Lorenz–Stirling and clathrate stages were
not located in `ValaQuenta` (see [12](12_smnnip_distribution_engine.md)).

## 5. The C implementation (`PtolC`)

`VAPMIP/PtolC/` holds `monad.c`, the daemon (`daemon.c`) and the corpus tools;
the Python header states that the field logic matches `PtolC/monad.c` exactly.
The operations map to the CLI as `learn` → `-l`, `hear` → `-h`, bulk ingest →
`-I`, daemon → `-d` / `-D`, and the daemon speaks JSON over a Unix socket
(`~/.ptolemy/ptolemy.sock`) with `HEAR`, `STATUS`, `HEALTH`, `QUIT`.
`monad_wordnet.bin` is the read-only WordNet baseline, protected against
overwrite; session state is saved separately.

Recorded in the earlier version and **not re-verified in this pass** (marked
for the next check against `PtolC/`): the build line (`make && make corpus`),
the baseline size (≈ 13 MB, ≈ 14,000 vocabulary entries), and the checkpoint
v2 record layout (`"PTOL"`, version, N, count, ground, then per record
`idx wlen E home_stratum gen_stratum word`). Security behaviour recorded:
an extension whitelist, pruned directories (`.ssh`, `.gnupg`, `.aws`, …), and a
guard that refuses text beginning with a PEM header.

Native Space strata used by the vocabulary entries: σ₀ ℝ (enumerable), σ₁ ℂ
(relational; the language default), σ₂ ℍ (non-commuting), σ₃ 𝕆
(non-associating), σ₄ 𝕊 (non-alternative). These are the σ-strata; they are
not Re(s) and not σ_RB ([133](133_canonical_maths.md) §0).

## 6. What it is not

Not a statistical estimator, a next-token predictor, a vector database, or a
retrieval-augmented system. Retrieval is by derivation from an address, so its
path length does not grow with the size of the corpus. What it does *not*
yet do is guarantee that two words with one meaning receive one address; §3
measures that.

## 7. Open items

| Item | State |
|---|---|
| Synonyms and translations sharing one address | OPEN: not produced by P1; requires the baseline calibration |
| The Tongue (attractor coordinate → nearest word) | scaffold only ([09](09_hyperwebster_engine.md), [12](12_smnnip_distribution_engine.md)) |
| σ = 0 boot (ground state before any symmetry breaking) | characterisation pending |
| d* gap, 0.000707… | OPEN ([07](07_berry_keating_engine.md)) |
| PtolC details in §5 | to re-verify |

## 8. Related pages

[09 HyperWebster](09_hyperwebster_engine.md) · [14 RedBlue](14_redblue_hamiltonian.md) ·
[16 Semantic word engine](16_semantic_word_engine.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md) ·
[20 Three-phase architecture](20_three_phase_architecture.md) · [127 Null Operator names](127_names_of_the_null_operator.md)
