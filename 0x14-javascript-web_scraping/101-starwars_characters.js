#!/usr/bin/node
// script that takes an id of a movie then returns characters
// name in the movie

const request = require('request');

// get character name
function getName (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const userData = JSON.parse(body);
    const userName = userData.name;
    console.log(userName);
  });
}

// get characters
function getCharacters (id) {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    for (let i = 0; i < characters.length; i++) {
      getName(characters[i]);
    }
  });
}

if (process.argv[2]) {
  const id = process.argv[2];
  getCharacters(id);
}
