// Obtener de la data obtenida:
// el valor de hello
$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (data) {
		 $('div#hello').text(data.hello);
  });
});
