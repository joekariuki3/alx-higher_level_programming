#!/usr/bin/node
// convert firts argument to number if its a digit

let firstArg = process.argv[2];
if (!isNaN(firstArg)) {
  firstArg = parseInt(firstArg);
  console.log('My number:' + ' ' + firstArg);
} else {
  console.log('Not a number');
}
