#!/usr/bin/node
// rectangle

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let out_ = '';
    for (let cont1 = 0; cont1 < this.height; cont1++) {
      for (let cont = 0; cont < this.width; cont++) {
        out_ = out_ + 'X';
      }
      console.log(out_);
      out_ = '';
    }
  }
};

module.exports = Rectangle;
