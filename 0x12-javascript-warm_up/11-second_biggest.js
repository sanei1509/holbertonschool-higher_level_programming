#!/usr/bin/node

/* obtener el segundo valor más grande */
const argv = process.argv;
let ordArr = [];

if (argv.length <= 3) { console.log(0); } else {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (isNaN(num)) { continue; } else { ordArr.push(num); }
  }
}

if (ordArr.length > 1) {
  ordArr = ordArr.sort();
  console.log(ordArr[ordArr.length - 2]);
}
