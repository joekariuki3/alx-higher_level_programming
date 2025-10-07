<div align="center">

# ALX Higher Level Programming

Foundational Python, SQL, and JavaScript projects completed as part of the ALX Software Engineering curriculum. This repository tracks my progression from basic syntax to object‑oriented design, data persistence, networking, testing, and higher‑level abstractions.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![SQL](https://img.shields.io/badge/SQL-MySQL-orange?logo=mysql) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript)

</div>

## 📚 Repository Structure

Each directory (`0x00*`, `0x01*`, …) is a self‑contained mini‑project focusing on one topic. Inside each you will find:

- `README.md` – detailed description of the topic, learning objectives, task summaries, usage examples
- `resources.md` – curated links (articles, docs, videos, practice) I used while learning
- Source files – Python scripts, C helpers, SQL scripts, JS programs, etc.
- (Where applicable) test files, input data, or helper headers (e.g. `lists.h`)

Example:

```
0x03-python-data_structures/
	README.md
	resources.md
	0-print_list_integer.py
	1-element_at.py
	...
```

## 🧭 Learning Roadmap (Progression Overview)

| Phase     | Focus                       | Key Concepts                                                                      |
| --------- | --------------------------- | --------------------------------------------------------------------------------- |
| 0x00–0x02 | Core Python Basics          | Printing, formatting, control flow, import/module system                          |
| 0x03–0x04 | Data Structures             | Lists, tuples, sets, dictionaries, slicing, immutability                          |
| 0x05      | Errors & Robustness         | Exceptions, raising, handling, clean exits                                        |
| 0x06–0x08 | OOP Foundations             | Classes, encapsulation, methods, inheritance, magic methods                       |
| 0x09      | Python Internals            | Object identity, mutability vs immutability, reference semantics                  |
| 0x0A–0x0C | Advanced OOP & Architecture | Inheritance chains, serialization, almost-a-circle project (review + integration) |
| 0x0D–0x0F | Data Persistence & ORM      | SQL basics, advanced queries, ORM (MySQL + Python)                                |
| 0x10–0x11 | Networking                  | HTTP fundamentals, cURL, Python requests/urllib                                   |
| 0x12–0x15 | JavaScript Foundations      | Syntax, scopes, closures, web scraping, DOM/jQuery                                |

## 🧪 Running Code

Most Python scripts are executable directly:

```
python3 0x03-python-data_structures/3-print_reversed_list_integer.py
```

Some tasks may require execution permissions:

```
chmod +x 0x00-python-hello_world/2-print.py
./0x00-python-hello_world/2-print.py
```

JavaScript exercises (Node.js required):

```
node 0x12-javascript-warm_up/0-javascript_is_amazing.js
```

SQL scripts (MySQL client required):

```
cat 0x0D-SQL_introduction/0-list_databases.sql | mysql -u root -p
```

Where C helper code exists (e.g. cycle detection), compile with:

```
gcc -Wall -Werror -Wextra -pedantic 10-check_cycle.c lists.h -o check_cycle
```

## 🧰 Environment & Tooling

- Python 3.x (CPython)
- Node.js (LTS) for JS projects
- MySQL server & client (for SQL units)
- `gcc` for occasional C helper programs
- Recommended linters: `pycodestyle` / `flake8`, `eslint`, and `shellcheck` (for any shell helpers)

## 📐 Coding Style

- Python: PEP 8 formatting, descriptive names, explicit is better than implicit
- JavaScript: ES6+ syntax, `const`/`let` appropriately, no unused vars
- SQL: Uppercase keywords, snake_case identifiers
- Commit messages: concise present tense (e.g., "Implement tuple unpacking utility")

## ✅ Testing Approach

For conceptual exercises, many scripts are self-validating via expected output. For more complex modules:

- Use REPL experiments to validate data structure operations
- Add ad hoc test harnesses when exploring edge cases
- Potential future enhancement: introduce `unittest` / `pytest` and structured test suites

## 📎 resources.md Files

Every mini‑project will include a `resources.md` file listing:

- Official documentation
- Concept articles / blog posts
- Video explanations
- Practice challenge links
- Personal notes / distilled summaries

These documents serve both as a learning trace and quick refresh reference.

## 🤝 Contributing

While this repository tracks a personal learning journey, suggestions and optimizations are welcome:

1. Fork the repo
2. Create a feature branch: `git checkout -b improve-docs`
3. Commit changes: `git commit -m "Add explanation for list slicing"`
4. Push and open a Pull Request

Please follow existing structure and style consistency.

## 🔍 Future Enhancements

- Add automated tests where logic complexity increases
- Introduce CI (GitHub Actions) for lint & style checks
- Expand `almost_a_circle` project documentation with UML diagrams
- Add performance notes for data structure operations

## 📄 License

Unless otherwise stated in specific subdirectories, this repository is released under the MIT License. See `LICENSE` (to be added if not present yet).

## 💬 Contact / Reflection

This repository is a living record of practical growth—early commits may prioritize correctness over elegance, later ones refactor toward readability and maintainability.

Feel free to open an issue if something is unclear or could use elaboration.

---

> “First, solve the problem. Then, write the code.” – John Johnson
