#!/usr/bin/node
const fs = require('fs');
let filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, inputData) => {
    if (err) throw err;
    console.log (inputData.toString());
});
