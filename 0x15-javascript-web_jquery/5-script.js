// Script que añada un elemento <list> a una lista al click sobre DIV#add_item:
$(document).ready(function () {
    $('#add_item').click(function () {
      $('ul.my_list').append('<li>Item</li>');
    });
  });
  