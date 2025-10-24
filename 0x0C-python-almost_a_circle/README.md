## 0x0C. Python — Almost a Circle

> Integration project: inheritance, validation, serialization, dynamic creation, and testing across geometric models.

## Overview

Unifies earlier OOP lessons into a mini framework of base + shape subclasses. Emphasizes DRY serialization, id management, polymorphic reconstruction, and test coverage to ensure consistent behavior across evolving classes.

## Learning Objectives

- Design reusable base class (`Base`)
- Manage object identity deterministically
- Implement JSON (and CSV) serialization centrally
- Support dynamic reconstruction via class factories
- Validate and normalize constructor arguments
- Structure unit tests across inheritance chains

## Structure

| Path                             | Purpose                                     |
| -------------------------------- | ------------------------------------------- |
| `models/base.py`                 | Core id mgmt & (de)serialization helpers    |
| `models/rectangle.py`            | Rectangle with validation & area/display    |
| `models/square.py`               | Square specialization enforcing equal sides |
| `tests/test_models/`             | Unit tests for models                       |
| `Rectangle.json` / `Square.json` | Sample serialized artifacts                 |

## Usage

```bash
python3 -m unittest discover tests
```

## Key Concepts

- Central abstraction reduces duplication
- Class vs static methods for alternate constructors
- Coordinate attributes decouple presentation from size

## Testing / Validation

Run full test suite; mutate serialized files to simulate edge cases; confirm `create()` reconstructs accurate instances.

## Resources

See `resources.md` for design patterns & serialization references.

## Reflection

Mirrors real-world iterative library design: abstract → specialize → serialize → test.
