## 0x07. Python - Test-driven Development (TDD)

Introduction to specifying behavior before (or alongside) implementation using doctests and unit tests.

## 📌 Learning Objectives

- What TDD means conceptually
- Using doctest style in text files
- Structuring pure functions for easier testing
- Handling edge cases explicitly

## 📂 Files

| File                    | Description                                             |
| ----------------------- | ------------------------------------------------------- |
| `0-add_integer.py`      | Adds two ints/floats with type checks                   |
| `2-matrix_divided.py`   | Divide matrix values with validation                    |
| `3-say_my_name.py`      | Formatted name output with validation                   |
| `4-print_square.py`     | Print square of `#` characters                          |
| `5-text_indentation.py` | Format text with indentation after punctuation          |
| `6-max_integer.py`      | Return max integer (with test file)                     |
| `tests/`                | Contains `.txt` doctest specs & `6-max_integer_test.py` |

## 🧪 Testing Tools

- Doctest for simple I/O examples
- Custom unittest module usage in `6-max_integer_test.py`

## 🔍 Notable Concepts

- Defensive programming via explicit type checks
- Separation of concerns (I/O vs logic)

## 📎 Resources

See `resources.md` for TDD guides.

## 🗒 Reflection

Writing expected behavior first surfaces ambiguity earlier.
