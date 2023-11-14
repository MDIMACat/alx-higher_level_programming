#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Reectangle {
    constructor (size) {
        super(size, size)
    }
};
