#!/usr/bin/node
const input = process.argv[2];
const newString = process.argv[3];
const fs = require('fs');
fs.writeFile(input, 'utf8', (error, newString) => {
  if (error) {
    console.log(error);
  } else {
    console.log(newString);
  }
});
