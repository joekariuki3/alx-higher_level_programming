## 0x00. Python — Hello, World

> First contact with Python: execution modes, basic I/O, formatting, and a glimpse under the hood (bytecode + a C helper).

## Overview

Establishes the mechanics of running Python in multiple ways (inline, file, executable script), reinforces clean output formatting, and introduces minimal introspection + a supporting C snippet to encourage awareness of lower-level representations early.

## Learning Objectives

- Run Python via script file, inline env var, and executable bit
- Understand role of the interpreter & `.pyc` bytecode
- Use print formatting for strings, ints, floats
- Perform slicing & concatenation idiomatically
- Compile & inspect simple bytecode (`dis` module)
- Build/compile a tiny C helper (`check_cycle`)

## Task Index

| File / Script              | Purpose                                         |
| -------------------------- | ----------------------------------------------- |
| `0-run`                    | Execute a Python file referenced by `$PYFILE`   |
| `1-run_inline`             | Execute Python code stored in `$PYCODE` env var |
| `2-print.py`               | Basic string output                             |
| `3-print_number.py`        | Integer printing & formatting                   |
| `4-print_float.py`         | Float precision formatting                      |
| `5-print_string.py`        | Repetition & slicing demonstration              |
| `6-concat.py`              | String concatenation into sentence              |
| `7-edges.py`               | Indexing & slice practice                       |
| `8-concat_edges.py`        | Construct phrase through slices                 |
| `9-easter_egg.py`          | Prints the Zen of Python                        |
| `10-check_cycle.c`         | Linked list cycle detection (C)                 |
| `lists.h`                  | Struct & prototype for cycle helper             |
| `100-write.py`             | Direct write to stderr/file descriptor          |
| `101-compile`              | Produce bytecode from source                    |
| `102-magic_calculation.py` | Recreate logic from given bytecode              |
| `resources.md`             | Curated references & notes                      |

## Usage

```bash
python3 2-print.py
chmod +x 0-run && ./0-run
export PYCODE='print("Inline!" )' && ./1-run_inline
gcc -Wall -Werror -Wextra -pedantic 10-check_cycle.c lists.h -o check_cycle
```

## Key Concepts

- Multiple execution pathways reinforce environment understanding
- Formatting vs concatenation tradeoffs
- Early exposure to bytecode fosters curiosity about internals
- Simple C interplay contextualizes Python abstractions

## Testing / Validation

- Manual stdout comparison for early scripts
- `python3 -m py_compile` or `dis.dis()` for bytecode tasks
- Compile C helper with strict flags; run against crafted cyclic / acyclic lists

## Resources

See `resources.md` for official docs, articles, and distilled notes.

## Reflection

Clarity > cleverness at this stage; patterns here seed consistency for later, more complex modules.
