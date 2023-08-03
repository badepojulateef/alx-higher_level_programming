// Use JQuery ready() to ensure the DOM is ready before excuting the script
$(document).ready(function () {
  // Fetch data from the specified URL using JQuery's $.getJSON() method
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character name from the fetched data.
    const characterName = data.name;
    // Use JQuery selector to target the <div> element with ID "character"
    // and update its content with the character name.
    $('DIV#character').text(characterName);
  });
});
