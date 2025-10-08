## 0x06. Python — Classes & Objects

> Progressive construction of a `Square` class illustrates encapsulation, validation, and dunder method usage.

## Overview

Introduces foundational OOP constructs in Python via iterative file progression—each adding one concern (validation, representation, comparison) to keep changes focused and traceable.

## Learning Objectives

- Define classes & instantiate objects
- Differentiate instance vs class attributes
- Use `@property` for controlled access & validation
- Implement dunder methods: `__init__`, `__str__`, `__repr__`, comparisons
- Enforce invariants (positive integers) in setters

## Task Index

| File                        | Purpose                        |
| --------------------------- | ------------------------------ |
| `0-square.py`               | Minimal empty class            |
| `1-square.py`               | Private size attr init         |
| `2-square.py`               | Size validation logic          |
| `3-square.py`               | Area computation               |
| `4-square.py`               | Property getter/setter         |
| `5-square.py`               | Textual square printing        |
| `6-square.py`               | Position offsets in print      |
| `100-singly_linked_list.py` | Sorted singly linked list impl |
| `101-square.py`             | Enhanced string form           |
| `102-square.py`             | Rich comparison by area        |

## Usage

```bash
python3 5-square.py
```

## Key Concepts

- Encapsulation via private attributes
- Data validation centralization
- Rich comparisons to enable natural ordering

## Testing / Validation

Instantiate with invalid sizes (negative, non‑int) expect `TypeError` / `ValueError`. Compare two squares for ordering semantics.

## Resources

See `resources.md` for OOP primers & property patterns.

## Reflection

Layered evolution makes each responsibility explicit and testable.
