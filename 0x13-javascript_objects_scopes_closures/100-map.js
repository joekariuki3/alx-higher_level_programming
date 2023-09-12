#!/usr/bin/node
// import an array and compute a new array

const list = require('./100-data.js').list;

const newList = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
