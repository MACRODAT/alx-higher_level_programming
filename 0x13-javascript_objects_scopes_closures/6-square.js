#!/usr/bin/node
// square

const Square_ = require('./5-square');

const Square = class Square extends Square_ {
  charPrint (c) {
    if (c) {
      let prints = '';
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.height; i++) {
          prints = prints + c;
        }
        console.log(prints);
        prints = '';
      }
    } else {
      super.print();
    }
  }
};

module.exports = Square;
