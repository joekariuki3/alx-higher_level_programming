#!/usr/bin/node
// get Square to inherit from
const SquareParent = require('./5-square.js');

// square class that inherits from square
class Square extends SquareParent {
  charPrint (c) {
    let sqp = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let row = 0; row < this.width; row++) {
      for (let col = 0; col < this.height; col++) {
        sqp = sqp + c;
      }
      if (row < this.height - 1) {
        sqp = sqp + '\n';
      }
    }
    console.log(sqp);
  }
}

module.exports = Square;
