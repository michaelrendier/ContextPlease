#!/usr/bin/env bash
# Run telescope_download.py (or verify_downloads.py) so that it survives lid-close, idle and screen-lock sleeps and
# cannot take the machine down: low CPU and I/O priority, a memory cap, and a systemd sleep inhibitor held for the run.
# usage: run_download.sh MANIFEST.json STATE.json "/media/rendier/Telescope Data" LOGFILE [extra args]
set -u
manifest="$1"; state="$2"; mount="$3"; log="$4"; shift 4
here="$(cd "$(dirname "$0")" && pwd)"
cmd=(python3 "$here/telescope_download.py" "$manifest" --state "$state" --require-mount "$mount" --min-free-gb 20 --notify-secs 900 "$@")
if command -v systemd-inhibit >/dev/null; then
  exec systemd-inhibit --what=sleep:idle:handle-lid-switch --who=telescope-download --why="download in progress" \
       nice -n 10 ionice -c3 "${cmd[@]}" >>"$log" 2>&1
else
  exec nice -n 10 ionice -c3 "${cmd[@]}" >>"$log" 2>&1
fi
