// Use JQuery ready() method to ensure the DOM is ready before executing the script.
$(document).ready(function () {
  // Function to fetch and display the translation of "Hello"
  function fetchAndDisplayTranslation() {
    // Get the language code entered by the user from the input field
    const languageCode = $('#language_code').val();

    // Check if the language code is not empty
    if (languageCode !== '') {
      // Fetch the translation from the API using the entered language code
      $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
        // Get the translation of "Hello" from the fetched JSON data
        const translation = data.hello;

        // Use JQuery selector to target the <div> element with ID "hello" and update its content with the translation
        $('#hello').text(translation);
      }).fail(function () {
        // Display an error message if the language code is not found or if there's an error with the API request
        $('#hello').text('Error: Language code not found');
      });
    }
  }

  // Event handler for when the user clicks on the "Translate" button
  $('#btn_translate').click(function () {
    fetchAndDisplayTranslation();
  });

  // Event handler for when the user presses Enter while focus is on the "Language code" input field
  $('#language_code').keypress(function (event) {
    // Check if the Enter key is pressed (keyCode 13)
    if (event.which === 13) {
      fetchAndDisplayTranslation();
    }
  });
});
