#!/usr/bin/node
// script that uses API n prints starwar movie where episod number is passed as argument

const request = require('request');

function printmovie (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const jsondata = JSON.parse(body);
    const title = jsondata.title;
    console.log(title);
  });
}
if (process.argv[2]) {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  printmovie(url);
}
