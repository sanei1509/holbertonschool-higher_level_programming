// Script que actualice/cambie el texto de un elemento a "New Header!!!" al click sobre DIV#update_header
$(document).ready(function () {
    $('#update_header').click(function () {
      $('header').text('New Header!!!');
    });
  });