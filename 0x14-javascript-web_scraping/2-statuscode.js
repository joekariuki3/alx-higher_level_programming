#!/usr/bin/node
// script that prints status code of a GET request
// url is pased as first argument

const request = require('request');
function checkstatus (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log('code:', response.statusCode);
  });
}

checkstatus(process.argv[2]);
