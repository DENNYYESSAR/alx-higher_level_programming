#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter(film =>
      film.characters.some(characterUrl => characterUrl.includes('/18/'))
    ).length;
    console.log(count);
  }
});
