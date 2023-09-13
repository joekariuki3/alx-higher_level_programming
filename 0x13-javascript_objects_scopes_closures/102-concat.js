#!/usr/bin/node
// read data from file 1 and file to then write to file 3
// import required package to read file that is fs
const fs = require('fs');

const argv = process.argv;
if (argv.length < 5) {
  console.log('Usage: <script> fileA fileB fileC');
} else {
// get the files to read from and write to
  const file1 = process.argv[2];
  const file2 = process.argv[3];
  const file3 = process.argv[4];

  // read from first file
  fs.readFile(file1, function (err, buff) {
    if (err) {
      console.log('error reading Data of file 1');
    }
    const file1Data = buff.toString();
    // write first file data to file3
    fs.writeFile(file3, file1Data, function (err) {
      if (err) {
        console.log('error writing file1Data to file 2');
      }
    });
  });

  // read from 2nd file
  fs.readFile(file2, function (err, buff) {
    if (err) {
      console.log('error reading Data of file 2');
    }
    const file2Data = buff.toString();
    // append 2nd file data to file 3
    fs.appendFile(file3, file2Data, function (err) {
      if (err) {
        console.log('error writing file2Data to file 2');
      }
    });
  });
}
