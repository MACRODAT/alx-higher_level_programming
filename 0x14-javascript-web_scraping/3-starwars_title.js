#!/usr/bin/node
// title of a mmovie where the episode id

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
