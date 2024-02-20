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
        if (!container[content.userID]) {
          container[content.userID] = 1;
        } else {
          container[content.userID] += 1;
        }
      }
    });
    console.log(container);
  }
});
