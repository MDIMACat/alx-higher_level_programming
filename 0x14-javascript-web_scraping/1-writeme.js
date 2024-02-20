#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const inputData = process.argv[3];

fs.writeFile(filePath, inputData, 'utf-8', (err, data) => {
  if (err) throw err;
});
