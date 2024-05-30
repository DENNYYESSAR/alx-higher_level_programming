/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      console.log(data);
      $('#hello').text(data.hello);
    })
      .fail(function () {
        $('#hello').text('Translation not found');
      });
  });
});
