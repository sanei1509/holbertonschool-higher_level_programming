#!/usr/bin/node
/* escribir en cosnole x veces  "C is fun" */
const msg = 'C is fun';
const x = process.argv[2];

for (let i = 0; i < x; i++) { console.log(msg); }
