## 0x05. Python - Exceptions

Error handling patterns: anticipating, raising, and recovering from runtime issues while preserving program stability.

## 📌 Learning Objectives

- Difference between errors and exceptions
- Using `try / except / else / finally`
- Specific vs broad exception catching
- Why not to use bare `except:`
- Raising built‑ins vs custom exceptions
- Printing to stderr vs stdout

## 📂 Files

| File                            | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| `0-safe_print_list.py`          | Safely print x elements of a list                |
| `1-safe_print_integer.py`       | Safely print an integer with formatting          |
| `2-safe_print_list_integers.py` | Print first x ints (skip non‑ints)               |
| `3-safe_print_division.py`      | Division with finally and result capture         |
| `4-list_division.py`            | Element-wise division with robust error handling |
| `5-raise_exception.py`          | Raise a `TypeError` deliberately                 |
| `6-raise_exception_msg.py`      | Raise a `NameError` with custom message          |
| `100-safe_print_integer_err.py` | Print integer or write error to stderr           |
| `101-safe_function.py`          | Execute a function safely and capture exceptions |

## 🧠 Key Concepts

- Separation of normal flow and error flow
- Granular exception targeting improves diagnostics
- Use of `finally` for guaranteed cleanup paths

## 🧪 Testing Ideas

Feed malformed lists, zero divisors, non‑callables to `101-safe_function`.

## 📎 Resources

See `resources.md` for links on Python exception hierarchy.

## 🗒 Reflection

Structured error handling improves reliability and clarity when failures occur.
