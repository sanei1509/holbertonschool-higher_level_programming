#!/usr/bin/node
/* script que importe una lista y calcule una nueva */
const list = require('./100-data').list;

const listMod = list.map((x, index) => x * index);

console.log(list);
console.log(listMod);
