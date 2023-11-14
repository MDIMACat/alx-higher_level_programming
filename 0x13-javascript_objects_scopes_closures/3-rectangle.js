#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || w < 1 || h === undefined || h < 1) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print() {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
