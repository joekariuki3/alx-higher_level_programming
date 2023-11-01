// script to fetch and print how to say hello in defferent lang

document.addEventListener('DOMContentLoaded', function () {
  // when enter is pressed when input is active it trigers a click event
  $('input#language_code').keyup(function (event) {
    if (event.which === 13) {
      $('input#btn_translate').click();
    }
  });
  $('input#btn_translate').click(function () {
    // save the lang in a variable
    const lang = $('input#language_code').val();
    // add lan in the url
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    // send a GET request to the api returns data
    $.get(url, function (data, textStatus) {
      // access key hello f=from the data
      $('div#hello').text(data.hello);
    });
  });
});
