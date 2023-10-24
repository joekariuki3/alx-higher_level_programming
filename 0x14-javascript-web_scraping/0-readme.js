#!/usr/bin/node
// read a file and display its content.
// file path/name is pased as an urgument

const fs = require('fs').promises;

async function readFile (filename) {
  try {
    const data = await fs.readFile(filename, 'utf8');
    console.log(data.toString());
  } catch (error) {
    console.error(error);
  }
}
readFile(process.argv[2]);
