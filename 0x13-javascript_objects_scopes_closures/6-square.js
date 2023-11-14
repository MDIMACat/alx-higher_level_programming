#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint(c) {
    let i = 0;

    for (i = 0; i < this.height; i++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
    }
  }
};
