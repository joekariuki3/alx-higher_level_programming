## 0x0E. SQL — More Queries

> Intermediate SQL: constraints, privileges, relationships, joins, grouping, and conditional aggregation.

## Overview

Builds on basics with schema constraints, user management, foreign keys, join strategies, and reporting queries. Reinforces normalized design thinking and query readability.

## Learning Objectives

- Create users & grant least‑privilege access
- Apply NOT NULL, UNIQUE, default values
- Define foreign keys & maintain referential integrity
- Compare INNER JOIN vs subquery approaches
- Aggregate & group with filtering (HAVING)

## Task Index (Selection)

| File                          | Purpose              |
| ----------------------------- | -------------------- |
| `0-privileges.sql`            | Show user privileges |
| `1-create_user.sql`           | Create basic user    |
| `2-create_read_user.sql`      | Read‑only user       |
| `3-force_name.sql`            | Enforce NOT NULL     |
| `4-never_empty.sql`           | Set default value    |
| `5-unique_id.sql`             | Unique constraint    |
| `6-states.sql`                | States table         |
| `7-cities.sql`                | Cities table w/ FK   |
| `9-cities_by_state_join.sql`  | Join example         |
| `10-genre_id_by_show.sql`     | Relationship query   |
| `13-count_shows_by_genre.sql` | Group count          |
| `16-shows_by_genre.sql`       | Full listing         |
| `100-not_my_genres.sql`       | Exclusion logic      |
| `102-rating_shows.sql`        | Ratings aggregation  |

## Usage

```bash
mysql -u root -p < 9-cities_by_state_join.sql
```

## Key Concepts

- Constraints as first line of data quality defense
- Joins vs subqueries trade‑offs (clarity vs flexibility)
- Aggregations + HAVING for analytical queries

## Testing / Validation

Attempt inserting invalid FK rows (expect failure), test uniqueness violations, compare join vs subquery results for equivalence.

## Resources

See `resources.md` for relational modeling & indexing guides.

## Reflection

Solidifies mental model necessary to appreciate ORM abstractions. Reinforces that declarative constraints are cheaper and more reliable than scattered application logic checks.
