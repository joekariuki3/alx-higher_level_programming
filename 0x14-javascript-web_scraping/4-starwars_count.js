#!/usr/bin/node
// script to print number of movies a character is in

const request = require('request');

function printmovie (url, urluser) {
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
        if (character === urluser) {
          count++;
        }
      }
    }
    console.log(count);
  });
}
if (process.argv[2]) {
  const url = process.argv[2];
  const urluser = 'https://swapi-api.alx-tools.com/api/people/18/';
  printmovie(url, urluser);
}
