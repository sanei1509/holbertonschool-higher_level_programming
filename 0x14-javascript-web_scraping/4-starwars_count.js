#!/usr/bin/node
/* crear un script que imprima la cantidad de peliculas con el actor 18
- de todas las peliculas
- usando axios
- url -> https://swapi-api.hbtn.io/api/films/:id
*/
const axios = require('axios').default;

const url = process.argv[2];

axios.get(url)
  .then((res) => {
    const peliculas = res.data.results;
    let apariciones = 0;

    //   ITERO SOBRE MIS PELICULAS
    for (const arr of peliculas) {
      const personajesArr = arr.characters;
      //   ITERO SOBRE EL ARRAY DE PERSONAJES de la pelicula
      for (const personaje of personajesArr) {
        if (personaje.includes('18')) { apariciones++; }
      }
    }
    console.log(apariciones);
  })
  .catch((err) => {
    console.log(err);
  });
