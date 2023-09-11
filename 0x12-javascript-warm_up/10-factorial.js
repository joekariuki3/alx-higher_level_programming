#!/usr/bin/node
// factorial using recission

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log(1);
} else {
  function factorial (a) {
    if (a === 0) {
      return 1;
    }
    return a * factorial(a - 1);
  }
  console.log(factorial(num));
}
