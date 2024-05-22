#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./script.js <API_URL>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch API: ${response.statusCode}`);
    process.exit(1);
  }

  const todos = JSON.parse(body);

  // Initialize an object to store completed task counts by user ID
  const completedTasksByUser = {};

  // Count completed tasks by user ID
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print users with completed tasks in the desired format
  console.log(completedTasksByUser);
});
