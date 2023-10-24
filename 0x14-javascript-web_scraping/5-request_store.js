#!/usr/bin/node
// script that gets data from website and saves it in a file
// first argument id the url
// the second argument is path to store the body response

const request = require('request');
const fs = require('fs').promises;

// funtion to write data to a file
async function writeFile (filename, data) {
  try {
    await fs.writeFile(filename, data, 'utf8');
  } catch (error) {
    console.log(error);
  }
}
// function to get data from the page
function getPageData (url, filename) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    // call writefile function to save body to a file
    writeFile(filename, body);
  });
}

if ((process.argv).length > 3) {
  const url = process.argv[2];
  const filename = process.argv[3];
  getPageData(url, filename);
}
