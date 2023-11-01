// script to fetch a charactor name rrom url n display in DIV#character

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, textStatus) {
  $('div#character').text(data.name);
});
