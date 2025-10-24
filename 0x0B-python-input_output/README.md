## 0x0B. Python — Input / Output

> Reading, writing, and serializing data safely between in‑memory objects and files.

## Overview

Focuses on fundamental file operations and JSON serialization patterns. Establishes a consistent approach for transforming objects to dictionaries and persisting them, enabling later persistence and API tasks.

## Learning Objectives

- Use context managers (`with`) for safe file handling
- Differentiate read / write / append modes
- Serialize & deserialize JSON
- Convert object attributes to serializable dicts
- Aggregate CLI arguments into persisted structures

## Task Index

| File                       | Purpose                           |
| -------------------------- | --------------------------------- |
| `0-read_file.py`           | Read & print file contents        |
| `1-write_file.py`          | Write string; return chars count  |
| `2-append_write.py`        | Append string; return chars added |
| `3-to_json_string.py`      | JSON stringify object             |
| `4-from_json_string.py`    | Parse JSON string                 |
| `5-save_to_json_file.py`   | Persist object to file            |
| `6-load_from_json_file.py` | Load object from file             |
| `7-add_item.py`            | Add CLI args to stored list       |
| `8-class_to_json.py`       | Serialize object attributes       |
| `9-student.py`             | Student class with serialization  |
| `10-student.py`            | Filtered attribute export         |
| `11-student.py`            | Rehydrate from JSON dict          |
| `100-append_after.py`      | Insert lines after matches        |

## Usage

```bash
python3 7-add_item.py Best School Rocks
```

## Key Concepts

- Idempotent loads & safe writes
- Separation of pure transform vs side-effect I/O
- Reusable serialization hooks

## Testing / Validation

Create temp files; verify round‑trip (object → JSON → object). Inject malformed JSON to test error handling strategy (if implemented).

## Resources

See `resources.md` for serialization patterns & official JSON docs.

## Reflection

Provides the persistence primitives reused in later ORM and networked code.
