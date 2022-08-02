#!/usr/bin/node
/* imprimir el numero de argumentos ya impresos */
const logList = [];

exports.logMe = function (item) {
  logList.push(item);
  console.log(`${logList.length - 1}: ${item}`);
};
