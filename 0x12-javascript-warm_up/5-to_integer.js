#!/usr/bin/node
arg = process.argv[2];

if (isNaN(arg))
	console.log("Not a number");
else
	console.log(parseInt(arg));
