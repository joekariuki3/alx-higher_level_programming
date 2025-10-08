## 0x07. Python — Test Driven Development (TDD)

> Writing expectations (tests/doctests) to guide and validate implementation.

## Overview

Introduces documenting behavior with doctests and focused unit tests before (or alongside) code. Emphasizes pure functions, explicit validation, and edge case handling to reduce ambiguity.

## Learning Objectives

- Explain core TDD loop (red → green → refactor)
- Author doctests for simple examples
- Use `unittest` for structured assertions
- Separate I/O from logic for testability
- Validate and sanitize inputs defensively

## Task Index

| File                    | Purpose                                        |
| ----------------------- | ---------------------------------------------- |
| `0-add_integer.py`      | Add two numbers with type checks               |
| `2-matrix_divided.py`   | Divide matrix elements safely                  |
| `3-say_my_name.py`      | Format name with validation                    |
| `4-print_square.py`     | Print square using `#`                         |
| `5-text_indentation.py` | Reformat text after punctuation                |
| `6-max_integer.py`      | Return max integer                             |
| `tests/`                | Doctest `.txt` specs & `6-max_integer_test.py` |

## Usage

```bash
python3 -m doctest -v tests/*.txt
python3 -m unittest tests/6-max_integer_test.py
```

## Key Concepts

- Deterministic pure functions ease testing
- Early failing tests clarify required behavior
- Input validation prevents silent logical errors

## Testing / Validation

Run doctests for quick syntax/behavior checks, then targeted `unittest` for edge cases (empty list, single element, negatives, non‑int inputs triggering errors).

## Resources

See `resources.md` for TDD guides and Python testing docs.

## Reflection

TDD here enforces deliberate API design and encourages small, composable functions.
