## 0x01. Python — if/else, loops, functions

> Core control flow patterns + first reusable functions; shifts thinking from linear code to structured branching.

## Overview

Builds fluency with conditional logic, looping constructs, and encapsulation of behavior inside functions. Introduces small algorithmic patterns (classification, formatting, numeric transforms) and a C helper to reinforce data handling rigor.

## Learning Objectives

- Differentiate `if` / `elif` / `else` roles
- Choose `for` vs `while` appropriately
- Use `range()` idiomatically (bounds, step, reverse)
- Handle modulo & negatives correctly
- Define simple, pure functions (parameters, returns)
- Apply loops to string & numeric processing

## Task Index

| File                        | Purpose                                      |
| --------------------------- | -------------------------------------------- |
| `0-positive_or_negative.py` | Classify sign of random integer              |
| `1-last_digit.py`           | Extract & evaluate last digit                |
| `2-print_alphabet.py`       | Print lowercase alphabet                     |
| `3-print_alphabt.py`        | Alphabet excluding specific letters          |
| `4-print_hexa.py`           | Decimal ↔ hex pairs formatting               |
| `5-print_comb2.py`          | All numbers 00–99 (padded)                   |
| `6-print_comb3.py`          | Unique ascending digit pairs                 |
| `7-islower.py`              | Implement lowercase predicate                |
| `8-uppercase.py`            | Manual uppercase conversion                  |
| `9-print_last_digit.py`     | Print & return last digit                    |
| `10-add.py`                 | Integer addition function                    |
| `11-pow.py`                 | Power function implementation                |
| `12-fizzbuzz.py`            | Classic FizzBuzz logic                       |
| `13-insert_number.c`        | Insert node in sorted singly linked list (C) |
| `100-print_tebahpla.py`     | Reverse alternating case alphabet            |
| `101-remove_char_at.py`     | Copy string without specific index           |
| `102-magic_calculation.py`  | Reproduce given bytecode behavior            |
| `resources.md`              | Curated control flow references              |

## Usage

```bash
python3 12-fizzbuzz.py
python3 4-print_hexa.py
gcc -Wall -Werror -Wextra -pedantic 13-insert_number.c lists.h -o insert && ./insert
```

## Key Concepts

- Branch coverage & guarding against off‑by‑one
- Single‑responsibility function design
- Loop patterns: counting, filtering, pair generation
- Manual case conversion to internalize ASCII logic

## Testing / Validation

REPL assertions for predicates & arithmetic helpers. Edge cases: zero, negatives, upper boundaries (e.g. 99), non‑alphabet characters. C insertion validated with sorted list sequences and head/tail insert scenarios.

## Resources

See `resources.md` for deeper dives into control flow and function basics.

## Reflection

This module converts raw syntax familiarity into disciplined branching + iteration habits foundational for later algorithmic work.
