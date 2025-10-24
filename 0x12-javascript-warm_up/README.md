## 0x12. JavaScript — Warm Up

> First exposure to Node.js scripting & core JavaScript syntax fundamentals.

## Overview

Small scripts that build fluency with variables, conditionals, loops, functions, arrays, objects, and basic higher‑order patterns using Node.js.

## Learning Objectives

- Run JavaScript with Node
- Use `const` vs `let` appropriately
- Parse and validate CLI arguments via `process.argv`
- Implement loops, conditionals, recursion
- Work with arrays (iteration, searching) and objects (mutation)
- Define and export functions / modules
- Intro to higher‑order functions & callbacks

## Task Index

| File                         | Purpose                                         |
| ---------------------------- | ----------------------------------------------- |
| `0-javascript_is_amazing.js` | Print a string constant                         |
| `1-multi_languages.js`       | Multi line output                               |
| `2-arguments.js`             | Report count of CLI arguments                   |
| `3-value_argument.js`        | Print first argument or default message         |
| `4-concat.js`                | Concatenate two arguments                       |
| `5-to_integer.js`            | Convert arg to integer or say "Not a number"    |
| `6-multi_languages_loop.js`  | Loop for multi line output                      |
| `7-multi_c.js`               | Repeat a message N times                        |
| `8-square.js`                | Print square of size N with character X         |
| `9-add.js`                   | Simple addition function (CLI)                  |
| `10-factorial.js`            | Recursive factorial (graceful base cases)       |
| `11-second_biggest.js`       | Find 2nd largest integer among args             |
| `12-object.js`               | Modify object property value                    |
| `13-add.js`                  | Exported addition function (module)             |
| `100-let_me_const.js`        | Force update external variable (scope)          |
| `101-call_me_moby.js`        | Higher‑order function invoking callback N times |
| `102-add_me_maybe.js`        | Callback with incremented value                 |
| `103-object_fct.js`          | Add & invoke object method manipulating data    |

## Usage

```bash
node 8-square.js 5
node 11-second_biggest.js 1 4 2 9 3
node 101-call_me_moby.js
```

## Key Concepts

- Separation of concerns: computation vs I/O (printing)
- Defensive argument handling (missing / invalid values)
- Recursion vs iteration trade‑offs (factorial)
- Mutation vs reassignment for objects & arrays
- Intro to higher‑order functions enables later async patterns

## Testing / Validation

- Provide edge arguments: none, one, many, non‑numeric strings
- For factorial: test 0, 1, 5, large small; ensure no infinite recursion
- For second biggest: fewer than two numbers should yield expected fallback
- Lint with a basic style (if later adding ESLint) to ensure consistency

## Resources

See `resources.md` for Node runtime basics and JS syntax references.

## Reflection

Builds muscle memory for JS syntax so later object, async, and network topics focus on concepts rather than language mechanics.
