//Script that toggles the class of the <header> al click sobre DIV#toggle_header
$(document).ready(function () {
    $('#toggle_header').click(function () {
      $('header').toggleClass('red green');
    });
  });