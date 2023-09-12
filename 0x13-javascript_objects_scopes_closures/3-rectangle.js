#!/usr/bin/node
// rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectPrint = '';
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        rectPrint = rectPrint + 'X';
      }
      if (row < this.height - 1) {
        rectPrint = rectPrint + '\n';
      }
    }
    console.log(rectPrint);
  }
}

// Export the class to be used ouside the file
module.exports = Rectangle;
