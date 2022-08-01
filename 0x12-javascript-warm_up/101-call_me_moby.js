#!/usr/bin/node
/* Write a function that executes x times a function */
exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (let i = 0; i < 3; i++) {
    theFunction();
  }
};
