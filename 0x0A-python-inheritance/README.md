## 0x0A. Python — Inheritance

> Constructing hierarchies, extending behavior, and leveraging polymorphism.

## Overview

Covers base vs derived responsibilities, safe type introspection, validation reuse, and controlled attribute extension—building toward composable abstractions.

## Learning Objectives

- Use `isinstance` vs `issubclass` accurately
- Understand (intro) MRO implications
- Override vs extend method behavior
- Provide validator helpers to reduce duplication
- Enforce abstraction via placeholder / raising methods

## Task Index

| File                    | Purpose                       |
| ----------------------- | ----------------------------- |
| `0-lookup.py`           | Introspect attributes/methods |
| `1-my_list.py`          | Augmented list subclass       |
| `2-is_same_class.py`    | Exact class comparison        |
| `3-is_kind_of_class.py` | Inheritance-aware check       |
| `4-inherits_from.py`    | True only for subclasses      |
| `5-base_geometry.py`    | Empty geometric base          |
| `6-base_geometry.py`    | Add `area` placeholder        |
| `7-base_geometry.py`    | Integer validator helper      |
| `8-rectangle.py`        | Rectangle subclass validate   |
| `9-rectangle.py`        | Area & string formatting      |
| `10-square.py`          | Square specialization         |
| `11-square.py`          | Extended square string repr   |
| `100-my_int.py`         | Int subclass w/ inverted ops  |
| `101-add_attribute.py`  | Dynamic attribute addition    |

## Usage

```bash
python3 11-square.py
```

## Key Concepts

- LSP (substitutability) in practice
- DRY validation via base helpers
- Safe dynamic attribute extension

## Testing / Validation

Create instances of each class, test inheritance predicates, and ensure invalid geometry raises errors.

## Resources

See `resources.md` for inheritance design guidelines & MRO references.

## Reflection

Illustrates trade-offs between depth of reuse and complexity. Encourages designing minimal, stable base contracts while deferring specialization—skills that scale when introducing mixins, multiple inheritance, or interface-style abstractions later.

---
