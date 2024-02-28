//Queries an API for wind speed in SF and replaces the text of the
$(document).ready(function () {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
      $("#hello").text(data.hello);
    });
  });
