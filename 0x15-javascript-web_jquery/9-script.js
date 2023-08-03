// Use JQuery ready() to ensure the DOM is ready before excuting the script
$(document).ready(function () {
  // Fetch data from the specified URL using JQuery's $.getJSON() method
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    // Get the translation of "hello" from the fetched data.
    const translation = data.hello;
	console.log('data', data)
    // Use JQuery selector to target the <div> element with ID "hello"
    // and update its content with the translation.
    $('DIV#hello').text(translation);
  });
});
