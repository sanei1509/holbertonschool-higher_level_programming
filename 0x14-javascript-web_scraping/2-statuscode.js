#!/usr/bin/node
/* Crear un script que muestre el status code of a GET request */
const axios = require('axios').default;

const url = process.argv[2];

axios.get(url)
  .then((response) => { console.log(response.status); })
  .catch((err) => {
    console.log(err.response.status);
  });
