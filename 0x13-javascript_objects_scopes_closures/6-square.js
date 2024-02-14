#!/usr/bin/node
// square

const Square_ = require('./5-square');

const Square = class Square extends Square_ {
  charPrint (c) {
    if (c) {
      let out_ = '';
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.height; i++) {
          out_ = out_ + c;
        }
        console.log(out_);
        out_ = '';
      }
    } else {
      super.print();
    }
  }
};

module.exports = Square;
