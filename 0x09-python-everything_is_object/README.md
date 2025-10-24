## 0x09. Python — Everything Is Object

> Understanding identity, mutability, and binding to prevent subtle bugs.

## Overview

Explores how Python names reference objects, differences between identity and equality, immutability guarantees, interning behaviors, and shallow copy nuances.

## Learning Objectives

- Distinguish `is` vs `==`
- Identify mutable vs immutable built‑ins
- Recognize small integer / string interning cases (implementation detail awareness)
- Understand argument passing (object reference semantics)
- Perform shallow copy vs simple assignment

## Task Index

Concept Q&A answer files (`*-answer.txt`) plus illustrative scripts:
| File | Purpose |
| ---- | ------- |
| `100-magic_string.py` | Stateful behavior via default / closure |
| `101-locked_class.py` | Restrict dynamic attributes (`__slots__` idea) |
| `19-copy_list.py` | Return shallow copy instead of alias |

## Usage

```bash
python3 100-magic_string.py
```

## Key Concepts

- Names bind to objects; assignment never copies by default
- Immutability allows safe reuse (interning optimizations possible)
- Limiting attributes can reduce memory & enforce API contracts

## Testing / Validation

Use `id()` comparisons, mutate copies vs originals, and confirm locked class rejects new attributes.

## Resources

See `resources.md` for CPython internals & data model references.

## Reflection

Grasping binding & mutability prevents hidden side effects (e.g., unintended shared references) and sets a mental model that improves debugging efficiency and correctness in later concurrency, networking, and persistence tasks.

---
