#!/usr/bin/node
/* convertir numero de base 10 a otra base pasada por argumento */

exports.converter = function (base) {
  return (number) => number.toString(base);
};
