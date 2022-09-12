#!/usr/bin/node
/* leer e imprimir el contenido de un archivo
  - el primer argumento es la ruta del archivo */
const fs = require('fs');

const argv = process.argv[2];

fs.readFile(argv, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
