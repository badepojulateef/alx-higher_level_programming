#!/usr/bin/node

const request = require('request');

/**
 * Print the number of movies where the character "Wedge Antilles" (character ID 18) is present.
 *
 * @param {string} apiUrl - The API URL of the Star Wars API films endpoint.
 */
function countMoviesWithWedgeAntilles (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const wedgeAntillesMovies = movieData.results.filter(movie =>
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(wedgeAntillesMovies.length);
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  });
}

// Get the API URL from the command-line argument.
const apiUrl = process.argv[2];

// Call the function to count the number of movies where "Wedge Antilles" is present.
countMoviesWithWedgeAntilles(apiUrl);
