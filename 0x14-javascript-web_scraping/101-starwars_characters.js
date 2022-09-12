#!/usr/bin/node
/* Imprimir todos los caracteres de una movie especifica
- 1er argumento - id de la pelicula
- printear todos los personajes de esta
*/
const axios = require('axios').default;

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

// DEBEMOS USAR ASYNC
const mostrarPersonajes = async () => {
  try {
    // SOLICITAMOS LA URL ESPECIFICA (PELICULA)
    const movie = await axios.get(url);

    // DE LA PELICULA NECESITAMOS LOS PERSONAJES
    const personajes = movie.data.characters;
    // ITERAMOS TODOS LOS PERSONAJES DE LA PELICULA
    for (const personaje of personajes) {
      const content = await axios.get(personaje);
      // MOSTRAMOS CADA PERSONAJES
      console.log(content.data.name);
    }
  } catch (err) {
    console.log(err);
  }
};

mostrarPersonajes();
