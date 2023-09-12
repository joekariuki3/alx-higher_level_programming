#!/usr/bin/node
// rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // prints the Rectangle using X
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

  // exchange the value of width and height
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // multiply width by 2 and also height by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

// Export the class to be used ouside the file
module.exports = Rectangle;
