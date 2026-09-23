# ~/.clauderc — Claude Code environment
# Sourced by .bashrc. Bash-first protocol shortcuts, repo paths, constants.
# Do not duplicate vars already in .bashrc / .profile.

# ============================================================
# PROJECT ROOT
# ============================================================

export PROJ="/home/rendier/Projects/ThePlace"

# ============================================================
# REPO SHORTCUTS
# ============================================================

export AIN="$PROJ/Ainulindale"
export VALE="$PROJ/ValaQuenta"
export VAPMIP_DIR="$PROJ/VAPMIP"
export FAP="$PROJ/FourthAgePapers"
export TURING="$PROJ/TuringStack"
export PTORRENT="$PROJ/PTorrent"
export POE_DIR="$PROJ/POE"
export USYNTH="$PROJ/UniversalSynth"
export DATASETS="$PROJ/DataSets"
export ADDPAPERS="$AIN/AddPapers"
# added 2026-09-22 -- these were missing despite being in active, heavy use
export GLL="$PROJ/GenerationalLineage"
export CTXPLZ="$PROJ/ContextPlease"
export PTOLDESK="$PROJ/PtolemyDesktop"
export SSR="$PROJ/SedenionSpectralRelativity"
export MMA="$PROJ/MultiplicationMatrixAnimator"

# ============================================================
# MEMORY + SCRATCHPAD
# ============================================================

export CLAUDE_MEMORY="/home/rendier/.claude/projects/-home-rendier-Projects-ThePlace/memory"

# PERSISTENT SCRATCHPAD (Cody, 2026-08-08) — NOT /tmp.
# Claude's side work has archival value and feeds the "complete storytelling"
# of the Ainulindale CS paper. The harness still hands Claude a /tmp path at
# session start; Claude is to IGNORE it and use this instead, one dated
# subdirectory per piece of work, each with a README.md.
export CLAUDE_SCRATCH="/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad"
scratch() { mkdir -p "$CLAUDE_SCRATCH/$(date +%F)_$1" && cd "$CLAUDE_SCRATCH/$(date +%F)_$1"; }

# ============================================================
# CONTEXT PRIMERS + TODO HISTORY  (Cody, 2026-08-28)
# ============================================================
# ALL context/session primers were migrated out of every ThePlace repo into
# a single centralised store, organised by originating repo. PTOLEMY_DOCS was
# moved wholesale and deleted. TODO.md files were COPIED (originals stay).
#
#   hist_prime = every context primer, PTOLEMY_DOCS, session-context docs
#   hist_todo  = a snapshot copy of every repo's TODO(.md)
#
export CLAUDE_HIST_PRIME="/home/rendier/Projects/ThePlace/ContextPlease/claude/hist_prime"
export CLAUDE_HIST_TODO="/home/rendier/Projects/ThePlace/ContextPlease/claude/hist_todo"
#
# PROTOCOL — every context primer written from now on goes to
#   $CLAUDE_HIST_PRIME/<OriginatingRepo>/<original-subpath>
# (repo = the top-level ThePlace dir it pertains to; "_root" for none).
# Never leave a new primer loose in a repo. `histprime` jumps there:
histprime() { mkdir -p "$CLAUDE_HIST_PRIME/${1:-_root}" && cd "$CLAUDE_HIST_PRIME/${1:-_root}"; }

# ============================================================
# PYTHON PATH — enables: from ValaQuenta.X import Y
# ============================================================

export PYTHONPATH="$PROJ:${PYTHONPATH}"

# ============================================================
# AINULINDALE CANONICAL CONSTANTS
# Exact values from canonical_math.md — use these, never retype.
# ============================================================

export D_STAR="0.24600"
export OMEGA_ZS="0.5671432904097838"
export GAP="0.000707357533249"
export GAP_APPROX="1/(1000*sqrt(2))"       # 0.035% approx — NOT 1/sqrt(2000)
export N_STAR="5.2570"                       # n-ball volume peak
export V16="0.2353"                          # V(16) — NOT equal to D_STAR
export ZD_PAIRS="84"                         # diagonals = 42 Assessors x 2
export ZD_CLASSES="42"                       # Assessors (canonical classes)
export ZD_PRIMITIVE="168"                    # PRIMITIVE unit ZDs = 42x4 = |PSL(2,7)|
export ZD_COMPOSITE="168"                    # DEPRECATED alias of ZD_PRIMITIVE.
# LABEL CORRECTION 2026-08-05 (de Marrais 2000, verified by modules/box_kite):
#   168 is the count of PRIMITIVE UNIT zero divisors, = |PSL(2,7)|, arranged as
#   point-set quartets along the 42 Assessors. COMPOSITE zero divisors are NOT
#   168 -- they "comprise all points of certain hyperplanes of up to 4
#   dimensions", i.e. a continuum, not a count. ZD_COMPOSITE is kept as an alias
#   so nothing breaks; use ZD_PRIMITIVE in new work.
export ZD_ORDERED_PAIRS="336"                # ordered annihilating pairs = 84x4
export ZD_BOX_KITES="7"                      # octahedral charts, 6 Assessors each
export ZD_GROUP="PSL(2,7)"                   # order 168 = Aut(Fano) = GL(3,2).
# NOT G2. Moreno (1997): norm-one ZDs are homeomorphic to G2 -- true, but that
# is a "blow-up" (de Marrais) that forgets which Fano line is which. PSL(2,7) is
# the finite subgroup of G2 that PRESERVES the labelling. Build there.
export PG32_POINTS="15"                      # pure imaginaries as PG(3,2) points
export PG32_LINES="35"                       # multiplication triplets
export PG32_PLANES="15"                      # Fano planes -- 15, NOT 32

# ============================================================
# ⚠ CREDENTIAL RULE (Cody, 2026-08-08) — READ BEFORE TOUCHING ANY TOKEN
# ============================================================
# GITHUB_TOKEN is the ONLY token Claude ever uses. Full stop.
#
# PTOL_SEED_TOKEN (and anything else token-shaped in ~/.bashrc) belongs to
# THE MONAD. It is unspecified, it is not Claude's, and it must never be read,
# tested, exported, or sent anywhere — not even to check which of two tokens
# is which. If two token-shaped strings turn up, identify the right one by its
# VARIABLE NAME, never by trying both.
#
# GITHUB_TOKEN lives in ~/.bashrc (not here, not in any repo). A newly created
# PAT can take a minute to activate on GitHub's side — a 401 immediately after
# creating one is usually propagation, not a bad token. Wait and retry before
# diagnosing anything.

# ============================================================
# GIT — push any repo using GITHUB_TOKEN
# Usage: gpush                    (auto-detects repo name + CURRENT branch)
#        gpush RepoName           (explicit repo, still current branch)
#
# FIXED 2026-09-22 -- this used to hardcode `main` as the push/pull target,
# which was silently wrong the moment FourthAgePapers became a legitimate
# exception to main-only (see feedback_branch_policy memory, corrected same
# day): PtolemyDesktop/PTorrent use device-arch branches, FourthAgePapers is
# allowed genuine thematic work-in-progress branches, everything else (22+
# repos) is still main-only by policy -- but the FUNCTION now follows
# whatever branch you're actually on rather than assuming, so it can't push
# a FourthAgePapers branch's work onto main by accident, and can't silently
# no-op on the other three either.
# ============================================================

gpush() {
    local repo="${1:-$(basename "$(git rev-parse --show-toplevel 2>/dev/null)")}"
    if [ -z "$repo" ]; then
        echo "gpush: not in a git repo and no repo name given" >&2
        return 1
    fi
    local branch; branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
    if [ -z "$branch" ] || [ "$branch" = "HEAD" ]; then
        echo "gpush: could not determine current branch (detached HEAD?)" >&2
        return 1
    fi
    git push "https://michaelrendier:${GITHUB_TOKEN}@github.com/michaelrendier/${repo}.git" "$branch"
}

# Pull with token
gpull() {
    local repo="${1:-$(basename "$(git rev-parse --show-toplevel 2>/dev/null)")}"
    local branch; branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
    if [ -z "$branch" ] || [ "$branch" = "HEAD" ]; then
        echo "gpull: could not determine current branch (detached HEAD?)" >&2
        return 1
    fi
    git pull "https://michaelrendier:${GITHUB_TOKEN}@github.com/michaelrendier/${repo}.git" "$branch"
}

# ============================================================
# REPO STATUS — quick sweep of all project repos
# ============================================================

rstatus() {
    # updated 2026-09-22 -- added the repos that became active/heavily used
    # since this list was last touched: GenerationalLineage, ContextPlease,
    # PtolemyDesktop, SedenionSpectralRelativity, ArdaQuenta, MultiplicationMatrixAnimator
    for repo in Ainulindale ValaQuenta VAPMIP FourthAgePapers TuringStack PTorrent POE UniversalSynth \
                GenerationalLineage ContextPlease PtolemyDesktop SedenionSpectralRelativity ArdaQuenta \
                MultiplicationMatrixAnimator; do
        local path="$PROJ/$repo"
        if [ -d "$path/.git" ]; then
            local branch count
            branch=$(git -C "$path" rev-parse --abbrev-ref HEAD 2>/dev/null)
            count=$(git -C "$path" status --porcelain 2>/dev/null | wc -l)
            printf "%-20s  %-6s  %s dirty files\n" "$repo" "$branch" "$count"
        fi
    done
}

# ============================================================
# VALAQUEST — run a ValaQuenta engine one-liner
# Usage: vale "from ValaQuenta.bao_mass_gap import validate; validate()"
# ============================================================

vale() {
    python3 -c "$@"
}

# ============================================================
# CANONICAL MATH CHECK — print key constants to console
# Prevents introducing wrong values mid-session.
# ============================================================

canon() {
    echo "d*       = $D_STAR"
    echo "OMEGA_ZS = $OMEGA_ZS   (Lambert W(1))"
    echo "GAP      = $GAP"
    echo "GAP approx: $GAP_APPROX  (NOT 1/sqrt(2000))"
    echo "n*       = $N_STAR       (n-ball peak)"
    echo "V(16)    = $V16          (≠ d*, 4.3% off)"
    echo "ZD:      $ZD_PAIRS diagonals / $ZD_CLASSES Assessors / $ZD_PRIMITIVE primitive (=|PSL(2,7)|)"
    echo "         $ZD_ORDERED_PAIRS ordered pairs / $ZD_BOX_KITES box-kites (octahedra) / group $ZD_GROUP -- NOT G2"
    echo "PG(3,2): $PG32_POINTS points / $PG32_LINES lines / $PG32_PLANES Fano planes (not 32)"
    echo ""
    echo "Full table: $CLAUDE_MEMORY/canonical_math.md"
}

# ============================================================
# SEARCH — grep across all project repos
# Usage: psearch "symbol_name"
#        psearch "symbol_name" "*.py"
# ============================================================

psearch() {
    local pattern="$1"
    local glob="${2:-*}"
    grep -r --include="$glob" -l "$pattern" "$PROJ" \
        --exclude-dir=".git" --exclude-dir="__pycache__" \
        --exclude-dir=".archive" 2>/dev/null
}

# Print matching lines with context
pgrep() {
    local pattern="$1"
    local glob="${2:-*.py}"
    grep -r --include="$glob" -n "$pattern" "$PROJ" \
        --exclude-dir=".git" --exclude-dir="__pycache__" \
        --exclude-dir=".archive" 2>/dev/null
}

# ============================================================
# MEMORY — quick read of a memory file by partial name
# Usage: mem canonical_math
#        mem user_profile
# ============================================================

mem() {
    local name="$1"
    local file
    file=$(find "$CLAUDE_MEMORY" -name "*${name}*" 2>/dev/null | head -1)
    if [ -n "$file" ]; then
        cat "$file"
    else
        echo "mem: no file matching '$name' in $CLAUDE_MEMORY" >&2
        ls "$CLAUDE_MEMORY"
    fi
}

# ============================================================
# WIKI — open a ValaQuenta wiki page by number or name
# Usage: wiki 64
#        wiki noether
# ============================================================

wiki() {
    local query="$1"
    local file
    file=$(find "$VALE/wiki" -name "*${query}*" 2>/dev/null | head -1)
    if [ -n "$file" ]; then
        cat "$file"
    else
        echo "wiki: no page matching '$query'" >&2
        ls "$VALE/wiki" 2>/dev/null | head -20
    fi
}

# ============================================================
# BIN ARCHIVE — holcus monad .bin files
# ============================================================

export BIN_ARCHIVE="/home/rendier/Projects/ThePlace/PTorrent/bin_archive/clean"

# ============================================================
# PTOL — C sedenion engine shortcuts
# ============================================================

export PTOL_BIN="$VAPMIP_DIR/PtolC/ptol"
export PTOL_DIR="$VAPMIP_DIR/PtolC"
export PTOL_PAPERS="$HOME/.ptolemy/papers"

# Run ptol with raw output piped to ptol_layer for full response
ptol_r() { "$PTOL_BIN" -r "$@"; }
ptol_s() { "$PTOL_BIN" "$@"; }   # default: SVG + English path

# ============================================================
# UDEO — Unified Dimensional Entropy Oracle (TuringStack)
# Zero-divisor attack class; embargo ends 2026-11-25.
# CLARIFIED 2026-09-19: embargo is CVE-disclosure only -- researchers/
# general findings are OK to discuss/publish, just not the CVE-specific
# exploit detail before the date above.
# ============================================================

export UDEO_POC="$TURING/udeo_poc.py"
export UDEO_EMBARGO="2026-11-25"

# ============================================================
# NETCUP SERVER — ssh shorthand
# ============================================================

ptol_ssh() {
    ssh "${NETCUP_REMOTE_SSH_USERNAME}@${NETCUP_REMOTE_SSH_HOSTNAME}" "$@"
}


# ── THE BOUNDARY LEVER (2026-08-15) ─────────────────────────────────────────
# Paper : FourthAgePapers/BoundaryLever/   (00_vision 01_predictions 02_data 03_results)
# Engine: ValaQuenta/modules/angular_rank/ (the 16D oscilloscope, 12 equations)
# Wiki  : Ainulindale/wiki/87_the_boundary_lever.md
#         Ainulindale/wiki/86_the_16d_oscilloscope.md
#         ValaQuenta/wiki/angular_rank.md
#         VAPMIP/docs/wiki/Operating-L-IO.md   (the L_(I|O) operator's manual)
# Canonical maths: ~/.clauderc_canonical_maths, THE BOUNDARY LEVER block.
#
# CLAIM: the Cayley-Dickson doubling boundary is a CHIRAL MIRROR
#   e_(i+H) e_(j+H) = e_j e_i,  H = dim/2
# whose two fixed points e_0 and e_(dim/2) are exactly the indices in no
# zero-divisor plane, at every level from dim=16 up.
# P1 (orphans at dim=128 == [0,64]) CONFIRMED as a pre-registered prediction.
# P2/P4/P5 falsified and reported as such; P5's failure produced the parity law
# (non-crossing nullity EVEN x4, crossing ODD x4), pre-registered as P6 @ 256.
#
# The norm is CHIRALITY-BLIND: M is an isometry and an involution, and
# |M(x)M(y)| matches BOTH |xy| and |yx| -- the handedness lives entirely in the
# ORDERING, never in the metric. "right and left switch places but the hands
# don't." Two reflections compose to a rotation; boundaries at dim/2 give pitch
# ln 2; rotation + log advance = the Archimedes screw, from the algebra.


# ── PROVENANCE FILES (2026-08-28) ──────────────────────────────────────────
# ~/.clauderc_user_provenance  — Cody's ORIGINAL work vs the established
#   literature it is built on. Companion to ~/.clauderc_context. NOT sourced.
#   Claude's to edit freely. First pass covers Ainulindale only; VAPMIP and the
#   other repos get appended passes. Any entry later found to be already
#   established is MOVED to that file's "reclassified as prior art" section.
# ~/.clauderc_citations  (2026-09-04) — the LIVE citation queue: published work
#   that names/formalises after the fact something Cody engineered independently,
#   organised BY REPO. Populate opportunistically ("as I step on legos"); before
#   a repo's paper/README/wiki ships, run that repo's section and add the cites.
#   Replaces ThePlace/CITABLE_WORK_INDEX.md as the working queue (that file =
#   history). NOT sourced. Claude's to edit freely.
# Ainulindale's own bibliographies (scattered, want consolidating into a new
#   Ainulindale/wiki/98_provenance_and_citations.md):
#   - Ainulindale/README.md  §References  (7 items)
#   - Ainulindale/AgeSecond/Second_Age_Ainulindale_Conjecture.md  §References (25)
#   - Ainulindale/AgeThird/D-CS_Memory.md  "The Mathematics Used — An Inventory"
#   - Ainulindale/PROVENANCE.md  (development narrative, no citations)
#   - Ainulindale/METHODOLOGY.md (BCE — Boundary Constraint Engineering)


# ── LOAD ANY ADDITIONAL .clauderc SHELL FRAGMENTS (2026-08-28) ─────────────
# Authorized by Cody to ensure new .clauderc pieces load. Reference/data
# files (.clauderc_context*, _canonical_maths, _memory, _user_provenance …)
# are read by Claude, NOT shell-sourced. Anything that IS a shell fragment
# goes in ~/.clauderc.d/*.sh and is sourced here automatically.
if [ -d "$HOME/.clauderc.d" ]; then
    for _frag in "$HOME"/.clauderc.d/*.sh; do
        [ -r "$_frag" ] && . "$_frag"
    done
    unset _frag
fi
