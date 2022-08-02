#!/usr/bin/node
/* Devolver el numero de ocurrencias en una lista dada */
exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  list.forEach(el => {
    if (el === searchElement) { cont++; }
  });
  return cont;
};
