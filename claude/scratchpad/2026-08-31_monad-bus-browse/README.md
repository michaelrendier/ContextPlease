# 2026-08-31 — Monad bus: language-blind backend + browse + governor

Cody: insert **browse/search**, a **threading bus**, and **memory management**
into *both* the harness (`VAPMIP/harness.py`) and the python3 monad
(`RotaryBoxKiteMonad`, `rotary_rerun_boxkite_monad.py`), for smoke + unit
testing. The harness must be **blind to the monad's language** — it loads the
C binary (the `ptolemy` daemon) *or* the python monad, at discretion, then
reports. All harness connections warn-not-fault; boot continues.

## Pieces

- `VAPMIP/monad_bus.py` — NEW
  - `ResourceGovernor` — `CEILING = MemTotal + min(SwapTotal, MemTotal//2)`
    (Cody's "RAM + ½ RAM swap" rule). `Job{name,tier,ram_peak,bw_cost}`,
    `admit()` (slots ∧ RAM ∧ bandwidth), `guard()` ctx-mgr (waits by tier,
    tracks the running set, `gc.collect()` on retire). Memory management
    falls out of threading admission, exactly as described.
  - `MonadBackend` / `PyMonadBackend` / `CMonadBackend` / `NullMonadBackend`
    + `load_monad(prefer='auto'|'c'|'python')` → `(backend, report)`.
- `VAPMIP/monad_browse.py` — NEW — `search_url()`, `fetch()` (minimal urllib,
  size-capped), `strip_html()` (html2text → `harness.strip_to_prose`),
  `estimate_ram()` (parse blowup for the governor).
- `VAPMIP/harness.py` — EDIT — `'web'` ingest class; `load_monad()` / `backend`
  / `governor`; `search()` / `browse()` (dedup + governor-guarded); backend
  wired into `_observe_in_process`.
- `VAPMIP/rotary_rerun_boxkite_monad.py` — EDIT — bare `search()` (default
  browser via `webbrowser`), `browse_observe()` (governor-guarded minimal
  fetch → strip → `_hear` into its own field); delegate to the harness when
  attached. KVM tie-in left as a docstring note.
- `VAPMIP/tests/test_monad_bus_browse.py` — NEW — unit.
- `smoke.py` (this dir) — end-to-end against a real `Harness` + example.com.

## Deferred (monad notes)
- KVM as the bare monad's eyes (poll focused URL → `browse_observe`).
- code-type text stripping (only prose today).
- `ptol_blockchain` as the real dedup ledger (in-memory `_seen` dict stands in).
- bandwidth EWMA is a stub cap; wire to real throughput later.
