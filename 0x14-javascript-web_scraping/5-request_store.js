#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./script.js <URL> <file_path>');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch URL: ${response.statusCode}`);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(`Failed to write to file: ${err.message}`);
      process.exit(1);
    }
    console.log(`Successfully saved response to ${filePath}`);
  });
});
