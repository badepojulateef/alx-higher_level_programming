// Use JQuery ready() to ensure the DOM is ready before excuting the script
$(document).ready(function () {
  // Use JQuery click() method to handle the click event on the element with "red_header"
  $('DIV#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
