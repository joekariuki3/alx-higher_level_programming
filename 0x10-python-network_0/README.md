## 0x10. Python — Network #0

> Low‑level HTTP exploration with `curl` before introducing higher‑level libraries.

## Overview

Focuses on raw request crafting from the shell to internalize verbs, headers, payloads, status codes, and basic JSON submission. Includes a logic detour (`6-peak.py`) for algorithm practice.

## Learning Objectives

- Use HTTP verbs (GET, POST, DELETE)
- Inspect response size & status code
- Send custom headers & form data
- Submit JSON payloads via curl
- Recognize when low-level inspection aids debugging

## Task Index

| File                 | Purpose                        |
| -------------------- | ------------------------------ |
| `0-body_size.sh`     | Display response body size     |
| `1-body.sh`          | Fetch body for 200 OK          |
| `2-delete.sh`        | Issue DELETE request           |
| `3-methods.sh`       | List allowed methods (OPTIONS) |
| `4-header.sh`        | Add custom header              |
| `5-post_params.sh`   | POST form fields               |
| `6-peak.py`          | Find peak in unsorted list     |
| `100-status_code.sh` | Print only status code         |
| `101-post_json.sh`   | POST JSON payload              |

## Usage

```bash
bash 0-body_size.sh https://example.com
python3 6-peak.py
```

## Key Concepts

- Protocol fundamentals precede abstraction
- Headers & methods shape server behavior

## Testing / Validation

Point scripts at known endpoints (local mock or public echo services) and verify status codes / headers. For `6-peak.py`, test arrays with single peak, multiple peaks, sorted/descending.

## Resources

See `resources.md` for HTTP fundamentals.

## Reflection

Groundwork that demystifies what higher-level libraries automate later. Direct curl practice sharpens intuition for debugging headers, payload mismatches, and status anomalies before abstraction layers hide them.
