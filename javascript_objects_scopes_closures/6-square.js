#!/usr/bin/node
const Square2 = require('5-square');
const Square = class Square extends Square2 {
  charPrint (c) {
    if (c) {
      let outputs = '';
      for (let count = 0; count < this.height; count++) {
        for (let count = 0; count < this.width; count++) {
          outputs = outputs + c;
        }
        console.log(outputs);
        outputs = '';
      }
    } else {
      super.print();
    }
  }
};
module.exports = Square;
