#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const ApiEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request.get(ApiEndpoint, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const ApiMovieId = JSON.parse(body);
    console.log(ApiMovieId.title);
  }
});
