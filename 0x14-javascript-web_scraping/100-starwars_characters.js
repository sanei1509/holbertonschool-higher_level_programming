#!/usr/bin/node
/* Numero de tareas completadas por id del usuario
- 1er argumento - url solicitada
- solo printear usuarios con tareas completadas
- usando axios
*/
const axios = require('axios').default;

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

axios.get(url)
  .then((res) => {
    const personajes = res.data.characters;

    for (const personaje of personajes) {
      axios.get(personaje).then((content) => {
        console.log(content.data.name);
      });
    }
  });
