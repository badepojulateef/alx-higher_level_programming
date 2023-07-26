#!/usr/bin/node

const request = require('request');

/**
 * Compute the number of tasks completed by user ID.
 *
 * @param {string} apiUrl - The API URL to request.
 */
function getCompletedTasksPerUser (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const tasks = JSON.parse(body);
      const completedTasks = {};

      // Filter the tasks to include only the completed ones.
      const completedTasksList = tasks.filter(task => task.completed);

      // Count the completed tasks per user ID.
      completedTasksList.forEach(task => {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      });

      console.log(completedTasks);
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  });
}

// Get the API URL from the command-line argument.
const apiUrl = process.argv[2];

// Call the function to compute the number of tasks completed by user ID.
getCompletedTasksPerUser(apiUrl);
