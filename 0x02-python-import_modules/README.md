## 0x02. Python — Import & Modules

> Building modular programs: organizing code, controlling namespaces, and handling CLI arguments.

## Overview

Introduces splitting logic across files, safe entry points, argument parsing via `sys.argv`, and dynamic symbol discovery. Reinforces avoiding namespace pollution while enabling reuse.

## Learning Objectives

- Use `import`, selective `from ... import`, and aliases
- Inspect available names with `dir()`
- Protect executable blocks with `if __name__ == "__main__":`
- Parse command‑line arguments (`sys.argv` basics)
- Structure a lightweight calculator dispatcher

## Task Index

| File                       | Purpose                               |
| -------------------------- | ------------------------------------- |
| `0-add.py`                 | Import function & print sum           |
| `1-calculation.py`         | Import multiple arithmetic functions  |
| `2-args.py`                | Print argument count & list           |
| `3-infinite_add.py`        | Sum all integer args                  |
| `4-hidden_discovery.py`    | List non‑dunder names                 |
| `5-variable_load.py`       | Import variable and display           |
| `100-my_calculator.py`     | CLI operation dispatcher              |
| `101-easy_print.py`        | Indirect print via module side effect |
| `102-magic_calculation.py` | Recreate logic from bytecode          |
| `103-fast_alphabet.py`     | Efficient alphabet output             |

## Usage

```bash
python3 3-infinite_add.py 10 20 7
python3 100-my_calculator.py 3 + 5
```

## Key Concepts

- Explicit imports > wildcard clarity
- Entry point guard prevents unintended execution
- Dynamic discovery encourages introspection skills

## Testing / Validation

Run scripts with varying argument counts, invalid operators for calculator, and verify graceful error messaging.

## Resources

See `resources.md` for import system references & packaging primers.

## Reflection

Modularity here lays the foundation for maintainability and future packaging.
