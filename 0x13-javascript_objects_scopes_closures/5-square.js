#!/usr/bin/node
// Get the apropriate Rectangle class
const Rectangle = require('./4-rectangle.js');

// Square class extends Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
// export the Square class
module.exports = Square;
