#!/usr/bin/node
/* Calcular e imprimir el factorial */
const num = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(num))
	return 1;
  else 
	return num * factorial(x - 1);
}
