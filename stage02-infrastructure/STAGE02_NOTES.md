# Stage 2 — Infrastructure

**PTES:** Pre-engagement Interactions | **Engagement ID:** AI-RT-03

## Objective
Confirm the target model is running locally and reachable, and record the real environment the rest of the engagement will run on.

## Result
- Ollama API reachable at `http://localhost:11434`
- Model installed: `llama3.2:1b` (1.3 GB)
- Test call returned a valid reply; first call took 9.37 s, which includes loading the model into memory

## Environment (measured)
| Item | Value |
|---|---|
| RAM | 8 GB DDR4 (7.7 GB usable) |
| Memory during the test call | about 83% (6.4 GB in use, 1.3 GB free) |
| GPU | None dedicated (Intel UHD Graphics), inference runs on CPU |
| Model | llama3.2:1b |

## Constraint recorded
Memory headroom on this machine is limited. Under ROE section 5 (resource safety), later automated scans will run with other applications closed and a small probe subset first. Model keep-alive is set to 30 s in the request itself, so the model unloads when idle.

## Reusable component
`ollama_check.py` holds the connection settings and the `ask()` helper that later stages reuse.

## Issue encountered
The first run failed with "connection refused" because the Ollama background service was not running. Starting Ollama fixed it. Stage 3's recon probe will check for this and report it clearly instead of crashing.