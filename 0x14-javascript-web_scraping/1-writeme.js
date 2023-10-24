#!/usr/bin/node
// write a strinf to a file
// file name is pased as 1st urgument n sting as 2nd argument

const fs = require('fs').promises;

async function writeFile (filename, string) {
  try {
    await fs.writeFile(filename, string, 'utf8');
  } catch (error) {
    console.error(error);
  }
}
writeFile(process.argv[2], process.argv[3]);
