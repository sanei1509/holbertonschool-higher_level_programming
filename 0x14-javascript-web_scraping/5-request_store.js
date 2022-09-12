#!/usr/bin/node
/* crear un script que obtenga el contenido de una página web y lo guarde en archivo
- 1er argumento - url solicitada
- 2do argumento - ruta del archivo guardado en la response
- The file must be UTF-8 encoded
- usando axios
*/
const axios = require('axios').default;
const fs = require('fs');

const url = process.argv[2];
const fileStore = process.argv[3];

axios.get(url)
  .then((res) => {
    const contenido = res.data;

    fs.writeFile(fileStore, contenido, err => {
		if (err)
      		console.error(err);
    });
  });
