#!/usr/bin/node
const size = parseInt(process.argv[2]);
let counter = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (counter = 0; counter < size; counter++) {
  console.log('X'.repeat(size));
  }
}
