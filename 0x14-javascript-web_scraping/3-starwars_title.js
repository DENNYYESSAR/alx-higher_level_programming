#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
