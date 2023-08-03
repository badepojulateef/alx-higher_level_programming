// Use JQuery ready() method to ensure the DOM is ready before executing the script.
$(document).ready(function () {
  
  // Event handler for adding a new element to the list
  $('#add_item').click(function () {
    // Create a new <li> element with the text "Item"
    const newItem = $('<li>Item</li>');

    // Append the new element to the <ul> element with class "my_list"
    $('UL.my_list').append(newItem);
  });

  // Event handler for removing the last element from the list
  $('#remove_item').click(function () {
    // Select the last <li> element and remove it
    $('UL.my_list LI:last-child').remove();
  });

  // Event handler for clearing all elements from the list
  $('#clear_list').click(function () {
    // Remove all <li> elements inside the <ul> element with class "my_list"
    $('UL.my_list').empty();
  });
});
