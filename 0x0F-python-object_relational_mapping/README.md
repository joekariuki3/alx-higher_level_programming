## 0x0F. Python — Object Relational Mapping (ORM)

> Bridging raw SQL to Python abstractions using MySQLdb and SQLAlchemy.

## Overview

Transitions from direct SQL scripting to declarative models. Demonstrates safe parameterization, model class definitions, relationship mapping, and when falling back to raw SQL is pragmatic.

## Learning Objectives

- Connect to MySQL from Python
- Execute parameterized queries safely
- Define SQLAlchemy models & metadata
- Map one‑to‑many relationships
- Perform CRUD & filtered queries via ORM
- Recognize when raw SQL may outperform ORM

## Task Index (Representative)

| File                                | Purpose                    |
| ----------------------------------- | -------------------------- |
| `0-select_states.py`                | List states (raw)          |
| `1-filter_states.py`                | Filter by letter           |
| `2-my_filter_states.py`             | Unsafe filtering example   |
| `3-my_safe_filter_states.py`        | Parameterized safety       |
| `4-cities_by_state.py`              | Join states & cities       |
| `6-model_state.py`                  | SQLAlchemy model           |
| `7-model_state_fetch_all.py`        | ORM query all              |
| `8-model_state_fetch_first.py`      | First row                  |
| `9-model_state_filter_a.py`         | Filtered query             |
| `11-model_state_insert.py`          | Insert record              |
| `12-model_state_update_id_2.py`     | Update record              |
| `13-model_state_delete_a.py`        | Delete records             |
| `14-model_city_fetch_by_state.py`   | Relationship query         |
| `relationship_state.py`             | Relationship model (state) |
| `relationship_city.py`              | Relationship model (city)  |
| `100-relationship_states_cities.py` | Create related objects     |

## Usage

```bash
python3 7-model_state_fetch_all.py root password db_name
```

## Key Concepts

- ORM adds abstraction & safety (but not magic)
- Session patterns manage transactions
- Relationship helpers simplify navigation

## Testing / Validation

Set up a test DB; run raw vs ORM queries to ensure parity. Inject unsafe input into unsafe script to illustrate risk; contrast with parameterized variant.

## Resources

See `resources.md` for SQLAlchemy docs & parameterization guidance.

## Reflection

Elevates database work from ad hoc scripts to maintainable, testable data access layers. Clarifies ORM strengths (productivity, safety) while acknowledging when targeted raw SQL remains the pragmatic choice.
