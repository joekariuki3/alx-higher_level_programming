## 0x02. Python - import & modules

Focus on modularity, namespace management, argument handling from CLI, and dynamic imports.

## 📌 Learning Objectives

- Why modules matter (reuse, organization)
- Using `import`, `from ... import`, and aliasing
- Discovering available names via `dir()`
- Executing code conditionally under `if __name__ == "__main__":`
- Parsing command-line arguments (`sys.argv`)
- Basics of creating a custom module

## 📂 Files

| File                       | Description                                 |
| -------------------------- | ------------------------------------------- |
| `0-add.py`                 | Imports a function and prints sum           |
| `1-calculation.py`         | Imports multiple arithmetic functions       |
| `2-args.py`                | Prints argument count & list                |
| `3-infinite_add.py`        | Adds all integer arguments                  |
| `4-hidden_discovery.py`    | Lists names in a module excluding dunders   |
| `5-variable_load.py`       | Imports variable from module and prints it  |
| `100-my_calculator.py`     | CLI calculator dispatching operations       |
| `101-easy_print.py`        | One-liner print using external module trick |
| `102-magic_calculation.py` | Matches given bytecode behavior             |
| `103-fast_alphabet.py`     | Efficient alphabet printing                 |
| `hidden_4.pyc`             | Compiled Python bytecode (ignored in logic) |

## 🔍 Notable Techniques

- Avoiding wildcard imports to preserve clarity
- Leveraging `sys.modules` understanding (intro level)
- Encapsulation of logic behind `__name__ == '__main__'`

## 🧪 Validation

Invoke scripts with various arguments and compare outputs to specifications.

## 📎 Resources

See `resources.md` for reading list (imports, packaging basics).

## 🗒 Reflection

This unit emphasized controlling execution side effects and reusability.

---
