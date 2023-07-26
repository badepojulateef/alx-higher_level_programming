#!/usr/bin/node

const request = require('request');
const fs = require('fs');

/**
 * Get the contents of a webpage and store it in a file.
 *
 * @param {string} url - The URL to request.
 * @param {string} filePath - The file path to store the body response.
 */
function getRequestAndStoreToFile (url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      try {
        // const jsonData = JSON.parse(body);
        fs.writeFile(filePath, body, 'utf-8', (err) => {
          if (err) {
            console.error(err);
          } else {
            console.log(`${filePath} created successfully.`);
          }
        });
      } catch (err) {
        console.error('Error: Response is not valid JSON.');
      }
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  });
}

// Get the URL and file path from the command-line arguments.
const url = process.argv[2];
const filePath = process.argv[3];

// Call the function to get the contents of the webpage and store them in the file.
getRequestAndStoreToFile(url, filePath);
