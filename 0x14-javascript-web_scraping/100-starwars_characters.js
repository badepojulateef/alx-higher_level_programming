#!/usr/bin/node

const request = require('request');

/**
 * Print all characters of a Star Wars movie.
 *
 * @param {string} movieId - The movie ID to fetch characters from.
 */
function printStarWarsCharacters (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const charactersUrls = movie.characters;

      // Fetch character names from the characters URLs.
      charactersUrls.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
          } else if (response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          } else {
            console.error(`Error: Status code ${response.statusCode}`);
          }
        });
      });
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  });
}

// Get the movie ID from the command-line argument.
const movieId = process.argv[2];

// Call the function to print all characters of the specified Star Wars movie.
printStarWarsCharacters(movieId);
