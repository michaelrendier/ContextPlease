# User-agent values seen in this project's tooling

Started 2026-11-22 at Cody's request: "keep a list of these user agent values; 90% of the bot-refusal issue goes away with a Mozilla user agent."
Standing rule: every outbound request we write carries the Mozilla value below. This list records what each *tool* sends by default, so a block
can be diagnosed by looking here, and so we know which tools do NOT follow the rule unless told to.

## The project's value

| name | value | where set |
|---|---|---|
| `$CLAUDE_UA` | `Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0` | `~/.clauderc` line 416; `fetch()` helper wraps `curl -A "$CLAUDE_UA"` |

## What tools send by default (measured 2026-11-22, VAPMIP/.venv)

| tool | default user agent | follows the Mozilla rule? | how to override |
|---|---|---|---|
| curl 8.5.0 | `curl/8.5.0` | only with `-A "$CLAUDE_UA"` | `curl -A "$CLAUDE_UA"` |
| python `urllib` (also `nltk.download`) | `Python-urllib/3.12` | no | `urllib.request.Request(url, headers={'User-Agent': UA})`, or `opener.addheaders` |
| `requests` 2.34.2 (stanza, many libs) | `python-requests/2.34.2` | no | `headers={'User-Agent': UA}` or `session.headers.update(...)` |
| `httpx` 0.28.1 | `python-httpx/0.28.1` | no | `httpx.Client(headers={'User-Agent': UA})` |
| `pip` 26.2.1 (also `spacy download`) | `pip/26.2.1 {json: installer, python, distro "Linux Mint 22.1", cpu, openssl, ...}` | no; no command-line option | `PIP_USER_AGENT` is not honoured; the string is built in `pip._internal.network.session.user_agent()`; to change it, download the wheel with curl and `pip install ./file.whl` |
| `huggingface_hub` 1.33 | `unknown/None; hf_hub/2.4.0; python/3.12.3; torch/2.15.0; agent/claude-code` | no | env `HF_HUB_USER_AGENT_ORIGIN` only appends; for the files themselves use `hf_hub_download(..., headers=...)` / `build_hf_headers(user_agent=...)` or `curl` against `https://huggingface.co/<repo>/resolve/main/<file>` |

Note: pip's and Hugging Face's strings carry the OS distribution, CPU and (for HF) the name of the calling agent. Neither contains the user's name or email.

## Downloads made with a non-Mozilla agent (2026-11-22, package managers; Cody informed)

| what | tool | agent sent |
|---|---|---|
| textblob, emoji, empath, stanza, transformers, onnxruntime, sentencepiece, safetensors, torch (VAPMIP/.venv) | pip | pip default |
| spaCy `en_core_web_md` | `spacy download` (pip) | pip default |
| SamLowe/roberta-base-go_emotions, j-hartmann/emotion-english-distilroberta-base, cardiffnlp/twitter-roberta-base-irony | `huggingface_hub.snapshot_download` | hf_hub default |

All other downloads of other people's work (papers, corpora) go through curl with `$CLAUDE_UA` per the Literature Download Protocol.

## Add a row whenever a new tool or a refusal (HTTP 403/429) shows up. Record: tool, default string, whether Mozilla fixed it.
