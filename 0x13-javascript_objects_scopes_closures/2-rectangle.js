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
}

module.exports = Rectangle;
