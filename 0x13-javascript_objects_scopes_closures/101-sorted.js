#!/usr/bin/node
// import a dict of occurence by user id and compute a dict of users id by occurence

const dict = require('./101-data.js').dict;
const newDict = {};
let key = '';
let val = '';
for ([key, val] of Object.entries(dict)) {
  newDict[val] = [];
}
for ([key, val] of Object.entries(dict)) {
  if (val in newDict) {
    newDict[val].push(key);
  }
}
console.log(newDict);
