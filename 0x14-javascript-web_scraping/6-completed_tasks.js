#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const contents = JSON.parse(body);
    const container = {};
    contents.forEach(content => {
      if (content.completed) {
        if (!container[content.userId]) {
          container[content.userId] = 1;
        } else {
          container[content.userId] += 1;
        }
      }
    });
    console.log(container);
  }
});
