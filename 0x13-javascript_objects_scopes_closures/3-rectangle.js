#!/usr/bin/node
// A class Rectangle that defines a rectangle:

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i += 1) {
      let row = '';
      for (let j = 0; j < this.width; j += 1) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
