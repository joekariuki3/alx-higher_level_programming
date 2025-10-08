# Contributing

Thanks for your interest in improving this learning repository. The focus is clarity, incremental progression, and consistency across languages.

## Principles

1. Optimize for pedagogy first; performance tweaks come after correctness & readability.
2. Keep diffs small and purposeful (one concern per commit when possible).
3. Prefer explicit naming over brevity.
4. Avoid adding external dependencies unless they reinforce a specific learning goal.

## Directory Structure

Each `0xNN-*` directory is self‑contained. When adding a new topic directory, include:

- `README.md` with the standard section sequence
- `resources.md` linking to authoritative docs
- Source files named with succinct numeric prefixes when part of a series

## Tooling & Linting

These tools are optional locally but recommended for consistency:

| Domain   | Tool                                     | Purpose               | Example Invocation       |
| -------- | ---------------------------------------- | --------------------- | ------------------------ |
| Python   | Black                                    | Consistent formatting | `black .`                |
| Python   | Ruff (or Flake8)                         | Lint & static checks  | `ruff check .`           |
| Python   | isort (if not using Ruff's import rules) | Import sorting        | `isort .`                |
| JS       | ESLint                                   | Code quality rules    | `npx eslint .`           |
| JS       | Prettier                                 | Formatting            | `npx prettier --check .` |
| Markdown | markdownlint-cli                         | Style consistency     | `markdownlint '**/*.md'` |

### Suggested Config Snippets

`.editorconfig` (optional):

```
root = true
[*]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
insert_final_newline = true
trim_trailing_whitespace = true
```

`pyproject.toml` (if you add one later):

```
[tool.black]
line-length = 88
target-version = ['py311']

[tool.ruff]
line-length = 88
select = ["E", "F", "I"]
```

`.eslintrc.json` (minimal):

```
{
  "env": {"es2022": true, "node": true},
  "extends": ["eslint:recommended"],
  "parserOptions": {"ecmaVersion": 2022},
  "rules": {"no-unused-vars": ["warn", {"args": "none"}]}
}
```

## Commit Messages

Format: imperative mood + concise scope.
Examples:

- `Add set intersection helper`
- `Refactor rectangle print logic`
- `Document networking reflection improvements`

Avoid batching unrelated changes. If you update docs and code, consider separate commits.

## Adding or Updating Documentation

- Maintain the established section order.
- Keep task descriptions concise (≤ 6 words when possible).
- Use backticks for identifiers and commands.
- Prefer tables for index-style listings; bullet lists for conceptual points.
- Update `CHANGELOG.md` when you make widespread documentation improvements.

## Testing Guidelines

While many tasks are output-driven, aim to add lightweight tests where logic is non-trivial:

- Python: consider `pytest` or simple `unittest` modules under a future `tests/` directory.
- JavaScript: lightweight Node assertions (future addition; no heavy frameworks unless required).

## Opening an Issue

Include:

- Context (file paths, task numbers)
- Expected vs actual behavior (if code-related)
- Proposed improvement (if documentation)

## Code of Conduct

Keep discourse constructive and focused on learning outcomes. Assume good intent; prefer clarification questions before critique.

---

Happy contributing! Iteration is the path to mastery.
