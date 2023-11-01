// script that fetched data from an url and display the value of hello in div#hello

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
  $('div#hello').text(data.hello);
});
