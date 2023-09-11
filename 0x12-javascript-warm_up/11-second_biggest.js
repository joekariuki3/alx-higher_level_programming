#!/usr/bin/node
// search for second bigest in list of arguments

const argv = process.argv;
const argvLength = argv.length;
if (argvLength < 3) {
  console.log(0);
} else if (argvLength < 4) {
  console.log(1);
} else {
  const list = [];
  for (let i = 2; i < argvLength; i++) {
    list[i - 2] = parseInt(argv[i]);
  }
  const desSortList = list.sort().reverse();
  console.log(desSortList[1]);
}
