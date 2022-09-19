// Script para listar todas las peliculas obtenidas de la siguiente URL
// https://swapi-api.hbtn.io/api/films/?format=json (json con data)
$(document).ready(function () {
	// url del ejercicio
	const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
	// obtenemos la data de la url con el método get
	$.get(url, function (data) {
	  const movies = data.results;
	//   iteramos las peliculas obtenidas
	for (const peli of movies) {
		const title_element = $('<li></li>').text(peli.title);
		$('#list_movies').append(title_element);
	}
	});
  });
