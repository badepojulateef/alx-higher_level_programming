// Use JQuery ready() to ensure the DOM is ready before excuting the script
$(document).ready(function () {
  // Fetch data from the specified URL using JQuery's $.getJSON() method
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Get the movie titles from the fetched data
    const movieTitles = data.results;
	  
    // Use JQuery selector to target the <div> element with ID "character"
    // and update its content with the character name.
    const listElement = $('UL#list_movies');
    
    // Loop through the movie titles and append each title as a list item to the <ul> element.
    movieTitles.forEach(function (movie) {
      listElement.append('<li>' + movie.title + '</li>');
    })
  });
});
