// Use JQuery ready() to ensure the DOM is ready before excuting the script
$(document).ready(function () {
  // Use JQuery click() method to handle the click event
  // on the element with "red_header"
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
