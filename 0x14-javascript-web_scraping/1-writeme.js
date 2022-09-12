#!/usr/bin/node
/* Crear script que escriba una cadena dentro del archivo */
const fs = require('fs');

const archivo = process.argv[2];
const contenido = process.argv[3];

fs.writeFile(archivo, contenido, err => {
  if (err) {
    console.error(err);
  }
});
