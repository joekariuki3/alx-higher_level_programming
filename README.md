<div align="center">

# Higher Level Programming (ALX Curriculum)

End‑to‑end journey through Python, SQL, and JavaScript fundamentals → data modeling → networking → higher‑level abstractions. Each numbered directory is a focused, self‑contained learning sprint.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![MySQL](https://img.shields.io/badge/DB-MySQL-orange?logo=mysql) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript) ![Status](https://img.shields.io/badge/Progress-Iterative-success?logo=github)

</div>

> This repository captures incremental skill building. Earlier solutions favor clarity & correctness; later ones introduce refactoring, efficiency, and abstraction.

## Overview

Each `0xNN-<topic>` directory contains:

- A dedicated `README.md` (objectives, task index, usage)
- `resources.md` with curated links & distilled notes
- Source code (Python / SQL / JS / occasional C helpers)
- Sometimes experiment or support files (headers, scripts)

The structure is intentionally flat so you can jump directly to any topic.

## Quick Start

Clone and explore (Python 3.x, Node.js LTS, and a local MySQL client recommended):

```bash
git clone https://github.com/joekariuki3/alx-higher_level_programming.git
cd alx-higher_level_programming
python3 0x00-python-hello_world/2-print.py
```

Run a JavaScript exercise:

```bash
node 0x12-javascript-warm_up/0-javascript_is_amazing.js
```

Execute a SQL script (example requires a configured MySQL instance):

```bash
mysql -u root -p < 0x0D-SQL_introduction/0-list_databases.sql
```

Compile an auxiliary C check (where present):

```bash
gcc -Wall -Werror -Wextra -pedantic 0x00-python-hello_world/10-check_cycle.c \
      0x00-python-hello_world/lists.h -o check_cycle
```

## Learning Progression

| Range       | Theme / Focus                     | Representative Skills                                 |
| ----------- | --------------------------------- | ----------------------------------------------------- |
| 0x00 – 0x02 | Python syntax & execution         | Printing, formatting, control flow, modules           |
| 0x03 – 0x04 | Core data structures              | Lists, tuples, sets, dicts, slicing, immutability     |
| 0x05        | Exceptions & robustness           | Raising, handling, defensive coding                   |
| 0x06 – 0x08 | Object‑oriented programming       | Classes, attributes, dunder methods, inheritance      |
| 0x09        | Python object model               | Identity, mutability, reference semantics             |
| 0x0A – 0x0C | Advanced OOP & architecture       | Inheritance depth, serialization, integration project |
| 0x0D – 0x0F | Persistence & ORM                 | SQL queries, joins, constraints, Python ↔ MySQL ORM   |
| 0x10 – 0x11 | Networking & HTTP                 | cURL, request headers, Python urllib/requests basics  |
| 0x12 – 0x15 | JavaScript fundamentals & tooling | Scopes, closures, objects, web scraping, DOM/jQuery   |

## Project Index

> The list below links topics for quick navigation. Descriptions are concise; see each sub‑README for details.

| Directory                                 | Topic (Short)       | Notes                                          |
| ----------------------------------------- | ------------------- | ---------------------------------------------- |
| `0x00-python-hello_world`                 | Intro & execution   | Interpreter basics, printing, bytecode glimpse |
| `0x01-python-if_else_loops_functions`     | Flow control        | Conditionals, loops, functions, basic algos    |
| `0x02-python-import_modules`              | Imports & modules   | Namespaces, argument parsing, dynamic import   |
| `0x03-python-data_structures`             | Sequences           | Lists & tuples operations, immutability basics |
| `0x04-python-more_data_structures`        | Sets & dicts        | Hash structures, comprehension patterns        |
| `0x05-python-exceptions`                  | Error handling      | Raising, catching, cleanup semantics           |
| `0x06-python-classes`                     | OOP I               | Class design, attributes, simple methods       |
| `0x07-python-test_driven_development`     | TDD basics          | Specifying behavior first (doctest/unittest)   |
| `0x08-python-more_classes`                | OOP II              | Richer dunder methods, encapsulation depth     |
| `0x09-python-everything_is_object`        | Object model        | Identity vs equality, mutability exploration   |
| `0x0A-python-inheritance`                 | Inheritance         | Subclassing patterns, isinstance checks        |
| `0x0B-python-input_output`                | File I/O & JSON     | Reading/writing, JSON serialization            |
| `0x0C-python-almost_a_circle`             | Integration project | Geometry classes, review, testing intro        |
| `0x0D-SQL_introduction`                   | SQL basics          | Databases, tables, simple queries              |
| `0x0E-SQL_more_queries`                   | Advanced SQL        | Joins, relationships, constraints              |
| `0x0F-python-object_relational_mapping`   | ORM bridge          | Python ↔ MySQL via ORM patterns                |
| `0x10-python-network_0`                   | HTTP shell tools    | cURL, verbs, headers, status codes             |
| `0x11-python-network_1`                   | HTTP in Python      | urllib / requests style scripting              |
| `0x12-javascript-warm_up`                 | JS syntax warmup    | Basics, first scripts                          |
| `0x13-javascript_objects_scopes_closures` | JS deeper           | Objects, scopes, closures                      |
| `0x14-javascript-web_scraping`            | Web scraping        | APIs & HTML data extraction                    |
| `0x15-javascript-web_jquery`              | DOM & jQuery        | Dynamic updates, events                        |

> [!NOTE]
> Some later directories may be added or expanded over time; check commit history for evolution.

## Style & Conventions

- Python: PEP 8, explicit readability, small focused functions
- JavaScript: ES6+, prefer `const`/`let`, no unused symbols
- SQL: Capitalized keywords, singular table naming, clear aliasing
- Commit messages: imperative mood (e.g. "Add list reversal helper")

## Documentation Conventions

- Each subdirectory README follows a consistent structure: Overview, Learning Objectives, Task Index, Usage, Key Concepts, Testing / Validation, Resources, Reflection.
- Headings use sentence case; no decorative emojis to keep diffs clean.
- Task tables: concise verb–object descriptions, no repetition of file extension intent.
- Reflection sections focus on transferable reasoning (trade‑offs, patterns) not restating objectives.
- Inline code formatting for identifiers (`function_name`, `ClassName`, SQL keywords) and backticks around commands.
- External links (where present) live in `resources.md` to decouple narrative from outbound references.
- Avoid passive voice; prefer direct instructional phrasing.
- No autogenerated notices—docs are treated as first‑class, hand‑curated artifacts.

## Running Examples

Python script:

```bash
python3 0x03-python-data_structures/3-print_reversed_list_integer.py
```

Grant + run executable (where scripts are set up that way):

```bash
chmod +x 0x00-python-hello_world/2-print.py
./0x00-python-hello_world/2-print.py
```

JavaScript:

```bash
node 0x13-javascript_objects_scopes_closures/0-rectangle.js
```

SQL (inspect schema first, then query):

```bash
mysql -u root -p < 0x0D-SQL_introduction/2-create_database_if_missing.sql
```

## Testing & Validation

Most tasks are output‑driven. Approaches used:

| Context                | Method                                                 |
| ---------------------- | ------------------------------------------------------ |
| Simple scripts         | Compare stdout with expected text                      |
| Data structure helpers | REPL spot checks & edge case probing                   |
| Bytecode tasks         | `dis` module inspection                                |
| C helpers              | Compile with strict flags, test against crafted inputs |
| SQL scripts            | Run queries, verify row counts / constraints           |

> [!TIP]
> Future enhancement: add lightweight `pytest` suites for data structure & OOP projects.

## Tooling

| Domain | Tooling                                                    |
| ------ | ---------------------------------------------------------- |
| Python | `python3`, (optionally `flake8`, `black` for local sanity) |
| JS     | Node.js LTS, optional `eslint`                             |
| SQL    | MySQL server/client                                        |
| C      | `gcc -Wall -Werror -Wextra -pedantic`                      |

## FAQ (Condensed)

**Why mix C with Python early on?** To expose lower‑level memory / structure introspection (e.g. linked list cycle checks) and appreciate Python's abstractions.

**Why no external libraries?** Intentional constraint to strengthen core language features first.

**Will tests be added?** Yes—progressively where logic benefits from regression protection.

## Roadmap / Potential Improvements

- Add CI workflow for lint + sample test runs
- Expand reflections section per directory
- Benchmark common operations (copy vs slice, tuple packing, etc.)
- Provide UML / diagrams for `almost_a_circle`

## Reflection

Learning is iterative—solutions are snapshots. Rewrites will trade didactic verbosity for brevity over time.

> “First, solve the problem. Then, write the code.” – John Johnson

---

If something looks unclear or inconsistent, open an issue or start a discussion—feedback accelerates refinement.
