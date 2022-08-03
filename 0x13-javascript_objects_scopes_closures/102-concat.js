#!/usr/bin/node
/* concatenar el contenido de dos archivos diferentes */
/* cargado y dirigido desde los argumentos */
const fs = require('fs');
const args = process.argv;

const srcFirst = args[2];
const srcSecond = args[3];
const srcThird = args[4];

fs.readFile(srcFirst, (err, data) => {
  if (err) throw err;
  fs.writeFile(srcThird, data.toString() + '\n', (err) => { if (err) throw err; });
});

fs.readFile(srcSecond, (err, data) => {
  if (err) throw err;
  fs.appendFile(srcThird, data.toString() + '\n', (err) => { if (err) throw err; });
});
