## 0x08. Python — More Classes & Objects

> Richer class design with `Rectangle`, class/static methods, and an algorithmic detour (`101-nqueens.py`).

## Overview

Extends OOP depth: representation, lifecycle (`__del__`), class vs instance state, alternative constructors, and a classic backtracking problem to reinforce abstraction and recursion.

## Learning Objectives

- Distinguish `__str__` vs `__repr__`
- Implement class vs static methods appropriately
- Track instance count via class attribute
- Provide flexible constructors (`@classmethod` factories)
- Apply backtracking for N Queens

## Task Index

| File             | Purpose                        |
| ---------------- | ------------------------------ |
| `0-rectangle.py` | Skeleton class                 |
| `1-rectangle.py` | Width/height initialization    |
| `2-rectangle.py` | Area & perimeter               |
| `3-rectangle.py` | User‑friendly `__str__`        |
| `4-rectangle.py` | Reproducible `__repr__`        |
| `5-rectangle.py` | Deletion hook message          |
| `6-rectangle.py` | Instance counter               |
| `7-rectangle.py` | Custom print symbol            |
| `8-rectangle.py` | Area comparison (staticmethod) |
| `9-rectangle.py` | Square factory (classmethod)   |
| `101-nqueens.py` | N Queens solver                |

## Usage

```bash
python3 9-rectangle.py
python3 101-nqueens.py 4
```

## Key Concepts

- Class vs instance scope separation
- Alternate constructors for clarity
- Backtracking search pattern

## Testing / Validation

Invalid dimensions raise errors; verify instance counter increments/decrements; solve N=4, N=5 for correctness.

## Resources

See `resources.md` for OOP deep dives & backtracking references.

## Reflection

Shows evolution from structural classes to behavior-rich, reusable abstractions. Reinforces disciplined state management (class vs instance), encourages thoughtful public API design, and previews algorithmic problem solving integration with OOP.
