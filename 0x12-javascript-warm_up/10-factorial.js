#!/usr/bin/node
/* Calcular e imprimir el factorial */
const num = parseInt(process.argv[2]);

function factorial (num) {
  if (num <= 1 || isNaN(num)) { return 1; } else { return num * factorial(num - 1); }
}

console.log(factorial(num));
