#!/usr/bin/node
arg = process.argv[2];

if (isNaN(Number(arg)))
	console.log("Not a number");
else
	console.log(Number(arg));
