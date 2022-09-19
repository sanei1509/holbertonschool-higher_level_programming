// Recuperar el dato pedido en el ejericio de la siguiente api
// https://swapi-api.hbtn.io/api/people/5/?format=json
// data -> name
// const $ = window.$; -> posible solución al semi standard

$(document).ready(function () {
	// url del ejercicio
	const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
	// obtenemos la data de la url con el método get
	$.get(url, function (data, status) {
	  $('#character').text(data.name);
	  console.log(status);
	});
  });
  