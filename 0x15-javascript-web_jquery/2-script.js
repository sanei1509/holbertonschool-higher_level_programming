// Capturando el evento click actualizar el color del header clickeado
$(document).ready(function () {
    $('#red_header').click(function () {
      $('header').css('color', '#FF0000');
    });
  });