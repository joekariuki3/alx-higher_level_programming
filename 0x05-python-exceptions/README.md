## 0x05. Python — Exceptions

> Anticipating, raising, and handling runtime errors to preserve stability & clarity.

## Overview

Introduces structured error handling using `try/except/else/finally`, deliberate raising for validation, and safe execution wrappers—building resilience into small scripts.

## Learning Objectives

- Distinguish errors vs exceptions
- Apply `try / except / else / finally` blocks effectively
- Target specific exception types over broad catches
- Avoid bare `except:` anti-pattern
- Raise built‑ins (TypeError, NameError) intentionally
- Print diagnostics to stderr when appropriate

## Task Index

| File                            | Purpose                       |
| ------------------------------- | ----------------------------- |
| `0-safe_print_list.py`          | Safely print x elements       |
| `1-safe_print_integer.py`       | Safely print integer          |
| `2-safe_print_list_integers.py` | Print first x ints only       |
| `3-safe_print_division.py`      | Division with finally cleanup |
| `4-list_division.py`            | Element-wise guarded division |
| `5-raise_exception.py`          | Raise TypeError demo          |
| `6-raise_exception_msg.py`      | Raise NameError w/ message    |
| `100-safe_print_integer_err.py` | Print or log error to stderr  |
| `101-safe_function.py`          | Execute function safely       |

## Usage

```bash
python3 4-list_division.py
```

## Key Concepts

- Separation of normal vs exceptional control paths
- Granular exception handling improves diagnostics
- `finally` ensures resource or state cleanup

## Testing / Validation

Feed: non‑int elements, division by zero, functions that raise internally to `101-safe_function` and observe captured errors.

## Resources

See `resources.md` for Python exception hierarchy references.

## Reflection

Clear, minimal exception handling scaffolds scale as logic complexity grows.
