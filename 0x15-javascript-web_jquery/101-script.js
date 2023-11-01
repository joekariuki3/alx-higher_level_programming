// script that adds, remove and clear li elements from a list when user clicks DIV#add_item, DIV#remove_item, DIV#clear_list

document.addEventListener('DOMContentLoaded', function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });

  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
