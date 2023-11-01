// script to toggle class of <header> when user clicks on div with id toggle_leader

$('div#toggle_header').click(function () {
  $('header').toggleClass('green red');
});
