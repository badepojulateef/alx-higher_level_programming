#!/usr/bin/node

const request = require('request');

/**
 * Display the status code of a GET request to the given URL.
 *
 * @param {string} url - The URL to request (GET).
 */
function getRequestStatusCode (url) {
  request(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

// Get the URL from the command-line argument.
const url = process.argv[2];

// Call the function to display the status code of the GET request.
getRequestStatusCode(url);
