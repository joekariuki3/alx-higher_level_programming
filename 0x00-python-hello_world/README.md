# 0x00. Python - Hello, World

Foundational introduction to Python syntax, execution models, basic I/O, string manipulation, and simple compilation/bytecode concepts.

## 📌 Learning Objectives

By the end of this project I could explain:

- How to run Python scripts in different ways (`python3 file.py`, inline, executable bit)
- What the Python interpreter does
- The role of the `.pyc` / bytecode and how to inspect it (briefly)
- Basic printing, string literals, escaping, and concatenation
- Simple integer and float formatting
- How to write and run a simple C function helper (cycle checking)

## 📂 Files

| File                       | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| `0-run`                    | Shell script to run a Python script stored in `$PYFILE`       |
| `1-run_inline`             | Shell script to execute Python code from an env var `$PYCODE` |
| `2-print.py`               | Prints a simple string in Python                              |
| `3-print_number.py`        | Demonstrates printing integers with f-strings / format        |
| `4-print_float.py`         | Formats a float to specific precision                         |
| `5-print_string.py`        | String repetition & slicing basics                            |
| `6-concat.py`              | Concatenates strings into a full sentence                     |
| `7-edges.py`               | String indexing and slicing practice                          |
| `8-concat_edges.py`        | Advanced slicing to build a phrase                            |
| `9-easter_egg.py`          | Prints “The Zen of Python” via `this` module                  |
| `10-check_cycle.c`         | C function to detect linked list cycle (with `lists.h`)       |
| `100-write.py`             | Writes output to stderr / file descriptor usage               |
| `101-compile`              | Script to compile Python file to bytecode                     |
| `102-magic_calculation.py` | Function stub matching given bytecode                         |
| `lists.h`                  | Header for singly linked list structure used in cycle check   |
| `resources.md`             | curated learning links                                        |

## 🛠 Usage Examples

```bash
python3 2-print.py
./0-run        # if executable
./1-run_inline # after exporting PYCODE
```

## 🔍 Notable Concepts

- Importance of readable output formatting
- Distinction between printing vs returning values
- Intro to debugging using prints

## 🧪 Validation

Manual comparison of outputs against expected results. Bytecode tasks verified with `python3 -m py_compile` or `python3 -c 'import dis; dis.dis(...)'`.

## 🚧 Potential Improvements

- Include a tiny Python unit test for formatting scripts

## 📎 Resources

See `resources.md` for references used.

## 🗒 Reflection

This project set the tone for emphasizing clarity and Pythonic idioms early on.

---
