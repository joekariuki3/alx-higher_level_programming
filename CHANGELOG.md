# Changelog

All notable documentation changes for this repository are tracked here. (Semantic versioning is not applied since this is a learning workspace; entries are chronological.)

## 2025-10-08

### Added

- Introduced `Documentation Conventions` section in root `README.md` clarifying structure, tone, and formatting rules.
- Added `CONTRIBUTING.md` with guidelines on pedagogy principles, linting (Black, Ruff, ESLint, Prettier), markdown lint suggestions, and commit message style.
- Created initial `CHANGELOG.md` to record doc evolution going forward.

### Changed

- Standardized every subproject `README.md` to a unified structure (Overview, Learning Objectives, Task Index, Usage, Key Concepts, Testing / Validation, Resources, Reflection).
- Strengthened Reflection sections across directories to emphasize transferable reasoning (trade-offs, abstraction benefits, error handling discipline) rather than restating objectives.
- Removed informal emoji headings for a cleaner diff footprint and accessibility.
- Eliminated residual phrases referencing internal generation mechanics; documentation is now written as canonical source.

### Fixed

- Inconsistent wording across networking and ORM READMEs (aligned terminology: "raw SQL", "parameterized query", "HTTP verbs", "aggregation").
- Minor heading level inconsistencies and extraneous trailing notes.

### Notes

- Future doc improvements (testing examples, diagrams, CI lint integration) will be captured in subsequent entries.
