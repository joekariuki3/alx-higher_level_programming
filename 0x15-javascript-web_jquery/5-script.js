// script to add <li> to <u> when div with id add_item is clicked

$('div#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
