#!/usr/bin/node

const fs = require('fs');

/**
 * Read and print the content of a file in utf-8 encoding.
 *
 * @param {string} filePath - The file path to read.
 */
function readFileContent (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      // If an error occurred during reading, print the error object.
      console.error(err);
    } else {
      // If the file is read successfully, print the content of the file.
      console.log(data);
    }
  });
}

// Get the file path from the first argument passed when running the script.
const filePath = process.argv[2];

// Call the function to read and print the content of the file.
readFileContent(filePath);
