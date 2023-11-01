// script to get list of titles for all movies from url n display in ul#list_movies

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  $.each(data.results, function (index, movie) {
    $('ul#list_movies').append($('<li></li>').text(movie.title));
  });
});
