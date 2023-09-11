#!/usr/bin/node
// print first argument

const argv = process.argv;
if (!argv[2]) {
  console.log('No argument');
} else if (argv[2]) {
  console.log(argv[2]);
}
