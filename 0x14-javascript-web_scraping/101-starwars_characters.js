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

  // Iterate through each character URL and print their names
  const charactersUrls = film.characters;
  const charactersNames = [];

  function fetchCharacter (index) {
    if (index === charactersUrls.length) {
      // All characters fetched, print their names
      charactersNames.forEach(name => console.log(name));
      return;
    }

    request.get(charactersUrls[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
        process.exit(1);
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character:', charResponse.statusCode);
        process.exit(1);
      }

      const character = JSON.parse(charBody);
      charactersNames.push(character.name);

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  }

  fetchCharacter(0);
});
