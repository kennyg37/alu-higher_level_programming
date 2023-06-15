#!/usr/bin/node
const input = process.argv[2];
const fs = require('fs');
fs.writeFile(input, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(input);
  }
});
