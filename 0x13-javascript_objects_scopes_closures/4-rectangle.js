#!/usr/bin/node
/* crear 2 metódos rotate(), double() */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    /* imprimir el rectangulo */
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  rotate () {
    /* intercambiar valores de ancho y largo */
    const auxWidth = this.width;
    this.width = this.height;
    this.height = auxWidth;
  }

  double () {
    /* duplicar valores de ancho y largo */
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
