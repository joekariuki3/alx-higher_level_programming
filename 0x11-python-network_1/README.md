## 0x11. Python — Network #1

> Higher‑level HTTP scripting with `urllib` and Requests‑style patterns & JSON handling.

## Overview

Builds on raw protocol understanding to fetch, parse, and handle responses in Python—introducing error handling, authentication examples, and JSON payload processing.

## Learning Objectives

- Fetch & decode HTTP responses programmatically
- Gracefully handle HTTP errors
- Parse JSON body content
- Use headers for simple auth (GitHub API example)
- Compare builtin `urllib` vs higher-level approach

## Task Index

| File                    | Purpose                    |
| ----------------------- | -------------------------- |
| `0-hbtn_status.py`      | Basic status fetch         |
| `1-hbtn_header.py`      | Retrieve header value      |
| `2-post_email.py`       | POST email field           |
| `3-error_code.py`       | Handle HTTP errors         |
| `4-hbtn_status.py`      | Alternate implementation   |
| `5-hbtn_header.py`      | Requests variant           |
| `6-post_email.py`       | Requests variant POST      |
| `7-error_code.py`       | Requests variant errors    |
| `8-json_api.py`         | POST & parse JSON response |
| `10-my_github.py`       | GitHub auth example        |
| `100-github_commits.py` | Recent commits listing     |

## Usage

```bash
python3 0-hbtn_status.py
python3 100-github_commits.py repo owner
```

## Key Concepts

- Abstraction reduces boilerplate but still needs explicit error handling
- JSON parsing enables structured automation

## Testing / Validation

Call endpoints with and without required headers to test error paths. Use invalid repo/user for GitHub script to confirm graceful failure.

## Resources

See `resources.md` for HTTP & requests documentation.

## Reflection

Shows progression from manual protocol probing to robust scripted consumption of APIs. Emphasizes disciplined error handling and structured JSON parsing—foundations for auth flows, pagination, and rate limit strategies later.

---
