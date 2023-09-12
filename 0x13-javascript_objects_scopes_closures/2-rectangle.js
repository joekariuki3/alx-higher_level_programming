#!/usr/bin/node
// rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

// Export the class to be used ouside the file
module.exports = Rectangle;
