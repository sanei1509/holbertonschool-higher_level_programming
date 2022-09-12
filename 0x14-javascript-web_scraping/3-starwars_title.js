#!/usr/bin/node
/* crear un script que imprima el titulo de star wars movie
- del episodio pasado por parametros
- usando axios
- url -> https://swapi-api.hbtn.io/api/films/:id
*/

const axios = require('axios').default;

const id = process.argv[2];

const titleExtract = (id) => {
  axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
    .then((res) => {
      console.log(res.data.title);
    })
    .catch((err) => {
      console.log(err);
    });
};

titleExtract(id);
