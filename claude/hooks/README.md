# monad_observe.py — the conversation-ingest hook (mirrored copy)

Mirrored here 2026-09-22 for the same reason everything else in
`ContextPlease/claude/` is mirrored: this repo's job is to carry exact,
checkable historical context of ThePlace's work into Claude Code sessions
and other tooling — not to run anything itself. **This is not the live
copy.** The hook that actually executes is `~/.claude/hooks/monad_observe.py`,
wired into `~/.claude/settings.json`; a second working copy lives in
`VAPMIP/monad_bin/hooks/` next to the `harness.py` it imports from. This
copy is documentation-of-record, kept in sync by hand when the live hook
changes.

## What it is

A Claude Code hook that pipes every conversation turn — the human's prompt
and Claude's own reply — into the Ptolemy Monad's live language field,
passively, as the conversation happens:

```
UserPromptSubmit -> monad_observe.py external   (human prompt, full weight)
Stop              -> monad_observe.py internal   (Claude's last text reply,
                                                    lower weight, flagged echo)
```

Text is stripped to plain prose (code, tables, links, notation-dense lines
removed — thinking blocks and tool I/O never leave the transcript at all),
split to sentences, and written non-blocking to the Monad's ingest FIFO
(`~/.ptolemy/monad.observe.fifo`), falling back to a local spool file if
the resident daemon isn't up. Best-effort throughout — it is never allowed
to block or fail a turn.

## The weight asymmetry — the actual number, not a description of it

From `VAPMIP/harness.py`'s `INGEST_POLICY`:

```python
'external': {'w_sem': 1.5, 'w_ctx': 1.5, 'echo': 0}   # the human, full weight
'internal': {'w_sem': 0.9, 'w_ctx': 0.6, 'echo': 1}   # Claude, reduced + flagged
```

The human is ingested uncapped and never treated as an echo. Claude's own
prose is ingested at a deliberately lower and asymmetric weight
(semantic weight `0.9`, context weight `0.6`) and tagged `echo=1` — the
Monad is built to be shaped more by what it is told than by the sound of
its own voice answering.

## Where this sits in the larger pipeline

`hook -> OBSERVE_FIFO/SPOOL -> ptolemy-monad.service (systemd --user,
resident field) -> repack.py (folds drift into monad3_c.bin at the repack
knee) -> PtolC/monad3_c.bin`. Full detail: `VAPMIP/monad_bin/hooks/README.md`
and `VAPMIP/monad_bin/README.md` / `SPEC.md`.

## Provenance

Live paths at the time of mirroring: `~/.claude/hooks/monad_observe.py`
(hook), `~/.claude/settings.json` (wiring, `UserPromptSubmit`/`Stop`),
`~/.config/systemd/user/ptolemy-monad.{service,socket}` (daemon),
`VAPMIP/PtolC/monad3_c.bin` (the packed store it ultimately feeds). Copied
byte-identical (`md5sum` checked against the live file at copy time).
