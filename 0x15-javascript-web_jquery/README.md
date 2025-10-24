## 0x15. JavaScript — Web jQuery

> DOM selection, manipulation, event handling, and lightweight AJAX with jQuery.

## Overview

Pairs HTML scaffolds with incremental scripts to practice dynamic UI updates, list mutations, event-driven logic, and API data injection into the DOM.

## Learning Objectives

- Select & manipulate DOM elements efficiently
- Bind events & manage callbacks
- Fetch remote JSON & update UI (AJAX)
- Create, append, and remove DOM nodes
- Manage class lists & text content changes
- Understand jQuery convenience vs vanilla JS equivalents

## Task Index

Representative page/script pairs:

| Pair                              | Purpose                        |
| --------------------------------- | ------------------------------ |
| `0-main.html` / `0-script.js`     | Update header text             |
| `1-main.html` / `1-script.js`     | Toggle class on header         |
| `2-main.html` / `2-script.js`     | Add class to element           |
| `3-main.html` / `3-script.js`     | Add `<li>` element to list     |
| `4-main.html` / `4-script.js`     | Remove last `<li>`             |
| `5-main.html` / `5-script.js`     | Append new `<li>` on click     |
| `6-main.html` / `6-script.js`     | Update text via input          |
| `7-main.html` / `7-script.js`     | Fetch & display character name |
| `8-main.html` / `8-script.js`     | Fetch & list film titles       |
| `9-main.html` / `9-script.js`     | Fetch & display translation    |
| `100-main.html` / `100-script.js` | Advanced chain of updates      |
| `101-main.html` / `101-script.js` | Additional dynamic behaviors   |
| `102-main.html` / `102-script.js` | More complex DOM ops           |
| `103-main.html` / `103-script.js` | Combined features showcase     |

## Usage

Open the HTML files in a browser with network access (or host locally) and ensure jQuery is loaded (typically via CDN). Interact with buttons/inputs per task description.

## Key Concepts

- Event delegation vs direct binding (scalability)
- Minimizing layout thrashing when manipulating DOM
- Progressive enhancement (behavior layered atop markup)

## Testing / Validation

- Verify DOM changes occur idempotently on repeated actions
- Simulate slow network responses for AJAX sections (check loading state if implemented)
- Confirm elements added/removed leave no orphan event handlers

## Resources

See `resources.md` for jQuery API and DOM references.

## Reflection

Provides a fast, expressive path to interactive pages while developing an intuition for DOM change costs and event choreography—useful when later evaluating modern frameworks.
