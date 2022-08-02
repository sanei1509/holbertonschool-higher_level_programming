#!/usr/bin/node
/* crear una clase Square que herede de Rectangle */
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
