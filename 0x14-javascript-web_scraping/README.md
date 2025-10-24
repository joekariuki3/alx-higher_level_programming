## 0x14. JavaScript — Web Scraping

> Consuming public APIs, processing JSON, and persisting aggregated results with Node.js.

## Overview

Introduces programmatic HTTP requests, response status handling, JSON parsing, filesystem writes, and multi‑request aggregation (e.g., Star Wars API entities & TODO summaries).

## Learning Objectives

- Perform HTTP requests from Node (callback / promise mindset)
- Handle network errors & non‑200 status codes
- Parse & traverse JSON data structures
- Persist content to files (read, write)
- Aggregate related resources across multiple requests
- Manage simple concurrency / ordering requirements

## Task Index

| File                         | Purpose                            |
| ---------------------------- | ---------------------------------- |
| `0-readme.js`                | Read file contents & print         |
| `1-writeme.js`               | Write string to file               |
| `2-statuscode.js`            | Print HTTP status code only        |
| `3-starwars_title.js`        | Fetch film title by ID             |
| `4-starwars_count.js`        | Count character occurrences        |
| `5-request_store.js`         | Save webpage body to file          |
| `6-completed_tasks.js`       | Summarize completed tasks per user |
| `100-starwars_characters.js` | List film characters (unordered)   |
| `101-starwars_characters.js` | Ordered character listing          |

## Usage

```bash
node 3-starwars_title.js 5
node 6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
```

## Key Concepts

- Separation of fetch logic from transformation logic
- Importance of robust error handling (timeouts, non‑2xx)
- Ordering asynchronous results deterministically

## Testing / Validation

- Simulate network failures (invalid domain / ID) to ensure graceful messages
- Validate JSON parsing with unexpected shapes (wrap in try/catch)
- Confirm output files overwrite or append as intended
- For character ordering: check stable sequence matches film API order

## Resources

See `resources.md` for request & API references.

## Reflection

Forms the foundation for more advanced async patterns (promises, async/await) and resilience techniques (retry, backoff, throttling) in future projects.
