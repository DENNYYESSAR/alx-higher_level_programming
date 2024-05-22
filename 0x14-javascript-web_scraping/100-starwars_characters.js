#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./script.js <Movie_ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch API:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);

  console.log(`Characters in "${film.title}":`);
  film.characters.forEach(characterUrl => {
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        process.exit(1);
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character:', charResponse.statusCode);
        process.exit(1);
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
