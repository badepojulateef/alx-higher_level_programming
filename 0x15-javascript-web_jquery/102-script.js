// 102-script.js

// Use JQuery ready() method to ensure the DOM is ready before executing the script.
$(document).ready(function () {
  // Event handler for when the user clicks on the "Translate" button
  $('#btn_translate').click(function () {
    // Get the language code entered by the user from the input field
    const languageCode = $('#language_code').val();

    // Check if the language code is not empty
    if (languageCode !== '') {
      // Fetch the translation from the API using the entered language code
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
        // Get the translation of "Hello" from the fetched JSON data
        const translation = data.hello;

        // Use JQuery selector to target the <div> element with ID "hello" and update its content with the translation
        $('#hello').text(translation);
      }).fail(function () {
        // Display an error message if the language code is not found or if there's an error with the API request
        $('#hello').text('Error: Language code not found');
      });
    }
  });
});
