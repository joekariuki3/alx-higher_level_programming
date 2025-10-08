## 0x03. Python — Data Structures: Lists & Tuples

> Practical exploration of Python's core sequence types with emphasis on mutability, safe modification, and idiomatic traversal.

## Overview

This module drills comfortable manipulation of ordered collections. It contrasts list mutability with tuple immutability, emphasizes when to copy vs mutate in place, and sets groundwork for later set/dict operations.

## Learning Objectives

- Distinguish lists vs tuples (mutability, typical use cases)
- Perform indexing, slicing, reversing, and safe replacement
- Avoid unintended side effects via defensive copying
- Return structured data (multiple values) via tuples
- Implement simple algorithms using sequence operations

## Task Index

| File                               | Purpose                                  |
| ---------------------------------- | ---------------------------------------- |
| `0-print_list_integer.py`          | Print integers in list (basic iteration) |
| `1-element_at.py`                  | Safe element access with bounds handling |
| `2-replace_in_list.py`             | In-place element replacement             |
| `3-print_reversed_list_integer.py` | Reverse‑order printing                   |
| `4-new_in_list.py`                 | Non‑mutating replacement (copy variant)  |
| `5-no_c.py`                        | Filter characters from string            |
| `6-print_matrix_integer.py`        | Matrix formatting output                 |
| `7-add_tuple.py`                   | Safe tuple element‑wise addition         |
| `8-multiple_returns.py`            | Tuple return (length, first char)        |
| `9-max_integer.py`                 | Manual max search                        |
| `10-divisible_by_2.py`             | Boolean mask for divisibility            |
| `11-delete_at.py`                  | Delete by index carefully                |
| `12-switch.py`                     | Swap variable values (Pythonic)          |
| `100-print_python_list_info.c`     | C introspection of list object           |

## Usage

```bash
python3 3-print_reversed_list_integer.py
python3 6-print_matrix_integer.py
gcc -Wall -Werror -Wextra -pedantic 100-print_python_list_info.c -o list_info \
	&& ./list_info
```

## Key Concepts

- Mutability & reference semantics
- Defensive copying vs in-place edits
- Sequence traversal patterns (forward, reverse, matrix)
- Tuple packing/unpacking for readable returns

## Testing / Validation

- Manual REPL checks for edge cases (empty list, single element, out-of-range index)
- Custom crafted matrices to verify formatting
- C helper compiled with strict flags; run to inspect structure metadata

## Resources

See `resources.md` for deeper dives and supporting references.

## Reflection

Mastering mutation vs copy semantics here reduces bugs in later data manipulation and algorithmic tasks.
