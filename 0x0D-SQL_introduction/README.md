## 0x0D. SQL — Introduction

> Foundational relational concepts: schema creation, basic querying, and simple aggregation.

## Overview

Covers essential DDL/DML operations used to define tables, insert rows, and query/filter data. Establishes habits (idempotent creation, UTF‑8 readiness) for clean database setup.

## Learning Objectives

- Distinguish databases, tables, rows
- Use basic DDL (CREATE, DROP) safely
- Perform simple DML (SELECT, INSERT, UPDATE, DELETE)
- Filter, order, and count result sets
- Understand charset/UTF‑8 migration considerations

## Task Index (Representative)

| File                               | Purpose                      |
| ---------------------------------- | ---------------------------- |
| `0-list_databases.sql`             | List databases               |
| `1-create_database_if_missing.sql` | Idempotent DB creation       |
| `2-remove_database.sql`            | Conditional drop             |
| `3-list_tables.sql`                | List tables                  |
| `4-first_table.sql`                | Create table                 |
| `5-full_table.sql`                 | Show table schema            |
| `6-list_values.sql`                | Select all rows              |
| `7-insert_value.sql`               | Insert row                   |
| `8-count_89.sql`                   | Conditional count            |
| `9-full_creation.sql`              | Create + populate end‑to‑end |
| `10-top_score.sql`                 | Order by score desc          |
| `14-average.sql`                   | Compute average              |
| `15-groups.sql`                    | GROUP BY aggregation         |
| `100-move_to_utf8.sql`             | Charset conversion           |
| `101-avg_temperatures.sql`         | Aggregation over dataset     |
| `102-top_city.sql`                 | Top city by metric           |
| `103-max_state.sql`                | State with max value         |

## Usage

```bash
mysql -u root -p < 0-list_databases.sql
```

## Key Concepts

- Idempotent operations ease reruns
- Aggregate queries summarize large sets
- Charset consistency prevents encoding issues

## Testing / Validation

Run scripts in order, verify schema with `DESCRIBE`, compare row counts. For UTF‑8 migration, inspect `SHOW VARIABLES LIKE 'character_set_%';`.

## Resources

See `resources.md` for SQL introductory references.

## Reflection

Provides minimal relational literacy required for subsequent ORM abstraction. Establishes disciplined habits (idempotency, charset awareness) that reduce migration friction and production misconfiguration later.
