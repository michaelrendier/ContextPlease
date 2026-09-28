# ScalarContextPropagation README update (2026-09-28)

Branch `scalar-context-propagation` of FourthAgePapers (found via `git branch -a`; a stale worktree
from an earlier session, at `/tmp/.../64f74468.../scp_read`, was pruned first per the
persistent-scratchpad rule -- /tmp is never canonical).

## What was checked
No UDEO or GenerationalLineage sibling-count mentions exist in this paper at all -- searched fully,
none found -- so the UDEO/TuringStack-drop fix in GenerationalLineage needed no correction here.
Re-ran live, against GL's just-released 1.0.0: `import lineage; lineage.un_sieve(100_000)` (paper
§4.4) still reproduces 313 / 49999 / 7.193551572213686 bit-for-bit; `from GenerationalLineage.engine
.toolsets.cs_benchmark import descend` (paper §8) still imports and runs exactly as shown (tested
from ThePlace root -- Python 3 namespace packages make `GenerationalLineage.engine...` resolve with
no __init__.py needed). Nothing in the paper needed a correction; added a changelog entry saying so.

## What was added
Facebook link (facebook.com/rendier) to both author-contact blocks (top author line, section 12
Provenance and attribution), matching the existing GitHub/ORCID format.

## Push conflict, resolved
`gpush FourthAgePapers` first failed: the remote branch had moved (Cody's own live edit, "edit to
Readme to include Holcus as The Extractor.", one line at section 3 / Figure 3b, unrelated to my
edits). Fetched, confirmed my local base was a clean ancestor of the new remote tip, rebased (no
conflicts -- different parts of the file), pushed. Commit `fe2f6c3` on `scalar-context-propagation`,
FourthAgePapers.

## Worktree
Created at ContextPlease/claude/scratchpad/2026-09-28_scp_readme_update/ScalarContextPropagation
(persistent, per [[feedback-persistent-scratchpad]]), removed after the push. Re-add with:
`cd FourthAgePapers && git worktree add <path> scalar-context-propagation`
