// script that adds a class red to <header> when a user clicks on Div with id red_header

$('div#red_header').click(function () {
  $('header').addClass('red');
});
