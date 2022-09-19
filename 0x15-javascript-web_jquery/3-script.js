// Script que le agregue la clase red to the <header> al click sobre DIV#red_header
$(document).ready(function () {
    $('#red_header').click(function () {
      $('header').addClass('red');
    });
  });