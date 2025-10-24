## 0x13. JavaScript — Objects, Scopes & Closures

> Deepening understanding of object construction, prototypes, inheritance, lexical scoping, and closures.

## Overview

Progressively enhances a Rectangle/Square abstraction while exploring prototype methods, inheritance patterns, closures for encapsulation, and functional utilities over arrays & objects.

## Learning Objectives

- Define constructor functions / ES5 style classes
- Attach & share methods via `prototype`
- Validate constructor parameters defensively
- Extend behavior (Square from Rectangle) without duplication
- Understand lexical scope & closure persistence
- Use closures to capture state (counters, converters)
- Perform file concatenation & object reorganization

## Task Index

| File               | Purpose                              |
| ------------------ | ------------------------------------ |
| `0-rectangle.js`   | Empty Rectangle constructor scaffold |
| `1-rectangle.js`   | Add width/height initialization      |
| `2-rectangle.js`   | Input validation guard clauses       |
| `3-rectangle.js`   | Instance method for printing shape   |
| `4-rectangle.js`   | Add rotate & double methods          |
| `5-square.js`      | Inherit from Rectangle (Square)      |
| `6-square.js`      | Extend Square with charPrint method  |
| `7-occurrences.js` | Count occurrences in list            |
| `8-esrever.js`     | Reverse list algorithmically         |
| `9-logme.js`       | Closure counting function calls      |
| `10-converter.js`  | Base converter factory (closure)     |
| `100-map.js`       | Transform list with map & index      |
| `101-sorted.js`    | Reindex dictionary by value          |
| `102-concat.js`    | Concatenate two files sequentially   |

## Usage

```bash
node 5-square.js
node 10-converter.js 15
```

## Key Concepts

- Prototypes share implementation across instances (memory & speed)
- Inheritance via prototype chain vs composition trade‑offs
- Closures enable private state (counters, configuration)
- Separation of data transformation (`map`, custom utilities) from I/O

## Testing / Validation

- Instantiate shapes with invalid dimensions (0, negative, non‑numeric) to confirm guards
- Verify prototype methods appear once across instances (`Object.getPrototypeOf`)
- Check closure counters increment predictably across multiple calls
- File concat: confirm order and newline handling

## Resources

See `resources.md` for prototype & closure references.

## Reflection

Bridges procedural basics to more expressive patterns that underpin modular & scalable JavaScript design.
