#!/usr/bin/node

const request = require('request');

/**
 * Print the title of a Star Wars movie where the episode number matches the given integer.
 *
 * @param {number} movieId - The movie ID (episode number) to search for.
 */
function getMovieTitleById (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  });
}

// Get the movie ID from the command-line argument and convert it to a number.
const movieId = parseInt(process.argv[2]);

// Call the function to print the title of the Star Wars movie with the given ID.
getMovieTitleById(movieId);
