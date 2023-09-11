#!/usr/bin/node
// print square

const argument = process.argv[2];
if (isNaN(argument)) {
  console.log('Missing size');
} else {
  const argumentInt = parseInt(argument);
  for (let row = 0; row < argumentInt; row++) {
    for (let cell = 0; cell < argumentInt; cell++) {
      process.stdout.write('x');
    }
    console.log();
  }
}
