#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const API_URL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(API_URL, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Error:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  console.log(film.title);
});
