#!/usr/bin/node

/* obtener el segundo valor más grande */
const argv = process.argv;
const ordArr = [];

if (argv.length <= 3) { console.log(0); } else {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (isNaN(num)) { continue; }
    ordArr.push(num);
  }
}

if (ordArr.length > 3) {
  ordArr.sort();
  console.log(ordArr[ordArr.length - 2]);
}
