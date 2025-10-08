## 0x04. Python — More Data Structures (Set, Dict)

> Leveraging hashing structures for fast membership, counting, and transformation tasks.

## Overview

Extends sequence knowledge with sets & dictionaries, emphasizing O(1) lookups, safe mutation patterns, and functional style transformations via comprehension and mapping.

## Learning Objectives

- Perform set algebra (union, intersection, symmetric difference)
- Create/update/iterate dictionaries safely
- Use set & dict comprehensions for concise transforms
- Avoid mutating containers while iterating
- Implement basic counting/aggregation patterns

## Task Index

| File                           | Purpose                              |
| ------------------------------ | ------------------------------------ |
| `0-square_matrix_simple.py`    | Map over matrix producing new matrix |
| `1-search_replace.py`          | Replace occurrences of a value       |
| `2-uniq_add.py`                | Sum unique integers                  |
| `3-common_elements.py`         | Intersection of two sets             |
| `4-only_diff_elements.py`      | Symmetric difference                 |
| `5-number_keys.py`             | Count dictionary keys                |
| `6-print_sorted_dictionary.py` | Print dict ordered by keys           |
| `7-update_dictionary.py`       | Insert/update key:value              |
| `8-simple_delete.py`           | Safe key deletion                    |
| `9-multiply_by_2.py`           | Value doubling copy                  |
| `10-best_score.py`             | Key with max value                   |
| `11-multiply_list_map.py`      | Multiply list via map                |
| `12-roman_to_int.py`           | Roman numeral conversion             |
| `100-weight_average.py`        | Weighted average                     |
| `101-square_matrix_map.py`     | Functional matrix square             |
| `102-complex_delete.py`        | Delete keys by value match           |
| `103-python.c`                 | C exploration of object model        |

## Usage

```bash
python3 12-roman_to_int.py
python3 10-best_score.py
```

## Key Concepts

- Hash-based membership efficiency
- Defensive copying vs in-place edits
- Comprehensions for readability & performance

## Testing / Validation

Edge cases: empty set/dict, Roman subtractive pairs (`IV`, `IX`), repeated symbols, deleting non-existent keys.

## Resources

See `resources.md` for deeper algorithmic references.

## Reflection

Mastery of sets & dicts reduces algorithmic complexity in later projects.
