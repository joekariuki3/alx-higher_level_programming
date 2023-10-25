#!/usr/bin/node
// script to print number of movies a character is in

const request = require('request');

function printmovie (url, userId) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    let count = 0;
    let alljsondata = JSON.parse(body);
    alljsondata = alljsondata.results;
    for (let i = 0; i < alljsondata.length; i++) {
      const characters = alljsondata[i].characters;
      for (let j = 0; j < characters.length; j++) {
        const character = characters[j];
        const charList = character.split('/');
        if (charList.includes(userId)) {
          count++;
        }
      }
    }
    console.log(count);
  });
}
if (process.argv[2]) {
  const url = process.argv[2];
  const userId = '18';
  printmovie(url, userId);
}
