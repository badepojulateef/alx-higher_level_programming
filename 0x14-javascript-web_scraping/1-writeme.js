#!/usr/bin/node

const fs = require('fs');

/**
 * Write a string to a file in utf-8 encoding.
 *
 * @param {string} filePath - The file path to write.
 * @param {string} content - The content to write to the file.
 */
function writeFileContent (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      // If an error occurred during writing, print the error object.
      console.error(err);
    } else {
      // If the content is written successfully, log a success message.
      console.log('File written successfully!');
    }
  });
}

// Get the file path and content from the command-line arguments.
const filePath = process.argv[2];
const content = process.argv[3];

// Call the function to write the content to the file.
writeFileContent(filePath, content);
